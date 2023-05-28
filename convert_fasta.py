n = 0
output = ""

with open('Negative Data/negative_proven.txt', 'r') as f:
    for line in f:
        n += 1
        output += '>' + str(n) + '\n' + line.strip() + '\n'

# Save the output to a file
with open('output.txt', 'w') as f:
    f.write(output)
