#!/usr/bin/python3
# -*-coding:Utf-8 -*

'''
Classe pour le champ de la sélection de la source
- enfant de SelectionInformations dans champs.selection.py
- utilisée dans ChampPrincipal dans champs.principal
'''

from champs.selection import ChampSelectionInformations
from fenetres.source import FenetreSelectionSource

class ChampSelectionSource(ChampSelectionInformations):
    def selectionner(self):
        source = FenetreSelectionSource(self, "Sélection de la source", "Veuillez :" + "\n" + 
                                                                        "1- Cocher le type de source souhaitée" + "\n" +
                                                                        "2- Sélectionner ensuite la source correspondante").go()
        if source:
            self.textvariable.set(source)