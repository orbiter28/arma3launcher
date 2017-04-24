import os
from tkinter import *
from tkinter.filedialog import askdirectory
from tkinter.messagebox import *
import ftplib
import time

def dest():
    showwarning('Dossier des destination', 'Selectionner le dossier dans lequel seront téléchargé les mods')
    global rep
    rep = askdirectory(initialdir="/",title='Choisissez un repertoire')
    if len(rep) > 0:
        showwarning ('Selectionner le dossier', 'vous avez choisi le repertoire %s' % rep)
    os.chdir (rep)

def mdp():
    global mot_de_passe
    mot_de_passe = StringVar()
    entreee = Entry(fenetre, textvariable=mot_de_passe, width=30)
    entreee.grid(row =3, column =1, padx=100,pady=5)
    
def telechargement():
    global mot_de_passe
    ftp = ftplib.FTP("ftp.ecaline.fr")
    ftp.login("ecaline", mot_de_passe.get())
    ftp.cwd("mods")
    
    os.chdir (rep)
    ftp.retrbinary("RETR " + "list.txt" ,open("list.txt", 'wb').write)
    time.sleep(1)
    
    fichier=open("list.txt","r")
    
    liste = fichier.read()
    liste2=liste.splitlines()
    listedossier=[]
    listefichier=[]
    
    i = 0
    try:
        while liste2[i]:
            print("***********")
            print("tris des fichier et dossier")
            print("et création des listes")
            print("***********")
            i += 1
            if os.path.isfile(liste2[i]) :
                listefichier.append(liste2[i])
            else :
                listedossier.append(liste2[i])
    except IndexError:
        print("tris terminé")
        
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
        
    print("***********")
    print ("création des dosssier sur windows")
    i = 0
    try:
        while listedossier[i]:
            i += 1
            newpath = listedossier[i]
            if not os.path.exists(newpath):
                os.makedirs(newpath)
    except IndexError:
        print("Création des dossiers terminé")
    print("***********")
    print ("Téléchargement des fichiers")
    i = 1
    try:
        while listefichier[i]:
            i += 1
            temp_str = listefichier[i]
            folder=os.path.splitext(os.path.dirname(temp_str))
            folder=''.join(folder)
            file=os.path.splitext(os.path.basename(temp_str))
            file=''.join(file)
            print("traitement de", file)
            print("Il s'agit du fichier ",i," sur", nbr_fichier)
            os.chdir (rep +"\\"+folder)
            if os.path.isfile(file):
                print("le fichier existe déjà")
            else:
                print ("Téléchargement du fichier", file)
                ftp_folder=folder.replace("\\","/")
                ftp_folder = "/" + ftp_folder
                ftp.cwd(ftp_folder)
                fhandle = open(file, 'wb')
                ftp.retrbinary('RETR ' + file, fhandle.write)
                fhandle.close()
    except IndexError:
        print("Téléchargement terminé")
    ftp.quit()


#------ Programme principal -------
 
# Création du widget principal ("maître") :
fenetre = Tk()
fenetre.title('Incrustation') 
fenetre.geometry("300x200")

# création des boutons :
bou1 = Button(fenetre,text='Dossier de destination',command=dest)
bou2 = Button(fenetre,text='Télécharger',command=telechargement)
bou3 = Button(fenetre,text='bouton inutile',command=inutile)
bou4 = Button(fenetre,text='Quitter',command=fenetre.quit)

bou1.grid(row =1, column =1, padx=100,pady=5)
bou2.grid(row =2, column =1, padx=100,pady=5)
bou3.grid(row =4, column =1, padx=100,pady=5)
bou4.grid(row =5, column =1, padx=100,pady=5)




 
fenetre.mainloop()              # démarrage du réceptionnaire d'événements
 
fenetre.quit()               # destruction (fermeture) de la fenêtre
