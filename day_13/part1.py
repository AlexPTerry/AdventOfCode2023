import os

def get_input(name="input.txt"):
    current_directory = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(current_directory, name)
    with open(input_file_path, 'r') as file:
        input_file = file.read().strip().split('\n\n')
    
    return input_file

def get_tranpose(grid):
    transpose = [['_' for _ in range(len(grid))] for _ in range(len(grid[0]))]
    for j, line in enumerate(grid):
        for i, char in enumerate(line):
            transpose[i][j] = char
    return transpose

def compare_lists(top, bottom):
    for i in range(min(len(top), len(bottom))):
        if bottom[i] != top[-i-1]:
            return -1
    return len(top)

def get_horizontal_score(grid):
    for i in range(1, len(grid)):
        score = compare_lists(grid[:i], grid[i:])
        if score > -1:
            return score
    return -1

def get_score(grid):
    transpose = get_tranpose(grid)
    horizontal_score = get_horizontal_score(grid)
    if horizontal_score > -1:
        return 100*horizontal_score
    
    vertical_score = get_horizontal_score(transpose)
    if vertical_score > -1:
        return vertical_score
    
    return 0

def main():
    input_file = get_input()
    total = 0
    for chunk in input_file:
        total += get_score(chunk.split('\n'))
            
    print(total)
            
            



if __name__ == "__main__":
    main()
