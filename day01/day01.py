from sys import argv
import yaml
'''
Reads in any text file and returns a list of the data in that file
@param input_text - the file to be read from
@return initial - a list containing the data from the file
'''

def read_file(input_text):
        with open(input_text,'r') as f:
            initial = [(x.strip('\n')) for x in f.readlines()]
        return initial

def locate_2020_part1(file):
    data = set(map(int, read_file(file)))
    for val in data:
        check = 2020 - int(val)
        if check in data:
            return val * check

def locate_2020_part2(file):
    data = set(map(int, read_file(file)))
    for val in (data):
        remaining = 2020 - val
        for num in data:
            final = remaining - num
            if final in data:
                return val * num * final



if __name__ == "__main__":
    part1 = locate_2020_part1(argv[1])
    print(f"Part1: {part1}")    
    part2 = locate_2020_part2(argv[1])
    print(f"Part2: {part2}")