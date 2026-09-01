nature genetics
Article https://doi.org/10.1038/s41588-024-01702-0
Cell-type-specific and disease-associated
expression quantitative trait loci in the
human lung
Received: 21 March 2023 Heini M. Natri 1,12, Christina B. Del Azodi2,3,12, Lance Peter1, Chase J. Taylor 4,
Sagrika Chugh2,3,5, Robert Kendle1, Mei-i Chung1, David K. Flaherty6,
Accepted: 28 February 2024
Brittany K. Matlock6, Carla L. Calvi4, Timothy S. Blackwell4,7,8,
Published online: 28 March 2024 Lorraine B. Ware 4,9, Matthew Bacchetta 10, Rajat Walia 11, Ciara M. Shaver4,
Jonathan A. Kropski 4,7,8,13, Davis J. McCarthy 2,3,5,13 &
Check for updates Nicholas E. Banovich 1,13
Common genetic variants confer substantial risk for chronic lung
diseases, including pulmonary fibrosis. Defining the genetic control of
gene expression in a cell-type-specific and context-dependent manner is
critical for understanding the mechanisms through which genetic variation
influences complex traits and disease pathobiology. To this end, we
performed single-cell RNA sequencing of lung tissue from 66 individuals
with pulmonary fibrosis and 48 unaffected donors. Using a pseudobulk
approach, we mapped expression quantitative trait loci (eQTLs) across 38
cell types, observing both shared and cell-type-specific regulatory effects.
Furthermore, we identified disease interaction eQTLs and demonstrated
that this class of associations is more likely to be cell-type-specific and linked
to cellular dysregulation in pulmonary fibrosis. Finally, we connected lung
disease risk variants to their regulatory targets in disease-relevant cell types.
These results indicate that cellular context determines the impact of genetic
variation on gene expression and implicates context-specific eQTLs as key
regulators of lung homeostasis and disease.
Genomic and functional studies have the potential to reveal the complex traits2. However, cell type and context (for example, disease
genetic, molecular and cellular drivers of clinical phenotypes, laying status) and the specificity of trait-associated SNPs poses a challenge to
the groundwork for the development of targeted interventions. Many understanding the regulatory mechanisms that modulate disease risk
disease-associated variants identified in genome-wide association and progression.
studies (GWAS) are located in the regulatory regions of the genome and Single-cell RNA sequencing (scRNA-seq) has emerged as a power-
contribute to disease risk and progression by effecting changes in gene ful tool for the transcriptional profiling of individual cells and cell types,
expression1. Combining genotype information with transcriptional pro- mitigating many limitations of bulk RNA-seq. Capturing scRNA-seq
files allows for the identification of genetic regulators of gene expres- profiles and genome-wide genotype information from a population
sion (that is, expression quantitative trait loci (eQTLs)). This approach of individuals allows for the unbiased, cell-type-specific interrogation
has been widely applied to bulk RNA sequencing of primary tissues, of variant effects on gene expression. This approach can enable the
providing insights into the tissue specificity of regulatory effects and discovery of eQTLs that are specific to rare or disease-relevant cell
contributing to our understanding of the mechanisms underlying types and eQTLs that have opposing effects in different cell types, all of
A full list of affiliations appears at the end of the paper. e-mail: nbanovich@tgen.org
Nature Genetics | Volume 56 | April 2024 | 595–604 595

Article https://doi.org/10.1038/s41588-024-01702-0
which could go undetected in bulk RNA-seq of heterogeneous tissues. for analyzing measures of effect sizes across many conditions to iden-
These context-specific eQTLs are more likely to escape the purifying tify patterns of sharing and specificity12. After applying multivariate
selection that limits mutations impacting ubiquitous eQTLs and are adaptive shrinkage with mashr (Methods), eQTLs were considered
thus more likely to have roles in disease3,4. significant if they had a local false sign rate (LFSR) of 0.05 or less in
Interstitial lung diseases (ILDs) are chronic, progressive respira- at least one cell type and 0.1 or less in any additional cell type. A gene
tory disorders characterized by the scarring of lung tissue accompanied was considered an eGene for a cell type if any eQTL for that gene was
by epithelial remodeling, loss of functional lung alveoli and accumu- significant. Of the 6,995 genes tested for eQTL (Methods), 6,637 (95%)
lation of extracellular matrix5. Pulmonary fibrosis is the end-stage were eGenes in at least one cell type. The number of eGenes found
clinical phenotype of ILD. Pulmonary fibrosis remains incurable; the per cell type was greater for more abundant cell types (Fig. 2a), with
most severe form of pulmonary fibrosis (idiopathic pulmonary fibrosis a positive correlation (R = 0.66, P = 6.6 × 10−6) between the number
(IPF)) leads to death or lung transplant within 3–5 years of diagnosis5,6. of eGenes and the number of individuals used for mapping (Fig. 2b).
The pathogenesis and progression of IPF involve a complex interplay of To evaluate the robustness of these results, we used a permutation
predisposing factors, cell types and regulatory pathways7,8. GWAS and scheme by shuffling genotypes and repeating the analysis for each
meta-analyses have identified 20 IPF-associated variants, and polygenic cell type, and then comparing the permuted P values to the observed
analyses suggest that a large number of unreported variants contribute P values and to a theoretical null distribution (Supplementary Figs. 7
to IPF susceptibility9. Some of these variants are eQTLs in bulk lung and 8). We observed no notable deviation between the empirical and
tissue; however, their cell-type-specific regulatory consequences have theoretical null distributions, demonstrating that our approach was
not been explored. well-calibrated to avoid false positives.
To investigate the genetic control of disease-related gene expres- To summarize the overall pattern of eQTL sharing between cell
sion in pulmonary fibrosis, we generated scRNA-seq data from the types and compare this pattern with the transcriptional similarity, we
lung tissue samples of 114 individuals (66 individuals with ILD and 48 visualized the top two principal components of the median pseudob-
unaffected donors). Combining these data with genome-wide geno- ulked gene expression levels across all 38 cell types for the 6,995 genes
type data, we mapped shared, lineage-specific and cell-type-specific included in the eQTL mapping (Fig. 2c) and of the mashr-estimated
cis-eQTLs across 38 cell types (Fig. 1a). We analyzed these data in con- effect sizes of top eQTL across all 38 cell types (Fig. 2d). This analysis
junction with IPF and other GWAS summary statistics to uncover the demonstrated that the relationships between the regulatory mecha-
regulatory mechanisms underlying ILD risk and progression. Using nisms across lung cell types largely reflected the differences in expres-
interaction models, we reveal disease-specific regulatory effects that sion patterns across cell types. We identified a set of top eQTLs by
further elucidate the mechanisms underlying disease biology. selecting the eQTL with the lowest, significant LFSR for each gene in
each cell type. Using these criteria, there were 50,389 top eQTLs, with
Results a median of 7 top eQTLs per gene across cell types (minimum = 1, maxi-
scRNA-seq of 114 lung tissue samples mum = 33). Top eQTLs were considered shared between two cell types if
To enable cell-type-level eQTL mapping, we generated scRNA-seq and they were significant in both cell types and their mashr-estimated effect
genome-wide genotype profiles for 114 individuals, including 66 (58%) size was within a factor of 0.5. Across all cell types, the median pairwise
with ILD and 48 (42%) unaffected donors (Fig. 1a and Supplementary sharing of top eQTLs was 93.5% (minimum = 55%, maximum = 99.3%;
Table 1). The ILD lungs included samples from 39 individuals with IPF Fig. 3). The epithelial and endothelial lineages had the highest levels of
and 27 with other forms of pulmonary fibrosis, including sarcoidosis interlineage sharing (median = 97.9%) while sharing between cell types
(n = 4), connective tissue disease-associated ILD (n = 3), idiopathic within the mesenchymal lineage (median = 96.9%) and the immune
nonspecific interstitial pneumonia (n = 3), coal worker’s pneumoco- lineages (median = 95.4%) was slightly lower.
niosis (n = 3), chronic hypersensitivity pneumonitis (n = 2), intersti- We further classified top eQTLs as global (n = 34,030), multi-cell
tial pneumonia with autoimmune features (n = 2) and unclassifiable type (n = 14,027) or unique to a specific cell type (n = 2,332) (Methods).
ILD (n = 10). Most (67%) the lung samples were from individuals with Global top eQTLs tended to be found in genes with higher average
self-reported ethnicity of European ancestry; 53 (46%) reported past expression and that were more widely expressed across cells (Supple-
or present tobacco use (Fig. 1b). mentary Fig. 10). Top eQTLs unique to a single cell type tended to have
Single-cell suspensions were generated from fresh peripheral higher absolute estimated effect sizes (Supplementary Fig. 10), prob-
lung tissue samples and processed using the 10X Genomics Chromium ably due in part to limited statistical power to detect cell-type-specific
platform. For the 55 ILD lung samples, two libraries were prepared effects in some cell types (Supplementary Fig. 10). Finally, these
from differentially affected (more or less fibrotic) areas of one lung cell-type-specific top eQTLs also tended to be located further from
to account for regional heterogeneity. Genotype data was obtained the transcription start site (TSS) (Supplementary Fig. 10) of their tar-
through low-pass whole-genome sequencing (WGS) followed by impu- get, which is consistent with the observation that cell-type-specific
tation (Methods). We performed data integration, dimensionality eQTLs typically impact enhancers, while widely shared eQTLs impact
reduction and unsupervised clustering of the 475,047 cells passing promoters13,14. We overlapped the top eQTLs with genic annotations
quality control using the Seurat package10 (Methods and Supplemen- from TxDb. Out of the 63% of sc-eQTL SNPs (eSNPs) that overlapped
tary Figs. 1–3). Based on marker gene expression (Supplementary genic annotations, 7.9% were located on promoters and 30.3% were
Table 2), we identified 43 cell types with a median of 5,811 cells (mini- intergenic; the remaining overlapped at least one intron, exon or UTR.
mum = 253, maximum = 94,413, mean = 11,048 cells; Fig. 1c). Out of the sc-eQTLs unique to a single cell type, shared between multi-
ple cell types or globally across all cell types, 4.0%, 7.1% and 6.7% were
Most eQTLs are shared between cell types located on promoters, and 14.2%, 26.0% and 22.9% were intergenic,
Out of 43 annotated cell types, we selected 38 that had 40 or more with no statistically significant differences in annotations between
donors with five or more cells for that cell type to use for eQTL discovery eQTLs belonging to the different categories (Supplementary Fig. 13a).
(Fig. 1d). These inclusion criteria were selected to maximize our ability to We further explored the overlap of the various classes of eQTL among
map eQTLs with confidence across many cell types (Supplementary all enhancers in the EnhancerAtlas 2.0 (ref. 15) lung tissue enhancers,
Note 1). Pseudobulk eQTL mapping was performed on each cell type and the human lung epithelial cell line (Calu-3) enhancers, as well as
using LIMIX according to the optimized approach described in ref. 11. cis-regulatory elements in the Human Cell Atlas16. Testing for the equal-
To maximize precision and overcome varying statistical power across ity of proportions overlapping enhancer annotations between eQTLs
cell types, we used multivariate adaptive shrinkage, a statistical method and the null set, we found that multistate sc-eQTLs were more likely to
Nature Genetics | Volume 56 | April 2024 | 595–604 596

Article https://doi.org/10.1038/s41588-024-01702-0
a
b c
Immune
Epithelial
Mesenchymal
Endothelial
UMAP-1
d
Nature Genetics | Volume 56 | April 2024 | 595–604 597
2-PAMU
100
75
50
25
sllec
5≥ htiw slaudividni
fo
.oN
Diagnosis Self-reported Ever
ethnicity smoker
sronod
fo
egatnecreP
114
donors
48 unaffected
66 with ILD
(39 with IPF)
Cells Donors
seneG seneG
Mean
aggregation
stceffe
LTQe
scRNA-seq and WGS 475,047 cells
cis-eQTL Disease-specific
LMM effects
ILD Control
Posterior effect Regulatory loci
Cell types estimates underlying disease
Multivariate GWAS
adaptive colocalization
shrinkage
Other
Other N/A
N/A
African
American
IPF No
European
Yes
Control
Immune Mesenchymal
90
60
30
0
Infla M m m D m M o a n t o o c r y y te m M oD o C noc
A
yt
lv
e
e
P c
o
ro D
la
l C i
r
f 2 e m ra a t c in ro g ph
I
a
n
C g
te
e D
r
8
s
/
it
N
ia
K
l
T ma C c D ro 4 phage MastNK B cel P l las ma cD C1 pD C Adventitia A l F lv B eolar FB S M C Peri M cy e t s e othelial
Epithelial Endothelial
90
60
30
0
Alveo S la e r c t y – p S S e e C c 2 G – C B i S 1 li A C a 1 t G + e / B d M 1A U 1 C +/ 5 S B C + S G e B c 3 – A S 2+ C G A B l 3 v A e 2 o + lar typ T e ra 1 nsit B i P o a r s n o a a li l l f e a D r l i v a ff e t e i o n r l g e a n r t t i y a p ti e n g 2 cil K ia R te T d 5−/KRT17+ Arteriole Venule Syst a e C m a i p c venou Ly s G m e p n h e a ra ti l c capillary
Fig. 1 | Mapping eQTLs across cell types in the human lung. a, Schematic the eQTL analysis. Pseudocoloring indicates cell type; primary cell lineages are
illustration of the present study. b, Percentage proportions of donors according labeled. d, Numbers of donors with ≥5 cells for each cell type included in the
to diagnosis (42.1% unaffected controls, 34.2% IPF, 23.7% other ILD), self-reported analysis. LMM, linear mixed model; moDC, monocyte-derived dendritic cell; N/A,
ethnicity (66.7% European, 9.6% African American, 17.5% N/A, 6.1% other) and not applicable; NK, natural killer cell; NKT, natural killer T cell; pDC, plasmacytoid
smoking history (46.5% ever smoker, 29.8% never smoker, 23.7% N/A). c, UMAP dendritic cell; SMC, smooth muscle cell. Panel a created with BioRender.com.
dimensionality reduction of 437,618 cells across the 38 cell types included in

| Article             |     |                                    |     |                    |     |       |     |                                  |                            |     | https://doi.org/10.1038/s41588-024-01702-0 |               |     |               |
| ------------------- | --- | ---------------------------------- | --- | ------------------ | --- | ----- | --- | -------------------------------- | -------------------------- | --- | ------------------------------------------ | ------------- | --- | ------------- |
| a                   |     |                                    |     |                    |     | b     |     |                                  |                            |     |                                            |               |     |               |
|                     |     |                                    |     |                    |     |       |     |                                  |                            |     |                                            | Immune        |     | Mesenchymal   |
|                     |     |                                    |     |                    |     |       |     |                                  |                            |     |                                            | Lymphoid      |     | Fibroblast    |
|                     |     |                                    |     |                    |     |       |     |                                  |                            |     |                                            | Myeloid       |     | Mesothelial   |
| seneGe fo .oN 6,400 |     |                                    |     |                    |     | 6,400 |     |                                  |                            |     |                                            |               |     |               |
|                     |     |                                    |     |                    |     |       |     |                                  |                            |     |                                            | Proliferating |     | Pericyte      |
|                     |     |                                    |     |                    |     |       |     |                                  |                            |     |                                            | Epithelial    |     | Endothelial   |
| 6,200               |     |                                    |     |                    |     | 6,200 |     |                                  |                            |     |                                            |               |     |               |
|                     |     |                                    |     |                    |     |       |     |                                  |                            |     |                                            | Distal        |     | Lymphatic     |
|                     |     |                                    |     |                    |     |       |     |                                  |                            |     |                                            | Proliferating |     | Macrovascular |
|                     |     |                                    |     |                    |     |       |     |                                  |                            |     |                                            | Proximal      |     | Microvascular |
|                     |     |                                    |     | R = 0.3, P = 0.067 |     |       |     |                                  | R = 0.66, P = 6.6  ×  10−6 |     |                                            |               |     |               |
| 6,000               |     |                                    |     |                    |     | 6,000 |     |                                  |                            |     |                                            |               |     |               |
|                     | 0   |                                    | 100 |                    | 200 | 500   | 40  | 60                               | 80                         |     | 100                                        |               |     |               |
|                     |     | Median no. of cells per individual |     |                    |     |       |     | No. of individuals with ≥5 cells |                            |     |                                            |               |     |               |
| c                   |     |                                    |     |                    |     |       |     | d                                |                            |     |                                            |               |     |               |
0.3
|     |     |     |     |     | Alveolar macrophage |                    |     |     |     |     |     |     | Monocyte−derived macrophage |          |
| --- | --- | --- | --- | --- | ------------------- | ------------------ | --- | --- | --- | --- | --- | --- | --------------------------- | -------- |
|     |     |     |     |     |                     | Macrophage − SPP1+ |     |     |     |     |     |     |                             | Alveolar |
|     |     |     |     |     | cDC1                |                    |     |     |     |     |     |     | moDC                        |          |
macrophage
Inflammatory monocyte moDC Proliferating − Immune Proliferating − Immune
|     | 0.2 |          |     |      |                             |     |     |     | 0.2  |     |      |      | Monocyte | Inflammatory |
| --- | --- | -------- | --- | ---- | --------------------------- | --- | --- | --- | ---- | --- | ---- | ---- | -------- | ------------ |
|     |     |          |     |      | Monocyte−derived macrophage |     |     |     |      |     | Mast | cDC1 |          |              |
|     |     | Monocyte |     | cDC2 |                             |     |     |     | cDC2 |     |      |      |          | monocyte     |
Macrophage − SPP1+
|              | CD8/NKT   |         |           | pDC             |        |             |        |              |                  |        |          |           |     |     |
| ------------ | --------- | ------- | --------- | --------------- | ------ | ----------- | ------ | ------------ | ---------------- | ------ | -------- | --------- | --- | --- |
|              |           | B cells |           |                 |        |             |        |              | 0.1 B cells      | pDC    |          |           |     |     |
| )%20.81( 2CP |           | NK      | Mast      |                 | Plasma |             |        | )%85.61( 2CP | Pericyte         |        |          | NK        |     |     |
|              |           | CD4     | Lymphatic |                 |        |             |        |              |                  | Plasma |          | CD4       |     |     |
|              | 0         |         |           |                 |        |             |        |              |                  |        | SMC      | CD8/NKT   |     |     |
|              | Arteriole | Venule  |           | Peribronchiolar |        |             |        |              | Capillary        |        |          | Lymphatic |     |     |
|              |           |         |           | Matrix FB       |        |             |        |              | 0 CA4+ capillary |        |          |           |     |     |
|              | Capillary |         |           | WNT2+ FB        |        | Mesothelial |        |              |                  |        |          | Arteriole |     |     |
|              |           | SMC     | Pericyte  |                 |        |             |        |              | Mesothelial      |        | WNT2+ FB |           |     |     |
|              |           |         |           |                 | Basal  |             | KRT5−/ |              |                  |        |          | Venule    |     |     |
CA4+ Alv e o la r T r a n s it i o n a l KRT17+ KRT5−/KRT17+ Matrix FB Peribronchiolar
|     | capillary |      |      |     | A l ve o lar | al v e o l a r  t y p e 2 |     | −0.1 |     |     |     |     |     |     |
| --- | --------- | ---- | ---- | --- | ------------ | ------------------------- | --- | ---- | --- | --- | --- | --- | --- | --- |
|     |           | ty p | e  1 |     | ty p e  2    |                           |     |      |     |     |     |     |     |     |
−0.2 S e cr e to r y  − S e c r et o r y  − Prolif e ra t in g  − Alveolar type 1 Secretory −
SCGB1A1+ /S C G B 3 A 2 + +/ E p it h e lia l Basal SCGB1A1+/MUC5B+
|     |     |     |     |     | S C G B 1 A 1 |     |     |      |     |     |                       |                               | Alveolar |     |
| --- | --- | --- | --- | --- | ------------- | --- | --- | ---- | --- | --- | --------------------- | ----------------------------- | -------- | --- |
|     |     |     |     |     | MUC5B+        |     |     | −0.2 |     |     | Tr an s i t io n a l  | a l v e o l a r   t y p e   2 | ty pe 2  |     |
Secretory − Differentiating S e c r e to r y   −  S C G B 1 A 1 +/ S C G B 3 A 2 + S e c r et o r y  −
SCGB3A2+ P ro l if e r a t i n g   −   Ep i th e l ia l S C G B 3 A 2 +
Ciliated
|     |     |      |     |              | Ciliated |     |     |     |     |      | Differentiating Ciliated |              | Ciliated |     |
| --- | --- | ---- | --- | ------------ | -------- | --- | --- | --- | --- | ---- | ------------------------ | ------------ | -------- | --- |
|     |     | −0.2 |     | 0            |          | 0.2 |     | 0.4 |     | −0.2 |                          | 0            |          | 0.2 |
|     |     |      |     | PC1 (34.75%) |          |     |     |     |     |      |                          | PC1 (59.14%) |          |     |
Fig. 2 | sc-eQTL structure reflects lineage and cell type relationships.   per cell type and the number of individuals with at least five cells of that cell type
a, Comparison of the number of eGenes per cell type and the median number of  (Pearson correlation). c, Principal component analysis (PCA) plot of pseudobulk
cells per individual of that cell type (two-sided Pearson correlation). Cell types  expression across the 6,995 genes included in the eQTL mapping analysis.
are colored according to sublineage. b, Comparison of the number of eGenes  d, PCA plot of mashr-estimated effect sizes for the top eQTLs (n = 50,389).
be found overlapping the Human Cell Atlas cis-regulatory elements  between the epithelial and immune lineages and were enriched for
than the null set (P = 3.502 × 10−11; Supplementary Fig. 13b).
genes associated with highly lineage-specific functions, such as epi-
To explore the pattern of eQTL sharing across cell types more  thelial cell morphogenesis.
closely, we focused on multi-cell-type top eQTLs. We pruned these
top eQTLs to get a representative sample for plotting (n = 3,725; Sup- Disease-specific eQTLs are highly cell-type specific
plementary Table 5) and adjusted the sign of the effect sizes to where  To identify eQTLs specific to healthy or affected individuals or
positive indicates the common effect direction and negative indicates  showing a different direction or degree of effect in the two groups,
an opposite effect direction; Methods). In an unsupervised clustering  we performed disease-state interaction eQTL (int-eQTL) mapping
of the sign-adjusted effect sizes of these pruned eQTLs, we identified  (Methods). Testing across 33 cell types with five or more individu-
distinct classes of eQTLs (Fig. 4), including groups of eQTLs primarily  als with ILD and five or more unaffected donors and a minor allele
active in epithelial or immune cell types, or exhibiting opposing effects  frequency (MAF) ≥ 5% in each group, we detected 83,596 int-eQTLs.
between lineages. To connect these eQTLs to biological processes, we  Applying this same analysis to our data after permuting the disease
tested for the enrichment of their target eGenes among Gene Ontology  status resulted in 829 int-eQTLs, supporting a 1% false positive rate.
(GO) terms against a set of 6,995 background genes (Fig. 4 and Meth- Compared to the non-int-eQTLs, there was substantially less lineage
ods). The eQTLs in cluster 3 were primarily active in the epithelial cell  and cell type sharing of int-eQTLs (Fig. 5a and Supplementary Fig. 12):
types and were enriched for genes involved in the regulation of JUN  for each gene, there was a median of 21 top int-eQTLs (minimum = 2,
kinase, which has been implicated in lung fibrosis and is a potential  maximum = 28), resulting in a total of 75,482 top int-eQTLs. Com-
target for interventions for ILD17. Epithelial eQTLs in cluster 5 were  pared to the top non-int-eQTLs, int-eQTLs were further from the TSS
enriched for genes associated with metabolism and response to bac- (mean absolute distance, sc-eQTL = 43.1 Mb, int-eQTL = 52.9 Mb, t-test
teria. The eQTLs in cluster 4 were primarily significant in the myeloid  P = 2.22 × 10−16) and had larger effect sizes (mean absolute mashr pos-
innate immune cell types and showed enrichment for genes involved  terior beta, sc-eQTLs = 0.10, int-eQTLs = 0.66, t-test P = 2.22 × 10−16;
in, for example, cholesterol metabolism. Furthermore, eQTLs in cluster  Fig. 5b) and higher MAFs (mean MAF sc-eQTLs = 0.29, int-eQTLs = 0.37,
1 were mainly significant in the immune lineage and were enriched for  P = 2.22 × 10−16). Some disease int-eQTLs were linked to overall expres-
genes contributing to cholesterol homeostasis, reflecting the central  sion differences between groups (Fig. 5c): 43% of int-eGenes were dif-
role of cholesterol metabolism in immune functions18. Cluster 7, also  ferentially expressed (adjusted P < 0.1) between ILD and unaffected
mainly active in the immune lineage, was enriched for genes involved  samples in the particular cell type. Out of these genes, 50.8% were
with, for example, lipid transport. Lipid mediators have an important  expressed at a higher level in ILD. However, 21% of int-eGenes were
role in lung fibrosis19. The eQTLs in cluster 2 showed opposing effects
widely expressed (>30% of cells) in both groups in the particular cell
| Nature Genetics | Volume 56 | April 2024 | 595–604 |     |     |     |     |     |     |     |     |     |     |     |     |     | 598 |
| -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Article https://doi.org/10.1038/s41588-024-01702-0
type and did not exhibit notable differences in expression levels (log least one cell type when using a significance threshold of adjusted
fold change < 0.2), indicating that these eGenes were equally expressed P < 0.1. When examined across all cell types with significant differen-
but were differentially affected by cis-regulatory loci. These include DSP tial expression, 43.0% of these genes were expressed at a higher level
with three top int-eQTLs, including rs2003916, which was not signifi- in the ILD samples. The seven that were equally expressed between
cantly associated with IPF risk in the GWAS meta-analysis (P = 0.15) but cases and controls (adjusted P > 0.1), including WT1, SOX10, PAX7,
showed differential effects between individuals with ILD and unaffected HOXA11, HOXD12, NKX6-1 and SCRT1, could contribute to ILD patho-
donors in four of the tested epithelial cell types (Fig. 5d). genesis through differences in protein levels or localization, differential
To further interrogate the mechanisms underlying these int-eQTLs, binding to cis-regulatory elements or chromatin-level differences in
we analyzed the int-eQTLs associated with eGenes expressed equally addition to or instead of differential transcription factor abundance.
between individuals with ILD and unaffected donors for the enrich- We further examined the expression of these transcription factors by
ment of known transcription factor binding sites (TFBS) (Methods). contrasting donors with 0/0 genotypes for rs2003916 (Fig. 5d) and
We identified 42 significantly enriched transcription factor motifs those with at least one alternative allele or those with two alternative
(q < 0.05), including WT1, several SOX, HOX and PAX family members, alleles. We found no differential expression of the significantly enriched
ERG and NF1 (Fig. 5e and Supplementary Table 6). Several of these transcription factors in any of the epithelial cell types included in the
have known importance in lung fibrosis. WT1 functions as a positive eQTL analysis, corroborating that the effect is not due to overall dif-
regulator of fibroblast proliferation, myofibroblast transformation ferences in transcription factor expression, but due to sequence-level
and extracellular matrix production20. A number of SOX transcription or chromatin-level differences.
factors are upregulated in IPF and are associated with fibroblast activa- We assessed the level at which sc-eQTLs and int-eQTLs are
tion21,22. Out of the 37 genes encoding transcription factors disrupted replicated in bulk analyses by overlapping the eQTLs detected in
by int-eQTLs that were also tested for differential expression, 30 were this study with lung eQTLs from the Genotype-Tissue Expression
differentially expressed between ILD and unaffected samples in at (GTEx) project (Supplementary Note 2 and Supplementary Fig. 15)2.
Nature Genetics | Volume 56 | April 2024 | 595–604 599
etycireP lailehtoseM BF
raloevlA
BF
laititnevdA
CMS yrallipac
lareneG
etycoreA citahpmyL suonev
cimetsyS
eluneV eloiretrA 1
epyt
raloevlA
2
epyt
raloevla
lanoitisnarT
2
epyt
raloevlA
lailehtipE—gnitarefilorP lasaB +2A3BGCS/+1A1BGCS—yroterceS +B5CUM/+1A1BGCS—yroterceS +2A3BGCS
−
yroterceS
detailic
gnitaitnereffiD
detailiC +71TRK/−5TRK
ylppa
esaelP
llec
B
amsalP KN 4DC TKN/8DC tsaM CDp 1CDc 2CDc CDom enummI—gnitarefilorP egahporcam
laititsretnI
egahporcam
raloevlA
egahporcam
devired−etyconoM
etyconoM etyconom
yrotammaflnI
No. of individuals No. of donors
with ≥5 cells log 10 (nCells)
Lineage
Sublineage
40 60 80 100 120
Pericyte
Median no. of cells Mesothelial
per individual Alveolar FB
Adventitial FB
96.9% SMC
10 100 1,000 General capillary
Aerocyte
Lymphatic
Mesenchymal Systemic venous
Fibroblast Venule
Mesothelial 97.9% Arteriole
Pericyte Alveolar type 1
Transitional alveolar type 2
Endothelial Alveolar type 2
Proliferating—Epithelial
Lymphatic
Basal
Macrovascular Secretory—SCGB1A1+/SCGB3A2+
Microvascular Secretory—SCGB1A1+/MUC5B+
Secretory—SCGB3A2+
Epithelial Differentiating ciliated
Distal Ciliated
Proliferating
97.8% KRT5−/KRT17+
B cell
Proximal
Plasma
Immune NK
CD4
Lymphoid
CD8/NKT
Myeloid
Mast
Proliferating pDC
cDC1
cDC2
moDC
Percentage shared
Proliferating—Immune
Interstitial macrophage
Alveolar macrophage
50 60 70 80 90100 Monocyte-derived macrophage
Monocyte
95.4% Inflammatory monocyte
Fig. 3 | eQTLs are largely shared between lung cell types. Percentage of top according to lineage, sublineage, the number of individuals with five or more
eQTLs (n = 50,389) shared between two cell types. Top eQTLs are considered cells and the median number of cells per individual for that cell type. Median
shared if they are significant in both cell types (LFSR ≤ 0.1) and the mashr- pairwise percentage sharing per lineage is shown in black.
estimated effect size is within a factor of 0.5. Cell types are annotated above

Article https://doi.org/10.1038/s41588-024-01702-0
No. of individuals with No. of individuals
≥5 cells No. of cells
Lineage
Sublineage
40 60 80 100 120 1 1. Cholesterol homeostasis
Median no. of cells per 1. Epithelial cell morphogenesis
individual 2 2. Positive regulation of cysteine-
type endopeptidase activity in apoptosis
3. Keratinocyte development
10 100 1,000
D E iv s e ti r m ge a n t t ed effe C c o t m s m iz o e n 3 1 to . R n e u g c u le la u t s ion of protein localization
2. Negative regulation of JUN kinase
0.4 0.2 0 0.2 0.4 3. Endoplasmic reticulum stress-induced
preemptive quality control
Mesenchymal
Fibroblast
Mesothelial
Pericyte 1. Cholesterol catabolic process
Endothelial 4 2. Extracellular matrix disassembly
Lymphatic 3. Positive regulation of IL-1β
Macrovascular
Microvascular
Epithelial 1. Negative regulation of
Distal endopeptidase activity
Proliferating 5 2. Response to bacterium
Proximal 3 C . a P 2+ o c s o it n iv c e e r n e t g ra u t l i a o t n ion of mitochondrial
Immune
Lymphoid
Myeloid
1. Sphingolipid biosynthetic process
Proliferating
2. Regulation of small GTPase-mediated
6 signal transduction
3. RNA polymerase I pre-
initiation complex assembly
1. Epithelial cilium movement
involved in extracellular fluid movement
7 2. Opsonization
3. Lipid transport
Fig. 4 | Multi-cell-type eQTLs act in a highly lineage-specific manner. The most common effect direction for each eQTL is shown in red and cell
Visualization of a representative subset (Methods) of multi-cell-type top eQTLs types with opposite effect directions are shown in blue. The top three most
and IPF-GWAS eQTLs (n = 2,158). eQTLs are clustered according to their estimated significantly enriched GO terms for each cluster, excluding terms with support
effect sizes, with nonsignificant associations set to zero. eQTL effect sizes are not from less than two genes, are shown.
shown (gray) for genes expressed in less than 10% of cells of that cell type.
All classes of sc-eQTLs and int-eQTLs were enriched among GTEx lung In addition to the intersection analysis described above, we colo-
eQTLs (Fisher’s exact test, P < 2.2 × 10−16). Out of the globally shared calized eQTL signals for 2,092 genes, including the target genes of the
and multi-cell-type top eQTLs, 19.1% and 21.9% were also eQTLs in multistate eQTLs in Fig. 4 and 103 GWAS-implicated genes, with the IPF
the GTEx lung with a nominal P < 1 × 10−6 (Fig. 5f). However, only GWAS meta-analysis9, the UK Biobank (UKBB) IPF GWAS24 and an East
11.7% of sc-eQTLs unique to a single cell type and 13.4% of int-eQTLs Asian IPF GWAS25 (Methods). We identified five loci with evidence of
were GTEx-significant. This finding demonstrates the power of colocalization (posterior probability for a single shared causal variant
cell-type-specific and context-specific analyses in uncovering reg- greater than 0.6) between risk loci and eQTLs in at least one cell type.
ulatory effects concealed by less granular approaches. We further These patterns largely overlapped between the IPF GWAS meta-analysis
compared the immune cell type eQTLs detected in this study to the and the UKBB (Fig. 6 and Supplementary Table 8). Three of these loci
ones reported in a previous study on peripheral blood mononuclear were eQTLs for genes previously implicated in a GWAS in the National
cells (n = 982; Supplementary Note 2)23. Out of the 848 eQTLs for NK Human Genome Research Institute (NHGRI)-EBI GWAS Catalog26:
cells and 104 eQTLs for plasma cells detected by Yazar et al.23 that were MUC5B, DSP and KANSL1. The locus associated with KANSL1 in both
also tested for in our study, 31.0% and 19.2% were significant in our the GWAS and eQTL analysis was also associated with the expression
analysis of these cell types, respectively. of KANSL1-AS1 across several cell types in our dataset. Additionally,
we found that an eQTL for the gene JAML was significantly colocalized
Cell-type-specific patterns of colocalization at GWAS loci with a locus from the GWAS analysis. This variant did not meet the
To connect the shared and cell-type-specific regulatory variants to IPF criterion for genome-wide significance in the GWAS analysis but was
risk, we compared our results to a recent IPF GWAS meta-analysis9. All an eQTL across a number of myeloid lineage cell types (Supplementary
major classes of eQTLs were enriched among loci implicated (nominal Fig. 19). MUC5B was robustly expressed and colocalized with the IPF
P < 1 × 10−6, Supplementary Table 7) by the IPF GWAS meta-analysis GWAS meta-analysis and the UKBB IPF GWAS in SCGB1A1+/MUC5B+ and
(Fisher’s exact test, globally shared P < 5.09 × 10−64, multi-cell-type SCGB3A2+ secretory cells, implicating these as the most likely cell types
P < 1.83 × 10−98, unique to a single cell type P = 0.0525), while a null set in which the risk variant functions (Supplementary Figs. 17 and 18). In
of nonsignificant eQTLs with a matched distribution of distances to contrast to the mostly European IPF GWAS meta-analysis and UKBB,
the TSS was not (P = 1). GTEx bulk lung eQTLs were similarly highly the MUC5B eQTL did not significantly colocalize with the East Asian
enriched (P = 2.22 × 10−111) among the IPF GWAS loci. Surprisingly, dis- IPF GWAS in any cell type, probably because of the low frequency of the
ease interaction eQTLs were not more enriched among IPF GWAS loci risk allele in Asian populations27. The pattern of population sharing was
than a null set of nonsignificant eQTLs. different for the DSP eQTL, which was colocalized with the IPF GWAS
Nature Genetics | Volume 56 | April 2024 | 595–604 600

| Article |     |     |     |     |     |     | https://doi.org/10.1038/s41588-024-01702-0 |     |     |     |     |
| ------- | --- | --- | --- | --- | --- | --- | ------------------------------------------ | --- | --- | --- | --- |
| a       |     |     |     | b   |     |     |                                            |     |     |     |     |
int-eQTLs
|     | 40,000 |     |     |     |     | P < 2.22 × 10–16 |     |     |     | P < 2.22 × 10–16 |     |
| --- | ------ | --- | --- | --- | --- | ---------------- | --- | --- | --- | ---------------- | --- |
|     |        |     |     |     | 3   |                  |     | 12  |     |                  |     |
sc-eQTLs
|     | sLTQe pot fo .oN |     |     | )bM( SST ot ecnatsiD |     |     |     |     |     |     |     |
| --- | ---------------- | --- | --- | -------------------- | --- | --- | --- | --- | --- | --- | --- |
9
|     |        |     |     |     | 2   |     |     | ezis tceffE |     |     |     |
| --- | ------ | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- |
|     | 20,000 |     |     |     |     |     |     | 6           |     |     |     |
1
3
|     |     | 0       |     |     | 0   |          |         | 0   |          |     |         |
| --- | --- | ------- | --- | --- | --- | -------- | ------- | --- | -------- | --- | ------- |
|     |     | 0 10 20 | 30  |     |     |          |         |     |          |     |         |
|     |     |         |     |     |     | int-eQTL | sc-eQTL |     | int-eQTL |     | sc-eQTL |
Significant in no. of cell types
| c   |                              |                 |            | d   |     |     |         | e    |     |                      |     |
| --- | ---------------------------- | --------------- | ---------- | --- | --- | --- | ------- | ---- | --- | -------------------- | --- |
|     |                              | Alveolar type 1 | Lineage    |     |     |     |         |      |     |                      |     |
|     |                              |                 |            |     |     | ILD | Control | −log | (P) | Percentage of tested |     |
|     |                              |                 |            |     |     |     |         |      | 10  | int-eQTLs with motif |     |
|     | Transitional alveolar type 2 |                 | Epithelial |     |     |     |         |      |     |                      |     |
Alveolar type 1, LFSR = 0.004
|     |     | Alveolar type 2 | Immune |     |     |     |     |     |     |     |     |
| --- | --- | --------------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
1.2
|                           |                          |     |             |     |     |     |     | 6.0 | 8.0 |     |         |
| ------------------------- | ------------------------ | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | ------- |
|                           | Proliferating—Epithelial |     | Endothelial |     | 0.8 |     |     |     |     | 4   | 8 12 16 |
| Secretory—SCGB1A1+/MUC5B+ |                          |     |             |     | 0.4 |     |     |     |     |     |         |
Mesenchymal
|     |     |     |     |     | 0   |     |     | WT1 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Secretory—SCGB1A1+/SCGB3A2+
|     | Secretory—SCGB3A2+ |     |     | −0.4 |     |     |     | Sox4 |     |     |     |
| --- | ------------------ | --- | --- | ---- | --- | --- | --- | ---- | --- | --- | --- |
int-eGenes
|     |     |     |     |     | 0/0 | 0/1 1/1 | 0/0 0/1 1/1 | Sox17 |     |     |     |
| --- | --- | --- | --- | --- | --- | ------- | ----------- | ----- | --- | --- | --- |
Ciliated
6,000
|     |     |     |     |     | Alveolar type 2, LFSR = 0.043 |     |     | Sox15 |     |     |     |
| --- | --- | --- | --- | --- | ----------------------------- | --- | --- | ----- | --- | --- | --- |
Differentiating ciliated
|     |     | Basal |     |     | 0.4 |     |     | PU.1 |     |     |     |
| --- | --- | ----- | --- | --- | --- | --- | --- | ---- | --- | --- | --- |
0
|     |     |     |     |     | 0.2 |     |     | EWS:ERG |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- |
fusion
NK
|     |     |     | DEGs              |     | 0   |     |     | Znf263 |     |     |     |
| --- | --- | --- | ----------------- | --- | --- | --- | --- | ------ | --- | --- | --- |
|     |     | CD4 | (adjusted P <0.1) |     |     |     |     |        |     |     |     |
Sox10
|     |     | CD8/NKT | 15,000 |     | 0/0 | 0/1 1/1 | 0/0 0/1 1/1 |     |     |     |     |
| --- | --- | ------- | ------ | --- | --- | ------- | ----------- | --- | --- | --- | --- |
PSD naeM
|     |     | Plasma |               |     |                               |              |     | PAX5      |     |         |           |
| --- | --- | ------ | ------------- | --- | ----------------------------- | ------------ | --- | --------- | --- | ------- | --------- |
|     |     |        |               |     | Transitional alveolar type 2, |              |     | NF1       |     |         |           |
|     |     | B cell | 0             |     |                               | LFSR = 0.026 |     | half-site |     |         |           |
|     |     | cDC2   |               |     | 1.5                           |              |     |           | Zf  | M G ETS | CTF e d , |
|     |     |        |               |     |                               |              |     |           |     | H       | ir ox     |
|     |     | moDC   | int-eGene-DEG |     | 1.0                           |              |     |           |     |         | Pa o b    |
|     |     |        | overlap (%)   |     |                               |              |     |           |     |         | m e       |
|     |     |        |               |     | 0.5                           |              |     |           |     |         | ho        |
Alveolar macrophage
|     |     |     | 100 |     | 0   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Monocyte
|     |                       |     |     | −0.5 |     |         |             | f        |     |     |     |
| --- | --------------------- | --- | --- | ---- | --- | ------- | ----------- | -------- | --- | --- | --- |
|     | Inflammatory monocyte |     |     |      | 0/0 | 0/1 1/1 | 0/0 0/1 1/1 | int-eQTL |     |     |     |
0
Monocyte-derived
|     |     | macrophage |     |     | Secretory,SCGB3A2+, |     |     |     |     |     |     |
| --- | --- | ---------- | --- | --- | ------------------- | --- | --- | --- | --- | --- | --- |
Unique
|     |                      | Mast |     |     |     | LFSR = 0.040 |     |            |     |     |     |
| --- | -------------------- | ---- | --- | --- | --- | ------------ | --- | ---------- | --- | --- | --- |
|     | Proliferating—Immune |      |     |     |     |              |     | Multistate |     |     |     |
1.0
|     |     | Lymphatic |     |     |     |     |     |     | Global |     |     |
| --- | --- | --------- | --- | --- | --- | --- | --- | --- | ------ | --- | --- |
0.5
Arteriole
0
|     |     |     |     |     |     |     |     |     | 0   | 10  | 20  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Venule
Percentage of eQTLs in GTEx lung
|     |     |     |     |     | 0/0 | 0/1 1/1 | 0/0 0/1 1/1 |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------- | ----------- | --- | --- | --- | --- |
SMC
rs2003916
Pericyte
Fig. 5 | Disease interaction eQTLs converge on pathways relevant to lung  and differentially expressed genes (DEGs) between fibrotic and unaffected
fibrosis. a, Histogram of the cell type sharing of the top int-eQTLs and the top  samples, and proportion of their overlap for each cell type included in the int-
non-int-eQTLs. b, Comparison of absolute distances to the eGene TSS and  eQTL analysis. d, Example of an int-eQTL for DSP. In the violin plots, the mean
absolute effect sizes of the top sc-eQTLs (n = 50,506) and int-eQTLs (n = 83,596).  and two s.d. are indicated. e, Top transcription factor motifs enriched among int-
Two-sided t-test P values are indicated. In the box plots, the lower and upper  eSNPs associated with eGenes that were equally expressed between individuals
hinges correspond to the first and third quartiles. The upper whisker extends  with ILD and unaffected donors but exhibited differences in eQTL effect sizes.
from the hinge to the largest value no further than 1.5 times the interquartile  Transcription factors are grouped according to family on the x axis. f, Percentage
range (IQR) from the hinge; the lower whisker extends from the hinge to the  of int-eQTLs, sc-eQTLs unique to a single cell type, multi-cell-type sc-eQTLs and
globally shared sc-eQTLs that are also eQTLs in GTEx lung (P < 1 × 10−6).
smallest value at most 1.5 times the IQR of the hinge. c, Numbers of int-eGenes
meta-analysis in alveolar type 2, transitional alveolar type 2 and alveolar  types. However, the expression levels and eQTL effect sizes of KANSL1
type 1 cells, and with the UKBB and the East Asian IPF GWAS in alveolar  and KANSL1-AS1 were highly correlated (Supplementary Figs. 22–24);
type 2 cells (Supplementary Fig. 21). The eQTL for KANSL1 colocalized  both genes were ubiquitous but lowly expressed across cell types,
with the meta-analysis and UKBB in ciliated epithelial cells. Additionally,  impeding an exact evaluation of the cell type specificity of these effects.
the eQTL for KANSL1-AS1 antisense RNA was widely colocalized with the  When examining how these signals were colocalized in the
meta-analysis and UKBB across epithelial, immune and endothelial cell  bulk eQTL analyses, we found that the colocalization patterns of
| Nature Genetics | Volume 56 | April 2024 | 595–604 |     |     |     |     |     |     |     |     |     |     | 601 |
| -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Article https://doi.org/10.1038/s41588-024-01702-0
| All cell types               |     | 5   | 4 1 0 | 0 MUC5B | DSP | KANSL1 |     | KANSL1-AS1 |
| ---------------------------- | --- | --- | ----- | ------- | --- | ------ | --- | ---------- |
| Alveolar type 1              |     | 2   | 0 0 0 | 0       |     |        |     |            |
| Transitional alveolar type 2 |     | 3   | 1 0 0 | 0       |     |        |     |            |
| Alveolar type 2              |     | 3   | 3 1 0 | 0       |     |        |     |            |
| Proliferating—Epithelial     |     | 2   | 2 0 1 | 1       |     |        |     |            |
Secretory—SCGB1A1+/MUC5B+
|     |     | 2   | 2 0 1 | 0   |     |     |     |     |
| --- | --- | --- | ----- | --- | --- | --- | --- | --- |
Secretory—SCGB1A1+/SCGB3A2+
|     |     | 1   | 0 0 0 | 0   |     |     |     |     |
| --- | --- | --- | ----- | --- | --- | --- | --- | --- |
Secretory—SCGB3A2+
|          |     | 2   | 2 0 1 | 0   |     |     |     |     |
| -------- | --- | --- | ----- | --- | --- | --- | --- | --- |
| Ciliated |     | 1   | 1 0 2 | 0   |     |     |     |     |
Differentiating ciliated
|         |      | 1   | 0 0 1 | 0   |     |     |     |     |
| ------- | ---- | --- | ----- | --- | --- | --- | --- | --- |
|         | NK   | 1   | 1 0 0 | 0   |     |     |     |     |
|         | CD4  | 1   | 1 0 0 | 0   |     |     |     |     |
| CD8/NKT |      | 1   | 1 0 0 | 0   |     |     |     |     |
|         | cDC2 | 1   | 1 0 1 | 0   |     |     |     |     |
| moDC    |      | 1   | 1 0 2 | 1   |     |     |     |     |
Interstitial macrophage
|                             |      | 1   | 1 0 1 | 0   |     |     |     |     |
| --------------------------- | ---- | --- | ----- | --- | --- | --- | --- | --- |
| Alveolar macrophage         |      | 3   | 2 0 1 | 0   |     |     |     |     |
| Monocyte                    |      | 1   | 1 0 2 | 0   |     |     |     |     |
| Inflammatory monocyte       |      | 1   | 1 0 2 | 0   |     |     |     |     |
| Monocyte−derived macrophage |      | 3   | 2 0 5 | 1   |     |     |     |     |
|                             | Mast | 1   | 1 0 0 | 0   |     |     |     |     |
Lymphatic
|     |     | 1   | 1 0 0 | 0   |     |     |     |     |
| --- | --- | --- | ----- | --- | --- | --- | --- | --- |
Arteriole
|                   |             | 1             | 1 0 0       | 0                 |                    |            |                 |                         |
| ----------------- | ----------- | ------------- | ----------- | ----------------- | ------------------ | ---------- | --------------- | ----------------------- |
| Systemic venous   |             | 1             | 1 0 0       | 0                 |                    |            |                 |                         |
| Venule            |             | 1             | 1 0 0       | 0                 |                    |            |                 |                         |
| Adventitial FB    |             | 1             | 0 0 0       | 0                 |                    |            |                 |                         |
|                   | SMC         | 1             | 0 0 0       | 0                 |                    |            |                 |                         |
| Alveolar FB       |             | 1             | 0 0 0       | 0                 |                    |            |                 |                         |
| GTEx lung         |             | 7             | 2 2 9       | 4                 |                    |            |                 |                         |
| GTEx whole-blood  |             | 5             | 1 1 7       | 7                 |                    |            |                 |                         |
| GTEx brain cortex |             | 1             | 0 1 3       | 5                 |                    |            |                 |                         |
|                   |             | s i s s i s A | S A S A S   | AS                |                    | P e r      | c e n t a g e   |                         |
|                   | l           | y l y W       | W W W       |                   |                    |            |                 |                         |
|                   | n a         | n a   G       |   G   G   G | Line a g e        | Stud y   t y p e   | o f   e    | Q T L s         |                         |
|                   | a - a       | a - a P F P F | m a m a     |                   |                    |            |                 | S i g n i fi c a n t ly |
|                   | e t e t     | B   I n   I   | h h         | E p i t h e l i a | l I P F   G W A S  | o v e      | r l a p p i n g |                         |
|                   | m m         | K B i a a s t | a s t       |                   |                    | I P F      |   G W A S   l o | ci c o l o c a li z e d |
| A                 | S   A S   U | A s e t   e   | t           | I m m u n e       | O t h e r   G W AS |            | – 6             |                         |
| W                 | W           | s t   n s n s |             |                   |                    | ( P   <    |   1   ×   1 0 ) | g e n e s               |
| G                 | G E a       | - o - o       |             | E n d o t h e     | l i a l            |            |                 |                         |
| IPF  PF           |             | o d u l t     |             |                   |                    |            |                 |                         |
| I                 | h o         | A d           |             | M e s e n c       | h y m al           |            |                 |                         |
|                   | d           |               |             |                   |                    | 0          | 2 5+            | 0 5+                    |
|                   | h il        |               |             | G T E x           |                    |            |                 |                         |
|                   | C           |               |             |                   |                    | P e r      | c e n t a g e   |                         |
|                   |             |               |             |                   |                    | of cells   |                 | Posterior probability   |
|                   |             |               |             |                   |                    | expressing |                 | for a single shared     |
|                   |             |               |             |                   |                    | the eGene  |                 | causal variant          |
|                   |             |               |             |                   |                    | 0          | 80              | 0 1                     |
Fig. 6 | Cell-type-specific eQTLs colocalize with the lung trait GWAS. Numbers  (orange) and the posterior probabilities for a single shared causal variant between
of SNPs that were nominally significant (P < 1 × 10−6) in the IPF GWAS meta-analysis  the tested cell types and the GWAS for the selected top IPF-associated genes
and also eQTL (blue), the numbers of significant colocalizations between cell  (MUC5B, DSP, KANSL1, KANSL1-AS1, shown in green) across 27 cell types with at
type and bulk eQTLs and three IPF GWAS, as well as childhood-onset and adult- least one colocalized gene.
onset asthma GWAS (red). Shown are the proportion of cells expressing the gene
MUC5B and DSP between GTEx lung and IPF GWAS reflected those  Discussion
of the cell-type-level analysis (Supplementary Fig. 15 and Supple- In this study, we present a characterization of regulatory genetic vari-
mentary Table 8). MUC5B was significantly colocalized with the  ants across major cell types in the human lung, using scRNA-seq to
IPF GWAS meta-analysis and UKBB, but not with the East Asian IPF  identify eQTLs at cell-type resolution. In total, we characterized eQTLs
GWAS. DSP was colocalized in all three IPF GWAS. KANSL1, however,  across 38 different cell types identifying cis-eQTLs in over 6,000 genes.
did not colocalize between the GTEx lung and any IPF GWAS. To  Building on bulk eQTL studies, such as the GTEx project2, which sought
assess to what extent the genetic and cell-type-specific regulatory  to characterize differences in gene regulatory architecture across tis-
architecture of IPF risk may be shared with other lung diseases, we  sues, we used a multivariate adaptive shrinkage approach to robustly
colocalized the cell-type eQTL signals with the childhood-onset and  identify shared and specific eQTLs across cell types2. In addition to the
adult-onset asthma GWAS28. The childhood-onset asthma colocaliza- majority of eQTLs that were shared across cell types, we identified thou-
tion revealed a regulatory architecture distinct from IPF, with a lack  sands of eQTLs that were limited to a subset or single cell type. These
of colocalization in epithelial cells and most of the significant colo- eQTL classes were enriched among chronic lung disease GWAS loci and
calizations being specific to immune cells, particularly monocytes and  DEGs in fibrotic lungs, suggesting that context-specific gene regula-
monocyte-derived macrophages, which may shape some of the clinical  tory mechanisms are important but yet, to date, largely unrecognized
and inflammatory features of asthma29,30. These results highlight the  contributors to the mechanisms underlying chronic lung diseases.
broader utility of this dataset in the investigation of other lung traits   Highlighting the power of this approach, we demonstrate that
and diseases. many of the eQTLs identified in this study were not eQTLs in bulk
Nature Genetics | Volume 56 | April 2024 | 595–604 602

Article https://doi.org/10.1038/s41588-024-01702-0
data from primary lung tissue (Fig. 5f). This was particularly true of to ILD. For example, we found enrichment for WT1 (ref. 20) and SOX
eQTLs limited to a single cell type (11.7% significant in bulk) and dis- family members21,22, which previous experimental evidence connected
ease interaction eQTLs, which were far less likely to be shared across to fibroblast activation and proliferation in the lung. The eQTLs that
cell types (13.4% significant in bulk). Both of these classes of eQTLs disrupt key binding sites probably further propagated the molecular
tended to be further away from the TSS than global and multistate dysregulation observed in ILD by modulating the binding efficiency
eQTLs suggesting that these loci may be disrupting enhancers rather of transcription factors and altering the expression of their direct
than promoters (Figs. 4a and 5b). This observation would be con- and downstream target genes. Of note, int-eQTLs were not enriched
sistent with the cell type specificity of these eQTLs and would distin- for overlaps with risk variants, as anticipated based on the presumed
guish them from eQTLs identified in bulk studies, which are strongly requirement for disease-associated contextual cues for these variants
enriched for disrupting promoter regions. Indeed, some work sug- to manifest their effects. We postulate that these context-specific eQTLs
gested that common eQTLs (enriched near promoters) are less likely may have a role in disease progression rather than initiation. Again,
to have functional relevance1,31,32. In addition to being more distal from these results highlight the importance of identifying context-specific
the TSS, cell-type-specific eQTLs tended to have larger effect sizes eQTLs that are best captured using single-cell approaches.
(Figs. 4a and Fig. 5b). At present, it is uncertain whether the difference Taken together, our study demonstrates the powerful application
in effect size is due to statistical power to identify these associations or of single-cell genomics to study genetic regulation of gene expres-
if cell-type-specific eQTLs inherently exhibit larger effect sizes. As this sion in complex, solid, primary human tissues. Integrating scRNA-seq
class of eQTL is the least likely to benefit from the mashr12 approach, data from control and disease-affected lung samples with genetic
it seems plausible that we only have statistical power to identify those data provides insights into the cell-type-specific function of risk vari-
with large effects. If this is the case, future single-cell eQTL studies with ants for ILD and highlights int-eQTLs as a class of regulatory variants
increased sample numbers and cell type representation from rare cell that contribute to disease pathobiology. Future work combining
populations are likely to identify a substantial number of additional single-cell multiomic assays, healthy and disease-affected samples,
cell-type-specific and context-specific eQTLs. and context-specific analysis methods, will be important to understand
Over the past 10 years, there has been an increased appreciation the interplay of dysfunctional genetic regulation and cellular contexts
for the degree to which eQTLs may be context-specific, starting first in complex human disease.
with tissue type, then to functional and environmental contexts, and
finally to cell type23,33–39. The results of this study suggest that sc-eQTL Online content
studies have the power to elucidate this context specificity and that Any methods, additional references, Nature Portfolio reporting sum-
they will better recover eQTLs associated with disease states or envi- maries, source data, extended data, supplementary information,
ronmental perturbations because these effects are less likely to be acknowledgements, peer review information; details of author contri-
shared across cell types within a tissue. butions and competing interests; and statements of data and code avail-
In addition to a general characterization of eQTLs in the lung, this ability are available at https://doi.org/10.1038/s41588-024-01702-0.
study is uniquely positioned to explore the interplay between genetic
variation and the molecular underpinnings of chronic lung diseases References
including pulmonary fibrosis. Focusing first on the known risk loci iden- 1. Umans, B. D., Battle, A. & Gilad, Y. Where are the
tified in various GWAS studies, we found eQTLs to be enriched among disease-associated eQTLs? Trends Genet. 37, 109–124 (2021).
GWAS risk loci regardless of class (Fig. 6). These enrichments were simi- 2. Aguet, F. et al. The GTEx Consortium atlas of genetic regulatory
lar to those found in the bulk eQTL analysis from the human lung (Fig. 6); effects across human tissues. Science 369, 1318–1330 (2020).
however, using cell-type-level associations, we were able to partition the 3. Lea, A. J., Peng, J. & Ayroles, J. F. Diverse environmental
function of these risk variants into discrete cell types. Indeed, we found perturbations reveal the evolution and context-dependency
that risk variants were most likely to be eQTLs in alveolar type 2 cells, of genetic effects on gene expression levels. Genome Res. 32,
followed by a number of cells from the myeloid lineage, including both 1826–1839 (2022).
resident and recruited macrophages (Fig. 6 and Supplementary Table 7). 4. Aguet, F. et al. Genetic effects on gene expression across human
Using a more formal colocalization analysis, we found four GWAS loci tissues. Nature 550, 204–213 (2017).
with strong support for a shared causal variant with an eQTL (compared 5. Lederer, D. J. & Martinez, F. J. Idiopathic pulmonary fibrosis.
to seven colocalizations in the bulk eQTL data), for which we identified N. Engl. J. Med. 378, 1811–1823 (2018).
the likely cell type in which these risk variants are acting (Fig. 6). Our find- 6. Ley, B., Collard, H. R. & King, T. E. Jr. Clinical course and prediction
ings align with recent insights into the cellular and regulatory drivers of of survival in idiopathic pulmonary fibrosis. Am. J. Respir. Crit.
ILD. Epithelial cell types have a central role in driving alveolar remodeling Care Med. 183, 431–440 (2011).
in IPF40. Indeed, in a GWAS colocalization analysis, we found that the top 7. Moss, B. J., Ryter, S. W. & Rosas, I. O. Pathogenic mechanisms
IPF risk variants flanking MUC5B and DSP regulated the expression levels underlying idiopathic pulmonary fibrosis. Annu. Rev. Pathol. 17,
of their targets in specific epithelial cell types. 515–546 (2022).
In addition to assessing the effect of known risk loci on gene expres- 8. Habermann, A. C. et al. Single-cell RNA sequencing reveals
sion traits, we also more directly examined how genetic variation may profibrotic roles of distinct epithelial and mesenchymal lineages
alter key regulatory processes involved in disease. Turning back to the in pulmonary fibrosis. Sci. Adv. 6, eaba1972 (2020).
disease interaction eQTL analysis, enabled by the collection of a cohort 9. Allen, R. J. et al. Genome-wide association study of susceptibility
consisting of both affected and unaffected individuals, we assessed to idiopathic pulmonary fibrosis. Am. J. Respir. Crit. Care Med. 201,
how these context-specific eQTLs may further drive disease processes. 564–574 (2020).
Roughly half of the interaction eQTLs were driven by differences in 10. Hao, Y. et al. Integrated analysis of multimodal single-cell data.
overall mean expression between the disease-affected and control sam- Cell 184, 3573–3587.e29 (2021).
ples. In the case of disease-emergent expression difference (expression 11. Cuomo, A. S. E. et al. Optimizing expression quantitative trait
increased in the disease-affected samples), loci that further upregulate locus mapping workflows for single-cell studies. Genome Biol. 22,
gene expression may propagate additional molecular dysfunction. 188 (2021).
Focusing on the set of interaction eQTLs with similar mean expression 12. Urbut, S. M., Wang, G., Carbonetto, P. & Stephens, M. Flexible
across disease-affected and control samples, we found the loci to be statistical methods for estimating and testing effects in genomic
enriched for TFBS associated with key biological processes related studies with multiple conditions. Nat. Genet. 51, 187–195 (2019).
Nature Genetics | Volume 56 | April 2024 | 595–604 603

Article https://doi.org/10.1038/s41588-024-01702-0
13. Dimas, A. et al. Common regulatory variation impacts gene 29. van der Veen, T. A., de Groot, L. E. S. & Melgert, B. N. The different
expression in a cell type-dependent manner. Science 325, faces of the macrophage in asthma. Curr. Opin. Pulm. Med. 26,
1246–1250 (2009). 62–68 (2020).
14. Mu, Z. et al. The impact of cell type and context-dependent 30. Niessen, N. M. et al. Neutrophilic asthma features increased
regulatory variants on human immune traits. Genome Biol. 22, 122 airway classical monocytes. Clin. Exp. Allergy 51, 305–317
(2021). (2021).
15. Gao, T. & Qian, J. EnhancerAtlas 2.0: an updated resource with 31. Glassberg, E. C., Gao, Z., Harpak, A., Lan, X. & Pritchard, J. K.
enhancer annotation in 586 tissue/cell types across nine species. Evidence for weak selective constraint on human gene
Nucleic Acids Res. 48, D58–D64 (2020). expression. Genetics 211, 757–772 (2019).
16. Moody, J. et al. A single-cell atlas of transcribed cis-regulatory 32. Mostafavi, H., Spence, J. P., Naqvi, S. & Pritchard, J. K. Systematic
elements in the human genome. Preprint at bioRxiv https://doi.org/ differences in discovery of genetic effects on gene expression
10.1101/2023.11.13.566791 (2023). and complex traits. Nat. Genet. 55, 1866–1875 (2023).
17. Popmihajlov, Z. et al. CC-90001, a c-Jun N-terminal kinase (JNK) 33. Lonsdale, J. et al. The Genotype-Tissue Expression (GTEx) project.
inhibitor, in patients with pulmonary fibrosis: design of a phase Nat. Genet. 45, 580–585 (2013).
2, randomised, placebo-controlled trial. BMJ Open Respir. Res. 9, 34. Strober, B. J. et al. Dynamic genetic regulation of gene expression
e001060 (2022). during cellular differentiation. Science 364, 1287–1290 (2019).
18. Aguilar-Ballester, M., Herrero-Cervera, A., Vinué, Á., 35. Banovich, N. E. et al. Impact of regulatory variation across human
Martínez-Hervás, S. & González-Navarro, H. Impact of cholesterol iPSCs and differentiated cells. Genome Res. 28, 122–131 (2018).
metabolism in immune cell function and atherosclerosis. 36. Ward, M. C., Banovich, N. E., Sarkar, A., Stephens, M. & Gilad, Y.
Nutrients 12, 2021 (2020). Dynamic effects of genetic variation on gene expression revealed
19. Suryadevara, V., Ramchandran, R., Kamp, D. W. & Natarajan, following hypoxic stress in cardiomyocytes. eLife 10, e57345
V. Lipid mediators regulate pulmonary fibrosis: potential (2021).
mechanisms and signaling pathways. Int. J. Mol. Sci. 21, 4257 37. Resztak, J. A. et al. Genetic control of the dynamic transcriptional
(2020). response to immune stimuli and glucocorticoids at single-cell
20. Sontake, V. et al. Wilms’ tumor 1 drives fibroproliferation and resolution. Genome Res. 33, 839–856 (2023).
myofibroblast transformation in severe fibrotic lung disease. 38. Bryois, J. et al. Cell-type-specific cis-eQTLs in eight human
JCI Insight 3, e121252 (2018). brain cell types identify novel risk genes for psychiatric and
21. Gajjala, P. R. et al. Dysregulated overexpression of Sox9 induces neurological disorders. Nat. Neurosci. 25, 1104–1112 (2022).
fibroblast activation in pulmonary fibrosis. JCI Insight 6, e152503 39. Nathan, A. et al. Single-cell eQTL models reveal dynamic T cell
(2021). state dependence of disease loci. Nature 606, 120–128 (2022).
22. Zhou, J. et al. microRNA-186 in extracellular vesicles from bone 40. Chakraborty, A., Mastalerz, M., Ansari, M., Schiller, H. B. &
marrow mesenchymal stem cells alleviates idiopathic pulmonary Staab-Weijnitz, C. A. Emerging roles of airway epithelial cells in
fibrosis via interaction with SOX4 and DKK1. Stem Cell Res. Ther. idiopathic pulmonary fibrosis. Cells 11, 1050 (2022).
12, 96 (2021).
23. Yazar, S. et al. Single-cell eQTL mapping identifies cell Publisher’s note Springer Nature remains neutral with regard to
type-specific genetic control of autoimmune disease. Science jurisdictional claims in published maps and institutional affiliations.
376, eabf3041 (2022).
24. Duckworth, A. et al. Telomere length and risk of idiopathic Open Access This article is licensed under a Creative Commons
pulmonary fibrosis and chronic obstructive pulmonary disease: Attribution 4.0 International License, which permits use, sharing,
a Mendelian randomisation study. Lancet Respir. Med. 9, 285–294 adaptation, distribution and reproduction in any medium or format,
(2021). as long as you give appropriate credit to the original author(s) and the
25. Sakaue, S. et al. A cross-population atlas of genetic associations source, provide a link to the Creative Commons licence, and indicate
for 220 human phenotypes. Nat. Genet. 53, 1415–1424 (2021). if changes were made. The images or other third party material in this
26. Buniello, A. et al. The NHGRI-EBI GWAS Catalog of published article are included in the article’s Creative Commons licence, unless
genome-wide association studies, targeted arrays and summary indicated otherwise in a credit line to the material. If material is not
statistics 2019. Nucleic Acids Res. 47, D1005–D1012 (2019). included in the article’s Creative Commons licence and your intended
27. Peljto, A. L. et al. The MUC5B promoter polymorphism is use is not permitted by statutory regulation or exceeds the permitted
associated with idiopathic pulmonary fibrosis in a Mexican cohort use, you will need to obtain permission directly from the copyright
but is rare among Asian ancestries. Chest 147, 460–464 (2015). holder. To view a copy of this licence, visit http://creativecommons.
28. Ferreira, M. A. R. et al. Genetic architectures of childhood- and org/licenses/by/4.0/.
adult-onset asthma are partly distinct. Am. J. Hum. Genet. 104,
665–684 (2019). © The Author(s) 2024, corrected publication 2024
1Translational Genomics Research Institute, Phoenix, AZ, USA. 2St. Vincent’s Institute of Medical Research, Melbourne, Victoria, Australia. 3Melbourne
Integrative Genomics, University of Melbourne, Melbourne, Victoria, Australia. 4Division of Allergy, Pulmonary and Critical Care Medicine, Department of
Medicine, Vanderbilt University Medical Center, Nashville, TN, USA. 5School of Mathematics and Statistics, Faculty of Science, University of Melbourne,
Melbourne, Victoria, Australia. 6Flow Cytometry Shared Resource, Vanderbilt University Medical Center, Nashville, TN, USA. 7Department of Cell and
Developmental Biology, Vanderbilt University, Nashville, TN, USA. 8Department of Veterans Affairs Medical Center, Nashville, TN, USA. 9Department
of Pathology, Microbiology and Immunology, Vanderbilt University Medical Center, Nashville, TN, USA. 10Department of Cardiac Surgery, Vanderbilt
University Medical Center, Nashville, TN, USA. 11Department of Thoracic Disease and Transplantation, Norton Thoracic Institute, Phoenix, AZ, USA.
12These authors contributed equally: Heini M. Natri, Christina B. Azodi. 13These authors jointly supervised this work: Jonathan A. Kropski, Davis J. McCarthy,
Nicholas E. Banovich. e-mail: nbanovich@tgen.org
Nature Genetics | Volume 56 | April 2024 | 595–604 604

Article https://doi.org/10.1038/s41588-024-01702-0
Methods features were identified for each object and integration features across
Compliance with ethical regulations objects were selected with SelectIntegrationFeatures(); data in each
This study was approved by the local institutional review boards (IRBs) batch-specific object was scaled and underwent PCA dimensionality
(Vanderbilt IRB nos. 060165 and 171657; Western IRB no. 20181836). reduction using 2,000 variable features. rPCA integration was car-
Written informed consent was obtained from all participants. ried out using 3,000 integration anchors and four reference batches
(6, 12, 18, 24). PCA dimensionality reduction on the integrated data was
Participants, samples and tissue processing performed using 3,000 variable features. To determine the optimal
The scRNA-seq data presented in this article include previously pub- number of principal components to identify neighbors and to con-
lished41 and unpublished samples (Supplementary Table 1). Lung tissue struct the uniform manifold approximation (UMAP), we determined
samples were processed as described previously by Habermann et al.8. the difference between the variation explained by each principal com-
Briefly, ILD tissue samples were obtained from lungs removed at the ponent and the subsequent principal component and identified the
time of lung transplantation at either the Vanderbilt University Medi- last point where the percentage change was more than 0.1%. A shared
cal Center (VUMC) or the National Thoracic Institute. Control tissue nearest neighbor graph was constructed with k = 20; clusters of cells
samples were obtained from lungs declined for organ donation either were identified using the modularity optimization-based clustering
at the Donor Network of Arizona or VUMC. Tissue sections were taken algorithm43 implemented in Seurat v.4.
from multiple peripheral (within ~2 cm of the pleural surface) regions The resulting clusters were divided into four major cell subgroups
in each lung. For ILD-affected lungs, representatively diseased areas based on marker gene expression: PTPRC+ for immune cells; EPCAM+
were selected on the basis of preoperative chest computed tomogra- for epithelial cells; PECAM1/+PTPRC− for endothelial cells; and PTPRC−/
phy, while for control lungs, the most normal-appearing region was EPCAM−/PECAM1− for mesenchymal cells. Each subgroup-specific
identified by gross inspection and selected for biopsy. For ILD-affected object underwent the same dimensionality reduction and cluster-
lungs, diagnoses were determined according to the American Thoracic ing approach as described above. We removed doubles using a man-
Society/European Respiratory Society consensus criteria42. No statis- ual approach, as described previously8,41, by identifying clusters of
tical methods were used to predetermine sample sizes but inclusion cells that expressed markers from multiple lineages8,41. Our previous
thresholds were determined to maximize the ability to map eQTLs with work found this method to be more conservative than automated
confidence across many cell types (Supplementary Note 2). Studies approaches. Indeed, when applying DoubletFinder v.2.0 (ref. 44) to
were approved by the local IRBs. one lineage (epithelial cells), DoubletFinder recovered 8,230 dou-
Tissue samples were digested in either collagenase I/dispase II blets (3.7%), whereas the marker-based approach identified 18,588
(1 μg ml−1) or Miltenyi Multi Tissue Dissociation Kit using a gentleMACS doublets (8.5%). After manual doublet removal and reclustering,
Octo Dissociator (Miltenyi Biotec). Tissue lysates were serially filtered subgroup-specific objects were further annotated for specific cell
through sterile gauze, 100-μm and 40-μm sterile filters (Fischer). The types based on known marker genes (Supplementary Table 2).
resulting suspensions then underwent cell sorting using serial columns For differential gene expression testing, we used the R/presto
(Miltenyi MicroBeads, CD235a and CD45) or fluorescence-activated implementation of the Wilcoxon rank-sum test (wilcoxauc)45.
cell sorting at VUMC or the Translational Genomics Research Institute
(TGen). CD45− and C45+ populations were mixed 2:1 in samples processed Low-pass WGS, genotyping and imputation
at VUMC and used to generate the scRNA-seq libraries. At TGen, calcein Flash-frozen tissue in DNA/RNA Shield was homogenized using a bullet
acetoxymethyl was used to stain live cells; 10,000–15,000 live cells blender. Genomic DNA was extracted using the Zymo Quick-DNA/RNA
were sorted directly into the 10X reaction buffer and transferred to the Microprep Plus Kit. Library preparation and low-pass WGS were carried
10× 5′ chip A (10X Genomics). out at TGen or by Gencove (Supplementary Table 9). At TGen, libraries
were prepared using PCR-free Watchmaker Kits (Watchmaker Genom-
scRNA-seq library preparation and next-generation ics) with a 200-ng input. Genomes were sequenced on a NovaSeq sys-
sequencing tem at low coverage (typically 0.4–1×). The resulting sequenced data
scRNA-seq libraries were generated using the 10X Chromium plat- were processed and imputed using Gencove’s imputation platform.
form 5′ library preparation kits (10X Genomics) according to the
manufacturer’s recommendations and targeting 5,000–10,000 cells Pseudobulk cell type eQTL mapping
per sample. From 12 donors, multiple tissue samples were processed For eQTL mapping, cells with more than 20% of reads mapping to the
and libraries were generated from separate biopsies taken from the mitochondrial genes were removed (466,989 cells remained). Mapping
same lung to account for regional heterogeneity (Supplementary was only performed on cell types with at least 40 donors with at least
Table 1). Next-generation sequencing was carried out on an Illumina 5 cells of that cell type (38 cell types met these criteria). Mitochon-
NovaSeq 6000 or HiSeq 4000. The resulting sequenced data were drial genes, genes encoding ribosomal proteins (downloaded from
filtered to retain reads with a read quality greater than 3; CellRanger https://www.genenames.org/cgi-bin/genegroup/download?id=1054
Count v.3.0.2 (10X Genomics) was used to align reads onto the GRCh38 &type=branch), genes expressed in less than 10% of cells in the study
reference genome. and genes with a mean count across all cells less than 0.1 were excluded,
resulting in 6,995 genes for eQTL mapping.
Data integration, clustering, cell type annotation and Pseudobulk cis-eQTL mapping was performed according to the
differential expression guidelines by Cuomo et al.11. For each cell type, raw counts were normal-
scRNA-seq data were processed and analyzed using Seurat v.4 ized and log-transformed using scran46 and mean-aggregated to get a
2
(ref. 10). CellRanger Count outputs were imported to create a Seurat single value for each gene for each donor for each cell type. Donors with
object for each sample. The sample-specific objects were merged fewer than five cells for a cell type were excluded from eQTL mapping
and the proportions of reads arising from mitochondrial genes were for that cell type; only cell types with at least 40 donors matching this
calculated for each sample. The merged object was filtered to retain criteria were included (maximum donors = 113). Biallelic, autosomal
samples with more than 1,000 identified features or less than 25% of SNPs were filtered to include SNPs with an MAF greater than 5%, Hardy–
mitochondrial reads. Weinberg equilibrium P > 1 × 10−6, and further pruned to remove highly
Samples sequenced across 24 batches were integrated using recip- correlated SNPs (--indep-pairwise 250 50 0.9) using plink2 (ref. 47),
rocal PCA (rPCA) as follows: the merged object was split by flowcell and resulting in ~1.9 million SNPs. We tested for associations for SNPs within
the count data in each batch-specific object was normalized; variable 1 Gb upstream and downstream of the gene body.
Nature Genetics

Article https://doi.org/10.1038/s41588-024-01702-0
Linear mixed models were used to map cis-eQTLs using the LIMIX_ Disease interaction cell-type eQTL mapping
qtl framework (https://github.com/single-cell-genetics/LIMIX_qtl)48. To test for disease interaction eQTL effects, cell types were required to
Expression levels for each gene were quantile-normalized to fit a nor- have at least ten control and ten ILD donors with at least five cells of that
mal distribution (--gaussianize_method). To control for unwanted cell type, resulting in KRT5−KRT17+, pDC, cDC1, alveolar fibroblast and
technical effects, the first 20 cell-type expression principal compo- mesothelial cell types being excluded from the interaction eQTL analy-
nents were regressed out before model fitting (--regress_covariates). sis. SNPs were further filtered to remove those with an MAF < 5% in either
To account for variance due to population structure, we included the control or ILD donor populations (1.77 million SNPs remained).
the identity-by-descent relationship matrix generated by apply- Interaction effects were tested using the run_interaction_QTL_analysis
ing plink2--make-rel on the filtered SNP data as a random effect. To from LIMIX_qtl. Random effects were handled as described above for
account for differences in cell type abundance across donors, we the eQTL mapping analysis. In the interaction term with SNP effect, we
included the number of cells aggregated (1/nCells) as a second ran- included the binary disease status (ILD versus unaffected). Fixed effects
dom effect, using the random effect weighting approach described by (for 20 principal components) were included but not regressed out
Cuomo et al.11. Random effects were marginalized from the model before modeling because disease status was strongly correlated with
using the low-rank optimization method (--low_rank_random_effect) some principal components. The results from this analysis were pro-
described by Cuomo et al.49. cessed using mashr, with significance calling, as described above, for
the eQTL analysis. For each cell type, we further pruned int-eQTLs to
Joint cell-type eQTL analysis retain associations where the observed eSNP MAF for individuals with
Joint analysis of the LIMIX estimated effect sizes and their correspond- ILD and unaffected donors for the given cell type was greater than 0.05.
ing standard errors across all 38 cell types was performed using mul-
tivariate adaptive shrinkage in R (mashr v.0.2 (ref. 12)) according to Colocalization with GWAS and GTEx
the approach outlined in the ‘eQTL analysis outline’ vignette from the Colocalization analysis was carried out between the cell type eQTL,
authors (https://stephenslab.github.io/mashr/articles/eQTL_outline. GTEx lung eQTL and three IPF GWAS. The UKBB24 and East Asian25 IPF
html). In this approach, a weighted combination of learned and canoni- GWAS summary statistics were downloaded from the GWAS Catalog26.
cal covariance matrices that describe patterns of eQTL sparsity and The discovery samples of these studies consisted of 1,369 cases with IPF,
sharing across cell types is used as a prior for generating adjusted sum- 14,103 cases with chronic obstructive pulmonary disease and 435,866
mary statistics. The data-driven covariance matrices were estimated controls, and 1,046 cases with East Asian ancestry and 176,974 controls,
from a subset of strong associations with an LFSR lower than 0.1 in at respectively. Summary statistics from an IPF GWAS meta-analysis9
least one cell type (n = 487), calculated using adaptive shrinkage in R leveraging data from three studies51–53 were downloaded after gaining
(ashr v.2.2 (ref. 50)). Default canonical covariance matrices were used, access by submitting a request (https://github.com/genomicsITER/
representing equal effect sharing across cell types, the top five principal PFgenetics)54. The meta-analysis consisted of 2,668 cases with IPF with
components from the strong associations and extreme deconvolution European ancestry and 8,591 controls.
matrices obtained from those principal components. The model was Additionally, GWAS on adult-onset and childhood-onset asthma28
fitted to a random subset of 10,000 SNP–gene associations and then (26,582 adult cases with European ancestry, 13,962 child cases and
applied to all associations tested. 300,671 controls) were downloaded from the GWAS Catalog and
included for comparison. For comparative analyses with bulk eQTL,
Assessing significance, sharing and eQTL classification GTEx lung, whole-blood and brain cortex eQTLs, summary statistics
The LFSR calculated by mashr was used to assess significance. To were downloaded from the GTEx Google Cloud bucket (https://console.
further reduce the impact of differential power on assessing shar- cloud.google.com/storage/browser/gtex-resources)55.
ing of eQTLs across cell types, if an eQTL was significant in one cell Bayesian colocalization analysis was performed using R/coloc v.5
type (LFSR ≤ 0.05), then it would be considered significant in other (ref. 56). For the pseudobulk cell-type eQTLs, mashr LFSR was used in
cell types at a less stringent threshold (LFSR ≤ 0.1). An eQTL was con- place of the nominal eQTL P value. A total of 2,092 genes, including
sidered shared in a pairwise comparison between two cell types if the multi-cell-type eQTLs presented in Fig. 4 and 103 IPF GWAS variant
the eQTL was significant in both cell types and the estimated effect flanking genes, were selected for the colocalization analysis; for each
size was within a factor of 0.5. An eQTL was classified as global if it gene, colocalization testing was carried out between datasets that
was significant in at least 36 of the 38 cell types (31 of 33 cell types for shared 100 or more variable (MAF > 0, <1) SNPs. Significantly colocal-
int-eQTLs). This two-cell-type buffer was included to reduce the impact ized loci were selected based on the posterior probability for a single
of low-powered cell types on our categorization. eQTLs that were shared causal variant of 0.6 or greater.
significant in only one cell type were classified as unique and eQTLs
significant in 2–36 cell types (2–31 for int-eQTLs) were considered multi- Enrichment testing
cell-type eQTLs. We tested for the enrichment of the clusters of eQTLs in Fig. 4 among
To simplify plotting of the top eQTLs (Fig. 4), a pruning step was GO terms using a Fisher’s exact test as implemented in R/TopGO
included, where for each gene, if there was a single top eQTL, that v.2.46.0 (ref. 57). All genes included in the eQTL analysis were used
eQTL was retained. If there were two top eQTLs, the Euclidean distance as a background set. A P value threshold of 0.01 was used to select
between the centered absolute values of the estimated effect sizes significant terms.
across cell types for the two eQTLs were compared. If the distance was We used a Fisher’s exact test to test for the enrichment of the vari-
greater than the set threshold (distribution = 0.2), both were retained. ous classes of sc-eQTLs (all eQTLs, globally shared, multistate, unique
If the distance was less than the threshold then the one that was signifi- to a single cell type, k1–k7 in Fig. 4) among IPF GWAS risk variants. From
cant in more cell types was retained. Finally, if there were more than the 1,617,891 SNPs tested for in the eQTL analysis and included in the
three top eQTLs, the pairwise Euclidean distance between the centered IPF GWAS meta-analysis, a set of 473 GWAS variants was selected with
absolute values of the estimated effect sizes for each pair of top eQTLs a relaxed genome-wide nominal P value threshold of 1 × 10−6. A null
was calculated. If all pairwise distances were above the threshold, all distribution of nonsignificant eQTLs was generated using the default
were retained. Otherwise, hierarchical clustering was performed and rejection method of R/nullranges58 v.3.16 to match the observed distri-
the tree was cut using cutree at a k between 2 and 5, which maximized bution of absolute distances to the TSS among the significant eQTLs.
the silhouette width. For each cluster, the top eQTL that was significant To test whether the various classes of regulatory variants detected
in most cell types was retained. in the sc-eQTL analyses disrupted the binding of known transcription
Nature Genetics

Article https://doi.org/10.1038/s41588-024-01702-0
factors, we used HOMER59 v.4.11 to analyze eQTL positions for the 53. Noth, I. et al. Genetic variants associated with idiopathic
enrichment of transcription factor binding site motifs. findMotif- pulmonary fibrosis susceptibility and mortality: a genome-wide
sGenome.pl with a default region size of 200 bp was used to detect association study. Lancet Respir. Med. 1, 309–317 (2013).
enriched motifs. In each analysis, a null set of nonsignificant eQTLs 54. Genomics ITER. PFgenetics. GitHub https://github.com/
with a matched distribution of distances to the TSS was used as a genomicsITER/PFgenetics (2019).
background. In the TFBS enrichment analysis of the int-eQTLs, the 55. gtex-resources. Google Cloud https://console.cloud.google.com/
non-int-eQTLs were used as a background set. A q-value threshold of storage/browser/gtex-resources (2023).
0.05 was used to select significant motifs. 56. Wallace, C. A more accurate method for colocalisation analysis
allowing for multiple causal variants. PLoS Genet. 17, e1009440
Statistics and reproducibility (2021).
The statistical analyses are detailed in the Methods and figure legends 57. Alexa, A. & Rahnenfuhrer J. topGO: Enrichment analysis for
and were performed using R v.4.1.1 and v.4.3.0. gene ontology. Bioconductor release 3.18. Bioconductor
https://bioconductor.org/packages/release/bioc/html/topGO.
Reporting summary html (2017).
Further information on research design is available in the Nature 58. Davis, E. S. et al. matchRanges: generating null hypothesis
Portfolio Reporting Summary linked to this article. genomic ranges via covariate-matched sampling. Bioinformatics
39, btad197 (2023).
Data availability 59. Heinz, S. et al. Simple combinations of lineage-determining
Raw and processed 10X Genomics data, Seurat objects, mean-aggregated transcription factors prime cis-regulatory elements required for
expression matrices and genome-wide LIMIX and mashr eQTL statistics macrophage and B cell identities. Mol. Cell 38, 576–589 (2010).
can be found on the Gene Expression Omnibus under accession no. 60. Natri, H. M. et al. Banovich-Lab/ILD_eQTL: Original release: Nat
GSE227136. Genotype data are available on the database of Genotypes Genet analysis. Zenodo https://doi.org/10.5281/zenodo.10459632
and Phenotypes under accession no. phs003521. (2024).
Code availability Acknowledgements
The code to reproduce the results presented in this study is available We thank the Tennessee Donor Services and the Donor Network of
via Zenodo at https://doi.org/10.5281/zenodo.10459632 (ref. 60). Arizona and the patients and families who donated tissue samples
to make these studies possible. This study was supported by a
References National Heart, Lung, and Blood Institute grant no. R01HL145372 and a
41. Bui, L. T. et al. Chronic lung diseases are associated with gene Department of Defense award no. W81XWH1910416 to N.E.B. and J.A.K.;
expression programs favoring SARS-CoV-2 entry and severity. Nat. grant no. P01HL092870 to T.S.B.; grant no. K08HL136888 to C.M.S.;
Commun. 12, 4314 (2021). NHGRI grant no. R01HG011886 to N.E.B., D.J.M. and J.A.K.; the Doris
42. Travis, W. D. et al. An official American Thoracic Society/European Duke Charitable Foundation to J.A.K. and N.E.B.; National Health and
Respiratory Society statement: update of the international Medical Research Council grant nos. GNT1195595 and GNT1162829
multidisciplinary classification of the idiopathic interstitial to D.J.M.; and National Institutes of Health grant nos. R01HL158906
pneumonias. Am. J. Respir. Crit. Care Med. 188, 733–748 (2013). and R01HL126176 to L.B.W. The Vanderbilt Flow Cytometry Shared
43. Waltman, L. & van Eck, N. J. A smart local moving algorithm for Resource is supported by the Vanderbilt Ingram Cancer Center (P30
large-scale modularity-based community detection. Eur. Phys. J. CA068485) and the Vanderbilt Digestive Disease Research Center
86, 471 (2013). (DK058404). Additional support was provided by the Vanderbilt
44. McGinnis, C. S., Murrow, L. M. & Gartner, Z. J. DoubletFinder: Institute of Clinical and Translational Research (UL1 TR002243).
doublet detection in single-cell RNA sequencing data using
artificial nearest neighbors. Cell Syst. 8, 329–337 (2019). Author contributions
45. Korsunsky, I., Nathan, A., Millard, N. & Raychaudhuri, S. Presto N.E.B., D.J.M., J.A.K., H.M.N. and C.B.D.A. conceptualized the study.
scales Wilcoxon and auROC analyses to millions of observations. C.B.D.A. devised the methodology. H.M.N. and C.B.D.A. carried out the
Preprint at bioRxiv https://doi.org/10.1101/653253 (2019). formal analysis. H.M.N., C.B.D.A., M.C., L.P., C.J.T., S.C. and R.K. carried
46. Lun, A. T. L., McCarthy, D. J. & Marioni, J. C. A step-by-step out the investigation. N.E.B., D.J.M., J.A.K., L.B.W., R.W., T.S.B., C.M.S.,
workflow for low-level analysis of single-cell RNA-seq data with D.K.F., B.K.M., M.B. and C.L.C. managed the resources. H.M.N., C.B.D.A.
Bioconductor. F1000Res. 5, 2122 (2016). and L.P. curated the data. H.M.N., C.B.D.A., N.E.B., D.J.M. and J.A.K.
47. Purcell, S. et al. PLINK: a tool set for whole-genome association wrote the original manuscript draft. H.M.N., C.B.D.A., N.E.B., D.J.M.
and population-based linkage analyses. Am. J. Hum. Genet. 81, and J.A.K. reviewed and edited the manuscript. H.M.N. and C.B.D.A.
559–575 (2007). visualized the data. N.E.B., D.J.M. and J.A.K. supervised the study.
48. Lippert, C., Casale, F. P., Rakitsch, B. & Stegle, O. LIMIX: genetic N.E.B., D.J.M., J.A.K., L.B.W., D.K.F. and B.K.M. acquired the funding.
analysis of multiple traits. Preprint at bioRxiv https://doi.org/
10.1101/003905 (2014). Competing interests
49. Cuomo, A. S. E. et al. CellRegMap: a statistical framework for J.A.K. reports advisory board fees from Boehringer Ingelheim,
mapping context-specific regulatory variants using scRNA-seq. nonfinancial study support from Genentech and grant funding from
Mol. Syst. Biol. 18, e10663 (2022). Boehringer Ingelheim. N.E.B. reports consulting fees from Deepcell.
50. Stephens, M. False discovery rates: a new deal. Biostatistics 18, L.B.W. has received advisory board fees from CSL Behring, Quark,
275–294 (2017). Bayer and Merck, and has research contracts with Genentech and CSL
51. Peljto, A. L. et al. Association between the MUC5B promoter Behring. T.S.B. reports consulting fees from Orinove, GRI Bio, Morphic
polymorphism and survival in patients with idiopathic pulmonary and Novelstar Pharmaceuticals, research grants and contracts from
fibrosis. JAMA 309, 2232–2239 (2013). Boehringer Ingelheim and Celgene, and nonfinancial study support
52. Fingerlin, T. E. et al. Genome-wide association study identifies from Genentech. R.W. reports consultant fees from Genentech and
multiple susceptibility loci for pulmonary fibrosis. Nat. Genet. 45, Boehringer Ingelheim. The remaining authors declare no competing
613–620 (2013). interests.
Nature Genetics

Article https://doi.org/10.1038/s41588-024-01702-0
Additional information Peer review information Nature Genetics thanks Nick Shrine and the
Supplementary information The online version contains supplementary other, anonymous, reviewer(s) for their contribution to the peer review
material available at https://doi.org/10.1038/s41588-024-01702-0. of this work. Peer reviewer reports are available.
Correspondence and requests for materials should be addressed to Reprints and permissions information is available at
Nicholas E. Banovich. www.nature.com/reprints.
Nature Genetics

(cid:4)(cid:1)(cid:11)(cid:13)(cid:10)(cid:14)(cid:8)(cid:5)(cid:9)(cid:12)(cid:6)(cid:3)(cid:2)(cid:7)(cid:14)
(cid:47)(cid:79)(cid:67)(cid:77)(cid:94)(cid:84)(cid:63)(cid:104)(cid:123)(cid:37)(cid:123)(cid:31)(cid:63)(cid:91)(cid:94)(cid:111)(cid:79)(cid:67)(cid:77)(cid:123)
(cid:33)(cid:95)(cid:101)(cid:101)(cid:71)(cid:105)(cid:97)(cid:95)(cid:92)(cid:69)(cid:80)(cid:92)(cid:75)(cid:123)(cid:64)(cid:109)(cid:107)(cid:78)(cid:95)(cid:101)(cid:120)(cid:105)(cid:5)(cid:27)(cid:123) (cid:91)(cid:65)(cid:63)(cid:91)(cid:94)(cid:111)(cid:79)(cid:67)(cid:77)(cid:29)(cid:108)(cid:76)(cid:72)(cid:91)(cid:12)(cid:94)(cid:102)(cid:76)(cid:123)
(cid:1)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:3)
(cid:43)(cid:64)(cid:105)(cid:107)(cid:123)(cid:109)(cid:97)(cid:69)(cid:64)(cid:107)(cid:71)(cid:69)(cid:123)(cid:66)(cid:116)(cid:123)(cid:64)(cid:109)(cid:107)(cid:78)(cid:95)(cid:101)(cid:121)(cid:105)(cid:5)(cid:27)(cid:123)(cid:58)(cid:96)(cid:59)(cid:67)(cid:108)(cid:25)(cid:59) (cid:8)(cid:15) (cid:59)(cid:22)(cid:20)(cid:59)(cid:22)(cid:59)(cid:23)(cid:60)(cid:123) (cid:60)(cid:60)(cid:60)(cid:60)(cid:60)(cid:60)(cid:60)(cid:60)(cid:60)(cid:61)(cid:123) (cid:123)
(cid:1)(cid:4)(cid:10)(cid:9)(cid:11)(cid:12)(cid:6)(cid:8)(cid:5)(cid:15)(cid:2)(cid:13)(cid:7)(cid:7)(cid:3)(cid:11)(cid:14)(cid:15)
(cid:48)(cid:64)(cid:107)(cid:109)(cid:101)(cid:71)(cid:123)(cid:50)(cid:95)(cid:101)(cid:107)(cid:73)(cid:95)(cid:85)(cid:80)(cid:95)(cid:123)(cid:113)(cid:80)(cid:105)(cid:78)(cid:71)(cid:105)(cid:123)(cid:107)(cid:95)(cid:123)(cid:80)(cid:89)(cid:97)(cid:101)(cid:95)(cid:112)(cid:71)(cid:123)(cid:107)(cid:78)(cid:71)(cid:123)(cid:101)(cid:71)(cid:97)(cid:101)(cid:95)(cid:69)(cid:109)(cid:68)(cid:80)(cid:66)(cid:80)(cid:85)(cid:80)(cid:107)(cid:116)(cid:123)(cid:95)(cid:73)(cid:123)(cid:107)(cid:78)(cid:71)(cid:123)(cid:113)(cid:95)(cid:101)(cid:82)(cid:123)(cid:107)(cid:78)(cid:64)(cid:107)(cid:123)(cid:113)(cid:71)(cid:123)(cid:97)(cid:109)(cid:66)(cid:85)(cid:80)(cid:105)(cid:78)(cid:13)(cid:123)(cid:55)(cid:78)(cid:80)(cid:105)(cid:123)(cid:73)(cid:95)(cid:101)(cid:89)(cid:123)(cid:97)(cid:101)(cid:95)(cid:112)(cid:80)(cid:69)(cid:71)(cid:105)(cid:123)(cid:105)(cid:107)(cid:101)(cid:109)(cid:68)(cid:107)(cid:109)(cid:101)(cid:71)(cid:123)(cid:73)(cid:95)(cid:101)(cid:123)(cid:68)(cid:95)(cid:92)(cid:105)(cid:80)(cid:105)(cid:107)(cid:71)(cid:92)(cid:68)(cid:116)(cid:123)(cid:64)(cid:92)(cid:69)(cid:123)(cid:107)(cid:101)(cid:64)(cid:92)(cid:105)(cid:97)(cid:64)(cid:101)(cid:71)(cid:92)(cid:68)(cid:116)(cid:123)
(cid:80)(cid:92)(cid:123)(cid:101)(cid:71)(cid:97)(cid:95)(cid:101)(cid:107)(cid:80)(cid:92)(cid:75)(cid:13)(cid:123)(cid:39)(cid:95)(cid:101)(cid:123)(cid:73)(cid:109)(cid:101)(cid:107)(cid:78)(cid:71)(cid:101)(cid:123)(cid:80)(cid:92)(cid:73)(cid:95)(cid:101)(cid:89)(cid:64)(cid:107)(cid:80)(cid:95)(cid:92)(cid:123)(cid:95)(cid:92)(cid:123)(cid:48)(cid:64)(cid:107)(cid:109)(cid:101)(cid:71)(cid:123)(cid:50)(cid:95)(cid:101)(cid:107)(cid:73)(cid:95)(cid:85)(cid:80)(cid:95)(cid:123)(cid:97)(cid:95)(cid:85)(cid:80)(cid:68)(cid:80)(cid:71)(cid:105)(cid:9)(cid:123)(cid:105)(cid:71)(cid:71)(cid:123)(cid:95)(cid:109)(cid:101)(cid:123)(cid:38)(cid:69)(cid:80)(cid:107)(cid:95)(cid:101)(cid:80)(cid:64)(cid:85)(cid:123)(cid:50)(cid:95)(cid:85)(cid:80)(cid:68)(cid:80)(cid:71)(cid:105)(cid:123)(cid:64)(cid:92)(cid:69)(cid:123)(cid:107)(cid:78)(cid:71)(cid:123)(cid:38)(cid:69)(cid:80)(cid:107)(cid:95)(cid:101)(cid:80)(cid:64)(cid:85)(cid:123)(cid:50)(cid:95)(cid:85)(cid:80)(cid:68)(cid:117)(cid:123)(cid:33)(cid:78)(cid:71)(cid:68)(cid:82)(cid:85)(cid:80)(cid:105)(cid:107)(cid:13)(cid:123)
(cid:1)(cid:12)(cid:2)(cid:12)(cid:7)(cid:11)(cid:12)(cid:7)(cid:3)(cid:11)(cid:14)
(cid:39)(cid:95)(cid:101)(cid:123)(cid:64)(cid:85)(cid:85)(cid:123)(cid:105)(cid:107)(cid:64)(cid:107)(cid:80)(cid:105)(cid:107)(cid:80)(cid:68)(cid:64)(cid:85)(cid:123)(cid:64)(cid:92)(cid:64)(cid:85)(cid:116)(cid:105)(cid:71)(cid:105)(cid:9)(cid:123)(cid:68)(cid:95)(cid:92)(cid:73)(cid:80)(cid:101)(cid:89)(cid:123)(cid:107)(cid:78)(cid:64)(cid:107)(cid:123)(cid:107)(cid:78)(cid:71)(cid:123)(cid:73)(cid:95)(cid:85)(cid:85)(cid:95)(cid:113)(cid:80)(cid:92)(cid:75)(cid:123)(cid:80)(cid:107)(cid:71)(cid:89)(cid:105)(cid:123)(cid:64)(cid:101)(cid:71)(cid:123)(cid:97)(cid:101)(cid:71)(cid:105)(cid:71)(cid:92)(cid:107)(cid:123)(cid:80)(cid:92)(cid:123)(cid:107)(cid:78)(cid:71)(cid:123)(cid:73)(cid:80)(cid:75)(cid:109)(cid:101)(cid:71)(cid:123)(cid:85)(cid:71)(cid:75)(cid:71)(cid:92)(cid:69)(cid:9)(cid:123)(cid:107)(cid:64)(cid:66)(cid:85)(cid:71)(cid:123)(cid:85)(cid:71)(cid:75)(cid:71)(cid:92)(cid:69)(cid:9)(cid:123)(cid:89)(cid:64)(cid:80)(cid:92)(cid:123)(cid:107)(cid:71)(cid:115)(cid:107)(cid:9)(cid:123)(cid:95)(cid:101)(cid:123)(cid:45)(cid:71)(cid:107)(cid:78)(cid:95)(cid:69)(cid:105)(cid:123)(cid:105)(cid:71)(cid:68)(cid:107)(cid:80)(cid:95)(cid:92)(cid:13)(cid:123)
(cid:92)(cid:16)(cid:64)(cid:123) (cid:33)(cid:95)(cid:92)(cid:73)(cid:80)(cid:101)(cid:89)(cid:71)(cid:69)(cid:123)
(cid:1)(cid:3)(cid:2)(cid:3)
(cid:55)(cid:78)(cid:71)(cid:123)(cid:71)(cid:115)(cid:64)(cid:68)(cid:107)(cid:123)(cid:105)(cid:64)(cid:89)(cid:97)(cid:85)(cid:71)(cid:123)(cid:105)(cid:80)(cid:119)(cid:71)(cid:123)(cid:120)(cid:93)(cid:5)(cid:123)(cid:73)(cid:95)(cid:101)(cid:123)(cid:71)(cid:64)(cid:68)(cid:78)(cid:123)(cid:71)(cid:115)(cid:97)(cid:71)(cid:101)(cid:80)(cid:89)(cid:71)(cid:92)(cid:107)(cid:64)(cid:85)(cid:123)(cid:75)(cid:101)(cid:95)(cid:109)(cid:97)(cid:16)(cid:68)(cid:95)(cid:92)(cid:69)(cid:80)(cid:107)(cid:80)(cid:95)(cid:92)(cid:9)(cid:123)(cid:75)(cid:80)(cid:112)(cid:71)(cid:92)(cid:123)(cid:64)(cid:105)(cid:123)(cid:64)(cid:123)(cid:69)(cid:80)(cid:105)(cid:68)(cid:101)(cid:71)(cid:107)(cid:71)(cid:123)(cid:92)(cid:109)(cid:89)(cid:66)(cid:71)(cid:101)(cid:123)(cid:64)(cid:92)(cid:69)(cid:123)(cid:109)(cid:92)(cid:80)(cid:107)(cid:123)(cid:95)(cid:73)(cid:123)(cid:89)(cid:71)(cid:64)(cid:105)(cid:109)(cid:101)(cid:71)(cid:89)(cid:71)(cid:92)(cid:107)(cid:123)
(cid:1)(cid:3)(cid:2)(cid:3)
(cid:30)(cid:123)(cid:105)(cid:107)(cid:64)(cid:107)(cid:71)(cid:89)(cid:71)(cid:92)(cid:107)(cid:123)(cid:95)(cid:92)(cid:123)(cid:113)(cid:78)(cid:71)(cid:107)(cid:78)(cid:71)(cid:101)(cid:123)(cid:89)(cid:71)(cid:64)(cid:105)(cid:109)(cid:101)(cid:71)(cid:89)(cid:71)(cid:92)(cid:107)(cid:105)(cid:123)(cid:113)(cid:71)(cid:101)(cid:71)(cid:123)(cid:107)(cid:64)(cid:82)(cid:71)(cid:92)(cid:123)(cid:73)(cid:101)(cid:95)(cid:89)(cid:123)(cid:69)(cid:80)(cid:105)(cid:107)(cid:80)(cid:92)(cid:68)(cid:107)(cid:123)(cid:105)(cid:64)(cid:89)(cid:97)(cid:85)(cid:71)(cid:105)(cid:123)(cid:95)(cid:101)(cid:123)(cid:113)(cid:78)(cid:71)(cid:107)(cid:78)(cid:71)(cid:101)(cid:123)(cid:107)(cid:78)(cid:71)(cid:123)(cid:105)(cid:64)(cid:89)(cid:71)(cid:123)(cid:105)(cid:64)(cid:89)(cid:97)(cid:85)(cid:71)(cid:123)(cid:113)(cid:64)(cid:105)(cid:123)(cid:89)(cid:71)(cid:64)(cid:105)(cid:109)(cid:101)(cid:71)(cid:69)(cid:123)(cid:101)(cid:71)(cid:97)(cid:71)(cid:64)(cid:107)(cid:71)(cid:69)(cid:85)(cid:116)(cid:123)
(cid:1)
(cid:87)(cid:123)(cid:55)(cid:78)(cid:71)(cid:123)(cid:105)(cid:107)(cid:64)(cid:107)(cid:80)(cid:105)(cid:107)(cid:80)(cid:68)(cid:64)(cid:85)(cid:123)(cid:107)(cid:71)(cid:105)(cid:107)(cid:120)(cid:105)(cid:5)(cid:123)(cid:109)(cid:105)(cid:71)(cid:69)(cid:123)(cid:30)(cid:48)(cid:35)(cid:123)(cid:113)(cid:78)(cid:71)(cid:107)(cid:78)(cid:71)(cid:101)(cid:123)(cid:107)(cid:78)(cid:71)(cid:116)(cid:123)(cid:64)(cid:101)(cid:71)(cid:123)(cid:95)(cid:92)(cid:71)(cid:10)(cid:95)(cid:101)(cid:123)(cid:107)(cid:113)(cid:95)(cid:10)(cid:105)(cid:80)(cid:69)(cid:71)(cid:69)
(cid:35)(cid:36) (cid:7)(cid:22)(cid:20)(cid:33)(cid:36)(cid:12)(cid:23)(cid:21)(cid:21)(cid:23)(cid:22)(cid:36)(cid:28)(cid:14)(cid:27)(cid:28)(cid:27)(cid:36)(cid:27)(cid:17)(cid:23)(cid:29)(cid:20)(cid:13)(cid:36)(cid:11)(cid:14)(cid:36)(cid:13)(cid:14)(cid:27)(cid:12)(cid:26)(cid:18)(cid:11)(cid:14)(cid:13)(cid:36)(cid:27)(cid:23)(cid:20)(cid:14)(cid:20)(cid:33)(cid:36)(cid:11)(cid:33)(cid:36)(cid:22)(cid:10)(cid:21)(cid:14)(cid:4)(cid:36)(cid:13)(cid:14)(cid:27)(cid:12)(cid:26)(cid:18)(cid:11)(cid:14)(cid:36)(cid:21)(cid:23)(cid:26)(cid:14)(cid:36)(cid:12)(cid:23)(cid:21)(cid:24)(cid:20)(cid:14)(cid:32)(cid:36)(cid:28)(cid:14)(cid:12)(cid:17)(cid:22)(cid:18)(cid:25)(cid:29)(cid:14)(cid:27)(cid:36)(cid:18)(cid:22)(cid:36)(cid:28)(cid:17)(cid:14)(cid:36)(cid:6)(cid:14)(cid:28)(cid:17)(cid:23)(cid:13)(cid:27)(cid:36)(cid:27)(cid:14)(cid:12)(cid:28)(cid:18)(cid:23)(cid:22)(cid:2)(cid:36)
(cid:1)(cid:3)(cid:2)(cid:3)
(cid:30)(cid:123)(cid:69)(cid:71)(cid:105)(cid:68)(cid:101)(cid:80)(cid:97)(cid:107)(cid:80)(cid:95)(cid:92)(cid:123)(cid:95)(cid:73)(cid:123)(cid:64)(cid:85)(cid:85)(cid:123)(cid:68)(cid:95)(cid:112)(cid:64)(cid:101)(cid:80)(cid:64)(cid:107)(cid:71)(cid:105)(cid:123)(cid:107)(cid:71)(cid:105)(cid:107)(cid:71)(cid:69)(cid:123)
(cid:1)(cid:3)(cid:2)(cid:3)
(cid:30)(cid:123)(cid:69)(cid:71)(cid:105)(cid:68)(cid:101)(cid:80)(cid:97)(cid:107)(cid:80)(cid:95)(cid:92)(cid:123)(cid:95)(cid:73)(cid:123)(cid:64)(cid:92)(cid:116)(cid:123)(cid:64)(cid:105)(cid:105)(cid:109)(cid:89)(cid:97)(cid:107)(cid:80)(cid:95)(cid:92)(cid:105)(cid:123)(cid:95)(cid:101)(cid:123)(cid:68)(cid:95)(cid:101)(cid:101)(cid:71)(cid:68)(cid:107)(cid:80)(cid:95)(cid:92)(cid:105)(cid:9)(cid:123)(cid:105)(cid:109)(cid:68)(cid:78)(cid:123)(cid:64)(cid:105)(cid:123)(cid:107)(cid:71)(cid:105)(cid:107)(cid:105)(cid:123)(cid:95)(cid:73)(cid:123)(cid:92)(cid:95)(cid:101)(cid:89)(cid:64)(cid:85)(cid:80)(cid:107)(cid:116)(cid:123)(cid:64)(cid:92)(cid:69)(cid:123)(cid:64)(cid:69)(cid:81)(cid:109)(cid:105)(cid:107)(cid:89)(cid:71)(cid:92)(cid:107)(cid:123)(cid:73)(cid:95)(cid:101)(cid:123)(cid:89)(cid:109)(cid:85)(cid:107)(cid:80)(cid:97)(cid:85)(cid:71)(cid:123)(cid:68)(cid:95)(cid:89)(cid:97)(cid:64)(cid:101)(cid:80)(cid:105)(cid:95)(cid:92)(cid:105)(cid:123)
(cid:1)(cid:3)(cid:2)(cid:3)(cid:30)(cid:123)(cid:73)(cid:109)(cid:85)(cid:85)(cid:123)(cid:69)(cid:71)(cid:105)(cid:68)(cid:101)(cid:80)(cid:97)(cid:107)(cid:80)(cid:95)(cid:92)(cid:123)(cid:95)(cid:73)(cid:123)(cid:107)(cid:78)(cid:71)(cid:123)(cid:105)(cid:107)(cid:64)(cid:107)(cid:80)(cid:105)(cid:107)(cid:80)(cid:68)(cid:64)(cid:85)(cid:123)(cid:97)(cid:64)(cid:101)(cid:64)(cid:89)(cid:71)(cid:107)(cid:71)(cid:101)(cid:105)(cid:123)(cid:80)(cid:92)(cid:68)(cid:85)(cid:109)(cid:69)(cid:80)(cid:92)(cid:75)(cid:123)(cid:68)(cid:71)(cid:92)(cid:107)(cid:101)(cid:64)(cid:85)(cid:123)(cid:107)(cid:71)(cid:92)(cid:69)(cid:71)(cid:92)(cid:68)(cid:116)(cid:123)(cid:120)(cid:71)(cid:13)(cid:75)(cid:13)(cid:123)(cid:89)(cid:71)(cid:64)(cid:92)(cid:105)(cid:5)(cid:123)(cid:95)(cid:101)(cid:123)(cid:95)(cid:107)(cid:78)(cid:71)(cid:101)(cid:123)(cid:66)(cid:64)(cid:105)(cid:80)(cid:68)(cid:123)(cid:71)(cid:105)(cid:107)(cid:80)(cid:89)(cid:64)(cid:107)(cid:71)(cid:105)(cid:123)(cid:120)(cid:71)(cid:13)(cid:75)(cid:13)(cid:123)(cid:101)(cid:71)(cid:75)(cid:101)(cid:71)(cid:105)(cid:105)(cid:80)(cid:95)(cid:92)(cid:123)(cid:68)(cid:95)(cid:71)(cid:73)(cid:73)(cid:80)(cid:68)(cid:80)(cid:71)(cid:92)(cid:107)(cid:5)
(cid:30)(cid:48)(cid:35)(cid:123)(cid:112)(cid:64)(cid:101)(cid:80)(cid:64)(cid:107)(cid:80)(cid:95)(cid:92)(cid:123)(cid:120)(cid:71)(cid:13)(cid:75)(cid:13)(cid:123)(cid:105)(cid:107)(cid:64)(cid:92)(cid:69)(cid:64)(cid:101)(cid:69)(cid:123)(cid:69)(cid:71)(cid:112)(cid:80)(cid:64)(cid:107)(cid:80)(cid:95)(cid:92)(cid:6)(cid:123)(cid:95)(cid:101)(cid:123)(cid:64)(cid:105)(cid:105)(cid:95)(cid:68)(cid:80)(cid:64)(cid:107)(cid:71)(cid:69)(cid:123)(cid:71)(cid:105)(cid:107)(cid:80)(cid:89)(cid:64)(cid:107)(cid:71)(cid:105)(cid:123)(cid:95)(cid:73)(cid:123)(cid:109)(cid:92)(cid:68)(cid:71)(cid:101)(cid:107)(cid:64)(cid:80)(cid:92)(cid:107)(cid:116)(cid:123)(cid:120)(cid:71)(cid:13)(cid:75)(cid:13)(cid:123)(cid:68)(cid:95)(cid:92)(cid:73)(cid:80)(cid:69)(cid:71)(cid:92)(cid:68)(cid:71)(cid:123)(cid:80)(cid:92)(cid:107)(cid:71)(cid:101)(cid:112)(cid:64)(cid:85)(cid:105)(cid:6)(cid:123)
(cid:1)
(cid:87)(cid:123) (cid:39)(cid:95)(cid:101)(cid:123)(cid:92)(cid:109)(cid:85)(cid:85)(cid:123)(cid:78)(cid:116)(cid:97)(cid:95)(cid:107)(cid:78)(cid:71)(cid:105)(cid:80)(cid:105)(cid:123)(cid:107)(cid:71)(cid:105)(cid:107)(cid:80)(cid:92)(cid:75)(cid:9)(cid:123)(cid:107)(cid:78)(cid:71)(cid:123)(cid:107)(cid:71)(cid:105)(cid:107)(cid:123)(cid:105)(cid:107)(cid:64)(cid:107)(cid:80)(cid:105)(cid:107)(cid:80)(cid:68)(cid:123)(cid:120)(cid:71)(cid:13)(cid:75)(cid:13)(cid:123)(cid:2)(cid:1)(cid:4)(cid:2)(cid:1)(cid:3)(cid:103)(cid:5)(cid:123)(cid:113)(cid:80)(cid:107)(cid:78)(cid:123)(cid:68)(cid:95)(cid:92)(cid:73)(cid:80)(cid:69)(cid:71)(cid:92)(cid:68)(cid:71)(cid:123)(cid:80)(cid:92)(cid:107)(cid:71)(cid:101)(cid:112)(cid:64)(cid:85)(cid:105)(cid:9)(cid:123)(cid:71)(cid:73)(cid:73)(cid:71)(cid:68)(cid:107)(cid:123)(cid:105)(cid:80)(cid:119)(cid:71)(cid:105)(cid:9)(cid:123)(cid:69)(cid:71)(cid:75)(cid:101)(cid:71)(cid:71)(cid:105)(cid:123)(cid:95)(cid:73)(cid:123)(cid:73)(cid:101)(cid:71)(cid:71)(cid:69)(cid:95)(cid:89)(cid:123)(cid:64)(cid:92)(cid:69)(cid:123)(cid:3)(cid:4)(cid:112)(cid:64)(cid:85)(cid:109)(cid:71)(cid:123)(cid:92)(cid:95)(cid:107)(cid:71)(cid:69)
(cid:35)(cid:36) (cid:5)(cid:18)(cid:30)(cid:14)(cid:36)(cid:8)(cid:36)(cid:30)(cid:10)(cid:20)(cid:29)(cid:14)(cid:27)(cid:36)(cid:10)(cid:27)(cid:36)(cid:14)(cid:32)(cid:10)(cid:12)(cid:28)(cid:36)(cid:30)(cid:10)(cid:20)(cid:29)(cid:14)(cid:27)(cid:36)(cid:31)(cid:17)(cid:14)(cid:22)(cid:14)(cid:30)(cid:14)(cid:26)(cid:36)(cid:27)(cid:29)(cid:18)(cid:28)(cid:10)(cid:11)(cid:20)(cid:14)(cid:3)(cid:36)
(cid:1)(cid:3)(cid:2)(cid:3)
(cid:39)(cid:95)(cid:101)(cid:123)(cid:32)(cid:64)(cid:116)(cid:71)(cid:105)(cid:80)(cid:64)(cid:92)(cid:123)(cid:64)(cid:92)(cid:64)(cid:85)(cid:116)(cid:105)(cid:80)(cid:105)(cid:9)(cid:123)(cid:80)(cid:92)(cid:73)(cid:95)(cid:101)(cid:89)(cid:64)(cid:107)(cid:80)(cid:95)(cid:92)(cid:123)(cid:95)(cid:92)(cid:123)(cid:107)(cid:78)(cid:71)(cid:123)(cid:68)(cid:78)(cid:95)(cid:80)(cid:68)(cid:71)(cid:123)(cid:95)(cid:73)(cid:123)(cid:97)(cid:101)(cid:80)(cid:95)(cid:101)(cid:105)(cid:123)(cid:64)(cid:92)(cid:69)(cid:123)(cid:45)(cid:64)(cid:101)(cid:82)(cid:95)(cid:112)(cid:123)(cid:68)(cid:78)(cid:64)(cid:80)(cid:92)(cid:123)(cid:45)(cid:95)(cid:92)(cid:107)(cid:71)(cid:123)(cid:33)(cid:64)(cid:101)(cid:85)(cid:95)(cid:123)(cid:105)(cid:71)(cid:107)(cid:107)(cid:80)(cid:92)(cid:75)(cid:105)(cid:123)
(cid:1)(cid:3)(cid:2)(cid:3)
(cid:39)(cid:95)(cid:101)(cid:123)(cid:78)(cid:80)(cid:71)(cid:101)(cid:64)(cid:101)(cid:68)(cid:78)(cid:80)(cid:68)(cid:64)(cid:85)(cid:123)(cid:64)(cid:92)(cid:69)(cid:123)(cid:68)(cid:95)(cid:89)(cid:97)(cid:85)(cid:71)(cid:115)(cid:123)(cid:69)(cid:71)(cid:105)(cid:80)(cid:75)(cid:92)(cid:105)(cid:9)(cid:123)(cid:80)(cid:69)(cid:71)(cid:92)(cid:107)(cid:80)(cid:73)(cid:80)(cid:68)(cid:64)(cid:107)(cid:80)(cid:95)(cid:92)(cid:123)(cid:95)(cid:73)(cid:123)(cid:107)(cid:78)(cid:71)(cid:123)(cid:64)(cid:97)(cid:97)(cid:101)(cid:95)(cid:97)(cid:101)(cid:80)(cid:64)(cid:107)(cid:71)(cid:123)(cid:85)(cid:71)(cid:112)(cid:71)(cid:85)(cid:123)(cid:73)(cid:95)(cid:101)(cid:123)(cid:107)(cid:71)(cid:105)(cid:107)(cid:105)(cid:123)(cid:64)(cid:92)(cid:69)(cid:123)(cid:73)(cid:109)(cid:85)(cid:85)(cid:123)(cid:101)(cid:71)(cid:97)(cid:95)(cid:101)(cid:107)(cid:80)(cid:92)(cid:75)(cid:123)(cid:95)(cid:73)(cid:123)(cid:95)(cid:109)(cid:107)(cid:68)(cid:95)(cid:89)(cid:71)(cid:105)(cid:123)
(cid:1)(cid:3)(cid:2)(cid:3)
(cid:38)(cid:105)(cid:107)(cid:80)(cid:89)(cid:64)(cid:107)(cid:71)(cid:105)(cid:123)(cid:95)(cid:73)(cid:123)(cid:71)(cid:73)(cid:73)(cid:71)(cid:68)(cid:107)(cid:123)(cid:105)(cid:80)(cid:119)(cid:71)(cid:105)(cid:123)(cid:3)(cid:71)(cid:13)(cid:75)(cid:13)(cid:123)(cid:33)(cid:95)(cid:78)(cid:71)(cid:92)(cid:1)(cid:105)(cid:123)(cid:2)(cid:1)(cid:3)(cid:50)(cid:71)(cid:64)(cid:101)(cid:105)(cid:95)(cid:92)(cid:2)(cid:105)(cid:123)(cid:103)(cid:5)(cid:9)(cid:123)(cid:80)(cid:92)(cid:69)(cid:80)(cid:68)(cid:64)(cid:107)(cid:80)(cid:92)(cid:75)(cid:123)(cid:78)(cid:95)(cid:113)(cid:123)(cid:107)(cid:78)(cid:71)(cid:116)(cid:123)(cid:113)(cid:71)(cid:101)(cid:71)(cid:123)(cid:68)(cid:64)(cid:85)(cid:68)(cid:109)(cid:85)(cid:64)(cid:107)(cid:71)(cid:69)(cid:123)
(cid:2)(cid:21)(cid:18)(cid:25)(cid:23)(cid:6)(cid:4)(cid:25)(cid:5)(cid:16)(cid:13)(cid:13)(cid:6)(cid:5)(cid:20)(cid:11)(cid:16)(cid:15)(cid:25)(cid:16)(cid:15)(cid:25)(cid:19)(cid:20)(cid:3)(cid:20)(cid:12)(cid:19)(cid:20)(cid:12)(cid:5)(cid:19)(cid:25)(cid:7)(cid:16)(cid:18)(cid:25)(cid:4)(cid:12)(cid:16)(cid:13)(cid:16)(cid:9)(cid:12)(cid:19)(cid:20)(cid:19)(cid:25)(cid:5)(cid:16)(cid:15)(cid:20)(cid:3)(cid:12)(cid:15)(cid:19)(cid:25)(cid:3)(cid:18)(cid:20)(cid:12)(cid:5)(cid:13)(cid:6)(cid:19)(cid:25)(cid:16)(cid:15)(cid:25)(cid:14)(cid:3)(cid:15)(cid:24)(cid:25)(cid:16)(cid:8)(cid:25)(cid:20)(cid:10)(cid:6)(cid:25)(cid:17)(cid:16)(cid:12)(cid:15)(cid:20)(cid:19)(cid:25)(cid:3)(cid:4)(cid:16)(cid:22)(cid:6)(cid:1)(cid:25)
(cid:1)(cid:9)(cid:6)(cid:12)(cid:13)(cid:2)(cid:10)(cid:5)(cid:14)(cid:2)(cid:8)(cid:4)(cid:14)(cid:3)(cid:9)(cid:4)(cid:5)(cid:14)
(cid:50)(cid:95)(cid:85)(cid:80)(cid:68)(cid:116)(cid:123)(cid:80)(cid:92)(cid:73)(cid:95)(cid:101)(cid:89)(cid:64)(cid:107)(cid:80)(cid:95)(cid:92)(cid:123)(cid:64)(cid:66)(cid:95)(cid:109)(cid:107)(cid:123)(cid:64)(cid:112)(cid:64)(cid:80)(cid:85)(cid:64)(cid:66)(cid:80)(cid:85)(cid:80)(cid:107)(cid:117)(cid:123)(cid:95)(cid:73)(cid:123)(cid:68)(cid:95)(cid:89)(cid:98)(cid:109)(cid:107)(cid:71)(cid:101)(cid:123)(cid:68)(cid:95)(cid:69)(cid:71)(cid:123)
(cid:35)(cid:64)(cid:107)(cid:64)(cid:123)(cid:68)(cid:95)(cid:85)(cid:85)(cid:71)(cid:68)(cid:107)(cid:80)(cid:95)(cid:92)(cid:123) (cid:8)(cid:26)(cid:23)(cid:30)(cid:18)(cid:13)(cid:14)(cid:36)(cid:10)(cid:36)(cid:13)(cid:14)(cid:27)(cid:12)(cid:26)(cid:18)(cid:24)(cid:28)(cid:18)(cid:23)(cid:22)(cid:36)(cid:23)(cid:15)(cid:36)(cid:10)(cid:20)(cid:20)(cid:36)(cid:12)(cid:23)(cid:21)(cid:21)(cid:14)(cid:26)(cid:12)(cid:18)(cid:10)(cid:20)(cid:1)(cid:36)(cid:23)(cid:24)(cid:14)(cid:22)(cid:36)(cid:27)(cid:23)(cid:29)(cid:26)(cid:12)(cid:14)(cid:36)(cid:10)(cid:22)(cid:13)(cid:36)(cid:12)(cid:29)(cid:27)(cid:28)(cid:23)(cid:21)(cid:36)(cid:12)(cid:23)(cid:13)(cid:14)(cid:36)(cid:29)(cid:27)(cid:14)(cid:13)(cid:36)(cid:28)(cid:23)(cid:36)(cid:12)(cid:23)(cid:20)(cid:20)(cid:14)(cid:12)(cid:28)(cid:36)(cid:28)(cid:17)(cid:14)(cid:36)(cid:13)(cid:10)(cid:28)(cid:10)(cid:36)(cid:18)(cid:22)(cid:36)(cid:28)(cid:17)(cid:18)(cid:27)(cid:36)(cid:27)(cid:28)(cid:29)(cid:13)(cid:34)(cid:1)(cid:36)(cid:27)(cid:24)(cid:14)(cid:12)(cid:19)(cid:33)(cid:18)(cid:22)(cid:16)(cid:36)(cid:28)(cid:17)(cid:14)(cid:36)(cid:30)(cid:14)(cid:26)(cid:27)(cid:18)(cid:23)(cid:22)(cid:36)(cid:29)(cid:27)(cid:14)(cid:13)(cid:36)(cid:7)(cid:9)(cid:36)
(cid:27)(cid:28)(cid:10)(cid:28)(cid:14)(cid:36)(cid:28)(cid:17)(cid:10)(cid:28)(cid:36)(cid:22)(cid:23)(cid:36)(cid:27)(cid:23)(cid:15)(cid:28)(cid:31)(cid:10)(cid:26)(cid:14)(cid:36)(cid:31)(cid:10)(cid:27)(cid:36)(cid:29)(cid:27)(cid:14)(cid:13)(cid:2)(cid:36)
(cid:1)(cid:2)
(cid:35)(cid:64)(cid:107)(cid:64)(cid:123)(cid:64)(cid:92)(cid:64)(cid:85)(cid:116)(cid:105)(cid:80)(cid:105)(cid:123) (cid:51)(cid:110)(cid:65)(cid:84)(cid:79)(cid:67)(cid:84)(cid:118)(cid:123)(cid:63)(cid:111)(cid:63)(cid:79)(cid:84)(cid:63)(cid:65)(cid:84)(cid:72)(cid:123)(cid:104)(cid:94)(cid:74)(cid:114)(cid:63)(cid:102)(cid:72)(cid:123)(cid:110)(cid:104)(cid:72)(cid:70)(cid:123)(cid:79)(cid:91)(cid:123)(cid:70)(cid:63)(cid:108)(cid:63)(cid:123)(cid:63)(cid:91)(cid:63)(cid:84)(cid:118)(cid:104)(cid:79)(cid:104)(cid:28)(cid:123)
(cid:34)(cid:72)(cid:84)(cid:84)(cid:53)(cid:63)(cid:91)(cid:76)(cid:72)(cid:102)(cid:123)(cid:34)(cid:94)(cid:110)(cid:91)(cid:108)(cid:123)(cid:111)(cid:23)(cid:14)(cid:20)(cid:14)(cid:22)(cid:123)
(cid:53)(cid:17)(cid:54)(cid:72)(cid:110)(cid:102)(cid:63)(cid:108)(cid:123)(cid:111)(cid:24)(cid:123)
(cid:99)(cid:84)(cid:79)(cid:91)(cid:83)(cid:22)(cid:123)(cid:111)(cid:86)(cid:14)(cid:20)(cid:26)(cid:123)
(cid:44)(cid:42)(cid:46)(cid:123)(cid:42)(cid:57)(cid:123)(cid:4)(cid:123)(cid:77)(cid:108)(cid:108)(cid:99)(cid:104)(cid:28)(cid:17)(cid:18)(cid:76)(cid:79)(cid:108)(cid:77)(cid:110)(cid:65)(cid:12)(cid:67)(cid:94)(cid:90)(cid:17)(cid:104)(cid:79)(cid:91)(cid:76)(cid:84)(cid:72)(cid:11)(cid:67)(cid:72)(cid:84)(cid:84)(cid:11)(cid:76)(cid:72)(cid:91)(cid:72)(cid:108)(cid:79)(cid:67)(cid:104)(cid:17)(cid:44)(cid:42)(cid:123)(cid:46)(cid:42)(cid:57)(cid:62)(cid:123)(cid:100)(cid:108)(cid:84)(cid:7)(cid:123)
(cid:53)(cid:17)(cid:90)(cid:63)(cid:104)(cid:77)(cid:102)(cid:123)(cid:111)(cid:20)(cid:12)(cid:22)(cid:123)
(cid:53)(cid:17)(cid:63)(cid:104)(cid:77)(cid:102)(cid:123)(cid:111)(cid:22)(cid:14)(cid:22)(cid:123)
(cid:53)(cid:17)(cid:67)(cid:94)(cid:84)(cid:94)(cid:67)(cid:123)(cid:111)(cid:106)(cid:123)
(cid:53)(cid:17)(cid:56)(cid:94)(cid:99)(cid:40)(cid:49)(cid:123)(cid:111)(cid:22)(cid:12)(cid:24)(cid:25)(cid:14)(cid:20)(cid:123)
(cid:53)(cid:17)(cid:91)(cid:110)(cid:84)(cid:84)(cid:102)(cid:63)(cid:91)(cid:76)(cid:72)(cid:104)(cid:123)(cid:111)(cid:23)(cid:12)(cid:21)(cid:25)(cid:123)
(cid:41)(cid:49)(cid:46)(cid:37)(cid:53)(cid:123)(cid:111)(cid:24)(cid:123)(cid:12)(cid:86)(cid:86)
(cid:34)(cid:110)(cid:104)(cid:108)(cid:94)(cid:90)(cid:123)(cid:104)(cid:67)(cid:102)(cid:79)(cid:99)(cid:108)(cid:104)(cid:123)(cid:108)(cid:94)(cid:123)(cid:102)(cid:72)(cid:99)(cid:102)(cid:94)(cid:70)(cid:110)(cid:67)(cid:72)(cid:123)(cid:108)(cid:77)(cid:72)(cid:123)(cid:102)(cid:72)(cid:104)(cid:110)(cid:84)(cid:108)(cid:123)(cid:99)(cid:102)(cid:72)(cid:104)(cid:72)(cid:91)(cid:108)(cid:72)(cid:70)(cid:123)(cid:77)(cid:72)(cid:102)(cid:72)(cid:123)(cid:63)(cid:102)(cid:72)(cid:123)(cid:63)(cid:111)(cid:63)(cid:79)(cid:84)(cid:63)(cid:65)(cid:84)(cid:72)(cid:123)(cid:94)(cid:91)(cid:123)(cid:40)(cid:79)(cid:108)(cid:41)(cid:110)(cid:65)(cid:123)(cid:63)(cid:108)(cid:123)(cid:77)(cid:108)(cid:108)(cid:99)(cid:104)(cid:28)(cid:19)(cid:17)(cid:76)(cid:79)(cid:108)(cid:77)(cid:110)(cid:65)(cid:14)(cid:67)(cid:94)(cid:90)(cid:17)(cid:108)(cid:76)(cid:72)(cid:91)(cid:17)(cid:65)(cid:63)(cid:91)(cid:94)(cid:111)(cid:79)(cid:67)(cid:77)(cid:84)(cid:63)(cid:65)(cid:17)(cid:108)(cid:102)(cid:72)(cid:72)(cid:17)(cid:90)(cid:63)(cid:104)(cid:108)(cid:72)(cid:102)(cid:17)(cid:123)
(cid:42)(cid:44)(cid:36)(cid:62)(cid:72)(cid:52)(cid:44)(cid:12)(cid:123)
(cid:1)(cid:2)
(cid:7)(cid:27)(cid:29)(cid:37)(cid:25)(cid:14)(cid:26)(cid:32)(cid:30)(cid:16)(cid:29)(cid:23)(cid:28)(cid:31)(cid:30)(cid:37)(cid:32)(cid:31)(cid:23)(cid:24)(cid:23)(cid:36)(cid:23)(cid:26)(cid:20)(cid:37)(cid:16)(cid:32)(cid:30)(cid:31)(cid:27)(cid:25)(cid:37)(cid:14)(cid:24)(cid:20)(cid:27)(cid:29)(cid:23)(cid:31)(cid:22)(cid:25)(cid:30)(cid:37)(cid:27)(cid:29)(cid:37)(cid:30)(cid:27)(cid:19)(cid:31)(cid:34)(cid:14)(cid:29)(cid:18)(cid:37)(cid:31)(cid:22)(cid:14)(cid:31)(cid:37)(cid:14)(cid:29)(cid:18)(cid:37)(cid:16)(cid:18)(cid:26)(cid:31)(cid:29)(cid:14)(cid:24)(cid:37)(cid:31)(cid:27)(cid:37)(cid:31)(cid:22)(cid:18)(cid:37)(cid:29)(cid:18)(cid:30)(cid:18)(cid:14)(cid:29)(cid:16)(cid:22)(cid:37)(cid:15)(cid:32)(cid:31)(cid:37)(cid:26)(cid:27)(cid:31)(cid:37)(cid:35)(cid:18)(cid:31)(cid:37)(cid:17)(cid:18)(cid:30)(cid:16)(cid:29)(cid:23)(cid:15)(cid:18)(cid:17)(cid:37)(cid:23)(cid:26)(cid:37)(cid:28)(cid:32)(cid:15)(cid:24)(cid:23)(cid:30)(cid:22)(cid:18)(cid:17)(cid:37)(cid:24)(cid:23)(cid:31)(cid:18)(cid:29)(cid:14)(cid:31)(cid:32)(cid:29)(cid:18)(cid:4)(cid:37)(cid:30)(cid:27)(cid:19)(cid:31)(cid:34)(cid:14)(cid:29)(cid:18)(cid:37)(cid:25)(cid:32)(cid:30)(cid:31)(cid:37)(cid:15)(cid:18)(cid:37)(cid:25)(cid:14)(cid:17)(cid:18)(cid:37)(cid:14)(cid:33)(cid:14)(cid:23)(cid:24)(cid:14)(cid:15)(cid:24)(cid:18)(cid:37)(cid:31)(cid:27)(cid:37)(cid:18)(cid:17)(cid:23)(cid:31)(cid:27)(cid:29)(cid:30)(cid:37)(cid:14)(cid:26)(cid:17)(cid:37)
(cid:29)(cid:18)(cid:33)(cid:23)(cid:18)(cid:34)(cid:18)(cid:29)(cid:30)(cid:5)(cid:37)(cid:13)(cid:18)(cid:37)(cid:30)(cid:31)(cid:29)(cid:27)(cid:26)(cid:20)(cid:24)(cid:35)(cid:37)(cid:18)(cid:26)(cid:16)(cid:27)(cid:32)(cid:29)(cid:14)(cid:20)(cid:18)(cid:37)(cid:16)(cid:27)(cid:17)(cid:18)(cid:37)(cid:17)(cid:18)(cid:28)(cid:27)(cid:30)(cid:23)(cid:31)(cid:23)(cid:27)(cid:26)(cid:37)(cid:23)(cid:26)(cid:37)(cid:14)(cid:37)(cid:16)(cid:27)(cid:25)(cid:25)(cid:32)(cid:26)(cid:23)(cid:31)(cid:35)(cid:37)(cid:29)(cid:18)(cid:28)(cid:27)(cid:30)(cid:23)(cid:31)(cid:27)(cid:29)(cid:35)(cid:37)(cid:2)(cid:18)(cid:6)(cid:20)(cid:6)(cid:37)(cid:8)(cid:23)(cid:31)(cid:9)(cid:32)(cid:15)(cid:3)(cid:5)(cid:37)(cid:12)(cid:18)(cid:18)(cid:37)(cid:31)(cid:22)(cid:18)(cid:37)(cid:10)(cid:14)(cid:31)(cid:32)(cid:29)(cid:18)(cid:37)(cid:11)(cid:27)(cid:29)(cid:31)(cid:19)(cid:27)(cid:24)(cid:23)(cid:27)(cid:37)(cid:21)(cid:32)(cid:23)(cid:17)(cid:18)(cid:24)(cid:23)(cid:26)(cid:18)(cid:30)(cid:37)(cid:19)(cid:27)(cid:29)(cid:37)(cid:30)(cid:32)(cid:15)(cid:25)(cid:23)(cid:31)(cid:31)(cid:23)(cid:26)(cid:21)(cid:37)(cid:16)(cid:27)(cid:17)(cid:18)(cid:37)(cid:1)(cid:37)(cid:30)(cid:27)(cid:19)(cid:31)(cid:34)(cid:14)(cid:29)(cid:18)(cid:37)(cid:19)(cid:27)(cid:29)(cid:37)(cid:19)(cid:32)(cid:29)(cid:31)(cid:22)(cid:18)(cid:29)(cid:37)(cid:23)(cid:26)(cid:19)(cid:27)(cid:29)(cid:25)(cid:14)(cid:31)(cid:23)(cid:27)(cid:26)(cid:5)(cid:37)

(cid:1)(cid:3)(cid:13)(cid:3)(cid:15)
(cid:43)(cid:87)(cid:80)(cid:75)(cid:62)(cid:107)(cid:112)(cid:75)(cid:85)(cid:68)(cid:87)(cid:93)(cid:83)(cid:58)(cid:97)(cid:75)(cid:87)(cid:85)(cid:112)(cid:58)(cid:60)(cid:87)(cid:99)(cid:97)(cid:112)(cid:58)(cid:101)(cid:58)(cid:75)(cid:80)(cid:58)(cid:60)(cid:75)(cid:80)(cid:75)(cid:97)(cid:108)(cid:112)(cid:87)(cid:68)(cid:112)(cid:64)(cid:58)(cid:97)(cid:58)(cid:112)
(cid:23)(cid:80)(cid:80)(cid:112)(cid:83)(cid:58)(cid:85)(cid:99)(cid:95)(cid:62)(cid:93)(cid:75)(cid:89)(cid:97)(cid:95)(cid:112)(cid:83)(cid:99)(cid:95)(cid:97)(cid:112)(cid:75)(cid:85)(cid:62)(cid:80)(cid:99)(cid:64)(cid:66)(cid:112)(cid:58)(cid:112)(cid:64)(cid:58)(cid:97)(cid:58)(cid:112)(cid:58)(cid:101)(cid:58)(cid:75)(cid:80)(cid:58)(cid:60)(cid:75)(cid:80)(cid:75)(cid:97)(cid:108)(cid:112)(cid:95)(cid:97)(cid:58)(cid:97)(cid:66)(cid:83)(cid:66)(cid:85)(cid:97)(cid:9)(cid:112)(cid:52)(cid:73)(cid:75)(cid:95)(cid:112)(cid:95)(cid:97)(cid:58)(cid:97)(cid:66)(cid:83)(cid:66)(cid:85)(cid:97)(cid:112)(cid:95)(cid:73)(cid:87)(cid:99)(cid:80)(cid:64)(cid:112)(cid:89)(cid:93)(cid:87)(cid:101)(cid:75)(cid:64)(cid:66)(cid:112)(cid:97)(cid:73)(cid:66)(cid:112)(cid:68)(cid:87)(cid:80)(cid:80)(cid:87)(cid:103)(cid:75)(cid:85)(cid:70)(cid:112)(cid:75)(cid:85)(cid:68)(cid:87)(cid:93)(cid:83)(cid:58)(cid:97)(cid:75)(cid:87)(cid:85)(cid:6)(cid:112)(cid:103)(cid:73)(cid:66)(cid:93)(cid:66)(cid:112)(cid:58)(cid:89)(cid:89)(cid:80)(cid:75)(cid:62)(cid:58)(cid:60)(cid:80)(cid:66)(cid:21)(cid:112)
(cid:8)(cid:24)(cid:63)(cid:63)(cid:67)(cid:96)(cid:96)(cid:76)(cid:88)(cid:86)(cid:112)(cid:63)(cid:88)(cid:65)(cid:67)(cid:96)(cid:7)(cid:112)(cid:100)(cid:86)(cid:76)(cid:92)(cid:100)(cid:67)(cid:112)(cid:76)(cid:65)(cid:67)(cid:86)(cid:98)(cid:76)(cid:69)(cid:76)(cid:67)(cid:94)(cid:96)(cid:7)(cid:112)(cid:88)(cid:94)(cid:112)(cid:104)(cid:67)(cid:61)(cid:112)(cid:81)(cid:76)(cid:86)(cid:78)(cid:96)(cid:112)(cid:69)(cid:88)(cid:94)(cid:112)(cid:90)(cid:100)(cid:61)(cid:81)(cid:76)(cid:63)(cid:81)(cid:109)(cid:112)(cid:59)(cid:102)(cid:59)(cid:76)(cid:81)(cid:59)(cid:61)(cid:81)(cid:67)(cid:112)(cid:65)(cid:59)(cid:98)(cid:59)(cid:96)(cid:67)(cid:98)(cid:96)(cid:112)
(cid:8)(cid:24)(cid:112)(cid:65)(cid:67)(cid:96)(cid:63)(cid:94)(cid:76)(cid:90)(cid:98)(cid:76)(cid:88)(cid:86)(cid:112)(cid:88)(cid:69)(cid:112)(cid:59)(cid:86)(cid:109)(cid:112)(cid:94)(cid:67)(cid:96)(cid:98)(cid:94)(cid:76)(cid:63)(cid:98)(cid:76)(cid:88)(cid:86)(cid:96)(cid:112)(cid:88)(cid:86)(cid:112)(cid:65)(cid:59)(cid:98)(cid:59)(cid:112)(cid:59)(cid:102)(cid:59)(cid:76)(cid:81)(cid:59)(cid:61)(cid:76)(cid:81)(cid:76)(cid:98)(cid:109)(cid:112)
(cid:8)(cid:32)(cid:88)(cid:94)(cid:112)(cid:63)(cid:81)(cid:76)(cid:86)(cid:76)(cid:63)(cid:59)(cid:81)(cid:112)(cid:65)(cid:59)(cid:98)(cid:59)(cid:96)(cid:67)(cid:98)(cid:96)(cid:112)(cid:88)(cid:94)(cid:112)(cid:98)(cid:74)(cid:76)(cid:94)(cid:65)(cid:112)(cid:90)(cid:59)(cid:94)(cid:98)(cid:109)(cid:112)(cid:65)(cid:59)(cid:98)(cid:59)(cid:7)(cid:112)(cid:90)(cid:81)(cid:67)(cid:59)(cid:96)(cid:67)(cid:112)(cid:67)(cid:86)(cid:96)(cid:100)(cid:94)(cid:67)(cid:112)(cid:98)(cid:74)(cid:59)(cid:98)(cid:112)(cid:98)(cid:74)(cid:67)(cid:112)(cid:96)(cid:98)(cid:59)(cid:98)(cid:67)(cid:84)(cid:67)(cid:86)(cid:98)(cid:112)(cid:59)(cid:65)(cid:74)(cid:67)(cid:94)(cid:67)(cid:96)(cid:112)(cid:98)(cid:88)(cid:112)(cid:88)(cid:100)(cid:94)(cid:112)(cid:46)(cid:112)
(cid:48)(cid:59)(cid:104)(cid:112)(cid:59)(cid:86)(cid:65)(cid:112)(cid:90)(cid:94)(cid:88)(cid:63)(cid:67)(cid:96)(cid:96)(cid:67)(cid:65)(cid:112)(cid:82)(cid:11)(cid:105)(cid:112)(cid:33)(cid:67)(cid:86)(cid:88)(cid:84)(cid:76)(cid:63)(cid:96)(cid:112)(cid:65)(cid:59)(cid:98)(cid:59)(cid:7)(cid:112)(cid:50)(cid:67)(cid:100)(cid:94)(cid:59)(cid:98)(cid:112)(cid:88)(cid:61)(cid:77)(cid:67)(cid:63)(cid:98)(cid:96)(cid:7)(cid:112)(cid:84)(cid:67)(cid:59)(cid:86)(cid:8)(cid:59)(cid:71)(cid:71)(cid:94)(cid:67)(cid:71)(cid:59)(cid:98)(cid:67)(cid:65)(cid:112)(cid:67)(cid:105)(cid:90)(cid:94)(cid:67)(cid:96)(cid:96)(cid:76)(cid:88)(cid:86)(cid:112)(cid:84)(cid:59)(cid:98)(cid:94)(cid:76)(cid:63)(cid:67)(cid:96)(cid:7)(cid:112)(cid:59)(cid:86)(cid:65)(cid:112)(cid:71)(cid:67)(cid:86)(cid:88)(cid:84)(cid:67)(cid:8)(cid:104)(cid:76)(cid:65)(cid:67)(cid:112)(cid:38)(cid:36)(cid:40)(cid:36)(cid:57)(cid:112)(cid:59)(cid:86)(cid:65)(cid:112)(cid:84)(cid:59)(cid:96)(cid:74)(cid:94)(cid:112)(cid:67)(cid:47)(cid:38)(cid:112)(cid:96)(cid:98)(cid:59)(cid:98)(cid:76)(cid:96)(cid:98)(cid:76)(cid:63)(cid:96)(cid:112)(cid:63)(cid:59)(cid:86)(cid:112)(cid:61)(cid:67)(cid:112)(cid:69)(cid:88)(cid:100)(cid:86)(cid:65)(cid:112)
(cid:88)(cid:86)(cid:112)(cid:33)(cid:30)(cid:42)(cid:112)(cid:104)(cid:76)(cid:98)(cid:74)(cid:112)(cid:98)(cid:74)(cid:67)(cid:112)(cid:59)(cid:63)(cid:63)(cid:67)(cid:96)(cid:96)(cid:76)(cid:88)(cid:86)(cid:112)(cid:86)(cid:100)(cid:84)(cid:61)(cid:67)(cid:94)(cid:112)(cid:33)(cid:50)(cid:30)(cid:13)(cid:13)(cid:18)(cid:12)(cid:14)(cid:17)(cid:10)(cid:112)(cid:33)(cid:66)(cid:85)(cid:87)(cid:97)(cid:107)(cid:89)(cid:66)(cid:112)(cid:64)(cid:58)(cid:97)(cid:58)(cid:112)(cid:58)(cid:93)(cid:66)(cid:112)(cid:58)(cid:101)(cid:58)(cid:75)(cid:80)(cid:58)(cid:60)(cid:80)(cid:66)(cid:112)(cid:87)(cid:85)(cid:112)(cid:64)(cid:60)(cid:33)(cid:58)(cid:43)(cid:112)(cid:103)(cid:75)(cid:97)(cid:73)(cid:112)(cid:97)(cid:73)(cid:66)(cid:112)(cid:58)(cid:62)(cid:62)(cid:66)(cid:95)(cid:95)(cid:75)(cid:87)(cid:85)(cid:112)(cid:85)(cid:99)(cid:83)(cid:60)(cid:66)(cid:93)(cid:112)(cid:89)(cid:73)(cid:95)(cid:11)(cid:11)(cid:14)(cid:16)(cid:13)(cid:12)(cid:9)
(cid:2)(cid:14)(cid:8)(cid:3)(cid:9)(cid:15)(cid:11)(cid:5)(cid:12)(cid:5)(cid:3)(cid:11)(cid:4)(cid:6)(cid:15)(cid:10)(cid:3)(cid:11)(cid:13)(cid:7)(cid:4)(cid:7)(cid:10)(cid:3)(cid:9)(cid:13)(cid:12)(cid:15)
(cid:43)(cid:87)(cid:80)(cid:75)(cid:62)(cid:107)(cid:112)(cid:75)(cid:85)(cid:68)(cid:87)(cid:93)(cid:83)(cid:58)(cid:97)(cid:75)(cid:87)(cid:85)(cid:112)(cid:58)(cid:60)(cid:87)(cid:99)(cid:97)(cid:112)(cid:95)(cid:97)(cid:99)(cid:64)(cid:75)(cid:66)(cid:95)(cid:112)(cid:75)(cid:85)(cid:101)(cid:87)(cid:80)(cid:101)(cid:75)(cid:85)(cid:72)(cid:112)(cid:73)(cid:99)(cid:83)(cid:58)(cid:85)(cid:112)(cid:93)(cid:66)(cid:95)(cid:66)(cid:58)(cid:93)(cid:62)(cid:73)(cid:112)(cid:91)(cid:58)(cid:93)(cid:97)(cid:75)(cid:62)(cid:75)(cid:91)(cid:58)(cid:85)(cid:97)(cid:95)(cid:112)(cid:58)(cid:85)(cid:64)(cid:112)(cid:51)(cid:66)(cid:106)(cid:112)(cid:58)(cid:85)(cid:64)(cid:112)(cid:34)(cid:66)(cid:85)(cid:64)(cid:66)(cid:93)(cid:112)(cid:75)(cid:85)(cid:112)(cid:49)(cid:66)(cid:95)(cid:66)(cid:58)(cid:93)(cid:62)(cid:73)(cid:10)(cid:112)
(cid:49)(cid:66)(cid:89)(cid:87)(cid:93)(cid:97)(cid:75)(cid:85)(cid:70)(cid:112)(cid:87)(cid:85)(cid:112)(cid:95)(cid:66)(cid:106)(cid:112)(cid:58)(cid:85)(cid:64)(cid:112)(cid:70)(cid:66)(cid:85)(cid:64)(cid:66)(cid:93)(cid:112) (cid:50)(cid:67)(cid:81)(cid:69)(cid:8)(cid:94)(cid:67)(cid:90)(cid:88)(cid:94)(cid:98)(cid:67)(cid:65)(cid:112)(cid:71)(cid:67)(cid:86)(cid:65)(cid:67)(cid:94)(cid:112)(cid:76)(cid:86)(cid:69)(cid:88)(cid:94)(cid:84)(cid:59)(cid:98)(cid:76)(cid:88)(cid:86)(cid:112)(cid:104)(cid:59)(cid:96)(cid:112)(cid:59)(cid:102)(cid:59)(cid:76)(cid:81)(cid:59)(cid:61)(cid:81)(cid:67)(cid:112)(cid:69)(cid:88)(cid:94)(cid:112)(cid:12)(cid:11)(cid:18)(cid:112)(cid:88)(cid:100)(cid:98)(cid:112)(cid:88)(cid:69)(cid:112)(cid:98)(cid:74)(cid:67)(cid:112)(cid:12)(cid:12)(cid:17)(cid:112)(cid:65)(cid:88)(cid:86)(cid:88)(cid:94)(cid:96)(cid:10)(cid:112)(cid:42)(cid:100)(cid:98)(cid:112)(cid:88)(cid:69)(cid:112)(cid:98)(cid:74)(cid:67)(cid:96)(cid:67)(cid:7)(cid:112)(cid:13)(cid:20)(cid:112)(cid:94)(cid:67)(cid:90)(cid:88)(cid:94)(cid:98)(cid:67)(cid:65)(cid:112)(cid:69)(cid:67)(cid:84)(cid:59)(cid:81)(cid:67)(cid:112)(cid:59)(cid:86)(cid:65)(cid:112)(cid:18)(cid:19)(cid:112)
(cid:94)(cid:67)(cid:90)(cid:88)(cid:94)(cid:98)(cid:67)(cid:65)(cid:112)(cid:84)(cid:59)(cid:81)(cid:67)(cid:10)(cid:112)(cid:41)(cid:88)(cid:112)(cid:96)(cid:67)(cid:105)(cid:8)(cid:96)(cid:90)(cid:67)(cid:63)(cid:76)(cid:69)(cid:76)(cid:63)(cid:112)(cid:59)(cid:86)(cid:59)(cid:81)(cid:109)(cid:96)(cid:67)(cid:96)(cid:112)(cid:104)(cid:67)(cid:94)(cid:67)(cid:112)(cid:90)(cid:67)(cid:94)(cid:69)(cid:88)(cid:94)(cid:84)(cid:67)(cid:65)(cid:112)(cid:76)(cid:86)(cid:112)(cid:98)(cid:74)(cid:76)(cid:96)(cid:112)(cid:96)(cid:98)(cid:100)(cid:65)(cid:109)(cid:112)(cid:65)(cid:100)(cid:67)(cid:112)(cid:98)(cid:88)(cid:112)(cid:98)(cid:74)(cid:67)(cid:112)(cid:81)(cid:88)(cid:104)(cid:112)(cid:86)(cid:100)(cid:84)(cid:61)(cid:67)(cid:94)(cid:112)(cid:88)(cid:69)(cid:112)(cid:69)(cid:67)(cid:84)(cid:59)(cid:81)(cid:67)(cid:112)(cid:96)(cid:59)(cid:84)(cid:90)(cid:81)(cid:67)(cid:96)(cid:10)(cid:112)
(cid:43)(cid:87)(cid:89)(cid:99)(cid:80)(cid:58)(cid:97)(cid:75)(cid:87)(cid:85)(cid:112)(cid:62)(cid:73)(cid:58)(cid:93)(cid:58)(cid:62)(cid:97)(cid:66)(cid:93)(cid:75)(cid:95)(cid:97)(cid:75)(cid:62)(cid:95)(cid:112) (cid:28)(cid:59)(cid:98)(cid:59)(cid:112)(cid:104)(cid:67)(cid:94)(cid:67)(cid:112)(cid:63)(cid:88)(cid:81)(cid:81)(cid:67)(cid:63)(cid:98)(cid:67)(cid:65)(cid:112)(cid:69)(cid:94)(cid:88)(cid:84)(cid:112)(cid:12)(cid:12)(cid:15)(cid:112)(cid:76)(cid:86)(cid:65)(cid:76)(cid:102)(cid:76)(cid:65)(cid:100)(cid:59)(cid:81)(cid:96)(cid:7)(cid:112)(cid:76)(cid:86)(cid:63)(cid:81)(cid:100)(cid:65)(cid:76)(cid:86)(cid:71)(cid:112)(cid:17)(cid:17)(cid:112)(cid:4)(cid:16)(cid:19)(cid:1)(cid:5)(cid:112)(cid:104)(cid:76)(cid:98)(cid:74)(cid:112)(cid:36)(cid:38)(cid:28)(cid:112)(cid:59)(cid:86)(cid:65)(cid:112)(cid:15)(cid:19)(cid:112)(cid:4)(cid:15)(cid:13)(cid:1)(cid:5)(cid:112)(cid:100)(cid:86)(cid:59)(cid:69)(cid:69)(cid:67)(cid:63)(cid:98)(cid:67)(cid:65)(cid:112)(cid:65)(cid:88)(cid:86)(cid:88)(cid:94)(cid:96)(cid:10)(cid:112)(cid:53)(cid:74)(cid:67)(cid:112)(cid:36)(cid:38)(cid:28)(cid:112)(cid:81)(cid:100)(cid:86)(cid:71)(cid:96)(cid:112)
(cid:76)(cid:86)(cid:63)(cid:81)(cid:100)(cid:65)(cid:67)(cid:65)(cid:112)(cid:96)(cid:59)(cid:84)(cid:90)(cid:81)(cid:67)(cid:96)(cid:112)(cid:69)(cid:94)(cid:88)(cid:84)(cid:112)(cid:14)(cid:20)(cid:112)(cid:76)(cid:86)(cid:65)(cid:76)(cid:102)(cid:76)(cid:65)(cid:100)(cid:59)(cid:81)(cid:96)(cid:112)(cid:104)(cid:76)(cid:98)(cid:74)(cid:112)(cid:36)(cid:44)(cid:32)(cid:112)(cid:59)(cid:86)(cid:65)(cid:112)(cid:13)(cid:18)(cid:112)(cid:104)(cid:76)(cid:98)(cid:74)(cid:112)(cid:88)(cid:98)(cid:74)(cid:67)(cid:94)(cid:112)(cid:69)(cid:88)(cid:94)(cid:84)(cid:96)(cid:112)(cid:88)(cid:69)(cid:112)(cid:44)(cid:32)(cid:7)(cid:112)(cid:76)(cid:86)(cid:63)(cid:81)(cid:100)(cid:65)(cid:76)(cid:86)(cid:71)(cid:112)(cid:96)(cid:59)(cid:94)(cid:63)(cid:88)(cid:76)(cid:65)(cid:88)(cid:96)(cid:76)(cid:96)(cid:112)(cid:4)(cid:86)(cid:22)(cid:15)(cid:5)(cid:7)(cid:112)(cid:63)(cid:88)(cid:86)(cid:86)(cid:67)(cid:63)(cid:98)(cid:76)(cid:102)(cid:67)(cid:112)(cid:98)(cid:76)(cid:96)(cid:96)(cid:100)(cid:67)(cid:112)
(cid:65)(cid:76)(cid:96)(cid:67)(cid:59)(cid:96)(cid:67)(cid:111)(cid:59)(cid:96)(cid:96)(cid:88)(cid:63)(cid:76)(cid:59)(cid:98)(cid:67)(cid:65)(cid:112)(cid:76)(cid:86)(cid:98)(cid:67)(cid:94)(cid:96)(cid:98)(cid:76)(cid:98)(cid:76)(cid:59)(cid:81)(cid:112)(cid:81)(cid:100)(cid:86)(cid:71)(cid:112)(cid:65)(cid:76)(cid:96)(cid:67)(cid:59)(cid:96)(cid:67)(cid:112)(cid:4)(cid:27)(cid:53)(cid:28)(cid:8)(cid:36)(cid:38)(cid:28)(cid:7)(cid:112)(cid:86)(cid:22)(cid:14)(cid:5)(cid:7)(cid:112)(cid:76)(cid:65)(cid:76)(cid:88)(cid:90)(cid:59)(cid:98)(cid:74)(cid:76)(cid:63)(cid:112)(cid:86)(cid:88)(cid:86)(cid:96)(cid:90)(cid:67)(cid:63)(cid:76)(cid:69)(cid:76)(cid:63)(cid:112)(cid:76)(cid:86)(cid:98)(cid:67)(cid:94)(cid:96)(cid:98)(cid:76)(cid:98)(cid:76)(cid:59)(cid:81)(cid:112)(cid:90)(cid:86)(cid:67)(cid:100)(cid:84)(cid:88)(cid:86)(cid:76)(cid:59)(cid:112)(cid:4)(cid:41)(cid:50)(cid:36)(cid:44)(cid:7)(cid:112)(cid:86)(cid:22)(cid:14)(cid:5)(cid:7)(cid:112)(cid:63)(cid:88)(cid:59)(cid:81)(cid:112)
(cid:104)(cid:88)(cid:94)(cid:78)(cid:67)(cid:94)(cid:3)(cid:96)(cid:112)(cid:90)(cid:86)(cid:67)(cid:100)(cid:84)(cid:88)(cid:63)(cid:88)(cid:86)(cid:76)(cid:88)(cid:96)(cid:76)(cid:96)(cid:112)(cid:4)(cid:27)(cid:56)(cid:44)(cid:7)(cid:112)(cid:86)(cid:22)(cid:14)(cid:5)(cid:7)(cid:112)(cid:63)(cid:74)(cid:94)(cid:88)(cid:86)(cid:76)(cid:63)(cid:112)(cid:74)(cid:109)(cid:90)(cid:67)(cid:94)(cid:96)(cid:67)(cid:86)(cid:96)(cid:76)(cid:98)(cid:76)(cid:102)(cid:76)(cid:98)(cid:109)(cid:112)(cid:90)(cid:86)(cid:67)(cid:100)(cid:84)(cid:88)(cid:86)(cid:76)(cid:98)(cid:76)(cid:96)(cid:112)(cid:4)(cid:63)(cid:35)(cid:44)(cid:7)(cid:112)(cid:86)(cid:22)(cid:13)(cid:5)(cid:7)(cid:112)(cid:76)(cid:86)(cid:98)(cid:67)(cid:94)(cid:96)(cid:98)(cid:76)(cid:98)(cid:76)(cid:59)(cid:81)(cid:112)(cid:90)(cid:86)(cid:67)(cid:100)(cid:84)(cid:88)(cid:86)(cid:76)(cid:59)(cid:112)(cid:104)(cid:76)(cid:98)(cid:74)(cid:112)
(cid:59)(cid:100)(cid:98)(cid:88)(cid:76)(cid:84)(cid:84)(cid:100)(cid:86)(cid:67)(cid:112)(cid:69)(cid:67)(cid:59)(cid:98)(cid:100)(cid:94)(cid:67)(cid:96)(cid:112)(cid:4)(cid:36)(cid:44)(cid:24)(cid:32)(cid:7)(cid:112)(cid:86)(cid:22)(cid:13)(cid:5)(cid:7)(cid:112)(cid:59)(cid:86)(cid:65)(cid:112)(cid:100)(cid:86)(cid:63)(cid:81)(cid:59)(cid:96)(cid:96)(cid:76)(cid:69)(cid:76)(cid:59)(cid:61)(cid:81)(cid:67)(cid:112)(cid:36)(cid:38)(cid:28)(cid:112)(cid:4)(cid:86)(cid:22)(cid:82)(cid:11)(cid:5)(cid:10)(cid:112)(cid:53)(cid:74)(cid:67)(cid:112)(cid:84)(cid:59)(cid:77)(cid:88)(cid:94)(cid:76)(cid:98)(cid:109)(cid:112)(cid:4)(cid:17)(cid:18)(cid:1)(cid:5)(cid:112)(cid:88)(cid:69)(cid:112)(cid:98)(cid:74)(cid:67)(cid:112)(cid:81)(cid:100)(cid:86)(cid:71)(cid:112)(cid:96)(cid:59)(cid:84)(cid:90)(cid:81)(cid:67)(cid:96)(cid:112)(cid:104)(cid:67)(cid:94)(cid:67)(cid:112)(cid:69)(cid:94)(cid:88)(cid:84)(cid:112)
(cid:76)(cid:86)(cid:65)(cid:76)(cid:102)(cid:76)(cid:65)(cid:100)(cid:59)(cid:81)(cid:96)(cid:112)(cid:104)(cid:76)(cid:98)(cid:74)(cid:112)(cid:96)(cid:67)(cid:81)(cid:69)(cid:111)(cid:94)(cid:67)(cid:90)(cid:88)(cid:94)(cid:98)(cid:67)(cid:65)(cid:112)(cid:67)(cid:98)(cid:74)(cid:86)(cid:76)(cid:63)(cid:76)(cid:98)(cid:109)(cid:112)(cid:76)(cid:86)(cid:69)(cid:88)(cid:94)(cid:84)(cid:59)(cid:98)(cid:76)(cid:88)(cid:86)(cid:112)(cid:88)(cid:69)(cid:112)(cid:30)(cid:100)(cid:94)(cid:88)(cid:90)(cid:67)(cid:59)(cid:86)(cid:112)(cid:59)(cid:86)(cid:63)(cid:67)(cid:96)(cid:98)(cid:94)(cid:109)(cid:7)(cid:112)(cid:59)(cid:86)(cid:65)(cid:112)(cid:16)(cid:14)(cid:112)(cid:4)(cid:15)(cid:17)(cid:1)(cid:5)(cid:112)(cid:94)(cid:67)(cid:90)(cid:88)(cid:94)(cid:98)(cid:67)(cid:65)(cid:112)(cid:90)(cid:59)(cid:96)(cid:98)(cid:112)(cid:88)(cid:94)(cid:112)(cid:90)(cid:94)(cid:67)(cid:96)(cid:67)(cid:86)(cid:98)(cid:112)(cid:98)(cid:88)(cid:61)(cid:59)(cid:63)(cid:63)(cid:88)(cid:112)
(cid:1)(cid:5)
(cid:100)(cid:96)(cid:67)(cid:10)(cid:112)
(cid:4)(cid:5)
(cid:49)(cid:66)(cid:62)(cid:93)(cid:99)(cid:75)(cid:97)(cid:83)(cid:66)(cid:85)(cid:97)(cid:112) (cid:44)(cid:59)(cid:94)(cid:98)(cid:76)(cid:63)(cid:76)(cid:90)(cid:59)(cid:86)(cid:98)(cid:96)(cid:112)(cid:104)(cid:67)(cid:94)(cid:67)(cid:112)(cid:61)(cid:67)(cid:112)(cid:90)(cid:59)(cid:98)(cid:76)(cid:67)(cid:86)(cid:98)(cid:96)(cid:112)(cid:88)(cid:69)(cid:112)(cid:98)(cid:74)(cid:67)(cid:112)(cid:27)(cid:81)(cid:76)(cid:86)(cid:76)(cid:63)(cid:59)(cid:81)(cid:112)(cid:36)(cid:86)(cid:102)(cid:67)(cid:96)(cid:98)(cid:76)(cid:71)(cid:59)(cid:98)(cid:88)(cid:94)(cid:112)(cid:98)(cid:74)(cid:59)(cid:98)(cid:112)(cid:59)(cid:94)(cid:67)(cid:112)(cid:96)(cid:63)(cid:74)(cid:67)(cid:65)(cid:100)(cid:81)(cid:67)(cid:65)(cid:112)(cid:69)(cid:88)(cid:94)(cid:112)(cid:59)(cid:112)(cid:81)(cid:100)(cid:86)(cid:71)(cid:112)(cid:98)(cid:94)(cid:59)(cid:86)(cid:96)(cid:90)(cid:81)(cid:59)(cid:86)(cid:98)(cid:112)(cid:96)(cid:100)(cid:94)(cid:71)(cid:67)(cid:94)(cid:109)(cid:10)(cid:112)(cid:53)(cid:74)(cid:67)(cid:112)(cid:27)(cid:81)(cid:76)(cid:86)(cid:76)(cid:63)(cid:59)(cid:81)(cid:112)
(cid:36)(cid:86)(cid:102)(cid:67)(cid:96)(cid:98)(cid:76)(cid:71)(cid:59)(cid:98)(cid:88)(cid:94)(cid:112)(cid:88)(cid:94)(cid:112)(cid:59)(cid:112)(cid:84)(cid:67)(cid:84)(cid:61)(cid:67)(cid:94)(cid:112)(cid:88)(cid:69)(cid:112)(cid:74)(cid:76)(cid:96)(cid:112)(cid:94)(cid:67)(cid:96)(cid:67)(cid:59)(cid:94)(cid:63)(cid:74)(cid:112)(cid:96)(cid:98)(cid:59)(cid:69)(cid:69)(cid:112)(cid:59)(cid:90)(cid:90)(cid:94)(cid:88)(cid:59)(cid:63)(cid:74)(cid:67)(cid:65)(cid:112)(cid:76)(cid:86)(cid:65)(cid:76)(cid:102)(cid:76)(cid:65)(cid:100)(cid:59)(cid:81)(cid:96)(cid:112)(cid:98)(cid:88)(cid:112)(cid:65)(cid:76)(cid:96)(cid:63)(cid:100)(cid:96)(cid:96)(cid:112)(cid:98)(cid:74)(cid:67)(cid:112)(cid:96)(cid:98)(cid:100)(cid:65)(cid:109)(cid:112)(cid:59)(cid:86)(cid:65)(cid:112)(cid:76)(cid:86)(cid:102)(cid:76)(cid:98)(cid:67)(cid:112)(cid:98)(cid:74)(cid:67)(cid:84)(cid:112)(cid:98)(cid:88)(cid:112)(cid:90)(cid:59)(cid:94)(cid:98)(cid:76)(cid:63)(cid:76)(cid:90)(cid:59)(cid:98)(cid:67)(cid:10)(cid:112)
(cid:31)(cid:97)(cid:73)(cid:75)(cid:62)(cid:95)(cid:112)(cid:87)(cid:101)(cid:66)(cid:93)(cid:95)(cid:75)(cid:70)(cid:73)(cid:97)(cid:112) (cid:50)(cid:98)(cid:100)(cid:65)(cid:76)(cid:67)(cid:96)(cid:112)(cid:104)(cid:67)(cid:94)(cid:67)(cid:112)(cid:59)(cid:90)(cid:90)(cid:94)(cid:88)(cid:102)(cid:67)(cid:65)(cid:112)(cid:61)(cid:109)(cid:112)(cid:98)(cid:74)(cid:67)(cid:112)(cid:81)(cid:88)(cid:63)(cid:59)(cid:81)(cid:112)(cid:36)(cid:86)(cid:96)(cid:98)(cid:76)(cid:98)(cid:100)(cid:98)(cid:76)(cid:88)(cid:86)(cid:59)(cid:81)(cid:112)(cid:48)(cid:67)(cid:102)(cid:76)(cid:67)(cid:104)(cid:112)(cid:25)(cid:88)(cid:59)(cid:94)(cid:65)(cid:96)(cid:112)(cid:4)(cid:55)(cid:59)(cid:86)(cid:65)(cid:67)(cid:94)(cid:61)(cid:76)(cid:81)(cid:98)(cid:112)(cid:36)(cid:48)(cid:25)(cid:112)(cid:86)(cid:88)(cid:96)(cid:10)(cid:112)(cid:11)(cid:17)(cid:11)(cid:12)(cid:17)(cid:16)(cid:112)(cid:59)(cid:86)(cid:65)(cid:112)(cid:12)(cid:18)(cid:12)(cid:17)(cid:16)(cid:18)(cid:112)(cid:59)(cid:86)(cid:65)(cid:112)(cid:56)(cid:67)(cid:96)(cid:98)(cid:67)(cid:94)(cid:86)(cid:112)(cid:36)(cid:48)(cid:25)(cid:112)(cid:86)(cid:88)(cid:10)(cid:112)
(cid:13)(cid:11)(cid:12)(cid:19)(cid:12)(cid:19)(cid:14)(cid:17)(cid:5)(cid:10)(cid:112)
(cid:41)(cid:88)(cid:98)(cid:67)(cid:112)(cid:98)(cid:74)(cid:59)(cid:98)(cid:112)(cid:69)(cid:100)(cid:81)(cid:81)(cid:112)(cid:76)(cid:86)(cid:69)(cid:88)(cid:94)(cid:84)(cid:59)(cid:98)(cid:76)(cid:88)(cid:86)(cid:112)(cid:88)(cid:86)(cid:112)(cid:98)(cid:74)(cid:67)(cid:112)(cid:59)(cid:90)(cid:90)(cid:94)(cid:88)(cid:102)(cid:59)(cid:81)(cid:112)(cid:88)(cid:69)(cid:112)(cid:98)(cid:74)(cid:67)(cid:112)(cid:96)(cid:98)(cid:100)(cid:65)(cid:109)(cid:112)(cid:90)(cid:94)(cid:88)(cid:98)(cid:88)(cid:63)(cid:88)(cid:81)(cid:112)(cid:84)(cid:100)(cid:96)(cid:98)(cid:112)(cid:59)(cid:81)(cid:96)(cid:88)(cid:112)(cid:61)(cid:67)(cid:112)(cid:90)(cid:94)(cid:88)(cid:102)(cid:76)(cid:65)(cid:67)(cid:65)(cid:112)(cid:76)(cid:86)(cid:112)(cid:98)(cid:74)(cid:67)(cid:112)(cid:84)(cid:59)(cid:86)(cid:100)(cid:96)(cid:63)(cid:94)(cid:76)(cid:90)(cid:98)(cid:10)(cid:112)
(cid:3)(cid:13)(cid:9)(cid:14)(cid:8)(cid:2)(cid:20)(cid:18)(cid:9)(cid:7)(cid:13)(cid:10)(cid:13)(cid:7)(cid:24)(cid:19)(cid:9)(cid:18)(cid:17)(cid:19)(cid:21)(cid:13)(cid:16)(cid:11)(cid:24)
(cid:43)(cid:80)(cid:66)(cid:58)(cid:95)(cid:66)(cid:112)(cid:95)(cid:66)(cid:80)(cid:66)(cid:62)(cid:97)(cid:112)(cid:97)(cid:73)(cid:66)(cid:112)(cid:87)(cid:85)(cid:66)(cid:112)(cid:60)(cid:66)(cid:80)(cid:87)(cid:103)(cid:112)(cid:97)(cid:73)(cid:58)(cid:97)(cid:112)(cid:75)(cid:95)(cid:112)(cid:97)(cid:73)(cid:66)(cid:112)(cid:60)(cid:66)(cid:95)(cid:97)(cid:112)(cid:68)(cid:75)(cid:97)(cid:112)(cid:68)(cid:87)(cid:93)(cid:112)(cid:107)(cid:87)(cid:99)(cid:93)(cid:112)(cid:93)(cid:66)(cid:95)(cid:66)(cid:58)(cid:93)(cid:62)(cid:73)(cid:10)(cid:112)(cid:37)(cid:68)(cid:112)(cid:107)(cid:87)(cid:99)(cid:112)(cid:58)(cid:93)(cid:66)(cid:112)(cid:85)(cid:87)(cid:97)(cid:112)(cid:95)(cid:99)(cid:93)(cid:66)(cid:6)(cid:112)(cid:93)(cid:66)(cid:58)(cid:64)(cid:112)(cid:97)(cid:73)(cid:66)(cid:112)(cid:58)(cid:89)(cid:89)(cid:93)(cid:87)(cid:89)(cid:93)(cid:75)(cid:58)(cid:97)(cid:66)(cid:112)(cid:95)(cid:66)(cid:62)(cid:97)(cid:75)(cid:87)(cid:85)(cid:95)(cid:112)(cid:60)(cid:66)(cid:68)(cid:87)(cid:93)(cid:66)(cid:112)(cid:83)(cid:58)(cid:79)(cid:75)(cid:85)(cid:70)(cid:112)(cid:107)(cid:87)(cid:99)(cid:93)(cid:112)(cid:95)(cid:66)(cid:80)(cid:66)(cid:62)(cid:97)(cid:75)(cid:87)(cid:85)(cid:10)(cid:112)
(cid:1)(cid:2) (cid:1)(cid:2) (cid:1)(cid:2)
(cid:39)(cid:75)(cid:68)(cid:66)(cid:112)(cid:95)(cid:62)(cid:75)(cid:66)(cid:85)(cid:62)(cid:66)(cid:95)(cid:112) (cid:26)(cid:66)(cid:73)(cid:58)(cid:101)(cid:75)(cid:87)(cid:99)(cid:93)(cid:58)(cid:80)(cid:112)(cid:2)(cid:112)(cid:95)(cid:87)(cid:62)(cid:75)(cid:58)(cid:80)(cid:112)(cid:95)(cid:62)(cid:75)(cid:66)(cid:85)(cid:62)(cid:66)(cid:95)(cid:112) (cid:31)(cid:62)(cid:87)(cid:80)(cid:87)(cid:70)(cid:75)(cid:62)(cid:58)(cid:80)(cid:6)(cid:112)(cid:66)(cid:101)(cid:87)(cid:80)(cid:99)(cid:97)(cid:75)(cid:87)(cid:85)(cid:58)(cid:93)(cid:107)(cid:112)(cid:2)(cid:112)(cid:66)(cid:85)(cid:101)(cid:75)(cid:93)(cid:87)(cid:85)(cid:83)(cid:66)(cid:85)(cid:97)(cid:58)(cid:80)(cid:112)(cid:95)(cid:62)(cid:75)(cid:66)(cid:85)(cid:62)(cid:66)(cid:95)(cid:112)
(cid:8)(cid:20)(cid:23)(cid:30)(cid:9)(cid:30)(cid:23)(cid:12)(cid:13)(cid:12)(cid:23)(cid:12)(cid:19)(cid:10)(cid:12)(cid:30)(cid:10)(cid:20)(cid:21)(cid:29)(cid:30)(cid:20)(cid:13)(cid:30)(cid:26)(cid:15)(cid:12)(cid:30)(cid:11)(cid:20)(cid:10)(cid:27)(cid:18)(cid:12)(cid:19)(cid:26)(cid:30)(cid:28)(cid:16)(cid:26)(cid:15)(cid:30)(cid:9)(cid:17)(cid:17)(cid:30)(cid:25)(cid:12)(cid:10)(cid:26)(cid:16)(cid:20)(cid:19)(cid:25)(cid:1)(cid:30)(cid:25)(cid:12)(cid:12)(cid:30)(cid:19)(cid:9)(cid:26)(cid:27)(cid:23)(cid:12)(cid:4)(cid:10)(cid:20)(cid:18)(cid:6)(cid:11)(cid:20)(cid:10)(cid:27)(cid:18)(cid:12)(cid:19)(cid:26)(cid:25)(cid:7)(cid:19)(cid:23)(cid:2)(cid:23)(cid:12)(cid:22)(cid:20)(cid:23)(cid:26)(cid:16)(cid:19)(cid:14)(cid:2)(cid:25)(cid:27)(cid:18)(cid:18)(cid:9)(cid:24)(cid:3)(cid:13)(cid:17)(cid:9)(cid:26)(cid:5)(cid:22)(cid:11)(cid:13)(cid:30)
(cid:4)(cid:13)(cid:10)(cid:9)(cid:24)(cid:20)(cid:7)(cid:13)(cid:9)(cid:16)(cid:7)(cid:9)(cid:20)(cid:24)(cid:20)(cid:21)(cid:22)(cid:8)(cid:23)(cid:24)(cid:8)(cid:9)(cid:20)(cid:13)(cid:11)(cid:16)(cid:24)
(cid:23)(cid:80)(cid:80)(cid:112)(cid:95)(cid:97)(cid:99)(cid:64)(cid:75)(cid:66)(cid:95)(cid:112)(cid:83)(cid:99)(cid:95)(cid:97)(cid:112)(cid:64)(cid:75)(cid:95)(cid:62)(cid:80)(cid:87)(cid:95)(cid:66)(cid:112)(cid:87)(cid:85)(cid:112)(cid:97)(cid:73)(cid:66)(cid:95)(cid:66)(cid:112)(cid:89)(cid:87)(cid:75)(cid:85)(cid:97)(cid:95)(cid:112)(cid:66)(cid:101)(cid:66)(cid:85)(cid:112)(cid:103)(cid:73)(cid:66)(cid:85)(cid:112)(cid:97)(cid:73)(cid:66)(cid:112)(cid:64)(cid:75)(cid:95)(cid:62)(cid:80)(cid:87)(cid:95)(cid:99)(cid:93)(cid:66)(cid:112)(cid:75)(cid:95)(cid:112)(cid:85)(cid:66)(cid:70)(cid:58)(cid:97)(cid:75)(cid:101)(cid:66)(cid:10)(cid:112)
(cid:51)(cid:58)(cid:83)(cid:89)(cid:80)(cid:66)(cid:112)(cid:95)(cid:75)(cid:110)(cid:66)(cid:112) (cid:53)(cid:74)(cid:67)(cid:112)(cid:69)(cid:76)(cid:86)(cid:59)(cid:81)(cid:112)(cid:65)(cid:59)(cid:98)(cid:59)(cid:96)(cid:67)(cid:98)(cid:112)(cid:63)(cid:88)(cid:86)(cid:96)(cid:76)(cid:96)(cid:98)(cid:67)(cid:65)(cid:112)(cid:88)(cid:69)(cid:112)(cid:65)(cid:59)(cid:98)(cid:59)(cid:112)(cid:63)(cid:88)(cid:81)(cid:81)(cid:67)(cid:63)(cid:98)(cid:67)(cid:65)(cid:112)(cid:69)(cid:94)(cid:88)(cid:84)(cid:112)(cid:12)(cid:12)(cid:15)(cid:112)(cid:65)(cid:88)(cid:86)(cid:88)(cid:94)(cid:96)(cid:7)(cid:112)(cid:76)(cid:86)(cid:63)(cid:81)(cid:100)(cid:65)(cid:76)(cid:86)(cid:71)(cid:112)(cid:17)(cid:17)(cid:112)(cid:36)(cid:38)(cid:28)(cid:112)(cid:59)(cid:86)(cid:65)(cid:112)(cid:15)(cid:19)(cid:112)(cid:100)(cid:86)(cid:59)(cid:69)(cid:69)(cid:67)(cid:63)(cid:98)(cid:67)(cid:65)(cid:112)(cid:65)(cid:88)(cid:86)(cid:88)(cid:94)(cid:96)(cid:10)(cid:112)
(cid:29)(cid:58)(cid:97)(cid:58)(cid:112)(cid:66)(cid:106)(cid:62)(cid:80)(cid:99)(cid:95)(cid:75)(cid:87)(cid:85)(cid:95)(cid:112) (cid:28)(cid:88)(cid:86)(cid:88)(cid:94)(cid:112)(cid:55)(cid:54)(cid:36)(cid:38)(cid:28)(cid:17)(cid:16)(cid:112)(cid:104)(cid:59)(cid:96)(cid:112)(cid:94)(cid:67)(cid:84)(cid:88)(cid:102)(cid:67)(cid:65)(cid:112)(cid:65)(cid:100)(cid:67)(cid:112)(cid:98)(cid:88)(cid:112)(cid:76)(cid:86)(cid:63)(cid:88)(cid:86)(cid:96)(cid:76)(cid:96)(cid:98)(cid:67)(cid:86)(cid:63)(cid:76)(cid:67)(cid:96)(cid:112)(cid:76)(cid:86)(cid:112)(cid:84)(cid:67)(cid:98)(cid:59)(cid:65)(cid:59)(cid:98)(cid:59)(cid:112)(cid:96)(cid:100)(cid:71)(cid:71)(cid:67)(cid:96)(cid:98)(cid:76)(cid:86)(cid:71)(cid:112)(cid:84)(cid:76)(cid:96)(cid:81)(cid:59)(cid:61)(cid:67)(cid:81)(cid:76)(cid:86)(cid:71)(cid:10)(cid:112)
(cid:1)(cid:2)
(cid:49)(cid:66)(cid:89)(cid:80)(cid:75)(cid:62)(cid:58)(cid:97)(cid:75)(cid:87)(cid:85)(cid:112) (cid:96)(cid:63)(cid:8)(cid:67)(cid:45)(cid:53)(cid:38)(cid:112)(cid:104)(cid:67)(cid:94)(cid:67)(cid:112)(cid:63)(cid:88)(cid:84)(cid:90)(cid:59)(cid:94)(cid:67)(cid:65)(cid:112)(cid:104)(cid:76)(cid:98)(cid:74)(cid:112)(cid:90)(cid:94)(cid:67)(cid:102)(cid:76)(cid:88)(cid:100)(cid:96)(cid:81)(cid:109)(cid:112)(cid:90)(cid:100)(cid:61)(cid:81)(cid:76)(cid:96)(cid:74)(cid:67)(cid:65)(cid:112)(cid:65)(cid:59)(cid:98)(cid:59)(cid:96)(cid:67)(cid:98)(cid:96)(cid:7)(cid:112)(cid:76)(cid:10)(cid:67)(cid:10)(cid:7)(cid:112)(cid:33)(cid:53)(cid:30)(cid:105)(cid:10)(cid:112)
(cid:3)(cid:5)
(cid:49)(cid:58)(cid:85)(cid:64)(cid:87)(cid:83)(cid:75)(cid:110)(cid:58)(cid:97)(cid:75)(cid:87)(cid:85)(cid:112) (cid:53)(cid:74)(cid:76)(cid:96)(cid:112)(cid:76)(cid:96)(cid:112)(cid:86)(cid:88)(cid:98)(cid:112)(cid:94)(cid:67)(cid:81)(cid:67)(cid:102)(cid:59)(cid:86)(cid:98)(cid:112)(cid:98)(cid:88)(cid:112)(cid:98)(cid:74)(cid:67)(cid:112)(cid:90)(cid:94)(cid:67)(cid:96)(cid:67)(cid:86)(cid:98)(cid:112)(cid:96)(cid:98)(cid:100)(cid:65)(cid:109)(cid:7)(cid:112)(cid:59)(cid:96)(cid:112)(cid:96)(cid:59)(cid:84)(cid:90)(cid:81)(cid:67)(cid:96)(cid:112)(cid:104)(cid:67)(cid:94)(cid:67)(cid:112)(cid:86)(cid:88)(cid:98)(cid:112)(cid:59)(cid:81)(cid:81)(cid:88)(cid:63)(cid:59)(cid:98)(cid:67)(cid:65)(cid:112)(cid:98)(cid:88)(cid:112)(cid:71)(cid:94)(cid:88)(cid:100)(cid:90)(cid:96)(cid:112)(cid:61)(cid:100)(cid:98)(cid:112)(cid:63)(cid:88)(cid:84)(cid:90)(cid:59)(cid:94)(cid:76)(cid:96)(cid:88)(cid:86)(cid:96)(cid:112)(cid:104)(cid:67)(cid:94)(cid:67)(cid:112)(cid:63)(cid:88)(cid:86)(cid:65)(cid:100)(cid:63)(cid:98)(cid:67)(cid:65)(cid:112)(cid:61)(cid:67)(cid:98)(cid:104)(cid:67)(cid:67)(cid:86)(cid:112)(cid:63)(cid:59)(cid:96)(cid:67)(cid:96)(cid:112)(cid:59)(cid:86)(cid:65)(cid:112)
(cid:100)(cid:86)(cid:59)(cid:69)(cid:69)(cid:67)(cid:63)(cid:98)(cid:67)(cid:65)(cid:112)(cid:65)(cid:88)(cid:86)(cid:88)(cid:94)(cid:96)(cid:10)(cid:112)
(cid:2)(cid:5)
(cid:26)(cid:80)(cid:75)(cid:85)(cid:64)(cid:75)(cid:85)(cid:70)(cid:112) (cid:53)(cid:74)(cid:76)(cid:96)(cid:112)(cid:76)(cid:96)(cid:112)(cid:86)(cid:88)(cid:98)(cid:112)(cid:94)(cid:67)(cid:81)(cid:67)(cid:102)(cid:59)(cid:86)(cid:98)(cid:112)(cid:98)(cid:88)(cid:112)(cid:98)(cid:74)(cid:67)(cid:112)(cid:90)(cid:94)(cid:67)(cid:96)(cid:67)(cid:86)(cid:98)(cid:112)(cid:96)(cid:98)(cid:100)(cid:65)(cid:109)(cid:112)(cid:59)(cid:96)(cid:112)(cid:96)(cid:59)(cid:84)(cid:90)(cid:81)(cid:67)(cid:96)(cid:112)(cid:104)(cid:67)(cid:94)(cid:67)(cid:112)(cid:86)(cid:88)(cid:98)(cid:112)(cid:59)(cid:81)(cid:81)(cid:88)(cid:63)(cid:59)(cid:98)(cid:67)(cid:65)(cid:112)(cid:98)(cid:88)(cid:112)(cid:71)(cid:94)(cid:88)(cid:100)(cid:90)(cid:96)(cid:10)(cid:112)
(cid:3)(cid:5)
(cid:5)(cid:9)(cid:18)(cid:17)(cid:19)(cid:21)(cid:13)(cid:16)(cid:11)(cid:24)(cid:10)(cid:17)(cid:19)(cid:24)(cid:20)(cid:18)(cid:9)(cid:7)(cid:13)(cid:10)(cid:13)(cid:7)(cid:24)(cid:15)(cid:6)(cid:21)(cid:9)(cid:19)(cid:13)(cid:6)(cid:14)(cid:20)(cid:1)(cid:24)(cid:20)(cid:23)(cid:20)(cid:21)(cid:9)(cid:15)(cid:20)(cid:24)(cid:6)(cid:16)(cid:8)(cid:24)(cid:15)(cid:9)(cid:21)(cid:12)(cid:17)(cid:8)(cid:20)(cid:24)
(cid:56)(cid:67)(cid:112)(cid:94)(cid:67)(cid:92)(cid:100)(cid:76)(cid:94)(cid:67)(cid:112)(cid:76)(cid:86)(cid:69)(cid:88)(cid:94)(cid:84)(cid:59)(cid:98)(cid:76)(cid:88)(cid:86)(cid:112)(cid:69)(cid:94)(cid:88)(cid:84)(cid:112)(cid:59)(cid:100)(cid:98)(cid:74)(cid:88)(cid:94)(cid:96)(cid:112)(cid:59)(cid:61)(cid:88)(cid:100)(cid:98)(cid:112)(cid:96)(cid:88)(cid:84)(cid:67)(cid:112)(cid:98)(cid:109)(cid:90)(cid:67)(cid:96)(cid:112)(cid:88)(cid:69)(cid:112)(cid:84)(cid:59)(cid:98)(cid:67)(cid:94)(cid:76)(cid:59)(cid:81)(cid:96)(cid:7)(cid:112)(cid:67)(cid:105)(cid:90)(cid:67)(cid:94)(cid:76)(cid:84)(cid:67)(cid:86)(cid:98)(cid:59)(cid:81)(cid:112)(cid:96)(cid:109)(cid:96)(cid:98)(cid:67)(cid:84)(cid:96)(cid:112)(cid:59)(cid:86)(cid:65)(cid:112)(cid:84)(cid:67)(cid:98)(cid:74)(cid:88)(cid:65)(cid:96)(cid:112)(cid:100)(cid:96)(cid:67)(cid:65)(cid:112)(cid:76)(cid:86)(cid:112)(cid:84)(cid:59)(cid:86)(cid:109)(cid:112)(cid:96)(cid:98)(cid:100)(cid:65)(cid:76)(cid:67)(cid:96)(cid:10)(cid:112)(cid:35)(cid:67)(cid:94)(cid:67)(cid:7)(cid:112)(cid:76)(cid:86)(cid:65)(cid:76)(cid:63)(cid:59)(cid:98)(cid:67)(cid:112)(cid:104)(cid:74)(cid:67)(cid:98)(cid:74)(cid:67)(cid:94)(cid:112)(cid:67)(cid:59)(cid:63)(cid:74)(cid:112)(cid:84)(cid:59)(cid:98)(cid:67)(cid:94)(cid:76)(cid:59)(cid:81)(cid:7)(cid:112)
(cid:96)(cid:109)(cid:96)(cid:98)(cid:67)(cid:84)(cid:112)(cid:88)(cid:94)(cid:112)(cid:84)(cid:67)(cid:98)(cid:74)(cid:88)(cid:65)(cid:112)(cid:81)(cid:76)(cid:96)(cid:98)(cid:67)(cid:65)(cid:112)(cid:76)(cid:96)(cid:112)(cid:94)(cid:67)(cid:81)(cid:67)(cid:102)(cid:59)(cid:86)(cid:98)(cid:112)(cid:98)(cid:88)(cid:112)(cid:109)(cid:88)(cid:100)(cid:94)(cid:112)(cid:96)(cid:98)(cid:100)(cid:65)(cid:109)(cid:10)(cid:112)(cid:36)(cid:69)(cid:112)(cid:109)(cid:88)(cid:100)(cid:112)(cid:59)(cid:94)(cid:67)(cid:112)(cid:86)(cid:88)(cid:98)(cid:112)(cid:96)(cid:100)(cid:94)(cid:67)(cid:112)(cid:76)(cid:69)(cid:112)(cid:59)(cid:112)(cid:81)(cid:76)(cid:96)(cid:98)(cid:112)(cid:76)(cid:98)(cid:67)(cid:84)(cid:112)(cid:59)(cid:90)(cid:90)(cid:81)(cid:76)(cid:67)(cid:96)(cid:112)(cid:98)(cid:88)(cid:112)(cid:109)(cid:88)(cid:100)(cid:94)(cid:112)(cid:94)(cid:67)(cid:96)(cid:67)(cid:59)(cid:94)(cid:63)(cid:74)(cid:7)(cid:112)(cid:94)(cid:67)(cid:59)(cid:65)(cid:112)(cid:98)(cid:74)(cid:67)(cid:112)(cid:59)(cid:90)(cid:90)(cid:94)(cid:88)(cid:90)(cid:94)(cid:76)(cid:59)(cid:98)(cid:67)(cid:112)(cid:96)(cid:67)(cid:63)(cid:98)(cid:76)(cid:88)(cid:86)(cid:112)(cid:61)(cid:67)(cid:69)(cid:88)(cid:94)(cid:67)(cid:112)(cid:96)(cid:67)(cid:81)(cid:67)(cid:63)(cid:98)(cid:76)(cid:86)(cid:71)(cid:112)(cid:59)(cid:112)(cid:94)(cid:67)(cid:96)(cid:90)(cid:88)(cid:86)(cid:96)(cid:67)(cid:10)(cid:112)