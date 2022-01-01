print("inserisci il $ per terminare")
while True:
	num = input("inserisci un numero base decimale -> ")
	if num != '$':
		try:
			# insert here a function for convertion
			num = int(num)
			binario = ""
			while num > 0:
				if num % 2 == 0:
					binario += "0"
				else:
					binario += "1"
				num = int(num / 2)
			print(binario[::-1])
		except:
			print("devi inserire un valore intero oppure il $")
			pass
	else:
		print("fine")
		break