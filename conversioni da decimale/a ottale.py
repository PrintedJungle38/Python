print("inserisci il $ per terminare")
while True:
	num = input("inserisci un numero base decimale -> ")
	if num != '$':
		try:
			num = int(num)
			ottale = ''
			while num > 0:
				resto = num % 8
				num = int((num-resto)/8)
				ottale +=str(resto)
			print(ottale[::-1])
		except:
			print("devi inserire un valore intero oppure il $")
			pass
	else:
		print("fine")
		break