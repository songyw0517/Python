# 문자열 함수 (String.함수 형식)
- split('기준 문자') : 문자열을 '기준 문자'를 기준으로 나누어 리스트로 반환
ex) list = input("문자 입력").split() : 공백을 기준으로 문자열을 나누어 리스트로 반환


# 입력
num = input()
num = int(input())
num, num2 = input().split()
cf) num1, num2 = int(input().split()) 는 오류가 발생한다. 
-> map 함수를 사용하면 된다. : num1, num2 = map(int, input().split())

# map 함수
- 여러개의 데이터에 대하여 같은 연산을 한번에 진행시키는 함수
- map(연산함수, 순회 가능한 데이터)의 형식을 가진다.
ex) num1, num2 = map(int, input().split())
-> input으로 받은 문자열을 공백으로 분할한 리스트에 int형을 지정한다.
++ split()함수를 수행하면 리스트로 반환한다.


# lambda
- 런타임에서 생성하여 사용할 수 있는 익명함수
- lambda '매개변수' : 식
- 매개변수를 식에 대입하여 결과를 반환한다.
ex) lambda u : u * 10
-> 매개변수 u를 받아서 * 10의 연산 값을 반환한다.

# filter
- 여러개의 데이터에서 일부의 데이터만 추출함
- filter(조건 식, 순회 가능한 데이터)
- 조건 식에는 함수가 들어갈 수 있다. (def로 지정함 함수 또는 lambda 함수)
- 반환 값은 <class 'filter'>이다.
<code>
t = [1,2,3,4,5,6]
a = list(filter(lambda x:x>3, t))
print(a)



</code>
# in
# range
#




# curious
-> 0 for i in range(41)
-> find, rfind
-> 튜플의 변환
# Method
0. skill
    > 빠른 입력
    빠르게 입력받기 위해서는 input함수가 아닌 sys.stdin.readline()함수를 이용해야한다.
    ``` python
    # input대신 sys.stdin.readline()함수를 쓰면 된다. 반환값은 string형이다. 그러나 input함수와 달리 맨 뒤의 개행문자까지 반환하기때문에 문자열을 받고싶은 경우 rstrip함수를 사용해야한다.
    
    # 숫자 하나를 받는 경우
    num = int(sys.stdin.readline())

    # 숫자 여러개를 받는 경우, split함수를 써줘야 한다.
    -> n1, n2 = map(int, sys.stdin.readline().split()) 

    # 문자열을 받는 경우, rstrip()함수를 안쓸 경우 개행까지 저장됨
    st = sys.stdin.readline().rstrip()
    ```

    > 여러개의 문자, 숫자 입력받기
    ``` python
    A, B = input('').split(' ') # 입력받은 문자열을 ' (띄어쓰기)로 나누어 변수에 저장한다.
    ``` 그런데 이때 A와 B에 들어가는 값은 숫자가 아닌 문자열이다.
    따라서 형변환을 하고 사칙연산을 수행해야 오류가 나지 않는다. ```
    ```
    > 리스트에 담기
    ``` python
    A=list(map(int,input().split())) #A에 여러개의 변수가 입력된 리스트를 저장
    ```
    > 각각에 적용하기
    ```python
    a,b=map(int,input().split()) # map(각각의 데이터에 적용시킬 일(함수), 값
    ``` 여기서는 입력받은 값을 int형으로 바꾸어 a, b에 저장한다. ```
    print(a-b)
    ```

    > 리스트 초기화
    ``` python
    arr = [0 for i in range(41)] # arr의 리스트에 0이 41개 들어간다. 
    ```
    
    > 서식문자 사용
    .format를 사용하면 된다.
    ``` python
    A=list(map(int,input().split())) #A에 여러개의 변수가 입력된 리스트를 저장
    print("{} {}".format(min(A), max(A)))
    ```

    > 함수의 형태
    ``` python
    def solve(a): # 반환시 오류가 뜬다.
        print(a)
    ```
    ```python
    def solve(a: list) -> int: #a라는 리스트를 매개변수로 받음, int로 반환함
        return sum(a)
    ```
1. 수학
2. 리스트 및 문자열 // []

    리스트 설명:
    - C언어의 배열과 비슷한 개념이다.
    - 인덱스로 접근할 수 있으며, 값의 변경이 가능하다.
    - 중복이 가능하다.

    > 리스트의 반복문
    - 리스트 접근 및 출력
    ``` python
    thislist = ["apple", "banana", "cherry"]
    for x in thislist:
        print(x)
    ```

    - 리스트 안에 존재하는가?
    ``` python
    thislist = ["apple", "banana", "cherry"]
    if "apple" in thislist:
        print("Yes, 'apple' is in the fruits list")
    ```


    > append : 리스트의 맨 뒤에 값을 추가한다.
    ``` python
    list = []
    list.append("abcd")
    print(list) # 'abcd'출력
    ```
    > insert : 원하는 인덱스에 값을 넣어준다.
    ``` python
    thislist = ["apple", "banana", "cherry"]
    thislist.insert(1, "orange")
    print(thislist) # ['apple', 'orange', 'banana', 'cherry'] 출력
    ```

    > pop : 리스트의 맨 뒤의 값을 없애면서 반환한다.
    ``` python
    list = ['ccc','abcd']
    print(list.pop()) # 'abcd'출력
    print(list) # 'ccc' 출력
    ```
    > pop(0) : 리스트의 맨 앞의 값을 없애면서 반환
    ```python
    list = ['a', 'b']
    print(list.pop(0)) # 'a'출력
    print(list) # 'b'출력
    ```

    > remove : 원하는 아이템을 리스트에서 삭제한다.
    ``` python
    thislist = ["apple", "banana", "cherry"]
    thislist.remove("banana") # list에서 banana를 찾아서 삭제한다.
    print(thislist)
    ```

    del : 리스트의 원하는 인덱스를 삭제한다. || 리스트 자체를 없앨 수 있다.
    ```python
    thislist = ["apple", "banana", "cherry"]
    del thislist[0]
    print(thislist) # ['banana', 'cherry']
    ```

    > 리스트 삭제
    - del 사용
    ```python
    thislist = ["apple", "banana", "cherry"]
    del thislist
    print(thislist) # thislist가 undefined라고 오류가 뜬다.
    ```

    - clear 사용
    ``` python
    thislist = ["apple", "banana", "cherry"]
    thislist.clear() # thislist는 빈 리스트가 된다. 없어지지 않는다.
    print(thislist) # [] 출력 됨
    ```

    > 리스트 복사
    - copy메소드를 사용
    ``` python
    thislist = ["apple", "banana", "cherry"]
    mylist = thislist.copy()
    print(mylist)
    ```
    - 할당 연산자 사용 (이게 더 직관적이다.)
    ``` python
    thislist = ["apple", "banana", "cherry"]
    mylist = list(thislist)
    print(mylist)
    ```

    > 두 개의 리스트를 합치기
    + 연산 사용하면 된다.

    > 리스트 출력시 대괄호 없애기
    ``` python
    lst = [1,2,3,4,5]
    print(",".join([str(i) for i in lst] )) #또는
    print(",".join(map(str, lst)))
    ```
    > join : 리스트를 특정 구분자를 포함하여 문자열로 변환해주는 함수.
    
    >> 사용법 : [구분할 문자열].join(리스트)
    ``` python
    animals = ['사자', '코끼리', '기린', '원숭이']

    print (','.join(animals)) 
    #출력 : 사자,코끼리,기린,원숭이  출력됨

    print ('\n'.join(animals))
    ''' 출력
    사자
    코끼리
    기린
    원숭이
    '''
    ```
    > sort
    > sorted
    > index
    > count
    > upper
    > lower
    > strip
    
3. 튜플 ()
    > 설명
    - 리스트와 같지만 값을 변경할 수 없다는 차이점이 있다.

    > 튜플의 값을 변경하기
    - 리스트로 변경 하고, 값을 변경하고 튜플로 바꾼다.
    ``` python
    x = ("apple", "banana", "cherry")
    y = list(x)     # 튜플x를 리스트로 변경
    y[1] = "kiwi"   # 값 변경
    x = tuple(y)    # 튜플로 변경

    print(x)
    ```

    > method
    - index : 찾으려는 아이템의 인덱스를 알려줌
    ``` python
    thistuple = ('apple', 'banana', 'cherry')
    print(thistuple.index('apple')) # 0 출력
    ```

    - count : 찾으려는 아이템의 갯수를 알려줌
    ``` python
    thistuple = ('apple', 'banana', 'cherry', 'cherry')
    print(thistuple.count('cherry')) # 2 출력
    ```

4. 집합 {}
    > 설명
    - 정렬되지 않은 집합을 의미한다.
    - 인덱스로 접근 할 수 없다.
    - 중복될 수 없다.
    - 아이템을 변경할 수 없으나 추가는 가능하다.

    > 아이템이 존재하는지? (in을 사용하면 된다.)
    ``` python 
    thisset = {"apple", "banana", "cherry"}
    print("banana" in thisset) # banana가 존재하므로 true를 반환한다.
    ```

    > add : 집합에 아이템 하나를 추가한다.
    ``` python
    thisset = {"apple", "banana", "cherry"}
    thisset.add("orange") # orange 추가
    print(thisset)
    ```

    > update : 집합에 여러개의 아이템을 추가한다.
    ``` python
    thisset = {"apple", "banana", "cherry"}
    thisset.update(["orange", "mango", "grapes"])
    print(thisset) # 순서는 랜덤으로 들어가는듯 하다
    ```

    > 집합 합치기 - union함수, update를 사용한다. 중복된 값은 알아서 처리된다.
    - union으로 합치기
    ``` python
    set1 = {"a", "b" , "c"}
    set2 = {1, 2, 3, 'a'}
    set3 = set1.union(set2) # 중복된 a는 하나만 들어간다.
    print(set3)
    ```
    - update로 합치기
    ``` python
    set1 = {"a", "b" , "c"}
    set2 = {1, 2, 3, 'a'}
    set1.union(set2) # 중복된 a는 하나만 들어간다.
    print(set3)
    ```

5. 딕셔너리
    > 설명
    - 정렬되지 않음
    - 값의 변경 가능
    - 인덱스 연산 가능
    - 중복 불가능
내장?함수
max
min
sum
round

리스트
.append
.pop
.count

문자열
.split
.format

서식문자 % : '%.3f' % round(n/A[0] * 100, 3)
print('%d %d' %(3,3))-> 3 3 출력