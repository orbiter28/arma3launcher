#dir /B /S > list.txt

#manque cups_terrain et chernarus et eods_example_mission_v2.Stratis et @FFISv1.25

import ftplib
import os
import time

try:
    ftp.quit()
except:
    pass
    
ftp = ftplib.FTP("ftp.ecaline.fr")
ftp.login("ecaline", "nop")
ftp.cwd("mods")

os.chdir (r"H:\test")
ftp.retrbinary("RETR " + "list.txt" ,open("list.txt", 'wb').write)
time.sleep(1)

fichier=open("list.txt","r")
liste = fichier.read()
print(liste)

liste2=liste.splitlines()


listedossier=[]
listefichier=[]

i = 0
try:
    while liste2[i]:
        print("***********")
        i += 1
        if "." in liste2[i]:
            print (liste2[i], "est un fichier")
            listefichier.append(liste2[i])
        else :
            print (liste2[i], "est un dossier")
            listedossier.append(liste2[i])
except IndexError:
    pass

    
    
    
i = 0
try:
    while listefichier[i]:
        print("fichier",i,listefichier[i])
        i += 1
except IndexError:
    pass
    
    
i = 0
try:
    while listedossier[i]:
        print("dossier",i, listedossier[i])
        i += 1
except IndexError:
    pass



print ("création des dosssier sur windows")
i = 0
try:
    while listedossier[i]:
        i += 1
        newpath = listedossier[i]
        if not os.path.exists(newpath):
            os.makedirs(newpath)
except IndexError:
    pass


print ("Téléchargement des fichiers")
i = 1
try:
    while listefichier[i]:
        i += 1
        temp_str = listefichier[i]
        print (temp_str)
        
        folder=os.path.splitext(os.path.dirname(temp_str))
        folder=''.join(folder)
        print("folder",folder)
        
        
        file=os.path.splitext(os.path.basename(temp_str))
        file=''.join(file)
        print("file", file)
        
        
        os.chdir (r"H:\test\\"+folder)
        if not os.path.isfile(file):
            print("le fichier n'existe pas")
            print ("****************")
            print ("folder :", folder)
            ftp_folder=folder.replace("\\","/")
            print ("ftp_folder avec les slash", ftp_folder)
            ftp_folder = "/" + ftp_folder
            print ("ftp_folder final", ftp_folder)
            print ("fichier dans le répertoire", ftp.nlst(ftp_folder))
            print ("****************")
            print ("ftp.cwd(",ftp_folder,")")
            ftp.cwd(ftp_folder)
            fhandle = open(file, 'wb')
            print ("Getting " , file)
            ftp.retrbinary('RETR ' + file, fhandle.write)
            fhandle.close()
            
            
         
        #changer de répertoire sous windows
        #tester si le fichier existe déja sous windows
        #sinon
        #changer de répertoire sur le ftp (mod + folder)
        #télécharger le fichier (...+folder)

        
        #newfile = listefichier[i]
        #if not os.path.isfile(newfile):
        #    ftp.retrbinary("RETR " + newfile ,open(newfile, 'wb').write)
        
except IndexError:
    ftp.quit()

ftp.quit()
        

        
