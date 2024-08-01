##Python script to perform a hypergeometric test
#Author: Owen Jones
#Date: 03/07/2024

###Purpose###
#To investigate whether Neanderthal SNPs are enriched in the selected GWA studies. 
#The merged data sets will be read and manually changed each time due to computational limitations.
#The below script is a template for how you could similarly perform this analysis

import pandas as pd

merged_data = pd.read_csv("[Your trait dataset]", sep = "\t")
print(merged_data.columns.values.tolist())

#  Function to align alleles, as the intogressed allele must align to the effect allele in the GWAS
def align_alleles(row):
    if row["A1"] == row["N_Allele"]:
        return row["BETA"]
    else:
        return -row["BETA"]

# Apply the function to align effect sizes
merged_data["Alligned_BETA"] = merged_data.apply(align_alleles, axis=1)

# Filter for significant SNPs
significant_snps = merged_data[merged_data["P"] <= 5e-8]
significant_snps.to_csv("Overlapping significant SNPs IS 5e-8.tsv", sep = "\t")

# Count total Neanderthal SNPs in GWAS
total_neanderthal_snps_in_gwas = len(merged_data)

# Count significant Neanderthal SNPs in GWAS
significant_neanderthal_snps = len(significant_snps)

# Total SNPs in GWAS dataset
total_snps_in_gwas = 7048241

# Total significant SNPs in GWAS dataset
total_significant_snps_in_gwas = 326 # As determined from the transformation of Z-scores from mungesumstats.py back to p-values.

# Perform Hypergeometric Test
import numpy as np
from scipy.stats import hypergeom

M = total_snps_in_gwas
n = total_neanderthal_snps_in_gwas
N = total_significant_snps_in_gwas
x = significant_neanderthal_snps


#p_value
p_value = hypergeom.sf(x-1, M, n, N)

#expected value and variance
expected_value = (n * N) / M # Expected number of significant Neanderthal SNPs given the number of Neanderthal SNPs (n)
# by the total significant SNPs in the GWAS dataset (M).
variance = (n * N * (M - n) * (M - N)) / (M**2 * (M - 1)) 

#Z-score
z_score = (x - expected_value) / np.sqrt(variance)

#Odds Ratio (OR)
odds_ratio = (x / (n - x)) / ((N - x) / (M - N - (n - x)))

#Fold Enrichment
fold_enrichment = (x / n) / (N / M)

print(f"P-value: {p_value}")
print(f"Expected Value: {expected_value}")
print(f"Variance: {variance}")
print(f"Z-score: {z_score}")  
print(f"Odds Ratio: {odds_ratio}")
print(f"Fold Enrichment: {fold_enrichment}")
