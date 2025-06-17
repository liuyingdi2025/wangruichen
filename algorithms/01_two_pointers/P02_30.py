from typing import *


class Solution:
    def to_dict(self, items: List[str]):
        mydict = dict()
        for item in items:
            if item not in mydict:
                mydict[item] = 0
            mydict[item] += 1
        return mydict

    def findSubstring(self, text: str, words: List[str]) -> List[int]:
        length = len(words[0])
        count = len(words)
        words = self.to_dict(words)
        ans = []
        for left in range(len(text)):
            right = left + length * count - 1
            if right < len(text):
                targets = [text[_:_ + length] for _ in range(left, right + 1, length)]
                # print(targets)
                if self.to_dict(targets) == words:
                    ans.append(left)
        return ans


print(Solution().findSubstring(
    text="wordgoodgoodgoodbestword",
    words=["word", "good", "best", "good"]
))  # 13
