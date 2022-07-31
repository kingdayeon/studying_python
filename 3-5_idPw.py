id = input('아이디를 입력해주세요: ')
pw = input('비밀번호를 입력해주세요: ')
if(id == 'python' and pw == 'fun'):
 print('로그인 성공입니다.')
 
elif(id != 'python'):
 print('아이디 오류입니다.')
elif(pw != 'fun'):
 print('비밀번호 오류입니다.')
