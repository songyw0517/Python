import sys
number = int(input())
ans = sys.stdin.readline().rstrip
print(type(ans))
for i in range(number):
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)

'''
sys.stdin.readline()을 배울 수 있는 문제였다.
input함수는 느리기때문에 sys를 import하여 입력을 직접 받을 수 있게 한다고 한다.
sys.stdin.readline()으로 반환되는 입력값은 문자열이고, 입력을 했다는 엔터(\n)까지 포함한다.

1. 순수한 문자열을 받기 위해서는 st = sys.stdin.readline().rstrip()로 받으면 뒤의 \n이 사라진다.
2. 받은 문자열을 정수형으로 받기 위해서는 a, b = map(int, sys.stdin.readline().split())으로 받으면 된다.


'''