import os

def get_input(name="input"):
    current_directory = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(current_directory, name)
    with open(input_file_path, 'r') as file:
        input_file = file.read().strip().split('\n')
    
    return input_file

def get_surrounding_coords(coord):
    return set((coord[0]+i, coord[1]+j) for i in range(-1,2) for j in range(-1,2) if not (i==0 and j==0))

def main():
    input_file = get_input()
    
    valid_coords = set()
    getting_num = False
    current_num = ''
    current_num_coords = []
    
    numbers = []
    coords = []
    
    def check_end():
        nonlocal getting_num, numbers, coords, current_num, current_num_coords
        if getting_num:
            numbers.append(int(current_num))
            coords.append(current_num_coords)

            getting_num = False
            current_num = ''
            current_num_coords = []
    
    for row, line in enumerate(input_file):
        for col, c in enumerate(line):
            
            if c.isdigit():
                getting_num = True
                current_num += c
                current_num_coords.append((row, col))
            elif c == '.':
                check_end()
            else:
                valid_coords |= get_surrounding_coords((row, col))
                check_end()
        
        check_end()
                    
    total = 0           
    for i in range(len(numbers)):
        number = numbers[i]
        number_coords = coords[i]
        
        for coord in number_coords:
            if coord in valid_coords:
                total += number
                found = True
                break
    print(total)



if __name__ == "__main__":
    main()
