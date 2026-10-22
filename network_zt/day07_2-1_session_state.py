SESSION_LIMITS = {"settlement": 30, "admin": 5}

SESSIONS = [
    {"id": 1, "user": "junho", "resource": "settlement", "age": 10},
    {"id": 2, "user": "junho", "resource": "settlement", "age": 26},
    {"id": 3, "user": "junho", "resource": "settlement", "age": 41},
    {"id": 4, "user": "gaeun", "resource": "admin", "age": 3},
    {"id": 5, "user": "gaeun", "resource": "admin", "age": 4},
    {"id": 6, "user": "gaeun", "resource": "admin", "age": 12},
    {"id": 7, "user": "seoyeon", "resource": "settlement", "age": 30},
]

def session_state(session):
    """세션이 '유지' '재인증' '종료' 중 어느 상태인지 리턴한다"""
    limit = SESSION_LIMITS[session["resource"]]

    if session["age"] > limit:
        return "종료"

    if session["age"] >= limit * 0.8:
        return "재인증"

    return "유지"

for session in SESSIONS:
    print(session["id"], session["user"], session["resource"], session["age"], "->", session_state(session))