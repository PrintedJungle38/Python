from termina import termina
print ("Ciao mondo, io sono bot WuW")

messaggio_simpatico = "nun sacciu chi diriti"
print (messaggio_simpatico)

cibo_preferito = "la pizza"
print("il mio cibo preferito è " + cibo_preferito)

print("\ncome ti chiami?")
nome = input()
print("\nCiao " + nome + " piacere di conoscerti")

if (nome == "gianpierpatrizio"):
	print("ma che nome è!??!!??")
	pass
else:
	print("bel nome")
	pass
lunghezza_nome = len(nome)
lunghezza_nome_stringa = str(lunghezza_nome)
print("il tuo nome ha " + lunghezza_nome_stringa + " lettere")

anno_di_nascita = input("\nIn che anno sei nato?")
anno_di_nascita_int = int(anno_di_nascita)
anno_corrente = input("\nIn che anno siamo?")
anno_corrente_int = int(anno_corrente)
eta = anno_corrente_int - anno_di_nascita_int
print(nome + " quindi hai " + str(eta) + " anni")

if (eta < 18):
	pass
	print("ottimo")
	anni_da_compiere = eta + 1
	print("\nl'anno prossimo avrai " + str(anni_da_compiere) + " anni")
else:
	print("diventi vecchio hahaha")
	eta_Silente = 150
	print("\ntra " + str(eta_Silente - eta) + " anni sarai vecchissimo come Albus Silente")
	pass

risposta = ""
while(risposta != "chi è?"):
	print("\ntoc toc")
	risposta = input()
print("nessuno, coglione")

animali = ["","1)Gatto", "2)Cane", "3)Pappagallo", "4)Criceto"]
print("\nQual'è il tuo animale preferito?")
for animale in animali:
	print(animale)
print("indicalo con un numero")
numero_animale = int(input())

if (numero_animale == 1 < numero_animale):
	print("hai sbagliato a scegliere")
	pass
else:
	animale_scelto = animali [numero_animale]
	print(animale_scelto + " ottima scelta")
	pass
termina()