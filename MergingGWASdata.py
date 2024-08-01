#Python script to merge neanderthal SNPs dataframe with selected GWAS results
#Author: Owen Jones
#Date: 03/07/2024

##Purpose##
#To merge Neanderthal SNPs data with GWA studies of interest. 
# This will be done individually for each GWAS, which will be manually changed and saved due to computational limitations.

import pandas as pd
import scipy.stats #To calculate P-value from Z-score

# Load GWAS summary statistics
gwas_data = pd.read_csv("[Your munged trait data]", sep = "\t") #e.g. the output from mungesumstats could be [trait name].tsv.sumstats
print(len(gwas_data)) # len of GWAS data: 
gwas_data = gwas_data.drop(columns=['P'])
gwas_data['P'] = ''
gwas_data['P'] = scipy.stats.norm.sf(abs(gwas_data['Z']))
print(gwas_data.head())
significantSNPs = gwas_data[gwas_data["P"] <= 5e-8]
print((significantSNPs))

# Load Neanderthal SNPs with alleles
neanderthal_snps = pd.read_csv("CleanedDF.tsv", sep = "\t")
neanderthal_snps = neanderthal_snps.rename(columns={"ID" : "SNP"})
# Merge data on SNP ID
merged_data = pd.merge(gwas_data, neanderthal_snps, on="SNP")
merged_data.to_csv("IS_Neander.tsv", sep = "\t")
