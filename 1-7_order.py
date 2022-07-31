name = input('주문자 이름: ')
product = input('상품명: ')
danga = int(input('단가: '))
amount = int(input('수량: '))
buga_luul = float(input('부가세율: '))
money = danga * amount
buga = money * buga_luul
chong = money + buga
print()
print()
print('------주문계산서------')
print('주문자 이름: %s' %(name))
print('주문금액: %d원' %(money))
print('부가세(세율(%.1f)) : %d원' %(buga_luul,buga))
print('주문 총 금액: %d원' %(chong))
