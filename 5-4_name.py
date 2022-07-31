i=0
nameList = []
print('이름 10개 입력: ')
while i < 10:
 name = input()
 nameList.append(name)
 i = i+1
find = input('찾고자 하는 이름을 입력하세요: ')
i=0
while i < 10:
 if(find==nameList[i]):
 print('%s는 %d번째 위치에 있습니다.' %(find,i)) ##중간에 , 쓰면 안돼ㅠㅠ #while문 안에 
 what = 1
 break
 else:
 what = 0
 i = i+1
 
if what == 0:
 print('이름이 리스트에 없습니다.')
