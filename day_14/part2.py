import os

def get_input(name="input.txt"):
    current_directory = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(current_directory, name)
    with open(input_file_path, 'r') as file:
        input_file = file.read().strip().split('\n')
    
    return input_file



def transpose(grid):
    return list(map(list, zip(*grid)))

def rotate_left(grid):
    return list(reversed(list(map(list, zip(*grid)))))

def rotate_right(grid):
    return [list(reversed(x)) for x in zip(*grid)]

def tilt_grid_left(grid):
    for line in grid:
        left_pos = -1
        for i, char in enumerate(line):
            if char == '#':
                left_pos = i
            elif char == 'O':
                line[i] = '.'
                line[left_pos + 1] = 'O'
                left_pos += 1

def cycle(grid):
    for _ in range(4):
        tilt_grid_left(grid)
        grid = rotate_right(grid)
    return grid, tuple(tuple(row) for row in grid)

def get_load(grid):
    load = 0
    for line in grid:
        for i, char in enumerate(line):
            if char == 'O':
                load += len(line) - i 
    return load

def main():
    input_file = get_input()
    grid = [list(row) for row in input_file]
    
    prev_states = dict()
    num_to_state = dict()
    
    grid = rotate_left(grid)
    i = 0
    tup_grid = tuple(tuple(row) for row in grid)
    prev_states[tup_grid] = i
    num_to_state[i] = list(list(row) for row in tup_grid)
    
    while True:
        grid, tup_grid = cycle(grid)
        if tup_grid in prev_states:
            break
        i += 1
        prev_states[tup_grid] = i
        num_to_state[i] = list(list(row) for row in tup_grid)
    
    final_grid = num_to_state[(1000000000 - prev_states[tup_grid]) % (i + 1 - prev_states[tup_grid]) + prev_states[tup_grid]]
    total = get_load(final_grid)
    
    print(total)
    


if __name__ == "__main__":
    main()
