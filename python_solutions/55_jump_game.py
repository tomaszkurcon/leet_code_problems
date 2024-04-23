from typing import List

#dynamic 2d
# def canJump(nums: List[int]) -> bool:
#     n = len(nums)
#     dynamic_tab = [[False for k in range(n)] for w in range(n)]
#     dynamic_tab[0][0] = True
#     for i in range(1,n):
#         flag = False
#         for j in range(i):
#             if(dynamic_tab[j][j] and nums[j]>=i-j):
#                 dynamic_tab[j][i] = True
#                 flag = True
#         if flag:
#             dynamic_tab[i][i]=True
#     return dynamic_tab[n-1][n-1]
# print(canJump([1,2,3]))

#dynamic
# def canJump(nums: List[int]) -> bool:
#     n = len(nums)
#     dynamic_tab = [False for _ in range(n)]
#     dynamic_tab[0] = True
#     for i in range(1, n):
#         for j in range(0, i):
#             if (dynamic_tab[j] and nums[j] >= i - j):
#                 dynamic_tab[i] = True
#     return dynamic_tab[n - 1]
#
# print(canJump([2,3,1,1,4]))

#recursion
# def canJump(nums: List[int]) -> bool:
#     n = len(nums)
#     def rec(nums, current, n):
#         if current >= n - 1:
#             return True
#         for i in range(1, nums[current] + 1):
#             if rec(nums, current + i, n):
#                 return True
#         return False
#     return rec(nums, 0, n)
#
#
# print(canJump([2,0,0,0]))

#correct solution O(n)
def canJump(nums: List[int]) -> bool:
    n = len(nums)
    x = nums[0]
    for i in range(1,n):
        x-=1
        if x < 0:
            return False
        if nums[i]>x:
            x=nums[i]
    return True


print(canJump([2, 0, 0]))


