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
win.geometry("600x500")
win.resizable(0,0)
win.iconbitmap("Hangman.ico")

def init():
    global hiddenword
    hiddenword=random.choice(wordlist)
    wordlength=len(hiddenword)
    global guessword
    guessword=[]
    for character in hiddenword:
        guessword.append("_")

    global hint
    hint=Label(win, text= "Length of the word:"+ str(wordlength))
    hint.grid(column=0,row=0)

    global lives
    lives=Label(win, text="Tries left "+str(tries))
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

    global button_A
    global button_B
    global button_C
    global button_D
    global button_E
    global button_F
    global button_G
    global button_H
    global button_I
    global button_J
    global button_K
    global button_L
    global button_M
    global button_N
    global button_O
    global button_P
    global button_Q
    global button_R
    global button_S
    global button_T
    global button_U
    global button_V
    global button_W
    global button_X
    global button_Y
    global button_Z

    button_A = Button(win, text="A", width=3, height=1)
    button_A.place(x=10, y=400)

    button_B = Button(win, text="B", width=3, height=1)
    button_B.place(x=60, y=400)

    button_C = Button(win, text="C", width=3, height=1)
    button_C.place(x=110, y=400)

    button_D = Button(win, text="D", width=3, height=1)
    button_D.place(x=160, y=400)

    button_E = Button(win, text="E", width=3, height=1)
    button_E.place(x=210, y=400)

    button_F = Button(win, text="F", width=3, height=1)
    button_F.place(x=260, y=400)

    button_G = Button(win, text="G", width=3, height=1)
    button_G.place(x=310, y=400)

    button_H = Button(win, text="H", width=3, height=1)
    button_H.place(x=360, y=400)

    button_I = Button(win, text="I", width=3, height=1)
    button_I.place(x=410, y=400)

    button_J = Button(win, text="J", width=3, height=1)
    button_J.place(x=460, y=400)

    button_K = Button(win, text="K", width=3, height=1)
    button_K.place(x=510, y=400)

    button_L = Button(win, text="L", width=3, height=1)
    button_L.place(x=560, y=400)

    button_M = Button(win, text="M", width=3, height=1)
    button_M.place(x=10, y=430)

    button_N = Button(win, text="N", width=3, height=1)
    button_N.place(x=60, y=430)

    button_O = Button(win, text="O", width=3, height=1)
    button_O.place(x=110, y=430)

    button_P = Button(win, text="P", width=3, height=1)
    button_P.place(x=160, y=430)

    button_Q = Button(win, text="Q", width=3, height=1)
    button_Q.place(x=210, y=430)

    button_R = Button(win, text="R", width=3, height=1)
    button_R.place(x=260, y=430)

    button_S = Button(win, text="S", width=3, height=1)
    button_S.place(x=310, y=430)

    button_T = Button(win, text="T", width=3, height=1)
    button_T.place(x=360, y=430)

    button_U = Button(win, text="U", width=3, height=1)
    button_U.place(x=410, y=430)

    button_V = Button(win, text="V", width=3, height=1)
    button_V.place(x=460, y=430)

    button_W = Button(win, text="W", width=3, height=1)
    button_W.place(x=510, y=430)

    button_X = Button(win, text="X", width=3, height=1)
    button_X.place(x=560, y=430)

    button_Y = Button(win, text="Y", width=3, height=1)
    button_Y.place(x=10, y=460)

    button_Z = Button(win, text="Z", width=3, height=1)
    button_Z.place(x=60, y=460)


def game_update(guess):
    global tries
    global hiddenword

    if guess in hiddenword:
        array=list(hiddenword)
        for i in range(0, len(hiddenword)):
            if str(array[i])==guess:
                guessword[i]=str(guess)
        word_display.configure(text=guessword)
        if not "_" in guessword:
            Win()
    else:
        tries=tries-1
        image = Image.open(image_path[tries])
        image = image.resize((200, 200), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(image)
        panel.configure(image=img)
        panel.image=img
        if tries==0:
            Lose()
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
    button_continue=Button(win, text="New", command=lambda:game_restart)
    button_continue(column=0, row=8)
    init()

def Lose():
    status.configure(text="You Win!\n Your score is"+str(score))
    game_disable()
    global button_continue
    button_continue=Button(win, text="Restart", command=lambda:next_game())
    button_continue(column=0, row=8)
    init()

def next_game():
    game_destroy()
    global tries
    tries=6
    init()

def game_restart():
    game_destroy()
    global score
    score=0
    global tries
    tries=6
    init()


init()
win.mainloop()