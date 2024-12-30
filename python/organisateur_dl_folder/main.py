#/usr/bin/python3

DOCUMENTATION = r"""
module: 
author: yindiana.fr
short_description: 
description:
    - 

prérequis
    - python -m pip install os

options
    N/A
"""

EXAMPLE = r"""
python3 main.py
"""

RETURN = r"""

"""

import os
import shutil       #pour déplacer les fichiers dans le bon répertoire

#nom d'utilisateur dynamique
nom_utilisateur = os.getlogin()

#définition du dossier téléchargement
fileDir = f"C:\\Users\\{nom_utilisateur}\\Downloads"

#définition des extensions des divers fichiers
executableExt = (".exe", ".msi")
imgExt = (".jpg", ".jpeg", ".png", ".gif", ".bmp")
docExt = (".pdf", ".txt")
wordExt = (".doc", ".docx")
excelExt = (".xls", ".xlsx", ".xlsm", ".csv")
vidExt = (".mp4", ".avi", ".mkv", ".mov")
musicExt = (".mp3", ".wav", ".aac", ".flac")
compressExt = (".zip", ".rar")

#parcourir le dossier à la recherche des extensions
#executable

for file in os.listdir(fileDir):
    if file.endswith(executableExt):    #parse toutes les extensions
        exeDir = os.path.join(fileDir, "exe")   #génération du chemin du dossier
        os.makedirs(exeDir, exist_ok=True)  #création du dossier de l'extension s'il n'existe pas
        source_path = os.path.join(fileDir, file)  # Chemin complet source
        destination_path = os.path.join(exeDir, file)  # Chemin complet destination
        shutil.move(source_path, destination_path)  #deplace tous les fichiers avec les extensions
        
    if file.endswith(imgExt):    #parse toutes les extensions
        exeDir = os.path.join(fileDir, "image")   #génération du chemin du dossier
        os.makedirs(exeDir, exist_ok=True)  #création du dossier de l'extension s'il n'existe pas
        source_path = os.path.join(fileDir, file)  # Chemin complet source
        destination_path = os.path.join(exeDir, file)  # Chemin complet destination
        shutil.move(source_path, destination_path)  #deplace tous les fichiers avec les extensions
        
    if file.endswith(docExt):    #parse toutes les extensions
        exeDir = os.path.join(fileDir, "docs")   #génération du chemin du dossier
        os.makedirs(exeDir, exist_ok=True)  #création du dossier de l'extension s'il n'existe pas
        source_path = os.path.join(fileDir, file)  # Chemin complet source
        destination_path = os.path.join(exeDir, file)  # Chemin complet destination
        shutil.move(source_path, destination_path)  #deplace tous les fichiers avec les extensions
        
    if file.endswith(wordExt):    #parse toutes les extensions
        exeDir = os.path.join(fileDir, "word")   #génération du chemin du dossier
        os.makedirs(exeDir, exist_ok=True)  #création du dossier de l'extension s'il n'existe pas
        source_path = os.path.join(fileDir, file)  # Chemin complet source
        destination_path = os.path.join(exeDir, file)  # Chemin complet destination
        shutil.move(source_path, destination_path)  #deplace tous les fichiers avec les extensions
        
    if file.endswith(excelExt):    #parse toutes les extensions
        exeDir = os.path.join(fileDir, "excel")   #génération du chemin du dossier
        os.makedirs(exeDir, exist_ok=True)  #création du dossier de l'extension s'il n'existe pas
        source_path = os.path.join(fileDir, file)  # Chemin complet source
        destination_path = os.path.join(exeDir, file)  # Chemin complet destination
        shutil.move(source_path, destination_path)  #deplace tous les fichiers avec les extensions
        
    if file.endswith(vidExt):    #parse toutes les extensions
        exeDir = os.path.join(fileDir, "video")   #génération du chemin du dossier
        os.makedirs(exeDir, exist_ok=True)  #création du dossier de l'extension s'il n'existe pas
        source_path = os.path.join(fileDir, file)  # Chemin complet source
        destination_path = os.path.join(exeDir, file)  # Chemin complet destination
        shutil.move(source_path, destination_path)  #deplace tous les fichiers avec les extensions
        
    if file.endswith(musicExt):    #parse toutes les extensions
        exeDir = os.path.join(fileDir, "music")   #génération du chemin du dossier
        os.makedirs(exeDir, exist_ok=True)  #création du dossier de l'extension s'il n'existe pas
        source_path = os.path.join(fileDir, file)  # Chemin complet source
        destination_path = os.path.join(exeDir, file)  # Chemin complet destination
        shutil.move(source_path, destination_path)  #deplace tous les fichiers avec les extensions
        
    if file.endswith(compressExt):    #parse toutes les extensions
        exeDir = os.path.join(fileDir, "compress")   #génération du chemin du dossier
        os.makedirs(exeDir, exist_ok=True)  #création du dossier de l'extension s'il n'existe pas
        source_path = os.path.join(fileDir, file)  # Chemin complet source
        destination_path = os.path.join(exeDir, file)  # Chemin complet destination
        shutil.move(source_path, destination_path)  #deplace tous les fichiers avec les extensions
        