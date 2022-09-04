import tkinter.ttk as ttk
from tkinter import *
from tokenize import Double
from tkinter import filedialog
import tkinter.messagebox as msgbox
from PIL import Image
import os

root = Tk()
root.title("nado GUI")

# 파일 추가


def add_file():

    files = filedialog.askopenfilenames(title="이미지 파일을 선택하세요", filetypes=(
        ("PNG 파일", "*.png"), ("모든 파일", "*.*")), initialdir="/Users/jeongju/Desktop/coding_project/gui_basic/images")

    for file in files:
        list_file.insert(END, file)

# 선택 삭제


def del_file():
    # 삭제할때는 뒤에것부터 지워야한다. 앞에것이 먼저 지워지면 뒤에것의 index가 변하므로
    for index in reversed(list_file.curselection()):
        # reverse 는 리스트가 변한다.
        # reversed는 비파괴함수
        list_file.delete(index)

# 저장 경로(폴더를 선택)


def browse_dest_path():
    folder_selected = filedialog.askdirectory()
    if folder_selected == None:  # 사용자가 취소를 누른 경우
        return
    txt_dest_path.delete(0, END)
    txt_dest_path.insert(0, folder_selected)

# 이미지 통합


def merge_image():
    # 가로 넓이
    img_width = cmb_width.get()
    if img_width == "원본유지":
        img_width = -1  # -1일때는 원본 기준으로
    else:
        img_width = int(img_width)

    # 간격
    img_space = cmb_space.get()
    if img_space == "좁게":
        img_space = 30
    elif img_space == "보통":
        img_space = 60
    elif img_space == "넓게":
        img_space = 90
    else:  # 없음
        img_space = 0

    # 포맷
    img_format = cmb_format.get().lower()  # png, jpg, bmp값을 받아와서 소문자로 변경

    images = [Image.open(x) for x in list_file.get(0, END)]

    # 이미지 사이즈 리스트에 넣어 하나씩 처리
    image_sizes = []  # (width1, height1),(width2, height2), ...
    if img_width > -1:
        # width 값 변경
        img_sizes = [(int(img_width), int(img_width * x.size[1] / x.size[0]))
                     for x in images]
    else:
        # 원본사이즈 사용
        image_sizes = [(x.size[0], x.size[1]) for x in images]

    # 계산식
    # 100x60 이미지 -> width를 80으로 줄이면 높이는?
    # 원본 width : 원본 height = 변경 width : 변경 height
    # 원본 height x 변경 width / 원본 width =  변경 height

    # 여기도 바꿔줘야한다.
    widths, heights = zip(*(image_sizes))
    max_width, total_height = max(widths), sum(heights)

    result_img = Image.new(
        "RGB", (max_width, total_height), (255, 255, 255))  # 배경 흰색
    y_offset = 0

    for idx, img in enumerate(images):
        result_img.paste(img, (0, y_offset))
        y_offset += img.size[1]

        progress = (idx + 1) / len(images) * 100  # 실제 퍼센트 정보를 계산
        p_var.set(progress)
        progress_bar.update()

    dest_path = os.path.join(txt_dest_path.get(), "nado_photo.jpg")
    result_img.save(dest_path)
    msgbox.showinfo("알림", "작업이 완료되었습니다.")


# 시작 - 각 옵션값을 가져와야한다.
def start():
    # 각 옵션들 값을 확인

    # 파일 목록 확인
    if list_file.size() == 0:
        msgbox.showwarning("error", "이미지파일을 추가하세요")
        return
    # 저장 경로 확인
    if len(txt_dest_path.get()) == 0:  # 문자열의 길이가 0 -> 아무것도 없다.
        msgbox.showwarning("error", "저장 경로를 선택하세요")
        return

    # 이미지 통합 작업
    merge_image()


# 파일 프레임 (파일 추가, 선택 삭제)
file_frame = Frame(root)
file_frame.pack(fill="x", padx=5, pady=5)

btn_add_file = Button(file_frame, padx=5, pady=5,
                      width=12, text="파일추가", command=add_file)
btn_add_file.pack(side="left")

btn_del_file = Button(file_frame, padx=5, pady=5,
                      width=12, text="선택삭제", command=del_file)
btn_del_file.pack(side="right")

# 리스트 프레임
list_frame = Frame(root)
list_frame.pack(fill="both", padx=5, pady=5)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

list_file = Listbox(list_frame, selectmode="extended",
                    height=15, yscrollcommand=scrollbar.set)
list_file.pack(side="left", fill="both", expand=True)
scrollbar.config(command=list_file.yview)

# 저장경로 프레임
path_frame = LabelFrame(root, text="저장경로")
path_frame.pack(fill="x", padx=5, pady=5, ipady=5)

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left", fill="x", expand=True, ipady=4, padx=5, pady=5)
# fill -> x 좌우로 펼쳐지도록한다
# ipady - inner padding 으로 높이 변경
btn_dest_path = Button(path_frame, text="찾아보기",
                       width=10, command=browse_dest_path)
btn_dest_path.pack(side="right", padx=5, pady=5)


# 옵션 프레임
frame_option = LabelFrame(root, text="옵션")
frame_option.pack(padx=5, pady=5, ipady=5)

# 1 가로 넓이 옵션
# 가로넓이 레이블
lbl_width = Label(frame_option, text="가로넓이", width=8)
lbl_width.pack(side="left", padx=5, pady=5)

# 가로넓이 콤보
opt_width = ["원본유지", "1024", "800", "640"]
cmb_width = ttk.Combobox(frame_option, state="readonly",
                         values=opt_width, width=10)
cmb_width.current(0)
cmb_width.pack(side="left", padx=5, pady=5)


# 2 간격 옵션
# 간격 옵션 레이블
lbl_space = Label(frame_option, text="간격", width=8)
lbl_space.pack(side="left", padx=5, pady=5)

# 간격 옵션 콤보
opt_space = ["없음", "좁게", "보통", "넓게"]
cmb_space = ttk.Combobox(frame_option, state="readonly",
                         values=opt_space, width=10)
cmb_space.current(0)
cmb_space.pack(side="left", padx=5, pady=5)


# 3 파일 포멧 옵션
# 파일 포멧 옵션 레이블
lbl_format = Label(frame_option, text="포맷", width=8)
lbl_format.pack(side="left", padx=5, pady=5)

# 파일 포멧 옵션 콤보
opt_format = ["PNG", "JPG", "BMP"]
cmb_format = ttk.Combobox(frame_option, state="readonly",
                          values=opt_format, width=10)
cmb_format.current(0)
cmb_format.pack(side="left", padx=5, pady=5)

# 진행상황 progress Bar
frame_progress = LabelFrame(root, text="진행상황")
frame_progress.pack(fill="x", padx=5, pady=5, ipady=5)

p_var = DoubleVar()
progress_bar = ttk.Progressbar(frame_progress, maximum=100, variable=p_var)
progress_bar.pack(fill="x", padx=5, pady=5)

# 실행 프레임
frame_run = Frame(root)
frame_run.pack(fill="x", padx=5, pady=5)

btn_close = Button(frame_run, padx=5, pady=5, text="닫기",
                   width=12, command=root.quit)
btn_close.pack(side="right", padx=5, pady=5)

btn_start = Button(frame_run, padx=5, pady=5,
                   text="시작", width=12, command=start)
btn_start.pack(side="right", padx=5, pady=5)


root.resizable(False, False)
root.mainloop()
