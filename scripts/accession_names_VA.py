from __future__ import division

import re

genes = ["xkn59438", "yhdck2", "eihd39d9", "chdsye847", "hedle3455", "xjhd53e", "45da", "de37dp"]

print("contains 5:")
for gen in genes: 
    if re.search(r"5", gen): 
        print("\t" + gen) 

print("contains d or e:")
for gen in genes: 
    if re.search(r"(d|e)", gen): 
        print("\t" + gen) 

print("contains d and e in that order:")
for gen in genes: 
    if re.search(r"d.*e", gen): 
        print("\t" + gen)

print("contains d and e separated by a single letter:")
for gen in genes: 
    if re.search(r"(d.e)", gen): 
        print("\t" + gen) 

print("contains d and e in any order:")
for gen in genes: 
    if re.search(r"d.*e", acc) or re.search(r"e.*d", gen): 
        print("\t" + gen) 

print("starts with either x or y:")
for gen in genes: 
    if re.search(r"^(x|y)", gen): 
        print("\t" + gen) 

print("starts with either x or y and ends with e:")
for gen in genes: 
    if re.search(r"^(x|y).*e$", gen): 
        print("\t" + gen) 

print("contains three or more numbers in a row:")
for gen in genes: 
    if re.search(r"\d{3,}", gen): 
        print("\t" + gen) 

print("ends with d followed by either a, r or p:")
for gen in genes: 
    if re.search(r"d[arp]$", gen): 
        print("\t" + gen) 
