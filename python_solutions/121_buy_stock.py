from typing import List


def maxProfit(prices: List[int]) -> int:
    n = len(prices)
    left = 0
    right = 1
    result = 0
    while right < n:
        if prices[right] < prices[left]:
            left = right
        else:
            result = max(result, prices[right] - prices[left])

        right += 1
    return result

