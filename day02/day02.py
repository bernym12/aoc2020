from sys import argv

'''
Reads in any text file and returns a list of the data in that file
@param input_text - the file to be read from
@return initial - a list containing the data from the file
'''

def read_file(input_text):
        with open(input_text,'r') as f:
            initial = [(x.strip('\n')) for x in f.readlines()]
        return initial

def data_split(line):
    info = line.split()
    counts = [int(val) for val in info[0].split('-')]
    letter = info[1].strip(':')
    password = info[2]
    return counts, letter, password
'''
@param data - a list of the data read in
'''
def part1(file):
    data = read_file(file)
    count = 0
    for line in data:
        counts, letter, password = data_split(line)
        amount = password.count(letter)
        if amount < counts[0] or amount > counts[1]:
            continue
        else:
            count += 1
    return count

def part2(file):
    data = read_file(file)
    count = 0
    for line in data:
        counts, letter, password = data_split(line)
        if password[counts[0] - 1] == letter and password[counts[1] - 1] == letter:
            continue
        elif password[counts[0] - 1] is not letter and password[counts[1] - 1] is not letter:
            continue
        else:
            count += 1
    return count
def main():
    org = part1(argv[1])
    correct = part2(argv[1])
    print(org)
    print(f"Day2 Part 2: {correct}")

if __name__ == "__main__":
    main()