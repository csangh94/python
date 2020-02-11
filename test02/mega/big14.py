from tkinter import messagebox

messagebox.showinfo("안녕하세요","홍길동이요")
messagebox.showwarning("지금은 오후예요!!", "졸음 주의!!!")
q = messagebox.askquestion("시간체크","지금은 오후인가요??")
print(q)