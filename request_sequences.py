secuencias = ['P81136', 'A5U0G8', 'A5I7X8',]

for i in secuencias:
      import requests
  #params = {"query": "P00750", "format": "fasta", "include": "yes"}
  params = {"query": i, "format": "fasta"}
  response = requests.get("http://www.uniprot.org/uniprot/", params=params)
  print (response.text)