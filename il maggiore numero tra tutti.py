from termina import termina
big = 0
print("inserisci quanti numeri vuoi per sapere quale di questi è il più grande")
while True:
	num = float(input("-> "))
	if num == 0:
		break
	elif num > big:
		big = num
print(f"il numero più grande che è uscito è {big}")
termina()