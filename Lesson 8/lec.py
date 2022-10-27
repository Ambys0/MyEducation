from tkinter import*
from tkinter import messagebox
from tkinter.filedialog import askopenfile, asksaveasfile

file_name = NONE

def new_file():
    global file_name
    file_name = "Nasvi nema"
    text.delete('1.0', END)

def open_as():
    global file_name
    opcom = askopenfile(mode = "r")
    if opcom is None:
        return
    file_name = opcom.name
    dany = opcom.read()
    text.delete("1.0", END)
    text.insert ("1.0", dany)

def save_as():
    out = asksaveasfile(mode = "w", defaultextension = ".txt")
    data = text.get("1.0", END)
    try:
        out.write(data.rstrip())
    except Exception:
        messagebox.showerror("Warning!! ", "Cant save file!")


root=Tk()
root.title("Project")
root.geometry("400x400")

menu_bar = Menu(root)
file_menu = Menu(menu_bar)
menu_bar.add_cascade(label = "File", menu = file_menu)

text = Text(root, width = 400, height = 400)
text.pack()

file_menu.add_command(label = "New", command = new_file)
file_menu.add_command(label = "Save as", command = save_as)
file_menu.add_command(label = "Open as", command = open_as)
file_menu.add_command(label = "Exit", command = quit)

root.config(menu = menu_bar)
root.mainloop()

f = open("noname.txt", "r")
f.read()
f.close()

