num = int(input('정수를 입력하세요. '))
print('천의 자리수: %d' %(num/1000))
print('백의 자리수: %d' %(num%1000/100))
print('십의 자리수: %d' %(num%100/10))
print('일의 자리수: %d' %(num%10))