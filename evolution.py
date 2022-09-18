import tkinter as tk
from tkinter import *
import tkinter.filedialog
from PIL import ImageTk, Image
from random import randint
import os
from os import walk



class Main():
    def __init__(self):
        super().__init__()

        self.filenames = next(walk(f'{os.path.abspath(os.curdir)}\EVOLUTION_PNG'), (None, None, []))[2]
        print(len(self.filenames))

        self.canvases = {}
        self.canvases2 = {}
        self.textes = {}
        self.imgs = {}
        self.imgs2 = {}
        self.rand = {}
        
        self.root = tk.Tk()
        self.root.geometry('900x750')

        self.root2 = tk.Toplevel()
        self.root2.geometry('900x750')

        self.canvas_main  = tk.Canvas(self.root, width = 900, height = 650, highlightthickness = 0)
        self.canvas_main.pack(expand = True)

        self.canvas_main2  = tk.Canvas(self.root2, width = 900, height = 650, highlightthickness = 0)
        self.canvas_main2.pack(expand = True)

        #but_remove = tk.Button(text='remove', command=lambda: self.delete(self.canvas1, self.image1))
        #but_remove.pack(side='bottom', padx=5, pady=5)

        but_add = tk.Button(text='add', command=lambda: self.add_card(len(self.canvases)),bg='#FFE4E1',height = 2,width = 10)
        but_add.pack(side='bottom', padx=5, pady=5)
        but_add.place(relx=.45, rely=.85)

        self.count = StringVar()
        inp = Entry(textvariable=self.count)
        inp.pack(side='left', padx=5, pady=5)
        inp.place(relx=.2, rely=.85)
        inp.bind('<Return>',self.delete)

        label1 = Label(text='1. Put a number\n2. Press ENTER for delete', justify=LEFT)
        label1.place(relx=.2, rely=.9)

        self.count_send = StringVar()
        inp_send = Entry(textvariable=self.count_send)
        inp_send.pack(side='left', padx=5, pady=5)
        inp_send.place(relx=.7, rely=.85)
        inp_send.bind('<Return>',self.send)

        label2 = Label(text='1. Put a number\n2. Press ENTER for sending', justify=LEFT)
        label2.place(relx=.7, rely=.9)

        label3 = Label(text='DELETE', justify=LEFT,bg='#FFF5EE',font=('Helvetica 12 bold'))
        label3.place(relx=.2, rely=.8)

        label4 = Label(text='SEND', justify=LEFT, bg='#FFF5EE', font=('Helvetica 12 bold'))
        label4.place(relx=.7, rely=.8)
        
        self.root2.mainloop()
        self.root.mainloop()

    
    def delete(self, key):
        self.canvases[int(self.count.get())].delete(ALL)
        del self.canvases[int(self.count.get())]
        self.canvases2[int(self.count.get())].delete(ALL)
        del self.canvases2[int(self.count.get())]

    def send(self, key):
        count = int(self.count_send.get())
        image = self.rand[count]
        self.canvases2[count] = tk.Canvas(self.root2, width=180, height=300)
        self.canvases2[count].place(x = 150, y = 300, anchor=CENTER)
        self.canvases2[count].create_text(90, 290, text=str(count),fill="black",font=('Helvetica 12 bold'))
        image = Image.open(image)
        image = image.resize((180,280), Image.ANTIALIAS)
        self.imgs[count] = ImageTk.PhotoImage(image)
        self.canvases2[count].create_image(0, 0, anchor='nw',image=self.imgs[count])
        self.canvases2[count].bind("<B1-Motion>", self.drag2)

    def add_card(self, s):
        self.canvases[s] = tk.Canvas(self.root, width=180, height=300)
        self.canvases[s].place(x = 150, y = 300, anchor=CENTER)
        rand = randint(0, len(self.filenames)-1)
        image = Image.open(f'{os.path.abspath(os.curdir)}\EVOLUTION_PNG\{self.filenames[rand]}')
        self.filenames.pop(rand)
        image = image.resize((180,280), Image.ANTIALIAS)
        self.imgs[s] = ImageTk.PhotoImage(image)
        self.rand[s] = f'{os.path.abspath(os.curdir)}\EVOLUTION_PNG\{self.filenames[rand]}'
        self.canvases[s].create_image(0, 0, anchor='nw',image=self.imgs[s])
        self.textes[s] = self.canvases[s].create_text(90, 290, text=str(s),fill="black",font=('Helvetica 12 bold'))
        self.canvases[s].bind("<B1-Motion>", self.drag2)

    
    def drag (self, event):
        mouse_x = self.canvas_main.winfo_pointerx() - self.canvas_main.winfo_rootx()
        mouse_y = self.canvas_main.winfo_pointery() - self.canvas_main.winfo_rooty()
        event.widget.place(x =mouse_x, y =mouse_y, anchor='nw')
    def drag2 (self, event):
        mouse_x = self.canvas_main2.winfo_pointerx() - self.canvas_main2.winfo_rootx()
        mouse_y = self.canvas_main2.winfo_pointery() - self.canvas_main2.winfo_rooty()
        event.widget.place(x =mouse_x, y =mouse_y, anchor='nw')




if __name__ == "__main__":
    main = Main()
