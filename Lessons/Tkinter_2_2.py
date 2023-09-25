import tkinter

def print():
    print('Hello World!')

hex() #Переводит число в шестнадцатеричную систему счисления

#свойства окна
window=tkinter.Tk()
window.title('Приложение') #название окна
window.geometry('500x300') #размеры
window.resizable(False, False) #возможность изменять его размеры

#Надпись сверху посередине в окне
label = tkinter.Label(text='Hello world!',
                      font=('Times New Roman', 18, 'italic', 'bold', 'underline'), #font=(Название шрифта, размер, стиль текста)
                      bg='white', fg='black', #цвет заднего фона текста(bg) и цвет самого текста(fg)
                      width=20, height=4, #высота и ширина заднего фона(лейбла)
                      )

label.pack(side='top') #Место где будет надпись(Top, bottom, left, right)

#Ввод в окно чего-либо
entry = tkinter.Entry()
entry.pack()

#Создание кнопки
button = tkinter.Button(text='Click me!',
                        activebackground='red', #Цвет кнопки при нажатии
                        activeforeground='black', #Цвет текста при нажатии
                        command=print) #Команда, что будет делать кнопка
button.pack()

#Изменение свойств в коде любого аргумента
#label['text'] = 'Goodbye World!'
#label.config(text='Goodbye World!')

#Открытие окна(обязательно в конце)
window.mainloop()