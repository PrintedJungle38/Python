import random
nome_giocatore = input("benvenuto a: INDOVINA IL NUMERO\nCome ti chiami?\n")
print("buona fortuna " + nome_giocatore)
while True:
	numero_segreto = random.randint(1,20)
	print("indovina un numero da 1 a 20")
	global tentativi
	tentativi = 0
	while True:
		try:
			numero_inserito = int(input())
			tentativi += 1
			if (numero_inserito == numero_segreto):
				if tentativi == 1:
					print(nome_giocatore + " hai indovinato, il numero era proprio "+str(numero_segreto)+", ci sei riuscito al primo tentativo")
					break
				else:
					print(nome_giocatore + " hai indovinato, il numero era proprio "+str(numero_segreto)+", ci sei riuscito con "+str(tentativi)+" tentativi")
					break
			if(numero_inserito > numero_segreto):
				print("prova un po' di meno")
				pass
			if(numero_inserito < numero_segreto):
				print("prova un po' di più")
				pass
		except ValueError:
			print("inserisci un valore numerico intero")
	loop = input("vuoi continuare il gioco? S/N ")
	if loop == "S" or loop == "s":
		print("bene, prendo un altro numero a caso")
		continue
	else:
		print("ok, fine del gioco")
		break