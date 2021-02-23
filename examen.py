#!/usr/bin/env python3
#####################
# Nom de fichier: examen.py
# Description: Squelette pour l'examen 1 du cours 243-413-SH
# Auteur : Julien Bosco
# Modification : 2021/02/23
####################

# Section pour les importations



# Fonction d'initialisation, appelée une seule fois au début du programme
def setup():
    print("setup()...")

# Fonction appelée à l'intérieur de la boucle while(True)
def loop():
    print("loop()...") # Peut être enlevé

# Fonction appelé lorsque Ctrl+c est appuyé
def destroy():
    print("destroy()...")

if __name__ == "__main__":
    setup()
    try:
        while(True):
            loop()
    except KeyboardInterrupt: # Capture Ctrl-c, appelle destroy, puis quitte
        destroy()
