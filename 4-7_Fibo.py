a=1
b=1
n= int(input('항의 개수를 입력: '))
print(a,b,end=' ')
k=2
while k<n:
 c=a+b
 print(c,end=' ')
 a=b
 b=c
 k = k+1
