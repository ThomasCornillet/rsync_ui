#!/usr/bin/python3
# -*-coding:Utf-8 -*

'''
Classe pour le champ de la sélection d'un repertoire
- enfant de SelectionInformations dans champs.selection.py
- utilisée dans FenetreSelectionSource de fenetres.source
'''

from champs.selection import ChampSelectionInformations
from tkinter import filedialog

class ChampSelectionRepertoire(ChampSelectionInformations):
    def selectionner(self):
        repertoire = filedialog.askdirectory(parent=self)
        if repertoire:
            self.textvariable.set(repertoire)