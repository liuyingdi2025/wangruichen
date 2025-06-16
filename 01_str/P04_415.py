class Solution:
    def padding(self, text, length):
        while len(text) < length:
            text = '0' + text
        return text

    def addStrings(self, num1: str, num2: str) -> str:
        max_length = max(len(num1), len(num2))
        num1 = self.padding(num1, max_length)
        num2 = self.padding(num2, max_length)
        result = ''
        carry = 0
        for index in range(max_length - 1, -1, -1):
            ch1 = num1[index]
            ch2 = num2[index]
            temp = (ord(ch1) - ord('0')) + (ord(ch2) - ord('0')) + carry
            result = str(temp % 10) + result
            carry = temp // 10
        if carry == 1:
            result = '1' + result
        return result
