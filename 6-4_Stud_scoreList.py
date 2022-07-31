studlist = ['박은별;90;80','한빛나;80;70','김라영;60;70']
##s는 문자열 하나
for s in studlist:
 wlist = s.split(';')
 tot = int(wlist[1]) + int(wlist[2]) ##정수로 형변환~~!!!
 print('%s 학생의 총점은 %d입니다.' %(wlist[0],tot))


##studlist2 = [['박은별',90,80],['한빛나',80,70],['김라영',60,70]]
##s는 서브리스트
##for s in studlist2:
##tot = s[1] + s[2]
##print('%s 학생의 총점은 %d입니다.' %(s[0],tot))
