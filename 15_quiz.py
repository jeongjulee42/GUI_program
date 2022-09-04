# tkinter를 이용한 메모장 만들기

# 1. title - 제목 없음 - Windows 메모장
# 2. 메뉴: 파일, 편집, 서식, 보기, 도움말
# 3. 실제 메뉴 구현: 파일 메뉴 내에서 열기, 저장, 끝내기 3개만 처리
# 3-1. 열기 : mynote.txt 파일 내용 열어서 보여주기
# 3-2. 저장 :  mynote.txt 파일에 현재 내용 저장하기
# 3-3. 끝내기 : 프로그램 종료
# 4. 프로그램 시작 시 본문은 비어 있는 상태
# 5. 하단 status 바는 필요 없음
# 6. 프로그램 크기, 위치는 자유롭게 하되, 크기 조정이 가능해야 한다.
# 7. 본문 우측에 상하 스크롤바 넣기


from fileinput import filename
from tkinter import *
import os

root = Tk()
root.title("제목 없음 - Windows 메모장")
root.geometry("640x480+300+100")

menu = Menu(root)
root.config(menu=menu)


file_name = "mynote.txt"


def open_file():
    # 파일이 있는지 먼저 체크
    if os.path.isfile(file_name):  # 있으면 true, 없으면 false
        with open(file_name, "r", encoding="utf8") as file:
            txt.delete("1.0", END)
            txt.insert(END, file.read())


def save_file():
    with open(file_name, "w", encoding="utf8") as file:
        file.write(txt.get("1.0", END))


menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="열기", command=open_file)
menu_file.add_command(label="저장", command=save_file)
menu_file.add_separator()
menu_file.add_command(label="끝내가", command=root.quit)
menu.add_cascade(label="파일(F)", menu=menu_file)

menu_edit = Menu(menu, tearoff=0)
menu.add_cascade(label="편집(E)", menu=menu_edit)
menu_s = Menu(menu, tearoff=0)
menu.add_cascade(label="서식(O)", menu=menu_s)
menu_view = Menu(menu, tearoff=0)
menu.add_cascade(label="보기(V)", menu=menu_view)
menu_help = Menu(menu, tearoff=0)
menu.add_cascade(label="도움말", menu=menu_help)


scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")

txt = Text(root, yscrollcommand=scrollbar.set)
txt.pack(side="left", fill="both", expand=True)

scrollbar.config(command=txt.yview)

root.mainloop()  # 창이 닫히지 않도록
