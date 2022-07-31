import time
a = 10
while a >= 1:
 print('%d ' %(a) ,end='') #쓸 거 다 쓰고 ,end=''은 마지막에!
 a = a-1
 time.sleep(1)
print ('발사!')
