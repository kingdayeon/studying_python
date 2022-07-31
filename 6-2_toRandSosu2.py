import random
N = random.randint(1,100)
print('발생된 난수: ',N)
k=0
for n in range(1,N+1):
 c=0
 for i in range(1,n+1):
 if n%i == 0:
 c=c+1
 
 if c == 2: ##소수는 1과 자기 자신
 print(n,end=' ')
 k = k+1 ##소수의 개수
print()
print('총 %d개의 소수가 있습니다.' %k)
