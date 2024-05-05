def count_logs_by_level(logs: list) -> dict:
    counts_by_level = {}

    for log in map(lambda log: log["log_level"], logs):
        if log in counts_by_level:
            counts_by_level[log] += 1
        else:
            counts_by_level[log] = 1

    return counts_by_level

def filter_logs_by_level(logs: list, level: str) -> list:                
    filtered_logs = filter(lambda log: log["log_level"] == level.upper(), logs)     

    return list(filtered_logs)
    