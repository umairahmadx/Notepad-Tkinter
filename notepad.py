import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

root = tk.Tk()
root.title('Notepad')
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
filePath=""

def newClicked(event=None):
    global filePath 
    filePath=""
    root.title('Notepad')
    textBox.delete('1.0',tk.END)

def saveAsClicked(event=None):
    global filePath 
    filePath = filedialog.asksaveasfilename(defaultextension='.txt',filetypes=[('Text Files',"*.txt"),("All Files","*.*")])
    if filePath:
        root.title(filePath)
        with open(filePath,"w") as file:
            content = textBox.get("1.0",tk.END)
            file.write(content.strip())

def saveClicked(event=None):
    global filePath
    if filePath:
        with open(filePath,"w") as file:
            content = textBox.get("1.0",tk.END)
            file.write(content.strip())
    else:
        saveAsClicked()

def openClicked(event=None):
    global filePath
    filePath = filedialog.askopenfilename(defaultextension='.txt',filetypes=[('Text Files',"*.txt"),("All Files","*.*")])
    if filePath:
        root.title(filePath)
        with open(filePath,"r") as file:
            content = file.read() 
            textBox.delete('1.0',tk.END)
            textBox.insert(tk.END,content)

def aboutClicked():
    messagebox.showinfo("About Notepad", "This is a simple Notepad application made with Python and Tkinter By me Umair \U0001F493")

menubar = tk.Menu(root)

FileMenu = tk.Menu(menubar, tearoff=False)
FileMenu.add_command(label='New', underline=0, accelerator='Ctrl+N', command=newClicked)
FileMenu.add_command(label='Open', underline=0, accelerator='Ctrl+O', command=openClicked)
FileMenu.add_command(label='Save', underline=0, accelerator='Ctrl+S', command=saveClicked)
FileMenu.add_command(label='Save As', underline=0, accelerator='Ctrl+Shift+S', command=saveAsClicked)

menubar.add_cascade(label='File', menu=FileMenu)
menubar.add_command(label="About",command=aboutClicked)

root.config(menu=menubar)

textBox = tk.Text(root,font="Calibri")
textBox.grid(column=0, row=1, sticky="nsew")

root.bind_all("<Control-n>", newClicked)
root.bind_all("<Control-o>", openClicked)
root.bind_all("<Control-s>", saveClicked)
root.bind_all("<Control-S>", saveAsClicked)
root.mainloop()