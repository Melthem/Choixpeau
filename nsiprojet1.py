# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 20:04:34 2022

@author: leoba
"""
from math import sqrt
from collections import Counter

SonGoku = {'Name': 'Son Goku', 'Courage': 10, 'Ambition': 2, 'Intelligence': 6, 'Good': 10}
table_persos = []
liste_distance = []

#Si quelqu'un regarde le code Son Goku c'est juste un test hein

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

for element in table_persos:
    for nom in table_base:
        if element['Name'] == nom['Name']:
            nom['House'] = element['House']

def choixpeau(student: dict, persos: list, voisins: int):
    for character in persos:
        distance = sqrt((int(character['Courage']) - student['Courage']) ** 2 + \
            (int(character['Intelligence']) - student['Intelligence']) ** 2 + \
            (int(character['Ambition']) - student['Ambition']) ** 2 + \
            (int(character['Good']) - student['Good']))
        liste_distance.append(distance)
        character['Distance'] = distance
    liste_distance.sort()
    
    liste_maisons_voisins = []
    for i in table_base:
        if len(liste_maisons_voisins) < voisins:
            if i['Distance'] in liste_distance[:voisins]:
                liste_maisons_voisins.append(i['House'])
    maison = Counter(liste_maisons_voisins)
    final  = str(maison.most_common(1)[0][0])
    
    return(f"L'élève {SonGoku['Name']} est, en fonction de ses {voisins} "
             "plus proches voisins, de la maison "
             f"{maison.most_common(1)[0][0]} !")
    

    
    