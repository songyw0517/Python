import sys

num = int(sys.stdin.readline().rstrip())

cy1 = int(num / 10)
cy2 = int(num % 10)

if cy1+cy2 < 10:
    cy = cy2*10 + cy1 + cy2
else:
    cy = cy1+cy2
    if cy >= 10:
        cy = cy2*10 + (cy % 10)
cnt = 1
while cy != num:
    cy1 = int(cy / 10)
    cy2 = int(cy % 10)
    if cy1+cy2 < 10:
        cy = cy2*10 + cy1 + cy2
    else:
        cy = cy1+cy2
        if cy >= 10:
            cy = cy2*10 + (cy % 10)
    cnt = cnt+1
    
print(cnt)

'''
문제의 조건을 맞추는데 힘들었던 문제이다.

'''