def selectMenu():
 print('1. 상품 추가')
 print('2. 상품 검색')
 print('3. 삭제하기')
 print('4. 변경하기')
 print('0. 프로그램 종료')
  while True:
     select = input('메뉴를 선택하세요')
     if '0' <= select <= '4': ##int아님
       return int(select)
 
def appendItem(iList):
 global count
 print()
 item = input('상품명 입력: ')
 quantity = int(input('수량입력: '))
 iList.append([item,quantity])
 count = count + 1
 return

def searchItem():
 for item in itemList:
   if item[0] == srchitem:
   return item[1] ##가격 리턴
 return -1 ##없으면 -1리턴

def printItem():
 print('현재 총',count,'개의 상품이 있습니다.')
 print('현재 상품 재고량:',itemList,'\n')
 return

def updateManager(name):
 manager = name ##manager이름으로 바꿔줘
 print()
 print(manager,'님으로 관리자가 변경되었습니다.')
 return

def deletename(dname): ##여기서 dname은 리스트가아님
 for item in itemList:
  if item[0] == dname:
     itemList.remove(item)
     global count
     count = count - 1
     return True ##return True의 위치가 앞으로 가 있었음.. 이럼 실행이 안돼
 
 return False ## 다 뒤졌는데 없을 경우
 
def updateItem(uname,ucnt):
 for item in itemList:
  if item[0] == uname:
     item[1] = ucnt
     return True ##가격 리턴
return False

itemList = []
count = 0
manager = input('관리자의 이름을 입력: ')

while True:
 menu = selectMenu()
 if menu == 0:
  break
  
 elif menu == 1:
   appendItem(itemList)
   print('추가되었습니다.\n')
   printItem()
 
 elif menu == 2:
  srchitem = input('\n검색할 상품명 입력: ')
   n = searchItem()
   if n >= 0:
     print(srchitem,'의 재고량은',n,'입니다\n')
   else:
     print('상품명이 없습니다.')
 
 elif menu == 3:
   deleteItem = input('\n삭제할 상품명 입력: ')
   k=deletename(deleteItem)
 
   if k==True:
    print('삭제되었습니다.')
   else:
     print('상품명이 없습니다.')
  printItem()
 
 else:
  changeName = input('\n변경할 상품명 입력: ')
   changeNum = int(input('\n변경수량 입력: '))
   k = updateItem(changeName,changeNum)
 
   if k == True:
    print('변경되었습니다.')
   else:
    print('상품명이 없습니다.')
  printItem()
 
updateManager('홍길동')
