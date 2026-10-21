
LOG = [
    ("www.naver.com", "NOERROR", "정상"),
    ("mail.google.com", "NOERROR", "정상"),
    ("update.microsoft.com", "NOERROR", "정상"),
    ("e6030.a.akamaiedge.net", "NOERROR", "정상"),
    ("cdn.jsdelivr.net", "NOERROR", "정상"),
    ("xn--3e0b707e.kr", "NOERROR", "정상"),
    ("kxq3vz9a.top", "NXDOMAIN", "의심"),
    ("p0w8rk2mzq.xyz", "NXDOMAIN", "의심"),
    ("qwrtpzkx7v.com", "NOERROR", "의심"),
    ("zzx9q2lk.top", "NXDOMAIN", "의심"),
    ("bnk-secure-login.xyz", "NOERROR", "의심"),
    ("www.example.com", "NOERROR", "정상")
]

THRESHOLD = 3

print("| 이름 | 응답 | 점수 | 판정 | 실제 |")
print("|---|---|---|---|---|")

for name, rcode, truth in LOG:
    parts = name.split(".")
    score = 0

    if len(parts[-2]) >= 10:
        score = score + 1

    if parts[-1] in ["top", "xyz", "tk"]:
        score = score + 1

    if rcode == "NXDOMAIN":
        score = score + 2

    if score >= THRESHOLD:
        judged = "의심"
    else:
        judged = "정상"

    print(f"| {name} | {rcode} | {score} | {judged} | {truth} |")
