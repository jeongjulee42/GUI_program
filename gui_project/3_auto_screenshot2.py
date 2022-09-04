# 개선된 스샷 프로그램

import keyboard
from PIL import ImageGrab
import time

# keyboard.add_hotkey("key", function)
# 해당 key를 입력 했을 떄 , function을 실행 한다.


def screenshot():
    curr_time = time.strftime("_%Y%m%d_%H%M%S")
    img = ImageGrab.grab()
    img.save("image{}.png".format(curr_time))


keyboard.add_hotkey("F9", screenshot)  # 사용자가 shift를 누르면 스크린샷 저장
# ctrl + shift + s 같은것도 가능

keyboard.wait("esc")  # esc를 누를때까지 이 프로그램을 계속 쓴다.
