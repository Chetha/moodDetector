#https://www.datacamp.com/community/tutorials/gui-tkinter-python
import tkinter as tk

#As a next step, you initialize the window manager with the tkinter.Tk() method and assign it to a variable. This method creates a blank window with
#close, maximize, and minimize buttons on the top as a usual GUI should have
window = tk.Tk()

#Renaming the title of the window, this is optional
window.title("How do you feel now?")

#WE WILL USE .grid() for this
#A_1.grid(row = random.choice(place), column = random.choice(place)) where A1 is the Label
#and place is a list and below is how you populate the list
'''
    place = []

    nums  = [0, 1]

    for i in range(8):

        place.append(i)
'''


#Finally, as the last step, you use the mainloop() method to display the window until you manually close it.
#It runs an infinite loop in the backend.
window.mainloop()
