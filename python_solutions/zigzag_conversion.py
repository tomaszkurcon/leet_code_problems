class Solution:
    def convert(self, s: str, numRows: int) -> str:
        result = ''
        rows = [''] * numRows
        sign = 1
        w = 0
        if numRows == 1:
            return s
        for i in range(len(s)):
            rows[w] += s[i]
            w += 1 * sign
            if w == numRows - 1 or w == 0:
                sign *= -1
        for row in rows:
            result += row
        return result
