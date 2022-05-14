import string
import random
from art import *


## variables qui vont permettrent la génération du mot de passe
alphabets = list(string.ascii_letters)
digits = list(string.digits)
special_characters = list("!@#$%^&*()")
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def header():
    print("\n▪====================================================================================================================================================▪\n")
    tprint("Julien  Password   Generator")
    print("▪====================================================================================================================================================▪\n")

def generate_random_password():
    ## Longueur du mot de passe
    length = int(input("● Renseigner la longueur du mot de passe: "))

    ## on défini le nombre de lettres, de chiffres et de caractères spéciaux du mot de passe
    alphabets_count = int(input("● Nombre de lettres: "))
    digits_count = int(input("● Nombre de chiffres: "))
    special_characters_count = int(input("● Nombre de caractères spéciaux: "))

    characters_count = alphabets_count + digits_count + special_characters_count

    ## Verification si le nombre total de caractères renseigné est plus grand que la longueur du mot de passe
    if characters_count > length:
        print("● Le nombre total de caractères est supérieur à la longueur du mot de passe.")
        return

    ## Initialisation du mot de passe
    password = []

    ## Choix des lettres au hasard
    for i in range(alphabets_count):
        password.append(random.choice(alphabets))

    ## Choix des chiffres au hasard
    for i in range(digits_count):
        password.append(random.choice(digits))

    ## Choix des caractères spéciaux au hasard
    for i in range(special_characters_count):
        password.append(random.choice(special_characters))

    ## si le nombre total de caractères est inférieur à la longueur du mot de passe
    ## on ajoute des caractères aléatoires pour qu'il soit égal à la longueur du mot de passe.
    if characters_count < length:
        random.shuffle(characters)
        for i in range(length - characters_count):
            password.append(random.choice(characters))

    ## on melange le resultat pour que le mot de passe soit encore plus aléatoire
    random.shuffle(password)

    ## on convertit le mot de passe en chaine de caractère
    ## et on l'affiche
    print("● Votre mot de passe généré :","".join(password))

def credit():
    print("\nmerci d'avoir utilisé ce générateur :)")
    print("\ncréateur : https://github.com/chadow4")


## Appel de la fonction
header()
generate_random_password()
credit()
