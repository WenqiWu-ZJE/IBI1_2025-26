import re
seq = 'AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG'
pattern = r'(?=(AUG(?:...)*?(?:UAA|UAG|UGA)))'
orfs = re.findall(pattern, seq)
if orfs:
    longest_orf = max(orfs, key=len)
    print("Longest ORF: ", longest_orf)
    print("Length: ", len(longest_orf))
else:
    print("No ORF found.")