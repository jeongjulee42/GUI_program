# 리스트 박스 -  여러줄에 걸친 목록을 관리하는 목록 위젯
from tkinter import *
# 텍스트 위젯 만들기 - 글자 입력을 가능하도록 한다.
root = Tk()  # root 는 메인 창을 말함(ex - window ,,,)
root.title("nado GUI")  # 프로그램 상단에 이름

listbox = Listbox(root, selectmode="extended", height=0)
# extended - 여러개 선택 가능
# single - 하나만 선택 가능
# height=3 -> 지정된 숫자 개수(3개)만큼만 보여준다. 즉 바나나까지 보여진다 , 밑에꺼는 방향키로 선택 가능
# 0 은 전부 보여준다.
listbox.insert(0, "apple")
listbox.insert(1, "straw")
listbox.insert(2, "banana")
listbox.insert(END, "water")
listbox.insert(END, "grape")

listbox.pack()

# 버튼 클릭시 글자를 가져오고 지워보기


def btncmd():
    # 리스트에서 맨뒤의 항목 삭제
    # listbox.delete(END)

    # 맨 처음의 항목 삭제
    # listbox.delete(0)

    # 갯수 확인
    # print(listbox.size())

    # 항목 확인
    # print("1~3:", listbox.get(0, 2))

    # 선택된 항목 확인
    print("select:", listbox.curselection())  # index값으로 출력된다.


btn = Button(root, text="click", command=btncmd)
btn.pack()

root.mainloop()  # 창이 닫히지 않도록
