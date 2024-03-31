
from tkinter import *
from tkinter.ttk import Combobox
window = Tk()
window.title('Программа для расчета показателей надежности')
window.geometry('500x500')  # размер окна

lbl = Label(window, text='Выберите формулу для расчета', font=('Arial', 15))
lbl.place(rely=0.02, relx=0.2)

combo = Combobox(window)
combo['values'] = (1, 2, 3, 4, 5, )
combo['state'] = ('readonly')
combo.current(0)  # установите вариант по умолчанию
combo.place(rely=0.1, relx=0.4, width=80)
def summa():
    a = EntryA.get()
    a = int(a)

    b = EntryB.get()
    b = int(b)

    result = str(a + b)
    EntryC.delete(0, END)
    EntryC.insert(0, result)

lbl = Label(window, text='Введите параметр а', font=('System', 8))
lbl.place(rely=0.25, relx=0.01)

EntryA = Entry(window, width=10)
EntryA.place(rely=0.3, relx=0.01)

lbl = Label(window, text='Введите параметр b', font=('System', 8))
lbl.place(rely=0.25, relx=0.4)

EntryB = Entry(window, width=10)
EntryB.place(rely=0.3, relx=0.4)

btn = Button(window, text="Рассчитать", command=summa)
btn.place(rely=0.4, relx=0.25, width=200)

lbl = Label(window, text='Ответ', font=('System', 8))
lbl.place(rely=0.25, relx=0.8)

EntryC = Entry(window, width=10)
EntryC.place(rely=0.3, relx=0.8)
window.mainloop()
