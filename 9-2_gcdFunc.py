##유클리드 호제법 이용

def gcd(x,y):
 r = x % y
 
 if r == 0:
   return y
 else:
   return gcd(y,r)
 
num1 = int(input('첫번째 정수'))
num2 = int(input('두번째 정수'))
if num1 < num2:
 num1,num2 = num2,num1
print('%d와 %d의 최대공약수는 %d입니다.' %(num1, num2, gcd(num1,num2)))
