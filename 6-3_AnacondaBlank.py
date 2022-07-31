cnt = 0
alist = 'Anaconda solutions are serious technology for real data science and ML applications. Anacon
blank = 0
for i in range(len(alist)): 
 
 if blank == 0:
 print(alist[i],end='')
 if alist[i] == ' ':
 blank = 1
 
 elif blank == 1:
 print(alist[i].upper(),end='') ##upper은 함수라 ()붙여야돼 
 blank = 0
 
 
for a in alist:
 if a == 'a': ##왼쪽 a는 변수
 cnt = cnt+1
print()
print(cnt)
