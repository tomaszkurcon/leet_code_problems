from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        m_dict = {}
        res = []
        length = 0
        for str_ in strs:
            sorted_str = ''.join(sorted(str_))
            index = m_dict.get(sorted_str)
            if index is None:
                length+=1
                res.append([str_])
                m_dict[sorted_str] = length - 1
            else:
                res[index].append(str_)
        return res
