import os, re, math

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
    current_locations = []
    for line in input_file[2:]:
        locations = re.findall(r'[A-Z]+', line)
        location_dict[locations[0]] = (locations[1], locations[2])
        if locations[0][-1] == 'A':
            current_locations.append(locations[0])
    
    loop_start = {i: -1 for i in range(len(current_locations))}
    loop_end = {i: -1 for i in range(len(current_locations))}
    z_found = {i: set() for i in range(len(current_locations))}
    locations_found = {i: set() for i in range(len(current_locations))}
    list_locations_found = {i: [] for i in range(len(current_locations))}
    
    moves = 0
    while any(loop_start[i] == -1 for i in range(len(current_locations))):
        direction = instructions[moves % len(instructions)]
        for i, current_location in enumerate(current_locations):
            if loop_start[i] != -1:
                continue
            
            new_location = location_dict[current_location][direction != 'L']
            current_locations[i] = new_location
            
            expanded_location = new_location + str(moves % len(instructions))
            if expanded_location in locations_found[i]:
                loop_start[i] = list_locations_found[i].index(expanded_location)
                loop_end[i] = moves
                continue
            
            locations_found[i].add(expanded_location)
            list_locations_found[i].append(expanded_location)
            if new_location[-1] == 'Z':
                z_found[i].add(moves)
        moves += 1
    
    print(loop_start)
    print(loop_end)
    print(z_found) # By a stroke of luck, the z's are all found right before the loop begins again!
    
    print(math.lcm(*[loop_end[i] - loop_start[i] for i in range(len(current_locations))]))
    # moves = 0
    # while not all(location[-1]=='Z' for location in current_locations):
    #     direction = instructions[moves % len(instructions)]
    #     for i, current_location in enumerate(current_locations):
    #         current_locations[i] = location_dict[current_location][direction != 'L']
    #     moves += 1
        
    # print(moves)
        



if __name__ == "__main__":
    main()
