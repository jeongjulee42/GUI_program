# 에러가 떴을때 팝업으로 뜨는것.

from tkinter import *
import tkinter.messagebox as msgbox


root = Tk()  # root 는 메인 창을 말함(ex - window ,,,)
root.title("nado GUI")  # 프로그램 상단에 이름
root.geometry("320x240")

# 기차 예매 시스템


def info():
    msgbox.showinfo("알림", "정상적으로 예매 완료")  # 첫번째꺼는 타이틀, 두번쨰꺼는 팝업창 메시지


def warn():
    msgbox.showwarning("warning2", "매진")


def err():
    msgbox.showerror("err2", "error rising")


def okcancel():  # 사용자에게 물어보기
    msgbox.askokcancel("확인/ 취소", "예매할래?")


def retrycancel():
    msgbox.askretrycancel("재시도/ 취소", "다시할래?")


def yesno():
    msgbox.askyesno("yes or no", "YES / NO")


def yesnocancel():
    reponse = msgbox.askyesnocancel(title=None, message="YES / NO / CANCEL")
    # yes - save & quit     ->true , 1
    # no - no save & quit   ->false , 0
    # cancel - 현재 화면 대기  ->none   , 그외
    print(reponse)  # true, false, none
    if reponse == 1:
        print("예")
    elif reponse == 0:
        print("아니오")
    else:
        print("취소")


Button(root, command=info, text="alarm").pack()
Button(root, command=warn, text="warning").pack()
Button(root, command=err, text="error").pack()

Button(root, command=okcancel, text="확인취소").pack()
Button(root, command=retrycancel, text="재시도 취소").pack()
Button(root, command=yesno, text="yes or no").pack()
Button(root, command=yesnocancel, text="yes or no").pack()


root.mainloop()  # 창이 닫히지 않도록
