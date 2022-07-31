import random
random = random.randint(1,100)
print('발생된 난수:',random)
print('1부터 %d까지의 수 중에서 소수:'%random,end=' ')
cnt = 0
for i in range(1, random+1):
 for j in range(2, i+1):
 if (j == i):
 print(i,end=' ')
 cnt = cnt+1
 elif (i % j == 0):
 break
 
print('\n총 %d 개의 소수가 있습니다' %cnt)
