import random

# print(random.randint(0,10)) # 0~10
# print(random.randrange(0,10)) # 0~9
# print(random.choice(['가위','바위','보'])) # 리스트 중 랜덤
person = []
random.seed(100)
for y in range(0,10000):
    person1 =[]
    for x in range(0,5):
        person1.append(random.randint(50,100))
    person.append(person1)
print(person1)
print(len(person))
print(person[0][0])
sum=0
for x in person:
   sum=sum+x[0]

print("국어점수의 합>>",sum)
print("국어점수 평균>>",sum/len(person))

#
# file = open("total.txt", 'w')    # writer 쓰기모드
# for x in person:
#     file.write(str(x))
#     file.write('\n')

file2 = open('total.txt', 'r') #read 읽기모드
# print(len(file2.readlines()))
sum1=0
for x in range(0,10000):
    row = file2.readline()
    sp = row.split('[')
    sp1 = sp[1].split(']')
    sp2 = sp1[0].split(',')
    sum1=sum1+int(sp2[4])
print(sum1/10000)
print(sum1)



