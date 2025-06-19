def binary_search_loop(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            return mid
    return -1


def binary_search_recursive(nums, target, left, right):
    if left > right:
        return -1
    mid = (left + right) // 2
    if nums[mid] < target:
        return binary_search_recursive(nums, target, mid + 1, right)
    elif nums[mid] > target:
        return binary_search_recursive(nums, target, left, mid - 1)
    else:
        return mid


def binary_search(nums, target):
    return binary_search_recursive(nums, target, 0, len(nums) - 1)
