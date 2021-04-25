from ..Direct import funcDeuxPoints



def funcSubD():
	print("-- Ici fonction funcSubD !")
	print("Je suis dans Projet\\Directory\\subDirectory\\subD.py")
	print("J'ai été appelée dans Projet.py par l'instruction from Directory.subDirectory.subD import *")
	print("Je suis appelée dans Projet.py")
	print("funcSubD terminée. Aurevoir ! --\n")


"""
En passant, petit exemple d'utilisation de if __name__ == '__main__':
Pour vois la différence, intervertissez funcDeuxPoints() et pass
"""
if __name__ == '__main__':
	funcDeuxPoints()
else:
	pass

