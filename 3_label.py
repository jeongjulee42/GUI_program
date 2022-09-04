import os


import imghdr
from tkinter import *


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


root = Tk()
root.title("nado GUI")  # 프로그램 상단에 이름
root.geometry("640x480")

# 레이블은 글자나 이미지를 보여주는것이다.
label1 = Label(root, text="hello")
label1.pack()

photo = PhotoImage(file=resource_path("image.png"))
label2 = Label(root, image=photo)
label2.pack()

# 버튼을 눌렀을때 레이블값 바꾸기


# def change():
#     label1.config(text="meet soon")
#     photo2 = PhotoImage(file="img2.png")
#     label2.config(image=photo2)
# 이렇게 하면 garbage Collection이 전역변수가 아닌것들을 주워서 폐기한다
# 따라서 photo2 = PhotoImage(file="img2.png") 를 global로 바꾸어준다.
def change():
    label1.config(text="meet soon")
    global photo2
    photo2 = PhotoImage(file=resource_path("img2.png"))
    label2.config(image=photo2)


btn = Button(root, text="click", command=change)
btn.pack()


root.mainloop()  # 창이 닫히지 않도록
