# 라디오 버튼 - 여러개중 택 1. 여러개는 한묶음이 되어야 하므로, variable은 하나의 변수를 공유하도록 한다.
# 사지선다같은것.

from tkinter import *
from tokenize import String

root = Tk()  # root 는 메인 창을 말함(ex - window ,,,)
root.title("nado GUI")  # 프로그램 상단에 이름
root.geometry("320x240")

# label1 = Label(root, text=":menu").pack()  # 가능
Label(root, text=":menu").pack()  # 가능


burger_var = IntVar()  # int형 값을 저장
btn_burger1 = Radiobutton(root, text="hamburger", value=1, variable=burger_var)
btn_burger2 = Radiobutton(root, text="cheese hamburger",
                          value=2, variable=burger_var)
btn_burger3 = Radiobutton(root, text="chicken hamburger",
                          value=3, variable=burger_var)

# 기본적으로 버거1을 선택
btn_burger1.select()

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()


Label(root, text=":음료").pack()
drink_var = StringVar()
btn_drink1 = Radiobutton(root, text="coke", value="coke", variable=drink_var)
btn_drink2 = Radiobutton(root, text="cider", value="cider", variable=drink_var)


btn_drink1.pack()
btn_drink2.pack()


# 선택한 값을 가져오기


def btncmd():
    print(burger_var.get())  # 선택된 라디오 항목의 value 반환
    print(drink_var.get())


btn = Button(root, text="click", command=btncmd)
btn.pack()

root.mainloop()  # 창이 닫히지 않도록
