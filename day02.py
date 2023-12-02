from get_puzzle import get_data
from collections import defaultdict


def calculate_parts(file_path):
    with open(file_path, 'r') as file:
        data = file.read().strip()
    
    part1_sum = 0
    part2_sum = 0

    # Define the maximum number of cubes for each color
    max_cubes = {'red': 12, 'green': 13, 'blue': 14}

    # Process each line (game) in the input data
    for line in data.split('\n'):
        game_valid = True
        game_id, events = line.split(':')
        
        # Initialize a dictionary to keep track of the maximum number of cubes shown per color
        max_shown_cubes = defaultdict(int)

        # Process each event (subset of cubes shown) in the game
        for event in events.split(';'):
            for cube_info in event.split(','):
                count, color = cube_info.split()
                count = int(count)

                # Update the maximum number of cubes shown for each color
                max_shown_cubes[color] = max(max_shown_cubes[color], count)

                # Check if the number of cubes shown exceeds the limit
                if count > max_cubes[color]:
                    game_valid = False

        # Calculate the score (power) of the minimum set of cubes
        score = 1
        for count in max_shown_cubes.values():
            score *= count
        part2_sum += score

        # If the game is valid, add its ID to part1_sum
        if game_valid:
            part1_sum += int(game_id.split()[-1])

    return part1_sum, part2_sum


get_data(2, 2023)

p1_result, p2_result = calculate_parts('./data/input_2.txt')
print(f'Part 1: {p1_result}')
print(f'Part 2: {p2_result}')