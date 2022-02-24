#!/usr/bin/python3
# -*-coding:Utf-8 -*

'''
Classe pour le champ de la barre des boutons en bas
- un peu nouveau par rapport à la V0-17
    pas seulement utiliser dans la fenêtre principale
        mais aussi dans les fenêtres de sélection des informations pour la commande
    ce qui va permettre d'enlever le bouton de visualisation des excludes de la fenêtre principale
        pour le mettre dans la fenêtre de sélection des excludes
    on va aussi regrouper les boutons commandes récentes et commandes sauvegardées pour la fenêtre principale
        un seul bouton : Commandes enregistrées
            qui ouvre sur une fenêtre ou on choisit de voir les commandes récentes ou les commandes sauveagradées
            ou peut-être voir les deux
            => à définir plus tard, la visualisation des commandes n'est pas une priorité

- fonctionnement
    j'ai eu du mal à définir ici les méthodes pour vider les lignes d'entrés de la fenêtre de sélection de la source
    du coup, les méthodes des boutons spécifiques aux fenêtres sont définies directement dans la fenêtre et renvoyer ici pour la définition des boutons
        définition des méthodes des boutons dans la fenêtre où s'affichent les boutons
            afin de réussir à envoyer le bon champs à vider avec .put("")

- des boutons de v0-17 en attente
    ouvrir source
    ouvrir cible
    commandes récentes
    commandes sauvegarder
    sauvegarder

'''

from tkinter import (
    Frame, Button, LEFT, RIGHT, SUNKEN
)

class ChampBarreBtn(Frame):
    def __init__(self, master, boutons):
        Frame.__init__(self, master, bd=2, relief=SUNKEN)
        self.dico_btn = self.generer(boutons)
        for btn, action in self.dico_btn["gauche"]:
            Button(self, text=btn, command=action).pack(side=LEFT)
        for btn, action in self.dico_btn["droite"]:
            Button(self, text=btn, command=action).pack(side=RIGHT)
    
    def generer(self, boutons):
        dico_btn_base = {"gauche": {"tout_vider": ["Tout\nvider"], "vider_fichier": ["Vider le\nfichier"],
                                    "vider_repertoire": ["Vider le\nrepertoire"], "vider_ligne" : ["Vider\nla ligne"],
                                    "vider_pattern": ["Vider\nle modèle"], "vider_nom_fichier": ["Vider\nle nom"],
                                    "vider_source": ["Vider\nla source"], "vider_cible": ["Vider\nla cible"],
                                    "vider_options": ["Vider\nles options"], "vider_excludes": ["Vider les\nexclusions"],
                                    "vider_log": ["Vider\nle log"],
                                    "tout_selectionner": ["Tout\nsélectionner"]},
                         "droite": {"quitter": ["Quitter"], "annuler": ["Annuler"]}}
        """ ancien dico complet, l'idée est d'en faire un nouveau en ajoutant au fur et à mesure de la création des boutons
        dico_btn_base = {"gauche": {"recente": ["Commandes\récentes"], "cmd_sauv": ["Commandes\nsauvegardées"],
                                   "vider": ["Vider les\nsources"], "vider_fichier": ["Vider la\nsource fichier"],
                                   "vider_repertoire": ["Vider la\nsource repertoire"], "vider_source": ["Vider\nla source"],
                                   "vider_cible": ["Vider\nla cible"], "vider_options": ["Vider\nles options"],
                                   "vider_excludes": ["Vider les\nexclusions"], "vider_log": ["Vider\nle log"],
                                   "vider_commande": ["Vider la\ncommande"], "ouvrir_source": ["Ouvrir \nla source"],
                                   "ouvrir_cible": ["Ouvrir\nla cible"], "visualiser_excl": ["Visualiser le\nfichier exclude"],
                                   "tout_selectionner": ["Tout\nsélectionner"], "vider_ligne" : ["Vider\nla ligne"],
                                   "vider_pattern": ["Vider\nle modèle"], "vider_fichier_excl": ["Vider\nle fichier"],
                                   "tout_vider": ["Tout\nvider"], "vider_emplacement" : ["Vider\nl'emplacement"],
                                   "vider_nom_fichier": ["Vider\nle nom"]},
                            "droite": {"quitter": ["Quitter"], "Sauvegarder": ["Sauvegarder"]}}
        """
        dico_btn = {"gauche": [], "droite": []}
        for btn in boutons["gauche"]:
            btn_tmp = dico_btn_base["gauche"][btn[0]]
            btn_tmp.append(btn[1])
            dico_btn["gauche"].append(btn_tmp)
        for btn in boutons["droite"]:
            btn_tmp = dico_btn_base["droite"][btn[0]]
            btn_tmp.append(btn[1])
            dico_btn["droite"].append(btn_tmp)
        return dico_btn