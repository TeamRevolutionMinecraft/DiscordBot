from datetime import datetime


class IpcMessage:
    def __init__(self, sender_id: 0, target_id: 0,
                 keep_alive: int,
                 data: dict = None) -> None:
        self.sender_id = sender_id
        self.target_id = target_id
        self.data = data
        self.creation_time = datetime.now()
        self.keep_alive = keep_alive

    def __repr__(self) -> str:
        return f"{self.sender_id} is sending {self.data} to {self.target_id}"

    def send_message(self, bus):
        bus.put_msg_on_bus(self)


TEST_MESSAGE = IpcMessage(
    sender_id=99,
    target_id=99,
    keep_alive=99,
    data={
        "sender": "test1",
        "msg": "test1"
    })
