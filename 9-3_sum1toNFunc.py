def sum1toN(n):
 if n <= 1:
 return 1 ##그냥 return이 아니라 return 1임
 else:
 return n + sum1toN(n-1) ##나는 if else로 안 짬..
 
num1 = int(input('정수 입력: '))
print('%d부터 %d까지의 합은 %d입니다.' %(1,num,sum1toN(num1)))
