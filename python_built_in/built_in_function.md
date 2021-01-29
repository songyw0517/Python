# 내장함수 (built-in function)
import과정을 필요로 하지 않는 파이썬 내부의 함수들을 말한다.

[python document](https://docs.python.org/3/library/functions.html)를 참고하여 작성하였다.

( python 3.9.1 version을 기준으로 작성 )

# 내장함수의 종류
|||Type|||
|:---:|:---:|:---:|:---:|:---:|
| bool() | str() | int() | float() | complex() |
| list() | tuple() | dict() | set() | frozenset() |
| object() | bytes() | bytearray() | memoryview() |
| range() | slice() |
|||Math|||
| abs() | min() | max() | sum() | pow()|
| round() | divmod()|
|||Notation|||
| | hex() | oct() | bin() ||
|||Convert|||
| chr() | ord() |
|||Check|||
| isinstance() | len() | type() | dir() | help() |
| callable() | vars() | id() 
|||Iterable|||
| all | any | iter() | enumerate() | filter() |
| map() | sorted() | zip() | reversed() | next()
|||Class|||
| delattr() | setattr() | hasattr() | getattr() | issubclass() |
| classmethod() | super() | staticmethod() |
|||I/O|||
| | open() | input() | print() ||
|||Etc|||
| __import__() | hash() | eval() | format() | locals() |
| globals() | compile() | breakpoint() | exec() | repr() |
| ascii() |

<br><br><br>

# Description function

|||Type|||
|:---:|:---:|:---:|:---:|:---:|
| bool() | str() | int() | float() | complex() |
| list() | tuple() | dict() | set() | frozenset() |
| object() | bytes() | bytearray() | memoryview() |
| range() | slice() | 
<br>
해당하는 객체를 반환한다. 
<br>
<hr>
<br>

|||Math|||
|:---:|:---:|:---:|:---:|:---:|
| abs() | min() | max() | sum() | pow()|
| round() | divmod()|
<br>

- abs(x) : x의 절댓값을 반환
    ``` python
    print(abs(-2)) # -2의 절댓값 -> 2
    ```
- min(iterable) : iterable에서 최소값을 반환
- min(arg1, arg2, arg3, ...) : argument 중에서 최소값을 반환
    ``` python
    print(min([1, 2, 3, 4, -1]))
    # iterable(리스트)에서의 최소값 반환 -> -1 
    print(min(1, 2, 3, 4, -1)) 
    # arguments에서의 최소값 반환 -> -1
    ```
- max(iterable) : iterable에서 최대값을 반환
- max(arg1, arg2, arg3, ...) : argument 중에서 최대값을 반환
    ``` python
    print(max([1, 2, 3, 4, -1])) 
    # iterable(리스트)에서의 최대값 반환 -> 4
    print(max(1, 2, 3, 4, -1)) 
    # arguments에서의 최대값 반환 -> 4
    ```
- sum(iterable / start=0) 
    - start에 iterable의 값들을 모두 더한 값을 반환
    - start의 default값은 0
    ``` python
    print(sum[1, 2, 3, 4, -1]) 
    # 1, 2, 3, 4, -1을 모두 더한 값 -> 9
    print(sum[1, 2, 3, 4, -1], 100)
    # 100에 1, 2, 3, 4, -1을 모두 더한 값 -> 109
    ```
- pow(base, exp[, mod])
    ```python
    print(pow(2, 3)) 
    # 2의 3승 -> 8
    print(pow(100, 3)) 
    # 100의 3승 -> 1000000
    print(pow(100, (1.0/2.0))) 
    # 100의 1/2승, 100의 제곱근 -> 10.0
    print(pow(100, -(1.0/2.0))) 
    # 100의 -1/2승 -> 0.1
    print(pow(2, 4)%3) 
    # 2의 4승을 3으로 나눈 나머지
    print(pow(2, 4, 3)) 
    # 2의 4승을 3으로 나눈 나머지, 위의 코드보다 짧다
    ```
- round(number[, ndigits])
    - number을 ndigits 자리까지 반올림한다.
    - ndigits은 None을 초기값으로 가진다.
    - ndigits가 None일 경우 인접한 정수를 반환한다.
    - cf) 사사오입 원칙을 따른다. 
    ``` python
    print(round(3,141592)) 
    # ndigits이 None이므로 인접한 정수인 3을 반환 -> 3
    print(round(3,141592, 0))
    # 소수점 아래 0자리까지 반올림 -> 3.0
    print(round(3,141592, 1))
    # 소수점 아래 첫째 자리까지 반올림 -> 3.1
    ========사사오입 원칙===========
    반올림할 자리의 수가 5이면,
    반올림할 앞자리의 수가 짝수이면 내림
    반올림할 앞자리의 수가 홀수이면 올림 한다.
    print(round(4.5))
    # 반올림할 앞자리의 수가 짝수이므로 내림한다. -> 4
    print(round(3.5))
    # 반올림할 앞자리의 수가 홀수이므로 올림한다. -> 4
    ```
- divmod(a, b)
    - a를 b로 나눈 몫과 나머지를 tuple 형식으로 반환
    ```python
    print(divmod(28, 5))
    # 28을 5로 나눈 몫과 나머지 -> (5, 3)
    a, b = divmod(28, 5) 
    print(a) # 몫 -> 5
    print(b) # 나머지 -> 3
    # a에는 몫, b에는 나머지가 들어간다.
    ```
<br>
<hr>
<br>

||Notation||
|:---:|:---:|:---:|
| hex() | oct() | bin() |
- hex(x) : 10진수 x를 받아서 16진수로 변환
    ``` python
    print(hex(255)) # 0xff
    ```
- oct(x) : 10진수 x를 받아서 8진수로 변환
    ``` python
    print(oct(8)) # 0o10
    ```
- bin(x) : 10진수 x를 받아서 2진수로 변환
    ``` python
    print(bin(10)) # 0b1010
    ```

<br>
<hr>
<br>

|||Convert|||
|:---:|:---:|:---:|:---:|:---:|
| chr() | ord() |
- chr(i) : 정수 i 를 받아서 아스키코드에 해당하는 문자(string) 반환
    ``` python
    print(chr(97)) # 97에 해당하는 'a' 반환 -> a
    ```
- ord(c) : 문자 c 를 받아서 아스키코드에 해당하는 정수(int) 반환
    ``` python
    print(ord('a')) # a에 해당하는 97 반환 -> 97
    ``` 
<br>
<hr>
<br>

|||Check|||
|:---:|:---:|:---:|:---:|:---:|
| isinstance() | len() | type() | dir() | help() |
| callable() | vars() | id()
- isinstance(object, classinfo)
    - object가 classinfo인지 확인한다.
    - classinfo에는 <class 'str'>과 같은 데이터, 또는 튜플이 들어가야한다.
    - cf) 만약 Classinfo가 타입이 아니거나 튜플이 아닐 경우 TypeError를 발생시킨다.
    - return True / False
    ```python
    print(isinstance(12, int))
    # 12는 int형이므로 -> True 반환

    print(isinstance('a', 'b'))
    # classinfo의 형이 올바르지 않으므로 TypeError 발생
    print(isinstance('a', type('b')))
    # type('b')는 <class str>이므로 올바른 형태, -> True를 반환
    
    testTuple = (dict, str)
    print(isinstance('a', testTuple))
    # 'a'의 타입인 str이 testTuple안에 있으므로 -> True반환
    # cf) 이때 testTuple 안에는 데이터 형만 들어가야 한다.
    ```
- len(s)
    - s의 길이를 반환한다.
    - s는 sequence(string, bytes, tuple, list, range) 또는
    - collection(dictionary, set, frozenset).
    ``` python
    a = [1,2,3,4,5,6,100]
    print(len(a))
    # a는 리스트, len(a)는 리스트 안의 원소의 갯수 반환 -> 7
    b = [[1,2,3], 4]
    print(len(b))
    # b는 [1,2,3]원소와 , 4를 가지므로, -> 2
    ```
- type(object) : object의 type을 반환
- type(name, bases, dict)
    - 새로운 type의 object를 생성하여 반환한다.
    - name : class이름, class안의 __name__ attribute가 됨
    - bases : 튜플형식, class안의 __bases__ attribute가 됨 (A list of base classes)
    - dict : 사전형식, class안의 attribute와 method 정의가 포함됨
        - __dict__ attribute가 되기 전에 복사 또는 wrapped가 될 수 있다. (data members, methods)
    ``` python
    print(type('a')) 
    # 'a'의 type 반환
    X = type('NewTypeObject', (), dict(a=1))
    '''
    class NewTypeObject:
        a=1
    X = NewTypeObject()
    '''
    ```
    [link](https://tech.ssut.me/understanding-python-metaclasses/)를 참고하자.
- dir([object])
    - 매개변수가 없는 경우 : current local scope에 있는 name 리스트를 반환
        ``` python
        print(dir())
        # ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']
        ```
    - 매개변수가 있는 경우 : object의 valid attribute 리스트를 반환
        ``` python
        print(dir(str))
        # ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
        ```
- help([object])
    - dir과 마찬가지인데, 더 많은 정보를 보여준다.
    - dir은 데이터의 이름, 함수의 이름만을 보여준다면
    - help는 함수의 정의, 반환값 등을 보여준다.
- callable(object)
    - object를 호출할 수 있는지 알려준다.
    - object에는 함수 호출이 아닌 함수 이름이 들어간다.
    ```python
    def func1(a):
        pass
    print(callable(func1)) 
    # func1()이 아닌 func1이 들어가야한다.
    ```
    - 호출을 할 수 있으면 True, 없으면 False를 반환한다.
- vars([object])
    - object의 __dict__ 를 반환
- id( object ) : object의 id를 반환한다.
<br>
<hr>
<br>

|||Iterable|||
|:---:|:---:|:---:|:---:|:---:|
| all | any | iter() | enumerate() | filter() |
| map() | sorted() | zip() | reversed() | next()
- all(iterable)
    - iterable의 원소가 모두 참인지 확인 (and 연산)
    - 모두 참이면 True 반환
    - 아니면 False 반환
        ``` python
        print(all([1,2,3,4,5]))
        # 리스트의 원소가 모두 참이므로 -> True 반환
        print(all([1,2,3,4,0]))
        # 리스트의 원소에 거짓(0)이 있으므로 -> False 반환
        ```
- any(iterable)
    - iterable의 원소가 하나라도 참인지 확인 (or 연산)
    - 하나라도 참이면 True 반환
    - 모두 거짓이면 False 반환
        ``` python
        print(any([1,2,3,4,0]))
        # 리스트의 원소에 참이 있으므로 -> True 반환
        print(any([0,0,0,0]))
        # 리스트의 원소가 모두 거짓이므로 -> False 반환
        ```
- enumerate(iterable, start=0)
    - iterable의 값과 인덱스(start)를 튜플로 묶어 enumerate 객체로 반환
    - enumerate형을 반환하므로, list로 묶는 것이 좋다.
    - 코드를 보는 것이 이해하기 쉽다
        ``` python
        print(list(enumerate(['a','b','c','d'])))
        # [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd')]
        print(list(enumerate(['a','b','c','d'], 3)))
        # start=3을 주어서 인덱스가 3부터 시작한다.
        # [(3, 'a'), (4, 'b'), (5, 'c'), (6, 'd')]
        ```
- filter(function, iterable)
    - iterable의 원소들에 대하여 function을 통과시킨 값을 filter 객체로 반환
    - filter형을 반환하므로, list로 묶는 것이 좋다.
        ``` python
        def moreTen(i):
        if i>10:
            return i
        print(list(filter(moreTen, [1,2,3,4,110, 22, 5, 6])))
        # filter을 사용하는 방법
        print(list(x for x in [1,2,3,4,110, 22, 5, 6] if moreTen(x)))
        # list comprehension을 사용하는 방법
        ```
    - 맞는지는 모르겠으나 filter에 사용되는 함수는 만족하면 반환, 아니면 pass식으로 해야 적용이 되는 것 같다.
- map(function, iterable)
    - iterable의 원소들에 대하여 function을 적용시켜 map 객체로 반환
    - map형을 반환하므로, list로 묶는 것이 좋다.
    ``` python
    def addTen(i):
    return i+10
    print(list(map(addTen, [1,2,3,4,5,6])))
    # [1,2,3,4,5,6]에 대하여 addTen함수를 적용시킨다.
    ```
- sorted(iterable, key=None, reverse=False)
    - 기존의 리스트를 변경하는 것이 아니라 정렬을 한 새로운 리스트를 반환
    ``` python
    print(sorted("hello"))
    # ['e', 'h', 'l', 'l', 'o']
    print(sorted(['b','c', 'a', 'd', 'e','z', 'x']))
    # ['a', 'b', 'c', 'd', 'e', 'x', 'z']
    ```
    - key : literable의 몇 번째 항목에 대해 정렬할 것인지 지정한다.
    ``` python
    student = [
        ('홍길동', 3.9, 160303),
        ('김철수', 4.2, 160102),
        ('김영자', 3.5, 160215),
        ('임지수', 3.7, 160412)
    ] # 학번으로 정렬하고 싶다면 key 를 지정하면 된다.
    print(sorted(student, key = lambda x:x[2])) 
    # x의 [2]인덱스로 정렬
    # [('김철수', 4.2, 160102), ('김영자', 3.5, 160215), ('홍길동', 3.9, 160303), ('임지수', 3.7, 160412)]
    ```
    - reverse : 
        - True - 내림차순
        - False - 오름차순 (default)
    ``` python
    print(sorted(['b','c', 'a', 'd', 'e','z', 'x'], reverse=True))
    # ['z', 'x', 'e', 'd', 'c', 'b', 'a']
    ```

- zip(*iterables)
    - 각 iterable의 같은 인덱스의 원소들을 튜플로 묶어준다.
    - zip 객체로 반환하므로 list로 묶는게 좋다
    - 각 iterable에 대해서 길이(index)가 다를 경우 매칭되지 않는다.
        ``` python
        a = [1,2,3]
        b = ['a', 'b']
        print(list(zip(a,b)))
        # 3은 b리스트에 대해 매칭할 수 없으므로 
        # [(1,'a'), (2,'b')] 만 반환된다.

        a = [1,2,3]
        b = ['a', 'b', 'c', 'd']
        c = [{'key1':'value1'}, {'key2':'value2'}]
        print(list(zip(a,b,c)))
        # [(1, 'a', {'key1': 'value1'}), (2, 'b', {'key2': 'value2'})]
        ```
- reversed(seq)
    - sequence의 순서를 reverse 시킨 새로운 reverse객체를 생성한다. 
    - <list_reverseiterator object at 0x000001B23D100F40>
    - list형 변환하는게 좋다.
    ``` python
    print(list(reversed([5,63,2,12,54,65,854,44,3,1])))
    # [1, 3, 44, 854, 65, 54, 12, 2, 63, 5]
    ```
- next(iterator [,default])
    - iterator의 다음 index로 접근하는 메소드이다.
    - 현재 가리키고 있는 iterator의 값을 반환하고, 다음 인덱스를 가리킨다.
    - C언어의 배열 포인터 느낌이다.
    - 마지막일 경우 Stoplteration 에러가 발생한다.
    ``` python
    a = iter([1,2,3,4,5,6,7,8]) # list를 iterator로 변환
    print(next(a)) # a[0]인 1을 반환하고, a[1]인 2를 가리킴
    print(list(a)) 
    # a[1]을 가리키고 있으므로, [2,3,4,5,6,7,8] 이 출력된다.
    print(next(a)) # 2반환, 3으로 이동
    print(next(a)) # 3반환, 4로 이동
    print(list(a)) # [4,5,6,7,8] 출력
    ```
- iter() 
    - iterator로 바꿔주는 함수
    - iterator와 iterable은 엄연히 다르다.
    - iterable (str, list, tuple)
    - iterator로 변경하기 위해서는 iter함수를 사용해야한다.
<br>
<hr>
<br>

|||Class|||
|:---:|:---:|:---:|:---:|:---:|
| delattr() | setattr() | hasattr() | getattr() | issubclass() |
| classmethod() | super() | staticmethod() |
- delattr(object, name)
- setattr() 
- hasattr() 
- getattr() 
- issubclass() 
- classmethod() 
- super() 
- staticmethod() 

<br>
<hr>
<br>

||I/O||
|:---:|:---:|:---:|
| open() | input() | print() |
- open
- input
- print

<br>
<hr>
<br>

|||Etc|||
|:---:|:---:|:---:|:---:|:---:| 
| __import__() | hash() | eval() | format() | locals() |
| globals() | compile() | breakpoint() | exec() | repr |
| ascii() |
- __import__() 
- hash() 
- repr() # [refer1](https://pinocc.tistory.com/168), [refer2](https://shoark7.github.io/programming/python/difference-between-__repr__-vs-__str__)
[refer3](https://itholic.github.io/python-str-repr/)
- ascii()
- eval() 
- format() 
- locals() 
- globals()
- compile() 
- breakpoint() 
- exec()

<br>


# Study
Python의 type 종류를 알기 위해서 document의 앞에 class가 붙은 내장 함수들의 타입을 print해보았다.
``` python
print(
    type(bool()),
    type(str()),
    type(int()),
    type(float()),
    type(complex()),
    type(list()),
    type(tuple()),
    type(dict()),
    type(set()),
    type(frozenset()),
    type(object()),
    type(bytes()),
    type(bytearray()),
    type(memoryview(bytearray())),
    type(range(2)),
    type(property()),
    type(slice(1))
)
```
결과는 모두 다른 타입을 보여주었다.
 <class 'bool'> <class 'str'> <class 'int'> <class 'float'> <class 'complex'> <class 'list'> <class 'tuple'> <class 'dict'> <class 'set'> <class 'frozenset'> <class 'object'> <class 'bytes'> <class 'bytearray'> <class 'memoryview'> <class 'range'> <class 'property'> <class 'slice'>

