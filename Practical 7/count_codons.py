from pathlib import Path
import re
import matplotlib.pyplot as plt


SCRIPT_DIR = Path(__file__).resolve().parent
input_file = SCRIPT_DIR / 'Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
valid_stop_codons = ['TAA', 'TAG', 'TGA']


target_stop = input("Enter a stop codon (TAA, TAG, TGA): ").upper().strip()
if target_stop not in valid_stop_codons:
    print("Invalid stop codon.")
    exit()
pattern = rf'(?=(ATG(?:...)*{target_stop}))'
codon_counts = {}
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
    output_file = SCRIPT_DIR / f"re_codon_distribution_{target_stop}.png"
    plt.savefig(output_file)
    print(f"Success! Plot saved to {output_file}.")
else:
    print(f"No in-frame codons were found for genes containing {target_stop}.")
