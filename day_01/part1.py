import os

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
        num = ""
        n = len(line)
        for i in range(n):
            if line[i].isdigit():
                num += line[i]
                break
            
        for i in range(n):
            if line[-(i+1)].isdigit():
                num += line[-(i+1)]
                break
        total += int(num)
        
    print(total)
        



if __name__ == "__main__":
    main()
