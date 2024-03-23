def letterCombination(digits):
    dict = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs","8":"tuv", "9":"wxyz"}
    result = []
    if len(digits) == 0: return []
    def seekCombinations(digits, combination, index):
        if len(digits)-1==index:
            str = dict.get(digits[index])
            for char in str:
                result.append(combination+char)
        else:
            for char in dict.get(digits[index]):
                seekCombinations(digits, combination+char, index+1)
    seekCombinations(digits, "", 0)
    return result

print(letterCombination("234422"))