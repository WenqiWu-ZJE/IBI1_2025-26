from pathlib import Path
import re


SCRIPT_DIR = Path(__file__).resolve().parent
input_file = SCRIPT_DIR / 'Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
output_file = SCRIPT_DIR / 'stop_genes.fa'


def get_gene_name(header):
    gene_match = re.search(r'gene:([^\s]+)', header)
    if gene_match:
        return gene_match.group(1)
    return header.split()[0].lstrip('>').removesuffix('_mRNA')


def find_stop_codons(sequence):
    found_stops = set()
    stop_codons = {'TAA', 'TAG', 'TGA'}
    for start_pos in range(len(sequence) - 2):
        if sequence[start_pos:start_pos + 3] == 'ATG':
            for i in range(start_pos, len(sequence) - 2, 3):
                codon = sequence[i:i+3]
                if codon in stop_codons:
                    found_stops.add(codon)
    return sorted(list(found_stops))


with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
    gene_name = ""
    sequence = ""
    for line in f_in:
        line = line.strip()
        if line.startswith(">"):
            if gene_name and sequence:
                stops = find_stop_codons(sequence)
                if stops:
                    f_out.write(f">{gene_name} {' '.join(stops)}\n")
                    f_out.write(f"{sequence}\n")
            gene_name = get_gene_name(line)
            sequence = ""
        else:
            sequence += line
    if gene_name and sequence:
        stops = find_stop_codons(sequence)
        if stops:
            f_out.write(f">{gene_name} {' '.join(stops)}\n")
            f_out.write(f"{sequence}\n")
print('Done! Output written to stop_genes.fa')
