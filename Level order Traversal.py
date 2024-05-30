class node():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def levelordertraversal(root):
    if root==None:
        return
    q=[root]
    result=[]
    while len(q)>0:
        n=len(q)
        subresult=[]
        for i in range(n):
            currnode=q.pop(0) #step-1 deleting
            subresult.append(currnode.data) #step-2 appending to subresult
            if currnode.left!=None: #step-3 enquing the left child
                q.append(currnode.left)
            if currnode.right!=None: #step-4 enquing the right child
                q.append(currnode.right)
        result.append(subresult)
    print(result)
obj1=node(100)
obj2=node(21)
obj3=node(-51)
obj4=node(87)
obj5=node(12)
obj6=node(52)
obj7=node(8)
obj8=node(27)
obj9=node(28)
obj10=node(7)

obj1.left=obj2
obj1.right=obj3
obj2.right=obj4
obj2.left=obj5
obj3.left=obj6
obj3.right=obj7
obj4.right=obj8
obj5.right=obj9
obj7.left=obj10
levelordertraversal(obj1)
