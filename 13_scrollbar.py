

from tkinter import *


root = Tk()
root.title("nado GUI")
root.geometry("320x240")

# 스크롤바는 스크롤바와 대상이 되는 위젯을 하나의 프레임 안에 넣어두는것이 편하다.
frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y")
# fill y -> y축으로 확장시켜 더 이쁘게 보이도록


# set이 없으면 스크롤을 내려도 다시 올라온다.
listbox = Listbox(frame, selectmode="extended",
                  height=10, yscrollcommand=scrollbar.set)
for i in range(1, 32):
    listbox.insert(END, str(i)+"일")

listbox.pack(side="left")

# 리스트박스와 스크롤바 매핑
scrollbar.config(command=listbox.yview)

root.mainloop()  # 창이 닫히지 않도록
