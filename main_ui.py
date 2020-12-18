#!/usr/bin/env python3

from tkinter import *
import tkinter.messagebox as mbox
from tkinter import ttk
from tkinter import filedialog as fd

font_std = "Helvetica 12"


def quit_prog():
    sys.exit(0)


def return_error():
    mbox.showwarning(title=u"⚠ ️Error", message=u"Написано же:\nне нажимать!")
    sys.exit(1)


class MainClass(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        self.master.title('Python UI unit')
        self.master.resizable(width=False, height=False)

        # Objects
        self.frame_header = Frame(self.master, bg='green', bd=5)
        self.frame_chb = Frame(self.master, bg='red', bd=5)
        self.frame_rb = Frame(self.master, bg='light gray', bd=5)
        self.frame_cb = Frame(self.master, bg='light blue', bd=5)
        self.frame_win = Frame(self.master, bg='gray', bd=5)
        self.frame_footer = Frame(self.master, bg='white', bd=5)

        self.text_win = Text(self.frame_win, font='Courier', width=30, height=15, bg='white')

        self.cbb = ttk.Combobox(self.frame_cb, width=3, values='')

        self.l_header = Label(self.frame_header, width=80, height=5, font=font_std + " bold", text="HEADER",
                              bg="dark green")

        r_var = BooleanVar()
        r_var.set(0)
        self.rbtn1 = Radiobutton(self.frame_rb, text='1', variable=r_var, value=0)
        self.rbtn2 = Radiobutton(self.frame_rb, text='2', variable=r_var, value=1)
        self.rbtn3 = Radiobutton(self.frame_rb, text='3', variable=r_var, value=2)

        self.l_chb = Label(self.frame_chb, width=25, height=30, text="CHECKBOX", bg="red")
        self.l_rb = Label(self.frame_rb, width=25, height=30, text="RADIOBUTTON", bg="light green")
        self.l_cbb = Label(self.frame_cb, width=25, text="Выбрать:", bg="light blue")

        self.main_btn = Button(self.frame_footer, font=font_std, bg="light gray", width=20, height=2, text=u"Открыть файл",
                               command=self.open_file)
        self.error_btn = Button(self.frame_footer, font=font_std + " bold", bg="light gray", fg="red", width=20,
                                height=2,
                                text=u"Не нажимать!!!", command=return_error)
        self.quit_btn = Button(self.frame_footer, font=font_std, bg="light gray", width=20, height=2, text=u"Выход",
                               command=quit_prog)

        # Pack
        self.frame_header.pack(side=TOP, fill=X, anchor=N)
        self.frame_footer.pack(side=BOTTOM, fill=X, anchor=S)
        self.frame_chb.pack(side=LEFT, fill=Y, anchor=NW)
        self.frame_win.pack(side=RIGHT, expand=1, fill=BOTH, anchor=NE)
        self.frame_cb.pack(side=TOP, fill=BOTH, anchor=S)
        self.frame_rb.pack(side=BOTTOM, fill=Y, anchor=N)

        self.main_btn.pack(anchor=SW, side='left')
        self.quit_btn.pack(anchor=SE, side='right')
        self.error_btn.pack(anchor='center', side='bottom')

        self.text_win.pack(anchor=W, expand=1, fill=BOTH)
        self.l_cbb.pack()
        self.cbb.pack(side='top', fill=BOTH)

        self.rbtn1.pack(side=TOP, anchor=NW)
        self.rbtn2.pack(side=TOP, anchor=NW)
        self.rbtn3.pack(side=TOP, anchor=NW)

        self.l_header.pack()
        self.l_chb.pack()
        self.l_rb.pack()

    def open_file(self):
        file_path = fd.askopenfilename(defaultextension='.txt',
                                       filetypes=[('File Text', '*.txt'),
                                                  ('All files', '*.*')])
        try:
            filename = open(file_path, "r", encoding='utf-8')
            print(file_path)
            content = filename.read()
            self.text_win.insert(END, content)
        except Exception:
            pass


def launch_ui():
    root = Tk()
    ui = MainClass(master=root)
    ui.mainloop()
