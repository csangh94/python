a = input("스티커 값 =")                              # 스티커값(변수)
q = int(a)                                           # 저장값 정수 변환
b = input("사려는 스티커 갯수 :")
w = int(b)
c = input("책갈피 값 =")
e = int(c)
d = input("책갈피 사려는 갯수 :")
r = int(d)
t=q*w                                                # 스티커 총 더한 값 저장
y=e*                                                 # 책갈피 총 더한 값 저장
u=t+y                                                # 스티커 총 값 + 책갈피 총 값
i=u/10                                               # 총 금액의 10% 값
print("---------------------------")
print("우수회원 할인으로 10% 할인을 받았습니다.")       # "입력"
print("내가 낼 금액 = ",u-i,"원 입니다.")             # 총 금액의 10%를 제한 값


