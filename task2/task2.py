import re
from typing import Callable

def generator_numbers(text:str):
    pattern = r'\d+(\.\d+)?'
    matches = re.finditer(pattern, text)

    for match in matches:
        yield float(match.group())

def sum_profit(text:str, gen:Callable):
    sum = 0.00
    for number in gen(text):
        sum += number

    return sum


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
# Загальний дохід: 1351.46
