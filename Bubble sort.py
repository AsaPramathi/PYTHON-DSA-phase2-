def performbubblesort(nums):
    n=len(nums)
    fixthisindex=n-1

    while fixthisindex>0:
        for index in range(fixthisindex):
            if nums[index]>nums[index+1]:
                temp=nums[index]
                nums[index]=nums[index+1]
                nums[index+1]=temp
        print(nums)
        fixthisindex-=1
nums=[]
nums=list(map(int,input().split()))
print("before sorting",nums)
performbubblesort(nums)
print("after sorting",nums)
            


+
