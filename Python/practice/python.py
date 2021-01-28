''' 입력 '''
# num = input() # 문자열로 입력 받음
# num = int(input()) # 정수로 입력받음
# num1, num2 = input().split() # 공백으로 나누어서 입력받음
# num1, num2 = int(input().split()) # cf, 오류발생함.

''' map함수
- 여러개의 데이터에 같은 연산을 한번에 진행시킴
- map(변환 함수, 순회 가능한 데이터)의 형식을 가짐

형식 1 : map(int, input().split())
- num1, num2 = map(int, input('입력').split())
- a = list(map(int, input().split())) # 리스트 입력받기


'''
def conver_to_name(user):
    first, last = user["name"].split()
    return {"first": first, "last": last}

users = [
    {'mail': 'gregorythomas@gmail.com', 'name': 'Brett Holland', 'sex': 'M'},
    {'mail': 'hintoncynthia@hotmail.com', 'name': 'Madison Martinez', 'sex': 'F'},
    {'mail': 'wwagner@gmail.com', 'name': 'Michael Jenkins', 'sex': 'M'},
    {'mail': 'daniel79@gmail.com', 'name': 'Karen Rodriguez', 'sex': 'F'},
    {'mail': 'ujackson@gmail.com', 'name': 'Amber Rhodes', 'sex': 'F'}
]

a = []
for name in map(conver_to_name, users):
    a.append(name)
print(a)
print("="*50)
'''
lambda
- 런타임에서 생성하여 사용할 수 있는 익명함수
형식 : lambda '매개변수' : 식

ex)
plus_ten = lambda x : x+10
plus_ten(1) -> 11
'''
'''for mail in map(lambda u: "남" if u["sex"]=="M" else "여", users): 
    print(mail)

foo = [2,18,9,22,7,24,8,12,27]
print(list(filter(lambda x: x%3==0, foo)))
'''
print("남" if 1==0 else "여")