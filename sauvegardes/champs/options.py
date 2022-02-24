#!/usr/bin/python3
# -*-coding:Utf-8 -*

'''
Classe pour le champ de la sélection des options
- enfant de SelectionInformations dans champs.selection.py
- utilisée dans champs.principal
'''

from champs.selection import ChampSelectionInformations
from fenetres.options import FenetreSelectionOptions

class ChampSelectionOptions(ChampSelectionInformations):
    def selectionner(self):
        options = FenetreSelectionOptions(self, "Sélection des options", "Veuillez sélectionner les options désirées en cochant les cases correspondantes").go()
        if options:
            self.textvariable.set(options)