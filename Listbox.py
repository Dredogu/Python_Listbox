from tkinter import *

window = Tk()


def submit():

    food = []

    for index in listbox.curselection():  # range degil dikkat!!! ornegin => index == 3 oldugu zaman
        food.insert(index,listbox.get(index))

    for index in food:
        print(index)

def add():
    listbox.insert(listbox.size(),entry.get())
    listbox.config(height=listbox.size())

def delete():
    listbox.delete(listbox.curselection())
    listbox.config(height=listbox.size())

listbox = Listbox(window,
                  bg='purple',
                  fg='white',
                  font=('Consolas',50),
                  width=15,
                  selectmode=MULTIPLE)
listbox.pack()

listbox.insert(0,'pizza')
listbox.insert(1,'hamburger')
listbox.insert(2,'hotdog')
listbox.insert(3,'sushi')

listbox.config(height=listbox.size())

entry = Entry(window,font=('Consolas',20))
entry.pack()

submitButton = Button(window,text='submit',command=submit,font=('Consolas',20))
submitButton.pack()

addButton = Button(window,text='add',command=add,font=('Consolas',20))
addButton.pack()

deleteButton = Button(window,text='delete',command=delete,font=('Consolas',20))
deleteButton.pack()

window.mainloop()
