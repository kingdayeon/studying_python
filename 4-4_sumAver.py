num = 0
sum = 0
n=0
while n != '입력끝': #cnt가 아니라 n 써
 n = input('정수 입력: ')
 
 if n != '입력끝':
 num = num + 1 #입력끝 개수는 세면 안돼~
 sum = sum + int(n)
aver = sum / num
print('합계는 %d 이고, 평균은 %.1f입니다.' %(sum,aver))
