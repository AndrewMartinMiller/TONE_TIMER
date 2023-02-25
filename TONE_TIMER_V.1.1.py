{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "20aebd82",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "00:54\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "invalid command name \"4524738432update_color\"\n",
      "    while executing\n",
      "\"4524738432update_color\"\n",
      "    (\"after\" script)\n"
     ]
    }
   ],
   "source": [
    "import tkinter as tk\n",
    "import os\n",
    "\n",
    "def update_color(i):\n",
    "    mins, secs = divmod(t-i, 60)\n",
    "    timer = '{:02d}:{:02d}'.format(mins, secs)\n",
    "    print(timer, end=\"\\r\")\n",
    "    color = tuple(int(sc - step_size[k] * i) for k, sc in enumerate(start_color))\n",
    "    color = \"#%02x%02x%02x\" % color\n",
    "    root.configure(background=color)\n",
    "    if i < t:\n",
    "        root.after(1000, update_color, i+1)\n",
    "        if i < t:\n",
    "            if t-i == 2:\n",
    "                os.system('say \"Times up Fuck Face\"')\n",
    "\n",
    "                \n",
    "def countdown():\n",
    "    # create GUI window\n",
    "    global root\n",
    "    root = tk.Tk()\n",
    "    root.title(\"TONE TIMER\")\n",
    "    root.geometry(\"300x300\")\n",
    "    \n",
    "    # create user input field\n",
    "    time_label = tk.Label(root, text=\"MINS:\", font=(\"Helvetica\", 9))\n",
    "    time_label.grid(row=1, column=0)\n",
    "    time_label.configure(highlightthickness=0, highlightbackground=root.cget('bg'))  \n",
    "    time_entry = tk.Entry(root)\n",
    "    time_entry.grid(row=1, column=1)\n",
    "    time_entry.configure(bg=\"white\", fg=\"black\", font=(\"Helvetica\", 9))\n",
    "    time_entry.configure(highlightthickness=0, highlightbackground=root.cget('bg'))\n",
    "\n",
    "    def reset_timer():\n",
    "        \n",
    "        time_label.grid(row=0, column=0)\n",
    "        time_entry.grid(row=0, column=1)\n",
    "        start_button.grid(row=1, column=0, columnspan=1)\n",
    "        reset_button.grid_forget()\n",
    "\n",
    "        # destroy current GUI window and restart countdown\n",
    "        root.destroy()\n",
    "        countdown()\n",
    "\n",
    "    def start_timer():\n",
    "        # get user input from entry field and convert to seconds\n",
    "        try:\n",
    "            global t\n",
    "            t = int(time_entry.get()) * 60\n",
    "        except ValueError:\n",
    "            t = 0\n",
    "\n",
    "\n",
    "        # define starting and ending colors\n",
    "        global start_color\n",
    "        start_color = (255, 255, 255)  # white\n",
    "        end_color = (0, 0, 0)   # black\n",
    "\n",
    "        # define color step size\n",
    "        global step_size\n",
    "        step_size = [(sc - ec) / t for sc, ec in zip(start_color, end_color)]\n",
    "        \n",
    "        # call the update_color func.\n",
    "        update_color(0)\n",
    "\n",
    "        root.configure() # Set the final color to black\n",
    "        root.update()\n",
    "        \n",
    "        # hide the label, input field, and start button\n",
    "        time_label.grid_forget()\n",
    "        time_entry.grid_forget()\n",
    "        start_button.grid_forget()\n",
    "\n",
    "    start_button = tk.Button(root, text=\"START\", command=start_timer)\n",
    "    start_button.grid(row=1, column=0, columnspan=1)\n",
    "    start_button.configure(bg=\"white\", fg=\"black\", font=(\"Helvetica\", 9))\n",
    "    start_button.configure(highlightthickness=0, highlightbackground=root.cget('bg'))\n",
    "    reset_button = tk.Button(root, text=\"RESET\", command=reset_timer)\n",
    "    reset_button.grid(row=2, column=0, columnspan=1)\n",
    "    reset_button.configure(bg=\"white\", fg=\"black\", font=(\"Helvetica\", 9))\n",
    "    reset_button.configure(highlightthickness=0, highlightbackground=root.cget('bg'))\n",
    "\n",
    "    # close the GUI window\n",
    "    root.mainloop()\n",
    "\n",
    "# call the countdown func.\n",
    "countdown()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cdb3f50f",
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "\n",
    "\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.1"
  },
  "vscode": {
   "interpreter": {
    "hash": "aee8b7b246df8f9039afb4144a1f6fd8d2ca17a180786b69acc140d282b71a49"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
