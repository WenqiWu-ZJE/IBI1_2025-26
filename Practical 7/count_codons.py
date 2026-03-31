import re
import matplotlib.pyplot as plt
target_stop = input("Enter a stop codon (TAA, TAG, TGA): ").upper().strip()
if target_stop not in ['TAA', 'TAG', 'TGA']:
    print("Invalid stop codon.")
    exit()
pattern = rf'(?=(ATG(?:...)*{target_stop}))'
codon_counts = {}
input_file = 'Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
with open(input_file, 'r') as f:
    content = f.read()
    entries = re.split(r'\n>', content)
    for entry in entries:
        lines = entry.strip().split('\n')
        sequence = "".join(lines[1:])
        matches = re.findall(pattern, sequence)
        if matches:
            longest_orf = max(matches, key=len)
            codons = re.findall(r'.{3}', longest_orf[:-3])
            for c in codons:
                codon_counts[c] = codon_counts.get(c, 0) + 1
if codon_counts:
    labels, sizes = zip(*codon_counts.items())
    plt.figure(figsize=(15, 10))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.title(f"Codon Usage for Genes with {target_stop}")
    plt.savefig(f"re_codon_distribution_{target_stop}.png")
    print(f"Success! Plot saved.")