# company = ('홍길동','김길동','박길동','송길동','마길동')
company= []
for x in range(0,5):
    company.append(input("이름 입력 >>"))
print(company)

company2 = list(company)
company2[0] = '김다인'
print(company2)

목록 = []
수강신청1 = dict()
수강신청2 = dict()
수강신청3 = dict()
수강신청1['수강자ID'] ='100'
수강신청1['수강과목'] ='파이썬'
수강신청1['강의실'] ='708호'
수강신청1['강의료'] =2000
수강신청2['수강자ID'] ='100'
수강신청2['수강과목'] ='자바'
수강신청2['강의실'] ='709호'
수강신청2['강의료'] =3000
수강신청3['수강자ID'] ='200'
수강신청3['수강과목'] ='소켓'
수강신청3['강의실'] ='709호'
수강신청3['강의료'] =5000

목록.append(수강신청1)
목록.append(수강신청2)
목록.append(수강신청3)
print("----------------------------------")
sum=0
for x in 목록:
    if x['수강자ID'] == '100':
        sum=sum+x['강의료']
print("수강ID 100의","총 수강료",sum,"원")
print("----------------------------------")
for x in 목록:
    print(x)