test=int(input(''))
item=[]
fibo=[1,1]
for i in range(test):
    item.append(int(input('')))
    
for i in range(2, max(item)):
    fibo.append(fibo[i-1]+fibo[i-2])
while item != []:
    value = item.pop(0)
    if value==0:
        print('1 0')
    elif value==1:
        print('0 1')
    else:
        print(fibo[value-2], fibo[value-1])
