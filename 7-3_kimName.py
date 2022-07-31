nlist=['최동수','김우빈','홍사랑','나현우','김철수','김영희'] 
#lastName == 성
lastName = input('찾고자 하는 친구의 성: ')
store = []
for i in range(len(nlist)):
 for j in range(len(nlist[i])):
 if lastName == nlist[i][0]:
 store.append(nlist[i]) ##nlist[i][j]아님!
 break ##break없으면 3번씩 출력해!!
 
print('김씨 성을 가진 친구들은',store,'입니다.')
