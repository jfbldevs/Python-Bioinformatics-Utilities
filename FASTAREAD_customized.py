#Read txt file and print the sequence and identifier
def get_sequence(filename):
    """
    Return the all sequences in dict from the txt file.
    """
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

for i in get_sequence('sequences_na.txt'):
    print(i, get_sequence('sequences_na.txt')[i])