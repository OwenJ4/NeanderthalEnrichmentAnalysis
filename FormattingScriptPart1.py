#Python script to clean and format probable Neanderthal SNPs
#Author: Owen Jones
#Date: 27/06/2024

##Purpose##
#This script was created to clean and format the 
# probable archaic SNPs found by Dannerman and Kelso (2017)
# The aims are to (1) match the CHR and POS and REF 
# and ALT alleles to the rsids in a Kaviar output.
# (2) Then to include identified archaic introgressed Neanderthal alleles 
# as a separate column, as these include REF and ALT alleles.

import pandas as pd
import numpy as np


#Part (1)
###Neanderthal intogressed SNPs Dannerman and Kelso 2017
NeanderDF = pd.read_csv("Neanderthal study - Asterisk Removed.tsv", sep ="\t")
#Renaming column names to standardise to VCF format and match Kaviar Output
NeanderDF = NeanderDF.rename(columns={"CHR:POS": "CHR_POS", "Ref_Allele": "REF", "Effect_Allele": "ALT"})
#print(NeanderDF) # Output was as expected

#Reading Kaviar Genomic Database Query VCF output (hg19) from CHR:POS coordinates found in Dannerman and Kelso 2017
KaviarDF = pd.read_csv("KaviarSNPs_Neanderthal_hg19_Ouput.txt", sep ="\t")
KaviarDF['CHR_POS'] = ''
#Converting POS float data type to int for the concatenate_columns function
KaviarDF['POS'] = KaviarDF['POS'].astype('Int64')

def concatenate_columns(row): #A function to concatenate SNP coordinates in order to match NeanderDF
   return str(row['#CHROM']) + ':' + str(row['POS'])

KaviarDF['CHR_POS'] = KaviarDF.apply(concatenate_columns, axis=1)
#print(KaviarDF) # Output was as expected

#Kaviar Output is longer than Dannerman and Kelso (2017) study results due to multiple SNPs being associated with the same CHR/POS
#A solution to ensure quality of the merged dataframe is to align the REF and ALT alleles 
#so that they match the corresponding SNP found by Kaviar, and the direction of effect preserved.

#To ensure allele alignment, dataframes need to be merged where alleles match ref and effect allele, and CHR_POS
merged_df = NeanderDF.merge(KaviarDF, how='inner', on=['CHR_POS', 'REF', 'ALT'])
#Merged dataframe has dropped 177 SNPs from the original study dataframe (6210 -> 6033)
print(merged_df)
merged_df.to_csv("MergedDF.tsv", sep='\t')
