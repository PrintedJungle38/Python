from termina import termina
lista = []
while True:
	num = input("inserisci il numero da vedere nella lista --> ")
	lista.append(num)
	if num == "basta":
		lista.remove("basta")
	if num == "stop":
		lista.remove("stop")	
	if num == "":
		lista.remove("")
	if num == "stop" or num == "basta":
		break
for numero in lista:
	print("@" * int(numero))
termina()