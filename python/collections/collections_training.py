from collections import Counter, defaultdict

def analyze_logs(logs):
    level_counts = Counter()
    latest_timestamps = {}
    error_msgs = Counter()

    for log_str in logs:
        words = log_str.split()
        level = words[2]
        timestamp = " ".join(words[:2])
        log_msg = " ".join(words[3:])
        level_counts[level] += 1
        latest_timestamps[level] = max(latest_timestamps.get(level, ""), timestamp)
        if level == "ERROR":
            error_msgs[log_msg] += 1
    
    return {"level_counts": dict(level_counts), 
            "top_errors": error_msgs.most_common(3),
            "latest_timestamps": latest_timestamps}

if __name__ == "__main__":
    logs = [
    "2026-01-07 10:23:45 ERROR database connection timeout",
    "2026-01-07 10:24:01 INFO user login successful",
    "2026-01-07 10:24:15 ERROR file not found",
    "2026-01-07 10:25:30 ERROR database connection timeout",
    "2026-01-07 10:26:00 WARNING low disk space"
    ]

    ret_dict = analyze_logs(logs)
    print(ret_dict)