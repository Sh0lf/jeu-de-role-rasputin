import tkinter as tk
from tkinter import filedialog as fd
import pygame
import os


def open_file_path():  # fonction qui permet de demander à l'utilisateur de choisir le fichier du jeu et qui affiche le boutton "suivant"
    filename = fd.askopenfilename()
    print(filename)
    file[0] = filename
    if len(file[0]) > 2:
        bouton_suivantfile.place(relx=0.604, rely=0.353, height=54, width=107)


def create_premier():  # fonction pour créer le premier menu
    Frame1 = tk.Frame(root, relief='groove', borderwidth="2", background="#80e1a7")
    Frame1.place(relx=0.033, rely=0.044, relheight=0.233, relwidth=0.942)

    label_acceuil = tk.Label(Frame1, background="#80e1a7", disabledforeground="#a3a3a3",
                             font="-family {Forte} -size 24 -weight bold -underline 1", foreground="#000000",
                             highlightbackground="#f0f0f0f0f0f0", text='''Bienvenue sur DualCent''')
    label_acceuil.place(relx=0.017, rely=0.133, height=71, width=574)

    Frame2 = tk.Frame(root, relief='groove', borderwidth="2", background="#80e1a7")
    Frame2.place(relx=0.031, rely=0.289, relheight=0.567, relwidth=0.945)

    bouton_jouer = tk.Button(Frame2, text='''JOUER''',
                             command=lambda: [create_deuxieme(), Frame1.place_forget(), Frame2.place_forget(),
                                              label_credits.place_forget()], activebackground="#ececec",
                             activeforeground="#000000", background="#85b90b", disabledforeground="#a3a3a3",
                             foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black", pady="0")
    bouton_jouer.place(relx=0.083, rely=0.353, height=54, width=107)

    bouton_editer = tk.Button(Frame2, text='''EDITER''', command=lambda: os.system('editor.py'),
                              activebackground="#ececec", activeforeground="#000000", background="#85b90b",
                              disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                              highlightcolor="black", pady="0")
    bouton_editer.place(relx=0.413, rely=0.353, height=54, width=107)

    bouton_quitter = tk.Button(Frame2, text='''QUITTER''', command=root.quit, activebackground="#ececec",
                               activeforeground="#000000", background="#85b90b", disabledforeground="#a3a3a3",
                               foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black", pady="0")
    bouton_quitter.place(relx=0.744, rely=0.353, height=54, width=107)

    label_credits = tk.Label(root, text='''Crée par Rasputin Team''', background="#bff2c7",
                             disabledforeground="#a3a3a3", foreground="#000000")
    label_credits.place(relx=0.719, rely=0.889, height=41, width=174)


def create_deuxieme():  # fonction pour créer la premiere fenetre apres le main menu
    global Frame3, bouton_suivantfile

    Frame3 = tk.Frame(root, relief='groove', borderwidth="2", background="#80e1a7")
    Frame3.place(relx=0.031, rely=0.289, relheight=0.567, relwidth=0.945)

    bouton_selectionfile = tk.Button(Frame3, text='''Choisir un fichier :''', command=open_file_path,
                                     activebackground="#ececec", activeforeground="#000000", background="#85b90b",
                                     disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                                     highlightcolor="black", pady="0")
    bouton_selectionfile.place(relx=0.404, rely=0.353, height=54, width=107)

    bouton_suivantfile = tk.Button(Frame3, text='''Suivant''', command=create_troisieme, activebackground="#ececec",
                                   activeforeground="#000000", background="#85b90b", disabledforeground="#a3a3a3",
                                   foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                   pady="0")

    bouton_retour = tk.Button(Frame3, text='''Retour''', command=lambda: [Frame3.place_forget(), create_premier()],
                              activebackground="#ececec", activeforeground="#000000", background="#85b90b",
                              disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 12", foreground="#000000",
                              highlightbackground="#d9d9d9", highlightcolor="black", pady="0")
    bouton_retour.place(relx=0.204, rely=0.353, height=54, width=107)


def create_troisieme():  # fonction pour créer la dexieme fenetre apres le main menu (statistiques)
    Frame3.destroy()

    global scale_attaque, scale_defense, scale_agilite, scale_chance, Frame5, monTexte, label_update, Frame4
    monTexte = tk.StringVar()
    monTexte.set("Il vous reste 30 points !")

    Frame4 = tk.Frame(root, relief='groove', borderwidth="2", background="#40cc58")
    Frame4.place(relx=0.017, rely=0.022, relheight=0.167, relwidth=0.958)

    label_caracteristiques = tk.Label(Frame4, text='''Choisissez vos caractéristiques :''', background="#40cc58",
                                      disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 14 -underline 1",
                                      foreground="#000000")
    label_caracteristiques.place(relx=0.016, rely=0.12, height=54, width=304)

    label_update = tk.Label(Frame4, textvariable=monTexte, background="#40cc58", disabledforeground="#a3a3a3",
                            font="-family {Segoe UI} -size 14", foreground="#000000")
    label_update.place(relx=0.538, rely=0.12, height=54, width=264)

    Labelframe1 = tk.LabelFrame(root, relief='groove', foreground="black", text='''Attaque''', background="#40cc58")
    Labelframe1.place(relx=0.016, rely=0.2, relheight=0.189, relwidth=0.781)

    scale_attaque = tk.Scale(Labelframe1, from_=0.0, to=30, command=update_text, activebackground="#ececec",
                             background="#55a25f", foreground="#000000", highlightbackground="#55a25f",
                             highlightcolor="black", length="586", orient="horizontal", troughcolor="#55a25f")
    scale_attaque.place(relx=0.016, rely=0.271, relheight=0.580, relwidth=0.962)

    Labelframe2 = tk.LabelFrame(root, relief='groove', foreground="black", text='''Défense''', background="#40cc58")
    Labelframe2.place(relx=0.016, rely=0.4, relheight=0.189, relwidth=0.781)

    scale_defense = tk.Scale(Labelframe2, from_=0.0, to=30, command=update_text, activebackground="#ececec",
                             background="#55a25f", foreground="#000000", highlightbackground="#55a25f",
                             highlightcolor="black", length="586", orient="horizontal", troughcolor="#55a25f")
    scale_defense.place(relx=0.016, rely=0.271, relheight=0.580, relwidth=0.962)

    Labelframe3 = tk.LabelFrame(root, relief='groove', foreground="black", text='''Agilité''', background="#40cc58")
    Labelframe3.place(relx=0.016, rely=0.6, relheight=0.189, relwidth=0.781)

    scale_agilite = tk.Scale(Labelframe3, from_=0.0, to=30, command=update_text, activebackground="#ececec",
                             background="#55a25f", foreground="#000000", highlightbackground="#55a25f",
                             highlightcolor="black", length="586", orient="horizontal", troughcolor="#55a25f")
    scale_agilite.place(relx=0.016, rely=0.271, relheight=0.580, relwidth=0.962)

    Labelframe4 = tk.LabelFrame(root, relief='groove', foreground="black", text='''Chance''', background="#40cc58")
    Labelframe4.place(relx=0.016, rely=0.8, relheight=0.189, relwidth=0.781)

    scale_chance = tk.Scale(Labelframe4, from_=0.0, to=30, command=update_text, activebackground="#ececec",
                            background="#55a25f", foreground="#000000", highlightbackground="#55a25f",
                            highlightcolor="black", length="586", orient="horizontal", troughcolor="#55a25f")
    scale_chance.place(relx=0.016, rely=0.271, relheight=0.580, relwidth=0.962)

    Frame5 = tk.Frame(root, relief='groove', borderwidth="2", background="#40cc58")
    Frame5.place(relx=0.813, rely=0.2, relheight=0.789, relwidth=0.164)

    bouton_retour = tk.Button(Frame5, text='''Retour''',
                              command=lambda: [create_deuxieme(), Frame4.place_forget(), Frame5.place_forget(),
                                               Labelframe1.place_forget(), Labelframe2.place_forget(),
                                               Labelframe3.place_forget(), Labelframe4.place_forget()],
                              activebackground="#ececec", activeforeground="#000000", background="#55a25f",
                              font="-family {Segoe UI} -size 12", disabledforeground="#a3a3a3", foreground="#000000",
                              highlightbackground="#d9d9d9", highlightcolor="black", pady="0")
    bouton_retour.place(relx=0.095, rely=0.817, height=44, width=87)


def reinit():  # fonction pour reinitialiser les statistiques si l'utilisateur veut d'autres choses
    scale_attaque.config(state="normal", takefocus=0)
    scale_agilite.config(state="normal", takefocus=0)
    scale_defense.config(state="normal", takefocus=0)
    scale_chance.config(state="normal", takefocus=0)
    scale_attaque.set(0)
    scale_agilite.set(0)
    scale_defense.set(0)
    scale_chance.set(0)
    bouton_suivantcara.place_forget()
    bouton_reinitcara.place_forget()
    label_update.configure(background="#40cc58")
    label_update.configure(foreground="#000000")


def update_text(var):  # fonction pour update le nombre de points restants
    global bouton_suivantcara, bouton_reinitcara

    bouton_suivantcara = tk.Button(Frame5, command=lambda: [create_quatrieme(), Frame5.destroy(), Frame4.destroy()])

    attaque = scale_attaque.get()
    defense = scale_defense.get()
    agilite = scale_agilite.get()
    chance = scale_chance.get()
    point_iu = 30 - attaque - defense - agilite - chance

    if point_iu == 0:  # s'il n'y a plus de points disponibles

        scale_attaque.config(state="disabled", takefocus=0)
        scale_defense.config(state="disabled", takefocus=0)
        scale_agilite.config(state="disabled", takefocus=0)
        scale_chance.config(state="disabled", takefocus=0)

        bouton_suivantcara.place(relx=0.095, rely=0.197, height=44, width=87)
        bouton_suivantcara.configure(activebackground="#ececec")
        bouton_suivantcara.configure(activeforeground="#000000")
        bouton_suivantcara.configure(background="#55a25f")
        bouton_suivantcara.configure(disabledforeground="#a3a3a3")
        bouton_suivantcara.configure(font="-family {Segoe UI} -size 12")
        bouton_suivantcara.configure(foreground="#000000")
        bouton_suivantcara.configure(highlightbackground="#d9d9d9")
        bouton_suivantcara.configure(highlightcolor="black")
        bouton_suivantcara.configure(pady="0")
        bouton_suivantcara.configure(text='''Suivant''')

        bouton_reinitcara = tk.Button(Frame5, text='''Réinitialiser''', command=reinit, activebackground="#ececec",
                                      activeforeground="#000000", background="#55a25f", disabledforeground="#a3a3a3",
                                      font="-family {Segoe UI} -size 12", foreground="#000000",
                                      highlightbackground="#d9d9d9", highlightcolor="black", pady="0")
        bouton_reinitcara.place(relx=0.095, rely=0.507, height=44, width=87)

        label_update.configure(background="#ff0000")
        label_update.configure(foreground="#ffffff")

    if 1 < point_iu:  # afficher le nombre de points restants avec un S
        monTexte.set("Il vous reste " + str(point_iu) + " points !")

    if point_iu <= 1:  # afficher le nombre de point restant sans S
        monTexte.set("Il vous reste " + str(point_iu) + " point !")

    if point_iu < 0:  # si la personne arrive à depasser le nombre de points max
        monTexte.set("Attention, trop de points")

        label_update.configure(background="#ff0000")
        label_update.configure(foreground="#ffffff")

        scale_attaque.config(state="disabled", takefocus=0)
        scale_defense.config(state="disabled", takefocus=0)
        scale_agilite.config(state="disabled", takefocus=0)
        scale_chance.config(state="disabled", takefocus=0)

        bouton_reinitcara = tk.Button(Frame5, text='''Réinitialiser''', command=reinit, activebackground="#ececec",
                                      activeforeground="#000000", background="#55a25f", disabledforeground="#a3a3a3",
                                      font="-family {Segoe UI} -size 12", foreground="#000000",
                                      highlightbackground="#d9d9d9", highlightcolor="black", pady="0")
        bouton_reinitcara.place(relx=0.095, rely=0.507, height=44, width=87)


def create_quatrieme():  # fonction pour créer la fenetre de jeu !
    Frame1 = tk.Frame(root)
    Frame1.place(relx=0.009, rely=0.014, relheight=0.118, relwidth=0.977)
    Frame1.configure(relief='groove')
    Frame1.configure(borderwidth="2")
    Frame1.configure(relief="groove")
    Frame1.configure(background="#d9d9d9")

    Label1 = tk.Label(Frame1)
    Label1.place(relx=0.009, rely=0.118, height=61, width=1033)
    Label1.configure(background="#d9d9d9")
    Label1.configure(disabledforeground="#a3a3a3")
    Label1.configure(font="-family {Segoe UI} -size 21 -weight bold -underline 1")
    Label1.configure(foreground="#000000")
    Label1.configure(text='''Titre histoire''')

    Frame2 = tk.Frame(root)
    Frame2.place(relx=0.009, rely=0.153, relheight=0.826
                 , relwidth=0.977)
    Frame2.configure(relief='groove')
    Frame2.configure(borderwidth="2")
    Frame2.configure(relief="groove")
    Frame2.configure(background="#d9d9d9")

    Frame3 = tk.Frame(Frame2)
    Frame3.place(relx=0.019, rely=0.168, relheight=0.277
                 , relwidth=0.175)
    Frame3.configure(relief='groove')
    Frame3.configure(borderwidth="2")
    Frame3.configure(relief="groove")
    Frame3.configure(background="#d9d9d9")

    Label2 = tk.Label(Frame3)
    Label2.place(relx=0.054, rely=0.061, height=141, width=164)
    Label2.configure(background="#d9d9d9")
    Label2.configure(disabledforeground="#a3a3a3")
    Label2.configure(foreground="#000000")
    Label2.configure(text='''Choix 1''')

    Frame4 = tk.Frame(Frame2)
    Frame4.place(relx=0.408, rely=0.168, relheight=0.277, relwidth=0.174)
    Frame4.configure(relief='groove')
    Frame4.configure(borderwidth="2")
    Frame4.configure(relief="groove")
    Frame4.configure(background="#d9d9d9")

    Label3 = tk.Label(Frame4)
    Label3.place(relx=0.054, rely=0.061, height=141, width=165)
    Label3.configure(background="#d9d9d9")
    Label3.configure(disabledforeground="#a3a3a3")
    Label3.configure(foreground="#000000")
    Label3.configure(text='''Choix 2''')

    Frame5 = tk.Frame(Frame2)
    Frame5.place(relx=0.796, rely=0.168, relheight=0.277
                 , relwidth=0.173)
    Frame5.configure(relief='groove')
    Frame5.configure(borderwidth="2")
    Frame5.configure(relief="groove")
    Frame5.configure(background="#d9d9d9")

    Label4 = tk.Label(Frame5)
    Label4.place(relx=0.055, rely=0.061, height=141, width=161)
    Label4.configure(background="#d9d9d9")
    Label4.configure(disabledforeground="#a3a3a3")
    Label4.configure(foreground="#000000")
    Label4.configure(text='''Choix 3''')

    Button1 = tk.Button(Frame2)
    Button1.place(relx=0.645, rely=0.067, height=24, width=247)
    Button1.configure(activebackground="#ececec")
    Button1.configure(activeforeground="#000000")
    Button1.configure(background="#d9d9d9")
    Button1.configure(disabledforeground="#a3a3a3")
    Button1.configure(foreground="#000000")
    Button1.configure(highlightbackground="#d9d9d9")
    Button1.configure(highlightcolor="black")
    Button1.configure(pady="0")
    Button1.configure(text='''Ouvrir l'inventaire''')

    Labelframe1 = tk.LabelFrame(Frame2)
    Labelframe1.place(relx=0.019, rely=0.017, relheight=0.126
                      , relwidth=0.483)
    Labelframe1.configure(relief='groove')
    Labelframe1.configure(foreground="black")
    Labelframe1.configure(text='''Points de vie''')
    Labelframe1.configure(background="#d9d9d9")

    Scale1 = tk.Scale(Labelframe1, from_=0.0, to=100.0)
    Scale1.place(relx=0.02, rely=0.267, relwidth=0.973, relheight=0.0
                 , height=42, bordermode='ignore')
    Scale1.configure(activebackground="#ececec")
    Scale1.configure(background="#d9d9d9")
    Scale1.configure(foreground="#000000")
    Scale1.configure(highlightbackground="#d9d9d9")
    Scale1.configure(highlightcolor="black")
    Scale1.configure(orient="horizontal")
    Scale1.configure(troughcolor="#d9d9d9")
    Scale1.set(100)

    Button2 = tk.Button(Frame2)
    Button2.place(relx=0.019, rely=0.555, height=64, width=187)
    Button2.configure(activebackground="#ececec")
    Button2.configure(activeforeground="#000000")
    Button2.configure(background="#d9d9d9")
    Button2.configure(disabledforeground="#a3a3a3")
    Button2.configure(foreground="#000000")
    Button2.configure(highlightbackground="#d9d9d9")
    Button2.configure(highlightcolor="black")
    Button2.configure(pady="0")
    Button2.configure(text='''Choisir''')

    Button3 = tk.Button(Frame2)
    Button3.place(relx=0.408, rely=0.555, height=64, width=187)
    Button3.configure(activebackground="#ececec")
    Button3.configure(activeforeground="#000000")
    Button3.configure(background="#d9d9d9")
    Button3.configure(disabledforeground="#a3a3a3")
    Button3.configure(foreground="#000000")
    Button3.configure(highlightbackground="#d9d9d9")
    Button3.configure(highlightcolor="black")
    Button3.configure(pady="0")
    Button3.configure(text='''Choisir''')

    Button4 = tk.Button(Frame2)
    Button4.place(relx=0.796, rely=0.555, height=64, width=177)
    Button4.configure(activebackground="#ececec")
    Button4.configure(activeforeground="#000000")
    Button4.configure(background="#d9d9d9")
    Button4.configure(disabledforeground="#a3a3a3")
    Button4.configure(foreground="#000000")
    Button4.configure(highlightbackground="#d9d9d9")
    Button4.configure(highlightcolor="black")
    Button4.configure(pady="0")
    Button4.configure(text='''Choisir''')

    Button5 = tk.Button(Frame2)
    Button5.place(relx=0.199, rely=0.79, height=64, width=217)
    Button5.configure(activebackground="#ececec")
    Button5.configure(activeforeground="#000000")
    Button5.configure(background="#d9d9d9")
    Button5.configure(disabledforeground="#a3a3a3")
    Button5.configure(foreground="#000000")
    Button5.configure(highlightbackground="#d9d9d9")
    Button5.configure(highlightcolor="black")
    Button5.configure(pady="0")
    Button5.configure(text='''Retour''')

    Button6 = tk.Button(Frame2)
    Button6.place(relx=0.588, rely=0.79, height=64, width=217)
    Button6.configure(activebackground="#ececec")
    Button6.configure(activeforeground="#000000")
    Button6.configure(background="#d9d9d9")
    Button6.configure(disabledforeground="#a3a3a3")
    Button6.configure(foreground="#000000")
    Button6.configure(highlightbackground="#d9d9d9")
    Button6.configure(highlightcolor="black")
    Button6.configure(pady="0")
    Button6.configure(text='''Quitter''')


def create_options():  # fonction pour créer la fenetre contenant les différentes options
    def change_volume(val):  # fonction pour changer le volume du son jouer par pygame
        var = int(val) / 100
        son.set_volume(var)

    top = tk.Toplevel(root)
    top.geometry("640x480+468+138")
    top.resizable(0, 0)
    top.title("Options")
    top.configure(background="#7dffbe")

    Labelframe5 = tk.LabelFrame(top, text='''Changer le volume de la musique''', relief='groove',
                                font="-family {Segoe UI} -size 13", foreground="black", background="#85a736")
    Labelframe5.place(relx=0.031, rely=0.313, relheight=0.281, relwidth=0.938)

    scale_volume = tk.Scale(Labelframe5, from_=0.0, to=100.0, command=change_volume, activebackground="#ececec",
                            background="#3ca253", foreground="#000000", highlightbackground="#3ca253",
                            highlightcolor="#000000", length="566", orient="horizontal", troughcolor="#3ca253")
    scale_volume.place(relx=0.033, rely=0.222, relheight=0.681, relwidth=0.943)
    scale_volume.set(50)

    bouton_retour = tk.Button(top, text='''Retour''', command=top.destroy, activebackground="#ececec",
                              activeforeground="#000000", background="#3ca253", disabledforeground="#a3a3a3",
                              font="-family {Segoe UI} -size 14", foreground="#000000", highlightbackground="#d9d9d9",
                              highlightcolor="black", pady="0")
    bouton_retour.place(relx=0.359, rely=0.813, height=64, width=177)

    label_options = tk.Label(top, text='''Options :''', background="#7dffbe", disabledforeground="#a3a3a3",
                             font="-family {Segoe UI} -size 14 -weight bold -underline 1", foreground="#000000")
    label_options.place(relx=0.328, rely=0.021, height=51, width=204)


file = ["0"]

pygame.mixer.init()

son = pygame.mixer.Sound('main_loop.wav')
son.play(loops=-1, maxtime=0, fade_ms=0)
son.set_volume(0.5)

# création du main menu

root = tk.Tk()
root.geometry("1080x720+468+138")
root.resizable(0, 0)
root.title("DualCent")
root.configure(background="#bff2c7")

create_premier()

# création du menu en haut de la page

menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Options", command=create_options)
file_menu.add_separator()
file_menu.add_command(label="Quitter", command=root.quit)
menu_bar.add_cascade(label="Fichier", menu=file_menu)
root.config(menu=menu_bar)

root.mainloop()
