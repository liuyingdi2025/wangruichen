from typing import List


class Queue:
    def __init__(self):
        self.values = []

    def size(self):
        return len(self.values)

    def is_empty(self):
        return len(self.values) == 0

    def enqueue(self, value):
        self.values.append(value)
        return self

    def enqueue_batch(self, values):
        self.values.extend(values)
        return self

    def dequeue(self):
        value = self.values[0]
        self.values = self.values[1:]
        return value

    def front(self):
        return self.values[0]

    def traverse(self):
        print(' <- '.join([str(_) for _ in self.values]))


class Solution:
    def predictPartyVictory(self, votes: str) -> str:
        timer = 1
        r_queue = Queue()
        d_queue = Queue()
        for vote in votes:
            if vote == 'R':
                r_queue.enqueue(timer)
            else:  # votes[index] == 'D'
                d_queue.enqueue(timer)
            timer += 1
        while not r_queue.is_empty() and not d_queue.is_empty():
            r_value = r_queue.dequeue()
            d_value = d_queue.dequeue()
            if r_value < d_value:
                r_queue.enqueue(timer)
            else:  # d_value < r_value
                d_queue.enqueue(timer)
            timer += 1
        return 'Radiant' if not r_queue.is_empty() else 'Dire'


print(Solution().predictPartyVictory('RDD'))
