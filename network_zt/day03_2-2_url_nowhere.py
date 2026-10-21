import socket

url = "https://abc.nowhere-not-exist.com/login"
parts = url.split("/")
name = parts[2]

print(parts)
print(name, "→", socket.gethostbyname(name))