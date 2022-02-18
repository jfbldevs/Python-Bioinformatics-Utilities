#Split a sequence of characters into groups of two characters
def split_seq(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))

print(list(split_seq("AAARANAAD", 2)))