def isAnagram(self, s: str, t: str) -> bool:
    t_dict = {}
    s_dict = {}
    t_len = len(t)
    s_len = len(s)
    if t_len != s_len:
        return False
    for i in range(t_len):
        t_dict[t[i]] = t_dict.get(t[i], 0) + 1
        s_dict[s[i]] = s_dict.get(s[i], 0) + 1
    keys = s_dict.keys()
    for key in keys:
        if s_dict.get(key) != t_dict.get(key):
            return False
    return True