#!/usr/bin/python3
# -*-coding:Utf-8 -*

'''
Classe pour le champ de la sélection des exclusions
- enfant de SelectionInformations dans champs.selection.py
- utilisée dans champs.principal
'''

from champs.selection import ChampSelectionInformations
from fenetres.excludes import FenetreSelectionExcludes

class ChampSelectionExcludes(ChampSelectionInformations):
    def selectionner(self):
        excludes = FenetreSelectionExcludes(self, "Sélection des exclusions", "Veuillez sélectionner les exclusions désirées :" + "\n" +
                                            "1- sélectionner le type d'esclusion en cochant la case correspondante" + "\n" +
                                            "2- renseigner les informations correspondantes au type d'esxclusion sélectionné" +"\n" +
                                            "3- cliquer sur OK quand la sélection est terminée").go()
        if excludes:
            self.textvariable.set(excludes)