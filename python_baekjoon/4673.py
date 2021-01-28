def solution(n) -> int:
    sum = n
    while n!=0:
        sum += n%10
        n = int(n/10)
    return sum

arr = [0 for i in range(10000)] # arr의 리스트에 false가 10001개 들어간다.
for i in range(10000):
    idx = solution(i)
    if int(idx) < 10000:
        arr[int(idx)] = 1
for i in range(1, 10000):
    if(arr[i]==0):
        print(i)