# 좌표 기반 위젯 배치


from tkinter import *


root = Tk()
root.title("nado GUI")
root.geometry("320x240")

# btn1 = Button(root, text="1")
# btn2 = Button(root, text="2")

# # btn1.pack()
# # btn2.pack()

# # btn1.pack(side="left")
# # btn2.pack(side="left")

# btn1.grid(row=0, column=0)
# btn2.grid(row=1, column=1)

btn_f16 = Button(root, text="F16")
btn_f17 = Button(root, text="F17")
btn_f18 = Button(root, text="F18")
btn_f19 = Button(root, text="F19")

btn_f16.grid(row=0, column=0)
btn_f17.grid(row=0, column=1)
btn_f18.grid(row=0, column=2)
btn_f19.grid(row=0, column=3)

btn_clear = Button(root, text="clear")
btn_equal = Button(root, text="=")
btn_div = Button(root, text="/")
btn_x = Button(root, text="*")

btn_clear.grid(row=1, column=0)
btn_equal.grid(row=1, column=1)
btn_div.grid(row=1, column=2)
btn_x.grid(row=1, column=3)

btn_enter = Button(root, text="enter")  # 세로로 합치기
btn_enter.grid(row=3, column=3, rowspan=2)
root.mainloop()  # 창이 닫히지 않도록
