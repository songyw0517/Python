result=1
for i in range(3):
    num=int(input())
    result*=num
arr=[0for i in range(10)]
result=str(result)
for i in range(len(result)):
    arr[int(result[i])]+=1

for i in range(10):
    print(arr[i])
