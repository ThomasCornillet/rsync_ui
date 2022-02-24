#!/usr/bin/python3
# -*-coding:Utf-8 -*

"""
Classe pour la fenêtre d'éécution de la commande
- utilisée dans champs.principal

Amélioration
- faire en sorte qu'on ne puisse pas modifier la ligner Text de la commande affichée
    pour l'instant pas grave parce que ce n'est pas le contenu de Text qui est éxécuté (d'ailleurs, je ne sais pas comment interagir avec Text
    mais en essayant avec en modifiant l'option state, ça m'efface complètement la ligne
        mais je crois avoir lu que c'est du au comportement de state
        il faudrait voir avec bind selon un onglet firefox
- faire scroller la scrollbar avec le bouton scroll de la souris
"""

from tkinter import (
    Tk, Toplevel, Label, Frame, Text, Scrollbar, TOP, BOTTOM, LEFT, RIGHT, NO, X, BOTH, END, HORIZONTAL, NONE
)
from champs.barre_boutons import ChampBarreBtn

class FenetreExecuterCommande():
    def __init__(self, master, commande):
        self.master = master
        self.commande = commande
        
        self.top = Toplevel(self.master)
        self.top.title("Fenêtre d'éxécution de la commande")
        
        Label(self.top, text="Éxécution de la commande", font=('Helvetica', 16, 'italic bold'), background='blue', foreground='white').pack(side=TOP, expand=NO, fill=X)
        
        Label(self.top, text="").pack(side=TOP, fill=X)
        
        self.champ_commande = Frame(self.top)
        self.champ_commande.pack(side=TOP)
        Label(self.champ_commande, text="Commande : ").pack(side=LEFT)
        self.champ_commande_entry = Frame(self.champ_commande) # modifier le nom, ce n'est plus une entry
        self.champ_commande_entry.pack(side=RIGHT)
        self.scrollbar = Scrollbar(self.champ_commande_entry, orient=HORIZONTAL)
        self.scrollbar.pack(side=BOTTOM, fill=X)
        self.ligne_commande = Text(self.champ_commande_entry, height=1, width=100, xscrollcommand=self.scrollbar.set, wrap=NONE)
        self.ligne_commande.pack(fill=BOTH, expand=0)
        self.ligne_commande.insert(END, commande)        
        self.scrollbar.config(command=self.ligne_commande.xview)
        
        Label(self.top, text="").pack(side=TOP, fill=X)
        
        self.champ_etat_exec = Frame(self.top)
        self.champ_etat_exec.pack(side=TOP)
        
        Label(self.champ_etat_exec, text="État de la commande :").pack(side=TOP)
        
        self.champ_exec_en_cours = Frame(self.champ_etat_exec)
        self.champ_exec_en_cours.pack(side=TOP)
        Label(self.champ_exec_en_cours, text="Éxécution de la commande en cours...").pack(side=TOP)
        
        self.champ_exec_terminee = Frame(self.champ_etat_exec)
        """attendre que la commande soit exécéutée et pack après avoir destroy self.champ_exec_en_cours
        - pour l'instant je laisse pour les tests
        
        - pour attendre que la commande soite compléter
            voir : https://stackoverflow.com/questions/16196712/python-to-wait-for-shell-command-to-complete
                remplacer popen par la commande d'éxécution d'avant
        """
        self.champ_exec_terminee.pack(side=TOP)
        Label(self.champ_exec_en_cours, text="La commande a été éxécutée").pack(side=TOP)
        # ajouter des choses selons l'état de la commande
        
        Label(self.top, text="").pack(side=TOP, fill=X)
        
        self.dico_btns = {"gauche":[],
                          "droite":[("quitter", self.top.destroy)]} # attention ici à comment ça va être gérer hors tests
        self.barre_btns = ChampBarreBtn(self.top, self.dico_btns)
        self.barre_btns.pack(side=BOTTOM, fill=X)

if __name__ == '__main__':
    root = Tk()
    root.title("Test")
    Label(root, text="Test de la fenêtre éxécution", font=('Helvetica', 16, 'italic bold'), background='blue', foreground='white').pack(side=TOP, expand=NO, fill=X)
    test = FenetreExecuterCommande(root,"sudo rsync -avi --delete --itemize-changes --progress --stats --exclude-from=/home/thomas/eclipse-workspace/sauvegardes/Excludes/test.excl --log-file=/home/thomas/eclipse-workspace/sauvegardes/Logs/$(date +%Y%m%d-%H:%M:%S)_test.log /home/thomas/eclipse-workspace/sauvegardes/tests/source/ /home/thomas/eclipse-workspace/sauvegardes/tests/cible")
    root.mainloop()