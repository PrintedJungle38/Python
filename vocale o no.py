vocali = "aeiouAEIOU"
consonanti = "bcdfghjklmnpqrstvwxyzBCDFGHJKMNPQRSTVWXYZ"
while True:
	carattere = input("inserisci una lettera --> ")
	if carattere in vocali:
		print(f"Il carattere {carattere} è una vocale")
	elif carattere in consonanti:
		print(f"Il carattere {carattere} è una consonante")
	else:
		print(f"Il carattere {carattere} è un carattere alfanumerico")

	loop = input("vuoi ripetere? S/N --> ")
	if loop == "S" or loop == "s":
		continue
	else:
		break