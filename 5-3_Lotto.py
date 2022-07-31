import random
i=0
alist = []
blist = alist
while i < 6:
 n = random.randint(1,45) #난 이 범위 안적음..
 if n not in alist: ##True 안써도 됨?? 쓰려면 괄호 있어야함!! 안써도 된대~
 alist.append(n)
 i = i+1 ##없으면 증가 들여쓰기 조심해~~~
print(alist)
print(blist) ##오이것도 가능.. 서로 연동 삭제하면 서로서로 삭제됨
