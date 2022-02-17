#Dipeptide composition of a given peptide   
sequence = "ARNDCQEGHILKMFPSTWYV"

x = [i for i in sequence] 

combination_list = []

for j in x:
    for k in x:
        combination_list.append(j+k)

print(combination_list)
print(len(combination_list))
