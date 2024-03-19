from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # longest_prefix = ''
        # if len(strs) == 0: return ''
        # longest_prefix=strs[0]
        # for i in range(1, len(strs)):
        #     p = 0
        #     while p < len(longest_prefix) and p<len(strs[i]) and longest_prefix[p]==strs[i][p]:
        #         p+=1
        #     longest_prefix=strs[i][:p]
        # return longest_prefix
        sorted_strs = sorted(strs)
        p = 0
        longest_prefix = ''
        first = sorted_strs[0]
        last = sorted_strs[-1]
        while (p < min(len(first), len(last))):
            if (first[p] == last[p]):
                longest_prefix += first[p]
                p += 1
            else:
                break
        return longest_prefix









