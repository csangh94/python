import random

a = random.randint(0,100)
random.seed(50)
while True:
    a1 = int(input("숫자 입력>>"))
    if a1 == a:
        print("정답입니다. ",a1)
        break
    elif a1 > a:
        print("숫자가 큽니다.")
    elif a1 < a:
        print("숫자가 작습니다.")

