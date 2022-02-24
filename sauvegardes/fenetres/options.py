#!/usr/bin/python3
# -*-coding:Utf-8 -*

'''
Classe pour la fenêtre de sélection des options
- enfant de FenetreSelection dans fenetres.selection
- utilisée dans champs.source.py

Bugs connus
- quand un avertissement messagebox se lance, ça ne renvoie rien
    et donc, si précédemment, dans la fenêtre principale, la ligne de la source contenait quelque chose, ça reste
'''

from tkinter import (
    messagebox, IntVar, Entry, Checkbutton, BOTTOM, TOP, X, END
)
from fenetres.selection import FenetreSelection
from champs.barre_boutons import ChampBarreBtn

class FenetreSelectionOptions(FenetreSelection):
    def __init__(self, master, text, instruction):
        super().__init__(master, text, instruction)
        
        self.ligne_commande = Entry(self.champ_particulier_selection, width=100)
        self.ligne_commande.pack(side=BOTTOM, fill=X, padx=15)
        
        self.dico_opt = {"archive":IntVar(), "verbosity":IntVar(), "infos":IntVar(), "delete":IntVar(), "itemize-changes":IntVar(),
                         "progress":IntVar(),"stats":IntVar()}
        self.dico_rep = {"archive":"non","verbosity":"non","infos":"non","delete":"non","itemize-changes":"non","progress":"non","stats":"non"}
        for opt in self.dico_opt:
            cb = Checkbutton(self.champ_particulier_selection, text=opt, variable=self.dico_opt[opt], command=lambda arg=opt:self.recup(arg))
            cb.pack(side=TOP)
        
        self.dico_btns = {"gauche": [("tout_selectionner", self.tout_selectionner), ("vider_ligne", self.vider_ligne)],
                          "droite":[("annuler", self.quit)]}
        self.barre_btns = ChampBarreBtn(self.champ_particulier_boutons, self.dico_btns)
        self.barre_btns.pack(side=BOTTOM, fill=X)
    
    def go(self,default=""):
        self.set_selection(default)
        self.ligne_commande.focus_set()
        self.top.wait_visibility()
        self.top.grab_set()
        self.how = None
        self.master.mainloop()
        self.top.destroy()
        return self.how
    
    def recup(self,opt):
        a = int(self.dico_opt[opt].get())
        if a == 0:
            self.dico_rep[opt] = "non"
        elif a == 1:
            self.dico_rep[opt] = "oui"
        self.ligne_cmd = self.generer(self.dico_rep)
        self.ligne_commande.delete(0, END)
        self.ligne_commande.insert(END,self.ligne_cmd)
        return self.dico_rep[opt]
    
    def generer(self,options):
        self.dico_opt_det = {"opt_lettre":{"archive":options["archive"],"verbosity":options["verbosity"],"infos":options["infos"]},
                            "opt_mot":{"delete":options["delete"],"itemize-changes":options["itemize-changes"],"progress":options["progress"],"stats":options["stats"]}}
        self.liste_opt_lettre =[]
        for opt in self.dico_opt_det["opt_lettre"]:
            if self.dico_opt_det["opt_lettre"][opt] == "oui":
                self.liste_opt_lettre.append(opt)
        if len(self.liste_opt_lettre) == 0:
            self.cmd_opt_lettre = ""
        else:
            self.cmd_opt_lettre = "-"
            for opt in self.liste_opt_lettre:
                lettre = opt[0]
                self.cmd_opt_lettre += lettre    
        self.liste_opt_mot = []
        for opt in self.dico_opt_det["opt_mot"]:
            if self.dico_opt_det["opt_mot"][opt] == "oui":
                self.liste_opt_mot.append(opt)
        self.cmd_opt_mot = ""
        if len(self.liste_opt_mot) == 0:
            pass
        else:
            for opt in self.liste_opt_mot:
                self.cmd_opt_mot += "--" + opt + " "
            if self.cmd_opt_mot[-1] == " ":
                self.cmd_opt_mot = self.cmd_opt_mot.rstrip(self.cmd_opt_mot[-1])
        if self.cmd_opt_lettre == "" and self.cmd_opt_mot == "":
            self.cmd_opt = ""
        elif self.cmd_opt_lettre == "":
            self.cmd_opt = self.cmd_opt_mot
        elif self.cmd_opt_mot == "":
            self.cmd_opt = self.cmd_opt_lettre
        else:
            self.cmd_opt = self.cmd_opt_lettre + " " + self.cmd_opt_mot
        return self.cmd_opt
    
    def get_selection(self):
        file = self.ligne_commande.get()
        if file == "":
            messagebox.showwarning("Attention","Aucune option n'a été sélectionnée", parent=self.top)
        return file
    
    def set_selection(self,selection):
        self.ligne_commande.delete(0, END)
        self.ligne_commande.insert(END,selection)
    
    def tout_selectionner(self):
        for opt in self.dico_opt:
            self.dico_opt[opt].set(1)
        ligne_toutes_options = "-avi --delete --itemize-changes --progress --stats"
        self.ligne_commande.delete(0, END)
        self.ligne_commande.insert(END,ligne_toutes_options)
    
    def vider_ligne(self):
        for opt in self.dico_opt:
            self.dico_opt[opt].set(0)
        self.ligne_commande.delete(0, END)
        self.dico_rep = {"archive":"non","verbosity":"non","infos":"non","delete":"non","itemize-changes":"non","progress":"non","stats":"non"}