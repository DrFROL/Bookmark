from tkinter import *
import tkinter.ttk as ttk
import datetime


def OnDoubleClick(event):
    global iid
    sel = Tk()
    sel.title('Bookmark')
    sel.minsize(width=430, height=430)
    f = open(str(iid) + '.txt', "r")
    for i in f:
        txt = i
    f.close()
    t = Message(sel,bg="White",width=430,text=txt)
    t.pack()

    sel.meinloop()


def row(event):
    def OnOneClick(event):
        global iid
        global now
        ss = entry.get()
        fl = entry2.get()
        tx = text.get("1.0", END)
        iid = 0
        f = open('f.txt', 'r')
        for rw in f:
            if int(rw[0]) >= iid:
                iid=int(rw[0])
                iid = iid + 1
                print(rw[0])
        f.close()

        tree.insert('', index='end',iid=iid, text="Parent", values=(iid,fl,now.strftime("%d.%m.%Y"), ss))


        # Создание файла

        f = open(str(iid) + '.txt', "w")

        f.write(fl +'\n')
        f.write('    '+'\n')
        f.write(ss +'\n')
        f.write('    '+'\n')
        f.write(tx)

        f.close()

        f = open('f.txt', "a")

        f.write(str(iid) + ' ')
        f.write(fl + ' ')
        f.write(now.strftime("%d.%m.%Y") + ' ')
        f.write(ss + ' ' + '\n')
        #list = [fl, now.strftime("%d.%m.%Y"), ss ]
        #with open("f.txt", "a") as file:
            #print(list, file=file)
        f.close()

        root.destroy()

    def OnOneClick1(event):
        root.destroy()

    root = Tk()
    root.title('Bookmark')
    root.configure(background="White")
    root.maxsize(width=480, height=400)
    root.minsize(width=480, height=400)

    lebel1 = Label(root, text='Ссылка', bg='white', fg='#A8A6A6')
    lebel1.place(relx=0.09, rely=0.08)

    entry = Entry(root, bg='#E0E0E0', bd=0,fg='#A8A6A6')
    entry.place(relx=0.1, rely=0.14, relwidth=0.52, relheight=0.1)

    lebel2 = Label(root, text='Название', bg='white')
    lebel2.place(relx=0.09, rely=0.24)

    entry2 = Entry(root, bg='#F2F2F2', bd=0)
    entry2.place(relx=0.1, rely=0.3, relwidth=0.52, relheight=0.1)

    lebel3 = Label(root, text='Текст', bg='white')
    lebel3.place(relx=0.09, rely=0.42)

    text = Text(root, bg='#F2F2F2', width=31, height=9, bd=0)
    text.place(relx=0.1, rely=0.48)

    button1 = Button(root, bg='#F2F2F2', text='Готово', bd=0)
    button1.place(relx=0.68, rely=0.9)

    button2 = Button(root, bg='#F2F2F2', text='Отмена', bd=0)
    button2.place(relx=0.8, rely=0.9)

    button1.bind("<Button-1>", OnOneClick)
    button2.bind("<Button-1>", OnOneClick1)

    root.mainloop()


self = Tk()

self.title('Bookmark')
self.iconphoto(True, PhotoImage(file=r"C:\Users\Пользователь\Desktop\проекь\rr.png"))
self.configure(background="White")
self.minsize(width=899, height=530)

now = datetime.datetime.now()

button = Button(self,bg='#F2F2F2',text='+Добавить',bd=0)
button.place(rely=0.001)
button.bind("<Button-1>", row)

tree = ttk.Treeview(self, show="headings", height=333)
scroll = ttk.Scrollbar(self, orient=VERTICAL)
scroll.configure(command=tree.yview)
tree.configure(yscrollcommand=scroll.set)

scroll.place(relx=0.98,rely=0.05, height=333)
tree.place(rely=0.05)

tree['columns'] = ("№",'Название', 'Дата', 'Ссылка', 'o')

tree.column('№', width=30)
tree.column('Название', width=200)
tree.column('Дата', width=61)
tree.column('o', width=360)

tree.heading('№', text='№', anchor='w')
tree.heading('Название', text='Название', anchor='w')
tree.heading('Дата', text='Дата', anchor='w')
tree.heading('Ссылка', text='Ссылка', anchor='w')
tree.heading('o', text='', anchor='w')

f = open('f.txt','r')
for rw in f:
    tree.insert('', index='end', iid=rw[0], values=rw)

f.close()
tree.insert('', index='end', text="Parent", values=('test', '01.12.21', 'test'))


tree.bind("<Button-1>", OnDoubleClick)




self.mainloop()
