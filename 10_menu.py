#

from tkinter import *


root = Tk()  # root 는 메인 창을 말함(ex - window ,,,)
root.title("nado GUI")  # 프로그램 상단에 이름
root.geometry("320x240")


def create_new_file():
    print("create new file")


menu = Menu(root)
root.config(menu=menu)  # 루트에 포함하기

# file menu
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="New File", command=create_new_file)
menu_file.add_command(label="New Window")
menu_file.add_separator()
menu_file.add_command(label="Open File...")
menu_file.add_separator()

# disable 된 메뉴, 비활성화
menu_file.add_command(label="Save All", state="disable")
menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit)  # root.quit - 바로 종료

menu.add_cascade(label="File", menu=menu_file)  # 큰 메뉴에 집어 넣기

# edit menu
menu.add_cascade(label="Edit", menu=menu_file)

# 메뉴에 라디오 버튼 넣기
# language menu - radio 버튼을 통해 택 1을 추가
menu_lang = Menu(menu, tearoff=0)
menu_lang.add_radiobutton(label="Python")
menu_lang.add_radiobutton(label="Java")
menu_lang.add_radiobutton(label="C++")
menu.add_cascade(label="Language", menu=menu_lang)

# checkBox
# view menu
menu_view = Menu(menu, tearoff=0)
menu_view.add_checkbutton(label="이동 경로 표시")
menu.add_cascade(label="View", menu=menu_view)


root.mainloop()  # 창이 닫히지 않도록
