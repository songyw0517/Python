import sys

T, x = map(int, sys.stdin.readline().split()) # T, x를 입력받는다.
a = list(map(int, sys.stdin.readline().split())) # 배열을 입력받는다.
ans = [] # 정답 배열을 만든다.
for i in range(T):
    if a[i]<x:
        ans.append(a[i]) # 조건을 만족할 때 정답 배열에 넣는다.

print(" ".join(map(str, ans))) # 정답을 출력한다.

'''
join 함수에 대해 배우는 문제였다.

사용법 : [구분할 문자열].join(리스트)

animals = ['사자', '코끼리', '기린', '원숭이']

print (','.join(animals)) 
#출력 : 사자,코끼리,기린,원숭이  출력됨

print ('\n'.join(animals))

출력

> 사자
> 코끼리
> 기린
> 원숭이
    
'''