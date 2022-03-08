# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

table_persos = []

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

print(table_base)
            