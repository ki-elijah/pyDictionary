from tkinter import *
from PyDictionary import PyDictionary

dictionary = PyDictionary()
root = Tk()

root.geometry("600x600")

def dict():
    meaning.config(text=dictionary.meaning(word.get())['Noun'][0])
    synonym.config(text=dictionary.synonym(word.get()))
    antonym.config(text=dictionary.antonym(word.get()))


Label(root, text="Dictionary", font=("Helvatica 18 bold"), fg="green").pack(pady=10)

frame = Frame(root)
Label(frame, text="Please Enter a Word", font = ("Helvatica 16 bold")).pack(side=LEFT)
word = Entry(frame, font = ("Helvatica 15 bold"))
word.pack()

frame.pack(pady=10)

#frame1
frame1 = Frame(root)

Label(frame1, text="Meaning:- ", font = ("Helvatica 10 bold")).pack(side=LEFT)
meaning=Label(frame1, text="", font=("Helvatica 10 bold"))
meaning.pack()
frame1.pack(pady=10)

#frame2
frame2=Frame(root)

Label(frame2, text="Synonym:- ", font=("Helvatica 10 bold")).pack(side=LEFT)
synonym = Label(frame2, text="", font=("Helvatica 10 bold"))
synonym.pack()
frame2.pack(pady=10)

#frame3
frame3 = Frame(root)

Label(frame3, text="Antonym:- ", font=("Helvatica 10 bold")).pack(side=LEFT)
antonym = Label(frame3, text="", font = ("Helvatica 10 bold"))
antonym.pack(side=LEFT)
frame3.pack(pady=10)

Button(root, text="Submit", font=("Helvatica 10 bold"), command=dict).pack()

root.mainloop()
