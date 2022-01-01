import socket
from requests import get
from termina import termina

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
public_ip = get('https://api.ipify.org').text

print(f"Hostname: {hostname}")
print(f"local ip: {local_ip}")
print(f"public ip: {public_ip}")
termina()