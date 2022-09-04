# 체크, 체크해제 등등, -> 주로 팝업창에서 사용

from tkinter import *

root = Tk()  # root 는 메인 창을 말함(ex - window ,,,)
root.title("nado GUI")  # 프로그램 상단에 이름


chkvar = IntVar()  # 여기에 int 형으로 값을 저장한다.
chkbox = Checkbutton(root, text="오늘 하루 보지 않기", variable=chkvar)
# variable 는 체크, 체크해제에 대한 값을 변수에 저장할 수 있다.
# chkbox.select()  # 자동 선택 처리
# chkbox.deselect()  # 선택 해제 처리
chkbox.pack()

chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text="일주일동안 보지 않기", variable=chkvar2)
chkbox2.pack()

# 버튼 클릭시 체크버튼 값 가져오기


def btncmd():
    print(chkvar.get())  # 0-체크 해제, 1 - 체크
    print(chkvar2.get())


btn = Button(root, text="click", command=btncmd)
btn.pack()

root.mainloop()  # 창이 닫히지 않도록
