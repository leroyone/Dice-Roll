#!/usr/bin/python

import Tkinter

class theApp(Tkinter.Tk):
    def __init__(self, parent):
        Tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.geometry('387x415+422+195')
        self.initialize()

    def initialize(self):
        self.grid()
        #### first line
        Tkinter.Label(self).grid(row=0)
        #### second line
        Tkinter.Label(self).grid(row=1, column=0, padx=30)

        effort = Tkinter.StringVar()
        label = Tkinter.Label(self, textvariable=effort, anchor='e')
        label.grid(row=1, column=1, sticky='EW')
        effort.set('How many dice? ')

        self.entryVariable = Tkinter.StringVar()
        self.entry = Tkinter.Entry(self, textvariable=self.entryVariable)
        self.entry.grid(row=1, column=2)
        self.entry.bind('<Return>', self.onPressEnter)
        self.entryVariable.set('1')

        Tkinter.Label(self).grid(row=1, column=3, padx=30)
        #### third line
        self.button = Tkinter.Button(self, text='ROLL!', font=70, command=self.onButtonClick)
        self.button.grid(row=2, column=0, pady=15, columnspan=4)
        #### fourth line
        ''' 
        photo0 = Tkinter.PhotoImage(file="images/5.gif")
        label = Tkinter.Label(self, image=photo0)
        label.grid(row=3, column=0, columnspan=2, pady=20)
        label.image = photo0
        
        photo1 = Tkinter.PhotoImage(file="images/1.gif")
        label = Tkinter.Label(self, image=photo1)
        label.grid(row=3, column=1, columnspan=4)
        label.image = photo1
        
        photo2 = Tkinter.PhotoImage(file="images/1.gif")
        label = Tkinter.Label(self, image=photo2)
        label.grid(row=3, column=3, columnspan=1)
        label.image = photo2
        #### fifth line
        photo3 = Tkinter.PhotoImage(file="images/5.gif")
        label = Tkinter.Label(self, image=photo3)
        label.grid(row=4, column=0, columnspan=2, pady=20)
        label.image = photo3

        photo4 = Tkinter.PhotoImage(file="images/1.gif")
        label = Tkinter.Label(self, image=photo4)
        label.grid(row=4, column=1, columnspan=4)
        label.image = photo4

        photo5 = Tkinter.PhotoImage(file="images/1.gif")
        label = Tkinter.Label(self, image=photo5)
        label.grid(row=4, column=3, columnspan=1)
        label.image = photo5
        '''
        #### some other gubbins
        self.grid_columnconfigure(0, weight=1)
        self.resizable(False,False)
        self.button.focus_set()

    def buttonything(self, howMany):
        try:
            homMany = int(howMany)
        except:
            pass

    def onButtonClick(self):
        try:
            int(self.entryVariable.get())
            self.button.focus_set()
        except:
            pass

    def onPressEnter(self, event):
        #self.labelVariable.set(self.entryVariable.get()+'(You pressed enter!)')
        self.button.focus_set()

if __name__ == "__main__":
    app = theApp(None)
    app.title('Dice Roll App')
    app.mainloop()
