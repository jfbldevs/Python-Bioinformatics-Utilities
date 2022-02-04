n = 0
with open('PositiveData.txt', 'r') as f:
    for line in f:
        n += 1
        print('>' + str(n) + '\n' + line.strip())
        #print(line.strip())
        #print('>' + str(n) + '\n' + line)
