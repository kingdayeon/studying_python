n = int(input('요금을 입력하세요: ')) 
c = 1
d = 50000
while d >= 10:
 k = n // d ##몫!!
 print('%5d원: %d개' %(d,k)) ##오른쪽 정렬
 n = n % d
 if c % 2 ==0:
 d = d // 2
 else:
 d = d // 5
 c = c + 1
