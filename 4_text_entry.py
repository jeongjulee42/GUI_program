
from tkinter import *
# 텍스트 위젯 만들기 - 글자 입력을 가능하도록 한다.
root = Tk()  # root 는 메인 창을 말함(ex - window ,,,)
root.title("nado GUI")  # 프로그램 상단에 이름

txt = Text(root, width=30, height=5)
txt.pack()

# 기본으로 글자 넣어두기/ end는 위치
txt.insert(END, "put text")

# entry
e = Entry(root, width=30)
e.pack()
# entry는 줄바꿈이 불가능, 아이디, 패스워드같은거 입력받을때 사용, 텍스트는 여러줄 입력받을때 사용
e.insert(0, "한줄만 입력")
# 현재 값이 비어있으므로 end를 써도 0과 동일
# 0 - 처음 위치에 기본값이 들어간다.


# 버튼 클릭시 글자를 가져오고 지워보기
def btncmd():
    # 내용 출력
    print(txt.get("1.0", END))
    # 처음부터 끝까지의 모든 텍스트 내용을 가져오라는 뜻
    # 1.0 - 1-line1부터, 0-column기준으로 0번째 위치에서부터 가져오라는것.
    print(e.get())
    # 엔트리는 get이라고만 적어주면 된다.

    # 내용 삭제
    txt.delete("1.0", END)
    e.delete(0, END)


btn = Button(root, text="click", command=btncmd)
btn.pack()

root.mainloop()  # 창이 닫히지 않도록
