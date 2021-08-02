




from tkinter import * 
from PyDictionary import PyDictionary

dictionary = PyDictionary()
root = Tk()
root.geometry("900x700")
root.title('Dictionary')

def dict():
    meaning.config(text=dictionary.meaning(word.get())['Noun'][0])
    synonym.config(text=dictionary.synonym(word.get()))
    antonym.config(text=dictionary.antonym(word.get()))


l = Label(root, text="Dictionary", font=("Helvatica 18 bold"), fg="green")
l.grid(row=0, column=1, sticky=W, pady=2)

l2 = Label(root, text="Word", font = ("Helvatica 14"))
l2.grid(row=1, column=0, pady=2)

word = Entry(root, font=("Helvatica 13"), justify="left")
word.grid(row=1, column=1, pady=2)

l3 = Label(root, text="Meaning:- ", font = ("Helvatica 12 bold"))
l3.grid(row=2, column=0, pady=2)

meaning = Label(root, text="", font=("Helvatica 10"), wraplength=800, justify="left")
meaning.grid(row=2, column=1, pady=2)

l4 = Label(root, text="Synonym:- ", font=("Helvatica 12 bold"))
l4.grid(row=3, column=0, pady=2)

synonym = Label(root, text="", font=("Helvatica 10"), wraplength=800, justify="left")
synonym.grid(row=3, column=1, pady=2)

l5 = Label(root, text="Antonym:- ", font=("Helvatica 12 bold"))
l5.grid(row=4, column=0, pady=2)

antonym = Label(root, text="", font=("Helvatica 10"), wraplength=800, justify="left")
antonym.grid(row=4, column=1, pady=2)

b = Button(root, text="Submit", font=("Helvatica 11 bold"), fg="white", bg="gray", command=dict)
b.grid(row=5, column=0, pady=2)

root.mainloop()
