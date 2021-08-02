









from tkinter import *
from PyDictionary import PyDictionary

dictionary = PyDictionary()
root = Tk()

root.geometry("400x400")

def dict():
    meaning.config(text=dictionary.meaning(word.get())['Noun'][0])
    synonym.config(text=dictionary.synonym(word.get()))
    antonym.config(text=dictionary.antonym(word.get())
    

