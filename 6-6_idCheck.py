##다음은 아이디(ID)를 만드는 규칙이다. 입력받은 아이디가 규칙에 맞는 검사하는 프로그램을 작성하세요.
##알파벳 소문자(a-z)와 숫자(0-9)만 사용할 수 있다.
##반드시 1개 이상의 숫자를 포함해야 한다.
##전체 길이가 10자 이상 16자 이하가 되어야 한다.
##첫 글자는 반드시 영문자이어야 한다.

uid = input('생성할 아이디 입력: ')
check = True
if len(uid) < 10 or len(uid) > 16:
 check = False
elif not('a' <= uid[0] <= 'z'):
 check = False
 
else: ##각각의 문자
 a = 0 ##알파벳 개수
 d = 0 ##숫자 개수
 for s in uid:
 if 'a' <= s <= 'z':
 a = a+1
 elif '0' <= s <= '9': #elif블라블라: ##문자 하나가 영어면서 숫자일 수는 없으니까 elif가
 d = d+1 ##문자열에서 하나하나 가지고 오니까 문자임
 if (a+d) != len(uid) or d < 1:
 check = False
 
if check == True:
 print('아이디가 생성됨')
else:
 print('생성규칙에 맞지 않음')
