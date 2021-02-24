#!/usr/bin/env python3

from tkinter import *
import tkinter.messagebox as mbox
from tkinter import ttk
from tkinter import filedialog as fd
import calendar

font_std = "Helvetica 12"


def quit_prog():
    sys.exit(0)


def return_error():
    mbox.showwarning(title=u"⚠ ️Error", message=u"Написано же:\nне нажимать!")
    sys.exit(1)


class MonthList:
    def __init__(self, r_var, name, parent, i):
        self.rb = Radiobutton(parent, text=name, bg='light yellow', activebackgroun='light yellow',
                              highlightbackground='light yellow', font=font_std + " italic", variable=r_var, value=i)
        self.rb.pack(side=TOP, anchor=NW)


class DaysList:
    def __init__(self, name, parent):
        self.flag = IntVar()
        self.flag.set(1)
        self.chb = Checkbutton(parent, text=name, bg='dark red', activebackground='dark red', highlightbackground="red",
                               onvalue=1, offvalue=0, variable=self.flag)
        self.chb.pack(side=TOP, anchor=NW)


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
        self.frame_rb = Frame(self.master, bg='light yellow', bd=5)
        self.frame_cb = Frame(self.master, bg='pink', bd=5)
        self.frame_win = Frame(self.master, bg='dark blue', bd=5)
        self.frame_footer = Frame(self.master, bg='dark violet', bd=5)

        self.text_win = Text(self.frame_win, font='Courier', width=30, height=15, bg='light blue')

        self.cbb = ttk.Combobox(self.frame_cb, width=3, values='')

        self.l_header = Label(self.frame_header, width=80, height=5, font=font_std + " italic bold", text="HEADER",
                              bg="dark green", fg="light green")

        r_var = BooleanVar()
        r_var.set(0)
        months_str = calendar.month_name
        self.month_list = list()
        i = 0
        for month in months_str[1::]:
            i += 1
            self.rb = MonthList(r_var, month, self.frame_rb, i)
            self.month_list.append(self.rb)

        self.f_chb = Frame(self.frame_chb, bg='dark red', bd=5)
        self.f_chb.pack(side=LEFT, fill=BOTH, anchor=NW)
        days_str = calendar.day_name
        self.chb_list = list()
        for day in days_str:
            self.chb = DaysList(day, self.f_chb)
            self.chb.flag.set(1)
            self.chb_list.append(self.chb)

        self.l_rb = Label(self.frame_rb, width=25, height=15, text="•", bg="yellow")
        self.l_cbb = Label(self.frame_cb, width=25, text="Выбрать:", bg="magenta")

        self.main_btn = Button(self.frame_footer, font=font_std + " bold", bg="dark magenta", width=20, height=2,
                               text=u"Открыть файл", activebackground='green', fg="white", command=self.open_file)
        self.error_btn = Button(self.frame_footer, font=font_std + " bold", bg="white", fg="red", width=20,
                                height=2, activebackground='red', activeforeground='white',
                                text=u"Не нажимать!!!", command=return_error)
        self.quit_btn = Button(self.frame_footer, font=font_std + " bold", bg="dark magenta", width=20, height=2,
                               text=u"Выход", activebackground='green', fg="white", command=quit_prog)

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

        self.l_header.pack()
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
