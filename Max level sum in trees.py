class node(object):
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
def maxLevelSum(root):
        if root == None:
            return 0
        Q = [root]
        resultLevel = 0 
        resultSum = -100000000
        currLevel = 1
        while len(Q) > 0:
            n = len(Q)
            currSum = 0
            for i in range(n):
                currNode = Q.pop(0)# step-1 (Deleting)
                currSum += currNode.val # step-2 (Appending to subResult)
                if currNode.left != None: # step-3 (Enquing the left child)
                    Q.append(currNode.left) 
                if currNode.right != None: # step-4 (Enquing the right child)
                    Q.append(currNode.right)
            if currSum > resultSum:
                resultSum = currSum 
                resultLevel = currLevel 
            currLevel += 1
        print(resultLevel)  
   
obj1=node(12)
obj2=node(21)
obj3=node(-1)
obj4=node(7)
obj5=node(90)
obj6=node(18)

obj1.left=obj2
obj1.right=obj3
obj2.right=obj4
obj2.left=obj5
obj3.left=obj6
maxLevelSum(obj1)
