#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
import os

def update_color(i):
    mins, secs = divmod(t-i, 60)
    timer = '{:02d}:{:02d}'.format(mins, secs)
    print(timer, end="\r")
    color = tuple(int(sc - step_size[k] * i) for k, sc in enumerate(start_color))
    color = "#%02x%02x%02x" % color
    root.configure(background=color)
    if i < t:
        root.after(1000, update_color, i+1)
        if i < t:
            if t-i == 2:
                os.system('say "BLEEP, BLEEP, BLEEP"')

                
def countdown():
    # create GUI window
    global root
    root = tk.Tk()
    root.title("TONE TIMER")
    root.geometry("300x300")
    
    # create user input field
    time_label = tk.Label(root, text="MINS:", font=("Helvetica", 9))
    time_label.grid(row=1, column=0)
    time_label.configure(highlightthickness=0, highlightbackground=root.cget('bg'))  
    time_entry = tk.Entry(root)
    time_entry.grid(row=1, column=1)
    time_entry.configure(bg="white", fg="black", font=("Helvetica", 9))
    time_entry.configure(highlightthickness=0, highlightbackground=root.cget('bg'))

    def reset_timer():
        
        time_label.grid(row=0, column=0)
        time_entry.grid(row=0, column=1)
        start_button.grid(row=1, column=0, columnspan=1)
        reset_button.grid_forget()

        # destroy current GUI window and restart countdown
        root.destroy()
        countdown()

    def start_timer():
        # get user input from entry field and convert to seconds
        try:
            global t
            t = int(time_entry.get()) * 60
        except ValueError:
            t = 0


        # define starting and ending colors
        global start_color
        start_color = (255, 255, 255)  # white
        end_color = (0, 0, 0)   # black

        # define color step size
        global step_size
        step_size = [(sc - ec) / t for sc, ec in zip(start_color, end_color)]

        def update_color(i):
            mins, secs = divmod(t-i, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            color = tuple(int(sc - step_size[k] * i) for k, sc in enumerate(start_color))
            color = "#%02x%02x%02x" % color
            root.configure(background=color)
            if i < t:
                root.after(1000, update_color, i+1)
                if i < t:
                    if t-i == 10:
                        os.system('say "Times up Fuck Face"')
        
        # call the update_color func.
        update_color(0)

        root.configure() # Set the final color to black
        root.update()
        
        # hide the label, input field, and start button
        time_label.grid_forget()
        time_entry.grid_forget()
        start_button.grid_forget()

    start_button = tk.Button(root, text="START", command=start_timer)
    start_button.grid(row=1, column=0, columnspan=1)
    start_button.configure(bg="white", fg="black", font=("Helvetica", 9))
    start_button.configure(highlightthickness=0, highlightbackground=root.cget('bg'))
    reset_button = tk.Button(root, text="RESET", command=reset_timer)
    reset_button.grid(row=2, column=0, columnspan=1)
    reset_button.configure(bg="white", fg="black", font=("Helvetica", 9))
    reset_button.configure(highlightthickness=0, highlightbackground=root.cget('bg'))

    # close the GUI window
    root.mainloop()

# call the countdown func.
countdown()


# In[ ]:




