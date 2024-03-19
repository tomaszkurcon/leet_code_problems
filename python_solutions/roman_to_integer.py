#sol1
class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        roman_dict = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1, "IV": 4, "IX": 9, "XL": 40,
                      "XC": 90, "CD": 400, "CM": 900}
        i = 0
        while i < len(s):
            if i < len(s) - 1 and (s[i] + s[i + 1]) in roman_dict:
                result += roman_dict[s[i] + s[i + 1]]
                i += 1
            else:
                result += roman_dict[s[i]]
            i += 1
        return result

##sol2
# class Solution:
#     def romanToInt(self, s: str) -> int:
#         result = 0
#         roman_dict = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
#         i = 0
#         while i < len(s):
#             if i < len(s) - 1 and roman_dict[s[i]] < roman_dict[s[i + 1]]:
#                 result += roman_dict[s[i + 1]] - roman_dict[s[i]]
#                 i += 1
#             else:
#                 result += roman_dict[s[i]]
#             i += 1
#         return result



