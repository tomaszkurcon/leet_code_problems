from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if len(nums) == 0:
            return 0
        currentIndex = 1
        k = 1
        for i in range(1, n):
            if not nums[i] == nums[i - 1]:
                k += 1
                nums[currentIndex] = nums[i]
                currentIndex += 1
        return k


