ttl = 300
saved_at = 0

for now in [30, 100, 299, 300]:
    if now < saved_at + ttl:
        print(now, "초: 캐시의 답을 쓴다")
    else:
        print(now, "초: DNS 서버에 새로 묻는다")
