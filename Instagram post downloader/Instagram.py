import subprocess
print("Benvenuto su Pystagram Post downloader")
post = input("inserisci il link del post che vuoi scaricare => ")
if "https://www.instagram.com/p/" in post:
	stringa = post.replace("https://www.instagram.com/p/", "")
	if "/" in stringa:
		post = stringa.replace("/", "")
subprocess.run(f"instaloader -- -{post}")