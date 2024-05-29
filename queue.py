def enqueue(q,ele):
    q.append(ele)
    print(ele,"inserted into queue")
def dequeue(q):
    if len(q)==0:
        print("queue is emptyy")
        return
    print(q[0],"is deleted")
    q.pop(0)
q=[]
nums=list(map(int,input().split()))
for ele in nums:
    enqueue(q,ele)
print(q)
for ele in nums:
    dequeue(q)
    print(q)
dequeue(q)

