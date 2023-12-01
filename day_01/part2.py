import os

def get_input(name="input"):
    current_directory = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(current_directory, name)
    with open(input_file_path, 'r') as file:
        input_file = file.read().strip().split('\n')
    
    return input_file

def main():
    input_file = get_input()
    
    string_to_num = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }
    
    total = 0
    
    for line in input_file:
        num = ""
        n = len(line)
        
        for i in range(n):
            if line[i].isdigit():
                num += line[i]
                break
            if i >= 2:
                found = False
                for d in range(3,6):
                    if line[i-d+1:i+1] in string_to_num:
                        num += str(string_to_num[line[i-d+1:i+1]])
                        found = True
                        break
                if found:
                    break
            
        for i in range(n):
            if line[-(i+1)].isdigit():
                num += line[-(i+1)]
                break
            if i >= 2:
                found = False
                for d in range(3,6):
                    if line[n-i-1:n-i-1+d] in string_to_num:
                        num += str(string_to_num[line[n-i-1:n-i-1+d]])
                        found = True
                        break
                if found:
                    break
        # print(f"Line: {line}, number: {num}")
        total += int(num)
        
    print(total)
        



if __name__ == "__main__":
    main()
