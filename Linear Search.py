##nums=[12,18,6,54,36,27]
##target=27
##flag=-1
##n=len(nums)
##for index in range(n):
##    if nums[index]==target:
##        flag=index
##        break
##if flag==-1:
##    print("not found")
##else:
##    print("target found:",flag)

nums=list(map(int,input().split()))
target=int(input("enter your target element"))
flag=-1
n=len(nums)
for index in range(n):
    if nums[index]==target:
        flag=index
        break
if flag==-1:
    print("not found")
else:
    print("target found:",flag)


