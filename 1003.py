def fibonacci(n):
    global zero
    global one
    if n == 0:
        zero+=1
        return 0
    elif n == 1:
        one+=1
        return 1    
    else :
        return fibonacci(n-1) + fibonacci(n-2)

num = int(input(''))
for i in range(num):
    zero=one=0
    n = int(input(''))
    fibonacci(n)
    print(zero, one)
