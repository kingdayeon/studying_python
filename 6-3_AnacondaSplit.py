strS = 'Anaconda solutions are serious'
wlist = strS.split() ##반복문 전에 먼저 쪼개기도 가능~ 왜냐면 strS는 그냥 문자열이니까~~~~
for w in wlist:
 print(w[0].upper(),end='')
 print(w[1:],end=' ')
 
cnt = 0 
for a in strS:
 if a == 'a':
 cnt = cnt+1
print()
print('a의 개수:',cnt) 
