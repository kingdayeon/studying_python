def isPrime(N):
 for i in range(2,N):
 if N%2 == 0:
  return False
 return True

num = int(input('정수 입력: '))
result = isPrime(num)
if result == True:
 print('%d은 소수입니다.' %num)
else:
 print('%d은 소수가 아닙니다.' %num)
