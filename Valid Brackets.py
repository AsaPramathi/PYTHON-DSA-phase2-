#is balanced
def isbalanced(word):
    stack=[]
    for ele in word:
        if ele =='(':
            stack.append(ele)
        else:
            if len (stack)==0:
                return False
            else:
                stack.pop()
    if len(stack)==0:
        return True
    return False
word=input()
print(isbalanced(word))

#valid brackets
class Solution(object):
    def isValid(self, s):
        stack = []
        openBrackets = ["(", "{", "["]
        for ele in s:
            if ele in openBrackets:
                stack.append(ele)
            else:
                if len(stack) == 0:
                    return False 
                elif ele == ')':
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        return False
                elif ele == ']':
                    if stack[-1] == '[':
                        stack.pop()
                    else:
                        return False
                elif ele == '}':
                    if stack[-1] == '{':
                        stack.pop()
                    else:
                        return False
        if len(stack) == 0:
            return True 
        return False
value=Solution()
s=input()
print(value.isValid(s))
