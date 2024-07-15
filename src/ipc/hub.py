import asyncio
import multiprocessing as mp
import time
import logging

from . import message


class Bus:
    def __init__(self, name: str) -> None:
        self.name = name
        self.queue = mp.Queue()

    def get_msg_from_bus(self, timeout: int) -> message.IpcMessage:
        return self.queue.get(timeout=timeout)

    def put_msg_on_bus(self, msg: message.IpcMessage):
        self.queue.put(msg)

    def is_empty(self):
        return self.queue.empty()

class Hub:
    loop = asyncio.get_event_loop()

    def __init__(self) -> None:
        self.bus_dict = {}
        # self.loop.run_until_complete(self._bus_clean_up())

    def add_bus_to_hub(self, bus: Bus) -> None:
        self.bus_dict = self.bus_dict | {bus.name: bus}

    def get_bus_from_hub(self, name: str) -> Bus:
        return self.bus_dict[name]

    # async def _bus_clean_up(self):
    #     await asyncio.sleep(10)
    #
    #     for _ in self.bus_dict:
    #         message = self.bus_dict[_].get(0.2)
    #         if message.creation_time.timestamp() + message.keep_alive < time.time:
    #             self.bus_dict[_].put(message)
