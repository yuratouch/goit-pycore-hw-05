import sys
from pathlib import Path
from file_handler import load_logs
from log_handler import count_logs_by_level
from output_handler import display_log_counts, display_log_details

def main():
    logs = []
    load_logs(Path(sys.argv[1]),logs)
    logs_by_level = count_logs_by_level(logs)

    try:
        level = sys.argv[2]
        
        if level.upper() in logs_by_level:
            display_log_details(logs, level)
        else:
            print(f"'{level}' logging level not found")

    except IndexError:
        if len(logs) != 0:
            print(display_log_counts(logs_by_level))

        return None

if __name__ == '__main__':
    main()
