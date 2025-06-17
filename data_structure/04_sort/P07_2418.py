from typing import *


class Item:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def __lt__(self, number):
        return self.height < number.height

    def __le__(self, number):
        return self.height <= number.height

    def __gt__(self, number):
        return self.height > number.height

    def __ge__(self, number):
        return self.height >= number.height

    def __eq__(self, number):
        return self.height == number.height


class Solution:
    def calc_pivot(self, items, left, right):
        # print(left, right)
        pivot = left
        while left <= right:
            while left <= right and items[pivot] <= items[right]:
                right -= 1
            if left <= right:
                items[pivot], items[right] = items[right], items[pivot]
                pivot = right
            while left <= right and items[left] < items[pivot]:
                left += 1
            if left <= right:
                items[left], items[pivot] = items[pivot], items[left]
                pivot = left
        return pivot

    def quick_sort(self, items, left, right):
        # print([_.height for _ in items], [_.name for _ in items])
        pivot = self.calc_pivot(items, left, right)
        # print(pivot)
        if left < pivot:
            self.quick_sort(items, left, pivot - 1)
        if pivot < right:
            self.quick_sort(items, pivot + 1, right)

    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        items = [Item(name, height) for name, height in zip(names, heights)]
        self.quick_sort(items, 0, len(items) - 1)
        return [_.name for _ in items][::-1]


print(Solution().sortPeople(
    names=["Mary", "John", "Emma"], heights=[180, 165, 170]
))
