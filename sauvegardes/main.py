#!/usr/bin/python3
# -*-coding:Utf-8 -*

from tkinter import Tk
from champs.principal import ChampPrincipal

def main():
    root = Tk()
    root.title("Sauvegardes.py V1-1")
    
    cadre_principal = ChampPrincipal(root)
    cadre_principal.pack()
    #cadre_principale.mainloop()
    root.mainloop()

if __name__ == '__main__':
    main()