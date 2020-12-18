#!/usr/bin/env python3

from tkinter import *


def launch_ui():
    root = Tk()
    root.resizable(width=False, height=False)

    frame_header = Frame(root, bg='green', bd=5)
    frame_chb = Frame(root, bg='red', bd=5)
    frame_result = Frame(root, bg='yellow', bd=5)
    frame_logger = Frame(root, bg='blue', bd=5)
    frame_btns = Frame(root, bg='white', bd=5)

    l_header = Label(frame_header, width=80, height=5, text="HEADER", bg="green")
    l_chb = Label(frame_chb, width=25, height=30, text="CHECKBOX", bg="red")
    l_rb = Label(frame_result, width=25, height=30, text="RADIOBUTTON", bg="yellow")
    l_logger = Label(frame_logger, width=50, height=30, text="WINDOW", bg="blue")
    l_btns = Label(frame_btns, width=80, height=5, text="BUTTONS", bg="white")

    frame_header.pack(side=TOP, fill=X, anchor=N)
    frame_btns.pack(side=BOTTOM, fill=X, anchor=S)
    frame_chb.pack(side=LEFT, fill=Y, anchor=NW)
    frame_result.pack(side=LEFT, fill=Y, anchor=NW)
    frame_logger.pack(side=RIGHT, expand=1, fill=BOTH, anchor=NE)

    l_header.pack()
    l_chb.pack()
    l_rb.pack()
    l_logger.pack()
    l_btns.pack()

    root.mainloop()
