from . Direct2 import funcpoint1


def funcDirect():
	print("-- Ici funcDirect !")
	print("Je suis dans Projet\\Directory\\Direct.py")
	print("J'ai été appelée dans Projet.py par l'instruction from Directory.Direct import *")
	print("Je suis appelée dans Projet.py")
	print("funcDirect terminée. Aurevoir ! --\n")


def funcDeuxPoints():
	print("-- Ici function funcDeuxPoints !")
	print("Je suis dans Projet\\Directory\\Direct.py")
	print("MAIS j'ai été importée depuis Directory\\subDirectory\\subD.py ")
	print("par l'instruction from ..Direct import funcDeuxPoints")
	print("Je suis appelée dans Projet.py")
	print("funcDeuxPoints terminée. Aurevoir ! --\n")

