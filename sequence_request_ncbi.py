#pip install dendropy
#Own customization
from urllib.parse import scheme_chars
from dendropy.interop import genbank
gb_pep = genbank.GenBankProtein(ids=["XP_015198995.1",
"XP_015198998.1",
"XP_015199004.1",
"XP_015198997.1",
"XP_041091045.1"]
)
#symbol = 0
for gb in gb_pep:
  #symbol += 1
  print(f">{gb.definition}")
  print(gb.sequence_text.upper())

