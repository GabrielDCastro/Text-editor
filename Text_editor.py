from tkinter import *
import tkinter.filedialog as fdialog
from tkinter import messagebox

file_name = 'my_file.txt'

def new_file():
    text_box.delete(0.0, END) #when open a file everything will be delete

def save_file():
    text = text_box.get(0.0, END) #will save fom 0 to end
    file = open(file_name, 'w')
    file.write(text)
    file.close()

def save_as():
    file = fdialog.assaveasfile(mode='w', defaultextension='txt')
    if file != None:
        text = text_box.get(0.0, END)
        try:
            file.write(text.rstrip())
        except:
            messagebox.showerror(title="Erro", message="não foi possível salvar")

def open_file():
    file = fdialog.askopenfile(mmode="r")
    if file != None:
        text = file.read()
        text_box.delete(0.0, END)
        text_box.insert(0.0, text)

width, height = 800, 600

window = Tk()
window.title("pyNote")
window.minsize(width=width, height=height)
window.maxsize(width=width, height=height)

text_box = Text(window, width=width, height=height)
text_box.pack() #The pack() geometry manager organizes widgets in blocks before placing them in the parent widget

menu_bar = Menu(window)
file_menu = Menu(menu_bar)
file_menu.add_command(label= "New", command=new_file)
file_menu.add_command(label= "Open", command=open_file)
file_menu.add_command(label= "Save", command=save_file)
file_menu.add_command(label= "Save as...", command=save_as)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.quit)

menu_bar.add_cascade(label="File", menu=file_menu)

window.config(menu=menu_bar)
window.mainloop()
