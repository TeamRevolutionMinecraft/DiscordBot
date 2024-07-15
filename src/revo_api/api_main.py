import os
from datetime import datetime

from flask import Flask, request, Response
from flask_restful import Resource, Api

from ipc import message


def main(hub):
    app = Flask(__name__)
    api = Api(app)

    class Base(Resource):

        def post(self):
            req = request.get_json()

            if os.getenv("MASTERKEY") != req["key"]:
                return Response(status=401)

            message.IpcMessage(req["sender"], req["target"],
                               datetime.now(), req["data"]).\
                send_message(hub.get_bus_from_hub("DISCORD"))

            return Response(status=200)

    class GetMessageFromDiscord(Resource):
        def post(self):
            bus = hub.get_bus_from_hub("MINECRAFT")

            if not bus.is_empty():
                msg = bus.get_msg_from_bus(0.1)
                if msg:
                    return msg.data
            else:
                return Response(status=133)

    api.add_resource(Base, '/toDiscord')
    api.add_resource(GetMessageFromDiscord, "/fromDC")

    app.run(debug=False, port=int(os.getenv("API_PORT")))
