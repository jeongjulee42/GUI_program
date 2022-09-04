from tkinter import *

root = Tk()  # root 는 메인 창을 말함(ex - window ,,,)
root.title("nado GUI")  # 프로그램 상단에 이름
# root.geometry("640x480")  # 창 크기
root.geometry("640x480+300+100")  # 창 크기 + x위치, y위치 - 컴퓨터 화면 어느 위치에 뜰지 결정

root.resizable(False, False)  # 너비, 높이 변경 불가하도록, 창 크기 변경 안됨

root.mainloop()  # 창이 닫히지 않도록
