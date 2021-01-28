C=int(input())
for i in range(C):
    A=list(map(int, input().split()))
    Sum=n=0
    for k in range(1, A[0]+1):
        Sum+=A[k]
    avg=float(Sum)/(A[0])
    for k in range(1, A[0]+1):
        if A[k]>avg:
            n+=1
    print(str('%.3f' % round(float(n)/A[0]*100, 3)) + '%')
    A.clear()
