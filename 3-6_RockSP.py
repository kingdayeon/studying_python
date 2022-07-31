import random
per1Choose = random.randint(1,3)
per2Choose = random.randint(1,3)
per3Choose = random.randint(1,3)
#사람 1의 숫자에 따른 가위, 바위, 보 배분
if per1Choose == 1:
 per1Hand = '가위'#==가 아니라 =임!! 조심하자!!
elif per1Choose == 2:
 per1Hand = '바위'
else:
 per1Hand = '보'
#사람 2의 숫자에 따른 가위, 바위, 보 배분
if per2Choose == 1:
 per2Hand = '가위'
elif per2Choose == 2:
 per2Hand = '바위'
else:
 per2Hand = '보'
 
#사람 3의 숫자에 따른 가위, 바위, 보 배분
if per3Choose == 1:
 per3Hand = '가위'
elif per3Choose == 2:
 per3Hand = '바위'
else:
 per3Hand = '보'
 
print('참가자1 : %s' %(per1Hand)) 
print('참가자2 : %s' %(per2Hand)) 
print('참가자3 : %s' %(per3Hand)) 
print() 
#참가자 세 명이 모두 다른 것이 선택된 경우
if(per1Hand != per2Hand and per2Hand != per3Hand and per3Hand != per1Hand):
 print('비겼다.')
#참가자 세 명이 모두 같은 것이 선택된 경우
if(per1Hand == per2Hand and per2Hand == per3Hand and per3Hand == per1Hand):
 print('비겼다.')
#참가자 두 명이 같은 것이 선택된 경우
elif((per1Hand == '가위' and per2Hand == '가위' and per3Hand == '보')
 or(per1Hand == '바위' and per2Hand == '바위' and per3Hand == '가위')
 or(per1Hand == '보' and per2Hand == '보' and per3Hand == '바위')):
 winner = '참가자 1 참가자 2'
 print('승자: %s' %(winner))
 
elif((per1Hand == '보' and per2Hand == '가위' and per3Hand == '가위')
 or(per1Hand == '가위' and per2Hand == '바위' and per3Hand == '바위')
 or(per1Hand == '바위' and per2Hand == '보' and per3Hand == '보')):
 winner = '참가자 2 참가자 3'
 print('승자: %s' %(winner))
elif((per1Hand == '가위' and per2Hand == '보' and per3Hand == '가위')
 or(per1Hand == '바위' and per2Hand == '가위' and per3Hand == '바위')
 or(per1Hand == '보' and per2Hand == '바위' and per3Hand == '보')):
 winner = '참가자 1 참가자 3'
 print('승자: %s' %(winner))
 
#참가자 한 명이 다른 두 명을 이길 경우
elif((per1Hand == '가위' and per2Hand == '보' and per3Hand == '보')
 or(per1Hand == '바위' and per2Hand == '가위' and per3Hand == '가위')
 or(per1Hand == '보' and per2Hand == '바위' and per3Hand == '바위')):
 winner = '참가자 1'
 print('승자: %s' %(winner))
 
elif((per1Hand == '보' and per2Hand == '가위' and per3Hand == '보')
 or(per1Hand == '가위' and per2Hand == '바위' and per3Hand == '가위')
 or(per1Hand == '바위' and per2Hand == '보' and per3Hand == '바위')):
 winner = '참가자 2'
 print('승자: %s' %(winner))
elif((per1Hand == '보' and per2Hand == '보' and per3Hand == '가위')
 or(per1Hand == '가위' and per2Hand == '가위' and per3Hand == '바위')
 or(per1Hand == '바위' and per2Hand == '바위' and per3Hand == '보')):
 winner = '참가자 3'
 print('승자: %s' %(winner))
