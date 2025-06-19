import random
import time


class Timer:
    def __init__(self):
        self.start = int(time.time() * 1000)  # 记录当前时间

    def stop(self):
        self.stop = int(time.time() * 1000)  # 记录结束的时间

    def cost(self):
        return self.stop - self.start


# 随机生成一个 list
def generate(size=10, low=1, high=100):
    return [random.randint(low, high) for _ in range(size)]


# 判断一个 list 是否为升序排列
def is_ascending(nums):
    for idx in range(1, len(nums)):
        if nums[idx - 1] > nums[idx]:
            return False
    return True


# 判断一个 list 是否为降序排列
def is_descending(nums):
    for idx in range(1, len(nums)):
        if nums[idx - 1] < nums[idx]:
            return False
    return True


# 判断两个 list 是否相等
def is_equal(nums1, nums2):
    if len(nums1) != len(nums2):
        return False
    for idx in range(len(nums1)):
        if nums1[idx] != nums2[idx]:
            return False
    return True


def selection_sort(nums):
    for idx in range(len(nums)):
        min_index = idx
        for k in range(idx + 1, len(nums)):
            if nums[k] < nums[min_index]:
                min_index = k
        nums[idx], nums[min_index] = nums[min_index], nums[idx]


def insertion_sort(nums):
    for idx in range(1, len(nums)):
        for k in range(idx, 0, -1):
            if nums[k - 1] <= nums[k]:
                break
            else:  # nums[k - 1] > nums[k]
                nums[k - 1], nums[k] = nums[k], nums[k - 1]


def bubble_sort(nums):
    for index in range(len(nums)):
        for k in range(0, len(nums) - 1):
            if nums[k] > nums[k + 1]:
                nums[k], nums[k + 1] = nums[k + 1], nums[k]


def bubble_sort_plus(nums):
    for index in range(len(nums)):
        flag = True
        for k in range(0, len(nums) - 1 - index):
            if nums[k] > nums[k + 1]:
                nums[k], nums[k + 1] = nums[k + 1], nums[k]
                flag = False
        if flag:
            break


def merge(nums1, nums2):
    nums3 = []
    idx1, idx2 = 0, 0
    while idx1 < len(nums1) and idx2 < len(nums2):
        if nums1[idx1] <= nums2[idx2]:
            nums3.append(nums1[idx1])
            idx1 += 1
        else:  # nums1[idx1] > nums2[idx2]
            nums3.append(nums2[idx2])
            idx2 += 1
    while idx1 < len(nums1):
        nums3.append(nums1[idx1])
        idx1 += 1
    while idx2 < len(nums2):
        nums3.append(nums2[idx2])
        idx2 += 1
    return nums3


def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    nums_left_part = merge_sort(nums[:mid])
    nums_right_part = merge_sort(nums[mid:])
    nums = merge(nums_left_part, nums_right_part)
    return nums


def partition(nums, left, right):
    pivot = left
    while left < right:
        # 从右向左，找到一个比 nums[pivot] 更小的数
        while left <= right and nums[pivot] <= nums[right]:
            right -= 1
        if left <= right:
            nums[pivot], nums[right] = nums[right], nums[pivot]
            pivot = right
        # 从左向右，找到一个比 nums[pivot] 更大的数
        while left <= right and nums[left] < nums[pivot]:
            left += 1
        if left <= right:
            nums[left], nums[pivot] = nums[pivot], nums[left]
            pivot = left
    return pivot


def quick_sort(nums, left, right):
    pivot = partition(nums, left, right)
    if left < pivot:
        quick_sort(nums, left, pivot - 1)
    if pivot < right:
        quick_sort(nums, pivot + 1, right)
