ACCOUNTS = {
    "seoyeon": {"employed": True, "device": "NB-0417", "role": "sales"},
    "junho": {"employed": True, "device": "NB-0522", "role": "finance"},
    "gaeun": {"employed": True, "device": "NB-0188", "role": "account_admin"},
    "dami": {"employed": False, "device": "NB-0333", "role": "sales"},
}


def decide_settlement(req):
    account = ACCOUNTS.get(req["user"])

    if account is None or not account["employed"]:
        return "거부", ["재직 중인 계정이 아님"]

    if req["device"] != account["device"]:
        return "거부", ["이 계정에 등록된 기기가 아님"]

    score = 0
    reasons = []

    if req["health"] != "ok":
        score = score + 40
        reasons.append("기기 보안 상태 이상 (+40)")

    if req["country"] != "KR":
        score = score + 30
        reasons.append("해외에서 접속 (+30)")

    if req["hour"] < 6:
        score = score + 20
        reasons.append("새벽 접속 (+20)")

    if req["mfa"] == False:
        score = score + 20
        reasons.append("MFA 안 함 (+20)")

    if req["count"] >= 20:
        score = score + 30
        reasons.append("대량 조회 (+30)")

    if score >= 50:
        return "거부", reasons

    if score >= 20:
        return "추가확인", reasons

    return "허용", reasons
if __name__ == "__main__":
    requests = [
        {
            "user": "gaeun",
            "device": "NB-0188",
            "health": "ok",
            "country": "KR",
            "hour": 10,
            "mfa": True,
            "count": 5,
        },
        {
            "user": "seoyeon",
            "device": "NB-0417",
            "health": "ok",
            "country": "KR",
            "hour": 10,
            "mfa": True,
            "count": 5,
        },
    ]

    for req in requests:
        result, reasons = decide_settlement(req)
        print(req["user"], result, reasons)