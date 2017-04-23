#dir /B /S > list.txt

#manque cups_terrain et chernarus et eods_example_mission_v2.Stratis et @FFISv1.25

import ftplib
import os
import time
    
ftp = ftplib.FTP("ftp.ecaline.fr")
ftp.login("ecaline", "nop")
ftp.cwd("mods")

os.chdir (r"H:\test")
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
        if "." in liste2[i]:
            listefichier.append(liste2[i])
        else :
            listedossier.append(liste2[i])
except IndexError:
    print("Une erreure est apparue")
print("***********")
print("liste des fichiers :")   
i = 0
try:
    while listefichier[i]:
        print("fichier",i,listefichier[i])
        i += 1
except IndexError:
    print("Une erreure est apparue")
print("***********")
print("liste des dossier :")
i = 0
try:
    while listedossier[i]:
        print("dossier",i, listedossier[i])
        i += 1
except IndexError:
    print("Une erreure est apparue")
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
    print("Un erreure est apparue")
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
        os.chdir (r"H:\test\\"+folder)
        if not os.path.isfile(file):
            print("le fichier n'existe pas")
        print ("Téléchargement du fichier", file)
        ftp_folder=folder.replace("\\","/")
        ftp_folder = "/" + ftp_folder
        ftp.cwd(ftp_folder)
        fhandle = open(file, 'wb')
        ftp.retrbinary('RETR ' + file, fhandle.write)
        fhandle.close()
except IndexError:
    print("Une erreure est apparue")
ftp.quit()
        

        
