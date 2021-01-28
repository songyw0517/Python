test=int(input())
for i in range(test):
    string=input()
    Sum=0
    cnt=1
    k=0
    while k<len(string):
        if string[k]is'O':
            Sum+=cnt
            cnt+=1
        else:
            cnt=1
        k+=1
    print(Sum)
    
