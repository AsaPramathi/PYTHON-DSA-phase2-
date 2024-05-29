#stack implementation
'''def push(stack,ele):
    stack.append(ele)
    print(ele,"inserted into stack successfully")
def pop(stack):
    if len(stack)==0:
        print("stack is empty")
        return
    print(stack[-1],"deleted  successfully")
    stack.pop()
stack=[]
push(stack,50)
push(stack,60)
push(stack,70)
push(stack,80)
push(stack,90)

pop(stack)
pop(stack)
pop(stack)
pop(stack)
pop(stack)
pop(stack)

def push(stack,ele):
    stack.append(ele)
    print(ele,"inserted into stack successfully")
def pop(stack):
    if len(stack)==0:
        print("stack is empty")
        return
    print(stack[-1],"deleted  successfully")
    stack.pop()
stack=[]
nums=list(map(int,input().split()))
for ele in nums:
    push(stack,ele)
print(stack)
for ele in nums:
    pop(stack)
    print(stack)
pop(stack)

#example of stack
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
print(isbalanced(word))'''


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





