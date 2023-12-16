import os

def get_input(name="input.txt"):
    current_directory = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(current_directory, name)
    with open(input_file_path, 'r') as file:
        input_file = file.read().strip().split('\n')
    
    return input_file

direction_dict = {
    '|': {
        (-1, 0): [(0, 1), (0, -1)],
        (1, 0): [(0, 1), (0, -1)],
        (0, -1): [(0, -1)],
        (0, 1): [(0, 1)]
    },
    '-': {
        (0, -1): [(1, 0), (-1, 0)],
        (0, 1): [(1, 0), (-1, 0)],
        (-1, 0): [(-1, 0)],
        (1, 0): [(1, 0)]
    },
    '\\': {
        (0, -1): [(-1, 0)],
        (0, 1): [(1, 0)],
        (-1, 0): [(0, -1)],
        (1, 0): [(0, 1)]
    },
    '/': {
        (0, -1): [(1, 0)],
        (0, 1): [(-1, 0)],
        (-1, 0): [(0, 1)],
        (1, 0): [(0, -1)]
    }
}

def get_direction(tile_type, in_direction):
    return direction_dict[tile_type][in_direction]
    
def add_tuple(tup1, tup2):
    return tuple(i + j for i, j in zip(tup1, tup2))

def get_energised_spots(input_file, light_list):
    energised_spots = set()
    old_light_set = set()
    
    def get_type(pos):
        return input_file[pos[1]][pos[0]]
    
    def is_out_of_bounds(pos):
        return not (0 <= pos[0] < len(input_file[0]) and 0 <= pos[1] < len(input_file))
    
    while len(light_list) > 0:
        next_light_list = []
        for i, light in enumerate(light_list):
            if light in old_light_set or is_out_of_bounds(light[0]):
                continue
            old_light_set.add(light)
            
            tile_type = get_type(light[0])
            energised_spots.add(light[0])
            
            if tile_type != '.':
                direction_list = get_direction(tile_type, light[1])
            else:
                direction_list = [light[1]]
            
            for direction in direction_list:
                next_light_list.append((add_tuple(light[0], direction), direction))
            
        light_list = next_light_list
        
    return len(energised_spots)

def main():
    input_file = get_input()
    light_list = [((0,0), (1,0))]
    
    max_energised = 0
    for i in range(0, len(input_file[0])):
        light_list = [((i, 0), (0, 1))]
        max_energised = max(max_energised, get_energised_spots(input_file, light_list))
        
        light_list = [((i, len(input_file)-1), (0, -1))]
        max_energised = max(max_energised, get_energised_spots(input_file, light_list))
        
    for i in range(0, len(input_file)):
        light_list = [((0, i), (1, 0))]
        max_energised = max(max_energised, get_energised_spots(input_file, light_list))
        
        light_list = [((len(input_file[0])-1, i), (-1, 0))]
        max_energised = max(max_energised, get_energised_spots(input_file, light_list))
        
    print(max_energised)
    
    
    
            



if __name__ == "__main__":
    main()
