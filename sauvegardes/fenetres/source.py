#!/usr/bin/python3
# -*-coding:Utf-8 -*

'''
Classe pour la fenêtre de sélection de la source
- enfant de FenetreSelection dans fenetres.selection
- utilisée dans champs.source.py

Amélioration
- pour l'instant, si la source est un répertoire, on ajoute automatique '/' pour synchroniser le contenu de la source et non la source
    il faudra penser à laisser le chpox à l'utilisateur ou l'utilisatrice
- je voulais faire que lorsque l'on clique dans un champ, ça sélectionne le radibutton correspondant et ça efface l'entry de l'autre champ
    mais ça marche que sur la ligne sur radibutton et pas sur la ligne de la sélection correspondante
        alors que j'aurai voulu que lorsque l'on clique dans un champ, ça vide l'autre
    -> en attendant, je fait faire qu'au moins lorsqu'on choisit un champ, ça efface l'autre
        mais on peut toujours écrire dans l'autre champ, ce qui provoque alors un messagebos

Bugs connus
- quand un avertissement messagebox se lance, ça ne renvoie rien
    et donc, si précédemment, dans la fenêtre principale, la ligne de la source contenait quelque chose, ça reste
    une solution pourrait être de définir moi-même une fenêtre d'avertissement afin qu'à sa femeture le code continue d'être lu, et donc la variable "" envoyé pour vider la ligne
'''

from tkinter import (
    messagebox, StringVar, Frame, Radiobutton, TOP, BOTTOM, X
)
from fenetres.selection import FenetreSelection
from champs.fichier import ChampSelectionFichier
from champs.repertoire import ChampSelectionRepertoire
from champs.barre_boutons import ChampBarreBtn

class FenetreSelectionSource(FenetreSelection):
    def __init__(self, master, text, instruction):
        super().__init__(master, text, instruction)
        
        self.type_source = StringVar()
        self.dico_source = {"fichier":"non","repertoire":"non"}
        
        self.champ_fichier = Frame(self.champ_particulier_selection)
        self.champ_fichier.pack(side=TOP)
        #self.champ_fichier.bind('<Button-1>', self.click_champ_fichier_event)
        self.btn_fichier = Radiobutton(self.champ_fichier, text="Source fichier", variable=self.type_source, value="fichier")
        self.btn_fichier.pack(side=TOP)
        self.btn_fichier.bind('<Button-1>', self.choix_fichier_event)
        self.champ_selection_fichier = ChampSelectionFichier(self.champ_fichier, "Fichier :", "Parcourir")
        self.champ_selection_fichier.pack(side=TOP)
        #self.champ_selection_fichier.bind('<Button-1>', self.click_champ_fichier_event)
       
        self.champ_rep = Frame(self.champ_particulier_selection)
        self.champ_rep.pack(side=TOP)
        #self.champ_rep.bind('<Button-1>', self.click_champ_rep_event)
        self.btn_rep = Radiobutton(self.champ_rep, text="Source répertoire", variable=self.type_source, value="repertoire")
        self.btn_rep.pack(side=TOP)
        self.btn_rep.bind('<Button-1>', self.choix_rep_event)
        self.champ_selection_rep = ChampSelectionRepertoire(self.champ_rep, "Répertoire :", "Parcourir")
        self.champ_selection_rep.pack(side=TOP)
        
        self.dico_btns = {"gauche":[("tout_vider", self.tout_vider), ("vider_fichier", self.vider_fichier), ("vider_repertoire", self.vider_repertoire)],
                          "droite":[("annuler", self.quit)]}
        self.barre_btns = ChampBarreBtn(self.champ_particulier_boutons, self.dico_btns)
        self.barre_btns.pack(side=BOTTOM, fill=X)
    
    def get_selection(self):
        source_fichier = self.champ_selection_fichier.get()
        source_rep = self.champ_selection_rep.get()
        if self.dico_source["fichier"] == "oui" and source_fichier != "" and source_rep == "":
            source = source_fichier
        elif self.dico_source["repertoire"] == "oui" and source_rep != "" and source_fichier == "":
            source = self.champ_selection_rep.get()
            source += "/"
        else:
            messagebox.showwarning("Attention","Aucune source n'a été sélectionnée", parent=self.top)
            source = "" # la suite n'est pas lancé, messagebox interrompt surement la fin du code
        return source
    
    def vider_fichier(self):
        self.champ_selection_fichier.put("")
    
    def vider_repertoire(self):
        self.champ_selection_rep.put("")
    
    def tout_vider(self):
        self.vider_fichier()
        self.vider_repertoire()
    
    def choix_fichier_event(self, event):
        self.vider_repertoire()
        self.dico_source["fichier"] = "oui"
        self.dico_source["repertoire"] = "non"
    
    def choix_rep_event(self,event):
        self.vider_fichier()
        self.dico_source["fichier"] = "non"
        self.dico_source["repertoire"] = "oui"
    
    """ en attente
    def click_champ_fichier_event(self, event):
        self.type_source.set("fichier")
    
    def click_champ_rep_event(self, event):
        self.type_source.set("repertoire")
    """