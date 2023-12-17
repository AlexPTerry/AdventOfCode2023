import os
import heapq

def get_input(name="input.txt"):
    current_directory = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(current_directory, name)
    with open(input_file_path, 'r') as file:
        input_file = file.read().strip().split('\n')
    
    return input_file

def add_tuple(tup1, tup2):
    return tuple(i + j for i, j in zip(tup1, tup2))

def is_valid(pos, max_x, max_y):
    return 0 <= pos[0] <= max_x and 0 <= pos[1] <= max_y

def main():
    input_file = get_input()
    grid = [list(map(int, list(row))) for row in input_file]

    max_x = len(input_file[0]) - 1
    max_y = len(input_file) - 1

    visited_states = set()
    current_pos = (0, 0)
    current_momentum = 1
    current_score = 0

    visit_queue = [(current_score, current_pos, (1, 0), current_momentum), 
                   (current_score, current_pos, (0, 1), current_momentum)]
    heapq.heapify(visit_queue)
    visited_states = set()

    while current_pos != (max_x, max_y) or current_momentum < 4:
        current_score, current_pos, current_dir, current_momentum = heapq.heappop(visit_queue)
        current_state = (current_pos, current_dir, current_momentum)
        if current_state in visited_states:
            continue
        visited_states.add(current_state)

        for new_dir in {(1, 0), (0, -1), (-1, 0), (0, 1)} - {(-current_dir[0], -current_dir[1])}:
            new_pos = add_tuple(current_pos, new_dir)
            if not is_valid(new_pos, max_x, max_y):
                continue
            if current_dir == new_dir:
                new_momentum = current_momentum + 1
                if new_momentum > 10:
                    continue
            else:
                if current_momentum < 4:
                    continue
                new_momentum = 1

            new_score = current_score + grid[new_pos[1]][new_pos[0]]
            heapq.heappush(visit_queue, (new_score, new_pos, new_dir, new_momentum))

    print(current_score)

        



            



if __name__ == "__main__":
    main()
