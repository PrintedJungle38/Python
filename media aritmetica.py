from termina import termina
print("inserisci tutti i numeri da \'mediare\' fino a quando dici stop")
numero = 0
media = []
while numero != "stop":
    numero = input("-> ")
    media.append(numero)
    if "stop" in media:
        media.pop()
somma = 0
dividendo = 0
for number in media:
    somma += float(number)
    dividendo += 1
media_fatta = somma/dividendo
print(media_fatta)
termina()