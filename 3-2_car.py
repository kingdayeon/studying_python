kind = int(input('응시 종류 입력하시오: '))
score = int(input('점수를 입력하시오: '))
if((kind == 1 and score >= 70) or (kind == 2 and score >= 60)):
 print('당신은 %d종 면허에 합격했습니다.' %(kind))
else:
 print('당신은 %d종 면허에 불합격했습니다.' %(kind)
