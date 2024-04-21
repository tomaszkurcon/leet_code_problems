from typing import List


# def majorityElement(nums: List[int]) -> int:
#     n = len(nums)
#     m_dict = {}
#     for el in nums:
#         m_dict[el] = m_dict.get(el, 0) + 1
#     for key in m_dict.keys():
#         if m_dict.get(key) > n // 2:
#             return key
#     return 0
#
# print(majorityElement([3,2,3]))

#Moore Voting Algorithm
def majorityElement(nums: List[int]) -> int:
    n = len(nums)
    if n == 0:
        return 0
    candidate = nums[0]
    count = 0

    for el in nums:
        if count == 0:
            candidate = el
            count+=1
        elif el == candidate:
            count += 1
        else:
            count -= 1
    return candidate

print(majorityElement([3,3,4]))