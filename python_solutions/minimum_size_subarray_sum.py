def minSubArrayLen_prefixes_sum(target: int, nums) -> int:
    n = len(nums)
    prefix_sum = [0 for _ in range(n + 1)]
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]
    start = 0
    end = 0
    result = 0
    while end < n:
        if prefix_sum[end + 1] - prefix_sum[start] >= target:
            if result > end + 1 - start or result == 0:
                result = end + 1 - start
            start += 1
        else:
            end += 1
    return result

def minSubArrayLen(target: int, nums) -> int:
    n = len(nums)
    start = 0
    end = 0
    result = 0
    m_sum = nums[0]
    while end < n:
        if m_sum >= target:
            if result > end + 1 - start or result == 0:
                result = end + 1 - start
            m_sum -= nums[start]
            start += 1
        else:
            end += 1
            if end < n:
                m_sum += nums[end]
    return result

print(minSubArrayLen(7, [2,3,1,2,4,3]))