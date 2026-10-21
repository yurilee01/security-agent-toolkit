import socket

url = "https://example.com/news/today"
parts = url.split("/")
name = parts[2]

print(parts)
print(name, "→", socket.gethostbyname(name))