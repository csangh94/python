# 콜렉션의 4가지
# 리스트, 튜플, 딕셔너리, 셋(set)

# person = ('홍길동', 100, 'mega') => row (레코드) - DB의 1row 를 튜플이라고도 한다.
# 튜플 , 리스트 는 인덱싱을 가진다. != set은 인덱싱이 없다.

person = ('홍길동', 100, 'mega')
print(person[0])

person2 = list(person)
person2[0] = '김길동'
print(person2)
a=tuple(person2)    # 다시 튜플로 전환
print(type(a))  # 타입 확인
a1 = set(a)
print(type(a1))


food = {1,1,1,1,1,2,2,2,2,2,3,3,3,3,4,4,4,4,5,5,6}
num = set()
food2 = [1,1,1,1,1,2,2,2,2,2,3,3,3,3,4,4,4,4,5,5,6]
food.add(2)
food.add(5)
food.add(7)
food.add(2)
num.add(5)
print(food)
print(set(food2))
print(num)


me = dict()
me['name'] = 'hong'
me['age'] = '100'
me['company'] = 'mega'
print('이름은 ',me['name'])
print(me)

for x in me: # 딕셔너리 for문 시 x는 key!역할
    print(me[x])
