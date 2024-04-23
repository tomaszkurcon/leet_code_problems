from typing import List


# def productExceptSelf(nums: List[int]) -> List[int]:
#     n = len(nums)
#     prefix_prod = [1 for _ in range(n)]
#     suffix_prod = [1 for _ in range(n)]
#     prefix_prod[0] = nums[0]
#     suffix_prod[n - 1] = nums[n - 1]
#     for i in range(1, n):
#         prefix_prod[i] = prefix_prod[i - 1] * nums[i]
#         suffix_prod[n - i - 1] = suffix_prod[n - i] * nums[n - i - 1]
#     nums[0] = suffix_prod[1]
#     nums[n - 1] = prefix_prod[n - 2]
#     for i in range(1, n - 1):
#         nums[i] = prefix_prod[i - 1] * suffix_prod[i + 1]
#     return nums

# def productExceptSelf(nums: List[int]) -> List[int]:
#     n = len(nums)
#     prefix_prod = [1 for _ in range(n)]
#     suffix_prod = [1 for _ in range(n)]
#     for i in range(1, n):
#         prefix_prod[i] = prefix_prod[i - 1] * nums[i-1]
#         suffix_prod[n - i - 1] = suffix_prod[n - i] * nums[n - i]
#
#     for i in range(n):
#         nums[i] = prefix_prod[i] * suffix_prod[i]
#     return nums

def productExceptSelf(nums: List[int]) -> List[int]:
    n = len(nums)
    ans = [1 for _ in range(n)]
    curr = 1
    for i in range(n):
        ans[i]*=curr
        curr*=nums[i]
    curr=1
    for i in range(n-1, -1, -1):
        ans[i]*=curr
        curr*=nums[i]
    return ans

print(productExceptSelf([1,2,3,4]))