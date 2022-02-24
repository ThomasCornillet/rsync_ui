#!/usr/bin/python3
# -*-coding:Utf-8 -*

'''
Classe pour le champ de la sélection d'un fichier
- enfant de SelectionInformations dans champs.selection.py
- utilisée dans FenetreSelectionSource de fenetres.source
'''

from tkinter.filedialog import LoadFileDialog
from champs.selection import ChampSelectionInformations

class ChampSelectionFichier(ChampSelectionInformations):
    def selectionner(self):
        fichier = LoadFileDialog(self).go(pattern='*')
        if fichier:
            self.textvariable.set(fichier)