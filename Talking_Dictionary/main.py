from tkinter import *
import pyttsx3
from PIL import Image, ImageTk
import json
from difflib import get_close_matches
from tkinter import messagebox

engine = pyttsx3.init()
voice = engine.getProperty('voices')

engine.setProperty('voice', voice[0].id)
engine.setProperty('rate', 150)

def search():
    data = json.load(open("data.json"))
    word = WordEnterBox.get()
    word = word.lower()

    if word in data:
        meaning = data[word]
        MeaningBox.delete(1.0, END)

        for item in meaning:
            MeaningBox.insert(END, u'\u2022' + item + '\n\n')

    elif len(get_close_matches(word, data.keys())) > 0:
        MeaningBox.delete(1.0, END)
        cmatch = get_close_matches(word, data.keys())[0]
        mBoxVal = messagebox.askyesno("confirm", 'Did you want to search ' + cmatch + ' ?')

        if mBoxVal == True:
            WordEnterBox.delete(0, END)
            WordEnterBox.insert(END, cmatch)
            meaning = data[cmatch]
            for item in meaning:
                MeaningBox.insert(END, u'\u2022' + item + '\n\n')

        else:
            messagebox.showerror('Info', 'Entered Word Doesnt Exist')
            WordEnterBox.delete(0, END)
            MeaningBox.delete(1.0, END)

    else:
        messagebox.showerror('Info', 'Entered Word Doesnt Exist')
        WordEnterBox.delete(0, END)
        MeaningBox.delete(1.0, END)


def clear():
    WordEnterBox.delete(0, END)
    MeaningBox.delete(1.0, END)


def audiov():
    engine.say(WordEnterBox.get())
    engine.runAndWait()

def audioM():
    engine.say(MeaningBox.get(1.0, END))
    engine.runAndWait()


vari = Tk()
vari.geometry('900x650')
vari.title("Talking Dictionary")
vari.resizable(False, False)

bgimg = ImageTk.PhotoImage(Image.open("bk.jpg"))
bglbl = Label(vari, image=bgimg)
bglbl.place(x=0, y=0)

WordEnterLbl = Label(vari, text="ENTER YOUR WORD", font=('Times New Roman', 20, "bold"), foreground="#D2691E",
                     background="white")
WordEnterLbl.place(x=320, y=20)
WordEnterBox = Entry(vari, font=("calibri", 25), justify=CENTER, bd=5, relief=GROOVE)
WordEnterBox.place(x=280, y=80)

Searchbtn = Button(vari, height=1, width=10, text="SEARCH", font=("bold"), bd=0, background="#808000", cursor='hand2',
                   activebackground="#808000", command=search)
Searchbtn.place(x=350, y=160)

spimg = ImageTk.PhotoImage(Image.open("speaker.png"))
SpeakBtn = Button(vari, image=spimg, bd=0, bg="whitesmoke", cursor="hand2", activebackground="whitesmoke",
                  command=audiov)
SpeakBtn.place(x=500, y=150)

MeaningLbl = Label(vari, text="WORD MEANING", font=('Times New Roman', 20, "bold"), foreground="#D2691E",
                   background="white")
MeaningLbl.place(x=340, y=250)
MeaningBox = Text(vari, font=("calibri", 15), bd=5, relief=GROOVE, width=50, height=10)
MeaningBox.place(x=200, y=300)

SpeakBtn = Button(vari, image=spimg, bd=0, bg="#808000", cursor="hand2", activebackground="whitesmoke", command=audioM)
SpeakBtn.place(x=350, y=570)

climg = ImageTk.PhotoImage(Image.open("close.png"))
ClBtn = Button(vari, image=climg, bd=2, activebackground="#808000", bg="#B22222", command=clear)
ClBtn.place(x=500, y=570)

vari.mainloop()