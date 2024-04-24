from tkinter import *

window = Tk()
window.geometry("820x560")
photoList = [None] * 4

num = 0

def left():
    global num
    if num > 0:
        num = num - 1
    label.config(image=photoList[num])

def right():
    global num
    if num >= 3:
        num = 2
    num = num + 1
    label.config(image=photoList[num])

button1 = Button(window, text = "<< 이전", command = left)
button2 = Button(window, text = "다음 >>", command = right)

photoList[0] = PhotoImage(file="./childhood_size_1500.gif")
photoList[1] = PhotoImage(file="./manhood_size_1500.gif")
photoList[2] = PhotoImage(file="./old_age_size_1500.gif")
photoList[3] = PhotoImage(file="./youth_size_1500.gif")

label = Label(window, image = photoList[0])

button1.grid(row=1, column=1)
button2.grid(row=1, column=2)
label.grid(row=2, column=1, columnspan=2)

window.mainloop()