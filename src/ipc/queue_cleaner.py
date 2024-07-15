from datetime import datetime

from .hub import Bus


class Queue_Cleaner:
    def __init__(self, bus: Bus) -> None:
        self.bus = bus

    def worker_job(self):
        for _ in range(self.bus.items_in_bus):
            tmp = self.bus.queue.get()
            if not (tmp.creation_time + tmp.keep_alive <= datetime.now()):
                self.bus.queue.put(tmp)