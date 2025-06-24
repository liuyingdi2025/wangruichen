from typing import *


class Solution:
    def threeSum(self, numbers):
        numbers.sort()
        # 数据预处理
        min_threshold = 0 - numbers[-1] - numbers[-2]  # 必须大于或等于当前阈值
        max_threshold = 0 - numbers[0] - numbers[1]  # 必须小于或等于当前阈值
        min_idx, max_idx = 0, len(numbers) - 1
        for min_idx in range(len(numbers)):
            if numbers[min_idx] >= min_threshold:
                break
        for max_idx in range(len(numbers) - 1, -1, -1):
            if numbers[max_idx] <= max_threshold:
                break
        numbers = numbers[min_idx:max_idx + 1]
        # 列表遍历
        # print(numbers)
        ans = []
        for first_idx in range(len(numbers)):
            if first_idx > 0 and numbers[first_idx - 1] == numbers[first_idx]:
                continue
            target = 0 - numbers[first_idx]
            second_idx = first_idx + 1
            third_idx = len(numbers) - 1
            while second_idx < third_idx:
                if numbers[second_idx] + numbers[third_idx] < target:
                    second_idx += 1
                elif numbers[second_idx] + numbers[third_idx] > target:
                    third_idx -= 1
                else:  # numbers[second_idx] + numbers[third_idx] == target
                    ans.append([numbers[first_idx], numbers[second_idx], numbers[third_idx]])
                    second_idx += 1
                    while second_idx < third_idx and numbers[second_idx - 1] == numbers[second_idx]:
                        second_idx += 1
                    third_idx -= 1
                    while second_idx < third_idx and numbers[third_idx] == numbers[third_idx + 1]:
                        third_idx -= 1
        return ans


print(Solution().threeSum(
    numbers=[2, -3, 0, -2, -5, -5, -4, 1, 2, -2, 2, 0, 2, -4, 5, 5, -10]
))
