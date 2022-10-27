from cProfile import label
from logging import root
from tkinter import*
from tkinter import messagebox
import pickle

HEIGHT = 550
WIDTH = 550

root = Tk()
root.title('Form')
root.geometry("%dx%d" % (HEIGHT, WIDTH))
root.resizable(False, False)

root.option_add('*Font', "Calibri")
root.option_add('*Background', 'white')

img = PhotoImage(file='/home/ambys/WORK/MyRepo/Basic/20.09/bg3.gif')
background_label = label(root, image = img)
background_label.place(relwidth = 1, relheight = 1)

root.mainloop()



