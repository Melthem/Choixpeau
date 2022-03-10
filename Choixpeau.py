# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from math import sqrt
from collections import Counter



table_persos = []

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
    

table_caracteristiques = []

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

    

def choixpeau(student: dict, persos: list, voisins: int):
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
    for character in persos:
        distance = sqrt((int(character['Courage']) - student['Courage']) ** 2 + \
            (int(character['Intelligence']) - student['Intelligence']) ** 2 + \
            (int(character['Ambition']) - student['Ambition']) ** 2 + \
            (int(character['Good']) - student['Good']))
        liste_distance.append(distance)
        character['Distance'] = distance
    liste_distance.sort()
    
    liste_maisons_voisins = []
    for length in persos:
        if len(liste_maisons_voisins) < voisins:
            if length['Distance'] in liste_distance[:voisins]:
                liste_maisons_voisins.append(length['House'])
                liste_voisins.append(length['Name'])
   
    maison = Counter(liste_maisons_voisins)
    
    return(f"L'élève {student['Name']} est, en fonction de ses {voisins} "
             "plus proches voisins, de la maison "
             f"{maison.most_common(1)[0][0]} ! Ses {voisins} plus proches "
             f"voisins sont {liste_voisins[0]}, {liste_voisins[1]}, "
             f"{liste_voisins[2]}, et {liste_voisins[4]} !")


def choixpeau_manuel(student: dict, persos: list, voisins: int):
    """
    Paramètres
    ----------
    student : dictionnaire
        Profil d'élève à analyser, modifié ensuite
    persos : liste
        Table de personnages servant à placer student
    voisins : int
        Nombre de profil à prendre en compte pour placer student, modifié
        ensuite
    ---------- 
    Renvoie une f-string contenant la maison de student selon ses plus proches
    voisins, ainsi que les dit voisins.
    """
    liste_distance_manuelle = []
    liste_voisins = []
    voisins = int(input("Saisissez le nombre de voisins pris en compte : "))
    student['Name'] = str(input("Saisissez le nom de l'élève : "))
    student['Courage'] = int(input("Saisissez le courage de l'élève : "))
    student['Intelligence'] = int(input("Saisissez l'intelligence de l'élève : "))
    student['Ambition'] = int(input("Saisissez l'ambition de l'élève : "))
    student['Good'] = int(input("Saisissez la bonté de l'élève : "))

    for character in persos:
        distance = sqrt((int(character['Courage']) - student['Courage']) ** 2 + \
            (int(character['Intelligence']) - student['Intelligence']) ** 2 + \
            (int(character['Ambition']) - student['Ambition']) ** 2 + \
            (int(character['Good']) - student['Good']))
        liste_distance_manuelle.append(distance)
        character['Distance'] = distance
    liste_distance_manuelle.sort()
    
    liste_maisons_voisins = []
    for length in persos:
        if len(liste_maisons_voisins) < voisins:
            if length['Distance'] in liste_distance_manuelle[:voisins]:
                liste_maisons_voisins.append(length['House'])
                liste_voisins.append(length['Name'])
    maison = Counter(liste_maisons_voisins)
    
    return(f"L'élève {student['Name']} est, en fonction de ses {voisins} "
             "plus proches voisins, de la maison "
             f"{maison.most_common(1)[0][0]} ! Ses {voisins} plus proches "
             f"voisins sont {liste_voisins[0]}, {liste_voisins[1]}, "
             f"{liste_voisins[2]}, et {liste_voisins[4]} !")
