from tkinter import *
from visual import *

win = Tk()

class Setup:
     def __init__(self, icon):
          self.icon = icon
          self.title = "ConsoleRPG"
          self.bgColor = "#323232"
          self.geo = "640x480"

          Visual(win, self.bgColor)

          self.setup()
     
     def setup(self):
          self.menu()

     def menu(self):
          menu1 = Menu(win)
          menu1.add_cascade(label="file")
          menu1.add_cascade(label="options")
          menu1.add_cascade(label="help")

          self.start(menu1)

     def start(self, menu):
          win.title(self.title)
          win.iconbitmap(self.icon)
          win.config(bg = self.bgColor, menu = menu)
          win.geometry(self.geo)
          win.maxsize(640, 480)
          win.minsize(640, 480)
          self.run()

     def run(self):
          win.mainloop()
