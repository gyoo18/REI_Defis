import os
import traceback
import time
from termcolor import colored
import math

def int2str(x : int):
    n_chiffres = math.floor(math.log10(x))
    print(n_chiffres,"chiffres à transformer.")
    timer = time.time()

    string = ""
    while x > 0:
        string += str(x-(10*(x//10)))
        x = x//10

        if time.time()-timer > 2:
            print("\r",end="")
            print(str(int((1 - math.floor(math.log10(x))/n_chiffres)*100)) + "%",end="")
            timer = time.time()
    
    string_return = ""
    for i in range(len(string)):
        string_return += string[-(i+1)]

    return string_return

fichiers = os.listdir("Soumissions_defis2")
programmes = []
for i in range(len(fichiers)):
    if ".py" in fichiers[i]:
        programmes.append(fichiers[i])

total = 0
gagnant = ""
gagnant_max = 0
for i in range(len(programmes)):
    fichier = open("Soumissions_defis2/" + programmes[i],"r")
    code = ""
    for ligne in fichier.readlines():
        code += ligne
    fichier.close()
    
    try:
        timer = time.time()

        exec(code)
        nombre = main()

        if time.time()-timer > 10:
            print(colored("[Échec] ", "red") + programmes[i] + " n'a pas respecté le budget de temps avec " + str(time.time()-timer) + " secondes.")
            break
        
        temps = int((time.time()-timer)*100)/100

        if type(nombre) != int:
            print(colored("[Échec] ", "red") + programmes[i] + " n'a pas renvoyé un int, mais plutôt un " + str(type(nombre)) + ".")
            break

        print(colored("[Succès] ","green") + programmes[i] + " a renvoyé un nombre.")
        # print("Conversion du nombre en string.")
        # nombre_str =  int2str(nombre)
        # print(programmes[i] + " a renvoyé " + nombre_str)

        if nombre > gagnant_max:
            gagnant_max = nombre
            gagnant = programmes[i]
            print(colored("[Succès] ","blue") + programmes[i] + " a battus le score précédent!")

    except:
        print(colored("[Erreur] ","red") + programmes[i] + " n'a pas pus s'exécuter correctement.")
        print(traceback.format_exc())

print(total)
