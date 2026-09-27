from tkinter import *
window=Tk()
def btnclick():
    print("you clicked button")

btn1=Button(window,text="click me",command=btnclick,activebackground="blue",
            activeforeground="white",anchor="center",bd=10,bg="white",cursor="hand2",
            disabledforeground="gray",fg="black",font=("Arial",12),height=5)
btn1.pack()
window.mainloop()
