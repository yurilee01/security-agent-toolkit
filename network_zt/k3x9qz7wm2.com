
LOG = [
    ("news.dailybrief.com", "NOERROR", "정상"),
    ("cafe-mocha-roasters.xyz", "NOERROR", "정상"),
    ("intranet-old-wiki.top", "NXDOMAIN", "정상"),
    ("m4n8v2qz.com", "NXDOMAIN", "의심"),
    ("secure-pay-bank.net", "NOERROR", "의심"),
    ("zxqv1.tk", "NXDOMAIN", "의심")
]

for name, rcode, truth in LOG:
    parts = name.split(".")
    score = 0

    if len(parts[-2]) >= 10:
        score = score + 1

    if parts[-1] in ["top", "xyz", "tk"]:
        score = score + 1

    if rcode == "NXDOMAIN":
        score = score + 2

    print(name, score, score >= 3, "실제:", truth)
