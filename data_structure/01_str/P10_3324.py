from typing import List


class Solution:
    def process(self, ch, prefix):
        result = []
        for number in range(ord('a'), ord(ch) + 1):
            result.append(prefix + chr(number))
        return result

    def stringSequence(self, target: str) -> List[str]:
        items = ['']
        for ch in target:
            items.extend(self.process(ch, items[-1]))
        return items[1:]
