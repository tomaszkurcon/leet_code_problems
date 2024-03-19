from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # n^2
        n = len(height)
        maxx = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                if (maxx < min(height[i], height[j]) * (j - i)):
                    maxx = min(height[i], height[j]) * (j - i)
        return maxx
        # n = len(height)
        # l_p = 0
        # r_p = n-1
        # maxx = 0
        # while l_p<r_p:
        #     v = (min(height[l_p], height[r_p]))*(r_p-l_p)
        #     if(maxx<v): maxx=v
        #     if(height[l_p]<height[r_p]):
        #         l_p+=1
        #     else:
        #         r_p-=1
        # return maxx
