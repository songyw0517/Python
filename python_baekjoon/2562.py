num=Max=int(input())
index=0
for i in range(1,9):
    num=int(input())
    if Max<num:
        Max=num
        index=i

print(Max)
print(index+1)
