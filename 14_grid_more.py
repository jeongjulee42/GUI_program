# 그리드 공간 넓히기 -sticky
# 버튼 내의 공간 키우기 padx, pady
# 버튼간의 간격 그리드에 padx, pady
# cmd + f 로 한번에 바꾸기
# padx, pady는 안의 글자 기준으로 여백을 줘서 살찍식 차이가 있다.
# 똑같은 크기를 부여하고싶을때는 width, height를 활용
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

btn_f16 = Button(root, text="F16", padx=10, pady=10)
btn_f17 = Button(root, text="F17", padx=10, pady=10)
btn_f18 = Button(root, text="F18", padx=10, pady=10)
btn_f19 = Button(root, text="F19", padx=10, pady=10)

btn_f16.grid(row=0, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_f17.grid(row=0, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_f18.grid(row=0, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_f19.grid(row=0, column=3, sticky=N+E+W+S, padx=3, pady=3)

btn_clear = Button(root, text="clear", padx=10, pady=10)
btn_equal = Button(root, text="=", padx=10, pady=10)
btn_div = Button(root, text="/", padx=10, pady=10)
btn_x = Button(root, text="*", padx=10, pady=10)

btn_clear.grid(row=1, column=0, sticky=W, padx=3, pady=3)
btn_equal.grid(row=1, column=1, sticky=E, padx=3, pady=3)
btn_div.grid(row=1, column=2, sticky=S, padx=3, pady=3)
btn_x.grid(row=1, column=3, sticky=N+E+W+S, padx=3, pady=3)

btn_enter = Button(root, text="enter")  # 세로로 합치기
btn_enter.grid(row=3, column=3, rowspan=2, sticky=N+E+W+S)
root.mainloop()  # 창이 닫히지 않도록
