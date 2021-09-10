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

    global status
    status=Label(win, text= "In Progress...")
    status.grid(column=0, row=6)

    global img
    img = Image.open(image_path[tries])
    img = img.resize((200, 200), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    global panel
    panel = Label(win, image=img)
    panel.grid(column=0, row=7)

def game_update(guess):
    global tries
    global hiddenword

    if guess in hiddenword:
        array=list(hiddenword)
        for i in range(0, len(hiddenword)):
            if str(array[i])==guess:
                guessword[i]=str(guess)
        word_display.configure(text=guessword)
        if not "*" in guessword:
            Win()
    else:
        tries=tries-1
        image = Image.open(image_path[tries])
        image = image.resize((200, 200), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(image)
        panel.configure(image=img)
        panel.image=img
        if tries==0:
            Loss()
        tries.configure(text="Remaining chances"+str(tries))
        word_display.configure(text=guessword)

def game_disable():
    button_A.configure(state="disabled")
    button_B.configure(state="disabled")
    button_C.configure(state="disabled")
    button_D.configure(state="disabled")
    button_E.configure(state="disabled")
    button_F.configure(state="disabled")
    button_G.configure(state="disabled")
    button_H.configure(state="disabled")
    button_I.configure(state="disabled")
    button_J.configure(state="disabled")
    button_K.configure(state="disabled")
    button_L.configure(state="disabled")
    button_M.configure(state="disabled")
    button_N.configure(state="disabled")
    button_O.configure(state="disabled")
    button_P.configure(state="disabled")
    button_Q.configure(state="disabled")
    button_R.configure(state="disabled")
    button_S.configure(state="disabled")
    button_T.configure(state="disabled")
    button_U.configure(state="disabled")
    button_V.configure(state="disabled")
    button_W.configure(state="disabled")
    button_X.configure(state="disabled")
    button_Y.configure(state="disabled")
    button_Z.configure(state="disabled")

def game_destroy():
    button_A.destroy()
    button_B.destroy()
    button_C.destroy()
    button_D.destroy()
    button_E.destroy()
    button_F.destroy()
    button_G.destroy()
    button_H.destroy()
    button_I.destroy()
    button_J.destroy()
    button_K.destroy()
    button_L.destroy()
    button_M.destroy()
    button_N.destroy()
    button_O.destroy()
    button_P.destroy()
    button_Q.destroy()
    button_R.destroy()
    button_S.destroy()
    button_T.destroy()
    button_U.destroy()
    button_V.destroy()
    button_W.destroy()
    button_X.destroy()
    button_Y.destroy()
    button_Z.destroy()


def Win():
    global score
    score=score+1
    status.configure(text="You Win!\n Your score is"+str(score))
    game_disable()
    global button_continue
    button_continue=Button(win, text="New")
    button_continue(column=0, row=8)
    init()

def Lose():
    status.configure(text="You Win!\n Your score is"+str(score))
    game_disable()
    global button_continue
    button_continue=Button(win, text="Restart" )
    button_continue(column=0, row=8)
    init()





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