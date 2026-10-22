
POLICY_LOG = [
    {"rid": 101, "time": "02:14", "user": "seoyeon", "decision": "거부", "score": 70},
    {"rid": 102, "time": "09:02", "user": "junho", "decision": "허용", "score": 0},
    {"rid": 103, "time": "09:10", "user": "seoyeon", "decision": "추가확인", "score": 30},
    {"rid": 104, "time": "10:05", "user": "junho", "decision": "허용", "score": 0},
    {"rid": 105, "time": "10:20", "user": "dami", "decision": "거부", "score": 0},
    {"rid": 106, "time": "11:02", "user": "gaeun", "decision": "허용", "score": 0},
    {"rid": 107, "time": "11:40", "user": "gaeun", "decision": "추가확인", "score": 30},
    {"rid": 108, "time": "13:15", "user": "junho", "decision": "추가확인", "score": 40},
    {"rid": 109, "time": "14:03", "user": "junho", "decision": "허용", "score": 0},
    {"rid": 110, "time": "15:22", "user": "junho", "decision": "거부", "score": 50},
    {"rid": 111, "time": "16:45", "user": "gaeun", "decision": "거부", "score": 50},
    {"rid": 112, "time": "17:30", "user": "junho", "decision": "허용", "score": 0},
]

ACCESS_LOG = [
    {"rid": 101, "time": "02:14", "user": "seoyeon", "status": 200},
    {"rid": 102, "time": "09:02", "user": "junho", "status": 200},
    {"rid": 103, "time": "09:10", "user": "seoyeon", "status": 401},
    {"rid": 104, "time": "10:05", "user": "junho", "status": 200},
    {"rid": 105, "time": "10:20", "user": "dami", "status": 403},
    {"rid": 106, "time": "11:02", "user": "gaeun", "status": 200},
    {"rid": 107, "time": "11:40", "user": "gaeun", "status": 401},
    {"rid": 201, "time": "12:34", "user": "seoyeon", "status": 200},
    {"rid": 108, "time": "13:15", "user": "junho", "status": 200},
    {"rid": 109, "time": "14:03", "user": "junho", "status": 200},
    {"rid": 110, "time": "15:22", "user": "junho", "status": 403},
    {"rid": 111, "time": "16:45", "user": "gaeun", "status": 403},
    {"rid": 112, "time": "17:30", "user": "junho", "status": 403},
]

EXPECTED = {"허용": 200, "추가확인": 401, "거부": 403}
STRENGTH = {200: 0, 401: 1, 403: 2}

access_status = {}
for a in ACCESS_LOG:
    access_status[a["rid"]] = a["status"]

counts = {}
policy_ids = []

for p in POLICY_LOG:
    policy_ids.append(p["rid"])
    status = access_status.get(p["rid"])
    expected = EXPECTED[p["decision"]]

    if status != expected:
        if STRENGTH[status] < STRENGTH[expected]:
            kind = "집행 누락"
        else:
            kind = "과집행"

        counts[kind] = counts.get(kind, 0) + 1
        print("[어긋남]", p["rid"], p["user"], p["decision"], status, kind)

for a in ACCESS_LOG:
    user = a["user"]

    if a["rid"] not in policy_ids:
        print("[우회]", a["rid"], user, a["status"])
        counts["우회"] = counts.get("우회", 0) + 1

print(counts)
