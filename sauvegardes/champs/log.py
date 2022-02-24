#!/usr/bin/python3
# -*-coding:Utf-8 -*

'''
Classe pour le champ de la sélection de du log
- enfant de SelectionInformations dans champs.selection.py
- utilisée dans champs.principal
'''

from champs.selection import ChampSelectionInformations
from fenetres.log import FenetreSelectionLog

class ChampSelectionLog(ChampSelectionInformations):
    def selectionner(self):
        log = FenetreSelectionLog(self, "Sélection des exclusions", "Veuillez :" + "\n" +
                                            "1- sélectionner l'emplacement du log" + "\n" +
                                            "2- définir l'affichage de la date" +"\n" +
                                            "3- définir le nom du log").go()
        if log:
            self.textvariable.set(log)