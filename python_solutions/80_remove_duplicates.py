from typing import List
def removeDuplicates(nums: List[int]) -> int:
    n = len(nums)
    if n <= 2:
        return n
    last_index = 1
    for i in range(1, n-1):
        if nums[i+1] == nums[i] and nums[last_index]==nums[last_index-1]:
            continue
        last_index += 1
        nums[last_index] = nums[i+1]
    return last_index + 1

print(removeDuplicates([1,1,1,2,2,3]))