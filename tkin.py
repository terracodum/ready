from tkinter import *
def hello():
    print("Hello!")
root = Tk()
root.resizable(False,False)
root.geometry("300x300")
b1 = Button(text ="Push me!",
            height=5,
            width=12,
            background="black",
            foreground="blue",
            command=hello
            )
b1.place(x= 110, y=130)
l1 = Label(text="Hello!",
           height=7,
           width=15,

           )
l1.place(x=70, y=10)


root.mainloop()