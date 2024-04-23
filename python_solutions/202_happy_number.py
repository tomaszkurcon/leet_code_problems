def isHappy(n: int) -> bool:
    m_dict = {}
    candidate = n
    _sum = 0
    while (m_dict.get(candidate, 0) < 2):
        _sum = 0
        while candidate > 0:
            digit = candidate % 10
            _sum += digit * digit
            candidate //= 10

        m_dict[_sum] = m_dict.get(_sum, 0)+1
        candidate = _sum

        if _sum == 1:
            return True
    return False

print(isHappy(19))
