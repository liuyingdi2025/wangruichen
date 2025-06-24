from typing import *


class Solution:
    def threeSumClosest(self, numbers: List[int], number: int) -> int:
        value = sum(numbers[:3])
        numbers.sort()
        min_distance = abs(value - number)
        for first_idx in range(len(numbers)):
            target = number - numbers[first_idx]  # target <- numbers[second] + number[third]
            second_idx = first_idx + 1
            third_idx = len(numbers) - 1
            while second_idx < third_idx:
                if numbers[second_idx] + numbers[third_idx] < target:
                    distance = target - (numbers[second_idx] + numbers[third_idx])
                    if distance < min_distance:
                        min_distance = distance
                        value = numbers[first_idx] + numbers[second_idx] + numbers[third_idx]
                    second_idx += 1
                elif numbers[second_idx] + numbers[third_idx] > target:
                    distance = numbers[second_idx] + numbers[third_idx] - target
                    if distance < min_distance:
                        min_distance = distance
                        value = numbers[first_idx] + numbers[second_idx] + numbers[third_idx]
                    third_idx -= 1
                else:  # numbers[second_idx] + numbers[third_idx] == target
                    return number
        return value


print(Solution().threeSumClosest(
    numbers=[1, 1, 1], number=3
))
