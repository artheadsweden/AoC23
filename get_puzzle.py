from aocd.models import Puzzle
import set_env

def get_data(day: int, year: int) -> list[int]:
    puzzle = Puzzle(year=year, day=day)

    puzzle.view()
    with open(f'./data/input_{day}.txt', 'w') as f:
        f.write(puzzle.input_data)
