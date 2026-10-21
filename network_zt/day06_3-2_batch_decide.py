
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


REQUESTS = [
    {"id": 1, "user": "junho", "device": "NB-0522", "health": "ok", "country": "KR", "hour": 14, "mfa": True, "count": 12},
    {"id": 2, "user": "seoyeon", "device": "NB-0417", "health": "ok", "country": "KR", "hour": 10, "mfa": True, "count": 25},
    {"id": 3, "user": "seoyeon", "device": "NB-7741", "health": "ok", "country": "KR", "hour": 2, "mfa": False, "count": 40},
    {"id": 4, "user": "dami", "device": "NB-0333", "health": "ok", "country": "KR", "hour": 11, "mfa": True, "count": 3},
    {"id": 5, "user": "junho", "device": "NB-0522", "health": "off", "country": "KR", "hour": 11, "mfa": True, "count": 5},
    {"id": 6, "user": "junho", "device": "NB-0522", "health": "ok", "country": "US", "hour": 3, "mfa": True, "count": 8},
    {"id": 7, "user": "seoyeon", "device": "NB-7741", "health": "ok", "country": "KR", "hour": 3, "mfa": False, "count": 35},
]


counts = {"허용": 0, "추가확인": 0, "거부": 0}
reason_counts = {}

for req in REQUESTS:
    decision, reasons = decide_settlement(req)

    counts[decision] = counts[decision] + 1

    if decision == "거부":
        print("[거부]", req["id"], req["user"], reasons)
        for reason in reasons:
            reason_counts[reason] = reason_counts.get(reason, 0) + 1

    if decision == "추가확인":
        print("[추가확인]", req["id"], req["user"], reasons)

print("허용", counts["허용"], "건 / 추가확인", counts["추가확인"], "건 / 거부", counts["거부"], "건")
print("거부 이유별 건수", reason_counts)
