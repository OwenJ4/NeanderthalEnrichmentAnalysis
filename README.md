# Neanderthal Enrichment Analysis
 ## Utilising likely archaic SNPs to investigate if they are enriched in neurological, psychiatric and cardio-metabolic traits

### Data Sources
Source	Total_SNPs (Post munge sumstats	Sig Snps (Post munge sumstats)	Signed_Summary_Statistic	Notes
Neanderthal SNPs	https://www.cell.com/ajhg/fulltext/S0002-9297(17)30379-8	NA	6210	NA	The introgressed archaic allele is marked with an asterisk (*) in column 3 or 4.

Neurological Disease Traits

35379992_Bellenguez_AD	https://www.ebi.ac.uk/gwas/publications/35379992	6809862	5004	OR
24076602_Beecham_MS https://www.ebi.ac.uk/gwas/publications/24076602 134209	3327	OR	
31701892_Nalls_PD	https://www.ebi.ac.uk/gwas/studies/GCST009325	6149662	2976	BETA	Cases included diagnosed PD and those with a first-degree relative with PD

Psychiatric Disorder Traits					

35396580_Trubetskoy_SCZ	https://www.ebi.ac.uk/gwas/publications/35396580	6399496	18130	BETA	
30718901_Howard_MDD	https://www.ebi.ac.uk/gwas/publications/30718901	6560747	4304	BETA	
30804558_Grove_ASD	https://www.ebi.ac.uk/gwas/publications/30804558	5524929	114	OR	

Cardio-Metabolic Disease Traits					

36474045_Aragam_CAD	https://www.ebi.ac.uk/gwas/studies/GCST90132314	7629939	15345	OR	
32541925_Vujkovic_T2D	https://www.ebi.ac.uk/gwas/studies/GCST010555	14631	27	BETA	
29531354_Malik_IS	https://www.ebi.ac.uk/gwas/studies/GCST006908	7048241	296	BETA

### Tools used 
Mungesumstats.py was used for data cleaning/formatting from LDSC (https://github.com/bulik/ldsc)


### Brief code descriptions
FormattingScriptPart1.py was used to clean and format the Neanderthal data, including a SNP column.
FormattingScriptPart2.py was used to find introgressed Neanderthal alleles in the REF and ALT columns to create a new Neanderthal allele column.
MergingGWASData.py created a dataframe of overlapping likely Neanderthal SNPs and trait SNPs.
HyperGeomTestNeander.py was used to perform a hypergeometric test between likely archaic Neanderthal SNPs and outcome trait GWA studies.

### Results
Results can be found here: https://github.com/OwenJ4/NeanderthalEnrichmentAnalysis/blobl/main/Results.md (best viewed in code mode)
No results from the hypergeometric tests were significant.

