import os, re, math

def get_input(name="input"):
    current_directory = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(current_directory, name)
    with open(input_file_path, 'r') as file:
        input_file = file.read().strip().split('\n')
    
    return input_file

def main():
    input_file = get_input()
    
    time = int(''.join(re.findall(r'\d+', input_file[0])))
    distance = int(''.join(re.findall(r'\d+', input_file[1])))
    
    disc = math.sqrt(time**2 - 4*distance)
    lower = math.ceil((time - disc) * 0.5+0.00001)
    upper = math.floor((time + disc) * 0.5 - 0.00001)
    prod = upper - lower + 1
        
    print(prod)
        



if __name__ == "__main__":
    main()
