import os

def get_input(name="input"):
    current_directory = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(current_directory, name)
    with open(input_file_path, 'r') as file:
        input_file = file.read().strip().split('\n')
    
    return input_file

def expand_grid(grid):
    row_blank = [True] * len(grid)
    col_blank = [True] * len(grid[0])
    
    for j, line in enumerate(grid):
        for i, char in enumerate(line):
            if char != '.':
                row_blank[j] = False
                col_blank[i] = False
                
    for i in range(len(row_blank)):
        j = len(row_blank) - i - 1
        if not row_blank[j]:
            continue
        grid.insert(j, ['.'] * len(grid[0]))
        
    for i in range(len(col_blank)):
        j = len(col_blank) - i - 1
        if not col_blank[j]:
            continue
        for row in grid:
            row.insert(j, '.')

def main():
    input_file = get_input()
    input_file = [list(row) for row in input_file]
    expand_grid(input_file)
    
    galaxy_list = []
    for j, row in enumerate(input_file):
        for i, char in enumerate(row):
            if char == '#':
                galaxy_list.append((i, j))
    
    total = 0
    for i in range(len(galaxy_list)):
        for j in range(i + 1, len(galaxy_list)):
            galaxy = galaxy_list[i]
            compare = galaxy_list[j]
            total += abs(galaxy[0] - compare[0]) + abs(galaxy[1] - compare[1])
            
    print(total)
            
            



if __name__ == "__main__":
    main()
