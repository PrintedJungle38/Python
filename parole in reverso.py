from termina import termina
while True:
	stringa = input("inserisci la parola da invertire -->")[::-1]
	if stringa == "stop":
		break
	print(stringa)
termina()