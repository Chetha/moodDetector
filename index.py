import tkinter as tk
import random

#def buttonClick():
#    print("I am a blue button")

window = tk.Tk()

window.title("How do you feel now?")
window.minsize(width=300, height=50)
window.maxsize(width=300, height=50)


#WE WILL USE .grid() for this
#A_1.grid(row = random.choice(place), column = random.choice(place)) where A1 is the Label
#and place is a list and below is how you populate the list
place = []

for i in range(8):
    place.append(i)

#blueButton = tk.Button(window, width = 25, bg = 'blue', command = quit)
blueButton = tk.Button(window, width = 25 , highlightbackground='blue', command = quit)
blueButton.pack()

window.mainloop()
