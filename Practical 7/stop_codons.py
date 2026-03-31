import re
input_file = 'Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
output_file = 'stop_genes.fa'
def find_stop_codons(sequence):
    start_pos = sequence.find('ATG')
    if start_pos == -1:
        return []
    found_stops = set()
    stop_codons = {'TAA', 'TAG', 'TGA'}
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
                    f_out.write(f">{gene_name}, {', '.join(stops)}\n")
                    f_out.write(f"{sequence}\n")
            gene_name = line.split()[0][1:] 
            sequence = "" 
        else:
            sequence += line
    if gene_name and sequence:
        stops = find_stop_codons(sequence)
        if stops:
            f_out.write(f">{gene_name}, {', '.join(stops)}\n")
            f_out.write(f"{sequence}\n")
print('Done! Output written to stop_genes.fa')
