import os

class HashMap:
    def __init__(self):
        self.box_list = [Box() for _ in range(256)]
        
    def follow_command(self, string):
        for i, char in enumerate(string):
            if not ('a' <= char <= 'z'):
                break
        label = string[:i]
        command = string[i]
        if command == '=':
            value = int(string[i+1])
            self.add_item(label, value)
        elif command == '-':
            self.remove_item(label)
                    
    def compute_hash(self, label):
        label_hash = 0
        for char in label:
            label_hash = ((label_hash + ord(char)) * 17) % 256
        return label_hash
        
    def add_item(self, label, value):
        box_num = self.compute_hash(label)
        self.box_list[box_num].add_item(label, value)
        
    def remove_item(self, label):
        box_num = self.compute_hash(label)
        self.box_list[box_num].remove_item(label)
        
    def compute_total_power(self):
        total = 0
        for box_num, box in enumerate(self.box_list):
            total += box.compute_box_power() * (box_num + 1)
        return total
    

class Box:
    def __init__(self):
        self.labels = []
        self.label_to_value = dict()
        
    def add_item(self, label, value):
        if label not in self.label_to_value:
            self.labels.append(label)
        self.label_to_value[label] = value
        
    def remove_item(self, label):
        if label not in self.label_to_value:
            return
        self.labels.remove(label)
        del self.label_to_value[label]
        
    def compute_box_power(self):
        total = 0
        for i, label in enumerate(self.labels):
            total += self.label_to_value[label] * (i+1)
        return total

def get_input(name="test.txt"):
    current_directory = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(current_directory, name)
    with open(input_file_path, 'r') as file:
        input_file = file.read().strip().split(',')
    
    return input_file

def main():
    input_file = get_input("input.txt")
    
    hash_map = HashMap()
    for command in input_file:
        hash_map.follow_command(command)
            
    print(hash_map.compute_total_power())
            
            



if __name__ == "__main__":
    main()
