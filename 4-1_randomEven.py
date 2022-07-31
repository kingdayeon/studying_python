import random #import.random 아님
cnt = 0
a=0
print('발생된 난수: ',end='')
while a<3:
 num = random.randint(1,10)
 print(num,end=' ')
 if (num%2 == 0):
 cnt = cnt + 1
 a = a+1
print()
print('짝수는 %d 개입니다.' %cnt)
