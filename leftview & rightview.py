class node():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def printLeftView(root):
     if root == None:
        return 
     Q = [root]
     result = []
     while len(Q) > 0:
         n = len(Q)
         for i in range(n):
            # step-1 (Deleting)
             currNode = Q.pop(0)
 
            # step-2 (Appending to result)
             if i == 0:
                 result.append(currNode.data)
 
            # step-3 (Enquing the left child)
             if currNode.left != None:
                 Q.append(currNode.left)
 
            # step-4 (Enquing the right child)
             if currNode.right != None:
                Q.append(currNode.right)
 
     print("Left view is:", result)
 
def printRightView(root):
    if root == None:
        return 
    Q = [root]
    result = []
    while len(Q) > 0:
        n = len(Q)
        for i in range(n):
            # step-1 (Deleting)
            currNode = Q.pop(0)
 
            # step-2 (Appending to result)
        if i == n - 1:
            result.append(currNode.data)
 
            # step-3 (Enquing the left child)
        if currNode.left != None:
            Q.append(currNode.left)
 
            # step-4 (Enquing the right child)
        if currNode.right != None:
            Q.append(currNode.right)
 
    print("Right view is:", result)
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
printRightView(obj1)
printLeftView(obj1)
