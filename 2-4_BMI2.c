print('체중(kg)을 입력하세요.')
kg = float(input())
print('신장(m)을 입력하세요.')
m = float(input())
bmi = kg / m**2
if bmi < 18.5:
 what = '저체중'
elif 18.5 <= bmi < 23:
 what = '정상체중'
elif 23 <= bmi < 25:
 what = '과체중'
else:
 what = '고도비만'
 
print('BMI점수는 %.1f 로 %s입니다.' %(bmi, what))
