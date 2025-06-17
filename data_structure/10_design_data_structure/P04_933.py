from typing import *


class RecentCounter:

    def __init__(self):
        self.requests = []
        self.pointer = 0

    def process(self):
        while self.requests[self.pointer] + 3000 < self.requests[-1]:
            self.pointer += 1

    def ping(self, t: int) -> int:
        self.requests.append(t)
        self.process()
        return len(self.requests) - self.pointer
