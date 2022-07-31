info=[['홍길동',20],['김영수',25]]
s=0
for n in Info:
 s = s + n[1]
print('학생들의 평균 나이는 %.1f' %(s/len(info)))
##김영수 찾기
for n in Info:
 if n[0] == '김영수':
 n[1] = 23
print('김영수 학생의 나이는',info[1][1])
name = input('이름 입력: ')
for n in Info:
 if n[0] == name:
 print('%s 학생의 나이는 %d살입니다.' %(n[0],n[1])
