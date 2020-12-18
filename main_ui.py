#!/usr/bin/env python3

from tkinter import *
import tkinter.messagebox as mbox
from tkinter import filedialog as fd


font_std = "Helvetica 12"


def quit_prog():
    sys.exit(0)


def return_error():
    mbox.showwarning(title=u"⚠ ️Error", message=u"Написано же:\nне нажимать!")
    sys.exit(1)


def open_file():
    file_path = fd.askopenfilename(defaultextension='.txt',
                                   filetypes=[('File Text', '*.txt'),
                                              ('All files', '*.*')])
    print(file_path)


def launch_ui():
    root = Tk()
    root.title('Python UI unit')
    root.resizable(width=False, height=False)

    frame_header = Frame(root, bg='green', bd=5)
    frame_chb = Frame(root, bg='red', bd=5)
    frame_result = Frame(root, bg='yellow', bd=5)
    frame_logger = Frame(root, bg='blue', bd=5)
    frame_footer = Frame(root, bg='white', bd=5)

    l_header = Label(frame_header, width=80, height=5, text="HEADER", bg="green")
    l_chb = Label(frame_chb, width=25, height=30, text="CHECKBOX", bg="red")
    l_rb = Label(frame_result, width=25, height=30, text="RADIOBUTTON", bg="yellow")
    l_logger = Label(frame_logger, width=50, height=30, text="WINDOW", bg="blue")
    main_btn = Button(frame_footer, font=font_std, bg="light gray", width=20, height=2, text=u"Кнопка",
                      command=open_file)
    error_btn = Button(frame_footer, font=font_std, bg="light gray", fg="red", width=20, height=2,
                       text=u"Не нажимать!!!", command=return_error)
    quit_btn = Button(frame_footer, font=font_std, bg="light gray", width=20, height=2, text=u"Выход",
                      command=quit_prog)

    frame_header.pack(side=TOP, fill=X, anchor=N)
    frame_footer.pack(side=BOTTOM, fill=X, anchor=S)
    frame_chb.pack(side=LEFT, fill=Y, anchor=NW)
    frame_result.pack(side=LEFT, fill=Y, anchor=NW)
    frame_logger.pack(side=RIGHT, expand=1, fill=BOTH, anchor=NE)
    main_btn.pack(anchor=SW, side='left')
    quit_btn.pack(anchor=SE, side='right')
    error_btn.pack(anchor='center', side='bottom')

    l_header.pack()
    l_chb.pack()
    l_rb.pack()
    l_logger.pack()

    root.mainloop()
