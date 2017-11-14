import tkinter as tk




LARGE_FONT = ("Verdana", 12) # font's family is Verdana, font's size is 12 
 
class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Label Poubelle") # set the title of the main window
        self.geometry("480x320") # set size of the main window to 300x300 pixels

        #SetFullScreen
        #self.overrideredirect(True)
        #self.geometry("{0}x{1}+0+0".format(self.winfo_screenwidth(), self.winfo_screenheight()))
        #self.focus_set()  # <-- move focus to this widget
        #self.bind("<Escape>", lambda e: e.widget.quit())
 
        # this container contains all the pages
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)   # make the cell in grid cover the entire window
        container.grid_columnconfigure(0,weight=1) # make the cell in grid cover the entire window
        self.frames = {} # these are pages we want to navigate to
 
        for F in (StartPage, Profil, Settings, Home, Types): # for each page
            frame = F(container, self) # create the page
            self.frames[F] = frame  # store into frames
            frame.grid(row=0, column=0, sticky="nsew") # grid it to container

        self.show_frame(Types) # Set the first page is StartPage
 
    def show_frame(self, name):
        frame = self.frames[name]
        frame.tkraise()








 
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Premiere Utilisation", font=LARGE_FONT)
        label.pack(pady=10, padx=10) # center alignment

        label1 = tk.Label(self, text="Bienvenue dans la configuration de \n votre poubelle connectee", height = 8 )
        label1.pack()



        button1 = tk.Button(self, text='Commencer la configuration',  # when click on this button, call the show_frame method to make PageOne appear
                            command=lambda : controller.show_frame(Profil), width = 30 , height = 5)
        button1.pack() # pack it in


        #Afficher Logo en bas
        #photo = tk.PhotoImage(file="logoPoubelle.png")
        #canvas = tk.Canvas(width=350, height=200)
        #canvas.create_image(300, 200, image=photo, bg="yellow")
        #canvas.pack()















class Profil(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


        label = tk.Label(self, text='Profil', font=LARGE_FONT)
        label.pack(pady=10, padx=10) # center alignment

        label1 = tk.Label(self, text='Nom du profil :')
        label1.pack()

        value = tk.StringVar()
        
        requete = """ Selec"""
        value.set(requete)
        entree = tk.Entry(self, textvariable=value, width=30)
        entree.pack()

        label2 = tk.Label(self, text='Ville :')
        label2.pack()

        value1 = tk.StringVar()
        entree1 = tk.Entry(self, textvariable=value1, width=30)
        entree1.pack()

        label3 = tk.Label(self, text='Code Postal :')
        label3.pack()

        value2 = tk.StringVar()
        entree2 = tk.Entry(self, textvariable=value2, width=30)
        entree2.pack()

        #saut d'espace
        label4 = tk.Label(self)
        label4.pack()


        button1 = tk.Button(self, text='Configuration des bacs',  # when click on this button, call the show_frame method to make PageOne appear
                            command=lambda : controller.show_frame(Settings), padx = 10, pady = 10)
        button1.pack() # pack it in

        #saut d'espace
        label5 = tk.Label(self)
        label5.pack()

        button2 = tk.Button(self, text='Retour accueil',  # when click on this button, call the show_frame method to make PageOne appear
                            command=lambda : controller.show_frame(Home), padx = 10, pady = 10)
        button2.pack() # pack it in

















class Settings(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Reglages', font=LARGE_FONT)
        label.pack(pady=10, padx=10) # center alignment





        label4 = tk.Label(self, text='Type du bac 1 :', font=LARGE_FONT)
        label4.place(x = 10, y = 50)


        listeOptions = ('Bleu', 'Jaune', 'Vert')
        v = tk.StringVar()
        v.set(listeOptions[0])
        om = tk.OptionMenu(self, v, *listeOptions)
        om.place(x = 40, y = 80)


        label5 = tk.Label(self, text='Type du bac 2 :', font=LARGE_FONT)
        label5.place(x = 170, y = 50)


        v1 = tk.StringVar()
        v1.set(listeOptions[0])
        om1 = tk.OptionMenu(self, v1, *listeOptions)
        om1.place(x = 200, y = 80)


        label6 = tk.Label(self, text='Type du bac 3 :', font=LARGE_FONT)
        label6.place(x = 330 ,  y = 50)


        v2 = tk.StringVar()
        v2.set(listeOptions[0])
        om = tk.OptionMenu(self, v2, *listeOptions)
        om.place(x = 360, y = 80)



        button1 = tk.Button(self, text='Configuration du profil',  # when click on this button, call the show_frame method to make PageOne appear
                            command=lambda : controller.show_frame(Profil), padx = 10, pady = 10)
        button1.place(x =170, y= 200) # pack it in



        button2 = tk.Button(self, text='Retour accueil',  # when click on this button, call the show_frame method to make PageOne appear
                            command=lambda : controller.show_frame(Home), padx = 10, pady = 10)
        button2.place(x = 190, y = 260) # pack it in
 












class Home(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Accueil', font=LARGE_FONT)
        label.pack(pady=10, padx=10) # center alignment

        #saut d'espace
        label2 = tk.Label(self)
        label2.pack(pady=10, padx=10)
 
        button1 = tk.Button(self, text='Configuration du profil',  # when click on this button, call the show_frame method to make PageOne appear
                            command=lambda : controller.show_frame(Profil), padx = 10, pady = 10)
        button1.pack() # pack it in

        #saut d'espace
        label1 = tk.Label(self)
        label1.pack()

        button2 = tk.Button(self, text='Configuration des bacs',  # when click on this button, call the show_frame method to make PageOne appear
                            command=lambda : controller.show_frame(Settings), padx = 10, pady = 10)
        button2.pack() # pack it in
 













class Types(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Types', font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        code = tk.StringVar(value = "lol")
        label = tk.Label(self, text='Votre objet n’est pas reconnu.')
        label.pack()

        label1 = tk.Label(self, text='Veuiller choisir un type pour le code a barres :')
        label1.pack()

        label2 = tk.Label(self,textvariable = code)
        label2.pack(pady=10, padx=10)

        listeOptions = ('Plastique', 'Papier', 'Carton')
        v = tk.StringVar()
        v.set(listeOptions[0])
        om = tk.OptionMenu(self, v, *listeOptions)
        om.pack()

        #saut d'espace
        label4 = tk.Label(self)
        label4.pack()

        #saut d'espace
        label5 = tk.Label(self)
        label5.pack()

        #saut d'espace
        label6 = tk.Label(self)
        label6.pack()

        #saut d'espace
        label7 = tk.Label(self)
        label7.pack()

        button = tk.Button(self, text='Valider le choix', # likewise StartPage
                            command=lambda : controller.show_frame(Home), padx = 60, pady = 15)
        button.pack()

 







if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()




#TODO : -Récuperer les inputs
#       -Envoyer les inputs en SQL
#       -Recevoir les données en SQL et les afficher
#       -Integrer la reconaissance de code a barres
#       -Integrer controle ouverture bacs