import tkinter as tk
from tkinter import *
from tkinter import ttk
from pygame import*
import time
from PIL import ImageTk, Image


#function for playing a note
def main_play_note():
    #main window of the note input
    win = tk.Tk()
    win.title("Sythesizer")
    win.geometry("750x350")
    win.resizable(True,True)
    bg = ImageTk.PhotoImage(Image.open("T2.png"))
    label1 = Label(win, image = bg)
    label1.place(x = -1, y = -1)
    def play_note(x):
        mixer.music.load(x)
        mixer.music.play()
        time.sleep(0.3)
        mixer.music.stop()
        print(x)

    mixer.init()

    #https://stackoverflow.com/questions/6920302/how-to-pass-arguments-to-a-button-command-in-tkinter
    #https://www.tutorialspoint.com/python/tk_place.htm

    button_A1 = ttk.Button(win, text="A1",width= 7, command = lambda: play_note("A1.wav"))
    button_A2 = ttk.Button(win, text="A2",width= 7, command = lambda: play_note("A2.wav"))
    button_A3 = ttk.Button(win, text="A3",width= 7, command = lambda: play_note("A3.wav"))
    button_A4 = ttk.Button(win, text="A4",width= 7, command = lambda: play_note("A4.wav"))
    button_A5 = ttk.Button(win, text="A5",width= 7, command = lambda: play_note("A5.wav"))
    button_A6 = ttk.Button(win, text="A6",width= 7, command = lambda: play_note("A6.wav"))
    button_A7 = ttk.Button(win, text="A7",width= 7, command = lambda: play_note("A7.wav"))

    button_B1 = ttk.Button(win, text="B1",width= 7, command = lambda: play_note("B1.wav"))
    button_B2 = ttk.Button(win, text="B2",width= 7, command = lambda: play_note("B2.wav"))
    button_B3 = ttk.Button(win, text="B3",width= 7, command = lambda: play_note("B3.wav"))
    button_B4 = ttk.Button(win, text="B4",width= 7, command = lambda: play_note("B4.wav"))
    button_B5 = ttk.Button(win, text="B5",width= 7, command = lambda: play_note("B5.wav"))
    button_B6 = ttk.Button(win, text="B6",width= 7, command = lambda: play_note("B6.wav"))
    button_B7 = ttk.Button(win, text="B7",width= 7, command = lambda: play_note("B7.wav"))

    button_C1 = ttk.Button(win, text="C1",width= 7, command = lambda: play_note("C1.wav"))
    button_C2 = ttk.Button(win, text="C2",width= 7, command = lambda: play_note("C2.wav"))
    button_C3 = ttk.Button(win, text="C3",width= 7, command = lambda: play_note("C3.wav"))
    button_C4 = ttk.Button(win, text="C4",width= 7, command = lambda: play_note("C4.wav"))
    button_C5 = ttk.Button(win, text="C5",width= 7, command = lambda: play_note("C5.wav"))
    button_C6 = ttk.Button(win, text="C6",width= 7, command = lambda: play_note("C6.wav"))
    button_C7 = ttk.Button(win, text="C7",width= 7, command = lambda: play_note("C7.wav"))
    button_C8 = ttk.Button(win, text="C8",width= 7, command = lambda: play_note("C8.wav"))

    button_D1 = ttk.Button(win, text="D1",width= 7, command = lambda: play_note("D1.wav"))
    button_D2 = ttk.Button(win, text="D2",width= 7, command = lambda: play_note("D2.wav"))
    button_D3 = ttk.Button(win, text="D3",width= 7, command = lambda: play_note("D3.wav"))
    button_D4 = ttk.Button(win, text="D4",width= 7, command = lambda: play_note("D4.wav"))
    button_D5 = ttk.Button(win, text="D5",width= 7, command = lambda: play_note("D5.wav"))
    button_D6 = ttk.Button(win, text="D6",width= 7, command = lambda: play_note("D6.wav"))
    button_D7 = ttk.Button(win, text="D7",width= 7, command = lambda: play_note("D7.wav"))

    button_E1 = ttk.Button(win, text="E1",width= 7, command = lambda: play_note("E1.wav"))
    button_E2 = ttk.Button(win, text="E2",width= 7, command = lambda: play_note("E2.wav"))
    button_E3 = ttk.Button(win, text="E3",width= 7, command = lambda: play_note("E3.wav"))
    button_E4 = ttk.Button(win, text="E4",width= 7, command = lambda: play_note("E4.wav"))
    button_E5 = ttk.Button(win, text="E5",width= 7, command = lambda: play_note("E5.wav"))
    button_E6 = ttk.Button(win, text="E6",width= 7, command = lambda: play_note("E6.wav"))
    button_E7 = ttk.Button(win, text="E7",width= 7, command = lambda: play_note("E7.wav"))

    button_F1 = ttk.Button(win, text="F1",width= 7, command = lambda: play_note("F1.wav"))
    button_F2 = ttk.Button(win, text="F2",width= 7, command = lambda: play_note("F2.wav"))
    button_F3 = ttk.Button(win, text="F3",width= 7, command = lambda: play_note("F3.wav"))
    button_F4 = ttk.Button(win, text="F4",width= 7, command = lambda: play_note("F4.wav"))
    button_F5 = ttk.Button(win, text="F5",width= 7, command = lambda: play_note("F5.wav"))
    button_F6 = ttk.Button(win, text="F6",width= 7, command = lambda: play_note("F6.wav"))
    button_F7 = ttk.Button(win, text="F7",width= 7, command = lambda: play_note("F7.wav"))

    button_G1 = ttk.Button(win, text="G1",width= 7, command = lambda: play_note("G1.wav"))
    button_G2 = ttk.Button(win, text="G2",width= 7, command = lambda: play_note("G2.wav"))
    button_G3 = ttk.Button(win, text="G3",width= 7, command = lambda: play_note("G3.wav"))
    button_G4 = ttk.Button(win, text="G4",width= 7, command = lambda: play_note("G4.wav"))
    button_G5 = ttk.Button(win, text="G5",width= 7, command = lambda: play_note("G5.wav"))
    button_G6 = ttk.Button(win, text="G6",width= 7, command = lambda: play_note("G6.wav"))
    button_G7 = ttk.Button(win, text="G7",width= 7, command = lambda: play_note("G7.wav"))


    button_A1.place(x = 5, y = 0)
    button_A2.place(x = 85, y = 0)
    button_A3.place(x = 165, y = 0)
    button_A4.place(x = 245, y = 0)
    button_A5.place(x = 325, y = 0)
    button_A6.place(x = 405, y = 0)
    button_A7.place(x = 485, y = 0)

    button_B1.place(x = 5, y = 40)
    button_B2.place(x = 85, y = 40)
    button_B3.place(x = 165, y = 40)
    button_B4.place(x = 245, y = 40)
    button_B5.place(x = 325, y = 40)
    button_B6.place(x = 405, y = 40)
    button_B7.place(x = 485, y = 40)

    button_C1.place(x = 5, y = 80)
    button_C2.place(x = 85, y = 80)
    button_C3.place(x = 165, y = 80)
    button_C4.place(x = 245, y = 80)
    button_C5.place(x = 325, y = 80)
    button_C6.place(x = 405, y = 80)
    button_C7.place(x = 485, y = 80)
    button_C8.place(x = 565, y = 80)

    button_D1.place(x = 5, y = 120)
    button_D2.place(x = 85, y = 120)
    button_D3.place(x = 165, y = 120)
    button_D4.place(x = 245, y = 120)
    button_D5.place(x = 325, y = 120)
    button_D6.place(x = 405, y = 120)
    button_D7.place(x = 485, y = 120)

    button_E1.place(x = 5, y = 160)
    button_E2.place(x = 85, y = 160)
    button_E3.place(x = 165, y = 160)
    button_E4.place(x = 245, y = 160)
    button_E5.place(x = 325, y = 160)
    button_E6.place(x = 405, y = 160)
    button_E7.place(x = 485, y = 160)

    button_F1.place(x = 5, y = 200)
    button_F2.place(x = 85, y = 200)
    button_F3.place(x = 165, y = 200)
    button_F4.place(x = 245, y = 200)
    button_F5.place(x = 325, y = 200)
    button_F6.place(x = 405, y = 200)
    button_F7.place(x = 485, y = 200)

    button_G1.place(x = 5, y = 240)
    button_G2.place(x = 85, y = 240)
    button_G3.place(x = 165, y = 240)
    button_G4.place(x = 245, y = 240)
    button_G5.place(x = 325, y = 240)
    button_G6.place(x = 405, y = 240)
    button_G7.place(x = 485, y = 240)
    

    win.mainloop()
