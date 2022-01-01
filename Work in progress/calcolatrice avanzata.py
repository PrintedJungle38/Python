print("Calcolatrice")
while True:
	a = float(input("inserisci un numero da operare --> "))
	operatore = input("scegli tra + - * / --> ")
	b = float(input("inserisci il secondo numero da operare --> "))
	if operatore == "+":
		print("Il risultato è: " + str(a + b))

	elif operatore == "-":
		print("Il risultato è: " + str(a - b))

	elif operatore == "*":
		print("Il risultato è: " + str(a * b))

	elif operatore == "/":
		print("Il risultato è: " +str(a / b)+ " oppure "+str(int(a / b))+" con resto di "+str(int(a % b)))

	ripeti = input("continua? ")
	if ripeti == "Si" or ripeti == "si" or ripeti == "S" or ripeti == "s":
		continue
	else:
		print("chiudo")
		break