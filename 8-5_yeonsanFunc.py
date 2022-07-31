def add(a,b):
 return a+b
def subtract(a,b):
 return a-b
def multiply(a,b):
 return a*b
def divide(a,b):
 return a//b
first = float(input('첫 번째 수 입력: '))
second = float(input('두 번째 수 입력: '))
yeonsanja = input('연산자 입력: ')
if yeonsanja == '+': ## +가 아니라 '+'임
 result = add(first,second)
elif yeonsanja == '-':
 result = subtract(first,second)
elif yeonsanja == '*':
 result = multiply(first,second)
elif yeonsanja == '//':
 result = divide(first,second)
print()
print('%.1f %s %.1f = %.2f' %(first,yeonsanja,second,result))
