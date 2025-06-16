class Solution:

    def color(self, coordinate):
        c = ord(coordinate[0]) - ord('a') + 1
        r = int(coordinate[1])
        if (c + r) % 2 == 0:
            return 'black'
        else:
            return 'white'

    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        return self.color(coordinate1) == self.color(coordinate2)
