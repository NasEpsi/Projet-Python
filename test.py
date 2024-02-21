import tkinter as tk
from tkinter import *

def afficher_message():
    print("Bonjour les SN1")

def mise_a_jour_etiquette():
    etiquet.configure(text="Bonjour " + champ_entree.get())
    
fenetre = tk.Tk()
fenetre.title("Ma premiere app")

bouton = tk.Button(fenetre,text="Cliquer moi", command=mise_a_jour_etiquette)
bouton.pack()

etiquet = Label(fenetre, text= "ETIQUETTE")
etiquet.pack()

champ_entree= Entry(fenetre)
champ_entree.pack()



fenetre.mainloop()

