import os

def get_input(name="input"):
    current_directory = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(current_directory, name)
    with open(input_file_path, 'r') as file:
        input_file = file.read().strip().split('\n')
    
    return input_file

def get_blank_row_col(grid):
    row_blank = [True] * len(grid)
    col_blank = [True] * len(grid[0])
    
    for j, line in enumerate(grid):
        for i, char in enumerate(line):
            if char != '.':
                row_blank[j] = False
                col_blank[i] = False
                
    return(list(i for i, val in enumerate(row_blank) if val),
           list(i for i, val in enumerate(col_blank) if val))


def get_distance(galaxy1, galaxy2, blank_rows, blank_cols, empty_mult):
    max_row = max(galaxy1[1], galaxy2[1])
    max_col = max(galaxy1[0], galaxy2[0])
    
    min_row = min(galaxy1[1], galaxy2[1])
    min_col = min(galaxy1[0], galaxy2[0])
    
    total = max_row - min_row + max_col - min_col
    for row in blank_rows:
        if min_row < row < max_row:
            total += empty_mult - 1
    for col in blank_cols:
        if min_col < col < max_col:
            total += empty_mult - 1
    return total
        

def main():
    input_file = get_input()
    input_file = [list(row) for row in input_file]
    blank_rows, blank_cols = get_blank_row_col(input_file)
    
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
            total += get_distance(galaxy, compare, blank_rows, blank_cols, 1000000)
            
    print(total)
            
            



if __name__ == "__main__":
    main()
