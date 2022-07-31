import random
i=0
alist = []
while i < 10:
 n = random.randint(1,100) #난 이 범위 안적음..
 alist.append(n)
 i = i+1
 
print(alist)
i=1 ##자기자신이랑 비교할필요 없으니까 0보단 1로
#max = 0 ##다 음수인 경우 있을 수 있으니까...초깃값을 list의 0번째 값으로 주는 게 좋아
max = alist[0]
maxPosition = 0 ##이거 꼭 0으로 초깃값을 줘야한대 없으면 오류날수도? 
while i < len(alist):
 if max < alist[i]:
 max = alist[i]
 maxPosition = i
 i = i+1
print(max, maxPosition)
i=1 ##자기자신이랑 비교할필요 없으니까 0보단 1로
#min = 0 ##다 음수인 경우 있을 수 있으니까...초깃값을 list의 0번째 값으로 주는 게 좋아
min = alist[0]
minPosition = 0
while i < len(alist):
 if min > alist[i]:
 min = alist[i]
 minPosition = i
 i = i+1
print(min, minPosition)
##max min 하나의 while문에 써도 괜츈 이때는 if if 이 구조로 쓰면 됨
##sort랑 index함수 써도 될듯~
##max라는 함수도 따로 있대
## maxValue = max(alist)
##maxPosition = alist.index(maxValue)
## print(maxValue,maxPosition)
