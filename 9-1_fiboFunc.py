def fibo(n):
 if n<= 2:
  return 1
 else:
  return fibo(n-1)+fibo(n-2)
num = int(input('항 입력: '))
print(num,'번째 항의 값은',fibo(num),'입니다.')
