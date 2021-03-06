from propy import PyPro
from propy.GetProteinFromUniprot import GetProteinSequence
#note : The missing values in some AAindex properties were replaced by zero.
with open('/content/negative.txt', 'r') as f: #Your peptide list in plain format
    for sequence in f:
      sequence = sequence.rstrip()
      #proteinsequence = GetProteinSequence("P48039")
      #proteinsequence = 'LNQNFRKEYRRIIVSLCTARVFFVDSDSV'    # download the protein sequence by uniprot id
      DesObject = PyPro.GetProDes(sequence)      # construct a GetProDes object
      paac = DesObject.GetPAAC(lamda=6,weight=0.05) #Setting lamda
      #trip = DesObject.GetTPComp()
      #print(list(paac.values()))               
      print(list(paac.values())) #Use len for verification

#paac.values()

#list(paac.values())
