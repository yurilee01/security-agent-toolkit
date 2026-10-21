
inner = {"src": "10.8.0.21", "dst": "10.10.20.5", "data": "GET /portal"}
outer = {"src": "211.36.10.7", "dst": "203.0.113.1", "data": inner}

print("중간 라우터가 보는 도착지:", outer["dst"])
print("data 칸:", outer["data"])
print("안쪽 도착지:", outer["data"]["dst"])
