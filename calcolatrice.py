def inserisci():
	global a,b
	a = float(input('Inserisci il Primo Numero --> '))
	b = float(input('Inserisci il Secondo Numero --> '))
while True:
	print('''
Benvenuto al programma calcolatrice!
Creato da: Reattino Gabriele
Di seguito un elenco delle varie funzioni disponibili:
  -Per effettuare un'Addizione, seleziona +
  -Per effettuare una Sottrazione, seleziona -
  -Per effettuare una Moltiplicazione, seleziona *
  -Per effettuare una Divisone, seleziona /
  -Per effettuare un Calcolo Esponenziale, seleziona e
  -Per effettuare una radice con indice a scelta, seleziona r
''')

	scelta = input('Inserisci il numero corrispondente all\'operazione selezionata --->  ')
	if scelta == "+":
		print('\nHai scelto: Addizione\n')
		inserisci()
		print('Il risultato della Somma è: ' + str(a + b))

	elif scelta == "-":
		print('\nHai Scelto: Sottrazione\n')
		inserisci()
		print('Il risultato della Sottrazione è: ' + str(a - b))

	elif scelta == "*":
		print('\nHai scelto: Moltiplicazione\n')
		inserisci()
		print('Il risultato della Moltiplicazione è: ' + str(a * b))

	elif scelta == "/":
		print('\nHai scelto: Divisione\n')
		inserisci()
		print('Il risultato della Divisione è: ' + str(a / b))

	elif scelta == "e":
		print('\nHai scelto: Calcolo Esponenziale\n')
		a = float(input('Inserisci la Base --> '))
		b = float(input('Inserisci l\'esponente --> '))
		print('Il risultato del Calcolo Esponenziale è: ' + str(a ** b))

	elif scelta == "r":
		print('\nHai scelto: Radice Con Indice a Scelta\n')
		a = int(input('Inserisci l\' indice di radice --> '))
		b = float(input('Inserisci il radicando --> '))
		print('Il risultato della radice di ' + str(a) + ' è ' + str(b ** (1/a)))

	loop = input('\nDesideri continuare ad usare l\'applicazione? S/N ')
	if loop == "S" or loop == "s":
		print("Sto tornando al Menù principale!")
		continue
	else:
		print("Grazie e arrivederci!")
		break