UCLA
UCLA Previously Published Works

Title
A single-cell transcriptomic atlas characterizes ageing tissues in the mouse

Permalink
https://escholarship.org/uc/item/7429b0mh

Journal
Nature, 583(7817)

ISSN
0028-0836

Authors
Almanzar, Nicole
Antony, Jane
Baghel, Ankit S
et al.

Publication Date
2020-07-23

DOI
10.1038/s41586-020-2496-1

Peer reviewed

eScholarship.org

Powered by the California Digital Library
University of California

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

HHS Public Access
Author manuscript
Nature. Author manuscript; available in PMC 2021 June 29.

Published in final edited form as:

Nature. 2020 July ; 583(7817): 590–595. doi:10.1038/s41586-020-2496-1.

A Single Cell Transcriptomic Atlas Characterizes Aging Tissues
in the Mouse

The Tabula Muris Consortium*

Abstract

Aging is characterized by a progressive loss of physiological integrity, leading to impaired
function and increased vulnerability to death1. Despite rapid advances over recent years, many of
the molecular and cellular processes which underlie progressive loss of healthy physiology are
poorly understood2. To gain a better insight into these processes we have created a single cell
transcriptomic atlas across the life span of Mus musculus which includes data from 23 tissues and
organs. We discovered cell-specific changes occurring across multiple cell types and organs, as
well as age related changes in the cellular composition of different organs. Using single-cell
transcriptomic data we were able to assess cell type specific manifestations of different hallmarks
of aging, such as senescence3, genomic instability4 and changes in the organism’s immune
system2. This Tabula Muris Senis provides a wealth of new molecular information about how the
most significant hallmarks of aging are reflected in a broad range of tissues and cell types.

We performed single cell RNA sequencing on more than 350,000 cells from male and
female C57BL/6JN mice belonging to six age groups ranging from one month (human early
childhood equivalent) to thirty months (human centenarian equivalent) (Figure 1a). We
prepared single cell suspensions of the bladder, bone marrow, brain (cerebellum, cortex,
hippocampus and striatum), fat (brown, gonadal, mesenteric and subcutaneous), heart and
aorta, kidney, large intestine, limb muscle and diaphragm, liver, lung, mammary gland,
pancreas, skin, spleen, thymus, tongue and trachea for all mice. Data were collected for all
six age groups using microfluidic droplets (droplet), while the 3m, 18m and 24m time points
were also analyzed using single cells sorted in microtiter well plates (FACS) (Extended Data

Reprints and permissions information is available at www.nature.com/reprints.
Correspondence and requests for materials should be addressed to Stephen R. Quake (steve@quake-lab.org), Tony Wyss-Coray
(twc@stanford.edu) or Spyros Darmanis (spyros.darmanis@czbiohub.org).
Author contributions See author list for full contributions.
*A list of participants and their affiliations appears in the online version of paper.
Data and code availability
The entire dataset can be explored interactively at tabula-muris-senis.ds.czbiohub.org. Gene counts and metadata are available from
figshare (https://doi.org/10.6084/m9.figshare.8273102.v2) and GEO (GSE132042), the code used for the analysis is available from
GitHub (https://github.com/czbiohub/tabula-muris-senis) and the raw data are available from a public AWS S3 bucket (https://
s3.console.aws.amazon.com/s3/buckets/czb-tabula-muris-senis/).

Reporting summary
Further information on research design is available in the Nature Research Reporting Summary linked to this paper.

Ethics declarations
Competing interests
The authors declare no competing interests.

Supplementary Information is available in the online version of the paper.

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Page 2

Figures 1-3; Supplementary Tables 1&2). Due to technical constraints, not every tissue was
analyzed at all timepoints; a complete list is in Extended Data Figure 4a. The droplet data
allow large numbers of cells to be analyzed using 3’ end counting, while the FACS data
allow for higher sensitivity measurements over smaller numbers of cells as well as sequence
information across the entire transcript length. Analyzing multiple organs from the same
animal enables data controlled for age, environment, and epigenetic effects.

The previously published 3m time point, referred to as the Tabula Muris5, represents ~20%
of the cells in the entire dataset and was used as a basis to perform semi-automated cell type
annotation of the additional time points (Figure 1b, Extended Data Figure 4b). Using this
approach, we were able to automatically annotate over 70% of the cells. All the automated
cell annotations were reviewed and approved by human experts, and the remaining cells
were annotated by hand, creating one of the largest manually curated single cell
transcriptomic resources in existence. Many of these cell types have not previously been
obtained in pure populations, and these data provide a wealth of new information on their
characteristic gene-expression profiles. Out of 529,823 total cells sequenced, 110,824 cells
for FACS and 245,389 cells for droplet passed our strict filtering criteria (Extended Data
Figure 4b) and were annotated (Extended Data Figure 2a,b), separately for each tissue and
method; the remaining cells are also included in the on-line dataset but were not used for
further analysis here. To investigate whether cell annotations were consistent across the
entire organism, we used bbknn6 to correct for method-associated batch effects
(Supplementary Table 3). Following batch correction, we clustered all cells using an
unbiased, graph-based clustering approach7,8 (Figure 1c,d) and assessed the co-occurrence
of similarly annotated cells in the same clusters. For example, cells annotated as B cells or
endothelial cells tend to occupy the same clusters irrespectively of their tissue of origin or
method with which they were processed (Figure 1e,f; Extended Data Figure 1g-l).

Tabula Muris Senis enables discovery of aging related changes in specific cell types. Single
cell data enables one to resolve whether gene expression changes observed in bulk
experiments are due to changes in gene expression in each cell of the population, or whether
the gene expression in each cell stays constant but the number of cells of that type changes,
or both. In a global analysis of gene expression changes using the Tabula Muris Senis and
bulk RNAseq from tissues9, we observed that in many cases changes in gene expression are
due to both changes in the numbers of cells in a population and to changes in the gene
expression levels in each cell (Extended Data Figure 5a,b). As one specific example, we
investigated how the fraction of cells expressing of Cdkn2a changes with age. Cdkn2a/p16 is
one of the most commonly used markers of senescence10 and an important hallmark of
aging11, and the proportion of cells expressing the gene more than doubled in older animals
in both FACS (Figure 2a) and droplet (Figure 2b), accompanied by a 2-fold increase in the
actual expression level of p16 by those cells that did express it (Figure 2c,d). Interestingly,
the fraction of cells expressing p16 in the 30m mice is smaller than at 24m, perhaps because
long-living animals have a slower rate of senescence. Using a list of previously characterized
senescence markers12–15 we plotted the fraction of cells expressing each marker across all
age groups (Supplementary Table 4). Cdkn2a has the highest correlation between aging and
fraction, and other genes with positive correlation include E2f216, Lmnb117,18 and Tnf and
Itgax19. For some genes the fraction of cells expressing decreased with age, including

Nature. Author manuscript; available in PMC 2021 June 29.

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Page 3

members of the Sirt family (Sirt3, Sirt4 and Sirt5); this is consistent with previous literature
finding that sirtuin is essential in delaying cellular senescence20,21.

The cellular composition of each tissue tends to vary with age, and we investigated changes
for tissues with at least three time points (Supplementary Table 5). Since dissociation does
not affect all cell types in a tissue equally, changes in the relative composition of a given cell
type with age are more meaningful than comparing proportions of different cell types at a
single age22–24. The bladder has pronounced changes in cell type composition with age
(Figure 2e). While the mesenchymal compartment of this tissue decreases by a factor of
three over the lifetime of the mouse (Figure 2e left), the urothelial compartment increases by
a similar amount (Figure 2e right). The observation that the bladder urothelial cells increase
with age is concordant with known age-related urothelial changes25. Differential gene
expression (DGE) analysis of overall tissue changes with age revealed that stromal-
associated genes (Col1a1, Col1a2, Col3a1, Dcn) are downregulated while epithelial-
associated genes (Krt15, Krt18, Sfn) are upregulated, supporting the compositional
observations (Figure 2f; Supplementary Table 6). The decline of the endothelial population
suggests that bladder aging in mice may be associated with lower organ vascularization,
consistent with recent findings26,27 and with the observed downregulation of vasculature
associated genes Htra1 and Fos (Figure 2f; Supplementary Table 6). The increase in the
leukocyte population could indicate an inflammatory tissue microenvironment, a common
hallmark of aging which is consistent with literature on overactive bladders28 and supported
by a significant overexpression of Lgals3, Igfbp2 and Ly6d across the tissue (Figure 2f;
Supplementary Table 6) and by the overexpression of immune response associate genes such
as Tnfrsf12a and Cdkn1a, by both bladder (mesenchymal) cells and bladder urothelial cells
(Supplementary Table 6). Moreover, when comparing across ages, we observed that old
leukocytes show increased expression of pro-inflammatory markers, such as Cd14, Lgals3
and Tnfrsf12a, and decreased expression of anti-inflammatory ones, such as Cd9 and Cd81
(Supplementary Table 6).

Age-dependent changes in the kidney include a decrease in the relative abundance of
mesangial cells, capillary endothelial cells, loop of Henle ascending limb epithelial cells and
loop of Henle thick ascending limb epithelial cells (Figure 2g). Both mesangial cells and
capillary endothelial cells are core glomerular cells and their relative abundances reduction
(Figure 2g top panels), together with a tissue-wide reduction of Egf and Atp1a1 expression
(Figure 2h; Supplementary Table 6) suggest impaired glomerular filtration rate29,30.
Interestingly, local Atp1a1 expression actually increases with age in both capillary
endothelial cells and mesangial cells, suggesting that a compensation mechanism
counteracts the effects of the cell proportion declining with age. This finding is reinforced by
differential gene expression results indicating that uromodulin (Umod), the most abundant
protein in urine31, is also reduced in expression across the tissue. Umod is produced by the
epithelial cells that line the thick ascending limb, and therefore given the relative decrease in
the proportion of epithelial cells in the ascending and thick ascending limb, our results
suggest that normal kidney functions are impaired32 (Figure 2g bottom panels, Figure 2h;
Supplementary Table 6). As with Atp1a1, we see that Umod expression increases in a cell
type whose abundance decreases with age, leading to an overall reduction of Umod
expression in the organ.

Nature. Author manuscript; available in PMC 2021 June 29.

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Page 4

In spleen the proportion of T cells decreases with age while the relative amount of plasma
cells increases (Figure 2i). This is supported by upregulation of B/plasma cell markers
(Cd79a, Igj; Figure 2j; Supplementary Table 6) and downregulation of Cd3d (Figure 2j;
Supplementary Table 6). Similarly, in mammary gland we observed a decline of the T cell
population (Extended Data Figure 5c). Age-related decline of T cell populations has been
associated with increased risk of infectious disease and cancer33 and our results suggest this
may also happen in spleen and mammary gland. Moreover, AP1 transcription factors34
(Junb, Jund and Fos) were upregulated with age (Extended Data Figure 5d; Supplementary
Table 6), consistent with the observation that normal involution of the mammary gland is
accompanied by increased expression of this gene family35.

The liver also displays changing tissue compositions with age, as the relative number of
hepatocytes decreases with age (Extended Data Figure 6a-d), which is supported by the
reduction in the expression of albumin (Alb; Extended Data Figure 6e; Supplementary Table
6). DGE showed an increased immune signature, as illustrated by overexpression of H2-Aa,
H2-Ab1, H2-D1, H2-Eb1, Cd74, Lyz2 and others (Extended Data Figure 6e). Previous
findings suggested that pro-inflammatory macrophages drive cellular senescence and
identified Il1b as a gene whose liver expression was remarkably different with age12
(Extended Data Figure 6f). We stained liver Kupffer cells (Extended Data Figure 6g) with
Clec4f and found the number of Clec4f+ cells does not change with age, consistent with the
results of the tissue composition analysis (Supplementary Table 7; Extended Data Figure
6h). However, when co-staining with Il1b, we found an increase with age in the number of
cells expressing Clec4f and Il1b (Extended Data Figure 6h-j). Il1b has low expression in
normal physiological conditions36. Specific blocking of IL1-RI in hepatocytes has been
shown to attenuate cell death upon injury, supporting the idea that increased expression of
Il1b in Kupffer cells is typically a poor prognostic37. Regarding immune defense within the
liver, sinusoidal endothelial cells (LSECs) play a unique role, being the main carriers of the
mannose receptor (Mrc1) in the liver38 (Extended Data Figure 6k). Our findings identified
increased Mrc1 age-related expression in Kupffer cells, while the overall expression of Mrc1
in liver endothelial cells was reduced with age (Supplementary Table 6). By performing in
situ RNA staining for Mrc1 alongside classical LSEC marker Pecam1 (Supplementary Table
7; Extended Data Figure 6l), we found that the number of Mrc1 expressing LSECs increased
with age (Extended Data Figure 6m-o). While the Mrc1 expression did not increase with age
in LSECs (Supplementary Table 6), the overall number of cells expressing Mrc1 did
increase significantly with age (Extended Figure 6n). LSECs have been found to have a
reduced endocytic capacity in aged livers, while it has been suggested that LSECs proliferate
after injury or that bone-marrow derived LSECs progenitors are recruited to the liver. This
suggests that changes in LSEC gene signatures with age are linked closely with their
function in immune response.

Genomic instability is among the most widely studied aging hallmarks1 and the full-length
transcript data enables analysis of somatic mutation accumulation with age. We used the
Genome Analysis ToolKit (GATK)39 to perform SNP discovery across all FACS samples
simultaneously (Supplementary Table 8)40,41. We focused on genes expressed in at least
75% of cells for each age group within a particular tissue and observed an age-related
increase in the number of mutations across all of the organs we analyzed (Figure 3;

Nature. Author manuscript; available in PMC 2021 June 29.

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Page 5

Extended Data Figure 7a,c,e), with tongue and bladder being the most affected. We
controlled for sequencing coverage and gene expression levels (Extended Data Figure
8a,c,e), and verified that the number of mutations exceeded technical errors due to
amplification and sequencing errors, which can be estimated using ERCC controls that were
spiked into each well42 (Figure 3; Extended Data Figure 7b,d,f; Extended Data Figure
8b,d,f). Despite the fact that it is difficult to infer absolute genome-wide mutation rates from
the transcriptome, which is known to inflate apparent mutational rates for a variety of
reasons42, the observed trend is a useful indirect estimate of mutational frequency and
genome stability.

Aging also affects the immune system2, and we analyzed clonal relationships between B-
cells and T-cells throughout the organism. We computationally reconstructed the sequence of
the B-cell receptor (BCR) and T-cell receptor (TCR) for B and T cells present in the FACS
data using singlecell-ige and TraCeR, respectively43,44. BCRs were assembled for 6,050
cells (Figure 4a, Extended Data Figure 9a) and TCRs for 6,000 cells (Figure 4b, Extended
Data Figure 9a). The number of cells with assembled BCRs was 1,818 for 3m, 1,356 for
18m and 2,876 for 24m old mice. We parsed the singlecell-ige43 output to define B-cell
clonotypes based on the sequence of the assembled BCR (Supplementary Table 9) and found
that while most of the cells at 3m were not part of a clone (9% were part of a clonal family),
the number of B-cells belonging to a clonotype doubled at 18m (20%) when compared to
3m and doubled again from 18m to 24m (~38%). The number of cells with assembled TCRs
were roughly equal between 3m, 18m and 24m (2,076, 2,056 and 1,868 cells, respectively).
Clonotype assignment is part of the output obtained by TraCeR44 (Supplementary Table 9).
Interestingly, only ~3% (55 out of 1,895) of the cells at 3m were part of a clone. For 18m
and 24m, ~23% (479 out of 2,056) and ~20% (348 out of 1,780) of the cells, respectively,
were part of a clone, indicating again an increase in clonality of the T-cell repertoire at later
ages. These changes in clonality for both B and T cell repertoires are noteworthy because
they suggest that the immune system of a 24m mouse is less likely to respond to new
pathogens, corroborating literature suggesting that older individuals have higher
vulnerability to new infections and lower benefits from vacination45,46.

Finally, we computed an overall diversity score to identify which cell types were more
susceptible to changes with age (Extended Data Figure 10). The diversity score is computed
as the Shannon entropy of the cluster assignment and then regressed against age to provide a
p-value (see Methods). We observed significant changes in diversity affecting cells of the
immune system originating from the brain and the kidney (Figure 4c, Extended Data Figure
11a,b). These results were not confounded by the number of genes expressed per cell
(Extended Data Figure 11c,d). In brain myeloid microglial cells, the majority of young (3m)
microglia occupy clusters 1 and 6, while old (18m, 24m) microglia constitute the vast
majority of cells in clusters 10, 12 and 14 (Figure 4d). Trajectory analysis suggests that
young microglia go through an intermediate state, represented by the clusters mostly
occupied by 18m microglial cells before acquiring the signature of old microglia (Extended
Data Figure 11e). Clusters 10, 12 and 14 are mainly comprised of 18- and 24-month old
microglia. These cells up-regulate MHC class I genes (H2-D1, H2-K1, B2m), along with
genes associated with degenerative disease (e.g. Fth1)47,48. When contrasting with clusters 1
and 6, which contain mostly 3m microglia, clusters 10, 12 and 14 gene expression is

Nature. Author manuscript; available in PMC 2021 June 29.

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Page 6

enriched with interferon responsive or regulatory genes (e.g. Oasl2, Oas1a, Ifit3, Rtp4, Bst2,
Stat1, Irf7, Ifitm3, Usp18, Ifi204, Ifit2), suggesting an expansion of this small pro-
inflammatory subset of microglia in the aging brain49. Moreover, the list of differentially
expressed genes between “young” and “old” clusters resembled the Alzheimer’s disease
specific microglial signature previously reported47, with 55 out of the top 200 differential
expressed genes being shared between the two differential gene expression lists (Figure 4e;
Supplementary Table 10). Regarding kidney macrophages, we found two clusters that
remarkably changed their composition with age. Cluster 10 is primarily composed of cells of
1m- and 3-month old mice while cluster 13 is mostly composed of cells of 18-, 21-, 24- and
30-month old mice (Figure 4f). Differential gene expression revealed that cluster 10 is
enriched for an M2-macrophage gene signature (e.g. Il10, H2-Eb1, H2-Ab1, H2-Aa, Cd74,
C1qa, Cxcl16, Hexb, Cd81, C1qb, Cd72) while cluster 13 resembles a M1-proinflammatory
macrophage state50 (e.g. Hp, Itgal, Spex1, Gngt2) (Extended Data Figure 11f;
Supplementary Table 10).

The Tabula Muris Senis is a comprehensive resource for the cell biology community which
offers a detailed molecular and cell-type specific portrait of aging. We view such cell atlas as
an essential companion to the genome: the genome provides a blueprint for the organism but
does not explain how genes are used in a cell type specific manner or how the usage of genes
changes over the lifetime of the organism. The cell atlas provides a deep characterization of
phenotype and physiology and serves as a reference for understanding many aspects of the
cell biological changes that mammals undergo during their lifespan.

Methods

All data, protocols, analysis scripts and an interactive data browser are publicly available.

Experimental Procedures

Mice and organ collection

Male and virgin female C57BL/6JN mice were shipped from the National Institute on Aging
colony at Charles River (housed at 67–73 °F) to the Veterinary Medical Unit (VMU; housed
at 68–76 °F)) at the VA Palo Alto (VA). At both locations, mice were housed on a 12-h light/
dark cycle and provided food and water ad libitum. The diet at Charles River was NIH-31,
and Teklad 2918 at the VA VMU. Littermates were not recorded or tracked, and mice were
housed at the VA VMU for no longer than 2 weeks before euthanasia, with the exception of
mice older than 18 months, which were housed at the VA VMU beginning at 18 months of
age. Before tissue collection, mice were placed in sterile collection chambers at 8 am for 15
min to collect fresh fecal pellets. After anaesthetization with 2.5% v/v Avertin, mice were
weighed, shaved, and blood was drawn via cardiac puncture before transcardial perfusion
with 20 ml PBS. Mesenteric adipose tissue was then immediately collected to avoid
exposure to the liver and pancreas perfusate, which negatively affects cell sorting. Isolating
viable single cells from both the pancreas and the liver of the same mouse was not possible;
therefore, two males and two females were used for each. Whole organs were then dissected
in the following order: large intestine, spleen, thymus, trachea, tongue, brain, heart, lung,
kidney, gonadal adipose tissue, bladder, diaphragm, limb muscle (tibialis anterior), skin

Nature. Author manuscript; available in PMC 2021 June 29.

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Page 7

(dorsal), subcutaneous adipose tissue (inguinal pad), mammary glands (fat pads 2, 3 and 4),
brown adipose tissue (interscapular pad), aorta and bone marrow (spine and limb bones).
Organ collection concluded by 10 am. After single-cell dissociation as described below, cell
suspensions were either used for FACS of individual cells into 384-well plates, or for
preparation of the microfluidic droplet library. All animal care and procedures were carried
out in accordance with institutional guidelines approved by the VA Palo Alto Committee on
Animal Research.

Tissue dissociation and sample preparation

All tissues were processed as previously described5.

Sample size, randomization and blinding

No sample size choice was performed before the study. Randomization and blinding were
not performed: the authors were aware of all data and metadata-related variables during the
entire course of the study.

Single-cell methods

All protocols used in this study are described in detail elsewhere5. Those include: i)
preparation of lysis plates, ii) FACS sorting, iii) cDNA synthesis using the Smart-seq2
protocol51,52, iv) library preparation using an in-house version of Tn553,54,v) library pooling
and Quality control and vi) sequencing. For further details please refer to http://dx.doi.org/
10.17504/protocols.io.2uwgexe

Microfluidic droplet single-cell analysis

Single cells were captured in droplet emulsions using the GemCode Single-Cell Instrument
(10x Genomics) and scRNA-seq libraries were constructed as per the 10x Genomics
protocol using GemCode Single-Cell 3′ Gel Bead and Library V2 Kit. In brief, single cell
suspensions were examined using an inverted microscope, and if sample quality was deemed
satisfactory, the sample was diluted in PBS with 2% FBS to a concentration of 1000 cells
per μl. If cell suspensions contained cell aggregates or debris, two additional washes in PBS
with 2% FBS at 300gfor 5 min at 4 °C were performed. Cell concentration was measured
either with a Moxi GO II (Orflo Technologies) or a haemocytometer. Cells were loaded in
each channel with a target output of 5,000 cells per sample. All reactions were performed in
the Biorad C1000 Touch Thermal cycler with 96-Deep Well Reaction Module. 12 cycles
were used for cDNA amplification and sample index PCR. Amplified cDNA and final
libraries were evaluated on a Fragment Analyzer using a High Sensitivity NGS Analysis Kit
(Advanced Analytical). The average fragment length of 10x cDNA libraries was quantitated
on a Fragment Analyzer (AATI), and by qPCR with the Kapa Library Quantification kit for
Illumina. Each library was diluted to 2 nM, and equal volumes of 16 libraries were pooled
for each NovaSeq sequencing run. Pools were sequenced with 100 cycle run kits with 26
bases for Read 1, 8 bases for Index 1, and 90 bases for Read 2 (Illumina 20012862). A PhiX
control library was spiked in at 0.2 to 1%. Libraries were sequenced on the NovaSeq 6000
Sequencing System (Illumina).

Nature. Author manuscript; available in PMC 2021 June 29.

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Page 8

Computational methods

Data extraction

Sequences from the NovaSeq were de-multiplexed using bcl2fastq version 2.19.0.316. Reads
were aligned using to the mm10plus genome using STAR version 2.5.2b with parameters
TK. Gene counts were produced using HTSEQ version 0.6.1p1 with default parameters,
except ‘stranded’ was set to ‘false’, and ‘mode’ was set to ‘intersection-nonempty’.
Sequences from the microfluidic droplet platform were de-multiplexed and aligned using
CellRanger version 2.0.1, available from 10x Genomics with default parameters.

Data pre-processing

Gene count tables were combined with the metadata variables using the Scanpy55 Python
package version 1.4.2. We removed genes not expressed in at least 3 cells and then cells that
did not have at least 250 detected genes. For FACS we removed cells with less than 5000
counts and for droplet cells with less than 2500 UMIs. The data was then normalized using
size factor normalization such that every cell has 10,000 counts and log transformed. We
computed highly variable genes using default parameters and then scaled the data to a
maximum value of 10. After we computed PCA, neighborhood graph and clustered the data
using Louvain7 and Leiden8 methods. The data was visualized using UMAP projection.
When performing batch correction to remove the technical artifacts introduced by the
technologies, we replaced the neighborhood graph computation with bbknn6. Step-by-step
instructions to reproduce the pre-processing of the data are available from GitHub.

Cell type annotation

To define cell types we analyzed each organ independently but combining all ages. In a
nutshell, we performed principal component analysis on the most variable genes between
cells, followed by Louvain and Leiden graph-based clustering. Next we subset the data for
3m (Tabula Muris5) and compute how many cell types map to each individual cluster. For
the clusters that we had a single 1:1 mapping (cluster:cell type) we propagate the
annotations for all ages; in case there is a 1:many mapping we flagged that cluster for
manual validation. Step-by-step instructions to reproduce this method are available from
GitHub. For each cluster, we provide annotations in the controlled vocabulary of the cell
ontology56 to facilitate inter-experiment comparisons. Using this method, we were able to
annotate automatically (~1min per tissue) over 70% of the dataset. The automatic
annotations were then reviewed by each of the tissue experts leading to a fully curated
dataset for all the cell types in Tabula Muris Senis.

Tissue cell composition analysis

For each tissue and age, we computed the relative proportion of each cell type. Next we used
scipy.stats linregress to regress the relative tissue-cell type changes against age and
considered significant the changes with p-value<0.05 for a hypothesis test whose null
hypothesis is that the slope is zero, using two-sided Wald Test with t-distribution of the test
statistic and a r2>0.5.

Nature. Author manuscript; available in PMC 2021 June 29.

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Page 9

Differential gene expression

We performed differential gene expression analysis on each tissue with a well-powered
sample size (>100 cells in both young (1m and 3m) and old age group (18m, 21m, 24m and
30m)). We used a linear model57 treating age as a numerical variable while controlling for
sex and technology. We applied a false-discovery rate (FDR) threshold of 0.01 and an age
coefficient threshold of 0.005 (corresponding to ~10% fold change).

In Situ RNA Hybridization and quantification.

In situ RNA hybridization was performed using the Advanced Cell Diagnostics RNAscope®
Multiplex Fluorescent Detection kit v2 (323110, Bio-techne) according to the
manufacturer’s instructions. Staining of mouse liver specimens was performed using 5μm
paraffin-embedded thick sessions. Mouse livers were fixed in 10% formalin buffer saline
(HT501128, Sigma Aldrich) for 24h at room temperature before paraffin embedding. For
multiplex staining the following probes were used; Clec4f (Mm-Clec4f 480421, Il1b (Mm-
Il1b 316891-C2), Pecam1 (Mm-Pecam-1 316721), Mrc1 (Mm-Mrc1 437511-C3). Slides
were counter stained with Prolong gold antifade reagent with DAPI (P36931, Life
technologies). Mounted slides were imaged on a Leica DM6 B fluorescent microscope
(Leica Biosystems). Image quantification was performed using the starfish open source
image-based transcriptomics pipeline (please refer to Starfish: Open Source Image Based
Transcriptomics and Proteomics Tools available from http://github.com/spacetx/starfish and
58)

Comparison between bulk and single-cell datasets

The differential gene analysis was defined on a per tissue basis. First, we investigated genes
based on the single-cell data. We only considered cells from male animals and perform our
analysis on the log (1 + CPM) transformed single-cell count matrices. Note that
normalization of the single-cell data was done on a per cell basis. We defined two groups of
cells based on age: young cells with age <= 3 months (Y) and old cells with age > 3 months
(O). For each gene we compute the log2 fold-change of cell and read counts between O and
Y. We defined cell count as the fraction of cells that express the gene. Similarly, we defined
read count as the mean read count of the gene in the cells that express it. The calculated log2
fold-changes of a gene reflect its expression changes with aging within the single-cell data.
Next we analyze each gene based on the bulk data. We computed the Spearman (Sp)
correlation of bulk DESeq2 normalized gene expression with aging. We defined two groups
of genes based on the bulk data, increasing with age Sp > 0.7 (U) and decreasing with age
Sp < −0.7 (D). Finally, we compared the single-cell data based log2 fold-changes between
the bulk data defined groups U and D. Specifically, we run Wilcoxon–Mann–Whitney test in
order to understand if log2 fold-changes of cell or read counts could distinguish between the
two groups. We used the U statistic for effect size.

T-Cell processing

We used TraCeR44 version 0.5 to identify T-Cell clonal populations. We ran tracer assemble
with --species Mmus set. We then ran tracer summarise with –species Mmus to create the
final results. We used the following versions for TraCeR dependencies: igblast version 1.7.0,

Nature. Author manuscript; available in PMC 2021 June 29.

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

kallisto version v0.43.1, Salmon version 0.8.2, Trinity version v2.4.0, GRCm38 reference
genome. Step-by-step instructions to reproduce the processing of the data are available from
GitHub.

Page 10

B-Cell processing

We used singlecell-ige43 version eafb6d126cc2d6511faae3efbd442abd7c6dc8ef (https://
github.com/dcroote/singlecell-ige) to identify B-Cell clonal populations. We used the default
configuration settings except we set the species to mouse. Step-by-step instructions to
reproduce the processing of the data are available from GitHub.

Mutation analysis

We used samtools59 version 1.9 and GATK39 version v4.1.1.0 for mutation analysis. We
used samtools faidx to create our index file. Then we used GATK CreateSequenceDictionary
and GRCm38, as the reference, to create our sequence dictionary. Next we used GATK
AddOrReplaceReadGroups to create a single read group using parameters -RGID 4 -RGLB
lib1 -RGPL illumina -RGPU unit1 -RGSM 20. Finally we used GATK HaplotypeCaller to
call the mutations. We disabled the following read filters: MappingQualityReadFilter,
GoodCigarReadFilter, NotSecondaryAlignmentReadFilter, MappedReadFilter,
MappingQualityAvailableReadFilter, NonZeroReferenceLengthAlignmentReadFilter,
NotDuplicateReadFilter, PassesVendorQualityCheckReadFilter, and WellformedReadFilter,
but kept all other default settings. The results were summarized per gene in the form of a
mutation count per cell table. We started by removing genes mutated in over 60% of cells, to
eliminate the possible bias of germline mutations. Then for each tissue we selected genes
expressed in at least 75% of the cells for all the time points to avoid confounding the
mutation results with differential gene expression associated with age. Next we computed
the average number of mutations in the gene set (or ERCC spike-in controls) per cell and
also the average number of raw counts (Supplementary Table 8) and plotted the different
distributions. Step-by-step instructions to reproduce the processing of the data are available
from GitHub.

Trajectory analysis

We used partition-based graph abstraction (PAGA60) to reconstruct the aging trajectory in
brain microglial cells. Step-by-step instructions to reproduce the processing of the data are
available from GitHub.

Diversity score

The raw FACS or droplet dataset were used as the input. We filtered genes expressed in
fewer than 5 cells, filtered cells if expressing fewer than 500 genes and discarded cells with
total number of counts less than 5000. Next we performed size factor normalization such
that every cell had 1e4 counts and performed a log1p transformation. This was followed by
clustering, where we clustered every tissue and every tissue-cell type for every mouse
separately using 6 different configurations: resolution parameters (0.3, 0.5, 0.7) * clustering
method (Louvain, Leiden). This is to provide a robust clustering result. For each
combination (each tissue-mouse and each tissue-cell_type-mouse), we computed the

Nature. Author manuscript; available in PMC 2021 June 29.

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Page 11

clustering diversity score as the Shannon entropy of the cluster assignment. We then
regressed the diversity score against age to detect the systematic increase/decrease of
clustering diversity with respect to age. FDR was used to correct for multiple comparisons.
A tissue or a tissue-cell type was selected if the slope was consistent (having the same sign)
in all 6 clustering configurations and at least 2 out of 6 clustering configurations had
FDR<0.3. For each selected tissue or tissue-cell type, a separate UMAP was computed using
cells from all mice for visualization using Leiden clustering with resolution parameter 0.7.

Interactive Data Browsers

http://tabula-muris-senis.ds.czbiohub.org/

https://tabula-maris-senis.cells.ucsc.edu

Nature. Author manuscript; available in PMC 2021 June 29.

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Extended Data

Page 12

Extended Data Figure 1. Overview of Tabula Muris Senis (cont.)
a,b, UMAP plot of all cells collected for FACS colored by tissue (a) or age (b). c, UMAP
plot of all cells collected by FACS, colored by organ (Extended Data Figure 4c), overlaid
with the Louvain cluster numbers. n = 110,824 individual cells for FACS. d,e, UMAP plot of
all cells collected for droplet colored by tissue (d) or age (e). f, UMAP plot of all cells
collected by droplet, colored by organ (Extended Data Figure 4c), overlaid with the Louvain
cluster numbers. n = 245,389 individual cells for droplet. g, B cells (top) and endothelial
cells (bottom) in FACS independently annotated for each organ cluster together by unbiased
whole-transcriptome Louvain clustering, irrespectively of the organ they originate from. h, B
cells (and endothelial cells) in droplet independently annotated for each organ cluster
together by unbiased whole-transcriptome Louvain clustering, irrespectively of the organ
where they were found. i,j, UMAP plot of all cells collected colored by method (i) or tissue

Nature. Author manuscript; available in PMC 2021 June 29.

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

(j). n = 356,213 individual cells for FACS and droplet combined. k,l, B cells (k) and
endothelial cells (l) cluster together by unbiased whole-transcriptome Louvain clustering,
irrespectively of the technology with which they were found.

Page 13

Extended Data Figure 2. Overview of Tabula Muris Senis (cont.)
a, Pie chart with the summary statistics for FACS. b, Pie chart with the summary statistics
for droplet. c, Box plot of the number of genes detected per cell for each organ and age for
FACS d, Box plot of the number of reads per cell (log-scale) for each organ and age for
FACS. For c and d, all data are expressed as mean ± s.d. The sample size (number of cells
for each tissue and age) is available in Supplementary Table 1.

Nature. Author manuscript; available in PMC 2021 June 29.

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Page 14

Extended Data Figure 3. Overview of Tabula Muris Senis (cont.)
a, Box plot of the number of genes detected per cell for each organ and age for droplet. b,
Box plot of the number of UMIs per cell (log-scale) for each organ and age for droplet. All
data are expressed as mean ± s.d. The sample size (number of cells for each tissue and age)
is available in Supplementary Table 2.

Nature. Author manuscript; available in PMC 2021 June 29.

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Page 15

Extended Data Figure 4. Overview of Tabula Muris Senis (cont.)
a, Balloon plot showing the number of sequenced cells per sequencing method per organ per
sex per age. b, Schematic analysis workflow. c,d, Tabula Muris Senis color dictionary for
organs and tissues (c) and ages (d).

Nature. Author manuscript; available in PMC 2021 June 29.

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Page 16

Extended Data Figure 5. Comparison of bulk and single-cell datasets and Tissue cell
compositions.
a,b, Aging patterns from bulk and single-cell data are consistent. Strong changes in bulk
gene expression with aging can be either explained by cell or read count-based changes in
single-cell data FACS (a) and droplet (b). Two-sided Wilcoxon–Mann–Whitney indicates
that single-cell data based log2 fold-changes of cell or read counts distinguish between up
and down regulated genes in bulk data. n = 110,824 individual cells for FACS and n =
245,389 individual cells for droplet. c, Mammary gland T cell relative abundances change
significantly with age (p-value<0.05 and r2>0.7 for a hypothesis test whose null hypothesis
is that the slope is zero, using two-sided Wald Test with t-distribution of the test statistic). d,
Top 20 upregulated and downregulated genes in mammary gland computed using MAST57,
treating age as a continuous covariate while controlling for sex and technology. Genes were
classified as significant under an FDR threshold of 0.01 and an age coefficient threshold of
0.005 (corresponding to ~10% fold change). n=6,393; 3,635; and 5,549 individual cells for

Nature. Author manuscript; available in PMC 2021 June 29.

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Page 17

mammary gland 3m; 18m and 21m, respectively. e, Marrow precursor B cell relative
abundances change significantly with age (p-value<0.05 and r2>0.7 for a hypothesis test
whose null hypothesis is that the slope is zero, using two-sided Wald Test with t-distribution
of the test statistic). f, Top 20 upregulated and downregulated genes in marrow computed
using MAST57, treating age as a continuous covariate while controlling for sex and
technology. Genes were classified as significant under an FDR threshold of 0.01 and an age
coefficient threshold of 0.005 (corresponding to ~10% fold change). n=3,027; 8,559; 11,496;
5,216; 12,943 and 13,496 individual cells for marrow 1m; 3m; 18m; 21m; 24m and 30m,
respectively. g, Skin keratinocyte stem cell relative abundances change significantly with age
(p-value<0.05 and r2>0.7 for a hypothesis test whose null hypothesis is that the slope is zero,
using two-sided Wald Test with t-distribution of the test statistic). h, Top 20 upregulated and
downregulated genes in skin computed using MAST57, treating age as a continuous
covariate while controlling for sex and technology. Genes were classified as significant
under an FDR threshold of 0.01 and an age coefficient threshold of 0.005 (corresponding to
~10% fold change). n=2,346; 1,494; 4,352= and 1,122 individual cells for skin 3m; 18m;
21m and 24m, respectively. The p-values for the cell type compositional changes are shown
in Supplementary Table 5.

Nature. Author manuscript; available in PMC 2021 June 29.

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Page 18

Extended Data Figure 6. Cellular changes during aging in the liver.
a, Liver hepatocyte relative abundances change significantly with age (p-value<0.05 and
r2>0.7 for a hypothesis test whose null hypothesis is that the slope is zero, using two-sided
Wald Test with t-distribution of the test statistic). n=2,791; 2,832; 3,806; 2,257; 6,384 and
5,713 individual cells for liver 1m; 3m; 18m; 21m; 24m and 30m, respectively. The p-values
for the cell type compositional changes are shown in Supplementary Table 5. b-d,
Brightfield imaging of hepatocytes across age (b) and respective quantification (c-d). e, Top
10 upregulated and downregulated genes in liver computed using MAST57, treating age as a
continuous covariate while controlling for sex and technology. Genes were classified as
significant under an FDR threshold of 0.01 and an age coefficient threshold of 0.005
(corresponding to ~10% fold change). The sample size is the same as for panel a. f,k, Gene
expression of Il1b and Clec4f (f) and Pecam1 and Mrc1 (k) in the liver droplet dataset for
the six ages. g-j, Staining of Kupffer cells across age (g) and respective quantification (h-j).

Nature. Author manuscript; available in PMC 2021 June 29.

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

l-o, Staining of liver endothelial cells across ages (l) and respective quantification (m-o). The
white scale bar corresponds to 100µm. For panels c-d, h-j and m-o, all data are expressed as
mean ± s.d. and p-values were obtained using a Welch’s test. The sample size for each group
is available in Supplementary Table 7.

Page 19

Extended Data Figure 7. Mutational burden across tissues in the aging mice (cont.).
a,b, Mean number of somatic mutations in genes and ERCC spike-in controls across all
tissues per age group (3m and 24m (a), 3m and 18m (b), 18m and 24 (c)). Mutations are
presented as the mean number of mutations per gene or ERCC spike-inn per cell.

Nature. Author manuscript; available in PMC 2021 June 29.

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Page 20

Extended Data Figure 8. Mutational burden across tissues in the aging mice (cont.).
a,b,c, Gene raw expression and ERCC spike-inn control raw expression across all tissues per
age group (3m and 24m (a), 3m and 18m (b), 18m and 24 (c)). Raw expression are
presented as the mean number of counts per gene or ERCC spike-inn control per cell.

Nature. Author manuscript; available in PMC 2021 June 29.

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Page 21

Extended Data Figure 9. Immune repertoire clonality analysis.
a, B-cell clonal families. For each time point, the clonal families are represented in a tree
structure for which the central node is age. Connected to the age node there is an additional
node (dark gray) that represents each animal and the clonal families are depicted for each
animal. For each clonal family, cells that are part of that family are colored by the organ of
origin. b, T-cell clonal families. For each time point, clonal families are represented in a tree
structure for which the central node is age. Connected to the age node there is an additional
node (dark gray) that represents each animal and the clonal families are depicted for each
animal. For each clonal family, cells that are part of that family are colored by the organ of
origin.

Nature. Author manuscript; available in PMC 2021 June 29.

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Page 22

Extended Data Figure 10. Diversity score summary.
a,b, Heatmap summary of the overall tissue diversity score for FACS (a) and droplet (b).
c,d, Heatmap summary of the tissue cell-type diversity score for FACS (c) and droplet (d).

Nature. Author manuscript; available in PMC 2021 June 29.

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Page 23

Extended Data Figure 11. The aging immune system (cont.)
a,b, Diversity score at different cluster resolutions for FACS brain myeloid microglia cell (a)
and droplet kidney macrophage (b). n = 14 mice for a and n = 16 mice for b. All data are
expressed as quantiles. The p-values were obtained using a linear regression and two-sided
F-test, adjusted for multiple comparison using the Benjamini-Hochberg procedure (i.e., bh-p
value). c,d, Diversity score correlation with the number of genes expressed per tissue (c) or
tissue cell-type (d). The red line corresponds to the linear regression curve. e, Trajectory
analysis for brain myeloid microglia cell. f, Heatmap showing differential gene expression
analysis of cluster 10 (mostly young macrophages) versus clusters 13 (mostly old
macrophages). For the complete gene list please refer to Supplementary Table 10.

Supplementary Material

Refer to Web version on PubMed Central for supplementary material.

Nature. Author manuscript; available in PMC 2021 June 29.

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Acknowledgements

We thank Sony Biotechnology for making an SH800S instrument available for this project. Some cell sorting/flow
cytometry analysis for this project was done on a Sony SH800S instrument in the Stanford Shared FACS Facility.
Some fluorescence activated cell sorting (FACS) was done with instruments in the VA Flow Cytometry Core, which
is supported by the US Department of Veterans Affairs (VA), Palo Alto Veterans Institute for Research (PAVIR),
and the National Institutes of Health (NIH). This work was supported by the Chan Zuckerberg Biohub, Department
of Veterans Affairs grant IK6 BX004599 (TWC) and NIH/NIA DP1 AG053015 grant (TWC). We would like to
thank Bruno Tojo for the artwork. We thank Chenling Xu and Joshua Batson for helpful discussions.

Page 24

The Tabula Muris Consortium

Overall Coordination

Angela Oliveira Pisco1, Aaron McGeever1, Nicholas Schaum2,3, Jim Karkanias1, Norma F.
Neff1, Spyros Darmanis1*, Tony Wyss-Coray3,4,7,8,*, and Stephen R. Quake1,6*

Organ collection and processing

Jane Antony2, Ankit S. Baghel2, Isaac Bakerman2,9,10, Ishita Bansal2, Daniela Berdnik4,
Biter Bilen3, Douglas Brownfield11, Corey Cain12, Michelle B. Chen6, Stephanie D.
Conley1, Spyros Darmanis1, Aaron Demers1, Kubilay Demir2,13, Antoine de Morree2, Tessa
Divita1, Haley du Bois4, Laughing Bear Torrez Dulgeroff2, Hamid Ebadi1, F. Hernán
Espinoza11, Matt Fish2,13,14, Qiang Gan3, Benson M. George2, Astrid Gillich11, Foad
Green1, Geraldine Genetiano1, Xueying Gu14, Gunsagar S. Gulati2, Michael Seamus
Haney3, Yan Hang14, Shayan Hosseinzadeh1, Albin Huang3, Tal Iram3, Taichi Isobe2,
Feather Ives1, Robert Jones6, Kevin S. Kao2, Guruswamy Karnam15, Aaron M. Kershner2,
Nathalie Khoury3, Bernhard M. Kiss2,17, William Kong2, Maya E. Kumar17,18, Jonathan
Lam14, Davis P. Lee4, Song E. Lee3, Olivia Leventhal4, Guang Li19, Qingyun Li20, Ling
Liu3, Annie Lo1, Wan-Jin Lu2,11, Maria F. Lugo-Fagundo4, Anoop Manjunath2, Andrew P.
May1, Ashley Maynard1, Marina McKay1, M. Windy McNerney21,22, Ross J. Metzger23,24,
Marco Mignardi1,6, Dullei Min25, Ahmad N. Nabhan11, Norma F. Neff1, Katharine M. Ng11,
Joseph Noh2, Rasika Patkar15, Weng Chuan Peng14, Lolita Penland1, Robert Puccinelli1,
Eric J. Rulifson14, Nicholas Schaum2,3, Shaheen S. Sikandar2, Rahul Sinha2,26–28, Rene V.
Sit1, Daniel Staehli3, Krzysztof Szade2,29, Weilun Tan1, Cristina Tato1, Krissie Tellez14,
Kyle J. Travaglini11, Carolina Tropini30, Lucas Waldburger1, Linda J. van Weele2, Michael
N. Wosczyna3, Jinyi Xiang2, Soso Xue6, Andrew C. Yang6, Lakshmi P. Yerra3, Justin
Youngyunpipatkul1, Fabio Zanini6, Macy E. Zardeneta4, Fan Zhang23,24, Hui Zhang4, Lu
Zhou20

Library preparation and sequencing

Spyros Darmanis1, Shayan Hosseinzadeh1, Ashley Maynard1, Norma F. Neff1, Lolita
Penland1, Rene V. Sit1, Michelle Tan1, Weilun Tan1, Alexander Zee1

Computational Data Analysis

Oliver Hahn3, Lincoln Harris1, Andreas Keller2,5, Benoit Lehallier3, Aaron McGeever1,
Angela Oliveira Pisco1, Róbert Pálovics3, Weilun Tan1, Martin Jinye Zhang31,32

Nature. Author manuscript; available in PMC 2021 June 29.

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Page 25

Cell Type Annotation

Nicole Almanzar25, Jane Antony2, Biter Bilen3, Spyros Darmanis1, Antoine de Morree3,
Oliver Hahn3, Yan Hang14, Mu He33, Shayan Hosseinzadeh1, Tal Iram3, Taichi Isobe2,
Aaron M. Kershner2, Jonathan Lam14, Guang Li19, Qingyun Li20, Ling Liu3, Wan-Jin
Lu2,11, Ashley Maynard1, Dullei Min25, Ahmad N. Nabhan11, Patricia K. Nguyen2,9,10,19,
Weng Chuan Peng14, Angela Oliveira Pisco1, Zhen Qi1, Nicholas Schaum2,3, Joe M.
Segal15, Shaheen S. Sikandar2, Rahul Sinha2,26–28, Rene Sit1, Michelle Tan1, Weilun Tan1,
Kyle J. Travaglini11, Margaret Tsui15, Bruce M. Wang15, Linda J. van Weele2, Michael N.
Wosczyna3, Jinyi Xiang2, Alexander Zee1, Lu Zhou20

Liver staining and data analysis

Rafael Gòmez-Sjöberg1, Angela Oliveira Pisco1, Joe M. Segal15, Margaret Tsui15, Kevin A
Yamauchi1

Microbiome analysis

Bryan Merrill30, Aaron McGeever1, Katharine M. Ng11, Angela Oliveira Pisco1, Carolina
Tropini30, Brian Yu1, Chunyu Zhao1, Katherine Pollard34, Justin Sonnenburg1,30, Kerwyn
Casey Huang1,6,30

Writing Group

Spyros Darmanis1, Angela Oliveira Pisco1, Stephen R. Quake1,6, Tony Wyss-Coray3,4,7,8

Principal Investigators

Ben A. Barres20, Philip A. Beachy2,11,13,14, Charles K. F. Chan35, Michael F. Clarke2,
Spyros Darmanis1, Kerwyn Casey Huang1,6,30, Jim Karkanias1, Seung K. Kim14,36, Mark A.
Krasnow11,13, Maya E. Kumar17,18, Christin S. Kuo11,13,25, Ross J. Metzger23,24, Norma F.
Neff1, Roel Nusse11,13,14, Patricia K. Nguyen2,9,10,19, Thomas A. Rando3,4,7, Justin
Sonnenburg1,30, Bruce M. Wang15, Kenneth Weinberg25, Irving L. Weissman2,26–28, Sean
M. Wu2,9,19, James Zou1,31,37, Stephen R. Quake1,6, Tony Wyss-Coray3,4,7,8

1 Chan Zuckerberg Biohub, San Francisco, California, USA.

2 Institute for Stem Cell Biology and Regenerative Medicine, Stanford University School of
Medicine, Stanford, California, USA.

3 Department of Neurology and Neurological Sciences, Stanford University School of
Medicine, Stanford, California, USA.

4 Veterans Administration Palo Alto Healthcare System, Palo Alto, California, USA.

5 Clinical Bioinformatics, Saarland University, Saarbrücken, Germany.

6 Department of Bioengineering, Stanford University, Stanford, California, USA.

Nature. Author manuscript; available in PMC 2021 June 29.

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Page 26

7 Paul F. Glenn Center for the Biology of Aging, Stanford University School of Medicine,
Stanford, California, USA.

8 Wu Tsai Neurosciences Institute, Stanford University School of Medicine, Stanford,
California, USA.

9 Stanford Cardiovascular Institute, Stanford University School of Medicine, Stanford,
California, USA

10 Department of Medicine, Division of Cardiology, Stanford University School of
Medicine, Stanford, California, USA

11 Department of Biochemistry, Stanford University School of Medicine, Stanford,
California, USA

12 Flow Cytometry Core, V.A. Palo Alto Healthcare System, Palo Alto, California, USA

13 Howard Hughes Medical Institute, USA

14 Department of Developmental Biology, Stanford University School of Medicine,
Stanford, California, USA

15 Department of Medicine and Liver Center, University of California San Francisco, San
Francisco, California, USA

16 Department of Urology, Stanford University School of Medicine, Stanford, California,
USA

17 Sean N. Parker Center for Asthma and Allergy Research, Stanford University School of
Medicine, Stanford, California, USA

18 Department of Medicine, Division of Pulmonary and Critical Care, Stanford University
School of Medicine, Stanford, California,

19 Department of Medicine, Division of Cardiovascular Medicine, Stanford University,
Stanford, California, USA

20 Department of Neurobiology, Stanford University School of Medicine, Stanford, CA USA

21 Mental Illness Research Education and Clinical Center, V.A. Palo Alto Healthcare
System, Palo Alto, California, USA

22 Department of Psychiatry, Stanford University School of Medicine, Stanford, California,
USA

23 Vera Moulton Wall Center for Pulmonary and Vascular Disease, Stanford University
School of Medicine, Stanford, California, USA

24 Department of Pediatrics, Division of Cardiology, Stanford University School of
Medicine, Stanford, California, USA

Nature. Author manuscript; available in PMC 2021 June 29.

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Page 27

25 Department of Pediatrics, Pulmonary Medicine, Stanford University School of Medicine,
Stanford, California, USA

26 Department of Pathology, Stanford University School of Medicine, Stanford, California,
USA

27 Ludwig Center for Cancer Stem Cell Research and Medicine, Stanford University School
of Medicine, Stanford, California, USA

28 Stanford Cancer Institute, Stanford University School of Medicine, Stanford, California,
USA

29 Department of Medical Biotechnology, Faculty of Biophysics, Biochemistry and
Biotechnology, Jagiellonian University, Poland

30 Department of Microbiology & Immunology, Stanford University School of Medicine,
Stanford, California, USA

31 Department of Electrical Engineering, Stanford University, Palo Alto, 94304 USA

32 Department of Epidemiology, Harvard T.H. Chan School of Public Health, Boston,
Massachusetts, USA

33 Department of Physiology, University of California, San Francisco, CA 94158

34 Department of Epidemiology and Biostatistics, University of California, San Francisco,
CA 94158

35 Department of Surgery, Division of Plastic and Reconstructive Surgery, Stanford
University, Stanford, California USA

36 Department of Medicine and Stanford Diabetes Research Center, Stanford University,
Stanford, California USA

37 Department of Biomedical Data Science, Stanford University, Palo Alto, 94304 USA

References

1. López-Otín C, Blasco MA, Partridge L, Serrano M & Kroemer G The Hallmarks of Aging. Cell

153, 1194–1217 (2013). [PubMed: 23746838]

2. Nikolich-Žugich J The twilight of immunity: emerging concepts in aging of the immune system.

Nat. Immunol 19, 10–19 (2018). [PubMed: 29242543]

3. Campisi J Aging, Cellular Senescence, and Cancer. Annu. Rev. Physiol 75, 685–705 (2013).

[PubMed: 23140366]

4. Vijg J & Suh Y Genome Instability and Aging. Physiology 75, 645–668 (2013).
5. Consortium TTM et al. Single-cell transcriptomics of 20 mouse organs creates a Tabula Muris.

Nature 562, 367–372 (2018). [PubMed: 30283141]

6. Polański K et al. BBKNN: fast batch alignment of single cell transcriptomes. Bioinformatics (2019)

doi:10.1093/bioinformatics/btz625.

7. Blondel VD, Guillaume J-L, Lambiotte R & Lefebvre E Fast unfolding of communities in large

networks (2008) doi:10.1088/1742-5468/2008/10/p10008.

Nature. Author manuscript; available in PMC 2021 June 29.

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Page 28

8. Traag VA, Waltman L & Eck N. J. van. From Louvain to Leiden: guaranteeing well-connected

communities. Sci. Rep 9, 5233 (2019). [PubMed: 30914743]

9. Schaum N et al. The murine transcriptome reveals global aging nodes with organ-specific phase and

amplitude. bioRxiv 662254 (2019) doi:10.1101/662254.

10. Rayess H, Wang MB & Srivatsan ES Cellular senescence and tumor suppressor gene p16. Int. J.

Cancer 130, 1715–1725 (2012). [PubMed: 22025288]

11. Hernandez-Segura A, Nehme J & Demaria M Hallmarks of Cellular Senescence. Trends Cell Biol

28, 436–453 (2018). [PubMed: 29477613]

12. Covarrubias AJ et al. Aging-related inflammation driven by cellular senescence enhances NAD
consumption via activation of CD38+ pro-inflammatory macrophages. bioRxiv 609438 (2019)
doi:10.1101/609438.

13. Nagano T et al. Identification of cellular senescence-specific genes by comparative transcriptomics.

Sci. Rep 6, 31758 (2016). [PubMed: 27545311]

14. Carnero A Methods in Molecular Biology. Methods Mol. Biol. Clifton NJ 965, 63–81 (2012).
15. Wang AS & Dreesen O Biomarkers of Cellular Senescence and Skin Aging. Front. Genet 9, 247

(2018). [PubMed: 30190724]

16. Vernier M et al. Regulation of E2Fs and senescence by PML nuclear bodies. Genes Dev 25, 41–50

(2011). [PubMed: 21205865]

17. Dreesen O et al. Lamin B1 fluctuations have differential effects on cellular proliferation and

senescence. J. Cell Biol 200, 605–17 (2013). [PubMed: 23439683]

18. Shah PP et al. Lamin B1 depletion in senescent cells triggers large-scale changes in gene

expression and the chromatin landscape. Genes Dev 27, 1787–99 (2013). [PubMed: 23934658]
19. Li P et al. The inflammatory cytokine TNF-α promotes the premature senescence of rat nucleus

pulposus cells via the PI3K/Akt signaling pathway. Sci. Rep 7, 42938 (2017). [PubMed:
28211497]

20. Saunders LR & Verdin E Sirtuins: critical regulators at the crossroads between cancer and aging.

Oncogene 26, 5489–5504 (2007). [PubMed: 17694089]

21. Lee S-H, Lee J-H, Lee H-Y & Min K-J Sirtuin signaling in cellular senescence and aging. BMB

Rep 52, 24–34 (2019). [PubMed: 30526767]

22. Brink S. C. van den et al. Single-cell sequencing reveals dissociation-induced gene expression in

tissue subpopulations. Nat. Methods 14, 935–936 (2017). [PubMed: 28960196]

23. Tung P-Y et al. Batch effects and the effective design of single-cell gene expression studies. Sci.

Rep 7, 39921 (2017). [PubMed: 28045081]

24. Nguyen QH, Pervolarakis N, Nee K & Kessenbrock K Experimental Considerations for Single-

Cell RNA Sequencing Approaches. Front. Cell Dev. Biol 06, 108 (2018).

25. Daly DM et al. Age‐related changes in afferent pathways and urothelial function in the male mouse

bladder. J. Physiol 592, 537–549 (2014). [PubMed: 24297847]

26. Burmeister DM, AbouShwareb T, Bergman CR, Andersson K-E & Christ GJ Age-Related

Alterations in Regeneration of the Urinary Bladder after Subtotal Cystectomy. Am. J. Pathol 183,
1585–1595 (2013). [PubMed: 24012523]

27. Andersson K-E, Boedtkjer DB & Forman A The link between vascular dysfunction, bladder

ischemia, and aging bladder dysfunction. Ther. Adv. Urol 9, 11–27 (2017). [PubMed: 28042309]
28. Suskind AM The Aging Overactive Bladder: a Review of Aging-Related Changes from the Brain

to the Bladder. Curr. Bladder Dysfunct. Rep 12, 42–47 (2017). [PubMed: 28947924]

29. Zhang D et al. Downregulation of ATP1A1 promotes cancer development in renal cell carcinoma.

Clin. Proteomics 14, 15 (2017). [PubMed: 28484360]

30. Isaka Y Epidermal growth factor as a prognostic biomarker in chronic kidney diseases. Ann.

Transl. Med 4, S62–S62 (2016). [PubMed: 27868030]

31. Devuyst O, Olinger E & Rampoldi L Uromodulin: from physiology to rare and complex kidney

disorders. Nat. Rev. Nephrol 13, 525–544 (2017). [PubMed: 28781372]

32. Tokonami N et al. Uromodulin is expressed in the distal convoluted tubule, where it is critical for
regulation of the sodium chloride cotransporter NCC. Kidney Int 94, 701–715 (2018). [PubMed:
30007527]

Nature. Author manuscript; available in PMC 2021 June 29.

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Page 29

33. Palmer S, Albergante L, Blackburn CC & Newman TJ Thymic involution and rising disease

incidence with age. Proc. Natl. Acad. Sci 115, 201714478 (2018).

34. Shen Q et al. The AP-1 transcription factor regulates postnatal mammary gland development. Dev.

Biol 295, 589–603 (2006). [PubMed: 16678816]

35. Girnius N, Edwards YJK & Davis RJ The cJUN NH2-terminal kinase (JNK) pathway contributes
to mouse mammary gland remodeling during involution. Cell Death Differ 25, 1702–1715 (2018).
[PubMed: 29511338]

36. Tan Q et al. The Role of IL-1 Family Members and Kupffer Cells in Liver Regeneration. BioMed

Res. Int 2016, 6495793 (2016). [PubMed: 27092311]

37. Gehrke N et al. Hepatocyte-specific deletion of IL1-RI attenuatesliver injury by blocking IL-1

driven autoinflammation. J. Hepatol 68, 986–995 (2018). [PubMed: 29366909]

38. Liu Y, Gardner CR, Laskin JD & Laskin DL Classical and alternative activation of rat hepatic
sinusoidal endothelial cells by inflammatory stimuli. Exp. Mol. Pathol 94, 160–167 (2013).
[PubMed: 23103612]

39. McKenna A et al. The Genome Analysis Toolkit: A MapReduce framework for analyzing next-

generation DNA sequencing data. Genome Res 20, 1297–1303 (2010). [PubMed: 20644199]
40. DePristo MA et al. A framework for variation discovery and genotyping using next-generation

DNA sequencing data. Nat. Genet 43, 491 (2011). [PubMed: 21478889]

41. Auwera GA et al. From FastQ Data to High‐Confidence Variant Calls: The Genome Analysis

Toolkit Best Practices Pipeline. Curr. Protoc. Bioinforma 11.10.1–11.10.33 (2013)
doi:10.1002/0471250953.bi1110s43.

42. Zook JM, Samarov D, McDaniel J, Sen SK & Salit M Synthetic Spike-in Standards Improve Run-
Specific Systematic Error Analysis for DNA and RNA Sequencing. PLoS ONE 7, e41356 (2012).
[PubMed: 22859977]

43. Croote D, Darmanis S, Nadeau KC & Quake SR High-affinity allergen-specific human antibodies

cloned from single IgE B cell transcriptomes. Science 362, 1306–1309 (2018). [PubMed:
30545888]

44. Stubbington MJT et al. T cell fate and clonality inference from single-cell transcriptomes. Nat.

Methods 13, nmeth.3800 (2016).

45. Goronzy JJ & Weyand CM Understanding immunosenescence to improve responses to vaccines.

Nat. Immunol 14, ni.2588 (2013).

46. Goronzy JJ & Weyand CM Successful and Maladaptive T Cell Aging. Immunity 46, 364–378

(2017). [PubMed: 28329703]

47. Keren-Shaul H et al. A Unique Microglia Type Associated with Restricting Development of

Alzheimer’s Disease. Cell 169, 1276–1290.e17 (2017). [PubMed: 28602351]

48. Li Q et al. Developmental Heterogeneity of Microglia and Brain Myeloid Cells Revealed by Deep

Single-Cell RNA Sequencing. Neuron 101, 207–223.e10 (2019). [PubMed: 30606613]

49. Hammond TR et al. Single-Cell RNA Sequencing of Microglia throughout the Mouse Lifespan and
in the Injured Brain Reveals Complex Cell-State Changes. Immunity 50, 253–271.e6 (2019).
[PubMed: 30471926]

50. Jablonski KA et al. Novel Markers to Delineate Murine M1 and M2 Macrophages. PLOS ONE 10,

e0145342 (2015). [PubMed: 26699615]

Aditional References

51. Picelli S et al. Smart-seq2 for sensitive full-length transcriptome profiling in single cells. Nat.

Methods 10, nmeth.2639 (2013).

52. Darmanis S et al. A survey of human brain transcriptome diversity at the single cell level. Proc.

Natl. Acad. Sci 112, 7285–7290 (2015). [PubMed: 26060301]

53. Picelli S et al. Tn5 transposase and tagmentation procedures for massively scaled sequencing

projects. Genome Res 24, 2033–2040 (2014). [PubMed: 25079858]

54. Hennig BP et al. Large-Scale Low-Cost NGS Library Preparation Using a Robust Tn5 Purification

and Tagmentation Protocol. G3 Genes Genomes Genet 8, 79–89 (2018).

Nature. Author manuscript; available in PMC 2021 June 29.

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Page 30

55. Wolf FA, Angerer P & Theis FJ SCANPY: large-scale single-cell gene expression data analysis.

Genome Biol 19, 15 (2018). [PubMed: 29409532]

56. Diehl AD et al. The Cell Ontology 2016: enhanced content, modularization, and ontology

interoperability. J. Biomed. Semant 7, 44 (2016).

57. Finak G et al. MAST: a flexible statistical framework for assessing transcriptional changes and
characterizing heterogeneity in single-cell RNA sequencing data. Genome Biol 16, 278 (2015).
[PubMed: 26653891]

58. McQuin C et al. CellProfiler 3.0: Next-generation image processing for biology. PLOS Biol 16,

e2005970 (2018). [PubMed: 29969450]

59. Li H et al. The Sequence Alignment/Map format and SAMtools. Bioinformatics 25, 2078–2079

(2009). [PubMed: 19505943]

60. Wolf FA et al. PAGA: graph abstraction reconciles clustering with trajectory inference through a
topology preserving map of single cells. Genome Biol 20, 59 (2019). [PubMed: 30890159]

Nature. Author manuscript; available in PMC 2021 June 29.

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Page 31

Figure 1. Overview of Tabula Muris Senis.
a, 23 organs from 19 male and 11 female mice were analyzed at 6 different time points. The
bar plot shows the number of sequenced cells per organ prepared by FACS (n=23 organs)
and microfluidic droplets (n=16 organs). For the droplet dataset the Fat sub-tissues were
processed together (Fat = BAT+GAT+MAT+SCAT). BAT, Brown Adipose Tissue; GAT,
Gonadal Adipose Tissue; MAT, Mesenteric Adipose Tissue; SCAT, Subcutaneous Adipose
Tissue. b, Annotation workflow. Data were clustered together across all time points. We
used the Tabula Muris (3m time point) as a reference for the automated pipeline and the
annotations were manually curated by tissue experts. c,d, UMAP plot of all cells, colored by
organ and overlaid with the Louvain cluster numbers (c) and age (d); n = 356,213 individual
cells. For the color dictionaries please refer to Extended Data Figure 2c. e, B cells (top) and
endothelial cells (bottom) independently annotated for each organ cluster together by
unbiased whole-transcriptome Louvain clustering, irrespectively of the organ they were
found.

Nature. Author manuscript; available in PMC 2021 June 29.

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Page 32

Figure 2. Cellular changes during aging.
a,b, Bar plot showing the fractions of cells expressing Cdkn2a at each age group for FACS
(a) and droplet (b). c,d, Bar plot of the median expression of Cdkn2a for the cells that do
express the gene at each age group for FACS (c) and droplet (d). The y-axis corresponds to
log-transformed and scaled values. All data are expressed as mean ± s.d. with individual data
points shown. p-values were obtained using a Mann-Whitney-Wilcoxon rank-sum two-sided
test. n=44,518; 34,027 and 31,551 individual cells for FACS 3m; 18m and 24m, respectively.
n=25,980; 45,602; 44,645; 35,828; 37,660 and 55,674 individual cells for droplet 1m; 3m;
18m; 21m; 24m and 30m, respectively. e, Bladder cell (left) and bladder urothelial cell
(right) relative abundances change significantly with age (p-value<0.05 and r2>0.7 for a
hypothesis test whose null hypothesis is that the slope is zero, using two-sided Wald Test
with t-distribution of the test statistic). f, Top 20 upregulated and downregulated genes in
bladder computed using MAST57, treating age as a continuous covariate while controlling
for sex and technology. Genes were classified as significant under an FDR threshold of 0.01
and an age coefficient threshold of 0.005 (corresponding to ~10% fold change). n=970;
3,804; 2,739 and 3,864 individual cells for bladder 1m; 3m; 18m and 24m, respectively. g,
Kidney capillary endothelial cell (top-left), mesangial cell (top-right), loop of Henle
ascending limb epithelial cell (bottom-left) and loop of Henle thick ascending limb
epithelial cell (bottom-right) relative abundances change significantly with age (p-
value<0.05 and r2>0.7 for a hypothesis test whose null hypothesis is that the slope is zero,

Nature. Author manuscript; available in PMC 2021 June 29.

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Page 33

using two-sided Wald Test with t-distribution of the test statistic). h, Top 20 upregulated and
downregulated genes in kidney computed using MAST57, treating age as a continuous
covariate while controlling for sex and technology. Genes were classified as significant
under an FDR threshold of 0.01 and an age coefficient threshold of 0.005 (corresponding to
~10% fold change). n=2,488; 2,832; 3,806; 2,257; 6,384 and 5,713 individual cells for
kidney 1m; 3m; 18m; 21m; 24m and 30m, respectively. i, Spleen plasma cell (left) and T
cell (right) relative abundances change significantly with age (p-value<0.05 and r2>0.7 for a
hypothesis test whose null hypothesis is that the slope is zero, using two-sided Wald Test
with t-distribution of the test statistic). j, Top 20 upregulated and downregulated genes in
spleen computed using MAST57, treating age as a continuous covariate while controlling for
sex and technology. Genes were classified as significant under an FDR threshold of 0.01 and
an age coefficient threshold of 0.005 (corresponding to ~10% fold change). n=2,986; 8,839;
7,141; 6,395; 5,245 and 8,946 individual cells for spleen 1m; 3m; 18m; 21m; 24m and 30m,
respectively. The p-values for the cell type compositional changes are shown in
Supplementary Table 5.

Nature. Author manuscript; available in PMC 2021 June 29.

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Page 34

Figure 3. Mutational burden across tissues in the aging mice.
Distribution of the difference of the mean mutation in the gene set (and ERCC spike-in
controls) per cell between 24m and 3m and 18m and 3m for all tissues and cells (a) and with
the cell types split in five functional groups, endothelial (b), immune (c), parenchymal (d),
stem/progenitor cell (e) and stromal (f). Filled and solid line distributions correspond to the
mean mutation difference in gene set. White and dashed line distributions correspond to the
mean mutation difference in ERCC spike-in controls. Please note that the mean mutation
difference in ERCC spike-in controls overlaps for both age groups.

Nature. Author manuscript; available in PMC 2021 June 29.

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Page 35

Figure 4. The aging immune system.
a, B-cell clonal families. The pie chart shows the proportion of singleton B cells and B cells
that are part of clonal families at 3m, 18m and 24m. Please refer to Extended Data Figure 9
for the clonal networks. b, T-cell clonal families. The pie chart shows the proportion of
singleton T cells and T cells that are part of clonal families at 3m, 18m and 24m. Please
refer to Extended Data Figure 9 for the clonal networks. c, Diversity score for the two cell
types that significantly change with age. d, UMAP plot of the brain myeloid microglial cell
Leiden clusters (numbers) colored by age. Faded clusters do not change their relative age
cell composition; colored clusters change their relative cell composition. e, UMAP plot of
the brain myeloid microglial cells when scored using the microglia Alzheimer’s disease
signature (Supplementary Table 10). n = 4,532; 4,461 and 4,424 individual microglia cells
for brain myeloid 3m, 18m and 24m, respectively. f, UMAP plot of the kidney macrophage
Leiden clusters (numbers) colored by age group. n = 62; 139; 264; 105; 284 and 553
individual macrophage cells for kidney 1m, 3m, 18m, 21m, 24m and 30m, respectively.

Nature. Author manuscript; available in PMC 2021 June 29.

