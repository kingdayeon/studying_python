def isSign(C):
 F = 9.0 / 5.0*C + 32.0
 return F
cc = int(input('섭씨 온도 입력: '))
ff = isSign(cc)
print('화씨 온도는 %.1f도 입니다.' %ff)
