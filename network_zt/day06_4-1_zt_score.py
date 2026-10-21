
STAFF = [
    {"name": "u01", "mfa": True,  "device_ok": True,  "extra_perms": 0},
    {"name": "u02", "mfa": True,  "device_ok": True,  "extra_perms": 0},
    {"name": "u03", "mfa": True,  "device_ok": True,  "extra_perms": 0},
    {"name": "u04", "mfa": True,  "device_ok": False, "extra_perms": 0},
    {"name": "u05", "mfa": True,  "device_ok": False, "extra_perms": 2},
    {"name": "u06", "mfa": True,  "device_ok": False, "extra_perms": 0},
    {"name": "u07", "mfa": False, "device_ok": False, "extra_perms": 0},
    {"name": "u08", "mfa": False, "device_ok": False, "extra_perms": 0},
    {"name": "u09", "mfa": False, "device_ok": False, "extra_perms": 1},
    {"name": "u10", "mfa": False, "device_ok": False, "extra_perms": 0},
    {"name": "u11", "mfa": False, "device_ok": False, "extra_perms": 0},
    {"name": "u12", "mfa": False, "device_ok": False, "extra_perms": 3},
]

SEGMENTED = False
RISK_AUTH = False

mfa_count = 0
device_count = 0
least_count = 0

for person in STAFF:
    if person["mfa"] == True:
        mfa_count = mfa_count + 1
    if person["device_ok"] == True:
        device_count = device_count + 1
    if person["extra_perms"] == 0:
        least_count = least_count + 1

# 수정한 계산식 3줄
mfa_score = mfa_count / len(STAFF) * 20
device_score = device_count / len(STAFF) * 20
least_score = least_count / len(STAFF) * 20

seg_score = 0
if SEGMENTED:
    seg_score = 20

risk_score = 0
if RISK_AUTH:
    risk_score = 20

# 수정한 총점 계산식
total = mfa_score + device_score + least_score + seg_score + risk_score

print("MFA", mfa_score, "/ 기기", device_score, "/ 최소권한", least_score, "/ 세그멘테이션", seg_score, "/ 위험기반인증", risk_score)
print("총점", total, "/ 100")
