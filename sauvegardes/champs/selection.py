#!/usr/bin/python3
# -*-coding:Utf-8 -*

'''
Classe de base (parent) pour les champs de sélections des informations
'''

from tkinter import (
    StringVar, Frame, Label, Entry, Button, LEFT, RIGHT, X
)

class ChampSelectionInformations(Frame):
        def __init__(self,master,text_label, text_btn):
            self.master = master
            Frame.__init__(self,master)
            Label(self,text=text_label, width=20).pack(side=LEFT)
            self.textvariable = StringVar()
            Entry(self, textvariable=self.textvariable, width=100).pack(side=LEFT, fill=X, padx=15)
            Button(self,text=text_btn, command=self.selectionner).pack(side=RIGHT)
        
        # méthode qui va changer selon les classes enfant
        def selectionner(self):
            pass
        
        
        def get(self):
            return self.textvariable.get()
        
        def put(self,val):
            self.textvariable.set(val)