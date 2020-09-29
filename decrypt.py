import time
from server import StartServer

def find_key(v, dico):

	for k, val in dico.items():
			
		if v == val:
			return k

	return "Invalide | "

class Decrypt():
	def __init__(self):
		resultat = ""
		b = 0
		dico = {}
		a = input("entrez le nom exact du fichier a decrypter (extension incluse)")
		with open(a, "r") as fic:
			print("Extraction de la clé de decryptage ...")
			time.sleep(2)
			print()
			cle = fic.readline()
			print("Extraction des dictionnaires encryptés ...")
			time.sleep(2)
			while b != 84:
				b += 1
				za = fic.readline()
				az = fic.readline()
				za = za.replace("\n", "")
				az = az.replace("\n", "")
				dico[za] = az
				w = fic.readline()
			print()
			print("Décryptage en cours ...")
			h = 0
			content = []
			zzz = ""
			for l in cle:
				zzz = zzz + l
				h += 1
				if h == 4:
					content.append(zzz)
					h = 0
					zzz = ""
			for s in content:
				resultat = resultat + find_key(s, dico)
			self.resultat = resultat
			time.sleep(2)
			print()
			print("Fichier decrypté !")
		self.key = cle
		StartServer(self.key, self.resultat)

Decrypt()