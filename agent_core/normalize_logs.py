import json

logs = []
skipped_count = 0

with open("sample_logs_raw.csv", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line:
            skipped_count += 1
            continue

        parts = line.split(",")

        if len(parts) < 3:
            skipped_count += 1
            continue

        try:
            time_val = parts[0]
            user_val = parts[1]
            event_val = parts[2].upper()
            hour_val = int(time_val.split(":")[0])

            if len(parts) >= 4 and parts[3]:
                ip_val = parts[3]
            else:
                ip_val = "unknown"

            log_dict = {
                "time": time_val,
                "user": user_val,
                "event": event_val,
                "ip": ip_val,
                "hour": hour_val
            }
            logs.append(log_dict)

        except ValueError:
            skipped_count += 1

with open("normalized_logs.json", "w", encoding="utf-8") as f:
    json.dump(logs, f, ensure_ascii=False, indent=2)

print(f"정규화 {len(logs)}건")
