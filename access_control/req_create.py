from rbac import USERS

REQUESTS = []


def create_request(user, resource, action, until, reason, received_at):
    """요청서를 만들어 REQUESTS에 넣고 (True, 요청서)를 리턴한다."""

    # 1. 등록되지 않은 사용자 확인
    if user not in USERS:
        return False, "등록되지 않은 사용자"

    # 2. 이유가 비어 있는지 확인
    if reason == "":
        return False, "이유가 없음"

    # 3. 만료 시각 확인
    if until <= received_at:
        return False, "만료 시각이 이미 지났음"

    # 4. 요청서 만들기
    request = {
        "id": len(REQUESTS) + 1,
        "user": user,
        "resource": resource,
        "action": action,
        "permission": f"{resource}:{action}",
        "until": until,
        "reason": reason,
        "requested_at": received_at,
        "status": "reviewing"
    }

    # 5. 요청서 목록에 추가
    REQUESTS.append(request)

    # 6. 접수 성공 반환
    return True, request