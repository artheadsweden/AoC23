
from get_puzzle import get_data


def process_line(line):
    number_words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    p1_digits = []
    p2_digits = []

    for i, c in enumerate(line):
        if c.isdigit():
            p1_digits.append(c)
            p2_digits.append(c)
        for d, val in enumerate(number_words):
            if line[i:].startswith(val):
                p2_digits.append(str(d + 1))
    
    return p1_digits, p2_digits

def calculate_sums(file_path):
    with open(file_path, 'r') as file:
        data = file.read().strip()

    p1_sum = 0
    p2_sum = 0

    for line in data.split('\n'):
        p1_digits, p2_digits = process_line(line)
        p1_sum += int(p1_digits[0] + p1_digits[-1])
        p2_sum += int(p2_digits[0] + p2_digits[-1])
    
    return p1_sum, p2_sum

get_data(1, 2023)
p1_sum, p2_sum = calculate_sums('./data/input_1.txt')
print(f'Part 1: {p1_sum}')
print(f'Part 2: {p2_sum}')