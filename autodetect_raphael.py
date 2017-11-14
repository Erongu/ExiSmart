#Imports
try:
    from Tkinter import *
except ImportError:
    from tkinter import *
import time
import mysql.connector
import serial
import sys
import string
import os

# Modèles de requêtes
sql_compteur = "SELECT COUNT(*) AS ans FROM tb_produits WHERE prd_code = "
sql_type = "SELECT typ_id, typ_libelle FROM tb_produits INNER JOIN tb_types ON typ_id = prd_typ_id WHERE prd_code = "
sql_bac = "SELECT bcs_bac FROM tb_bacs WHERE bcs_typ_id = "
sql_liste_types = "SELECT typ_id, typ_libelle FROM tb_types ORDER BY typ_libelle"

# Chargement de la fenêtre
root = Tk()
root.title("Auto-détection")
root.geometry("480x320")
root.resizable(0,0)
barcode = ""
state = "ok"

def key(key):
    global barcode
    global state
    if(state == "ok"):
        barcode = barcode + str(key.char)
def submit(event):
    global barcode
    global state
    if(state == "ok" and barcode != ""):
        state = "nok"
        #Connexion BDD
        conn = mysql.connector.connect(host="localhost",user="user_innov",password="pass_innov",database="db_innov")
        cursor = conn.cursor()
        bac_dechet = "aucun bac assigné"
        type_dechet = ""
        entry_result.configure(state='normal')
        if(barcode == ""):
            entry_result.insert(END, "[" + time.strftime("%H:%M:%S") + "] " + "Aucun code-barre détecté !\n")
            state = "ok"
        else:
            if(len(barcode) <= 5):# On élimine un tant soit peu les codes-barres incomplets
                entry_result.insert(END, "[" + time.strftime("%H:%M:%S") + "] " + "Code barre erroné/illisible !\n")
                state = "ok"
            else:
                cursor.execute(sql_compteur+"'"+barcode+"'")
                count = cursor.fetchall()
                compteur= count[0][0]
                if(compteur > 0):
                    cursor.execute(sql_type+"'"+barcode+"'")
                    typer = cursor.fetchall()
                    for rows in typer:
                            id_dechet = str(rows[0])
                            type_dechet = str(rows[1])
                    cursor.execute(sql_bac+"'"+barcode+"'")
                    bacs = cursor.fetchall()
                    if(len(bacs) > 0):
                        for rows in bacs:
                            id_bac = rows[0]
                            bac_dechet += str(id_bac) + ", "
                    entry_result.insert(END, "[" + time.strftime("%H:%M:%S") + "] " + 'Le produit scanné est de type "' + type_dechet + '"' + ", bac(s) : " + bac_dechet + "\n")
                    state = "ok"
                else:
                    entry_result.insert(END, "[" + time.strftime("%H:%M:%S") + "] " + "Le produit n'est pas encore répertorié !\n")
                    entry_result.insert(END, "Souhaitez-vous l'ajouter ? (O/N) (désactivé)\n")
                    state = "ok"
        entry_result.configure(state='disabled')
        barcode = ""
        # Fermeture de la connexion SQL
        conn.close()

def shutdown():
    global state
    global barcode
    state = "nok"
    barcode = ""
    os.system("sudo shutdown -h now")

def restart():
    global state
    global barcode
    state = "nok"
    barcode = ""
    os.system("sudo shutdown -r")
    
root.bind("<Return>", submit)
root.bind("<Key>", key)

label = Label(root,text="Historique des codes-barres détectés", justify=CENTER, font=("Helvetica", 15), fg="green")
label.pack()
entry_result=Text(root, bd=1,width=57,height=15,state="disabled")
entry_result.pack()

button_shutdown = Button(root, text="X", command=shutdown)
button_shutdown.pack()

button_reboot = Button(root, text="R", command=restart)
button_reboot.pack()

conn = mysql.connector.connect(host="localhost",user="user_innov",password="pass_innov",database="db_innov")
cursor = conn.cursor()
    
conn.close()
root.mainloop()
