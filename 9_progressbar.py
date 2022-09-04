# 다운로드같은데서 사용. 00% .... 진행상태를 표시 ,ttk 필요

from tkinter import *
import tkinter.ttk as ttk
import time

root = Tk()  # root 는 메인 창을 말함(ex - window ,,,)
root.title("nado GUI")  # 프로그램 상단에 이름
root.geometry("320x240")

# # progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate") # 언제 끝날지 모름
# progressbar = ttk(root, maximum=100, mode="determinate")
# progressbar.start(10)  # 프로그레스바 실행, 10ms 마다 움직임
# progressbar.pack().Progressbar


# def btncmd():
#     progressbar.stop()  # 작동 중지


# btn = Button(root, text="중지", command=btncmd)
# btn.pack()
p_var2 = DoubleVar()  # 퍼센테이지이므로 double
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)


def btncmd2():
    for i in range(1, 101):
        time.sleep(0.01)  # 0.01delay

        p_var2.set(i)  # 1~100
        # 여기까지만 하면 한번에 실행된다.
        # 따라서 매 동작시마다 gui에 반영을 해주는 코드를 만들어야 한다.
        progressbar2.update()
        print(p_var2.get())


btn = Button(root, text="start", command=btncmd2)
btn.pack()

progressbar2.pack()

root.mainloop()  # 창이 닫히지 않도록
