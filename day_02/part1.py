import os

def get_input(name="input"):
    current_directory = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(current_directory, name)
    with open(input_file_path, 'r') as file:
        input_file = file.read().strip().split('\n')
    
    return input_file

def check_valid_game(game, max_colours):
    for round in game.split('; '):
        for pull in round.split(', '):
            num, colour = pull.split(' ')
            if max_colours[colour] < int(num):
                return False
    return True
        

def main():
    input_file = get_input()
    
    max_colours = {
        'red': 12,
        'green': 13,
        'blue': 14
    }
    total = 0
    
    for line in input_file:
        game_id = int(line.split(':')[0].split(' ')[1])
        game = line.split(': ')[1]
        if check_valid_game(game, max_colours):
            total += game_id
    print(total)
        



if __name__ == "__main__":
    main()
