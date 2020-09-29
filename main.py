import random

cle = ""

class Init():
	def __init__(self):
		self.lang = {}

		self.lang["a"] = 0
		self.lang["b"] = 0
		self.lang["c"] = 0
		self.lang["d"] = 0
		self.lang["e"] = 0
		self.lang["f"] = 0
		self.lang["g"] = 0
		self.lang["h"] = 0
		self.lang["j"] = 0
		self.lang["k"] = 0
		self.lang["l"] = 0
		self.lang["m"] = 0
		self.lang["n"] = 0
		self.lang["o"] = 0
		self.lang["p"] = 0
		self.lang["q"] = 0
		self.lang["r"] = 0
		self.lang["s"] = 0
		self.lang["t"] = 0
		self.lang["u"] = 0
		self.lang["v"] = 0
		self.lang["w"] = 0
		self.lang["x"] = 0
		self.lang["y"] = 0
		self.lang["z"] = 0

		for lettres in self.lang:

			self.lang[lettres] = random.randint(1000, 9999)

def crypt(rp, cle, init):

	cle = str(cle)
	
	for l in rp:
		cle = cle + str(init.lang[l])

	return cle

a = Init()
b = 0

verif = True

while verif:

	rp = input("Mot a crypter : ")
	if rp == "":
		print()
	else:
		verif = False


key = crypt(rp, cle, a)

print("Cryptage terminé ! : " + key)