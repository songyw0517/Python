# List Methods
[w3schools.com](https://www.w3schools.com/python/python_ref_list.asp)를 참고하여 작성


## append(elem)
- 리스트의 마지막에 원소를 삽입한다.
    ``` python
    testList = ['apple', 'banana', 'cherry']
    testList.append('orange')
    print(testList)
    # ['apple', 'banana', 'cherry', 'orange']

    ListA = [1,2,3]
    ListB = [4,5,6]
    ListA.append(ListB)
    print(ListA)
    # [1, 2, 3, [4, 5, 6]]
    # [4, 5, 6]을 하나의 원소로 삽입해버린다.
    ```
## clear()
- 리스트의 모든 원소를 삭제한다.
    ``` python
    testList = ['apple', 'banana', 'cherry']
    testList.clear()
    print(testList)
    # [] 출력
    ```
## copy()
- 리스트를 복사하여 반환한다.
    ``` python
    '''이 함수가 왜 필요한지 생각해봤다.
    pyton은 = 연산이 c언어와 다르게 적용되는 듯 했다.
    ListA = [1,2,3]
    tempList = ListA
    tempList.clear()
    print(ListA)

    C언어라면 ListA가 복사되어 tempList에 저장이 되고,
    ListA와 tempList는 서로 다른 변수로 적용이 되어 
    tempList.clear()가 되어도 ListA에는 영향이 없을 것이다.

    하지만 python은 마치 포인터처럼 tempList.clear()을 할 경우
    ListA에도 영향이 가서 ListA도 clear가 되는 것을 확인 할 수 있다.
    그래서 copy라는 함수가 생긴 것 같다.
    '''
    ListA = [1,2,3]
    tempList = ListA.copy() # ListA를 복사
    tempList.clear() # tempList를 clear함
    print(ListA) # clear되지 않고 [1, 2, 3] 출력
    ```
## count(value)
- 리스트에서 value의 갯수를 반환한다.
- value는 string, number, list, tuple 등이 들어갈 수 있다.
    ``` python
    points = [1, 4, 2, 9, 7, 8, 9, 3, 1]
    x = points.count(9) # points에서 9의 갯수를 반환
    print(x) # 9가 2개 있으므로 -> 2
    ```

## extend(iterable)
- 현재 리스트의 마지막에 iterable을 삽입한다.
- 삽입되는 iterable은 현재 리스트에 차례대로 삽입된다. 
    ``` python
    ListA = [1,2,3]
    ListB = [4,5,6]
    ListA.extend(ListB)
    print(ListA)
    # append와 달리, [1, 2, 3, 4, 5, 6]으로 확장된다.
    ```
## index(elem)
- 찾는 원소의 인덱스를 반환한다.
    ``` python
    fruits = ['apple', 'banana', 'cherry']
    x = fruits.index("cherry") # 리스트에서 'cherry'의 인덱스를 반환
    print(x) # -> 2
    ```
## insert(pos, elem)
- 특정 인덱스에 원소를 삽입한다.
- pos인덱스에 elem을 삽입한다.
    ``` python
    fruits = ['apple', 'banana', 'cherry']
    fruits.insert(1, "orange") # 리스트[1]에 'orange'를 삽입한다.
    print(fruits) # ['apple', 'orange' 'banana', 'cherry']
    ```
## pop([pos])
- 특정 인덱스의 원소를 pop한다.
- pos인덱스의 원소를 pop한다. 
- pos의 default값은 -1로, 지정하지 않으면 리스트의 마지막 원소가 pop된다.
    ``` python
    fruits = ['apple', 'banana', 'cherry']
    x = fruits.pop(1)
    print(x) # 'banana'
    print(fruits) # ['apple', 'cherry']

    x = fruits.pop() 
    # pos를 지정하지 않았으므로 
    # 리스트의 마지막 원소를 pop한다.
    print(x) # 'cherry'
    print(fruits) # ['apple']
    ```

## remove(elem)
- 리스트에서 elem을 삭제한다.
- 반환 X
- 리스트에 elem이 없을 경우 ValueError 오류가 발생한다.
``` python
fruits = ['apple', 'banana', 'cherry'
fruits.remove("banana") # 리스트에서 'banana'를 삭제
print(fruits) # ['apple', 'cherry']
```

## reverse()
- 리스트를 reverse시킨다.
    ``` python
    fruits = ['apple', 'banana', 'cherry']
    fruits.reverse()
    print(fruits) # ['cherry', 'banana', 'apple']
    ```
## sort([reverse], [key])
- 리스트를 정렬한다.
    - [reverse]
        - False일 경우 오름차순
        - True일 경우 내림차순
    - [key] : 어떤 함수를 기준으로 정렬할 때 사용한다.
    ``` python
    points = [4,5,6,1,2,3]
    points.sort() # reverse는 False가 default이므로 오름차순 정렬
    print(points) # [1, 2, 3, 4, 5, 6]
    
    points = [4,5,6,1,2,3]
    points.sort(reverse=True) # reverse=True이므로 내림차순 정렬
    print(points) # [6, 5, 4, 3, 2, 1]
    
    # A function that returns the length of the value:
    def myFunc(e):
        return len(e)

    cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
    cars.sort(key=myFunc) 
    # cars 리스트를 정렬하는데 있어서 myFunc를 기준으로 정렬
    # 글자수로 정렬한다.
    print(cars) # ['VW', 'BMW', 'Ford', 'Mitsubishi']
    ```