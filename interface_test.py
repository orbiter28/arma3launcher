import sys
import os
import ntpath
import winreg
from tkinter import *
from tkinter.filedialog import askdirectory
from tkinter.messagebox import *
import ftplib
from ftplib import FTP

def dest():
    showwarning('Selectionner le dossier', 'Selectionner le dossier dans lequel serons télécharger les mods')
    global rep
    rep = askdirectory(initialdir="/",title='Choisissez un repertoire')
    if len(rep) > 0:
        showwarning ('Selectionner le dossier', 'vous avez choisi le repertoire %s' % rep)
    os.chdir (rep)

def telechargement():
	
    port=21
    ip="ftp.ecaline.fr"
    password='nop'
    
    os.chdir("c:/Users/Yoann/Desktop/test") #changes the active dir - this is where downloaded files will be saved to
    ftp = ftplib.FTP("ftp.ecaline.fr")
    ftp.login('ecaline',password)

    
    directory ="/INCRUSTATION" #dir i want to download files from, can be changed or left for user input
    filematch = '*.*' # a match for any file in this case, can be changed or left for user to input
    
    ftp.cwd(directory)
    print ("File List:")
    files = ftp.dir()
    
    for filename in ftp.nlst(filematch): # Loop - looking for matching files
        fhandle = open(filename, 'wb')
        print ('Getting ' + filename) #for confort sake, shows the file that's being retrieved
        ftp.retrbinary('RETR ' + filename, fhandle.write)
        fhandle.close()
    
    ftp.quit()

    
def inutile():
    showwarning('Cesser de cliquer sur des boutons inutiles')


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
bou3.grid(row =3, column =1, padx=100,pady=5)
bou4.grid(row =4, column =1, padx=100,pady=5)




 
fenetre.mainloop()              # démarrage du réceptionnaire d'événements
 
fenetre.quit()               # destruction (fermeture) de la fenêtre
