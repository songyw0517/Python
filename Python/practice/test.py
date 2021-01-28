# 형변환 내장함수
print("="*25,"형 변환 내장함수","="*25)
print(type(bool()), 
type(str()), 
type(int()), 
type(float()), 
type(complex()), 
type(list()), 
type(tuple()), 
type(dict()), 
type(set()), 
type(frozenset()), 
type(bytes()), 
type(bytearray()))
print("")
print("="*25,"수학 연산 함수","="*25)
print("abs(-1) 절대값 : ", abs(-1))
print("min([1,2,3,4,-1,2,2]) Iterable 최솟값 (리스트) : ", min([1,2,3,4,-1,2,2]))
print("min((1,2,3,4,-1,2,2)) Iterable 최솟값 (튜플) : ", min((1,2,3,4,-1,2,2)))
print("max([1,2,3,4,-1,2,2]) Iterable 최댓값 (리스트) : ", max([1,2,3,4,-1,2,2]))
print("max((1,2,3,4,-1,2,2)) Iterable 최댓값 (리스트) : ", max((1,2,3,4,-1,2,2)))
print("sum([1,2,3,4,-1,2,2]) Iterable의  합  (리스트) : ", sum([1,2,3,4,-1,2,2]))
print("sum((1,2,3,4,-1,2,2)) Iterable의  합   (튜플) : ", sum((1,2,3,4,-1,2,2)))
print("pow(4, 2) 4^2 : ", pow(4,2)) # 4^2
print("pow(-4, 3) (-4)^3", pow(-4,3))# (-4)^3
print("round(3.141592, 2) : ", round(3.141592, 2)) # 소수점 아래 2자리까지 반올림
print("round(3.141592) : ", round(3.141592)) # default : 0
print("divmod(7, 2) : 7을 2로 나눈 몫과 나머지 (튜플) : ", divmod(7,2))
print("")
print("="*25,"진수 표현","="*25)
print("hex(10) 16진수 표현 : ", hex(10))
print("oct(10) 8진수 표현 : ", oct(10))
print("bin(3) 2진수 표현 : ", bin(3)) # 3 -> 0b11 
print("type(hex(10)), type(oct(10)), type(bin(3))은 모두 str이다.", type(hex(10)), type(oct(10)), type(bin(3)))
print("")
print("="*25,"그 외 변환 함수","="*25)
print("chr(97) 97을 문자로 변환 : ", chr(97))
print("ord('a') 'a'을 정수로 변환 : ", ord('a'))
a = 12
print("id(a) a변수의 주소값 반환 : ", id(a)) # 얘를 가지고 무엇을 할 수 있을까?
print("="*25,"확인할 수 있는 함수","="*25)
print("isinstance(1, int) : 1이 int인지 확인 : ", isinstance(1, int))
print("isinstance(1, float) : 1이 int인지 확인 : ", isinstance(1, float))
class people:
    def study(self):
        return "turn"
P = people()
print("isinstance(P, people) : P가 people 클래스(객체)인지 확인 : ", isinstance(P, people))
# isinstance함수의 첫번째 매개변수와 두번째 매개변수의 클래스가 같으면 True, 다르면 False 반환
print("len([1,2,3,4]) 리스트 : ", len([1,2,3,4]))
print("len((1,2,3,4)) 튜플 : ", len((1,2,3,4)))
print("len({'name':'song', 'age':25, 'type':'dic'}) 사전 : ", len({'name':'song', 'age':25, 'type':'dic'}))
'''len에는 문자열, 바이트열, 튜플, 리스트, range, 사전, 집합, 불변 집합 등의 자료형이 들어갈 수 있다.'''
print("type(int()) 자료형을 알려줌 : ", type(int()))
print("dir(int()) int형-클래스?의 정보(함수, 변수)를 보여줌 : " , dir(int()))
# print("help(int()) int형-클래스?의 정보(함수, 변수)를 자세히 보여줌 : ", help(int()))
print("")
print("="*25,"파일 입출력 함수 open","="*25)
print("한글을 사용하기 위해서는 encoding=\"UTF8\"을 사용해야한다!")
print("write mode")
f = open("test.txt", "w") # write 모드로 파일 생성
f.write("The first line\n")
f.write("The second line\n")
f.close()
print('\nappend mode & write user input values')
f = open("test.txt", 'a', encoding="UTF8") # append 모드로 파일 불러오기
while True:
    string = input()
    if string.lower() == 'quit':
        break
    f.write(string + '\n')
f.close()
print('\nread mode & file path')
filePath = 'C:/Users/sng22/OneDrive/바탕 화면/파이썬.txt' # 파이썬에서는 경로를 \가 아닌 /를 사용한다.
f = open(filePath, "r", encoding="UTF8") # read 모드로 파일 불러오기 
line = f.readlines()
for i in range(len(line)):
    print(line[i], end = '')
'''open mode
w : 쓰기
r : 읽기
a : 추가
b : 바이너리
'''
f.close()
print('\ntest.txt 출력')
f = open('test.txt', 'r', encoding='UTF8')
line = f.readlines()
for i in range(len(line)):
    print(line[i], end = '')
print('line = ', line)

print('\nIterable 자료형과 관련된 함수')
print('all(iterable 자료형) : ', all([1,1,1,2, 3])) # all(iterable 자료형) : iterable 자료형들의 & 연산
print('all(iterable 자료형) : ', all((1,1,1,2, 0))) # all(iterable 자료형) : iterable 자료형들의 & 연산
print('any(iterable 자료형) : ', any([1,1,1,2, 3])) # any(iterable 자료형) : iterable 자료형들의 | 연산
print('any(iterable 자료형) : ', any((1,1,1,2, 0))) # any(iterable 자료형) : iterable 자료형들의 | 연산
print('range(5) == range(0,5), 자료형은 range임', type(range(5)))
print('이를 리스트로 변환한다면 : ', list(range(5)))
print('이를 튜플로 변환한다면 : ', tuple(range(5)))
print('enumerate(iterable 자료형) : ') # (인덱스, 값)으로 이루어진 enumerate 객체를 리턴한다.
print('enumerate의 튜플형 변환 : ', tuple(enumerate(['name', 'age', 'height'])))
print('enumerate의 리스트형 변환 : ', list(enumerate(['name', 'age', 'height'])))
print('이들을 하나씩 출력한다면')
for i, value in enumerate(['name', 'age', 'height']):
    print(i, value)


animals = ["eagle", "fox", "frog", "tiger"]
def isStartWithF(x):
    return x.startswith('f')
results = list(filter(isStartWithF, animals))
# - results = list(filter(lambda x:x.startswith('f'), animals)) # filter 사용시
# - results = [x for x in animals if isStartWithF(x)] # list comprehension 사용시
print(results)

'''
if문
if x > 0 :
    value = 10
else : 
    value = 20
을 한 줄로,
-> value = 10 if x > 0 else 20 # 조건을 만족하면 10, 아니면 20을 반환한다.
'''
print('if 문 : ', 10 if 10 < 0 else 30)

for i in animals:
    print('i = ', i)

