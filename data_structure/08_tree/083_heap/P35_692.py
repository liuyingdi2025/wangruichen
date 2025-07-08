from typing import *


class Node:
    def __init__(self, word, value):
        self.word = word
        self.value = value

    def __lt__(self, node):
        if self.value != node.value:
            return self.value < node.value
        return self.word > node.word

    def __le__(self, node):
        if self.value != node.value:
            return self.value < node.value
        return self.word >= node.word

    def __gt__(self, node):
        if self.value != node.value:
            return self.value > node.value
        return self.word < node.word

    def __ge__(self, node):
        if self.value != node.value:
            return self.value > node.value
        return self.word <= node.word

    def __eq__(self, node):
        return self.value == node.value and self.word == node.word

    def __ne__(self, node):
        return self.value != node.value or self.word != node.word


class MaxHeap:
    def __init__(self):
        self.nodes = []

    def get(self, word):
        for index in range(len(self.nodes)):
            if self.nodes[index].word == word:
                return index
        return -1

    def add(self, word):
        index = self.get(word)
        if index == -1:
            self.nodes.append(Node(word, 1))
            index = len(self.nodes) - 1
        else:
            self.nodes[index].value += 1
        # heapify up
        while index > 0:
            parent = (index - 1) // 2
            if self.nodes[parent] >= self.nodes[index]:
                break
            self.nodes[parent], self.nodes[index] = self.nodes[index], self.nodes[parent]
            index = parent

    def pop(self):
        node = self.nodes[0]
        self.nodes[0] = self.nodes[-1]
        self.nodes = self.nodes[:-1]
        # heapify down
        index = 0
        while index < len(self.nodes):
            if index * 2 + 1 >= len(self.nodes):
                break
            maximum = index * 2 + 1
            if index * 2 + 2 < len(self.nodes) and self.nodes[index * 2 + 2] > self.nodes[maximum]:
                maximum = index * 2 + 2
            if self.nodes[index] >= self.nodes[maximum]:
                break
            self.nodes[index], self.nodes[maximum] = self.nodes[maximum], self.nodes[index]
            index = maximum
        return node


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        max_heap = MaxHeap()
        for word in words:
            max_heap.add(word)
            # print([(node.word, node.value) for node in max_heap.nodes])
        ans = []
        for _ in range(k):
            ans.append(max_heap.pop().word)
        return ans

# print(Solution().topKFrequent(
#     words=["i", "love", "leetcode", "i", "love", "coding"],
#     k=2
# ))
