import subprocess
from termina import termina

data = subprocess.check_output('netsh wlan show profile').decode('utf-8', errors="backslashreplace").split('\n')
wifis = [
	line.split(':')[1][1:-1]
	for line in data if "Tutti i profili utente" in line
]
testo = ""
password = open("WIFI_password.txt", "w")
password.write(f"{testo:<14}WIFI{testo:<14}| PASSWORD\n")

print(f"{testo:<14}WIFI{testo:<14}| PASSWORD")
for wifi in wifis:
	try:
		results = subprocess.check_output(f'netsh wlan show profiles name = "{wifi}" key=clear')
		results = results.decode('utf-8', errors="backslashreplace").split('\n')
		result = [
			password.split(':')[1][1:-1]
			for password in results if "Contenuto chiave" in password
		]
		print(f"{wifi:<32}: {result[0]}")
		password.write(f"{wifi:<32}: {result[0]}\n")
	except IndexError:
		print(f"{wifi:<32}: aperta")
		password.write(f"{wifi:<32}: aperta\n")

password.close()
termina()