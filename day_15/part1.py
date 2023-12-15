import os

def get_input(name="input.txt"):
    current_directory = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(current_directory, name)
    with open(input_file_path, 'r') as file:
        input_file = file.read().strip().split(',')
    
    return input_file

def main():
    input_file = get_input()
    
    total = 0
    for step in input_file:
        step_hash = 0
        for char in step:
            step_hash = ((step_hash + ord(char)) * 17) % 256
        total += step_hash
            
    print(total)
            
            



if __name__ == "__main__":
    main()
