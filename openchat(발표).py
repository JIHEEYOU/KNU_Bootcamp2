from tkinter import*
import tkinter
import tkinter.ttk
import pandas as pd
from csv import writer
import time
from datetime import datetime
import tkinter.messagebox as msgbox
from PIL import ImageTk, Image




window=tkinter.Tk()
window.title("배달을 이룸")
window.geometry("550x750")
window.resizable(False, False)

##########
items = []
openurl = []
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
    listbox2.delete(0,255)
    for i in range(len(items)):
        listbox2.insert(0, items[i])
#########################
   

######################
        
def make_room(): #방 만들기
    global items,openurl,btn7,entry1,entry2,makes_room
        #bg_img = ImageTk.PhotoImage(file = 'C:/python/image/bg_color.png')
        #makes_room = Tk()
    makes_room = Toplevel(window)
    makes_room.geometry('250x250')
    makes_room.configure(bg="#f2db68")
        
    label1 = Label(makes_room,text='방 만들기',font=('배달의민족 주아',15))
    label1.configure(bg="#f2db68")
    label1.pack()

    label2 = Label(makes_room,text='오픈채팅 url을 입력해주세요',font=('배달의민족 주아',15))
    label2.configure(bg="#f2db68")
    label2.pack()

    entry1 = Entry(makes_room, width = 5)
    entry1.configure(bg="#d2cebd")
    entry1.place(x = 100, y = 100, width=100,height=20)
        #entry1.pack()

    entry2 = Entry(makes_room, width = 5)
    entry2.configure(bg="#d2cebd")
    entry2.place(x = 100, y = 130, width=100,height=20)

    label3 = Label(makes_room,text=' 방 제목:',font=('배달의민족 주아',15))
    label3.configure(bg="#f2db68")
    label3.place(x = 10, y = 100, width=60, height=20)
    

    label4 = Label(makes_room,text='URL :',font=('배달의민족 주아',15))
    label4.configure(bg="#f2db68")
    label4.place(x = 20, y = 130, width=60, height=20)
    

    btn7= Button(makes_room,text ='만들기',font=('배달의민족 주아',15),command = makes)
    btn7.configure(bg="#f2db68")
    btn7.place(x = 80, y = 200, width=100, height=30)

def makes():
    global openurl
    openurl = []
    room_name = entry1.get()
    url = entry2.get()
    openurl.append(url)
    items.insert(0,room_name)
    listbox.delete(0,255)
    for i in range(len(items)):
        listbox.insert(0, items[i])
    listbox2.delete(0,255)
    for i in range(len(items)):
        listbox2.insert(0, items[i])
        makes_room.destroy()

        
######################################
        
def modify_room(): # 방 수정하기
    global items
    selection = listbox.curselection()
    value = listbox.get(selection[0])
    
    mod_room = Tk()
    mod_room.geometry('250x250')
    mod_room.configure(bg="#f2db68")

    label1 = Label(mod_room,text=value)
    label1.configure(bg="#f2db68")
    label1.pack()

    label2 = Label(mod_room,text='방 제목 수정',font=('배달의민족 주아',15))
    label2.configure(bg="#f2db68")
    label2.pack()
    
    entry1 = Entry(mod_room, width = 5)
    entry1.pack()

    def modify_2():
        global items, value
        selection = listbox.curselection()
        value = listbox.get(selection[0])
            
        ans_mod = entry1.get()
        items.remove(value)
        items.insert(0,ans_mod)
        listbox.delete(0,255)
        for i in range(len(items)):
            listbox.insert(0, items[i])

        listbox2.delete(0,255)
        for i in range(len(items)):
            listbox2.insert(0, items[i])
            mod_room.destroy()


    btn8 = Button(mod_room,text = '수정하기',font=('배달의민족 주아',15),command = modify_2)
    btn8.configure(bg="#f2db68")
    btn8.place(x = 80, y = 200, width=100, height=30)
####################################
    
def choose(): #입장하기
    global items,openurl
    print(openurl)
    in_textName =input_name.get()
    in_textNum = input_num.get()
    list_data = [(time.strftime('%y-%m-%d %H:%M:%S %p')),in_textName,in_textNum]
    with open('NameNumList.csv', 'a', newline='') as f_object:  
        writer_object = writer(f_object)
        writer_object.writerow(list_data)
        print('csv에 저장하였습니다')
        f_object.close()

    enter_room = Tk()
    enter_room.geometry('250x250')
    enter_room.configure(bg="#f2db68")
    
    selection = listbox2.curselection()
    value = listbox2.get(selection[0])
    
    label1 = Label(enter_room,text=value)
    label1.pack()
    
    text = Entry(enter_room)
    text.pack()
    text.insert(0,openurl[0])

def data():#scroll
    for i in range(50):
       Label(frame3,text=i).grid(row=i,column=0)
       Label(frame3,text="my text"+str(i)).grid(row=i,column=1)
       Label(frame3,text="..........").grid(row=i,column=2)

def myfunction(event):#scroll
    window.configure(scrollregion=window.bbox("all"),width=200,height=200)


def confirm():
    msgbox.showinfo('로그인','로그인 완료하였습니다\n다음 창으로 이동해주세요')
   

#페이지 1

frame1=tkinter.Frame(window)
notebook.add(frame1, text="로그인")

bg_img1 = ImageTk.PhotoImage(file = 'C:/python/image/bg.png')
label1 = Label(frame1, image = bg_img1)
label1.pack()

input_name = Entry(frame1, width=20)#이름 입력하는곳
input_name.configure(background = "#d2cebd")

input_name.place(x=80,y=310,width=280,height=40)
input_num = Entry(frame1, width=20)#학번 입력하는곳

input_num.configure(background = "#d2cebd")
input_num.place(x=80,y=383,width=280,height=40)

login_button = PhotoImage(file = 'C:/python/image/login_logo.png')
btn = Button(frame1, image = login_button, command=confirm,text='로그인')
btn.place(x = 380, y = 310)

#페이지 2
frame2=tkinter.Frame(window)
bg_img2 = ImageTk.PhotoImage(file = 'C:/python/image/bg_color2.png')
label2 = Label(frame2, image = bg_img2)
label2.pack()

########
listbox = Listbox(frame2, selectmode='single')
listbox.place(x=15,y=100,width=500,height=280)

for i in range(len(items)):
    listbox.insert(0, items[i])
#########

 #방제목

btn1= PhotoImage(file = 'C:/python/image/btn1.png')#글 올리기
btn = Button(frame2, image = btn1, command = make_room)
btn.place(x = 15, y = 650,width=150,height=70)

btn2= PhotoImage(file = 'C:/python/image/btn2.png')#글 수정하기
btn = Button(frame2, image = btn2, command = modify_room)
btn.place(x = 200, y = 650,width=150,height=70)

btn3= PhotoImage(file = 'C:/python/image/btn3.png')#방 마감하기
btn = Button(frame2, image = btn3, command=csv_save)
btn.place(x = 380, y = 650,width=150,height=70)

notebook.add(frame2, text="방 만들기")
b3=Button(frame2,text='종료하기')

#페이지 3

frame3=tkinter.Frame(window)
bg_img3 = ImageTk.PhotoImage(file = 'C:/python/image/bg_color2.png')
label3 = Label(frame3, image = bg_img3)
label3.pack()


##########
listbox2 = Listbox(frame3, selectmode='single')
listbox2.place(x=15,y=100,width=600,height=280)

for i in range(len(items)):
    listbox2.insert(0, items[i])
###########
notebook.add(frame3, text="입장하기")

btn4= PhotoImage(file = 'C:/python/image/btn4.png')
btn = Button(frame3, image = btn4,command = choose)
btn.place(x = 200, y = 650,width=150,height=70)


window.mainloop()
