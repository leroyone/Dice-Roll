#!/usr/bin/python

import Tkinter
import random

class theApp(Tkinter.Tk):
    def __init__(self, parent):
        Tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.geometry('317x415+422+195')
        self.initialize()

    def initialize(self):
        self.grid()
        #### first line
        for each in range(12):
            Tkinter.Label(self).grid(row=0, column=each)
        #### second line
        effort = Tkinter.StringVar()
        label = Tkinter.Label(self, textvariable=effort, anchor='e')
        label.grid(row=1, column=0, columnspan=6)
        effort.set('How many dice? ')

        self.entryVariable = Tkinter.StringVar()
        self.entry = Tkinter.Entry(self, textvariable=self.entryVariable)
        self.entry.grid(row=1, column=6, columnspan=6)
        self.entry.bind('<Return>', self.onPressEnter)
        self.entryVariable.set('1')
        #### third line
        self.button = Tkinter.Button(self, text='ROLL!', font=70, command=self.onButtonClick)
        self.button.grid(row=2, column=0, pady=15, columnspan=12)
        #### fourth line
        self.notNumber = Tkinter.StringVar()
        errorLabel = Tkinter.Label(self, textvariable=self.notNumber)
        errorLabel.grid(row=3, columnspan=12)
        self.notNumber.set('')
        #### fourth line
        self.blankPhoto = Tkinter.PhotoImage(file="images/blank.gif")
        label0 = Tkinter.Label(self, image=self.blankPhoto)
        label0.grid(row=4, column=0, columnspan=4)
        label0.image = self.blankPhoto

        label1 = Tkinter.Label(self, image=self.blankPhoto)
        label1.grid(row=4, column=4, columnspan=4)
        label1.image = self.blankPhoto
        
        label2 = Tkinter.Label(self, image=self.blankPhoto)
        label2.grid(row=4, column=8, columnspan=4)
        label2.image = self.blankPhoto
        #### fifth line
        label3 = Tkinter.Label(self, image=self.blankPhoto)
        label3.grid(row=5, column=0, columnspan=4)
        label3.image = self.blankPhoto

        label4 = Tkinter.Label(self, image=self.blankPhoto)
        label4.grid(row=5, column=4, columnspan=4)
        label4.image = self.blankPhoto

        label5 = Tkinter.Label(self, image=self.blankPhoto)
        label5.grid(row=5, column=8, columnspan=4)
        label5.image = self.blankPhoto

        self.labelList = [label0, label1, label2, label3, label4, label5]
        #### some other gubbins
        #self.grid_columnconfigure(0, weight=1)
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
        self.notNumber.set('')
        for each in range(howMany):
            x = random.randint(1,6)
            photo = Tkinter.PhotoImage(file="images/" + str(x) + ".gif")
            self.labelList[each].configure(image = photo)
            self.labelList[each].image = photo
        for every in range(howMany,6):
            self.labelList[every].configure(image = self.blankPhoto)
            self.labelList[every].image = self.blankPhoto

    def onButtonClick(self):
        try:
            self.entryVariable.get() < 7
            self.buttonything(int(self.entryVariable.get()))
            self.button.focus_set()
        except:
            for each in self.labelList:
                each.configure(image = self.blankPhoto)
                each.image = ""
            try:
                int(self.entryVariable.get())
                self.notNumber.set('Sorry. I only have 6 dice.')
            except:
                self.notNumber.set('That is not a number!')
            self.entry.focus_set()
            self.entry.selection_range(0, Tkinter.END)

    def onPressEnter(self, event):
        #self.labelVariable.set(self.entryVariable.get()+'(You pressed enter!)')
        self.button.focus_set()

if __name__ == "__main__":
    app = theApp(None)
    app.title('Dice Roll')
    app.mainloop()
