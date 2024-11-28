from tkinter import*
import tkinter
import tkinter.ttk
import pandas as pd
from csv import writer
import time
from datetime import datetime
import tkinter.messagebox as msgbox
from PIL import ImageTk, Image
from client import*



window=tkinter.Tk()
window.title("배달을 이룸")
window.geometry("550x750")
window.resizable(False, False)

##########
items = ['치킨','피자','중식','일식','한식','야식','분식']
ID = {}
#############

notebook=tkinter.ttk.Notebook(window, width=550, height=750)
notebook.pack()

def csv_save(): #방 마감하기
    global items

    
    selection = listbox.curselection()
    value = listbox.get(selection[0])
    items.remove(value)
    listbox.delete(0,255)
    for i in range(len(items)):
        listbox.insert(0, items[i])

    
def choose(): #입장하기
    main()
    """
    in_textName =input_name.get()
    in_textNum = input_num.get()
    list_data = [(time.strftime('%y-%m-%d %H:%M:%S %p')),in_textName,in_textNum]
    with open('NameNumList.csv', 'a', newline='') as f_object:  
        writer_object = writer(f_object)
        writer_object.writerow(list_data)
        print('csv에 저장하였습니다')
        f_object.close()
    """


    

def data():#scroll
    for i in range(50):
       Label(frame3,text=i).grid(row=i,column=0)
       Label(frame3,text="my text"+str(i)).grid(row=i,column=1)
       Label(frame3,text="..........").grid(row=i,column=2)

def myfunction(event):#scroll
    window.configure(scrollregion=window.bbox("all"),width=200,height=200)


def confirm():
    global ID
    try:            
        in_textName =input_name.get()
        in_textNum = int(input_num.get())
        list_data = [(time.strftime('%y-%m-%d %H:%M:%S %p')),in_textName,in_textNum]
        with open('NameNumList.csv', 'a', newline='') as f_object:  
            writer_object = writer(f_object)
            writer_object.writerow(list_data)
            print('csv에 저장하였습니다')
            f_object.close()
        
        msgbox.showinfo('로그인','로그인 완료하였습니다\n다음 창으로 이동해주세요')
        ID[input_name.get()] = input_num.get()
        return ID
        
    except:
        msgbox.showerror('오류','이름 또는 학번을 잘못 입력하셨습니다')
    


#페이지 1

frame1=tkinter.Frame(window)
notebook.add(frame1, text="로그인")

bg_img1 = ImageTk.PhotoImage(file ='C:/python/image/bg.png')
label1 = Label(frame1, image = bg_img1)
label1.pack()

input_name = Entry(frame1, width=20)#이름 입력하는곳
input_name.configure(background = "#d2cebd")
#input_name.insert(0,'이름을 입력해주세요')
input_name.place(x=80,y=310,width=280,height=40)
input_num = Entry(frame1, width=20)#학번 입력하는곳
#input_num.insert(0,'학번을 입력해주세요')
input_num.configure(background = "#d2cebd")
input_num.place(x=80,y=383,width=280,height=40)

login_button = PhotoImage(file = 'C:/python/image/login_logo.png')
btn = Button(frame1, image = login_button, command=confirm,text='로그인')
btn.place(x = 380, y = 310)

#페이지 2
frame2=tkinter.Frame(window)
bg_img2 = ImageTk.PhotoImage(file = 'C:/python/image/bg_color.png')
label2 = Label(frame2, image = bg_img2)
label2.pack()

########
listbox = Listbox(frame2, selectmode='single')
listbox.place(x=15,y=100,width=500,height=280)

for i in range(len(items)):
    listbox.insert(0, items[i])
#########

 #방제목


notebook.add(frame2, text="음식 메뉴")

b3=Button(frame2,text='종료하기')

btn4= PhotoImage(file = 'C:/python/image/btn4.png')
btn = Button(frame2, image = btn4,command = choose)
btn.place(x = 200, y = 650,width=150,height=70)

#페이지 3


window.mainloop()
