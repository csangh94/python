# 기본 입력

name = input("이름 입력 >>>")
age = int(input("나이 입력 >>"))

# 처리...
total = '이름 :'+name +','+'나이 : '+str(age)+"세"
year = 2020 - age
if year % 2 == 0:
    # 들여쓰기, indent
    print("태어난 연도가 짝수입니다.")
else:
    print("태어난 연도가 홀수입니다.")

# 기본 출력
print("최종 결과>>"+total)
print("태어난 연도는 >>"+str(year))
print("태어난 연도는 >>",year)