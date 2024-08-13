import tkinter as ttk
from tkinter import *
from pygame import*
import time
import Temp7
import Temp5

#https://stackoverflow.com/questions/58581850/how-to-stop-mainloop-function-without-closing-window
#https://stackoverflow.com/questions/63779131/using-config-in-tkinter
#https://www.geeksforgeeks.org/python-after-method-in-tkinter/
#https://stackoverflow.com/questions/58299276/tkinter-window-not-updating-till-after-the-loop-is-done
#https://www.educative.io/answers/how-to-center-the-tkinter-label


def main_play_file(user, file):
    def play_note(x):
        mixer.music.load(x+".wav")
        mixer.music.play()
        time.sleep(0.3)
        mixer.music.stop()
        print(x)
    def loop(user):
        win.destroy()
        y = Temp7.input_return()
        if y == 1:
            Temp5.main_play_note()
        else:
            x = Temp7.file_return()
            main_play_file(user, x)
    def update_window(x, y, z,c = False):
        # global call
        play_note(x[y])
        notes_label.config(text = x[y])
        win.update()
        print("pop2")
        y += 1
        if y == z-2:
            print("pop1")
            win.after(300, update_window(x, y, z, True))
        elif c:
            play_note(x[y])
            notes_label.config(text = x[y])
            win.update()
            time.sleep(1)
            loop(user)

        else:
            win.after(300, update_window(x, y, z))
            # win.after_cancel(call)
            # win.update()
            # win.destroy()
    

    mixer.init()
    y = "Note"+str(file)+".txt"
    f = open("/home/nps/Downloads/Soundscapes-main/User"+str(user)+"/"+y, 'r')

    notes = f.read()
    notes = notes.strip("\n")
    notes = notes.split(" ")
    w = len(notes)
    print(w)

    win = Tk()
    win.title("Synthesizer")
    win.geometry("150x150")
    win.resizable = (False, False)

    notes_label = ttk.Label(win, text = "Notes")
    notes_label.place(relx = 0.5, y = 30, anchor=CENTER)

    q = 0

    start = ttk.Button(win,text = 'Start', command = lambda: update_window(notes, q,w))
    start.place(relx = 0.5, y = 90, anchor=CENTER)
    
    stop = ttk.Button(win, text="Stop", command=lambda: loop(user))
    stop.place(relx = 0.5, y = 120, anchor=CENTER)

    win.mainloop()
    # win.bind('<k>', lambda e: win.destroy())

    # for i in range(w):
    #     update_window(notes, i)
