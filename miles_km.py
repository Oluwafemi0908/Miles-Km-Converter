from tkinter import *

window = Tk()
window.title('Miles to Km Converter')
window.minsize(300, 200)
window.config(padx=50, pady=50)
label1 = Label(text='is equal to', font=('Arial', 10, 'normal'))
label1.grid(row=2, column=0)
label2 = Label(text='', font=('Arial', 10, 'normal'))
label2.grid(row=1, column=2)
label3 = Label(text='', font=('Arial', 10, 'normal'))
label3.grid(row=2, column=2)
answer = Label(text='', font=('Arial', 10, 'normal'))
answer.grid(column=1, row=2)


def listbox_used(event):
    # Gets current selection from listbox, Do not delete the event argument
    ls = listbox.get(listbox.curselection())
    if ls == converter[0]:
        label2.config(text='Miles')
        label3.config(text='Km')
        button.config(command=miles_to_km)
    elif ls == converter[1]:
        label2.config(text='Km')
        label3.config(text='Miles')
        button.config(command=km_to_miles)


listbox = Listbox(height=2, width=12)
converter = ["Miles to Km", 'Km to Miles']
for item in converter:
    listbox.insert(converter.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.grid(row=0, column=1)

user_input = Entry(width=10)
user_input.grid(row=1,column=1)


def miles_to_km():
    u = float(user_input.get())
    u *= 1.60934
    answer.config(text=u)


def km_to_miles():
    u = float(user_input.get())
    u /= 1.60934
    answer.config(text=u)


button = Button(text='convert', command='', padx=10)
button.grid(column=1, row=3)

window.mainloop()
