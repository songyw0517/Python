year=int(input(''))
if year%4==0 and year%100!=0: #윤년임
    print(1)
elif year%400==0: #윤년임
    print(1)
else:
    print(0)
