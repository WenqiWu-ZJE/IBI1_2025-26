# Practical 13 Summary

## 1. Human DLX5 information

The human DLX5 protein is 289 amino acids long.  
Its main subcellular localisation is the nucleus. GO cellular component annotations also include chromatin and cytoplasm.

## 2. Online BLAST results

I used the UniProt BLAST tool with human DLX5 as the query sequence and restricted the search to Eutheria.

- Number of BLAST hits: 250
- Percentage identity range: 52.3% to 100%
- Best alignment with mouse DLX5, UniProt ID P70396: 96.5% identity

In the alignment view, blue residues indicate identical amino acids, while grey residues indicate non-identical aligned residues.

## 3. Python alignment results

The Python script performed pairwise non-gapped global alignments using the BLOSUM62 matrix.

| Comparison | BLOSUM62 alignment score | Identical amino acids | Percentage identity |
|---|---:|---:|---:|
| Human DLX5 vs Mouse DLX5 | 1490 | 279 / 289 | 96.54% |
| Human DLX5 vs Random protein | -324 | 12 / 289 | 4.15% |
| Mouse DLX5 vs Random protein | -323 | 13 / 289 | 4.50% |

## 4. Interpretation

Human DLX5 and mouse DLX5 were the most closely related pair because they had the highest BLOSUM62 alignment score and the highest percentage identity. The comparisons involving the random protein sequence had much lower scores and lower percentage identities.

This suggests that the similarity between human and mouse DLX5 is biologically meaningful, rather than being caused by random amino acid matches.
