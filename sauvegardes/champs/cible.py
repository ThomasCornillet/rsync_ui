#!/usr/bin/python3
# -*-coding:Utf-8 -*

'''
Classe pour le champ de la sélection de la cible
- enfant de SelectionInformations dans champs.selection.py
- utilisée dans champs.principal
'''

from champs.selection import ChampSelectionInformations
from tkinter import filedialog

class ChampSelectionCible(ChampSelectionInformations):
    def selectionner(self):
        cible = filedialog.askdirectory()
        if cible:
            self.textvariable.set(cible)