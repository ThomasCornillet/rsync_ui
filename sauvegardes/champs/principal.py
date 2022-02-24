#!/usr/bin/python3
# -*-coding:Utf-8 -*

'''
Classe pour le champ principal de la fenêtre principale (root)
- utilisée dans main.py

Amélioration
- je pense qu'il serait possible d'actualiser la ligne de commande automatiquement dès qu'une ligne est modifiée
    du coup ça permettrait de ne pas utiliser de boutons générer
- il faudrait ajouter des scrollbar aux entry des sélections au cas où la ligne dépasse la taille de la fenêtre
- faire attention avec l'envoi d'une commande dans le shell, d'autant que c'est en sudo
    se renseigner s'il y a d'autres choses que celles déjà prévenues
- voir ce qu'on fait pendant l'éxécution de la commande
    ça pourrait être pas mal d'afficher une nouvelle fenêtre pour voir l'évolution de la commande
    il faudrait de toute façon pouvoir savoir quand la commande sera terminée
        et si elle a réussi (via commande_exec.returncode
    => mais avant, je vais voir comment gérer le mot de pass

Bugs connus
- si messagebox lors de l'event executer, le bouton reste "enfoncé"
    peut-être le même problème que pour les messagebox des fenêtres
'''

from tkinter import (
    messagebox, StringVar, Frame, Label, Button, Entry, RAISED, TOP, BOTTOM, LEFT, NO, X, END
)
from datetime import datetime
from subprocess import run
from champs.source import ChampSelectionSource
from champs.cible import ChampSelectionCible
from champs.options import ChampSelectionOptions
from champs.excludes import ChampSelectionExcludes
from champs.log import ChampSelectionLog
from champs.barre_boutons import ChampBarreBtn
from fenetres.execution import FenetreExecuterCommande

class ChampPrincipal(Frame):
    def __init__(self, master):
        Frame.__init__(self, master, relief=RAISED, bd=2)
        #self.bind('<Return>', self.btn_generer_event)
        
        Label(self, text='sauvegardes.py', font=('Helvetica', 16, 'italic bold'), background='green', foreground='white').pack(side=TOP, expand=NO, fill=X)
        Label(self, text="Veuillez saisir les renseignements de synchronisation").pack(side=TOP)
        
        self.champ_source = ChampSelectionSource(self, "Source : ", "Sélectionner la source")
        self.champ_source.pack(side=TOP, fill=X)
        
        self.champ_cible = ChampSelectionCible(self, "Cible : ", "Sélectionner la cible")
        self.champ_cible.pack(side=TOP, fill=X)
        
        self.champ_options = ChampSelectionOptions(self, "Options : ", "Sélectionner les options")
        self.champ_options.pack(side=TOP, fill=X)
        
        self.champ_excludes = ChampSelectionExcludes(self, "Exclusions : ", "Sélectionner les exclusions")
        self.champ_excludes.pack(side=TOP, fill=X)
        
        self.champ_log = ChampSelectionLog(self, "Log : ", "Sélectionner le log")
        self.champ_log.pack(side=TOP, fill=X)
        
        self.champ_generer = Frame(self)
        self.champ_generer.pack(side=TOP, fill=X)
        self.btn_generer = Button(self.champ_generer,text="Générer la\n commande", width=19)
        self.btn_generer.pack(side=LEFT)
        self.btn_generer.bind('<Button-1>', self.btn_generer_event)
        #self.btn_generer.bind('<Return>', self.btn_generer_event)
        self.textvariable = StringVar()
        self.ligne_commande_generee = Entry(self.champ_generer, textvariable=self.textvariable, width=100)
        self.ligne_commande_generee.pack(side=LEFT)
        
        self.champ_executer_cmd = Frame(self)
        self.champ_executer_cmd.pack(side=TOP)
        self.btn_executer = Button(self.champ_executer_cmd, text="Éxécuter\nla commade")
        self.btn_executer.pack(side=TOP)
        self.btn_executer.bind('<Button-1>', self.btn_executer_event)
        
        Label(self, text="").pack(side=TOP)
        
        self.dico_btns = {"gauche": [("tout_vider", self.tout_vider), ("vider_source", self.vider_source),
                                     ("vider_cible", self.vider_cible), ("vider_options", self.vider_options),
                                     ("vider_excludes", self.vider_excludes), ("vider_log", self.vider_log)],
                          "droite": [("quitter", quit)]}
        self.champ_barre_btns = ChampBarreBtn(self, self.dico_btns)
        self.champ_barre_btns.pack(side=BOTTOM, fill=X)
    
    def btn_generer_event(self, event):
        self.dico_rep = {"options":self.champ_options.get(), "excludes":self.champ_excludes.get(), "log":self.champ_log.get(),
                         "source":self.champ_source.get(), "cible":self.champ_cible.get()}
        commande = "sudo rsync"
        for opt in self.dico_rep:
            if self.dico_rep[opt] == "":
                pass
            else:
                commande = commande + " " + self.dico_rep[opt]
        self.ligne_commande_generee.delete(0, END)
        self.ligne_commande_generee.insert(END,commande)
    
    def btn_executer_event(self, event):
        commande = self.ligne_commande_generee.get()
        erreur = "non"
        for elt in commande:
            if elt == ";" or elt == "&" or elt == "|":
                    erreur = "oui"
        if commande == "":
            messagebox.showwarning("Attention", "La ligne de commande est vide")
        elif erreur == "oui" or commande[0:10] != "sudo rsync":
            messagebox.showwarning("Attention", "La ligne de commande est incorrecte")
        else:
            with open("dernieres_commandes.sauv", 'r') as fichier:
                self.dernier_fichier = fichier.read()
            self.date = str(datetime.now())
            self.sauvegarde = self.date + "," + commande + "\n" + self.dernier_fichier
            with open("dernieres_commandes.sauv", 'w') as fichier:
                fichier.write(self.sauvegarde)
        fenetre_execution = FenetreExecuterCommande(self.champ_executer_cmd, fichier) # voir pour quel widget ancrer la fenêtre
        
        
        
        """ version avant passage en fenêtre
        commande = self.ligne_commande_generee.get()
        erreur = "non"
        for elt in commande:
            if elt == ";" or elt == "&" or elt == "|":
                    erreur = "oui"
        if commande == "":
            messagebox.showwarning("Attention", "La ligne de commande est vide")
        elif erreur == "oui" or commande[0:10] != "sudo rsync":
            messagebox.showwarning("Attention", "La ligne de commande est incorrecte")
        else:
            with open("dernieres_commandes.sauv", 'r') as fichier:
                self.dernier_fichier = fichier.read()
            self.date = str(datetime.now())
            self.sauvegarde = self.date + "," + commande + "\n" + self.dernier_fichier
            with open("dernieres_commandes.sauv", 'w') as fichier:
                fichier.write(self.sauvegarde)
            #print(commande)
            commande_exec = run(commande, shell=True)
        """
    
    def vider_source(self):
        self.champ_source.put("")
    
    def vider_cible(self):
        self.champ_cible.put("")
    
    def vider_options(self):
        self.champ_options.put("")
    
    def vider_excludes(self):
        self.champ_excludes.put("")
    
    def vider_log(self):
        self.champ_log.put("")
    
    def tout_vider(self):
        self.vider_source()
        self.vider_cible()
        self.vider_options()
        self.vider_excludes()
        self.vider_log()