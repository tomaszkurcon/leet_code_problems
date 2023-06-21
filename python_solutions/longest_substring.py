def lengthOfLongestSubstring(s):
    n = len(s)
    answer = 0
    dict = {}
    start = 0
    for i in range(n):
        if s[i] not in dict:
            answer = max(answer, i - start + 1)
        else:
            if dict[s[i]] < start:
                answer = max(answer, i - start + 1)
            else:
                start = dict[s[i]] + 1
        dict[s[i]] = i
    return answer
