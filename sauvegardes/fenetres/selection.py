#!/usr/bin/python3
# -*-coding:Utf-8 -*

'''
Classe de base (parent) pour les fenêtres de sélections des informations

'''

from tkinter import (
    Toplevel, Label, Frame, Button, TOP, BOTTOM, NO, X
)

class FenetreSelection():
    def __init__(self, master, text, instructions):
        self.master = master
        
        self.top = Toplevel(self.master)
        self.top.title("Fenêtre de sélection des informations pour la commande")
        
        Label(self.top, text=text, font=('Helvetica', 16, 'italic bold'), background='blue', foreground='white').pack(side=TOP, expand=NO, fill=X)
        Label(self.top, text=instructions).pack(side=TOP)
        
        self.champ_particulier_selection = Frame(self.top)
        self.champ_particulier_selection.pack(side=TOP, fill=X)
        
        self.champ_particulier_boutons = Frame(self.top)
        self.champ_particulier_boutons.pack(side=BOTTOM, fill=X)
        
        Label(self.top, text="").pack(side=BOTTOM)
        
        Button(self.top, text="Ok", command=self.ok_command).pack(side=BOTTOM)
        
        Label(self.top, text="").pack(side=BOTTOM)
        
    def go(self,default=""):
        self.top.wait_visibility()
        self.top.grab_set()
        self.how = None
        self.master.mainloop()
        self.top.destroy()
        return self.how
    
    def quit(self, how=None):
        self.how = how
        self.top.quit()
        
    def ok_command(self):
        self.quit(self.get_selection())
        