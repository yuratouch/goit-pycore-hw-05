from prettytable import PrettyTable
from log_handler import count_logs_by_level, filter_logs_by_level

def display_log_counts(counts: dict):
    table = PrettyTable()
    table.field_names = ["Logging level", "Errors"]

    for key in counts:
        table.add_row([key, counts[key]])
    table.align["Logging level"] = "l" 
    return table

def display_log_details(logs:list, level:str):
    print(display_log_counts(count_logs_by_level(logs)))
    print(f"\nLog details for level {level.upper()}:")
    
    for log in filter_logs_by_level(logs, level):
        log_str = f"{log['date_time']} - {log['log_message']}"
        print(log_str)