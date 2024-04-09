def minRemoveToMakeValid(s: str) -> str:
    stack = []
    n = len(s)
    result = ''
    for i in range(n):
        if s[i] == '(':
            stack.append(i)
        if s[i] == ')':
            if len(stack) > 0:
                index = stack.pop()
                if s[index]==')':
                    stack.append(index)
                    stack.append(i)
            else:
                stack.append(i)
    to_remove_index = 0
    for i in range(n):
        if to_remove_index < len(stack) and i == stack[to_remove_index]:
            to_remove_index+=1
        else:
            result+=s[i]


minRemoveToMakeValid("))((")
