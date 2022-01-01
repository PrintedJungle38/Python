from termina import termina
numero_inserito = int(input("inserisci un numero --> "))
print("il numero "+str(numero_inserito)+" è un numero ", end="")
if numero_inserito % 2 == 0:
	print("pari")
else:
	print("dispari")
termina()