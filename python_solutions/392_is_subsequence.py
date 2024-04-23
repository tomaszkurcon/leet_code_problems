def isSubsequence(s: str, t: str) -> bool:
    s_pointer = 0
    t_pointer = 0
    n_s = len(s)
    n_t = len(t)
    while s_pointer < n_s and t_pointer < n_t:
        if s[s_pointer] == t[t_pointer]:
            s_pointer += 1
        t_pointer += 1
    return s_pointer == n_s

print(isSubsequence("abc", "ahbgdc"))
