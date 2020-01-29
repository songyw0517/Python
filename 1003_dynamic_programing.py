global cach
cach = [0 for i in range(41)]
def fibonacci(n):
    if n<=1:
        return cach[n]
    
    elif cach[n]!=0:
        return cach[n]

    else:
        return cach[n] = int(int(fibonacci(n-1)) + int(fibonacci(n-2)))

cach[1]=1
print(cach)
print(type(cach))
print(type(fibonacci(2)))
test=int(input(''))
for i in range(test):
    num = int(input(''))
    if num==0:
        print("1 0")
    elif num==1:
        print("0, 1")
    else:
        fibonacci(num)
        #print(cach[num-1]. cach[num])
