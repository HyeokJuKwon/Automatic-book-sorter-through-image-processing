import tkinter
from picamera import PiCamera
from time import sleep
import cv2
try:
        import Image
except ImportError:
        from PIL import Image
import pytesseract

win = tkinter.Tk()
a = 0
k = 0
l = 0
m = 0
u = []
f = open('art.txt','w')
f.close()
f = open('sci.txt','w')
f.close()
f = open('lan.txt','w')
f.close()
def click_find():
    def click():
        wn.destroy()
    def play():
        global u
        result=op1.get()
        f = open('art.txt','r')
        h = 0
        while True:
            line = f.readline()
            if result in line:
                h += 1
                u.insert(h-1, line)
            if not line: break    
        f.close()
        f = open('sci.txt','r')
        while True:
            line = f.readline()
            if result in line:
                h += 1
                u.insert(h-1, line)
            if not line: break
        f.close()
        f = open('lan.txt','r')
        while True:
            line = f.readline()
            if result in line:
                h += 1
                u.insert(h-1, line)
            if not line: break
        f.close()
        if h > 0:
            i = 0
            while i < h: 
                label=tkinter.Label(wn,text=u[i],font=("System",20))
                label.place(x=100, y=170+i*35)
                i += 1
        else:
            label=tkinter.Label(wn,text="검색결과가 없습니다.",font=("System",20))
            label.place(x=200, y=170)
    op1=tkinter.StringVar()
    op1.set("")
    result=tkinter.StringVar()
    result.set("")
    wn  = tkinter.Toplevel(win)
    wn.title("검색창")
    wn.geometry("600x400-100+0")
    label=tkinter.Label(wn, text="제목을 입력하세요.", font=("System",20))
    label.place(x=150, y=60)
    find=tkinter.Entry(wn,width=25,textvariable=op1)
    find.pack()
    find.place(x=150, y=130)
    button = tkinter.Button(wn,text="find",font=("System",20),command=play)
    button.place(x=390, y=120)
    button = tkinter.Button(wn,text="Close",font=("System",20),command=click)
    button.place(x=480, y=120)
    wn.mainloop()
   
def click_button():
    global a
    #camera
    camera = PiCamera()
    camera.rotation = 90
    camera. start_preview()
    sleep(3)
    camera. capture('/home/pi/book.jpg')
    camera. stop_preview()
    camera.close()
    #binary
    img_source = cv2.imread('book.jpg',0)
    ret,img_result1 = cv2.threshold(img_source, 127, 255, cv2.THRESH_BINARY)
    ret,img_result2 = cv2.threshold(img_source, 127, 255, cv2.THRESH_TRUNC)
    ret,img_result3 = cv2.threshold(img_source, 127, 255, cv2.THRESH_TOZERO)
    ret,img_result4 = cv2.threshold(img_source, 127, 255, cv2.THRESH_TOZERO_INV)
    cv2.imwrite("book_binary.jpg", img_result1)
    cv2.imwrite("book_binarya.jpg", img_result2)
    cv2.imwrite("book_binaryb.jpg", img_result3)
    cv2.imwrite("book_binaryc.jpg", img_result4)
    #tes
    print(pytesseract.image_to_string(Image.open('/home/pi/book_binary.jpg'), lang = 'Hangul'))
    print(pytesseract.image_to_string(Image.open('/home/pi/book_binarya.jpg'), lang = 'Hangul'))
    print(pytesseract.image_to_string(Image.open('/home/pi/book_binaryb.jpg'), lang = 'Hangul'))
    print(pytesseract.image_to_string(Image.open('/home/pi/book_binaryc.jpg'), lang = 'Hangul'))
    #data
    art = ['드로잉', '건축물', '조각', '서예', '공예', '디자인', '사진']
    sci = ['통신', '과학', '수학', '화학', '물리학', '생물학', '천문학', '반도체']
    lan = ['TOEIC', '영어', '중국어', '일본어', '문법', '작문', '회화', '어휘']
    d = pytesseract.image_to_string(Image.open('/home/pi/book_binaryb.jpg'), lang = 'Hangul')
    dd = d.strip()
    z = dd.replace(' ','')
    f = open('book.txt','w')
    f.write(z)
    f.close()
    f = open('book.txt','r')
    title = f.readline()
    f.close()
    
    for x in art:
        if x in z:
            global k
            k += 1
            if k == 1:
                f = open('art.txt','w')
                f.write(title)
                f.close()
            else:
                f = open('art.txt','a')
                f.write('\n')
                f.write(title)
                f.close()
            def click():
                wn.destroy()
            wn  = tkinter.Toplevel(win)
            wn.title("결과창")
            wn.geometry("500x300")
            label=tkinter.Label(wn, text="제목 : ", font=("System",20))
            label.place(x=130, y=40)
            label=tkinter.Label(wn, text=title, font=("System",20))
            label.place(x=210, y=40)
            label=tkinter.Label(wn, text="장르 : 예술",font=("System",20))
            label.place(x=170, y=90)
            label=tkinter.Label(wn, text="위치 : 예술",font=("System",20))
            label.place(x=170, y=140)
            label=tkinter.Label(wn, text=k,font=("System",20))
            label.place(x=310, y=140)
            button = tkinter.Button(wn,text="Close",font=("System",20),command=click)
            button.place(x=200, y=190)
            wn.mainloop()
            a=1
    for x in sci:
        if x in z:
            global l
            l += 1
            if l == 1:
                f = open('sci.txt','w')
                f.write(title)
                f.close()
            else:
                f = open('sci.txt','a')
                f.write(title)
                f.close()
            def click():
                wn.destroy()
            wn  = tkinter.Toplevel(win)
            wn.title("결과창")
            wn.geometry("500x300")
            label=tkinter.Label(wn, text="제목 : ", font=("System",20))
            label.place(x=130, y=40)
            label=tkinter.Label(wn, text=title, font=("System",20))
            label.place(x=210, y=40)
            label=tkinter.Label(wn, text="장르 : 과학",font=("System",20))
            label.place(x=170, y=90)
            label=tkinter.Label(wn, text="위치 : 과학",font=("System",20))
            label.place(x=170, y=140)
            label=tkinter.Label(wn, text=l,font=("System",20))
            label.place(x=310, y=140)
            button = tkinter.Button(wn,text="Close",font=("System",20),command=click)
            button.place(x=200, y=190)
            wn.mainloop()
            a=1
    for x in lan:
        if x in z:
            global m
            m += 1
            if m == 1:
                f = open('lan.txt','w')
                f.write(title)
                f.close()
            else:
                f = open('lan.txt','a')
                f.write(title)
                f.close()
            def click():
                wn.destroy()
            wn  = tkinter.Toplevel(win)
            wn.title("결과창")
            wn.geometry("500x300")
            label=tkinter.Label(wn, text="제목 : ", font=("System",20))
            label.place(x=130, y=40)
            label=tkinter.Label(wn, text=title, font=("System",20))
            label.place(x=210, y=40)
            label=tkinter.Label(wn, text="장르 : 언어",font=("System",20))
            label.place(x=170, y=90)
            label=tkinter.Label(wn, text="위치 : 언어",font=("System",20))
            label.place(x=170, y=140)
            label=tkinter.Label(wn, text=m,font=("System",20))
            label.place(x=310, y=140)
            button = tkinter.Button(wn,text="Close",font=("System",20),command=click)
            button.place(x=200, y=190)
            wn.mainloop()
            a=1
    if a==0:
        def click():
                wn.destroy()       
        wn  = tkinter.Toplevel(win)
        wn.title("결과창")
        wn.geometry("500x300")
        label=tkinter.Label(wn, text="장르를 찾을 수 없습니다.",font=("System",20))
        label.place(x=110, y=90)
        button = tkinter.Button(wn,text="Close",font=("System",20),command=click)
        button.place(x=200, y=155)
        wn.mainloop()


win.title("Automatic book sorter")
win.geometry("600x400-100+0")
label=tkinter.Label(win, text="Press the button",font=("System",30))
label.place(x=150, y=90)
button = tkinter.Button(win,text="Processing",font=("System",20),command=click_button)
button.place(x=90, y=220)
button = tkinter.Button(win,text="Close",font=("System",20),command=quit)
button.place(x=410, y=220)
button = tkinter.Button(win,text="Find",font=("System",20),command=click_find)
button.place(x=290, y=220)
win.mainloop()



