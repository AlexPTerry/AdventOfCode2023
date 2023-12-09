import os, re

def get_input(name="input"):
    current_directory = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(current_directory, name)
    with open(input_file_path, 'r') as file:
        input_file = file.read().strip().split('\n')
    
    return input_file

def main():
    input_file = get_input()
    
    instructions = input_file[0]
    
    location_dict = dict()
    for line in input_file[2:]:
        locations = re.findall(r'[A-Z]+', line)
        location_dict[locations[0]] = (locations[1], locations[2])
    
    current_location = 'AAA'
    moves = 0
    while current_location != 'ZZZ':
        direction = instructions[moves % len(instructions)]
        current_location = location_dict[current_location][direction != 'L'] # False == 0, True == 1
        moves += 1
        
    print(moves)
        



if __name__ == "__main__":
    main()
