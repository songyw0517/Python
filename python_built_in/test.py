#python types
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
print("="*50)
print(any([1,2,3,4,0]))
print(any([0,0,0,None]))
print("="*50)

def moreTen(i):
    if i>10:
        return i
print(list(filter(moreTen, [1,2,3,4,110, 22, 5, 6])))
# filter을 사용하는 방법
print(list(x for x in [1,2,3,4,110, 22, 5, 6] if moreTen(x)))
# list comprehension을 사용하는 방법
print("="*50)
def addTen(i):
    return i+10
print(list(map(addTen, [1,2,3,4,5,6])))
print("="*50)
print(sorted("hello"))
print(sorted(['b','c', 'a', 'd', 'e','z', 'x'], reverse=True))

student = [
    ('홍길동', 3.9, 160303),
    ('김철수', 4.2, 160102),
    ('김영자', 3.5, 160215),
    ('임지수', 3.7, 160412)
]
print(sorted(student, key = lambda x:x[2]))
print("="*40)
a = [1,2,3]
b = ['a', 'b', 'c', 'd']
c = [{'key1':'value1'}, {'key2':'value2'}]
print(list(zip(a,b,c)))
print("="*20)
print(list(reversed([5,63,2,12,54,65,854,44,3,1])))
print("="*20)
a = iter([1,2,3,4,5,6,7,8])
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(list(a))


print("="*30)
ListA = [1,2,3]
tempList = ListA.copy()
tempList.clear()
print(ListA)

print("="*30)
fruits = ['apple', 'banana', 'cherry']
x = fruits.pop(1)
print(x) # 'banana'
print(fruits) # ['apple', 'cherry']
x = fruits.pop()
print(x) # 'cherry'
print(fruits) # ['apple']