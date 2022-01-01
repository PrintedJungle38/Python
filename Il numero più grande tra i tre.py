from termina import termina
a = input("inserisci il valore di a: ")
b = input("inserisci il valore di b: ")
c = input("inserisci il valore di c: ")
if a == b and b == c:
	print("sono tutti numeri uguali")
elif a > b:
	if a > c:
		print("il numero più grande è: "+str(a))
	else:
		print("il numero più grande è: "+str(c))
else:
	if b > c:
		print("il numero più grande è: "+str(b))
	else:
		print("il numero più grande è: "+str(c))
termina()