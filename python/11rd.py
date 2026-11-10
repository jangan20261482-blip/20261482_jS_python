##from tkinter import *
##window = Tk()

##btnList = [None] * 3

##for i in range(0, 3) :
    ##btnList[i] = Button(window, text = "버튼" + str(i + 1))

##for btn in btnList :
    ##btn.pack(side = TOP, fill = X, ipadx = 10, ipady = 10, padx = 10, pady = 10)

##window.mainloop()

##from tkinter import *


## 전역 변수 선언 부분 ##
##btnList = [None] * 9
##fnameList = ["로시츠키.gif", "모드리치.gif", "헛발질.gif", "훔.gif"]
             
##photoList = [None] * 9
##i, k = 0, 0
##xPos, yPos = 0, 0
##num = 0

## 메인 코드 부분 ##
##window = Tk()
#3window.geometry("210x210")

#3for i in range(0, 4) :
   ## photoList[i] = PhotoImage(file = "gif/" + fnameList[i])
    #3btnList[i] = Button(window, image = photoList[i])

#3for i in range(0, 2) :
    ##for k in range(0, 2) :
        ##btnList[num].place(x = xPos, y = yPos)
        ##num += 1
        ##xPos += 70
   ## xPos = 0
   ## yPos += 70

##window.mainloop()

from tkinter import *
from PIL import Image, ImageTk, ImageOps

# --- 윈도우 창 설정 ---
window = tk.Tk()
window.title("JPG 이미지 불러오기")
window.geometry("200x200")

# 1. JPG 이미지 경로 설정 (확장자가 .jpg 또는 .jpeg인지 확인하세요)
image_path ="C:\Users\Admin\Documents\20261482_js_python\gif\훔.gif"   # 실제 JPG 파일 경로로 수정


# 2. JPG 이미지 열기
img = Image.open(image_path)

# 3. 비율을 유지하며 200*200 크기 안으로 축소 (찌그러지거나 잘리지 않음)
img_resized = ImageOps.contain(img, (200, 200))

# 4. Tkinter 호환 이미지로 변환
tk_img = ImageTk.PhotoImage(img_resized)

# 5. 화면에 이미지 표시
label = tk.Label(window, image=tk_img)
label.image = tk_img #이미지 깜빡임/사라짐 방지용 참조 유지
label.pack(pady=10)

# --- 윈도우 창 유지 ---
window.mainloop()