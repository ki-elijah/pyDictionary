from tkinter import *
from PyDictionary import PyDictionary

dictionary = PyDictionary()
root = Tk()

root.geometry("400x400")

def dict():
    meaning.config(text=dictionary.meaning(word.get())['Noun'][0])
    synonym.config(text=dictionary.synonym(word.get()))
    antonym.config(text=dictionary.antonym(word.get())
    
Label(root, text="Dictionary", font=("Helvatica 20 bold"), fg="Green").pack(pady=10)

frame = Frame(root)
Label(frame, text="Please Enter a Word", font = ("Helvatica 19 bold")).pack(side=LEFT)

word = Entry(frame, font = ("Helvatica 15 bold"))
word.pack()

frame.pack(pady=10)


frame1 = Frame(root)

Label(frame1, text="Please Enter a Word", font = ("Helvatica 10 bold")).pack(side=LEFT)

meaning=Entry(frame1, font=("Helvatica 10 bold"))

meaning.pack()

frame.pack(pady=10)
