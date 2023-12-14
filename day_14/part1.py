import os

def get_input(name="input.txt"):
    current_directory = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(current_directory, name)
    with open(input_file_path, 'r') as file:
        input_file = file.read().strip().split('\n')
    
    return input_file



def transpose_grid(grid):
    return list(map(list, zip(*grid)))

def main():
    input_file = get_input()
    input_file = [list(row) for row in input_file]
    
    transpose = transpose_grid(input_file)
    
    total = 0
    for line in transpose:
        left_pos = -1
        for i, char in enumerate(line):
            if char == '#':
                left_pos = i
            elif char == 'O':
                line[i] = '.'
                line[left_pos + 1] = 'O'
                left_pos += 1
                total += len(line) - left_pos
    
    print(total)
            
            



if __name__ == "__main__":
    main()
