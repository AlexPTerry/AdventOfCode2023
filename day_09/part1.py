import os

def get_input(name="input"):
    current_directory = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(current_directory, name)
    with open(input_file_path, 'r') as file:
        input_file = file.read().strip().split('\n')
    
    return input_file

def get_next_value(sequence):
    if not any(sequence):
        return 0
    
    difference = [sequence[1:][i] - sequence[:-1][i] for i in range(len(sequence) - 1)]
    return sequence[-1] + get_next_value(difference)

def main():
    input_file = get_input()
    
    total = 0
    for line in input_file:
        total += get_next_value(list(map(int, line.split())))
    print(total)
        



if __name__ == "__main__":
    main()
