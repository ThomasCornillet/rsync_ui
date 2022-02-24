#!/usr/bin/python3
# -*-coding:Utf-8 -*

'''
Classe pour la fenêtre de sélection des exclusions
- enfant de FenetreSelection dans fenetres.selection
- utilisée dans champs.source.py

Améliorations :
- ajouter la visualisation du fichier excl
- générer et enregistrer un nouveau fichier excl
- vider une ligne si l'autre radiobutton est sélectionner
    ex : si on clique sur pattern, on vide la ligne fichier, et inversement
    => du coup, peut-être pas besoin du boutons tout vider dans la barre des boutons
        pey de risque, mais au cas où on peut laisser quand même
- il faudrait qu'un bouton soit sélectionné par défaut
- il faudrait que quand un bouton est sélectionné, on ne puisse pas taper dans l'autre entry
    ou alors fait que quand on tape dans une entry ça sélectionne automatiquement le bouton correspondant

Bugs connus
- quand un avertissement messagebox se lance, ça ne renvoie rien
    et donc, si précédemment, dans la fenêtre principale, la ligne de la source contenait quelque chose, ça reste
'''

from tkinter import (
    messagebox, StringVar, Frame, Label, Entry, Radiobutton, TOP, BOTTOM, X, END
)
from fenetres.selection import FenetreSelection
from champs.fichier_excludes import ChampSelectionFichierExcludes
from champs.barre_boutons import ChampBarreBtn

class FenetreSelectionExcludes(FenetreSelection):
    def __init__(self, master, text, instruction):
        super().__init__(master, text, instruction)
        
        self.type_rep = StringVar()
        self.dico_rep = {"pattern":"non","fichier":"non"}
        
        self.champ_pattern = Frame(self.champ_particulier_selection)
        self.champ_pattern.pack(side=TOP)
        #self.btn_pattern = Radiobutton(self.champ_pattern, text="pattern", variable=self.type_rep, value="pattern", command=lambda arg="pattern":self.recup(arg))
        self.btn_pattern = Radiobutton(self.champ_pattern, text="pattern", variable=self.type_rep, value="pattern", command=self.recup)
        self.btn_pattern.pack(side=TOP)
        Label(self.champ_pattern, text="Renseignez le modèle :").pack(side=TOP)
        self.modele_rep = StringVar()
        self.modele_entry = Entry(self.champ_pattern, textvariable=self.modele_rep, width=10)
        self.modele_entry.pack(side=BOTTOM, fill=X, padx=15)
        
        self.champ_fichier = Frame(self.champ_particulier_selection)
        self.champ_fichier.pack(side=TOP)
        self.btn_fichier = Radiobutton(self.champ_fichier, text="fichier", variable=self.type_rep, value="fichier", command=self.recup)
        self.btn_fichier.pack(side=TOP)
        
        self.champ_choix_fichier = ChampSelectionFichierExcludes(self.champ_particulier_selection, "Fichier : ", "Parcourir")
        self.champ_choix_fichier.pack(side=TOP, fill=X)
        
        self.dico_btns = {"gauche":[("tout_vider", self.tout_vider), ("vider_pattern", self.vider_pattern), ("vider_fichier", self.vider_fichier_excl)],
                          "droite":[("annuler", self.quit)]}
        
        self.barre_btns = ChampBarreBtn(self.champ_particulier_boutons, self.dico_btns)
        self.barre_btns.pack(side=BOTTOM, fill=X)
    
    def recup(self):
        self.type_excl = str(self.type_rep.get())
        if self.type_excl == "pattern":
            self.dico_rep["pattern"] = "oui"
            self.dico_rep["fichier"] = "non"
        elif self.type_excl == "fichier":
            self.dico_rep["pattern"] = "non"
            self.dico_rep["fichier"] = "oui"
    
    def get_selection(self):
        if self.dico_rep["pattern"] == "oui" and self.dico_rep["fichier"] == "non":
            file_tmp = self.modele_rep.get()
            file = "--exclude=" + "\"" + str(file_tmp) + "\""
        elif self.dico_rep["pattern"] == "non" and self.dico_rep["fichier"] == "oui":
            file_tmp = self.champ_choix_fichier.get()
            file = "--exclude-from=" + str(file_tmp)
        else:
            messagebox.showwarning("Attention","Aucune exclusion n'a été sélectionnée", parent=self.top)
            file = ""
        return file
    
    def vider_pattern(self):
        self.modele_entry.delete(0, END)
    
    def vider_fichier_excl(self):
        self.champ_choix_fichier.put("")
    
    def tout_vider(self):
        self.vider_pattern()
        self.vider_fichier_excl()