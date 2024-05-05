def parse_log_line(line: str) -> dict:
    log_details = line.split(" ", 3)
    date_time = log_details[0] + ' ' + log_details[1]
    log_level = log_details[2]
    log_message = log_details[3].strip()

    parsed_log = {
        "date_time": date_time,
        "log_level": log_level,
        "log_message": log_message
    }

    return parsed_log

def load_logs(file_path: str, logs:list) -> list:
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            loaded_logs = file.readlines()
            for log in loaded_logs:
                logs.append(parse_log_line(log))

        return logs
    
    except FileNotFoundError:
        print("No such file or directory. Please try again with the correct path to log file.")
        
        return None
    