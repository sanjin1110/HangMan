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


img=Image.open(image_path[tries])
img=img.resize((200,200), Image.ANTIALIAS)
img=ImageTk.PhotoImage(img)
panel=Label(win, image=img)
panel.grid(column=0, row=7)

button_A=Button(win, text="A", width=1, height=1)
button_A.grid(column=1, row=3)

button_B=Button(win, text="B", width=1, height=1)
button_B.grid(column=2, row=3)

button_C=Button(win, text="C", width=1, height=1)
button_C.grid(column=3, row=3)

button_D=Button(win, text="D", width=1, height=1)
button_D.grid(column=4, row=3)

button_E=Button(win, text="E", width=1, height=1)
button_E.grid(column=5, row=3)

button_F=Button(win, text="F", width=1, height=1)
button_F.grid(column=6, row=3)

button_G=Button(win, text="G", width=1, height=1)
button_G.grid(column=7, row=3)

button_H=Button(win, text="H", width=1, height=1)
button_H.grid(column=8, row=3)

button_I=Button(win, text="I", width=1, height=1)
button_I.grid(column=9, row=3)

button_J=Button(win, text="J", width=1, height=1)
button_J.grid(column=10, row=3)

button_K=Button(win, text="K", width=1, height=1)
button_K.grid(column=1, row=4)

button_L=Button(win, text="L", width=1, height=1)
button_L.grid(column=2, row=4)

button_M=Button(win, text="M", width=1, height=1)
button_M.grid(column=3, row=4)

button_N=Button(win, text="N", width=1, height=1)
button_N.grid(column=4, row=4)

button_O=Button(win, text="O", width=1, height=1)
button_O.grid(column=5, row=4)

button_P=Button(win, text="P", width=1, height=1)
button_P.grid(column=6, row=4)

button_Q=Button(win, text="Q", width=1, height=1)
button_Q.grid(column=7, row=4)

button_R=Button(win, text="R", width=1, height=1)
button_R.grid(column=8, row=4)

button_S=Button(win, text="S", width=1, height=1)
button_S.grid(column=9, row=4)

button_T=Button(win, text="T", width=1, height=1)
button_T.grid(column=1, row=5)

button_U=Button(win, text="U", width=1, height=1)
button_U.grid(column=2, row=5)

button_V=Button(win, text="V", width=1, height=1)
button_V.grid(column=3, row=5)

button_W=Button(win, text="W", width=1, height=1)
button_W.grid(column=4, row=5)

button_X=Button(win, text="X", width=1, height=1)
button_X.grid(column=5, row=5)

button_Y=Button(win, text="Y", width=1, height=1)
button_Y.grid(column=6, row=5)

button_Z=Button(win, text="Z", width=1, height=1)
button_Z.grid(column=7, row=5)

win.mainloop()