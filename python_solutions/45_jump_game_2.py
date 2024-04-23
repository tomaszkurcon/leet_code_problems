from typing import List


def jump(nums: List[int]) -> int:
    n = len(nums)
    if n == 1:
        return 0
    i = 1
    result = 1
    maximum = 1
    gas = nums[0]
    while i < n - 1:
        gas -= 1
        if nums[maximum] - (i - maximum) <= nums[i]:
            maximum = i
        if gas == 0:
            result += 1
            gas = nums[maximum] - (i - maximum)
            maximum = i + 1
        i += 1

    return result


print(jump([7,0,9,6,9,6,1,7,9,0,1,2,9,0,3]))