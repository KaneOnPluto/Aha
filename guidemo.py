from tkinter import *

window=Tk()

window.geometry('420x420')
window.title('first GUI')
window.config(background="#329ea8")

label1=Label(window,text='First')
label1.pack()

b1=Button(window,text='stop',width=25,command=window.destroy)
b1.pack()

window.mainloop()



