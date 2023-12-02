import os

def get_input(name="input"):
    current_directory = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(current_directory, name)
    with open(input_file_path, 'r') as file:
        input_file = file.read().strip().split('\n')
    
    return input_file

def get_power(game):
    power = {
        'red': 0,
        'green': 0,
        'blue': 0
    }
    for round in game.split('; '):
        for pull in round.split(', '):
            num, colour = pull.split(' ')
            if power[colour] < int(num):
                power[colour] = int(num)
    return power['red'] * power['green'] * power['blue']
        

def main():
    input_file = get_input()
    
    total = 0
    for line in input_file:
        game = line.split(': ')[1]
        total += get_power(game)
    print(total)
        



if __name__ == "__main__":
    main()
