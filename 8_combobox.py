# 창을 열어 여러 목록중 하나를 선택
# import tkinter.ttk as ttk 해줘야 한다.

from tkinter import *
import tkinter.ttk as ttk

root = Tk()  # root 는 메인 창을 말함(ex - window ,,,)
root.title("nado GUI")  # 프로그램 상단에 이름
root.geometry("320x240")

values = [str(i) + "일" for i in range(1, 32)]
combobox = ttk.Combobox(root, height=5, values=values)
combobox.pack()
combobox.set("카드 결제일")  # 최초 목록 제목 설정, 버튼 클릭을 통한 값 설정도 가능

# 값입력 못하도록 설정 바꾸기
combobox2 = ttk.Combobox(root, height=10, values=values,
                         state="readonly")  # 읽기 전용
combobox2.current(0)  # 0번째 인덱스값 선택
combobox2.pack()

# height 목록 개수 설정하는것.


def btncmd():
    print(combobox.get())  # 선택된 값 출력


btn = Button(root, text="선택", command=btncmd)
btn.pack()

root.mainloop()  # 창이 닫히지 않도록
