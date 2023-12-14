import os

def get_input(name="input"):
    current_directory = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(current_directory, name)
    with open(input_file_path, 'r') as file:
        input_file = file.read().strip().split('\n\n')
    
    return input_file

def get_next_val(val, subpath):
    for conn in subpath:
        diff = val - conn[0]
        if (0 <= diff < conn[2]):
            return conn[1] + diff
    return val

def main():
    input_file = get_input()
    
    initial_nums = [int(n) for n in input_file[0].split(': ')[1].split()]
    seed_info = list(zip(initial_nums[0::2], initial_nums[1::2]))
    
    path = []
    for i, section in enumerate(input_file[1:]):
        lines = section.split('\n')
        subpath = []
        for line in lines[1:]:
            subpath.append(tuple(int(n) for n in line.split()))
        path = [subpath] + path
        
    min_location = -1
    
    max_val = max([location[0] + location[1] for location in path[0]])
    location = 0
    while True:
        if location % 100000 == 0:
            print(f"{location/max_val}%")
        current_val = location
        for subpath in path:
            current_val = get_next_val(current_val, subpath)
        
        for seed in seed_info:
            if seed[0] <= current_val < seed[0] + seed[1]:
                print(location)
                return
        location += 1
        
        
    # print(min_location)
        



if __name__ == "__main__":
    main()
