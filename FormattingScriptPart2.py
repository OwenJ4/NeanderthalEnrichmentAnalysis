#Python script to clean and format probable neanderthal SNPs
#Author: Owen Jones
#Date: 01/07/2024

##Purpose##
#This script was created to clean and format the 
# probable archaic  SNPs found by Dannerman and Kelso (2017)
# The aims are to (1) match the CHR and POS and REF 
# and ALT alleles to the rsids in a Kaviar output.
# (2) Then to include identified archaic introgressed Neanderthal alleles 
# as a separate column, as these include REF and ALT alleles.

import pandas as pd
import numpy as np

#Part(2)
#Reading mergedDF from FormattingScriptPart1.py
mergedDF = pd.read_csv("MergedDF.tsv", sep = "\t")
mergedDF = mergedDF.drop(['Unnamed: 0', '#CHROM', 'POS_y', 'QUAL', 'FILTER', 'INFO'], axis=1)
mergedDF = mergedDF.rename(columns={'POS_x': 'POS'})
print(mergedDF)

#Reading a DF with an additional allele column which indicates which allele was likely from 
#Neanderthals for next steps of the analysis pipeline which requires the GWAS ALT 
#alleles be aligned to the suspected neanderthal allele.
NeanderAllelesDF = pd.read_csv("Neanderthal study - Neanderthal_Alleles.tsv", sep = "\t")
print(NeanderAllelesDF)

CleanedDF = mergedDF.merge(NeanderAllelesDF, how='inner', on='CHR_POS')
print(CleanedDF)
CleanedDF.to_csv("CleanedDF.tsv", sep="\t")
