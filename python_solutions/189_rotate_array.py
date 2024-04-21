from typing import List


#Solution 1 with extra array
def rotate1(self, nums: List[int], k: int) -> None:
    n = len(nums)
    help_nums = [0] * n
    for i in range(n):
        help_nums[(i + k) % n] = nums[i]
    for i in range(n):
        nums[i] = help_nums[i]

#Solution 2 recursion O(1) space
def rotate2(nums: List[int], k: int) -> None:
    n = len(nums)
    def rec(nums, new, place, counter, generalCounter, n, starting_index):
        if starting_index == place:
            nums[place] = new
            counter+=1
            generalCounter+=1
        if generalCounter == n or starting_index==place:
            return counter
        old = nums[place]
        nums[place] = new
        return rec(nums, old, (place + k) % n, counter + 1, generalCounter+1, n, starting_index)
    generalCounter = 0
    for i in range(n):
        generalCounter+=rec(nums, nums[i], (k+i)%n, 0, generalCounter, n, i)
        if generalCounter == n:
            return

A = [-1,-100,3,99]
rotate2(A, 2)
print(A)