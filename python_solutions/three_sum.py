#Dictionary
#time exceeded
# def threeSum(nums):
#     n = len(nums)
#     pairs_dict = {}
#     sol = []
#
#     for i in range(n):
#         for j in range(i,n):
#             if i == j: continue
#
#             if pairs_dict.get(nums[i] + nums[j]) is None:
#                 pairs_dict[nums[i] + nums[j]] = [[i, j, nums[i], nums[j]]]
#             else:
#                 pairs_dict[nums[i] + nums[j]].append([i, j, nums[i], nums[j]])
#
#     set_of_indexes = set()
#     for i in range(len(nums)):
#         if pairs_dict.get(-nums[i]) is not None:
#             arr = pairs_dict[-nums[i]]
#             for triplet in arr:
#                 if i != triplet[0] and i != triplet[1]:
#                     triple_indexes = tuple(sorted((triplet[2], triplet[3], nums[i])))
#                     if triple_indexes not in set_of_indexes:
#                         set_of_indexes.add(triple_indexes)
#                         sol.append([nums[i], triplet[2], triplet[3]])
#     return sol

#Two pointers
#Passed tests
def threeSum(nums):
    n = len(nums)
    sol = []
    nums.sort()
    for i in range(n-2):
        if i-1 >=0 and nums[i]==nums[i-1]:
            continue
        l = i+1
        r = n-1
        while l<r:
            sum = nums[i] + nums[l] + nums[r]
            if sum > 0:
                r-=1
            elif sum < 0:
                l+=1
            else:
                sol.append([nums[i], nums[l], nums[r]])
                lastDigit = nums[r]
                while lastDigit == nums[r] and r>l:
                    r-=1


    return sol






print(threeSum([0,0,0,0]))