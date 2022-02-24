#!/usr/bin/python3
# -*-coding:Utf-8 -*

'''
Classe pour la fenêtre de sélection des exclusions
- enfant de FenetreSelection dans fenetres.selection
- utilisée dans champs.source.py

Améliorations
- il faudrait soit sélectionner automatiquement qqch pour la date
    soit faire une alerte si rien n'est sélectionner
- afficher la commande dans le log

Bugs connus
- quand un avertissement messagebox se lance, ça ne renvoie rien
    et donc, si précédemment, dans la fenêtre principale, la ligne de la source contenait quelque chose, ça reste
'''

from tkinter import (
    messagebox, StringVar, Frame, Label, Entry, Radiobutton, TOP, BOTTOM, X
)
from fenetres.selection import FenetreSelection
from champs.repertoire import ChampSelectionRepertoire
from champs.barre_boutons import ChampBarreBtn

class FenetreSelectionLog(FenetreSelection):
    def __init__(self, master, text, instruction):
        super().__init__(master, text, instruction)
        
        self.date_rep = StringVar()
        self.nom_rep = StringVar()
        self.dico_rep = {"emplacement":"","date":"", "nom":""}
        
        self.champ_emplacement = ChampSelectionRepertoire(self.champ_particulier_selection, "Emplacement : ", "Parcourir")
        self.champ_emplacement.pack(side=TOP, fill=X)
        
        self.champ_date = Frame(self.champ_particulier_selection)
        self.champ_date.pack(side=TOP, fill=X)
        Label(self.champ_date, text="Souhaitez-vous afficher la date dans le nom du log ? ").pack(side=TOP)
        
        self.btn_oui = Radiobutton(self.champ_date, text="oui", variable=self.date_rep, value="oui", command=self.recup)
        self.btn_oui.pack(side=TOP)
        self.btn_non = Radiobutton(self.champ_date, text="non", variable=self.date_rep, value="non", command=self.recup)
        self.btn_non.pack(side=BOTTOM)
        
        self.champ_nom = Frame(self.champ_particulier_selection)
        self.champ_nom.pack(side=TOP, fill=X)
        Label(self.champ_nom, text="Quel nom souhaitez-vous donner à votre fichier ?").pack(side=TOP)
        Entry(self.champ_nom, textvariable=self.nom_rep, width=100).pack(side=BOTTOM, fill=X, padx=15)
        
        self.dico_btns = {"gauche":[("tout_vider", self.tout_vider), ("vider_repertoire", self.vider_repertoire),
                                    ("vider_nom_fichier", self.vider_nom_fichier)],
                          "droite":[("annuler", self.quit)]}
        
        self.barre_btns = ChampBarreBtn(self.champ_particulier_boutons, self.dico_btns)
        self.barre_btns.pack(side=BOTTOM, fill=X)
    
    def recup(self):
        self.rep = str(self.date_rep.get())
        if self.rep == "oui":
            self.dico_rep["date"] = "/$(date +%Y%m%d-%H:%M:%S)"
        elif self.rep == "non":
            self.dico_rep["date"] = "/"
    
    def get_selection(self):
        emplacement = self.champ_emplacement.get()
        date = self.dico_rep["date"]
        nom = self.nom_rep.get()
        if emplacement == "" and nom == "":
            messagebox.showwarning("Attention","Aucun log n'a été sélectionné", parent=self.top)
            file = ""
        elif emplacement == "":
            messagebox.showwarning("Attention","Aucun emplacement n'a été sélectionnée" + "\n" +
                                                "Veuillez recommencer", parent=self.top)
            file = ""
        elif nom == "":
            messagebox.showwarning("Attention","Aucun nom n'a été défini" + "\n" +
                                                "Seule la date apparaitra", parent=self.top)
            file = "--log-file=" + str(emplacement) + date
        else:
            file = "--log-file=" + str(emplacement) + date + "_" + str(nom) + ".log"
        return file
        
    def vider_repertoire(self):
        self.champ_emplacement.put("")
    
    def vider_nom_fichier(self):
        self.nom_rep.set("")
    
    def tout_vider(self):
        self.vider_repertoire()
        self.vider_nom_fichier()