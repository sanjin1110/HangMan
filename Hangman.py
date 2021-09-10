from tkinter import*
from PIL import ImageTk,Image
import random
import sys

wordlist=["Nuwakot","Kathmandu", "Bhaktapur", "Chitwan", "Pokhara"]
tries=6
score=0
image_path=["hangman0.png","hangman1.png","hangman2.png","hangman3.png","hangman4.png","hangman5.png","hangman6.png"]

win=Tk()
win.title("Hangman")
win.geometry("800x500")
win.iconbitmap("Hangman.ico")

def init():
    global hiddenword
    hiddenword=random.choice(wordlist)
    wordlength=len(hiddenword)
    global guessword
    guessword=[]
    for character in hiddenword:
        guessword.append("*")

    global hint
    hint=Label(win, text= "length of the word:"+ str(wordlength))
    hint.grid(column=0,row=0)

    global lives
    lives=Label(win, text="Tries left"+str(tries))
    lives.grid(column=0, row=1)

    global word_display
    word_display=Label(win,text=guessword)
    word_display.grid(column=0,row=2)
    
win.mainloop()