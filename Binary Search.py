nums=list(map(int,input().split()))
print(nums)
target=int(input("enter your target element"))
nums=sorted(nums)
left=0
right=len(nums)-1
flag=-1
while left<=right:
    mid=(left+right)//2
    if nums[mid]==target:
        flag=mid
        break
    elif nums[mid]>target:
        right=mid-1
    else:
        left=mid+1
if flag == -1:
    print("target not found")
else:
    print("target found at index:",flag)
