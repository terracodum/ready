from tkinter import *
def hello():
    print("Hello!")
root = Tk()
root.resizable(False,False)
root.geometry("300x300")
l1 = Label(text="Hello!",
           height=10,
           width=15,
           )
b1 = Button(text ="Push me!",
            height=5,
            width=12,
            background="black",
            foreground="blue",
            command=hello
            )
b1.place(x= 110, y=130)



l1.place(x=70, y=10)


root.mainloop()