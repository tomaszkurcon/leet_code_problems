from typing import List


def maxProfit(prices: List[int]) -> int:
    stack = []
    profit = 0
    n = len(prices)
    for i in range(n):
        if len(stack) > 0:
            last_el = stack.pop()
            if last_el < prices[i]:
                profit += prices[i] - last_el
            else:
                stack.append(last_el)
        stack.append(prices[i])
    return profit