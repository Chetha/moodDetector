import tkinter as tk
import random

#def buttonClick():
#    print("I am a blue tk.Button")

window = tk.Tk()

window.title("How do you feel now?")
window.minsize(width=100, height=100)
window.geometry('500x310+0+0')


#WE WILL USE .grid() for this
#A_1.grid(row = random.choice(place), column = random.choice(place)) where A1 is the Label
#and place is a list and below is how you populate the list
buttons = []

colors = ["red", "blue", "green", "thistle4", "black", "brown", "purple", "orange", "pink"]
def disableButton(index, button):
    

for index in range(9):
    color = colors[index]
    button=tk.Button(window,text= index, highlightbackground = color,
    command=lambda index=index, color=color: disableButton(index, button))

    # Add the button to the window
    button.grid(padx=2, pady=2, row=int(index%3), column=int(index/3))

    # Add a reference to the button to 'buttons'
    buttons.append(button)
    print(buttons)

window.mainloop()



'''
button1=tk.Button(window,text="B1", highlightbackground = "thistle4", )
button1.grid(row=1,column=1)

button2=tk.Button(window, text="B2", highlightbackground = "blue")
button2.grid(row=1,column=2)

button3=tk.Button(window,text="B3", highlightbackground = "thistle4")
button3.grid(row=1,column=3)

button4=tk.Button(window,text="B4", highlightbackground = "thistle4")
button4.grid(row=2,column=1)

button5=tk.Button(window,text="B5", highlightbackground = "thistle4")
button5.grid(row=2,column=2)

button6=tk.Button(window,text="B6", highlightbackground = "thistle4")
button6.grid(row=2,column=3)

button7=tk.Button(window,text="B7", highlightbackground = "thistle4")
button7.grid(row=3,column=1)

button8=tk.Button(window,text="B8", highlightbackground = "thistle4")
button8.grid(row=3,column=2)

button9=tk.Button(window,text="B9", highlightbackground = "thistle4")
button9.grid(row=3,column=3)
'''
window.mainloop()
