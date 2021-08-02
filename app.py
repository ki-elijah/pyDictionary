from tkinter import * 
from PyDictionary import PyDictionary

dictionary = PyDictionary()
root = Tk()
root.geometry("950x700")
root.title('Dictionary')

def dict():
    meaning.config(text=dictionary.meaning(word.get())['Noun'][0])
    synonym.config(text=dictionary.synonym(word.get()))
    antonym.config(text=dictionary.antonym(word.get()))


l = Label(root, text="Dictionary", font=("Helvatica 18 bold"), fg="green")
l.grid(row=0, column=1)

l2 = Label(root, text="Word", font = ("Helvatica 14"), justify="left")
l2.grid(row=1, column=0)

word = Entry(root, font=("Helvatica 13"), justify="left")
word.grid(row=1, column=1, sticky=W)

s = Label(root)
s.grid(row=2, column=0)
s2 = Label(root)
s2.grid(row=2, column=1)

l3 = Label(root, text="Meaning:- ", font = ("Helvatica 12 bold"))
l3.grid(row=3, column=0)

meaning = Label(root, text="", font=("Helvatica 10"), wraplength=800, justify="left", borderwidth=2, relief="ridge")
meaning.grid(row=3, column=1, sticky=W)

s3 = Label(root)
s3.grid(row=4, column=0)
s4 = Label(root)
s4.grid(row=4, column=1)

l4 = Label(root, text="Synonym:- ", font=("Helvatica 12 bold"))
l4.grid(row=5, column=0)

synonym = Label(root, text="", font=("Helvatica 10"), wraplength=800, justify="left", borderwidth=2, relief="groove")
synonym.grid(row=5, column=1, sticky=W)

s5 = Label(root)
s5.grid(row=6, column=0)
s6 = Label(root)
s6.grid(row=6, column=1)

l5 = Label(root, text="Antonym:- ", font=("Helvatica 12 bold"))
l5.grid(row=7, column=0)

antonym = Label(root, text="", font=("Helvatica 10"),
                wraplength=800, justify="left", borderwidth=2, relief="groove")
antonym.grid(row=7, column=1, sticky=W)

s7 = Label(root)
s7.grid(row=8, column=0)
s8 = Label(root)
s8.grid(row=8, column=1)

b = Button(root, text="Submit", font=("Helvatica 11 bold"), borderwidth=3, relief="solid", fg="white", bg="gray", command=dict)
b.grid(row=9, column=0)

root.mainloop()
