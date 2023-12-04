import os, re

def get_input(name="input"):
    current_directory = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(current_directory, name)
    with open(input_file_path, 'r') as file:
        input_file = file.read().strip().split('\n')
    
    return input_file

def main():
    input_file = get_input()
    
    total = 0
    
    for line in input_file:
        start, end = line.split(' | ')
        winning_numbers = set(re.findall(r'\d+', start.split(':')[1]))
        acquired_numbers = re.findall(r'\d+', end)
        
        base = 0
        for number in acquired_numbers:
            if number in winning_numbers:
                base = max(base * 2, 1)
        total += base
    print(total)
        



if __name__ == "__main__":
    main()
