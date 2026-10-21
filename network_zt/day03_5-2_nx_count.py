logs = [
    ("10.20.0.15", "www.naver.com", "NOERROR"),
    ("10.20.0.42", "kxq3vz9a.top", "NXDOMAIN"),
    ("10.20.0.42", "p0w8rk2mzq.xyz", "NXDOMAIN"),
    ("10.20.0.33", "nevar.com", "NXDOMAIN"),
    ("10.20.0.42", "zzx9q2lk.top", "NXDOMAIN"),
    ("10.20.0.42", "qwrtpzkx7v.com", "NOERROR")
]

nx = {}

for pc, name, rcode in logs:
    if rcode == "NXDOMAIN":
        nx[pc] = nx.get(pc, 0) + 1

print(nx)
