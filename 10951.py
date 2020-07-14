import sys
a, b = map(int, sys.stdin.readline().split())
while(a != 0 and b != 0):
    try:
        print(a+b)
        a, b = map(int, sys.stdin.readline().split())
    except:
        break

'''
try, except에 대해 알아보게 해준 문제

오류가 생길시 except로 이동하여 해결한다. 자바에서 배운 것과 같은 내용
'''