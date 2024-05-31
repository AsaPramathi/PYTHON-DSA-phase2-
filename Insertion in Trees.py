class TreeNode:
    def __init__(self, data):
        self.val = data 
        self.left = None 
        self.right = None
 
def printInorder(root):
    if root == None:
        return
    
    # 1 
    printInorder(root.left)
    # 2 
    print(root.val, end = ", ")
    # 3
    printInorder(root.right)
 
 
def insertIntoBST(root, val):
    if root == None:
        return TreeNode(val)
    elif root.val > val:
        root.left = insertIntoBST(root.left, val)
    else:
        root.right = insertIntoBST(root.right, val)
    return root
 
nums = list(map(int,input().split()))
print(nums)
root = None
for ele in nums:
    root = insertIntoBST(root, ele)
printInorder(root)
