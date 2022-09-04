

from tkinter import *
from turtle import right


root = Tk()
root.title("nado GUI")
root.geometry("320x240")

Label(root, text="select menu").pack(side="top")
Button(root, text="order").pack(side="bottom")

frame_burger = Frame(root, relief="solid", bd=1)
# relief = 테두리 정보, bd = 이게 있어야 외곽선 표시
frame_burger.pack(side="left", fill="both", expand=True)
# side - 어느쪽에 넣을지

Button(frame_burger, text="hamburger").pack()  # 프레임에 넣어주기
Button(frame_burger, text="cheese hamburger").pack()
Button(frame_burger, text="chicken hamburger").pack()

frame_drink = LabelFrame(root, text="drink")  # 제목이 있는 프레임
Button(frame_drink, text="coke").pack()
Button(frame_drink, text="cider").pack()
frame_drink.pack(side="right", fill="both", expand=True)

root.mainloop()  # 창이 닫히지 않도록
