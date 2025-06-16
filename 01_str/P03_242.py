class Solution:
    def process(self, text):
        counter = dict()
        for char in text:
            if char not in counter:
                counter[char] = 0
            counter[char] += 1
        return counter

    def compare_dict(self, d1, d2):
        if len(d1) != len(d2):
            return False
        for key in d1.keys():
            if d1[key] != d2.get(key):
                return False
        return True

    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = self.process(s)
        t_dict = self.process(t)
        return self.compare_dict(s_dict, t_dict)
