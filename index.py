from tkinter import *

#def buttonClick():
#    print("I am a blue tk.Button")
#WE WILL USE .grid() for this
#A_1.grid(row = random.choice(place), column = random.choice(place)) where A1 is the Label
#and place is a list and below is how you populate the list
class buttonGrid(Frame):

    def __init__(self):
        Frame.__init__(self)
        #no need to add window parameter next to self, as master defaults to None and
        #also each widget properly associates with its parent without speicification
        #super().__init__(self)
        buttons = []
        #colors = ["light slate grey", "royalblue1", "indian red", "coral1", "black", "brown", "purple", "orange", "pink"]
        colors = ["indian red", "dark orange", "gold2", "DodgerBlue3", "dark violet", "purple1", "RosyBrown3", "light slate grey", "seashell3"]
        def disableButton(index, highlightbackground):
                #priority.append(buttons[index].cget())
            priority.append(buttons[index].cget("highlightbackground"))
            buttons[index].config(state="disabled")
        for index in range(len(colors)):
            color = colors[index]
            #no need to mention this as self.button,
            #it is understood that the button's type is this class
            button=Button(self,text= index, highlightbackground = color, highlightthickness=30,
            command=lambda index=index, highlightbackground=color: disableButton(index, highlightbackground))

            # Add the button to the window
            button.grid(row=int(index%3), column=int(index/3))

            # Add a reference to the button to 'buttons'
            buttons.append(button)
            #print(buttons)
            #print(priority)
class quitClass(Frame):

    def __init__(self):
        Frame.__init__(self)
        #super().__init__(self)
        def quitCommand():
            print(priority)
            window.destroy()

        quitButton = Button(self, text = "Done" , command = quitCommand)
        quitButton.pack(side = "bottom")

        genderLabel = Label(self, text = "Please select your gender:")
        genderLabel.pack(side = "left")

        variable = StringVar(self)
        variable.set("Select") # default value
        #For dropdown
        genderCombo = OptionMenu(self, variable, "Select", "Male", "Female", "Other")
        genderCombo.pack(side = "left")

window = Tk()
window.title("How do you feel now?")
window.minsize(width=100, height=100)
window.geometry('500x310+0+0')
priority = []
frame1 = buttonGrid()
#frame1 = buttonGrid(window) -> It is not necessary to pass window as parameter
frame2 = quitClass()
frame1.pack(side = "top")
frame2.pack()
window.mainloop()
