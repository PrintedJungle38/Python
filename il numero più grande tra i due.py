from termina import termina
a = int(input("inserisci un valore di a: "))
b = int(input("inserisci un valore di b: "))
if a == b:
	print("I numeri sono identici")
else:
	print("Il numero più grande tra i due è ", end="")
	if a > b:
		print(str(a))
	else:
		print(str(b))
termina()