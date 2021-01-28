from tkinter import *
import sys
from commands import *

class Visual():
    def __init__(self, win, BGhistory):
        self.win = win

        self.entry = Entry(self.win, bg="#323232", width=640, bd=3, fg="#e6e6e6")
        self.Lhistory = Label(self.win, text="History", bg='#323232', fg="#e6e6e6")
        self.terminal = Listbox(self.win, bg='#323232', fg="#e6e6e6", width=100)
        self.history = Listbox(self.win, bg='#323232', fg='#e6e6e6')

        self.BGhistory = BGhistory
        self.History = []
        self.HistoryLen = len(self.History)
        self.PlayerCommmand = Commandplayer(self.terminal)
        self.start()

    def start(self):
        self.visual()
        def keyHandler(event):
             if event.keycode == 13:
                self.history.delete(first=0, last=END)
                self.submitValues()

        self.win.bind("<Key>", keyHandler)

    def visual(self):
        ListPack = [self.entry, self.Lhistory, self.history, self.terminal]

        self.packing(ListPack)

    def submitValues(self):
        result = self.entry.get()
        self.PlayerCommmand.terminalOutput(result)
        print('result:', result)
        def insert():
            for i in self.History:
                self.history.insert(self.HistoryLen, i)
                self.history.pack()

        if result == "":
            print("nothing")
            insert()
        else:
            self.History.append(result)
            print(self.History)
            insert()

        self.entry.delete(first=0, last=1000)
        return result

    def packing(self, ListPack):
        for x in ListPack:
            x.pack()