name = input('이름 입력:')
score = int(input('필기점수 입력: '))
sScore = int(input('실기접수 입력: '))
total = score + sScore
aver = total / 2
print('-'*40)
print('이름\t필기\t실기\t총점\t평균')
print('%s\t%d\t%d\t%d\t%.1f' %(name,score,sScore,total,aver)) #\t는 양옆에 띄워쓰기 안 함!
print('-'*40)
