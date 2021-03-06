from propy import PyPro
from propy.GetProteinFromUniprot import GetProteinSequence
#note : The missing values in some AAindex properties were replaced by zero.
from propy.GetProteinFromUniprot import GetProteinSequenceFromTxt as gpst
#proteinsequence = GetProteinSequence("P48039")
#proteinsequence = 'LNQNFRKEYRRIIVSLCTARVFFVDSDSV'
from Bio import SeqIO
container = open('negative_dataset.txt','r')
for record in SeqIO.parse(container, "fasta"):#file
    DesObject = PyPro.GetProDes(record.seq)
    paac = DesObject.GetPAAC(lamda=6,weight=0.05) #Setting lamda
    #trip = DesObject.GetTPComp()
    #print(list(paac.values()))               
    #print(list(paac.values())) 
    #print(len(list(paac.values())))
    print(list(paac.values()))
    #print(len(record.seq))#Use len for verification
