#!/usr/bin/python

import Tkinter
import random

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
 
        label0 = Tkinter.Label(self, image="")
        label0.grid(row=3, column=0, columnspan=2, pady=20)
        label0.image = ""
        
        label1 = Tkinter.Label(self, image="")
        label1.grid(row=3, column=1, columnspan=4)
        label1.image = ""
        
        label2 = Tkinter.Label(self, image="")
        label2.grid(row=3, column=3, columnspan=1)
        label2.image = ""
        #### fifth line
        label3 = Tkinter.Label(self, image="")
        label3.grid(row=4, column=0, columnspan=2, pady=20)
        label3.image = ""

        label4 = Tkinter.Label(self, image="")
        label4.grid(row=4, column=1, columnspan=4)
        label4.image = ""

        label5 = Tkinter.Label(self, image="")
        label5.grid(row=4, column=3, columnspan=1)
        label5.image = ""

        self.labelList = [label0, label1, label2, label3, label4, label5]
        #### some other gubbins
        self.grid_columnconfigure(0, weight=1)
        self.resizable(False,False)
        self.button.focus_set()

    ''' 
    def buttonything(self, howMany):
        for each in range(howMany):
            if each%3 == 2:
                col = 3
                span = 1
            else:
                col = each%3
                span = (each%3+1)*2
            x = random.randint(1,6)
            photo = Tkinter.PhotoImage(file="images/" + str(x) + ".gif")
            labelList[howMany] = Tkinter.Label(self, image=photo)
            labelList[howMany].grid(row=each/3+3, column=col, columnspan=span, pady=20)
            labelList[howMany].image = photo
    '''
    def buttonything(self, howMany):
        for each in range(howMany):
            x = random.randint(1,6)
            photo = Tkinter.PhotoImage(file="images/" + str(x) + ".gif")
            self.labelList[each].configure(image = photo)
            self.labelList[each].image = photo
        for every in range(howMany,6):
            self.labelList[every].configure(image = "")
            self.labelList[every].image = ""

    def onButtonClick(self):
        try:
            self.buttonything(int(self.entryVariable.get()))
            self.button.focus_set()
        except:
            for each in self.labelList:
                each.configure(image = "")
                each.image = ""
            notNumber = Tkinter.StringVar()
            self.labelList[1].configure(textvariable=notNumber)
            notNumber.set('That is not a number!')
            self.entry.focus_set()
            self.entry.selection_range(0, Tkinter.END)

    def onPressEnter(self, event):
        #self.labelVariable.set(self.entryVariable.get()+'(You pressed enter!)')
        self.button.focus_set()

if __name__ == "__main__":
    app = theApp(None)
    app.title('Dice Roll App')
    app.mainloop()
