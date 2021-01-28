num=int(input())
A=list(map(int, input('').split()))
Max=max(A)
total=0
for i in range(num):
    total+=A[i]/Max*100

print(total/num)
