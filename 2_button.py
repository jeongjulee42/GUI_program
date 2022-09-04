from tkinter import *
from tkmacosx import Button
# from tkmacosx import Button -  맥에서 bg 넣으려면 써야함


root = Tk()
root.title("nado GUI")  # 프로그램 상단에 이름

# 새로운 버튼 만들기
btn1 = Button(root, text="button1")
btn1.pack()  # 이것을 호출해줘야 보인다

# padx - 버튼 크기 키우기 pady- 상하를 조절  -  여백!
btn2 = Button(root, padx=5, pady=10, text="btn222222222222")
btn2.pack()
# 글자에 따라 크기가 달라진다

btn3 = Button(root, padx=10, pady=5, text="btn3")
btn3.pack()

btn4 = Button(root, width=10, height=3,
              text="btn4444444444444")  # 버튼 크기 자체를 설정
btn4.pack()
# 고정크기 이므로 글자에 따라 크기가 변하지 않는다.

btn5 = Button(root, fg="red", bg="blue", text="btn5")  # 글자색, 배경색
btn5.pack()

# 이미지를 통해 버튼 만들기
photo = PhotoImage(file="img2.png")  # 파일에 있는것을 불러와 이미지로 저장하는 방법.
btn6 = Button(root, image=photo)
btn6.pack()

# 클릭시 동작하도록
# 버튼을 누르면 command에 따른 동작이 실행된다.


def btn():
    print("pressed button")


btn7 = Button(root, text="work", command=btn)
btn7.pack()

root.mainloop()  # 창이 닫히지 않도록
