
RECORDS = [
    {"no": 1, "count": 12, "country": "KR", "kind": "정상"},
    {"no": 2, "count": 38, "country": "KR", "kind": "정상"},
    {"no": 3, "count": 41, "country": "KR", "kind": "정상"},
    {"no": 4, "count": 35, "country": "KR", "kind": "정상"},
    {"no": 5, "count": 44, "country": "KR", "kind": "정상"},
    {"no": 6, "count": 8, "country": "KR", "kind": "정상"},
    {"no": 7, "count": 39, "country": "KR", "kind": "정상"},
    {"no": 8, "count": 52, "country": "US", "kind": "위험"},
    {"no": 9, "count": 36, "country": "KR", "kind": "정상"},
    {"no": 10, "count": 6, "country": "KR", "kind": "정상"},
    {"no": 11, "count": 49, "country": "US", "kind": "위험"},
]

PLANS = [
    ("현재", 20, 30),
    ("A", 50, 30),
    ("B", 20, 10),
    ("C", 20, 0),
]


def score(count, country, threshold, points):
    total = 0

    # 해외 접속이면 30점 추가
    if country != "KR":
        total += 30

    # 조회 건수가 기준 이상이면 대량 조회 점수 추가
    if count >= threshold:
        total += points

    return total


def decide(total):
    # 점수에 따라 접근 결정
    if total >= 50:
        return "거부"
    elif total >= 20:
        return "추가확인"
    else:
        return "허용"


for name, threshold, points in PLANS:
    false_positive = 0
    false_negative = 0

    for r in RECORDS:
        d = decide(
            score(
                r["count"],
                r["country"],
                threshold,
                points
            )
        )

        # 정상 요청인데 허용이 아니면 오탐
        if r["kind"] == "정상" and d != "허용":
            false_positive += 1

        # 위험 요청인데 거부가 아니면 미탐
        if r["kind"] == "위험" and d != "거부":
            false_negative += 1

    # 조정안별 오탐과 미탐 출력
    print(name, "오탐", false_positive, "미탐", false_negative)
