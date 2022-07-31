import random
alist = list()
for i in range(100):
 alist.append(random.randint(1,1000))
 
minv = alist[0]
maxv = alist[0]
for i in range(100):
 if minv > alist[i]:
 minv = alist[i]
 if maxv < alist[i]: ##elif로 하면 안돼~ 별개야~
 maxv = alist[i]
 
print(minv,maxv)
