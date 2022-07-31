mid = float(input('중간고사 점수를 입력해주세요: '))
final = float(input('기말고사 점수를 입력해주세요: '))
aver = (mid + final) / 2
if aver >= 90:
 print("Excellent!")
elif 80 <= aver < 90:
 print("Good!")
elif 70 <= aver < 80:
 print("Fair~")
else:
 print("See you again!")
print('평균점수는 %.1f입니다' %(aver))
