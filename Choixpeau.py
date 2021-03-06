# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from math import sqrt
from collections import Counter



table_persos = []
table_caracteristiques = []

#Importation des deux fichiers puis création des deux tables
with open("Characters.csv", mode='r', encoding='utf-8') as f:
    lines = f.readlines()
    key_line = lines[0].strip()
    keys = key_line.split(";")
    for line in lines[1:]:
        line = line.strip()
        values = line.split(';')
        dico = {}
        for i in range(len(keys)):
            dico[keys[i]] = values[i]
        table_persos.append(dico)

with open("Caracteristiques_des_persos.csv", mode='r', encoding='utf-8') as f:
    lines = f.readlines()
    key_line = lines[0].strip()
    keys = key_line.split(";")
    for line in lines[1:]:
        line = line.strip()
        values = line.split(';')
        dico = {}
        for i in range(len(keys)):
            dico[keys[i]] = values[i]
        table_caracteristiques.append(dico)
    
table_base = table_caracteristiques

#Fusion des deux tables
for element in table_persos:
    for nom in table_base:
        if element['Name'] == nom['Name']:
            nom['House'] = element['House']

#Création des profils prédéfinis
student1 = {'Name': 'Student1', 'Courage': 9, 'Ambition': 2, \
            'Intelligence': 8, 'Good': 9}
student2 = {'Name': 'Student2', 'Courage': 6, 'Ambition': 7, \
            'Intelligence': 9, 'Good': 7}
student3 = {'Name': 'Student3', 'Courage': 3, 'Ambition': 8, \
            'Intelligence': 6, 'Good': 3}
student4 = {'Name': 'Student4', 'Courage': 2, 'Ambition': 3, \
            'Intelligence': 7, 'Good': 8}
student5 = {'Name': 'Student5', 'Courage': 3, 'Ambition': 4, \
            'Intelligence': 8, 'Good': 8}

    

def choixpeau(student: dict, persos: list):
    """
    Paramètres
    ----------
    student : dictionnaire
        Profil d'élève à analyser
        
    persos : liste
        Table de personnages servant à placer student
        
    ---------- 
    Renvoie une f-string contenant la maison de student selon ses 5 plus proches
    voisins, ainsi que les dit voisins et leurs maisons.
    """
    
    liste_distance = []
    liste_voisins = []
    liste_maisons_voisins = []
       
    #Création d'une liste contenant la distance euclidienne de student avec
    #chaque personnage de persos
    for character in persos:
        distance = sqrt((int(character['Courage']) - student['Courage']) ** 2 + \
            (int(character['Intelligence']) - student['Intelligence']) ** 2 + \
            (int(character['Ambition']) - student['Ambition']) ** 2 + \
            (int(character['Good']) - student['Good']) ** 2)
        liste_distance.append(distance)
        character['Distance'] = distance
    liste_distance.sort()
    
    
    #Création d'une liste contenant les noms des voisins plus proches voisins
    #de student
    for length in persos:
        if len(liste_maisons_voisins) < 5:
            if length['Distance'] in liste_distance[:5]:
                liste_maisons_voisins.append(length['House'])
                liste_voisins.append(length['Name'])
   
    maison = Counter(liste_maisons_voisins)
    
    return(f"L'élève {student['Name']} est, en fonction de ses 5 plus proches "
           f"voisins, de la maison {maison.most_common(1)[0][0]} ! Ses "
           f"5 plus proches voisins sont {liste_voisins[0]} de "
           f"{liste_maisons_voisins[0]}, {liste_voisins[1]} de "
           f"{liste_maisons_voisins[1]}, {liste_voisins[2]} de "
           f"{liste_maisons_voisins[2]}, {liste_voisins[3]} de "
           f"{liste_maisons_voisins[3]} et {liste_voisins[4]} de "
           f"{liste_maisons_voisins[4]} !")


def choixpeau_k(student: dict, persos: list, voisins: int):
    """
    Paramètres
    ----------
    student : dictionnaire
        Profil d'élève à analyser
        
    persos : liste
        Table de personnages servant à placer student
        
    voisins : int
        Nombre de profil à prendre en compte pour placer student
    ---------- 
    Renvoie une f-string contenant la maison de student selon ses plus proches
    voisins, ainsi que les dit voisins.
    """
    
    liste_distance = []
    liste_voisins = []
    liste_maisons_voisins = []
       
    #Création d'une liste contenant la distance euclidienne de student avec
    #chaque personnage de persos
    for character in persos:
        distance = sqrt((int(character['Courage']) - student['Courage']) ** 2 + \
            (int(character['Intelligence']) - student['Intelligence']) ** 2 + \
            (int(character['Ambition']) - student['Ambition']) ** 2 + \
            (int(character['Good']) - student['Good']) ** 2)
        liste_distance.append(distance)
        character['Distance'] = distance
    liste_distance.sort()
    
    
    #Création d'une liste contenant les noms des voisins plus proches voisins
    #de student
    for length in persos:
        if len(liste_maisons_voisins) < voisins:
            if length['Distance'] in liste_distance[:voisins]:
                liste_maisons_voisins.append(length['House'])
                liste_voisins.append(length['Name'])
   
    maison = Counter(liste_maisons_voisins)
    
    return(f"L'élève {student['Name']} est, en fonction de ses {voisins} "
             "plus proches voisins, de la maison "
             f"{maison.most_common(1)[0][0]} ! Ses {voisins} plus proches "
             f"voisins sont {liste_voisins} !")



def choixpeau_manuel(persos: list):
    """
    Paramètres
    ----------
        
    persos : liste
        Table de personnages servant de base pour placer le profil à analyser

    ---------- 
    Renvoie une f-string contenant la maison du profil à analyser selon ses
    plus proches voisins, ainsi que les dit voisins.
    """
    
    student = {}
    liste_distance_manuelle = []
    liste_voisins = []
    liste_maisons_voisins = []
    
    #Création des valeurs de student
    voisins = int(input("Saisissez le nombre de voisins pris en compte : "))
    assert voisins > 0, "Le nombre de voisins doit être supérieur à 0 !"
    
    student['Name'] = str(input("Saisissez le nom de l'élève : "))
    
    student['Courage'] = int(input("Saisissez le courage de l'élève, de 1 à 10 : "))
    assert 1 <= student['Courage'] <= 10, "Le nombre saisi n'est pas compris entre 1 et 10 !"
    
    student['Intelligence'] = int(input("Saisissez l'intelligence de l'élève, de 1 à 10 : "))
    assert 1 <= student['Intelligence'] <= 10, "Le nombre saisi n'est pas compris entre 1 et 10 !"
    
    student['Ambition'] = int(input("Saisissez l'ambition de l'élève, de 1 à 10 : "))
    assert 1 <= student['Ambition'] <= 10, "Le nombre saisi n'est pas compris entre 1 et 10 !"
    
    student['Good'] = int(input("Saisissez la bonté de l'élève, de 1 à 10 : "))
    assert 1 <= student['Good'] <= 10, "Le nombre saisi n'est pas compris entre 1 et 10 !"

    
    #Création d'une liste contenant la distance euclidienne de student avec
    #chaque personnage de persos
    for character in persos:
        distance = sqrt((int(character['Courage']) - student['Courage']) ** 2 + \
            (int(character['Intelligence']) - student['Intelligence']) ** 2 + \
            (int(character['Ambition']) - student['Ambition']) ** 2 + \
            (int(character['Good']) - student['Good']) ** 2)
        liste_distance_manuelle.append(distance)
        character['Distance'] = distance
    liste_distance_manuelle.sort()
    
    #Création d'une liste contenant les noms des voisins plus proches voisins
    #de student
    for length in persos:
        if len(liste_maisons_voisins) < voisins:
            if length['Distance'] in liste_distance_manuelle[:voisins]:
                liste_maisons_voisins.append(length['House'])
                liste_voisins.append(length['Name'])
                        
    maison = Counter(liste_maisons_voisins)
    
    return(f"L'élève {student['Name']} est, en fonction de ses {voisins} "
             "plus proches voisins, de la maison "
             f"{maison.most_common(1)[0][0]} ! Ses {voisins} plus proches "
             f"voisins sont {liste_voisins} !")


#IHM
print("Bonjour ! Choisissez quelque chose à faire :")
print("1. Passer au choixpeau les profils prédéfinis")
print("2. Passer au choixpeau les profils prédéfnis en choisissant le nombre de voisins")
print("3. Passer au choixpeau un profil ayant des caractéristiques remplies manuellement")
print(" ")

choix = int(input("Choisissez un numéro d'option : "))
assert 1 <= choix <= 3, "Veuillez saisir une option valide"

if choix == 1:
    print(" ")
    print(choixpeau(student1, table_base))
    print(" ")
    print(choixpeau(student2, table_base))
    print(" ")
    print(choixpeau(student3, table_base))
    print(" ")
    print(choixpeau(student4, table_base))
elif choix == 2:
    print(" ")
    choix_voisins = int(input("Saisissez le nombre de voisins : "))
    assert 0 < choix_voisins, "Veuillez saisir un nombre supérieur à 0"
    print(choixpeau_k(student1, table_base, choix_voisins))
    print(" ")
    print(choixpeau_k(student2, table_base, choix_voisins))
    print(" ")
    print(choixpeau_k(student3, table_base, choix_voisins))
    print("")
    print(choixpeau_k(student4, table_base, choix_voisins))
elif choix == 3:
    print(" ")
    print(choixpeau_manuel(table_base))
