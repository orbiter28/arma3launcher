import os
import time

rep=input ("répertoire des mods")
os.chdir(rep)
#encoding utf-8 for the command prompt and the file list.txt
os.system("chcp 65001")
os.system("dir /B /S > list.txt")

fichier=open("list.txt","r")

liste = fichier.read()
liste2=liste.splitlines()
listedossier=[]
listefichier=[]

print("***********")
print("tri des fichier et dossier")
print("et création des listes")
print("***********")
i = 0
try:
    while liste2[i]:
        i += 1
        if os.path.isfile(liste2[i]) :
            listefichier.append(liste2[i])
        else :
            listedossier.append(liste2[i])
except IndexError:
    print("tri terminé")
    
print("***********")
print("liste des fichiers :")   
i = 0
try:
    while listefichier[i]:
        print("fichier",i,listefichier[i])
        i += 1
except IndexError:
    print("listage des fichiers terminé")
    
print("***********")
print("liste des dossier :")
i = 0
try:
    while listedossier[i]:
        print("dossier",i, listedossier[i])
        i += 1
except IndexError:
    print("listage des dossier terminé")
    nbr_fichier = i - 1
    
list_fichier=open("listfichier.txt","w")
listefichier=str(listefichier)
list_fichier.write(listefichier)
list_fichier.close()

print ("fichier listfichier créé !")

list_dossier=open("listdossier.txt","w")
listedossier=str(listedossier)
list_dossier.write(listedossier)
list_dossier.close()

print ("fichier listdossier créé !")
print ("Il ne reste plus qu'a envoyé les 3 fichiers dans le ftp à la base du dossier mod")
