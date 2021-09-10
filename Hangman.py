from tkinter import*
from PIL import ImageTk,Image
import random
import sys

wordlist=["Nuwakot","Kathmandu", "Bhaktapur", "Chitwan", "Pokhara"]
lives=6
score=0

win=Tk()
win.title("Hangman")
win.geometry("800x500")
win.iconbitmap("Hangman.ico")

win.mainloop()