print('년도를 입력하시오.')
year = int(input())
if ((year%4==0 and year%100 != 0)or(year%400 == 0)):
 print('윤년입니다.')
else:
 print('평년입니다')
