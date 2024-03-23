def generateParentheses(n):
    if n == 0:
        return []
    result = []
    s = "("*n

    def rec(combination, index, left_more,n):
        if n == 0:
            result.append(combination)
            return
        if index >= len(combination):
            for _ in range(n):
                combination+=")"
            result.append(combination)
            return
        if left_more > 0:
            rec(combination[:index]+")"+combination[index:], index+1, left_more-1, n-1)
        rec(combination, index+1, left_more + 1, n)

    rec(s,1, 1, n)
    return result

print(generateParentheses(4))