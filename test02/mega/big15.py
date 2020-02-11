from tkinter import messagebox

a = input("이름을 입력하세요. :")
b = input("관심사를 입력하세요. :")
messagebox.showinfo('확인',a+','+b)


if b=='파이썬':
    messagebox.showinfo('결과','프로그래머가 되실 거군요')
else:
    messagebox.showinfo('결과','데이터 분석가가 되실 거군요')


r=messagebox.askquestion("파이썬이","확실한가요?")

if r=='yes':
    messagebox.showinfo('답안','열심히하세요!')
else:
    messagebox.showinfo('답안','그럼 생각중이시군요!')