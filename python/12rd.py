from tkinter import *    
from tkinter import messagebox
from tkinter.filedialog import askopenfilename

## 함수 선언 부분 ##
def fun_open():
    filepath = askopenfilename(   
        title="gif 이미지 로드", 
        filetypes=(("gif이미지", "*.gif"), ("모든이미지", "*.png"))
    )
    
    if filepath: 
        
        tk_img = PhotoImage(file=filepath) 
        
        
        image_label.config(image=tk_img)
        
        
        image_label.image = tk_img

def func_exit():
    window.quit()
    window.destroy()


window = Tk()         
window.geometry("500x500") 


image_label = Label(window)
image_label.pack(expand=True)


mainMenu = Menu(window)  
window.config(menu=mainMenu)  

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label="파일", menu=fileMenu)
fileMenu.add_command(label="열기", command=fun_open)
fileMenu.add_separator()
fileMenu.add_command(label="종료", command=func_exit)

viewMenu = Menu(mainMenu)
mainMenu.add_cascade(label="보기", menu=viewMenu)
viewMenu.add_command(label="축소", command=fun_open)
viewMenu.add_separator()
viewMenu.add_command(label="확대", command=func_exit)

homeMenu = Menu(mainMenu)
mainMenu.add_cascade(label="홈", menu=homeMenu)
homeMenu.add_command(label="저장", command=fun_open)
homeMenu.add_separator()
homeMenu.add_command(label="선택", command=func_exit)
homeMenu.add_separator()
homeMenu.add_command(label="찾기", command=func_exit)


window.mainloop()




