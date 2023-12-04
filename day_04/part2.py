import os, re

def get_input(name="input"):
    current_directory = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(current_directory, name)
    with open(input_file_path, 'r') as file:
        input_file = file.read().strip().split('\n')
    
    return input_file

def calculate_wins(line):
    start, end = line.split(' | ')
    winning_numbers = set(re.findall(r'\d+', start.split(':')[1]))
    acquired_numbers = set(re.findall(r'\d+', end))
    return len(winning_numbers & acquired_numbers)

def main():
    input_file = get_input()
    
    total = 0
    mult_queue = [1]*len(input_file)
    
    for i, line in enumerate(input_file):
        total += mult_queue[i]
        n_wins = calculate_wins(line)
        for j in range(n_wins):
            mult_queue[i+j+1] += mult_queue[i]
    
    print(total)
        



if __name__ == "__main__":
    main()
