import matplotlib.pyplot as plt
gene_expression = {'TP53': 12.4,'EGFR': 15.1,'BRCA1': 8.2,'PTEN': 5.3,'ESR1': 10.7}
print("Initial dictionary with 5 genes:")
print(gene_expression)
gene_expression['MYC'] = 11.6
genes = list(gene_expression.keys())
expressions = list(gene_expression.values())
plt.figure(figsize=(8, 5))
plt.bar(genes, expressions, color='skyblue')
plt.title('Gene Expression Levels')
plt.xlabel('Gene Name')
plt.ylabel('Expression Value')
plt.show()
# Pseudocode: Create a variable representing a gene of interest and print its value
# Modify this variable to test different genes
gene_of_interest = 'BRCA1'  
if gene_of_interest in gene_expression:
    print('The expression value for ' + gene_of_interest + ' is ' + str(gene_expression[gene_of_interest]))
else:
    print('Error: The gene ' + gene_of_interest + ' is not present in the dataset.')
total_expression = sum(expressions)
num_genes = len(expressions)
average_expression = total_expression / num_genes
print(  "The average gene expression level across all " + str(num_genes) + " genes is " + str(average_expression))