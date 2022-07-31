def genRand(start, end):
 import random
 rnd = random.randint(start,end)
 return rnd
startt = int(input('시작 값을 입력하시오: '))
endd = int(input('종료 값을 입력하시오: '))
if startt > endd:
 startt, endd = endd, startt ##밖에서 스왑해주고 함수 호출하는 게 더 간단해
result = genRand(startt,endd)
print('%d에서 %d사이의 난수 %d이 발생했습니다.' %(startt,endd,result))
