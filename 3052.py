A=[0 for i in range(42)]
for i in range(10):
    num=int(input())
    A[num%42]+=1

print(len(A)-A.count(0))
    
