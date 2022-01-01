from termina import termina
contenuto = "ma ciao, ci sei riuscito XD"
file1 = open("esempio1.txt","w")
file1.write(contenuto)
file1.close()
nuova_stringa = "\nPython è una bomba"
file1 = open("esempio1.txt","a")
file1.write(nuova_stringa)
file1.close()
termina()