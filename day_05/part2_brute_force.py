import os

def get_input(name="input"):
    current_directory = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(current_directory, name)
    with open(input_file_path, 'r') as file:
        input_file = file.read().strip().split('\n\n')
    
    return input_file

def get_next_val(val, subpath):
    for conn in subpath:
        diff = val - conn[1]
        if (0 <= diff < conn[2]):
            return conn[0] + diff
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
        path.append(subpath)
        
    min_location = -1
    

    for single_seed_info in seed_info:
        n = single_seed_info[1]
        print(f'Num: {n}')
        i = 0
        for seed in range(single_seed_info[0], single_seed_info[0] + single_seed_info[1]):
            i += 1
            if i % 10000 == 0:
                print(f'Iteration: {i/n*100}%')
            current_val = seed
            for subpath in path:
                current_val = get_next_val(current_val, subpath)
                
            if min_location == -1:
                min_location = current_val
            else:
                min_location = min(min_location, current_val)
        
        
    print(min_location)
        



if __name__ == "__main__":
    main()
