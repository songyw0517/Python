import sys
def han_su(n):
    cnt=0
    for i in range(1,n+1):
        if i < 100:
            cnt +=1
        else:
            d = int((i/10)%10)-(i%10) # 공차
            temp = i
            temp_n = 0
            is_true = 0
            while(temp != 0):
                temp_n += 1
               
                if int((temp/10))%10-temp%10 == d:
                    is_true += 1
                temp = int(temp/10)
                if int(temp/10)==0: break
            if temp_n == is_true:
                cnt+=1
    return cnt
num = int(sys.stdin.readline().rstrip())
print(han_su(num))
'''
for문의 범위를 헷갈려서 헤맸다...
for i in range(1, 5)이면, 1,2,3,4 이다.
for i in range(5)이면 0이 생략된 것으로, 0,1,2,3,4로 5번 반복된다.

'''