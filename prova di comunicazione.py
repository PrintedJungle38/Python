from termina import termina
print("PC: Ciao io sono una tua prova di comunicazione")
print("PC: Come ti chiami?")
nome = input("User: ")
print("PC: piacere di conoscerti, " + nome )
cibo_preferito = input("qual'è il tuo cibo preferito? ")
scelta_cibo = ["pizza", "pasta", "carne"]
if (cibo_preferito in scelta_cibo):
	print("mmmm, che buono")
	pass
else:
	print("mhh, purtroppo non conosco quello che mangi")
	pass
termina()