def get_sequence(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        sequences = {}
        for line in lines:
            if line.startswith('>'):
                identifier = line.strip()
                sequences[identifier] = ''
            else:
                sequences[identifier] += line.strip()
        return sequences

for i in get_sequence('sequences.txt'):
    print(i, get_sequence('sequences.txt')[i])
