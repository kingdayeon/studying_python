fruit=['strawberry','banana','orange','pineapple','cherry','mango','blueberry']
vowel = ['a','e','i','o','u']
flist = []
for fname in fruit:
 cnt = 0
 for f in fname:
 if f in vowel:
 cnt = cnt+1
 if cnt >= 3:
 flist.append([fname,cnt])
print('모음이 3개 이상인 과일:',flist)
