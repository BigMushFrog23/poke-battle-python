# -*- coding: utf-8 -*-

# importation des bibliothèques nécessaires au projet
import tkinter, random, threading, pygame

# Initialize the victory_music_played flag
pygame.mixer.init()
victory_music_played = False
music_played = False             
crit_sound = pygame.mixer.Sound("Bonk.wav")

def play_crit_music():
    global crit_music        
    crit_sound.play()

def play_music_py():
    global music_played
    
    if not music_played:
        pygame.mixer.init()
        
        pygame.mixer.Channel(0).play(pygame.mixer.Sound('Cynthia_battle.wav'), -1)
        pygame.mixer.Channel(0).set_volume(0.7)
        music_played = True
        
        
def play_victory_music():
    global victory_music_played  # Use the global flag    

    if not victory_music_played:  # Check if victory music hasn't been played yet
        pygame.mixer.init()
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('Pokemon_Victory.wav'))
        pygame.mixer.Channel(1).set_volume(0.7)
        victory_music_played = True  # Set the flag to True after playing

# Function to stop the music and close the window
def stop_music_and_close_window():
    pygame.mixer.Channel(0).stop()
    pygame.mixer.Channel(1).stop()
    fenetre.quit()
    fenetre.destroy()

# création de la fenêtre de dessin
fenetre = tkinter.Tk()
fenetre.title("Pokemon Battle")
fenetre.attributes('-topmost', True)  # Set the window to be on top
mon_canvas = tkinter.Canvas(fenetre, width = 1400, height = 720,
                        background = 'lightgreen')
# affichage de la zone de dessin
mon_canvas.pack()

# Create a thread for playing music (with daemon=True)
music_thread = threading.Thread(target=play_music_py, daemon=True)
music_thread.start()

# Initialize the space_key_held flag
space_key_held = False
combat_in_progress = True  # Set combat as initially in progress
    
def on_space_key_press(event):
    global space_key_held

    if not space_key_held and combat_in_progress:
        space_key_held = True
        for pokemon in a1.listeDePokemons:
            pokemon.double_velocity()

# Add a function to handle the space key release event
def on_space_key_release(event):
    global space_key_held

    if space_key_held and combat_in_progress:
        space_key_held = False                                                                                                    
        for pokemon in a1.listeDePokemons:
            pokemon.reset_velocity()

# Bind the space key press and release events to the window (fenetre)                                               
fenetre.bind("<KeyPress-space>", on_space_key_press)
fenetre.bind("<KeyRelease-space>", on_space_key_release)


# Add the background image to the canvas
background_image = tkinter.PhotoImage(file="Pokemon_Arena.png")
background = mon_canvas.create_image(0, 0, anchor=tkinter.NW, image=background_image)

# stockage de l'image du pokemon Reptincel dans une variable
img_reptincel = tkinter.PhotoImage(file = "Reptincel.png")
img_reptincel_right = tkinter.PhotoImage(file = "Reptincel_Right.png")
img_mudkip = tkinter.PhotoImage(file = "Mudkip.png")
img_mudkip_right = tkinter.PhotoImage(file = "Mudkip_Right.png")
img_oshawott = tkinter.PhotoImage(file = "Oshawott.png")
img_oshawott_right = tkinter.PhotoImage(file = "Oshawott_Right.png")
img_mimikyu = tkinter.PhotoImage(file = "Mimikyu.png")
img_mimikyu_right = tkinter.PhotoImage(file = "Mimikyu_Right.png")
img_magikarp = tkinter.PhotoImage(file = "Magikarp.png")
img_magikarp_right = tkinter.PhotoImage(file = "Magikarp_Right.png")
liste_reptincel = [img_reptincel, img_reptincel_right]
liste_mudkip = [img_mudkip, img_mudkip_right]
liste_oshawott = [img_oshawott, img_oshawott_right]
liste_mimikyu = [img_mimikyu, img_mimikyu_right]
liste_magikarp = [img_magikarp, img_magikarp_right]

class Pokemon:
    #constructeur
    def __init__(self, xLoc, yLoc, image, puissance):
        self.xLoc      = xLoc # entier
        self.yLoc      = yLoc # entier
        xVel = random.randint(-5, 5)
        yVel = random.randint(-5, 5)
        self.xVel = xVel
        if self.xVel == 0:
            self.xVel = random.randint(-5, 5)
        self.yVel = yVel
        if self.yVel == 0:
            self.yVel = random.randint(-5, 5)
        self.image     = image # image du pokemon
        if self.image == img_reptincel:
            self.photo_image = random.choice(liste_reptincel)
        elif self.image == img_mudkip:
            self.photo_image = random.choice(liste_mudkip)
        elif self.image == img_oshawott:
            self.photo_image = random.choice(liste_oshawott)
        elif self.image == img_mimikyu:
            self.photo_image = random.choice(liste_mimikyu)
        elif self.image == img_magikarp:
            self.photo_image = random.choice(liste_magikarp)
        self.puissance = puissance #puissance du Pokemon
        self.ko        = False # etat du Pokemon: KO ou pas KO
        self.img       = mon_canvas.create_image(self.xLoc, self.yLoc,
                                                 image  = self.photo_image)
        
        # Create a text label for puissance and store it in an instance variable
        self.puissance_label = mon_canvas.create_text(
            self.xLoc, self.yLoc + self.photo_image.height() // 2 + 5,
            text=f"Puissance: {self.puissance}", fill="black", font = 16)
        
    def update_puissance_text(self):
        # Update the puissance text label by deleting the old label and creating a new one
        mon_canvas.delete(self.puissance_label)
        self.puissance_label = mon_canvas.create_text(
            self.xLoc, self.yLoc + self.photo_image.height() // 2 + 5,
            text=f"Puissance: {self.puissance}", fill="black", font = 16)
        
        
        
    # Display a end text when there's only 1 pokemon left
    def display_big_text():
        mon_canvas.create_text(
            703, 200,
            text = "WINNER",
            font = ("Helvetica", 50),
            fill = "black"
        )
        
        # Method to double the velocity
    def double_velocity(self):
        self.xVel = self.xVel * 2
        self.yVel = self.yVel * 2

    # Method to reset the velocity to its original value
    def reset_velocity(self):
        self.xVel = self.xVel / 2
        self.yVel = self.yVel / 2
        
    def setNom(self, nom):
        self.nom = nom
        
    def getNom(self):
        return self.nom
    
    def setKo(self, ko):
        self.ko = ko
            
    
    def getKo(self):
        return self.ko
    
    def setxLoc(self, xLoc):
        self.xLoc = xLoc
        
    def getxLoc(self):
        return self.xLoc
    
    def setyLoc(self, yLoc):
        self.yLoc = yLoc
        
    def getyLoc(self):
        return self.yLoc
    
    def setPuissance(self, puissance):
        self.puissance = puissance
        
    def getPuissance(self):
        return self.puissance
        
    def delete_from_canvas(self):
        if self.ko == True:
            mon_canvas.delete(self.img)  # Delete the canvas item
            mon_canvas.delete(self.puissance_label)  # Delete the puissance text label
    
    def affiche(self):
        """Affiche le Pokemon selon ses nouvelles coordonnées
        Uniquement si celui-ci n’est pas KO """
        # move de l'image dans la zone de dessin
        if self.ko == False:
            mon_canvas.move(self.img, self.xVel, self.yVel)
        
    def deplacement(self):
        """Mets à jour les coordonnées du Pokemon
        selon son vecteur (xVel,yVel)
        Uniquement si celui-ci n’est pas KO """
        # si le Pokemon peut sortir de l'arène, sa direction s'inverse
        if self.ko == False:
            next_positionX = self.xLoc + self.xVel
            next_positionY = self.yLoc + self.yVel
            
            if next_positionX <= 50 or next_positionX >= 1360:
                self.xVel = (self.xVel * -1)
                        
            elif next_positionY <= 50 or next_positionY >= 670:
                self.yVel = (self.yVel * -1)
                
            self.xLoc = self.xLoc + self.xVel
            self.yLoc = self.yLoc + self.yVel


class Arene:
    # listeDePokemons est de type list
    def __init__(self):
        self.listeDePokemons = [] # Liste de Pokemons
        self.combat_in_progress = False
        
    # pour ajouter un Pokemon de class Pokemon
    def ajouter(self, pokemon):
        self.listeDePokemons.append(pokemon)
        
    def retirer(self):
        defeated_pokemon = []
        for pokemon in self.listeDePokemons:
            if pokemon.ko == True:
                defeated_pokemon.append(pokemon)

        for pokemon in defeated_pokemon:
            pokemon.delete_from_canvas()  # Delete the canvas item and the object itself
            self.listeDePokemons.remove(pokemon)  # Remove from the list
                
        
                
    # pour avoir le nombre de Pokemons de l'arene
    def nbPokemons(self):
        return len(self.listeDePokemons)

    
    # pour gérer le combat
class Combat:    
    
    def crit(crit_hit_chance):
        return crit_hit_chance == 4 
    
    def is_overlap(sprite1, sprite2):
    # Get the coordinates of the top-left and bottom-right corners for each sprite
        left1 = sprite1.xLoc - sprite1.photo_image.width() // 3
        right1 = sprite1.xLoc + sprite1.photo_image.width() // 3
        top1 = sprite1.yLoc - sprite1.photo_image.height() // 3
        bottom1 = sprite1.yLoc + sprite1.photo_image.height() // 3
    
        left2 = sprite2.xLoc - sprite2.photo_image.width() // 3
        right2 = sprite2.xLoc + sprite2.photo_image.width() // 3
        top2 = sprite2.yLoc - sprite2.photo_image.height() // 3
        bottom2 = sprite2.yLoc + sprite2.photo_image.height() // 3
    
        # Check for overlap using the conditions described above
        if (
            right1 < left2 or
            left1 > right2 or
            bottom1 < top2 or
            top1 > bottom2
        ):
            return False
        else:
            return True
    
    def __init__(self):
        num_pokemons = a1.nbPokemons()
        defeated_pokemon = []
        
        
        
        for i in range(num_pokemons):    
            for j in range(i + 1, num_pokemons):
                
                if Combat.is_overlap(a1.listeDePokemons[i], a1.listeDePokemons[j]):
                        
                        # Determine the winner based on power
                        if a1.listeDePokemons[i] and a1.listeDePokemons[j] in a1.listeDePokemons:
                            
                            if a1.listeDePokemons[i] and a1.listeDePokemons[j] not in defeated_pokemon:
                                
                                if a1.listeDePokemons[i].puissance >= 1 and a1.listeDePokemons[j].puissance >= 1:
                                    
                                    if a1.listeDePokemons[i].puissance <= a1.listeDePokemons[j].puissance:
                                        crit_hit_chance = random.randint(1, 6)
                                        if Combat.crit(crit_hit_chance) == True:
                                            play_crit_music()
                                            print("Critical Hit!")
                                            defeated_pokemon.append(a1.listeDePokemons[j])
                                            a1.listeDePokemons[i].puissance = a1.listeDePokemons[i].puissance + a1.listeDePokemons[j].puissance
                                            a1.listeDePokemons[j].puissance = 0
                                        else:
                                            defeated_pokemon.append(a1.listeDePokemons[i])
                                            a1.listeDePokemons[j].puissance = a1.listeDePokemons[j].puissance + a1.listeDePokemons[i].puissance
                                            a1.listeDePokemons[i].puissance = 0
                                    else:
                                        crit_hit_chance = random.randint(1, 6)
                                        if Combat.crit(crit_hit_chance) == True:
                                            play_crit_music()
                                            print("Critical Hit!")
                                            defeated_pokemon.append(a1.listeDePokemons[i])
                                            a1.listeDePokemons[j].puissance = a1.listeDePokemons[j].puissance + a1.listeDePokemons[i].puissance
                                            a1.listeDePokemons[i].puissance = 0
                                        else:
                                            defeated_pokemon.append(a1.listeDePokemons[j])
                                            a1.listeDePokemons[i].puissance = a1.listeDePokemons[i].puissance + a1.listeDePokemons[j].puissance
                                            a1.listeDePokemons[j].puissance = 0
        
        # Set defeated Pokémon as KO
        for pokemon in defeated_pokemon:
            pokemon.setKo(True)
                        
                            
a1 = Arene()
for i in range(15):
    temp_xLoc      = random.randint(60, 1340)
    temp_yLoc      = random.randint(40, 660)
    temp_puissance = random.randint(10, 300)
    temp_image     = random.randint(1, 5)
    
    if temp_image == 1:
        temp_image = img_reptincel
        
    elif temp_image == 2:
        temp_image = img_mudkip
        
    elif temp_image == 3:
        temp_image = img_oshawott
        
    elif temp_image == 4:
        temp_image = img_mimikyu
        
    elif temp_image == 5:
        temp_image = img_magikarp
    
    pokemon = Pokemon(temp_xLoc, temp_yLoc, temp_image, temp_puissance) 
    a1.ajouter(pokemon)

def fonction_principale():
    global victory_music_played, combat_in_progress, music_played  # Use the global flag
    if a1.nbPokemons() > 1:
        Combat()
        a1.retirer()  # Remove defeated Pokemon

            
        for i in range(a1.nbPokemons()):
            a1.listeDePokemons[i].deplacement()
            a1.listeDePokemons[i].affiche()
            Pokemon.update_puissance_text(a1.listeDePokemons[i])
        
    else:
        if a1.listeDePokemons[0].xLoc != 690 or a1.listeDePokemons[0].yLoc != 360:
            # Remove the old image from its previous location
            mon_canvas.delete(a1.listeDePokemons[0].img)
        Pokemon.update_puissance_text(a1.listeDePokemons[0])
        a1.listeDePokemons[0].xLoc = 700
        a1.listeDePokemons[0].yLoc = 334
        a1.listeDePokemons[0].img  = mon_canvas.create_image(a1.listeDePokemons[0].xLoc, a1.listeDePokemons[0].yLoc, 
                                                             image  = a1.listeDePokemons[0].photo_image)
        a1.listeDePokemons[0].affiche()
        Pokemon.display_big_text()
        combat_in_progress = False  # Combat is no longer in progress
        pygame.mixer.Channel(0).stop()
        if not victory_music_played:  # Check if victory music hasn't been played yet  
            mon_canvas.after(20, play_victory_music())
        
    mon_canvas.after(20, fonction_principale)


fonction_principale()

# Set the window close event to stop the music and close the window
fenetre.protocol("WM_DELETE_WINDOW", stop_music_and_close_window)

# gestion des événements, à laisser à la fin du code
fenetre.mainloop()