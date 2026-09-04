Supplementary Materials for

Mapping the developing human immune system across organs

Chenqu Suo et al.

Corresponding authors: Menna R. Clatworthy, mrc38@cam.ac.uk; Muzlifah Haniffa, m.a.haniffa@newcastle.ac.uk;
Sarah A. Teichmann, st9@sanger.ac.uk

Science 376, e abo0510 (2022)
DOI: 10.1126/science.abo0510

The PDF file includes:

Materials and Methods
Figs. S1 to S33
References

Other Supplementary Material for this manuscript includes the following:

Tables S1 to S9
MDAR Reproducibility Checklist

Submitted Manuscript: Confidential

Supplementary Materials and Methods
Tissue acquisition and processing

All human developmental tissue samples used for this study were obtained from the MRC–
Wellcome Trust-funded Human Developmental Biology Resource (HDBR;
http://www.hdbr.org) with written consent and approval from the Newcastle and North Tyneside
NHS Health Authority Joint Ethics Committee (08/H0906/21+5).

All tissues were processed into single-cell suspensions immediately upon receipt. Tissue was
first minced in a tissue culture dish using scalpel. It was then digested with type IV collagenase
(final concentration of 1.6 mg/ml; Worthington) in RPMI (Sigma-Aldrich) supplemented with
10% fetal bovine serum (FBS; Gibco), at 37°C for 30 min with intermittent agitation. Digested
tissue was then passed through a 100-µm cell strainer and cells were pelleted by centrifugation at
500g for 5 min at 4°C. Cells were then resuspended in 5 ml of red blood cell lysis buffer
(eBioscience) and left for 5-10 min at room temperature. It was then topped up with flow buffer
(PBS containing 2% (v/v) FBS and 2 mM EDTA) to 45 ml prior to cell counting and antibody
staining. Single-cell suspensions were generated from 76 samples across yolk sac (7), liver (6),
spleen (30), thymus (4), kidney (2), and skin (27) of 16 donors. The ages of the donors spanned
from 4 pcw (post conception weeks) to 17 pcw. The metadata of all samples, including
previously published data, can be found in table S7.

Single-cell RNA sequencing experiment

Dissociated cells were stained with anti-CD45 antibody (BUV395 anti-human CD45 antibody,
BD Biosciences, 563791) and DAPI (Sigma-Aldrich, D9542) prior to sorting. For all FACS
experiments performed in this study, DAPI was used at a final concentration of 2.8 µM, and all
antibody solutions were used at a final concentration of 2 µl per 100 µl cell suspensions
containing fewer than 5 million cells. Sorting by flow cytometry was performed with BD
FACSAria Fusion Flow Cytometer. The CD45+ fraction was sorted from DAPI–CD45+ gate and
CD45– fraction was sorted from DAPI–CD45– gate. CD45 gating was contiguous so that no live
cells were lost in sorting.

For scRNA-seq experiments, either Chromium single cell 3′ reagent kit or Chromium single cell
V(D)J reagent kits from 10X Genomics were used. Unsorted, or DAPI–CD45+, or DAPI–CD45–
FACS-isolated cells were loaded onto each channel of the Chromium chip following the
manufacturer’s instructions before droplet encapsulation on the Chromium controller. Single-cell
cDNA synthesis, amplification, gene expression (GEX) and targeted B cell receptor (BCR) and
T cell receptor (TCR) libraries were generated. Targeted enrichment for γδTCR was performed
following the TCR enrichment protocol from 10X with customized primers binding to the
constant region of the TRD and TRG genes as described (75). Primers are listed in table S8.

Sequencing was performed on the Illumina Novaseq 6000 system. The gene expression libraries
were sequenced at a target depth of 50,000 reads per cell using the following parameters: Read1:
26 cycles, i7: 8 cycles, i5: 0 cycles; Read2: 91 cycles to generate 75-bp paired-end reads. BCR
and TCR libraries were sequenced at a target depth of 5000 reads per cell.

2

Submitted Manuscript: Confidential

Cell cultures for artificial thymic organoid (ATO)

MS5 line transduced with human DLL4 was obtained from G. Crooks (UCLA) as a gift. The
MS5-hDLL4 cells were cultured in DMEM (Gibco) with 10% FBS. Two iPSC lines were used in
this study. Cell lines HPSI0114i-kolf_2 (Kolf) and HPSI0514i-fiaj_1 (Fiaj) were obtained from
the Human Induced Pluripotent Stem Cell initiative (HipSci: www.hipsci.org) collection. All
iPSC lines were cultured on vitronectin (diluted 1:25 in PBS; Gibco) coated plates, in TeSR-E8
media (Stemcell Technologies).

We followed the PSC-ATO protocol as previously described (61). iPSC cells were harvested as a
single-cell suspension and seeded (3×106 cells per well) in GFR reduced Matrigel (Corning) -
coated 6-well plates in X-VIVO 15 media (Lonza), supplemented with rhActivin A, rhBMP4,
rhVEGF, rhFGF (all from R&D Systems), and ROCK inhibitor (Y27632; LKT Labs) on day
−17, and only rhBMP4, rhVEGF and rhFGF on days −16 and −15. Cells were harvested 3.5 days
later, and isolated by FACS for CD326–CD56+ (PE anti-human CD326 antibody, Biolegend,
324205; APC anti-human CD56 antibody, Biolegend, 318309) human embryonic mesodermal
progenitors (hEMPs).

Isolated hEMPs were combined with MS5-hDLL4 at a ratio of 1:50. Two or three cell-dense
droplets (5×105 cells in 6 μl hematopoietic induction medium) were deposited on top of an insert
in each well of a six-well plate. Hematopoietic induction medium composed of EGM2 (Lonza)
supplemented with ROCK inhibitor and SB blocker (TGF-β receptor kinase inhibitor SB-
431542; Abcam) was added into the wells outside the inserts so that the cells sat at the air-liquid
interface. The organoids were then cultured in EGM2 with SB blocker for 7 days (days −14 to
−7), before the addition of cytokines rhSCF, rhFLT3L, rhTPO (all from Peprotech) between days
−6 to 0. These 2 weeks formed the hematopoietic induction phase. On day 1, media was changed
again to RB27 (RPMI supplemented with B27 (Gibco), ascorbic acid (Sigma-Aldrich),
penicillin/streptomycin (Sigma-Aldrich) and glutamax (Thermo Fisher Scientific)) with rhSCF,
rhFLT3L and rhIL7. The organoids can be maintained in culture for 7 more weeks in this
medium.

For dissociation and checking of ATO, a cell scraper was used to detach ATOs from cell culture
insert membranes and detached ATOs were then submerged in cold flow buffer. Culture inserts
were washed and detached ATOs were pipetted up and down to form single-cell suspension
before passing through a 50-μm strainer. Cells were then stained with designed panels of
antibodies and analyzed by flow cytometry. FACS was performed at the same time and live
human DAPI–anti-mouse CD29– (APC/Cy7 anti-mouse CD29 antibody, Biolegend, 102225)
cells were sorted for week 3 ATO cells, and live (DAPI–) cells were sorted for week 5 and week
7 ATO cells before loading onto each channel of the Chromium chip from Chromium single cell
V(D)J kit (10X Genomics).

Visium

OCT embedded freshly frozen samples were used for 10X Genomics Visium, and samples were
processed following manufacturer’s instructions. All tissues were sectioned with a thickness of
15 µm on a cryostat (OTF5000, Bright instruments). Tissue optimization was then performed
with an 18-min permeabilization for fetal spleen and liver, whereas a 24-min permeabilization

3

Submitted Manuscript: Confidential

was used for fetal thymus. The spatial gene expression library was then generated following the
manufacturer's protocol. All images for this process were acquired with a Zeiss AxioImager
(Carl Zeiss Microscopy) and a 20X air objective (0.8 NA) using either fluorescence (Zeiss
Axiocam 503 monochrome camera) for optimization or brightfield mode (Zeiss Axiocam 105
color camera) for H&E imaging. ZEN (Blue edition) v.3.1 was used for acquisition and stitching
of the image tiles. The metadata of all samples can be found in table S9.

Single molecule fluorescence in situ hybridization (smFISH)

The smFISH technique RNAscope was performed on thymus, spleen, and gut sections, using the
RNAScope 2.5 LS multiplex fluorescent assay (ACD, Bio-Techne) on the automated BOND RX
system (Leica). Prior to running RNAscope probes of interest, positive and negative control
probes were used for optimization of these tissues. Tissue sections were placed onto superfrost
plus slides (Fisher scientific) and stained for DAPI (nuclei) and three or four probes of interest,
with fluorophores opal 520, opal 570, opal 650 and atto 425. DAPI was used at 1:50,000
concentration; opals at 1:1000 (1:500 for thymus) and atto 425 at 1:400 concentration.

For the fetal gut and spleen, OCT-embedded freshly frozen samples were sectioned to 10 µm-
thick. Following optimization, sections were pretreated offline for 15 min with chilled 4%
paraformaldehyde and dehydrated through an ethanol series (50%, 70%, 100%, 100% ethanol),
before processing on the Leica BOND RX with protease IV for 30 min at room temperature. The
sections were imaged on a Perkin Elmer Opera Phenix High Content Screening System (16-bit
sCMOS camera, PerkinElmer) with a 20X water objective (High NA, PerkinElmer). Due to high
levels of endogenous autofluorescence, we imaged one of the spleen sections (fig. S21A) with a
confocal microscope (Leica SP8) with a 40X 1.3NA oil immersion objective and SP8 Leica HyD
and PMT detectors. Emission spectral filters were set for DAPI, opal 520 (VPREB1), opal 570
(RAG1), opal 650 (CDH5). Images were processed with Fiji as follows. All channels were
subjected to z-max projection followed by 2D Gaussian filtering (sigma = 0.5 pixels). The DAPI
channel was flat field corrected (biovoxxel – pseudo flat field correction plugin) with a rolling
ball radius of 200 pixels. The large image was cropped around the tissue area to remove flat field
corrections edges.

Due to the high cellular density in thymic sections, we used 3 µm-thick FFPE sections. These
were treated on the Leica Bond RX with epitope retrieval 2 for 15 min at 95°C and protease III
for 15 min at 40°C. FFPE thymus did not require any offline pretreatment. Imaging was
performed on an Operetta CLS High Content Screening System (16-bit sCMOS camera,
PerkinElmer) with a 40X water objective (High NA, PerkinElmer) and 2-µm z-steps.

Cells were identified and annotated manually with an in-house OMERO platform
(https://www.openmicroscopy.org/omero/).

scRNA-seq analysis

Preprocessing
The gene expression data was mapped with cellranger 3.0.2 to an Ensembl 93 based GRCh38
reference (10X-distributed 3.0.0 version). Ambient RNA was removed with cellbender v0.2.0

4

Submitted Manuscript: Confidential

(76). Low-quality cells were filtered out (minimum number of reads = 2000, minimum number
of genes = 500, Scrublet (v0.2.3) (77) doublet detection score <0.4).

In order to identify possible maternal contamination, the samples were pooled on a per-donor
basis and processed with souporcell (v.2.4.0) (78). The common GRCh38 variants file (SNPs
with !2% frequency from 1k genomes) provided by souporcell authors was used. The pipeline
was run twice, setting the number of genotype clusters to 1 and 2 to obtain models for no
maternal contamination and possible maternal contamination. The better of these models was
identified via BIC (Bayesian Information Criterion), calculated using the formula below:

𝐵𝐼𝐶 = 𝑘𝑛	log(𝑚) − 2𝑙
Whereby k is the number of genotype clusters set for each souporcell run, n denotes the number
of loci used for genotype deconvolution, m is the cell count for a given donor, and 𝑙 is the log
likelihood obtained after running the pipeline with each k. In two donors (F19 and F37), the BIC
was smaller when k = 2. The cells with the minor genotype were identified as possible maternal
contaminants, which mainly consisted of NK cells, monocytes, mature B and T cells. The cells
of minor genotype from the remaining donors were further screened for similar cell
compositions, and a further donor (F33) was identified with possible maternal contamination.
For these three donors, cells from the minor genotype were excluded from the downstream
analysis.

Data integration and annotation
Data normalization and preprocessing were performed using the Scanpy workflow (v1.8.1) (79).
We normalized raw gene read counts by sequencing depth in each cell
(scanpy.pp.normalize_per_cell, with parameters counts_per_cell_after=10e4) and performed
ln(x)+1 transformation. Expression levels reported in this manuscript refer to normalized and
log-transformed gene read counts. We then selected highly variable genes (HVG) for joint
embedding by dispersion (scanpy.pp.highly_variable_genes with parameters min_mean = 0.001,
max_mean = 10). We considered the 10X chemistry (5′ and 3′) and the donor ID for each cell as
the technical covariates to correct for. We performed dimensionality reduction and batch
correction using the scVI model (12) as implemented in scvi-tools (v0.14.5) (80). For model
specification and training we used the recommended parameters to enable scArches mapping
(dropout_rate = 0.2, n_layers = 2). To verify conservation of biological variation after
integration, we collected and harmonized the available cell type labels from the published
datasets (66% of cells) and quantified the agreement between labels across different datasets in
the cell clusters identified post-integration, using the normalized mutual information (NMI)
score, as implemented in scikit-learn (81). The model was trained on raw counts of the 7500
most highly variable genes, excluding cell cycle genes and TCR/BCR genes (7) with 20 latent
dimensions. These parameters (number of HVGs, number of latent dimensions,
exclusion/inclusion of cell cycle and TCR/BCR genes) were picked through a parameter sweep,
focused on maximizing the NMI between clusters after embedding and pre-existing cell type
label annotation (data not shown). Unless otherwise specified, cell clustering was performed
using the Leiden algorithm (82) with resolution = 1.5 on a k-nearest neighbor graph with k = 30.
To verify that our cell type clusters were robust to the choice of integration method, we
performed in parallel integration on the full dataset using BBKNN (83) as previously described
(7) (fig. S30A). We found that clustering post-integration both with scVI and BBKNN was
consistent with previous annotations (fig. S30B).

5

Submitted Manuscript: Confidential

To annotate fine cell populations across tissues, we clustered cells in the scVI latent space and
preliminarily assigned cells to broad lineages examining expression of marker genes and
assigning putative cell labels based on previous annotations (we propagated existing cell type
labels to unannotated cells by taking the most abundant label in the k-nearest neighbors for each
unannotated cell). For each broad lineage we repeated scVI integration and clustering as
described above and defined further subsets (see hierarchy in fig. S5). Leiden clusters for the
highest resolution subsets (Stroma, megakaryocyte/erythroid, progenitors, lymphoid, myeloid)
were annotated manually, using marker panels shown in fig. S4. A common subset of progenitor
cells was included in scVI embeddings for all hematopoietic-derived cell subsets
(megakaryocyte/erythroid, lymphoid, myeloid, NK/T), to allow feature selection and
dimensionality reduction to capture the differentiation process of different lineages. A distinct
embedding of progenitor cells was then used to finely annotate these cell populations (fig. S4E-
F). Blood and immune cell progenitor annotation was based on the subsets and marker genes
identified by Jardine et al. (11) and Popescu et al. (3) (SFig. 31). Macrophage subsets were
annotated by analysis of marker genes from human studies in both adult and developmental
tissues (18–20, 62) and by unbiased marker gene detection (using scanpy.tl.rank_genes_groups)
and groupings were defined as follows: “LYVE1hi” expressing F13A1, LYVE1, and SPP1; “Iron-
recycling” expressing the highest levels of ferroportin (SLC40A1) and phosphatidylserine
receptor TIMD4 but best characterized by expression of CD5L, VCAM1, and APOE; “MHC class
IIhi” expressing the highest levels of HLA-DRA, HLA-DPA1, and CLEC7A among macrophages;
“Kupffer-like” expressing endothelial transcripts ENG, KDR, and CAV; “TREM2” with
expression of microglia-associated transcripts TREM2 and P2RY12; “Osteoclasts” expressing
characteristic MMP9 and ACP5; and “Proliferating macrophages” expressing genes associated
with cell-cycle progression (fig. S4H). Fetal macrophage subsets show a phenotype
corresponding to (TIMD4/LYVE1/FOLR2) TLF+ murine macrophages, with potentially
additional heterogeneity within the human fraction (100) (fig. S4H).

We verified that refined annotations were highly consistent with unsupervised clustering post-
integration on the full dataset both with scVI and BBKNN (fig. S30C).

After full annotation 23,156 cells (2.5% of total) were assigned to low quality clusters. These
comprised doublet clusters, maternal contaminants clusters and clusters displaying a high
percentage of reads from mitochondrial genes.

Differential abundance analysis
We tested for differences in cell abundances associated with gestational age or organ using the
Milo framework for differential abundance testing (22), with the python implementation milopy
(https://github.com/emdann/milopy). Briefly, we subsetted the dataset to cells from libraries
obtained with CD45+ FACS, CD45– FACS or no FACS. In addition, we excluded FACS-isolated
samples for which we were not able to recover the true sorting fraction quantification. In total,
we retained 228,731 lymphoid cells and 214,874 myeloid cells. To further minimize the
differences in cell numbers driven by differences in FACS efficiency, we calculated a FACS
correction factor for each tissue sample s sorted with gate i (where i is either CD45+ or CD45–):
𝑓! = log(𝑝"𝑆/𝑆")

where	𝑝" represents the true proportion of cells from gate i in the tissue samples from the same
organ and donor, S represents the total number of cells recovered from both CD45+ and CD45–
gates for this organ and donor and 𝑆" represents the number of cells recovered in gate i. For the

6

Submitted Manuscript: Confidential

unsorted samples we set 𝑓! = 0. Encoding the true proportions of CD45+/– cells with 𝑓!	reduced
the proportion of false positives that were found without regressing out the effect of FACS
isolation, or when encoding the effect of sorting as a label rather than a proportion (where CD45+
= 1, CD45– = -1, unsorted = 0) (fig. S32A). To validate this approach, we confirmed agreement
between estimated fold-changes testing on unsorted samples with the fold-changes estimated
accounting for FACS on sorted samples from the same organ (fig. S32B).

We constructed a KNN graph of remaining cells using similarity in the scVI embedding (k = 30
for test across gestation, k = 100 for test across tissues). We assigned cells to neighborhoods on
the KNN graph using the function milopy.core.make_nhoods (parameters: prop = 0.05). We then
counted the number of cells belonging to each sample in each neighborhood, creating a cell
count matrix with rows representing neighborhoods and columns representing samples (using the
function milopy.core.count_cells). We assigned each neighborhood a cell type label based on
majority voting of the cells belonging to that neighborhood. We assigned a “Mixed” label if the
most abundant label is present in less than 50% of cells within that neighborhood.

Differential abundance across time: To test for differences in cell numbers across gestational age,
we divided the sample ages into six equally sized bins (bin size = 2 pcw) and excluded from the
cell count matrix samples from organs where less than three consecutive age bins were profiled
(yolk sac, mesenteric lymph node, kidney, gut). For the matrix of cell counts from samples in
each organ, we modeled the cell count 𝑐#,!of cells from sample s in neighborhood n as a negative
binomial generalized linear model (NB-GLM):

𝑐#,! ∼ 𝑁𝐵(𝜇#,!, 𝜙#)
where 𝜇#,!is the mean number of cells from sample s in neighborhood n and 𝜙#is the dispersion
parameter. We used a log-linear model to model the effect of age on cell counts:

log 𝜇#,! 	 = 𝑓!𝛽#

%&'( + 𝑎!𝛽#

&)* +	log 𝐿!

here:

-  𝐿! is the sum of counts of cells of sample s over all the neighborhoods.
-  𝑎! is the age bin associated to sample s.
-  𝛽#

&)*	𝑖s the regression coefficient encoding the effect of age on the number of cells in
neighborhood n, that represents the log-fold change (logFC) that can be interpreted as the
per-bin linear change in neighborhood cell abundance.
-  𝑓!	is the FACS correction factor associated to sample s.
-  𝛽#

%&'( is the regression coefficient encoding the effect of CD45 enrichment on the number
of cells in neighborhood n.

To control for multiple testing, we used the weighted BH correction as previously implemented
(22). In addition, we tested in parallel for differential abundance associated with the library prep
protocol (instead of gestational age) and excluded neighborhoods where we detected significant
differential abundance associated with library prep protocol (SpatialFDR < 0.1). We applied this
stringent filtering step instead of including the library prep protocol as a covariate in the model
(as described below for the test on organ enrichment) to exclude from downstream analysis false
positive neighborhoods identified in a small number of thymus samples, where we observed
strong confounding between age bins and library prep protocol.

7

Submitted Manuscript: Confidential

To detect markers of early-specific neighborhoods (SpatialFDR < 0.1, logFC < 0) and/or late-
specific neighborhoods (SpatialFDR < 0.1, logFC > 0) in cell type c and organ o, we tested for
differential expression between cells from organ o assigned to the significant neighborhoods
labeled as cell type c and cells belonging to all other neighborhoods labeled as cell type c. We
used the t-test implementation in scanpy (scanpy.tl.rank_genes_groups, method = "t-
test_overestim_var"). Genes expressed in > 70% of tested cells were excluded. We considered
genes as significantly overexpressed (i.e. markers) if the differential expression logFC > 1 and
FDR < 0.1%. Gene set enrichment analysis was performed using the implementation of the
EnrichR workflow (84) in the python package gseapy (https://gseapy.readthedocs.io/). The list of
significantly overexpressed genes for all organs and cell types where differential expression
testing was carried out can be found in table S1 and S3.

Differential abundance between organs: We modeled the cell counts 𝑦#,! for each experimental
sample s in neighborhood n by a Negative Binomial distribution:

𝑦#,! = 	𝑁𝐵(𝜇#,!, 𝜙#,!)

Where the expected count value 𝜇#,!is given by the following log-linear model

	log 𝜇#,! = 𝑝!𝛽#

+,*+ + 	 𝑓!𝛽#

%&'( + 𝑜!𝛽#

- 	 + log𝐿!

here:

-  𝐿!	is the sum of counts of cells of sample s over all the neighborhoods.
-  𝑜! is a binary factor indicating whether sample s is derived from organ o.
-  𝛽#

- 	is the regression coefficient encoding the effect of the organ on the number of cells in
neighborhood n, that represents the log-fold change in abundance of cells from organ o
compared to the cells from other organs.

-  𝑓! is the FACS correction factor associated to sample s.
-  𝛽#

%&'(	is the regression coefficient encoding the effect of CD45 enrichment on the number
of cells in neighborhood n.

-  𝑝!	is the binary design matrix associating sample s to a library prep protocol.
-  𝛽#

+,*+ is the regression coefficient encoding the effect of the library prep protocol on the
number of cells in neighborhood n.

- 	for each n and o by fitting the NB-GLM to the count data for each

We estimated 𝛽#
neighborhood, i.e. by estimating the dispersion 𝜙#,! that models the variability of cell counts in
replicate samples for each neighborhood. To control for multiple testing we use the weighted BH
correction as implemented by Dann et al. (22).

We considered the neighborhoods where 𝛽#
that show organ-specific transcriptional signatures.

- > 0 and SpatialFDR < 0.01 as cell subpopulations

Having identified a subset of neighborhoods overlapping a cell type or a subset of
transcriptionally related cell types 𝑐̂ that were enriched in an organ 𝑜E, we performed differential
.,/,!
expression (DE) analysis between these cells and cells from cell type c in other organs. Let 𝑥"
be the raw gene expression counts of gene g in the ith cell from sample s and of cell type c. We
first aggregated single-cell expression profiles into pseudo-bulk expression profiles 𝑥E for each
(c,s) (as recommended by (85, 86)):

8

Submitted Manuscript: Confidential

𝑥̄ .,/,! = H 𝑥"

.,/,!

"

We next defined a subset of cell types and samples where we will fit the model to test for
differentially expressed genes in organ 𝑜E. First, we subsetted to the samples from donors where
'1,2 ≠ 𝑐̂ where
organ 𝑜E and at least 3 other organs were profiled. We then identified 3 cell types 𝑐0
at least 2 pseudobulks aggregated from at least 50 cells are profiled in the selected donors, for
organ 𝑜E and at least 3 other organs. These cell types represent populations where we don’t expect
to see biological differences in expression in organ 𝑜E.

After sample selection, we subsetted the number of genes for DE testing selecting the top 7500
highly variable genes in 𝑥̄ /̂,! using the method implemented in the R package scran. We further
'1,2 or 𝑐̂ is
excluded genes where the sum of expression values across pseudobulks from either 𝑐0
equal to 0.

These steps yielded a P-by-G data matrix 𝑋K , where P is the number of selected pseudobulks and
G is the number of selected genes.

We modeled the mRNA counts of gene 𝑔 in pseudobulk p by a NB-GLM:

𝑥̄ .,4 = 	𝑁𝐵(𝜇.,4, 𝜙.,4)

Where the expected count value 𝜇#,4	is given by the following log-linear model

log 𝜇.,4 = 𝛽5	 + 	𝑑4𝛽.
We estimated the log-fold change 𝛽.
using the quasi-likelihood method (87) implemented in the R package glmGamPoi (85).

8,)&9×'*221:+* in expression in a given cell type for organ 𝑜E

8,)&9×'*221:+* +	log 𝐿4

'*221:+* + 𝑐4𝑜4𝛽.

8,)&9 + 𝑐4𝛽.

7898,+𝑜4𝛽.

We used the estimated logFC from the test on the control cell types to filter out genes where
differential expression is driven by technical differences in tissue processing. In particular, we
considered a gene to be significantly overexpressed in cell types 𝑐̂ and organ 𝑜E if it is significant
in the test on 𝑐̂ (FDR < 10% and logFC > 1) but not in the test on control cell types (FDR > 10%
and logFC > 0). We provide the full results for the differential expression analysis between
organs in mature T cells and monocytes in tables S2 and S4.

TCR analysis
Single-cell αβTCR sequencing data was mapped with cellranger-vdj (v.6.0.0). The output file
filtered_contig_annotations.csv was used and analyzed with scirpy (v.0.6.0) (88).

Single-cell γδTCR sequencing data was mapped with cellranger-vdj (v.4.0.0). All contigs
deemed high-quality were selected, and re-annotated with igblastn (v.1.17.1) against IMGT
reference sequences (last downloaded: 01/08/2021), via a workflow provided in dandelion
(v0.2.0) (89) (https://github.com/zktuong/dandelion). The workflow runs igblastn with the
following parameters: minimum D gene nucleotide match = 9, V gene e-value cutoff = 10-4. It
also reannotates D and J genes separately using blastn with the following parameters: dust =
“no”, word size (J = 7; D = 9), e-value cutoff (J = 10-4; D = 10-3). igblastn outputs were parsed
into AIRR format with change-o scripts (90). The output file all_contig_dandelion.tsv was used
and analyzed with scirpy (v0.6.0).

9

Submitted Manuscript: Confidential

We determined productive TCR chain pairing status with scirpy.tl.chain_qc() function. For TCR
usage PCA and clonotype analysis, cells with orphan VDJ or orphan VJ were filtered out so that
each cell has at least one paired TCR. For clonotype analysis, only mature T cells were included
to look at clonotype sharing. Clonotypes were determined using scirpy.pp.ir_neighbors() and
scirpy.tl.define_clonotypes() functions with the CDR3 nucleotide sequence identity from both
TCR chains as a metric.

Two samples from F67, F67_TH_CD137_FCAImmP7851896 and
F67_TH_MAIT_FCAImmP7851897 were excluded from all downstream TCR analysis as they
were sorted for specific T cell subpopulations, instead of the CD45 sorting in all other donor
samples, and inclusion might result in biased TCR sampling within this donor.

BCR analysis
Single-cell BCR data was initially processed with cellranger-vdj (v.6.0.0). BCR contigs contained
in all_contigs.fasta and all_contig_annotations.csv were then processed as follows: i) re-annotated
with  igblastn  as  per  above;  ii)  re-annotated  heavy-chain  constant  region  calls  using  blastn
(v.2.12.0+) against curated sequences from CH1 regions of respective isotype class; and iii) heavy-
chain  v-gene  allele  correction  using  tigger  (v1.0.0)  (101).  Contigs  were  then  filtered  for  basic
quality  control  as  described  previously  (91).  Briefly,  the  following  would  lead  to  removal  of
contigs from further analysis: i) contigs were annotated with mismatched V, D, J, or constant gene
calls not from the same locus; ii) multiple heavy-chain contigs. Exceptions to this would be when
a) contigs were assessed to have identical V(D)J sequences but assigned as a different contig by
cellranger-vdj (due to difference in non-V(D)J elements), b) when UMI count differences were
large in which case the contig with the highest UMI count is retained, and c) if only IgM and IgD
were both assigned to a cell; iii) only light-chain contigs in a cell; iv) multiple light-chain contigs
in a cell. These were performed using dandelion (89) singularity container (v.0.2.0). BCR mutation
frequencies  were  obtained  using  the  observedMutations  function  in  shazam  (v.1.0.2)  (90)  with
default settings (mutation counts for the different regions and mutation types were combined and
returned as one frequency value per contig). Mutation rates per cell were averaged across contigs
if multiple combinations of productive BCRs pairings were found in a single cell.

BCR clonotypes were determined with dandelion.tl.find_clones() function, based on the following
criteria for both heavy-chain and light-chain contigs: (1) identical V and J gene usage, (2) identical
junctional CDR3 amino acid length, and (3) at least 85% amino acid sequence similarity at the
CDR3  junction  (based  on  hamming  distance).  This  strategy  was  chosen  instead  of  using  exact
CDR3 nucleotide sequence identity to account for possible somatic hypermutations that happen
within the same B cell clone.

B cell activation scoring
Gene Ontology B Cell Activation gene list was downloaded from Gene Set Enrichment Analysis
website (http://www.gsea-msigdb.org/gsea/msigdb/genesets.jsp). Cells were scored according to
expression values of all genes in this gene list apart from three genes that were not present in the
dataset (MIR17HG, MIR185, MIR19A) using scanpy.tl.score_genes() function.

Transcription factor activity inference
We used the DoRothEA Python package (v.1.0.5) (91) to infer TF activities in B1 and mature B
cells. Human regulons with confidence level A, B and C in DoRothEA database were utilized, and
TF  activities  were  inferred  in  each  cell  using  dorothea.run(adata,  regulons,  center=True,

10

Submitted Manuscript: Confidential

num_perm=100,  norm=True,  scale=True,  use_raw=False,  min_size=5,  use_hvg=False)
function.  TFs  that  had  higher  activities  (positive  “meanchange”)  in  B1  cells  were  then  ranked
according to their adjusted P-values and only top 25 TFs are shown in fig. S26F.

Cell–cell interaction analysis
We used the CellPhoneDB Python package (v.3.0) (92, 93) to infer cell–cell interactions. The
scRNA-seq dataset was split by organ and cell types with fewer than 20 cells in a given organ
were filtered out. CellPhoneDB was run separately to infer cell–cell interactions in each organ,
using default parameters. We used P-values from the permutation test (pvalues.txt output from
CellPhoneDB), as well as the average expressions (“means”) of the ligand and receptor within
their corresponding cell types (means.txt output from CellPhoneDB). To explore cell–cell
interactions between B cell progenitors and colocalizing cell types (fig. S24D), we aggregated
the interactions predicted between each colocalizing cell type (e.g., ILC3 and different subtypes
of B cell progenitors (pre-pro B, pro B, late pro B, large pre B and small pre B cells)), by
averaging the means and using the minimum of the P-values. We then filtered for the ligand-
receptor pairs that were significant (P<0.05) across all three organs of liver, spleen, and thymus,
and ranked by the maximum aggregated means. Only the top 60 ligand-receptor pairs are shown
in fig. S24C.

Query-to-reference mapping
We mapped query data to our prenatal data embeddings using online update of the scVI models
following the scArches method (15), as implemented in the scvi-tools package (80). The model
was trained for 200 epochs and setting weight_decay = 0, to ensure that the latent representation
of the reference cells remained exactly the same. Reference genes missing in the query were set
to 0, as recommended in (15). To generate a joint embedding of query and reference cells, we
concatenated the latent dimensions learnt for query cells to the latent dimensions used for the
reference embedding and computed the KNN graph and UMAP as described above. To assess
that the mapping to the developmental reference conserves biological variation while minimising
technical variation in the query data, we compared query cell type labels and batch labels with
clusters obtained from Leiden clustering on the learnt latent dimensions, using the Normalized
Mutual Information score (see fig. S33 for mapping of adult query data).

Annotation prediction using CellTypist
We used CellTypist v.0.1.9 Python package (21) to perform annotation prediction with logistic
regression models. For prediction on cycling B cells, the rest of the non-progenitor B cells,
including immature B, mature B, B1 and plasma B cells were used as training dataset. Default
parameters were used for model building and prediction was made without majority voting for
accurate enumeration of predicted B cell subtypes within cycling B cells.

Comparison with human adult immune cells
Single-cell RNA-seq data from adult immune cells was generated and preprocessed as described
(21). The dataset including cell type annotations were provided by the authors. We mapped
264,929 adult lymphoid cells to the lymphoid embeddings of our developmental dataset and
54,047 adult myeloid cells to our myeloid embedding.

In order to use cell annotations in our developmental dataset to predict adult cell types in the
joint embedding, for each adult cell c we identified its k nearest prenatal cell neighbors (𝑁/)
(k=50), and calculated the probability of assigning a label y to adult cell c as

11

Submitted Manuscript: Confidential

Pr(𝑌	 = 	𝑦	|	𝑋	 = 𝑐, 𝑁/) 	 =

1
𝑘

>
H 𝐼(𝑦(") = 	𝑦)
"?@

where 𝑦(") is the label of the ith nearest neighbor and I is the binary indicator function. To label
each cell we calculate 𝑦E/as follows

𝑦E/ = argmaxA		Pr	(𝑌	 = 	𝑦	|	𝑋	 = 𝑐, 𝑁/)
and label c as 𝑦E/ if Pr(𝑌	 = 	𝑦	|	𝑋	 = 𝑐, 𝑁/) 	 > 	0.8, otherwise c is labeled as “low confidence”.

To quantify similarity of adult cells to prenatal cells (fig. S12C, fig. S17C), for each adult cell c,
we calculated its similarity to prenatal cells labeled as 𝑦E/ taking the Euclidean distance in the
joint embedding, weighted by a Gaussian kernel following the approach described in (15).

Blood and immune cell progenitors scRNA-seq data analysis
For the cell fate prediction analysis shown in fig. S20, C and D, we used the Palantir method as
implemented in CellRank (94, 95). Briefly, from the scVI embedding on all immune cells (fig.
S20A) we selected cells belonging to progenitor populations and computed a KNN graph on
scVI latent dimensions on these cells (k=30). Then transition probabilities were calculated using
the ConnectivityKernel in the cellrank package. We computed coarse-grained macrostates with
Generalized Perron Cluster Cluster Analysis, setting the number of macrostates to the number of
annotated progenitor cell populations. We manually set the four target terminal states for each
lineage (small pre B cells, DN(Q) T cells, early MKs, and promonocytes) and computed the
probability of each cell to transition to one of the four terminal states. The fate simplex
visualization in fig. S20, C and D, was generated using the function
cellrank.pl.circular_projection.

Artificial thymic organoids scRNA-seq data analysis
Raw scRNA-seq reads were mapped with cellranger 3.0.2 with combined human reference of
GRCh38.93 and mouse reference of mm10-3.1.0. Low quality cells were filtered out (minimum
number of reads = 2000, minimum number of genes = 500, minimum Scrublet (77) doublet
detection score <0.4). Cells where the percentage of counts from human genes was <90% were
considered as mouse cells and excluded from downstream analysis. Cells were assigned to
different cell lines (Kolf, Fiaj) using genotype prediction with souporcell (v.2.4.0) (78). We
performed batch correction to minimize the differences between cells from different cell lines
using scVI and clustered cells using the Leiden algorithm on the latent embedding as described
above. We used CellTypist v.0.1.9 Python package (21) to perform annotation prediction with
logistic regression using the whole in vivo scRNA-seq developmental dataset for training.
Stochastic gradient descent was used (setting use_SGD = True), and maximum iterations were
set to 1000 in model building to reduce the run time. Predicted annotations were then aggregated
using a majority voting scheme with majority_voting = True, over_clustering = leiden in
CellTypist prediction to refine cell identities within Leiden clusters. For the in vivo-to-in vitro
similarity analysis in fig. S29D, we mapped in vitro cells to the scVI model of lymphoid cells as
described above. For each cell in the in vitro dataset we calculated the Euclidean distance
(weighted by a Gaussian kernel as described above) to the closest in vivo cell from each in vivo
cell population.

12

Submitted Manuscript: Confidential

Spatial data analysis

Spatial transcriptomics data was mapped using spaceranger v.1.2.1. In parallel, we used a custom
image-processing script to identify regions overlapping tissues and retained for analysis the
intersection of the tissue spots identified by this pipeline and by tissue calling by spaceranger. To
map cell types identified by scRNA-seq in the profiled spatial transcriptomics slides, we used the
cell2location method (16). Briefly, this consists of two steps. First, for each of the profiled
organs we trained a negative binomial regression model to estimate reference transcriptomic
profiles for all the cell types profiled with scRNA-seq in the organ. Here we excluded very lowly
expressed genes using a recommended filtering strategy (16). Cell types where fewer than 20
cells were profiled in the organ of interest and cell types labeled as low-quality cells were
excluded from the reference. For the analysis of unconventional T cell localization in thymus
(fig. S27C), we trained a reference adding all the prenatal thymic epithelial cells from a thymus
cell atlas (7) (data was downloaded from Zenodo (96)). Next, we estimated the abundance of cell
types in the spatial transcriptomics slides using reference transcriptomic profiles of different cell
types. All slides representing a given organ were analyzed jointly. Cell2location requires the
choice of two hyperparameters: (1) expected cell abundance (N_cells_per_location = 30) which
was determined by counting average number of nuclei in the histology images corresponding to
Visium spots; (2) regularization strength of detection efficiency effect (detection_alpha = 20)
was used at the low setting to account for variations in RNA detection sensitivity across different
spots of Visium slides. The training was stopped after the cell2location model converged, the
number of training iterations was 50,000 for thymus, liver, spleen and 30,000 for gut. All other
parameters were used at default settings. Cell2location estimates the posterior distribution of cell
abundance of every cell type in every spot. Posterior distribution was summarized as 5%
quantile, representing the value of cell abundance that the model has high confidence in, and thus
incorporating the uncertainty in the estimate into values reported in the paper and used for
downstream colocalization analysis.

To identify microenvironments of colocalizing cell types, we used non-negative matrix
factorization (NMF) on the matrix of estimated cell type abundances X of dimensions 𝑛 × 𝑐,
where n is the total number of spots in the Visium slides and c is the number of cell types in the
reference. We decomposed the estimated cell type abundances X as 𝑋 = 𝑊𝑍B, where Z is a
𝑛 × 𝑑 matrix of latent factor values for each spot and W is a 𝑑 × 𝑐 matrix representing the
fraction of abundance of each cell type attributed to each latent factor. Here latent factors
correspond to tissue microenvironments defined by a set of colocalized cell types. We use the
NMF implementation in scikit-learn (81), with the wrapper in the cell2location package, setting
the number of factors d = 10. For downstream analysis, we excluded cell types where the 99%
quantile of cell abundance across locations in every slide from the same organ was always below
the detection threshold of 0.15. Unless otherwise specified, we consider a cell type to be part of a
microenvironment if the cell type fraction was over 0.2.

For analysis of mature T cell localization in the thymic medulla (fig. S27, D and E), we retained
factors where the sum of the cell type fractions for mature T cells (CD4+ T, CD8+ T, Treg, type 1
innate T, type 3 innate T, and CD8AA) was above 0.8. We assigned spots to the inner medulla or
cortico-medullary microenvironment if the factor value in the spot was above the 90% quantile
of all values in the slide. To annotate histological regions in the thymus, we extracted image
features from the high resolution images of H&E staining using the python package squidpy

13

Submitted Manuscript: Confidential

(v1.1.2) (97) (running sq.im.calculate_image_features, with parameters features = "histogram",
spot_scale = 1, mask_circle = True). We scaled and mean centered image feature matrix, and
performed Leiden clustering on the first 10 principal components. We manually annotated spot
clusters overlapping the thymic cortex and medulla. To define the cortico-medullary junction
(CMJ), we detected the spatial neighbors of each spot in medulla or cortex (using the function
squidpy.gr.spatial_neighbours, with parameters n_rings = 1, coord_type = "grid", n_neighs =
6). We then labeled a spot as CMJ if it had at least five neighbors (to exclude tissue borders), and
if the neighbors included spots from both medulla and cortex regions. For each spot we
calculated the distance to the CMJ as the Euclidean distance between the spatial coordinates of
the spot and the closest spot annotated as CMJ.

B1 functional validation experiment

Spleens were isolated from two donors, F144 (17 pcw) and F145 (15 pcw). A single-cell
suspension was obtained following the protocol described in the “Tissue acquisition and
processing” section. Cells were then cryopreserved with 90% FBS and 10% DMSO (Sigma-
Aldrich). On the day of the ELISpot experiment, cells were thawed and stained with anti-CD3
(BV510 anti-human CD3 antibody, BD Biosciences, 563109), anti-CD20 (FITC anti-human
CD20 antibody, Biolegend, 302303), anti-CD43 (PE anti-human CD43 antibody, BD
Biosciences, 560199), anti-CD27 (APC/Cy7 anti-human CD27 antibody, Biolegend, 356424),
anti-CD38 (BV711 anti-human CD38 antibody, Biolegend, 303527), anti-CCR10 (APC anti-
human CCR10 antibody, Biolegend, 341505) antibodies and DAPI together with control
peripheral blood mononuclear cells (PBMC; Stemcell Technologies). B cells were gated as
singlet DAPI–CD3–CD20+ cells. Plasma cells should generally be CD20lo and therefore not
included. To further exclude plasma cell contamination, we also gated out the top 1% of B cells
expressing the highest level of CD38. The rest of the B cells were then sorted into four fractions:
CCR10hi, CCR10loCD27+CD43+, CCR10loCD27–CD43+, and CCR10loCD27–CD43–. CD27 and
CD43 gates were chosen based on fluorescence minus one (FMO) controls. The cells were sorted
into RPMI supplemented with 10% FBS, penicillin–streptomycin (Gibco) and glutamax (Thermo
Fisher Scientific).

The ELISpot experiment was performed with Human IgM ELISpotBASIC kit (ALP) from
Mabtech AB. Post sorting, 7000-8000 cells were added into ELISpot plate pre-coated with anti-
IgM antibody following manufacturer’s instructions and incubated in a 37°C humidified
incubator with 5% CO2 for 22 hours. The plate was then washed and incubated with biotinylated
anti-IgM for 2 hours at room temperature, followed by 1-hour incubation of streptavidin-ALP.
The colored spots were developed with 15-min incubation of BCIP/NBT substrate solution
(Thermo Fisher Scientific). Five rounds of washing were performed between each step of
incubation as per manufacturer’s instructions. After the colored spots appeared clearly, the
reaction was then stopped by rinsing under running tap water for 5 min. Spots were counted with
the AID ELISpot reader and iSpot software version 4.

14

Submitted Manuscript: Confidential

In addition, we performed scRNA-seq of the sorted B cell fractions on a different donor (F149,
18 pcw fetal spleen), using the same gating strategy to further confirm the identity of sorted cells.
The scRNA-seq data was preprocessed with scVI as above. Cell annotations were predicted
using CellTypist v.0.1.9 (21), initially with our original developmental dataset as the training
data to find the non-B cells, then with only the non-cycling mature B cells from the
developmental dataset as the training data to map the B cells in the sorted data. Default
parameters were used for model building and prediction was made with majority voting.

15

Submitted Manuscript: Confidential

Supplementary Figures

16

Submitted Manuscript: Confidential

17

Submitted Manuscript: Confidential

fig. S1: Characterization of cross-organ developmental scRNA-seq atlas. (A) Sample characteristics in integrated
atlas. UMAP embeddings (as in Fig. 1C) of scRNA-seq profiles colored by (top to bottom): 10X chemistry protocol,
FACS protocol (CD45P: CD45+; CD45N: CD45–; TOT: unsorted), donor ID, sex of donor. (B) Distribution of cells
from different organs in integrated atlas. UMAP embeddings (as in Fig. 1C) of scRNA-seq profiles, highlighting
cells from each organ. (C) UMAP embeddings (as in Fig. 1C) of scRNA-seq profiles, highlighting cells for which
paired αβTCR, γδTCR or BCR sequences were detected. (D) Percentage of cells of each broad type in each organ,
stratified by FACS protocol. (E) Percentage of cells of each broad type in each gestational age group, stratified by
organ. (YS: yolk sac; LI: liver; BM: bone marrow; TH: thymus; SP: spleen; SK: skin; GU: gut; KI: kidney).

18

Submitted Manuscript: Confidential

fig. S2: Distribution across organs (left) and gestational age (pcw, right) of annotated cell populations. Cell
populations are grouped according to broad population annotations. The category “Other” denotes clusters annotated
as low-quality cells. N indicates the total number of cells across the dataset for each annotation. (YS: yolk sac; LI:
liver; BM: bone marrow; TH: thymus; SP: spleen; SK: skin; GU: gut; KI: kidney).

19

Submitted Manuscript: Confidential

fig. S3: Consistency across donors of annotated cell populations. Dot size and color are proportional to the number
of cells of the annotated population from each donor and organ. Cell populations are grouped according to broad
population annotations. The category “Other” denotes clusters annotated as low-quality cells.

20

Submitted Manuscript: Confidential

21

Submitted Manuscript: Confidential

22

Submitted Manuscript: Confidential

fig.  S4:  Cross-tissue  annotation  of  hierarchical  subsets  of  scRNA-seq  integrated  dataset.  For  each  subset
embedding generated through scVI, we show UMAP embeddings of cells colored by annotated cell populations and
dot plots of mean expression (log-normalized counts, dot color) and fraction of expressing cells (dot size) of marker
genes  (columns)  used  for  cell  population  annotation  (rows).  (A  and  B)  Annotation  of  stromal  cells.  (C  and  D)
Annotation of megakaryocyte and erythroid cells (cells in gray are progenitors annotated through embedding shown
in (E)). (E and F) Annotation of hematopoietic and immune cell progenitors. (G and H) Annotation of myeloid cells
(cells  in  gray  are  progenitors  annotated  through  embedding  shown  in  (E)  or  low-quality  clusters)  (I  and  L)
Annotation of lymphoid cells (cells in gray are progenitors annotated through embedding shown in (E) or low-quality
clusters). The embedding of all lymphoid cells is shown in (I), the embedding used for annotation of NK/T cells is
visualized in (J). The dot plot for annotation of B cells is shown in (K), and the dot plot for annotation of T cells is
displayed in (L).

23

Submitted Manuscript: Confidential

fig. S5: Overview of the hierarchical subsetting strategy used for annotation of fine immune subtypes. In each
embedding, the cells that make up the data views in fig. S4 are highlighted in blue.

24

Submitted Manuscript: Confidential

fig. S6: Experimental design and library QC for Visium 10X data (A) H&E staining of tissue slides processed
for spatial transcriptomics with Visium 10X protocol. Slides are grouped by organ (columns) and embryo/fetus ID
(rows). (B) Total RNA counts in analyzed tissue spots (scale bar: 1 mm).

25

Submitted Manuscript: Confidential

fig. S7: Robustness of spatial cell type abundance predictions with cell2location. (A) Analysis of robustness of
cell type mapping with cell2location: for mapping on each organ we correlate the total abundance (in log10 scale) of
each cell type (points) in different tissue slides from the same organ (biological replicates). The Pearson correlation
coefficient and P-value for permutation test are reported. (B) Robustness of colocation predictions with NMF. We
compare the NMF model learnt on all samples from the same organ with NMF models learnt leaving one sample out
(as indicated by y-axis label). The color of the heatmaps represents the Pearson correlation between cell type fraction
attributed to each factor in the compared models.

26

Submitted Manuscript: Confidential

fig. S8: Cell type spatial microenvironments in the fetal liver detected by non-negative matrix factorization
on  spatial  cell  type  abundances.  (A)  Dot  plot  of  cell  type  contributions  to  latent  factors  (microenvironments)
identified with non-negative matrix factorization of spatial cell type abundances estimated with cell2location. The
color and the size of the dots represent the relative fraction of the cell population assigned to the factor. We exclude
cell types where the value for the 99% quantile of cell abundance in all the slides from the same organ is always
below the detection threshold of 0.15. (B to D) Spatial locations of microenvironments on liver slides, with the color
representing the weighted contribution of each microenvironment to each spot. H&E staining images for each slide
are shown for reference (scale bar: 1 mm).

27

Submitted Manuscript: Confidential

fig. S9: Cell type spatial microenvironments in the fetal thymus detected by non-negative matrix factorization
on spatial abundances. (A) Dot plot of cell type contributions to latent factors (microenvironments) identified with
non-negative matrix factorization of spatial cell type abundances estimated with cell2location. The color and the size
of the dots represent the relative fraction of the cell population assigned to the factor. We exclude cell types where
the value for the 99% quantile of cell abundance in all the slides from the same organ is always below the detection
threshold of 0.15. (B to D) Spatial locations of microenvironments on thymus slides, with the color representing the
weighted contribution of each microenvironment to each spot. H&E staining images for each slide are shown for
reference (scale bar: 1 mm).

28

Submitted Manuscript: Confidential

fig. S10: Cell type spatial microenvironments in the fetal spleen detected by non-negative matrix factorization
on spatial abundances. (A) Dot plot of cell type contributions to latent factors (microenvironments) identified with
non-negative matrix factorization of spatial cell type abundances estimated with cell2location. The color and the size
of the dots represent the relative fraction of the cell population assigned to the factor. We exclude cell types where
the value for the 99% quantile of cell abundance in all the slides from the same organ is always below the detection
threshold of 0.15. (B to E) Spatial locations of microenvironments on spleen slides, with the color representing the
weighted contribution of each microenvironment to each spot. H&E staining images for each slide are shown for
reference (scale bar: 1 mm). (F) Illustration of inset displayed in G of fetal spleen tissue slide shown in B (scale bar:
1 mm). (G) Higher magnification view of slide in F showing weighted microenvironment contribution (factor values)
of lymphoid aggregates B cell zone microenvironment (Factor 8) and T cell zone microenvironment (Factor 9) (scale
bar: 200 μm). These exemplify how the B and T cell zones were proximal to each other but did not completely
overlap.

29

Submitted Manuscript: Confidential

fig.  S11:  Distribution  of  proliferating  macrophages.  (A)  UMAP  embedding  of  macrophage  cells  colored  by
annotated  subpopulations.  Dimensionality  reduction  with  scVI,  KNN  graph  construction  and  UMAP  embedding
were performed on macrophages as described for other subsets. We repeated Leiden clustering on this embedding
and  propagated  labels  from  the  annotations  obtained  on  the  myeloid  embedding.  (B)  Distribution  and  mixing  of
proliferating  (MKI67+TOP2A+)  macrophages  identified  in  myeloid  clustering  (fig.  S4G).  (C)  Fraction  of
proliferating  macrophages  within  each  macrophage  subpopulation  defined  as  in  (A).  Each  point  represents  one
embryo/fetus, color-coded by organ. The size of the point represents the cell count (YS: yolk sac; LI: liver; BM:
bone marrow; TH: thymus; SP: spleen; MLN: mesenteric lymph node; SK: skin; GU: gut; KI: kidney).

30

Submitted Manuscript: Confidential

fig. S12: Mapping of adult myeloid cells to prenatal reference with transfer learning. (A) UMAP embeddings
of mapping of adult myeloid cells (54,047 cells) to developmental myeloid reference (218,758 cells) using scArches
on scVI model. Points are colored by the dataset of origin. (B) UMAP embedding as in A, points are colored by cell
population  annotation  label,  for  adult  cells  (left)  and  developmental  cells  (right).  (C)  Correspondence  between
developmental and adult myeloid transcriptional phenotypes estimated by label transfer after mapping with scArches.
The dot size is proportional to the fraction of cells in the adult population (y-axis) with a given predicted prenatal
cell population label (x-axis). The dot color denotes the median similarity of the adult cells to prenatal cells in the
common embedding. Adult cells where less than 80% of prenatal neighbors have a uniform annotation are labeled
as “low confidence”.

31

Submitted Manuscript: Confidential

fig. S13: Prenatal-adult comparison in monocytes. (A) Dot plot of expression of monocyte subtype markers in
adult cells aligned to prenatal monocyte subtypes. (B) Heat map of distribution across organs of adult cells aligned
to prenatal monocyte subtypes (TLN: thoracic lymph nodes, THY: thymus, TCL: transverse colon, SPL: spleen,
SKM: skeletal muscle, SCL: sigmoid colon, OME: omentum, MLN: mesenteric lymph node, LNG: lung, LIV: liver,
ILE: ileum, DUO: duodenum, CAE: cecum, BMA: bone marrow, BLD: blood).

32

Submitted Manuscript: Confidential

33

Submitted Manuscript: Confidential

fig. S14: Differential abundance across gestation in myeloid cell populations. (A) Milo neighborhood embedding
of myeloid cells showing differential abundance across gestation. Each point represents a neighborhood, the layout
of points is determined by the position of the neighborhood index cell in the UMAP in fig. S4G, the size of points is
proportional to the number of cells in the neighborhood. Neighborhoods are colored by their log-fold change (logFC)
in  abundance  over  time,  where  logFC>0  indicates  significant  enrichment  in  early  cells  and  logFC  >  0  indicates
significant  enrichment
late  cells.  Only  neighborhoods  showing  significant  differential  abundance
(SpatialFDR<10%) are colored. (B and C) Gene set enrichment analysis results for differentially expressed genes in
gestation stage-specific neighborhoods of macrophages. Each plot shows the top 10 significant hits for the gene list.
The x-axis shows the negative log10 of the P-value adjusted for multiple testing (Benjamini–Hochberg correction).
The size of the dots is proportional to the number of genes associated with the gene set. The color represents the
combined  enrichr  score  calculated  with  gseapy.  Results  using  the  Gene  Ontology  Biological  Process  and  the
MSigDB Hallmark 2020 databases are shown. (B) Gene set enrichment analysis for genes overexpressed in early-
specific neighborhoods of LYVE1hi macrophages and proliferating macrophages. (C) Gene set enrichment analysis
for genes overexpressed in late-specific neighborhoods of iron-recycling macrophages and MHCIIhi macrophages.

in

34

Submitted Manuscript: Confidential

35

Submitted Manuscript: Confidential

fig. S15: Differential expression analysis on early-specific neighborhoods of mast cells. (A) Average expression
by time point of 185 genes overexpressed in early-specific neighborhoods of mast cells. Genes associated with TNF
signaling via NF-κB are highlighted in red. (B) Gene set enrichment analysis results using the MSigDB Hallmark
2020 database. The x-axis shows the negative log10 of the P-value adjusted for multiple testing (Benjamini–Hochberg
correction).  The  size  of  the  dots  is  proportional  to  the  number  of  genes  associated  with  the  gene  set.  The  color
represents the combined enrichr score calculated with gseapy.

36

Submitted Manuscript: Confidential

fig. S16: Differential abundance across organs in myeloid cell populations. (A) Milo neighborhood embedding
of myeloid cells. Each point represents a neighborhood, the layout of points is determined by the position of the
neighborhood index cell in the UMAP in fig. S4G, the size of points is proportional to the number of cells in the
neighborhood. Neighborhoods are colored by their log-fold change in abundance between the specified organ and
all other organs. Only neighborhoods showing significant enrichment (SpatialFDR<10% and logFC!2) are colored.
(B) Dot plot of enrichment analysis results on genes upregulated (left) and downregulated (right) in bone marrow
CCR2hi monocytes compared to other organs. The x-axis represents the negative log10 of P-values adjusted for
multiple testing (Benjamini–Hochberg correction) The y-axis shows the top 10 enriched gene sets (using the
MSigDB Hallmark 2020 database). The size of the dots is proportional to the number of genes associated with the

37

Submitted Manuscript: Confidential

gene set. The color represents the combined enrichr score calculated with gseapy. (C) Dot plot of CXCL12
expression in cell populations in the bone marrow. The color represents the average expression level (normalized
and log-transformed counts) and the size represents the cell count of each cell type within bone marrow. Only cell
populations with average expression > 1, and cell count > 10 are shown. (D) Fraction of abundance of monocyte
subsets for each donor in liver (LI) and bone marrow (BM). Donors are ordered by gestational age.

38

Submitted Manuscript: Confidential

fig. S17: Mapping of adult lymphoid cells to prenatal reference with transfer learning. (A) UMAP embeddings
of mapping of adult lymphoid cells (264,929) to prenatal lymphoid reference (218,758 cells) using scArches on scVI
model.  Points  are  colored  by  the  dataset  of  origin.  (B)  UMAP  embedding  as  in  A,  points  are  colored  by  cell
population annotation label, for adult cells (left) and prenatal cells (right). (C) Correspondence between prenatal and
adult myeloid transcriptional phenotypes estimated by label transfer after mapping with scArches. The dot size is
proportional to the fraction of cells in the adult population (y-axis) with a given predicted prenatal cell population
label  (x-axis).  The  dot  color  denotes  the  median  similarity  of  the  adult  cells  to  prenatal  cells  in  the  common
embedding. Adult cells where less than 80% of prenatal neighbors have a uniform annotation are labeled as “low
confidence”. (D) The fraction of adult CD4+ effector T cells that were matched to fetal CD4+ T cells show increased
expression of naive markers (SELL, CCR7) and CD4+T effector markers (KLRB1) compared to effector cells not
having a developmental equivalent (low confidence). This indicates that the matching might be driven by additional
heterogeneity in this adult cell compartment, instead of the true correspondent of adult memory T cells within fetal
cells.

39

Submitted Manuscript: Confidential

fig.  S18:  Differential  abundance  across  gestation  in  lymphoid  cell  populations.  (A)  Milo  neighborhood
embedding of lymphoid cells showing differential abundance across gestation. Each point represents a neighborhood,
the layout of points is determined by the position of the neighborhood index cell in the UMAP in fig. S4I, the size
of points is proportional to the number of cells in the neighborhood. Neighborhoods are colored by their log-fold
change (logFC) in abundance over time, where logFC > 0 indicates significant enrichment in early cells and logFC >
0  indicates  significant  enrichment  in  late  cells.  Only  neighborhoods  showing  significant  differential  abundance
(SpatialFDR < 10%) are colored. (B-C) Gene set enrichment analysis results for differentially expressed genes in
early-specific  neighborhoods  (B)  and  late  specific  neighborhoods  (C)  of  NK  cells.  Each  plot  shows  the  top  10
significant hits for the gene set. The  x-axis shows the negative log10 of the P-value adjusted for multiple testing
(Benjamini–Hochberg correction). The size of the dots is proportional to the number of genes associated with the
gene set. The color represents the combined enrichr score calculated with gseapy. Results using the Gene Ontology
Biological Process and the MSigDB Hallmark 2020 databases are shown.

40

Submitted Manuscript: Confidential

fig. S19: Differential abundance across organs in lymphoid compartment. (A) Milo neighborhood embedding
of lymphoid cells showing differential abundance between organs. Each point represents a neighborhood, the layout
of points is determined by the position of the neighborhood index cell in the UMAP in fig. S4I, the size of points is
proportional  to  the  number  of  cells  in  the  neighborhood.  Neighborhoods  are  colored  by  their  log-fold  change  in
abundance between the specified organ and all other organs. Only neighborhoods showing significant enrichment
(SpatialFDR  <  10%  and  log-fold  change  >  2)  are  colored.  (B)  Dot  plot  of  enrichment  analysis  results  on  genes
upregulated (left) and downregulated (right) in thymic mature T cells compared to other organs. The x-axis represents
the negative log10 of P-values adjusted for multiple testing (Benjamini–Hochberg correction) The y-axis shows the
top 10 enriched gene sets (using the MSigDB Hallmark 2020 database). The size of the dots is proportional to the
number  of  genes  associated  with  the  gene  set.  The  color  represents  the  combined  enrichr  score  calculated  with
gseapy.

41

Submitted Manuscript: Confidential

42

Submitted Manuscript: Confidential

fig. S20. Full spectrum of hematopoietic progenitors in peripheral organs. (A) UMAP embedding of all immune
and blood cells, highlighting the progenitor cell populations. Dashed boxes highlight lineage populations shown in
B. (B) Density plot of cells from each organ on a subset of UMAP embedding for different hematopoietic lineages.
Density  is  calculated  over  all  immune  cells  within  each  organ.  (C)  Simplex  projection  of  cells  in  progenitor
populations according to fate probabilities for each immune and blood cell lineage. Each cell is placed inside the
simplex according to its probability of reaching any of the terminal states. Cells in the center have higher multilineage
potential, whereas cells closer to one of the corners are more committed. (D) Binned density of cells for each organ
over the fate simplex shown in C, where the color of the 2D bin represents the number of cells from the organ in that
position in the simplex.

43

Submitted Manuscript: Confidential

fig. S21. Multiplex smFISH validation of B cell progenitors in peripheral tissues. Multiplex smFISH staining of
DAPI, CDH5 for endothelial cells, and VPREB1, RAG1 with/without DNTT for B cell progenitors in the human (A)
prenatal spleen at 14 pcw and (B) prenatal thymus at 16 pcw. Left: cells highlighted from corresponding regions in
the right panel overview matched by numbers (scale bar: 20 μm). Middle: CDH5 channel alone depicting endothelial
cells.  Right:  full  section  view  with  the  areas  of  interest  boxed  (scale  bar:  1  mm).  White  arrows  point  to  B  cell
progenitors identified. (C) Dot plot showing log normalized expressions of CDH5, VPREB1, RAG1, and DNTT in
the corresponding cell populations. Only cell types with log normalized expression at least 2 in at least one of the
four genes are shown here.

44

Submitted Manuscript: Confidential

fig. S22. Multiplex smFISH validation of megakaryocyte/erythroid progenitors in peripheral tissues. Multiplex
smFISH staining of DAPI, CDH5 for endothelial cells, and KLF1, TESPA1 for megakaryocyte/erythroid progenitors
in  the  human  (A)  prenatal  spleen  at  14  pcw  and  (B)  prenatal  thymus  at  16  pcw.  Left:  cells  highlighted  from
corresponding regions in the right panel overview matched by numbers (scale bar: 20 μm). Middle: CDH5 channel
alone depicting endothelial cells. Right: full section view with the areas of interest boxed (scale bar: 1 mm). White
arrows point to megakaryocyte/erythroid progenitors identified. (C) Dot plot showing log normalized expressions of
CDH5, KLF1, and TESPA1 in the corresponding cell populations. Only cell types with log normalized expression at
least 2 in at least one of the three genes are shown here.

45

Submitted Manuscript: Confidential

fig. S23. Multiplex smFISH validation of myeloid progenitors in peripheral tissues. Multiplex smFISH staining
of DAPI, CDH5 for endothelial cells, and MPO and AZU1 for myeloid progenitors in the human (A) prenatal intestine
at 15 pcw and (B) prenatal thymus at 16 pcw. Left: cells highlighted from corresponding regions in the right panel
overview matched by numbers (scale bar: 20 μm in (A) and 10 μm in (B)). Middle: CDH5 channel alone depicting
endothelial cells. Right: full section view with the areas of interest boxed (scale bar: 1 mm). White arrows point to
myeloid progenitors identified. (C) Dot plot showing log normalized expressions of CDH5, MPO, and AZU1 in the
corresponding cell populations. Only cell types with log normalized expression at least 2 in at least one of the three
genes are shown here.

46

Submitted Manuscript: Confidential

fig.  S24.  System-wide  B  lymphopoiesis.  (A)  Sum  of  abundances  of  B  progenitor  cell  populations  in  spatial
transcriptomics slides estimated with cell2location (scale bar: 1 mm). (B) Distribution of distance to the closest spot
assigned as splenic lymphoid aggregate microenvironment from spots containing B cell progenitors (red) and from
all analyzed spots (gray). Distance is measured as Euclidean distance of spots in spatial coordinates. We test if the
distance to lymphoid aggregates is significantly smaller in B cell progenitor spots compared to other spots with a
permutation  test  (5000  samples).  Spots  were  assigned  to  the  lymphoid  aggregate  microenvironment  if  the  NMF
factor  value  for  the  microenvironment  (Fig.  1D,  “B  cell  zone”)  was  above  the  95%  quantile  for  that  slide.  We
considered spots to contain B cell progenitors if the sum of abundances of the B cell progenitors was above the 95%
quantile for that slide. (C) Predicted cell–cell interactions between B cell progenitors and colocalizing cell types
(ILC3, LYVE1hi macrophage, NK cells, cycling NK cells and type 1 innate T cells, excluding LMPP_MLP as they
are likely to be upstream progenitors of B lineage progenitors) from CellPhoneDB across liver (LI), spleen (SP) and
thymus (TH). The first gene in each ligand-receptor pair is expressed in B cell progenitors and the second in the

47

Submitted Manuscript: Confidential

interacting  cell  type.  The  color  represents  the  average  expression  values  of  the  ligand  and  receptor  within  their
corresponding cell types, and the size represents −log(P-value). In addition to the previously described CXCL12–
CXCR4 interaction in murine studies (102, 103), our analysis identified many additional novel interactions that may
inform efforts to generate and engineer B cells in vitro.

48

Submitted Manuscript: Confidential

fig. S25. Characterization of B cells. (A) Close-up view of B cell populations on the UMAP embedding of all
lymphoid cells (as shown in fig. S4I), colored by annotated cell population identity (top), status summary of cells
expressing  productive  heavy  (IGH)  and/or  light  chains  (IGK  or  IGL)  of  BCR  from  single-cell  BCR  sequencing
(middle), and colored by IL7R expression pattern (bottom). (B) Marker gene expression patterns overlaid onto the
same  UMAP  plot  in  Fig.  5A.  Immature  B  cells  were  characterized  by  higher  expression  of  CD19,  CD24,  and
VPREB3. Mature B, cycling B, plasma B, and putative B1 cells expressed MS4A1 except plasma B (MS4A1lo and
expressing CD38, SDC1, and JCHAIN). Cycling B cells were additionally marked with MKI67.

49

Submitted Manuscript: Confidential

50

Submitted Manuscript: Confidential

fig.  S26.  Characterization  of  putative  B1  cells.  (A)  Close-up  view  of  cycling  B  cell  population  on  UMAP
embedding of all lymphoid cells (as shown in fig. S4I), colored by original cell population annotation (left) and
annotations predicted by logistic regression trained on all non-progenitor B cell subsets (right). This assigns specific
cell identity to each of the cells within the cycling B cell group. The results are used in Fig. 5B. (B) Ratio of B1 cell
number over mature B cell number in different organs across different gestational age bins. (C) Heat map showing
the percentage of each BCR heavy (IGHV, IGHJ) and light chain (IGKV/IGLV, IGKJ/IGLJ) V and J gene segments
present in different B cell subtypes. (D) Barplot of cell fractions with different clonotype size across different mature
B cell subtypes. (E) Violin plot of B cell activation scores in B1 and mature B cells. Cells were scored according to
expression values of all genes in the Gene Ontology B Cell Activation gene list. A significant difference in B cell
activation scores was observed between B1 and mature B cells after controlling for donors and organs with linear
regression  (***P-value<10–10).  (F)  Heatmap  of  TF  activity  means  in  B1  and  mature  B  cells.  The  color  and  the
number represent the average TF activity estimated by DoRothEA (94). Only the top 25 TFs that had significantly
higher activities in B1 cells were shown here. TFs in TNF-α and NF-κB signaling pathway (CEBPD, JUN, MYC,
JUNB)  are  boxed  in  red.  (G)  Representative  flow  cytometry  plots  showing  the  sorting  strategy  for  the  ELISpot
experiment  shown  in  Fig.  5E.  The  splenic  B  cells  were  gated  from  live  single  cells  which  were  CD3–CD20+,
excluding the top 1% of cells expressing the highest level of CD38 to avoid plasma cells (which should also be CD20
low  and  therefore  not  gated  in),  and  split  the  rest  into  four  fractions:  CCR10hi,  CCR10loCD27+CD43+,
CCR10loCD27–CD43+, and CCR10loCD27–CD43–. We then performed an ELISpot experiment on all four fractions
without any stimulation. (H) Barplot of cell proportions with different predicted annotations in the four sort fractions:
CCR10hi,  CCR10loCD27+CD43+,  CCR10loCD27–CD43+,  and  CCR10loCD27–CD43–.  (I)  Dot  plot  showing  gene
expressions of CCL27 and CCL28 within the stromal cell populations. Only cell types with log normalized expression
of CCL27 or that of CCL28 above 0.05 are shown here.

51

Submitted Manuscript: Confidential

52

Submitted Manuscript: Confidential

fig. S27. Distribution of unconventional T cells across gestation and in thymic tissue. (A) Left: Close-up view
of mature T cells on UMAP embedding of all NK/T cells (as shown in fig. S4J). Type 1 innate T, type 3 innate T
and CD8AA contain both αβT cells and γδT cells. Right: ZBTB16 expression pattern overlaid onto the same UMAP
plot.  (B)  Left:  proportion  of  unconventional  T  cells  in  all  mature  T  cells  in  different  organs  across  different
gestational age bins. Point size represents the number of mature T cells in a given organ within that age bin. Lines
and points are color-coded by organs (YS: yolk sac; LI: liver; BM: bone marrow; TH: thymus; SP: spleen; MLN:
mesenteric lymph node; SK: skin; GU: gut; KI: kidney). Right: proportion of each unconventional T cell subtype in
all mature T cells in thymus across different age groups, using dataset from (7). Point size represents the number of
mature  T  cells  in  thymus  within  that  age  bin.  (C)  Left:  cell  type  contributions  to  medullary  microenvironments
containing mature T cells in thymus, identified with non-negative matrix factorization of spatial cell type abundances
estimated with cell2location. The color and the size of the dots represent the relative fraction of the cell population
assigned  to  the  microenvironment.  Unconventional  T  cell  types  are  highlighted  in  magenta.  Conventional  T  cell
types are highlighted in green. Right: spatial locations of medullary microenvironments on different thymic slides,
with the color representing the weighted contribution of each microenvironment to each spot (scale bar: 1 mm). (D)
Top: annotation of tissue regions on Visium spots inferred by clustering of H&E image features. Bottom: location
of interface region between cortex and medulla region, which we consider as the cortico-medullary junction (CMJ)
(scale bar: 1 mm). (E) Histogram of Euclidean distance to the nearest CMJ spot for spots assigned to inner-medulla
microenvironment (red) or cortico-medullary microenvironment (blue). Spots were assigned to a microenvironment
if  the  NMF  factor  value  for  the  microenvironment  (see  C)  was  above  the  90%  quantile.  The  P-value  for  the
Kolmogorov–Smirnov test comparing the two distributions is reported.

53

Submitted Manuscript: Confidential

fig. S28. T cell receptor (TCR) sequence analysis. (A) Proportions of cells without any paired TCR expressing
orphan γδTCR, i.e. one of γ or δ chain, or orphan αβTCR, i.e. one of α or β chain, or both or neither. (B) Top left:
clonotype network graph of γδTCR. Each fully connected subnetwork represents a clonotype cluster, with each dot
representing a cell. The dots are color-coded by organs (YS: yolk sac; LI: liver; BM: bone marrow; TH: thymus; SP:
spleen; MLN: mesenteric lymph node; SK: skin; GU: gut; KI: kidney). Top right: γδTCR clonotype network graph
color-coded by cell types. Bottom left: γδTCR clonotype network graph color-coded by donors. Bottom right: barplot
of cell fractions with different γδTCR clonotype size across different unconventional T cell subtypes. (C) Heat map
showing the percentage of each TRBV, TRBD and TRBJ gene segment present in different T cell subtypes. (D)
Barplot of cell fractions with different clonotype size across different mature T cell subtypes.

54

Submitted Manuscript: Confidential

fig. S29. Analysis of artificial thymic organoids scRNA-seq data. (A) Dot plot of marker genes for ATO cell
populations. (B) Cells colored by the starting iPSC lines in ATO overlaid on UMAP embedding shown in Fig. 6F.
(C) Expression of T cell marker genes in ATO overlaid on UMAP embedding shown in Fig. 6F. (D) Violin plots of
similarity to closest in vivo cell (x-axis) for each cell type in the in vivo dataset (y-axis) for in vitro single-positive T

55

Submitted Manuscript: Confidential

cells  (SP_T),  NK  cells  and  developing  T  cells  (DN/DP).  Similarities  are  calculated  in  the  scVI  latent  space  for
lymphoid cells after mapping in vitro cells with scArches.

56

Submitted Manuscript: Confidential

fig. S30: Comparison across data integration methods. (A) UMAP embeddings of scRNA-seq profiles after data
integration with BBKNN colored by (top to bottom): 10X library prep protocol, donor ID, cellular compartment. (B)
heat map of confusion matrices between Leiden clusters and previously annotated cell type labels, with clustering
on  BBKNN  integration  (left,  37  clusters)  or  scVI  integration  (right,  75  clusters)  of  the  full  dataset  (clustering
resolution = 1.5). (C) heat map of confusion matrices between Leiden clusters and newly annotated cell type labels,
with clustering on BBKNN integration (left, 37 clusters) or scVI integration (right, 75 clusters) of the full dataset
(clustering resolution = 1.5). For each confusion matrix, the normalized mutual information (NMI) score between
cluster labels and annotation labels is shown.

57

Submitted Manuscript: Confidential

fig. S31: Agreement between annotations of progenitor cells in this study and annotations from fetal bone
marrow atlas (11). (A) Confusion table between annotations of progenitor cells in bone marrow in this study and
the annotations for the same cells in fetal bone marrow atlas (11). The color is proportional to the fraction of cells in
the new population with a given old label. Only bone marrow cells for which a previous annotation was available
are shown (32,274/46,448 bone marrow cells). (B) Confusion table between annotations of progenitor cells in bone
marrow in this study and the annotations for the same cells in fetal liver atlas (3). The color is proportional to the
fraction of cells in the new population with a given old label. Only liver cells for which a previous annotation was
available are shown (11,330/26,377 liver cells).

58

Submitted Manuscript: Confidential

59

Submitted Manuscript: Confidential

fig. S32: Validation of quantification of FACS effect on cell abundances in Milo neighborhoods. (A) Scatter
plot of SpatialFDR (in –log10 scale) estimated in test for differential abundance across gestational age, regressing out
continuous FACS factor (x-axis), without regressing out FACS effect (y-axis, top) and regressing out FACS protocol
label (CD45+/CD45–/unsorted) (y-axis, bottom). Results for the test on cells from liver (LI), spleen (SP) and thymus
(TH) are shown. The dotted red lines indicate the significance threshold of 10% SpatialFDR. (B) Scatterplot of log-
fold  change  estimated  in  test  for  differential  abundance  across  gestational  age  testing  on  the  subset  of  unsorted
samples (x-axis) and on FACS-isolated samples (y-axis), regressing out the FACS protocol label (top) or the FACS
factor (bottom).

60

Submitted Manuscript: Confidential

fig. S33: Validation of biological conservation after scArches mapping of adult cells to prenatal reference. (A
and B) Heat maps of confusion matrix between adult immune cell annotations (21) and Leiden clusters obtained with
latent  dimensions  after  mapping  adult  cells  on  the  prenatal  reference  with  scArches,  for  myeloid  cells  (A)  and
lymphoid cells (B). (C and D) Barplots of normalized mutual information (NMI) between technical batch or cell
type annotation and Leiden clusters from scArches mapping or the clusters in the original BBKNN embedding (21).

61

References and Notes

1. J.-E. Park, L. Jardine, B. Gottgens, S. A. Teichmann, M. Haniffa, Prenatal development of

human immunity. Science 368, 600–603 (2020). doi:10.1126/science.aaz9330 Medline

2. M. Jagannathan-Bogdan, L. I. Zon, Hematopoiesis. Development 140, 2463–2467 (2013).

doi:10.1242/dev.083147 Medline

3. D.-M. Popescu, R. A. Botting, E. Stephenson, K. Green, S. Webb, L. Jardine, E. F.

Calderbank, K. Polanski, I. Goh, M. Efremova, M. Acres, D. Maunder, P. Vegh, Y.
Gitton, J.-E. Park, R. Vento-Tormo, Z. Miao, D. Dixon, R. Rowell, D. McDonald, J.
Fletcher, E. Poyner, G. Reynolds, M. Mather, C. Moldovan, L. Mamanova, F. Greig, M.
D. Young, K. B. Meyer, S. Lisgo, J. Bacardit, A. Fuller, B. Millar, B. Innes, S. Lindsay,
M. J. T. Stubbington, M. S. Kowalczyk, B. Li, O. Ashenberg, M. Tabaka, D. Dionne, T.
L. Tickle, M. Slyper, O. Rozenblatt-Rosen, A. Filby, P. Carey, A.-C. Villani, A. Roy, A.
Regev, A. Chédotal, I. Roberts, B. Göttgens, S. Behjati, E. Laurenti, S. A. Teichmann, M.
Haniffa, Decoding human fetal liver haematopoiesis. Nature 574, 365–371 (2019).
doi:10.1038/s41586-019-1652-y Medline

4. B. J. Stewart, J. R. Ferdinand, M. D. Young, T. J. Mitchell, K. W. Loudon, A. M. Riding, N.
Richoz, G. L. Frazer, J. U. L. Staniforth, F. A. Vieira Braga, R. A. Botting, D.-M.
Popescu, R. Vento-Tormo, E. Stephenson, A. Cagan, S. J. Farndon, K. Polanski, M.
Efremova, K. Green, M. Del Castillo Velasco-Herrera, C. Guzzo, G. Collord, L.
Mamanova, T. Aho, J. N. Armitage, A. C. P. Riddick, I. Mushtaq, S. Farrell, D.
Rampling, J. Nicholson, A. Filby, J. Burge, S. Lisgo, S. Lindsay, M. Bajenoff, A. Y.
Warren, G. D. Stewart, N. Sebire, N. Coleman, M. Haniffa, S. A. Teichmann, S. Behjati,
M. R. Clatworthy, Spatiotemporal immune zonation of the human kidney. Science 365,
1461–1466 (2019). doi:10.1126/science.aat5031 Medline

5. Y. Zeng, J. He, Z. Bai, Z. Li, Y. Gong, C. Liu, Y. Ni, J. Du, C. Ma, L. Bian, Y. Lan, B. Liu,

Tracing the first hematopoietic stem cell generation in human embryo by single-cell RNA
sequencing. Cell Res. 29, 881–894 (2019). doi:10.1038/s41422-019-0228-6 Medline

6. Y. Zeng, C. Liu, Y. Gong, Z. Bai, S. Hou, J. He, Z. Bian, Z. Li, Y. Ni, J. Yan, T. Huang, H.
Shi, C. Ma, X. Chen, J. Wang, L. Bian, Y. Lan, B. Liu, H. Hu, Single-cell RNA
sequencing resolves spatiotemporal development of pre-thymic lymphoid progenitors and
thymus organogenesis in human embryos. Immunity 51, 930–948.e6 (2019).
doi:10.1016/j.immuni.2019.09.008 Medline

7. J.-E. Park, R. A. Botting, C. Domínguez Conde, D.-M. Popescu, M. Lavaert, D. J. Kunz, I.

Goh, E. Stephenson, R. Ragazzini, E. Tuck, A. Wilbrey-Clark, K. Roberts, V. R. Kedlian,
J. R. Ferdinand, X. He, S. Webb, D. Maunder, N. Vandamme, K. T. Mahbubani, K.
Polanski, L. Mamanova, L. Bolt, D. Crossland, F. de Rita, A. Fuller, A. Filby, G.
Reynolds, D. Dixon, K. Saeb-Parsy, S. Lisgo, D. Henderson, R. Vento-Tormo, O. A.
Bayraktar, R. A. Barker, K. B. Meyer, Y. Saeys, P. Bonfanti, S. Behjati, M. R.
Clatworthy, T. Taghon, M. Haniffa, S. A. Teichmann, A cell atlas of human thymic
development defines T cell repertoire formation. Science 367, eaay3224 (2020).
doi:10.1126/science.aay3224 Medline

8. R. Elmentaite, A. D. B. Ross, K. Roberts, K. R. James, D. Ortmann, T. Gomes, K. Nayak, L.

Tuck, S. Pritchard, O. A. Bayraktar, R. Heuschkel, L. Vallier, S. A. Teichmann, M.

Zilbauer, Single-cell sequencing of developing human gut reveals transcriptional links to
childhood Crohn’s disease. Dev. Cell 55, 771–783.e5 (2020).
doi:10.1016/j.devcel.2020.11.010 Medline

9. J. Cao, D. R. O’Day, H. A. Pliner, P. D. Kingsley, M. Deng, R. M. Daza, M. A. Zager, K. A.
Aldinger, R. Blecher-Gonen, F. Zhang, M. Spielmann, J. Palis, D. Doherty, F. J.
Steemers, I. A. Glass, C. Trapnell, J. Shendure, A human cell atlas of fetal gene
expression. Science 370, eaba7721 (2020). doi:10.1126/science.aba7721 Medline

10. G. Reynolds, P. Vegh, J. Fletcher, E. F. M. Poyner, E. Stephenson, I. Goh, R. A. Botting, N.
Huang, B. Olabi, A. Dubois, D. Dixon, K. Green, D. Maunder, J. Engelbert, M.
Efremova, K. Polański, L. Jardine, C. Jones, T. Ness, D. Horsfall, J. McGrath, C. Carey,
D.-M. Popescu, S. Webb, X. N. Wang, B. Sayer, J.-E. Park, V. A. Negri, D.
Belokhvostova, M. D. Lynch, D. McDonald, A. Filby, T. Hagai, K. B. Meyer, A. Husain,
J. Coxhead, R. Vento-Tormo, S. Behjati, S. Lisgo, A.-C. Villani, J. Bacardit, P. H. Jones,
E. A. O’Toole, G. S. Ogg, N. Rajan, N. J. Reynolds, S. A. Teichmann, F. M. Watt, M.
Haniffa, Developmental cell programs are co-opted in inflammatory skin disease. Science
371, eaba6500 (2021). doi:10.1126/science.aba6500 Medline

11. L. Jardine, S. Webb, I. Goh, M. Quiroga Londoño, G. Reynolds, M. Mather, B. Olabi, E.
Stephenson, R. A. Botting, D. Horsfall, J. Engelbert, D. Maunder, N. Mende, C.
Murnane, E. Dann, J. McGrath, H. King, I. Kucinski, R. Queen, C. D. Carey, C.
Shrubsole, E. Poyner, M. Acres, C. Jones, T. Ness, R. Coulthard, N. Elliott, S. O’Byrne,
M. L. R. Haltalli, J. E. Lawrence, S. Lisgo, P. Balogh, K. B. Meyer, E. Prigmore, K.
Ambridge, M. S. Jain, M. Efremova, K. Pickard, T. Creasey, J. Bacardit, D. Henderson,
J. Coxhead, A. Filby, R. Hussain, D. Dixon, D. McDonald, D.-M. Popescu, M. S.
Kowalczyk, B. Li, O. Ashenberg, M. Tabaka, D. Dionne, T. L. Tickle, M. Slyper, O.
Rozenblatt-Rosen, A. Regev, S. Behjati, E. Laurenti, N. K. Wilson, A. Roy, B. Göttgens,
I. Roberts, S. A. Teichmann, M. Haniffa, Blood and immune development in human fetal
bone marrow and Down syndrome. Nature 598, 327–331 (2021). doi:10.1038/s41586-
021-03929-x Medline

12. R. Lopez, J. Regier, M. B. Cole, M. I. Jordan, N. Yosef, Deep generative modeling for

single-cell transcriptomics. Nat. Methods 15, 1053–1058 (2018). doi:10.1038/s41592-
018-0229-2 Medline

13. D. Pellin, M. Loperfido, C. Baricordi, S. L. Wolock, A. Montepeloso, O. K. Weinberg, A.
Biffi, A. M. Klein, L. Biasco, A comprehensive single cell transcriptional landscape of
human hematopoietic progenitors. Nat. Commun. 10, 2395 (2019). doi:10.1038/s41467-
019-10291-0 Medline

14. A.-C. Villani, R. Satija, G. Reynolds, S. Sarkizova, K. Shekhar, J. Fletcher, M. Griesbeck, A.
Butler, S. Zheng, S. Lazo, L. Jardine, D. Dixon, E. Stephenson, E. Nilsson, I. Grundberg,
D. McDonald, A. Filby, W. Li, P. L. De Jager, O. Rozenblatt-Rosen, A. A. Lane, M.
Haniffa, A. Regev, N. Hacohen, Single-cell RNA-seq reveals new types of human blood
dendritic cells, monocytes, and progenitors. Science 356, eaah4573 (2017).
doi:10.1126/science.aah4573 Medline

15. M. Lotfollahi, M. Naghipourfar, M. D. Luecken, M. Khajavi, M. Büttner, M. Wagenstetter,
Ž. Avsec, A. Gayoso, N. Yosef, M. Interlandi, S. Rybakov, A. V. Misharin, F. J. Theis,

Mapping single-cell data to reference atlases by transfer learning. Nat. Biotechnol. 40,
121–130 (2022). doi:10.1038/s41587-021-01001-7 Medline

16. V. Kleshchevnikov, A. Shmatko, E. Dann, A. Aivazidis, H. W. King, T. Li, R. Elmentaite, A.
Lomakin, V. Kedlian, A. Gayoso, M. S. Jain, J. S. Park, L. Ramona, E. Tuck, A.
Arutyunyan, R. Vento-Tormo, M. Gerstung, L. James, O. Stegle, O. A. Bayraktar,
Cell2location maps fine-grained cell types in spatial transcriptomics. Nat. Biotechnol.
10.1038/s41587-021-01139-4 (2022). doi:10.1038/s41587-021-01139-4 Medline

17. S. Z. Chong, M. Evrard, S. Devi, J. Chen, J. Y. Lim, P. See, Y. Zhang, J. M. Adrover, B.

Lee, L. Tan, J. L. Y. Li, K. H. Liong, C. Phua, A. Balachander, A. Boey, D. Liebl, S. M.
Tan, J. K. Y. Chan, K. Balabanian, J. E. Harris, M. Bianchini, C. Weber, J. Duchene, J.
Lum, M. Poidinger, Q. Chen, L. Rénia, C.-I. Wang, A. Larbi, G. J. Randolph, W.
Weninger, M. R. Looney, M. F. Krummel, S. K. Biswas, F. Ginhoux, A. Hidalgo, F.
Bachelerie, L. G. Ng, CXCR4 identifies transitional bone marrow premonocytes that
replenish the mature monocyte pool for peripheral responses. J. Exp. Med. 213, 2293–
2314 (2016). doi:10.1084/jem.20160800 Medline

18. S. A. MacParland, J. C. Liu, X.-Z. Ma, B. T. Innes, A. M. Bartczak, B. K. Gage, J. Manuel,

N. Khuu, J. Echeverri, I. Linares, R. Gupta, M. L. Cheng, L. Y. Liu, D. Camat, S. W.
Chung, R. K. Seliga, Z. Shao, E. Lee, S. Ogawa, M. Ogawa, M. D. Wilson, J. E. Fish, M.
Selzner, A. Ghanekar, D. Grant, P. Greig, G. Sapisochin, N. Selzner, N. Winegarden, O.
Adeyi, G. Keller, G. D. Bader, I. D. McGilvray, Single cell RNA sequencing of human
liver reveals distinct intrahepatic macrophage populations. Nat. Commun. 9, 4383 (2018).
doi:10.1038/s41467-018-06318-7 Medline

19. E. Gerrits, Y. Heng, E. W. G. M. Boddeke, B. J. L. Eggen, Transcriptional profiling of
microglia; current state of the art and future perspectives. Glia 68, 740–755 (2020).
doi:10.1002/glia.23767 Medline

20. S. M. Toor, S. Wani, O. M. E. Albagha, Comprehensive transcriptomic profiling of murine

osteoclast differentiation reveals novel differentially expressed genes and lncRNAs.
Front. Genet. 12, 781272 (2021). doi:10.3389/fgene.2021.781272 Medline

21. C. Domínguez Conde, C. Xu, L. B. Jarvis, D. B. Rainbow, S. B. Wells, T. Gomes, S. K.

Howlett, O. Suchanek, K. Polanski, H. W. King, L. Mamanova, N. Huang, P. A. Szabo,
L. Richardson, L. Bolt, E. S. Fasouli, K. T. Mahbubani, M. Prete, L. Tuck, N. Richoz, Z.
K. Tuong, L. Campos, H. S. Mousa, E. J. Needham, S. Pritchard, T. Li, R. Elmentaite, J.
Park, E. Rahmani, D. Chen, D. K. Menon, O. A. Bayraktar, L. K. James, K. B. Meyer, N.
Yosef, M. R. Clatworthy, P. A. Sims, D. L. Farber, K. Saeb-Parsy, J. L. Jones, S. A.
Teichmann. Cross-tissue immune cell analysis reveals tissue-specific features in humans.
Science 376, eabl5197 (2022). doi:10.1126/science.abl5197 Medline

22. E. Dann, N. C. Henderson, S. A. Teichmann, M. D. Morgan, J. C. Marioni, Differential

abundance testing on single-cell data using k-nearest neighbor graphs. Nat. Biotechnol.
40, 245–253 (2022). Medline

23. K. C. M. Jeucken, J. J. Koning, R. E. Mebius, S. W. Tas, The role of endothelial cells and

TNF-receptor superfamily members in lymphoid organogenesis and function during
health and inflammation. Front. Immunol. 10, 2700 (2019).
doi:10.3389/fimmu.2019.02700 Medline

24. X. Yang, P. Lu, C. Fujii, Y. Nakamoto, J.-L. Gao, S. Kaneko, P. M. Murphy, N. Mukaida,
Essential contribution of a chemokine, CCL3, and its receptor, CCR1, to hepatocellular
carcinoma progression. Int. J. Cancer 118, 1869–1876 (2006). doi:10.1002/ijc.21596
Medline

25. F. Hua, Y. Tian, CCL4 promotes the cell proliferation, invasion and migration of endometrial
carcinoma by targeting the VEGF-A signal pathway. Int. J. Clin. Exp. Pathol. 10, 11288–
11299 (2017). Medline

26. E. C. Keeley, B. Mehrad, R. M. Strieter, CXC chemokines in cancer angiogenesis and

metastases. Adv. Cancer Res. 106, 91–111 (2010). doi:10.1016/S0065-230X(10)06003-3
Medline

27. J. Heidemann, H. Ogawa, M. B. Dwinell, P. Rafiee, C. Maaser, H. R. Gockel, M. F.

Otterson, D. M. Ota, N. Lügering, W. Domschke, D. G. Binion, Angiogenic effects of
interleukin 8 (CXCL8) in human intestinal microvascular endothelial cells are mediated
by CXCR2. J. Biol. Chem. 278, 8508–8515 (2003). doi:10.1074/jbc.M208231200
Medline

28. K. Norrby, Mast cells and angiogenesis. APMIS 110, 355–371 (2002). doi:10.1034/j.1600-

0463.2002.100501.x Medline

29. D. Ribatti, E. Crivellato, The role of mast cell in tissue morphogenesis. Thymus, duodenum,

and mammary gland as examples. Exp. Cell Res. 341, 105–109 (2016).
doi:10.1016/j.yexcr.2015.11.022 Medline

30. W. Wood, P. Martin, Macrophage functions in tissue patterning and disease: New insights
from the fly. Dev. Cell 40, 221–233 (2017). doi:10.1016/j.devcel.2017.01.001 Medline

31. K. Hoorweg, T. Cupedo, Development of human lymph nodes and Peyer’s patches. Semin.

Immunol. 20, 164–170 (2008). doi:10.1016/j.smim.2008.02.003 Medline

32. P. Rantakari, N. Jäppinen, E. Lokka, E. Mokkala, H. Gerke, E. Peuhu, J. Ivaska, K. Elima, K.
Auvinen, M. Salmi, Fetal liver endothelium regulates the seeding of tissue-resident
macrophages. Nature 538, 392–396 (2016). doi:10.1038/nature19814 Medline

33. N. Li, V. van Unen, T. Abdelaal, N. Guo, S. A. Kasatskaya, K. Ladell, J. E. McLaren, E. S.
Egorov, M. Izraelson, S. M. Chuva de Sousa Lopes, T. Höllt, O. V. Britanova, J.
Eggermont, N. F. C. C. de Miranda, D. M. Chudakov, D. A. Price, B. P. F. Lelieveldt, F.
Koning, Memory CD4+ T cells are generated in the human fetal intestine. Nat. Immunol.
20, 301–312 (2019). doi:10.1038/s41590-018-0294-9 Medline

34. A. Mishra, G. C. Lai, L. J. Yao, T. T. Aung, N. Shental, A. Rotter-Maskowitz, E.

Shepherdson, G. S. N. Singh, R. Pai, A. Shanti, R. M. M. Wong, A. Lee, C. Khyriem, C.
A. Dutertre, S. Chakarov, K. G. Srinivasan, N. B. Shadan, X.-M. Zhang, S. Khalilnezhad,
F. Cottier, A. S. M. Tan, G. Low, P. Chen, Y. Fan, P. X. Hor, A. K. M. Lee, M. Choolani,
D. Vermijlen, A. Sharma, G. Fuks, R. Straussman, N. Pavelka, B. Malleret, N.
McGovern, S. Albani, J. K. Y. Chan, F. Ginhoux, Microbial exposure during early human
development primes fetal immune cells. Cell 184, 3394–3409.e20 (2021).
doi:10.1016/j.cell.2021.04.039 Medline

35. Y. Xing, X. Wang, S. C. Jameson, K. A. Hogquist, Late stages of T cell maturation in the

thymus involve NF-κB and tonic type I interferon signaling. Nat. Immunol. 17, 565–573

(2016). doi:10.1038/ni.3419 Medline

36. L. V. Webb, S. C. Ley, B. Seddon, TNF activation of NF-κB is essential for development of

single-positive thymocytes. J. Exp. Med. 213, 1399–1407 (2016).
doi:10.1084/jem.20151604 Medline

37. C. Collins, E. Sharpe, A. Silber, S. Kulke, E. W. Y. Hsieh, Congenital athymia: Genetic

etiologies, clinical manifestations, diagnosis, and treatment. J. Clin. Immunol. 41, 881–
895 (2021). doi:10.1007/s10875-021-01059-7 Medline

38. P. G. Holt, C. A. Jones, The development of the immune system during pregnancy and early
life. Allergy 55, 688–697 (2000). doi:10.1034/j.1398-9995.2000.00118.x Medline

39. D. O. Griffin, N. E. Holodick, T. L. Rothstein, Human B1 cells in umbilical cord and adult

peripheral blood express the novel phenotype CD20+ CD27+ CD43+ CD70-. J. Exp.
Med. 208, 67–80 (2011). doi:10.1084/jem.20101499 Medline

40. D. O. Griffin, T. L. Rothstein, Human b1 cell frequency: Isolation and analysis of human b1
cells. Front. Immunol. 3, 122 (2012). doi:10.3389/fimmu.2012.00122 Medline

41. T. L. Rothstein, D. O. Griffin, N. E. Holodick, T. D. Quach, H. Kaku, Human B-1 cells take

the stage. Ann. N. Y. Acad. Sci. 1285, 97–114 (2013). doi:10.1111/nyas.12137 Medline

42. N. Baumgarth, The double life of a B-1 cell: Self-reactivity selects for protective effector
functions. Nat. Rev. Immunol. 11, 34–46 (2011). doi:10.1038/nri2901 Medline

43. P. A. Lalor, L. A. Herzenberg, S. Adams, A. M. Stall, Feedback regulation of murine Ly-1 B

cell development. Eur. J. Immunol. 19, 507–513 (1989). doi:10.1002/eji.1830190315
Medline

44. K. Hayakawa, R. R. Hardy, D. R. Parks, L. A. Herzenberg, The “Ly-1 B” cell subpopulation

in normal immunodefective, and autoimmune mice. J. Exp. Med. 157, 202–218 (1983).
doi:10.1084/jem.157.1.202 Medline

45. E. Montecino-Rodriguez, K. Dorshkind, B-1 B cell development in the fetus and adult.

Immunity 36, 13–21 (2012). doi:10.1016/j.immuni.2011.11.017 Medline

46. A. B. Kantor, C. E. Merrill, L. A. Herzenberg, J. L. Hillson, An unbiased analysis of V(H)-

D-J(H) sequences from B-1a, B-1b, and conventional B cells. J. Immunol. 158, 1175–
1186 (1997). Medline

47. U. C. Tornberg, D. Holmberg, B-1a, B-1b and B-2 B cells display unique VHDJH repertoires

formed at different stages of ontogeny and under different selection pressures. EMBO J.
14, 1680–1689 (1995). doi:10.1002/j.1460-2075.1995.tb07157.x Medline

48. M. Miyama-Inaba, S. Kuma, K. Inaba, H. Ogata, H. Iwai, R. Yasumizu, S. Muramatsu, R. M.
Steinman, S. Ikehara, Unusual phenotype of B cells in the thymus of normal mice. J. Exp.
Med. 168, 811–816 (1988). doi:10.1084/jem.168.2.811 Medline

49. R. Elmentaite, N. Kumasaka, K. Roberts, A. Fleming, E. Dann, H. W. King, V.

Kleshchevnikov, M. Dabrowska, S. Pritchard, L. Bolt, S. F. Vieira, L. Mamanova, N.
Huang, F. Perrone, I. Goh Kai’En, S. N. Lisgo, M. Katan, S. Leonard, T. R. W. Oliver, C.
E. Hook, K. Nayak, L. S. Campos, C. Domínguez Conde, E. Stephenson, J. Engelbert, R.
A. Botting, K. Polanski, S. van Dongen, M. Patel, M. D. Morgan, J. C. Marioni, O. A.

Bayraktar, K. B. Meyer, X. He, R. A. Barker, H. H. Uhlig, K. T. Mahbubani, K. Saeb-
Parsy, M. Zilbauer, M. R. Clatworthy, M. Haniffa, K. R. James, S. A. Teichmann, Cells
of the human intestinal tract mapped across space and time. Nature 597, 250–255 (2021).
doi:10.1038/s41586-021-03852-1 Medline

50. J. Schulze-Luehrmann, S. Ghosh, Antigen-receptor signaling to nuclear factor kappa B.
Immunity 25, 701–715 (2006). doi:10.1016/j.immuni.2006.10.010 Medline

51. E. S. Alonzo, D. B. Sant’Angelo, Development of PLZF-expressing innate T cells. Curr.
Opin. Immunol. 23, 220–227 (2011). doi:10.1016/j.coi.2010.12.016 Medline

52. T. Dimova, M. Brouwer, F. Gosselin, J. Tassignon, O. Leo, C. Donner, A. Marchant, D.

Vermijlen, Effector Vγ9Vδ2 T cells dominate the human fetal γδ T-cell repertoire. Proc.
Natl. Acad. Sci. U.S.A. 112, E556–E565 (2015). doi:10.1073/pnas.1412058112 Medline

53. L. Tan, A. S. Fichtner, E. Bruni, I. Odak, I. Sandrock, A. Bubke, A. Borchers, C. Schultze-

Florey, C. Koenecke, R. Förster, M. Jarek, C. von Kaisenberg, A. Schulz, X. Chu, B.
Zhang, Y. Li, U. Panzer, C. F. Krebs, S. Ravens, I. Prinz, A fetal wave of human type 3
effector γδ cells with restricted TCR diversity persists into adulthood. Sci. Immunol. 6,
eabf0125 (2021). doi:10.1126/sciimmunol.abf0125 Medline

54. T. Mayassi, L. B. Barreiro, J. Rossjohn, B. Jabri, A multilayered immune system through the

lens of unconventional T cells. Nature 595, 501–510 (2021). doi:10.1038/s41586-021-
03578-0 Medline

55. Z. M. Carico, K. Roy Choudhury, B. Zhang, Y. Zhuang, M. S. Krangel, Tcrd rearrangement

redirects a processive Tcra recombination program to expand the Tcra repertoire. Cell
Rep. 19, 2157–2173 (2017). doi:10.1016/j.celrep.2017.05.045 Medline

56. Y. J. Lee, Y. K. Jeon, B. H. Kang, D. H. Chung, C.-G. Park, H. Y. Shin, K. C. Jung, S. H.

Park, Generation of PLZF+ CD4+ T cells via MHC class II-dependent thymocyte-
thymocyte interaction is a physiological process in humans. J. Exp. Med. 207, 237–246
(2010). doi:10.1084/jem.20091519 Medline

57. H. Cho, Y. Bediako, H. Xu, H.-J. Choi, C.-R. Wang, Positive selecting cell type determines

the phenotype of MHC class Ib-restricted CD8+ T cells. Proc. Natl. Acad. Sci. U.S.A.
108, 13241–13246 (2011). doi:10.1073/pnas.1105118108 Medline

58. H. Georgiev, C. Peng, M. A. Huggins, S. C. Jameson, K. A. Hogquist, Classical MHC
expression by DP thymocytes impairs the selection of non-classical MHC restricted
innate-like T cells. Nat. Commun. 12, 2308 (2021). doi:10.1038/s41467-021-22589-z
Medline

59. E. S. Hoffman, L. Passoni, T. Crompton, T. M. Leu, D. G. Schatz, A. Koff, M. J. Owen, A.
C. Hayday, Productive T-cell receptor beta-chain gene rearrangement: Coincident
regulation of cell cycle and clonality during development in vivo. Genes Dev. 10, 948–
962 (1996). doi:10.1101/gad.10.8.948 Medline

60. H. Spits, Development of alphabeta T cells in the human thymus. Nat. Rev. Immunol. 2, 760–

772 (2002). doi:10.1038/nri913 Medline

61. A. Montel-Hagen, C. S. Seet, S. Li, B. Chick, Y. Zhu, P. Chang, S. Tsai, V. Sun, S. Lopez,

H.-C. Chen, C. He, C. J. Chin, D. Casero, G. M. Crooks, Organoid-induced

differentiation of conventional T cells from human pluripotent stem cells. Cell Stem Cell
24, 376–389.e8 (2019). doi:10.1016/j.stem.2018.12.011 Medline

62. E. Mass, I. Ballesteros, M. Farlik, F. Halbritter, P. Günther, L. Crozet, C. E. Jacome-Galarza,

K. Händler, J. Klughammer, Y. Kobayashi, E. Gomez-Perdiguero, J. L. Schultze, M.
Beyer, C. Bock, F. Geissmann, Specification of tissue-resident macrophages during
organogenesis. Science 353, aaf4238 (2016). doi:10.1126/science.aaf4238 Medline

63. N. Mende, E. Laurenti, Hematopoietic stem and progenitor cells outside the bone marrow:

Where, when, and why. Exp. Hematol. 104, 9–16 (2021).
doi:10.1016/j.exphem.2021.10.002 Medline

64. N. Mende, H. P. Bastos, A. Santoro, K. T. Mahbubani, V. Ciaurro, E. F. Calderbank, M.

Quiroga Londoño, K. Sham, G. Mantica, T. Morishima, E. Mitchell, M. R. Lidonnici, F.
Meier-Abt, D. Hayler, L. Jardine, A. Curd, M. Haniffa, G. Ferrari, H. Takizawa, N. K.
Wilson, B. Gottgens, K. Saeb-Parsy, M. Frontini, E. Laurenti, Unique molecular and
functional features of extramedullary hematopoietic stem and progenitor cell reservoirs in
humans. Blood blood.2021013450 (2022). doi:10.1182/blood.2021013450 Medline

65. S. Krishnan, K. Wemyss, I. E. Prise, F. A. McClure, C. O’Boyle, H. M. Bridgeman, T. N.

Shaw, J. R. Grainger, J. E. Konkel, Hematopoietic stem and progenitor cells are present
in healthy gingiva tissue. J. Exp. Med. 218, e20200737 (2021).
doi:10.1084/jem.20200737 Medline

66. C. H. Kim, Homeostatic and pathogenic extramedullary hematopoiesis. J. Blood Med. 1, 13–

19 (2010). doi:10.2147/JBM.S7224 Medline

67. S. Brioschi, W.-L. Wang, V. Peng, M. Wang, I. Shchukina, Z. J. Greenberg, J. K. Bando, N.
Jaeger, R. S. Czepielewski, A. Swain, D. A. Mogilenko, W. L. Beatty, P. Bayguinov, J.
A. J. Fitzpatrick, L. G. Schuettpelz, C. C. Fronick, I. Smirnov, J. Kipnis, V. S. Shapiro,
G. F. Wu, S. Gilfillan, M. Cella, M. N. Artyomov, S. H. Kleinstein, M. Colonna,
Heterogeneity of meningeal B cells reveals a lymphopoietic niche at the CNS borders.
Science 373, eabf9277 (2021). doi:10.1126/science.abf9277 Medline

68. D. Schafflick, J. Wolbert, M. Heming, C. Thomas, M. Hartlehnert, A.-L. Börsch, A. Ricci, S.

Martín-Salamanca, X. Li, I.-N. Lu, M. Pawlak, J. Minnerup, J.-K. Strecker, T.
Seidenbecher, S. G. Meuth, A. Hidalgo, A. Liesz, H. Wiendl, G. Meyer Zu Horste,
Single-cell profiling of CNS border compartment leukocytes reveals that B cells and their
progenitors reside in non-diseased meninges. Nat. Neurosci. 24, 1225–1234 (2021).
doi:10.1038/s41593-021-00880-y Medline

69. Y. Wang, D. Chen, D. Xu, C. Huang, R. Xing, D. He, H. Xu, Early developing B cells

undergo negative selection by central nervous system-specific antigens in the meninges.
Immunity 54, 2784–2794.e6 (2021). doi:10.1016/j.immuni.2021.09.016 Medline

70. E. Montecino-Rodriguez, H. Leathers, K. Dorshkind, Identification of a B-1 B cell-specified

progenitor. Nat. Immunol. 7, 293–301 (2006). doi:10.1038/ni1301 Medline

71. B. L. Esplin, R. S. Welner, Q. Zhang, L. A. Borghesi, P. W. Kincade, A differentiation

pathway for B1 cells in adult bone marrow. Proc. Natl. Acad. Sci. U.S.A. 106, 5773–5778
(2009). doi:10.1073/pnas.0811632106 Medline

72. M. Yoshimoto, E. Montecino-Rodriguez, M. J. Ferkowicz, P. Porayette, W. C. Shelley, S. J.

Conway, K. Dorshkind, M. C. Yoder, Embryonic day 9 yolk sac and intra-embryonic
hemogenic endothelium independently generate a B-1 and marginal zone progenitor
lacking B-2 potential. Proc. Natl. Acad. Sci. U.S.A. 108, 1468–1473 (2011).
doi:10.1073/pnas.1015841108 Medline

73. T. Kreslavsky, J. B. Wong, M. Fischer, J. A. Skok, M. Busslinger, Control of B-1a cell
development by instructive BCR signaling. Curr. Opin. Immunol. 51, 24–31 (2018).
doi:10.1016/j.coi.2018.01.001 Medline

74. R. Graf, J. Seagal, K. L. Otipoby, K.-P. Lam, S. Ayoub, B. Zhang, S. Sander, V. T. Chu, K.

Rajewsky, BCR-dependent lineage plasticity in mature B cells. Science 363, 748–753
(2019). doi:10.1126/science.aau8475 Medline

75. E. P. Mimitou, A. Cheng, A. Montalbano, S. Hao, M. Stoeckius, M. Legut, T. Roush, A.
Herrera, E. Papalexi, Z. Ouyang, R. Satija, N. E. Sanjana, S. B. Koralov, P. Smibert,
Multiplexed detection of proteins, transcriptomes, clonotypes and CRISPR perturbations
in single cells. Nat. Methods 16, 409–412 (2019). doi:10.1038/s41592-019-0392-0
Medline

76. S. J. Fleming, J. C. Marioni, M. Babadi, CellBender remove-background: a deep generative
model for unsupervised removal of background noise from scRNA-seq datasets, bioRxiv
791699 [Preprint] (2019); https://doi.org/10.1101/791699.

77. S. L. Wolock, R. Lopez, A. M. Klein, Scrublet: Computational identification of cell doublets

in single-cell transcriptomic data. Cell Syst. 8, 281–291.e9 (2019).
doi:10.1016/j.cels.2018.11.005 Medline

78. H. Heaton, A. M. Talman, A. Knights, M. Imaz, D. J. Gaffney, R. Durbin, M. Hemberg, M.

K. N. Lawniczak, Souporcell: Robust clustering of single-cell RNA-seq data by genotype
without reference genotypes. Nat. Methods 17, 615–620 (2020). doi:10.1038/s41592-
020-0820-1 Medline

79. F. A. Wolf, P. Angerer, F. J. Theis, SCANPY: Large-scale single-cell gene expression data
analysis. Genome Biol. 19, 15 (2018). doi:10.1186/s13059-017-1382-0 Medline

80. A. Gayoso, R. Lopez, G. Xing, P. Boyeau, V. Valiollah Pour Amiri, J. Hong, K. Wu, M.

Jayasuriya, E. Mehlman, M. Langevin, Y. Liu, J. Samaran, G. Misrachi, A. Nazaret, O.
Clivio, C. Xu, T. Ashuach, M. Gabitto, M. Lotfollahi, V. Svensson, E. da Veiga
Beltrame, V. Kleshchevnikov, C. Talavera-López, L. Pachter, F. J. Theis, A. Streets, M.
I. Jordan, J. Regier, N. Yosef, A Python library for probabilistic analysis of single-cell
omics data. Nat. Biotechnol. 40, 163–166 (2022). doi:10.1038/s41587-021-01206-w
Medline

81. F. Pedregosa et al., Scikit-learn: Machine learning in python. j. mach. learn. res. 12, 2825–

2830 (2011).

82. V. A. Traag, L. Waltman, N. J. van Eck, From Louvain to Leiden: Guaranteeing well-

connected communities. Sci. Rep. 9, 5233 (2019). doi:10.1038/s41598-019-41695-z
Medline

83. K. Polański, M. D. Young, Z. Miao, K. B. Meyer, S. A. Teichmann, J. E. Park, BBKNN:

Fast batch alignment of single cell transcriptomes. Bioinformatics 36, 964–965 (2020).
Medline

84. E. Y. Chen, C. M. Tan, Y. Kou, Q. Duan, Z. Wang, G. V. Meirelles, N. R. Clark, A.

Ma’ayan, Enrichr: Interactive and collaborative HTML5 gene list enrichment analysis
tool. BMC Bioinformatics 14, 128 (2013). doi:10.1186/1471-2105-14-128 Medline

85. C. Ahlmann-Eltze, W. Huber, glmGamPoi: Fitting Gamma-Poisson generalized linear

models on single cell count data. Bioinformatics 36, 5701–5702 (2021).
doi:10.1093/bioinformatics/btaa1009 Medline

86. J. W. Squair, M. Gautier, C. Kathe, M. A. Anderson, N. D. James, T. H. Hutson, R. Hudelle,
T. Qaiser, K. J. E. Matson, Q. Barraud, A. J. Levine, G. La Manno, M. A. Skinnider, G.
Courtine, Confronting false discoveries in single-cell differential expression. Nat.
Commun. 12, 5692 (2021). doi:10.1038/s41467-021-25960-2 Medline

87. M. D. Robinson, D. J. McCarthy, G. K. Smyth, edgeR: A Bioconductor package for

differential expression analysis of digital gene expression data. Bioinformatics 26, 139–
140 (2010). doi:10.1093/bioinformatics/btp616 Medline

88. G. Sturm, T. Szabo, G. Fotakis, M. Haider, D. Rieder, Z. Trajanoski, F. Finotello, Scirpy: A

Scanpy extension for analyzing single-cell T-cell receptor-sequencing data.
Bioinformatics 36, 4817–4818 (2020). doi:10.1093/bioinformatics/btaa611 Medline

89. E. Stephenson, G. Reynolds, R. A. Botting, F. J. Calero-Nieto, M. D. Morgan, Z. K. Tuong,

K. Bach, W. Sungnak, K. B. Worlock, M. Yoshida, N. Kumasaka, K. Kania, J. Engelbert,
B. Olabi, J. S. Spegarova, N. K. Wilson, N. Mende, L. Jardine, L. C. S. Gardner, I. Goh,
D. Horsfall, J. McGrath, S. Webb, M. W. Mather, R. G. H. Lindeboom, E. Dann, N.
Huang, K. Polanski, E. Prigmore, F. Gothe, J. Scott, R. P. Payne, K. F. Baker, A. T.
Hanrath, I. C. D. Schim van der Loeff, A. S. Barr, A. Sanchez-Gonzalez, L. Bergamaschi,
F. Mescia, J. L. Barnes, E. Kilich, A. de Wilton, A. Saigal, A. Saleh, S. M. Janes, C. M.
Smith, N. Gopee, C. Wilson, P. Coupland, J. M. Coxhead, V. Y. Kiselev, S. van Dongen,
J. Bacardit, H. W. King, A. J. Rostron, A. J. Simpson, S. Hambleton, E. Laurenti, P. A.
Lyons, K. B. Meyer, M. Z. Nikolić, C. J. A. Duncan, K. G. C. Smith, S. A. Teichmann,
M. R. Clatworthy, J. C. Marioni, B. Göttgens, M. Haniffa; Cambridge Institute of
Therapeutic Immunology and Infectious Disease-National Institute of Health Research
(CITIID-NIHR) COVID-19 BioResource Collaboration, Single-cell multi-omics analysis
of the immune response in COVID-19. Nat. Med. 27, 904–916 (2021).
doi:10.1038/s41591-021-01329-2 Medline

90. N. T. Gupta, J. A. Vander Heiden, M. Uduman, D. Gadala-Maria, G. Yaari, S. H. Kleinstein,
Change-O: A toolkit for analyzing large-scale B cell immunoglobulin repertoire
sequencing data. Bioinformatics 31, 3356–3358 (2015).
doi:10.1093/bioinformatics/btv359 Medline

91. C. H. Holland, J. Tanevski, J. Perales-Patón, J. Gleixner, M. P. Kumar, E. Mereu, B. A.

Joughin, O. Stegle, D. A. Lauffenburger, H. Heyn, B. Szalai, J. Saez-Rodriguez,
Robustness and applicability of transcription factor and pathway analysis tools on single-
cell RNA-seq data. Genome Biol. 21, 36 (2020). doi:10.1186/s13059-020-1949-z
Medline

92. M. Efremova, M. Vento-Tormo, S. A. Teichmann, R. Vento-Tormo, CellPhoneDB: Inferring
cell-cell communication from combined expression of multi-subunit ligand-receptor
complexes. Nat. Protoc. 15, 1484–1506 (2020). doi:10.1038/s41596-020-0292-x Medline

93. L. Garcia-Alonso, L.-F. Handfield, K. Roberts, K. Nikolakopoulou, R. C. Fernando, L.

Gardner, B. Woodhams, A. Arutyunyan, K. Polanski, R. Hoo, C. Sancho-Serra, T. Li, K.
Kwakwa, E. Tuck, V. Lorenzi, H. Massalha, M. Prete, V. Kleshchevnikov, A.
Tarkowska, T. Porter, C. I. Mazzeo, S. van Dongen, M. Dabrowska, V. Vaskivskyi, K. T.
Mahbubani, J. E. Park, M. Jimenez-Linan, L. Campos, V. Y. Kiselev, C. Lindskog, P.
Ayuk, E. Prigmore, M. R. Stratton, K. Saeb-Parsy, A. Moffett, L. Moore, O. A.
Bayraktar, S. A. Teichmann, M. Y. Turco, R. Vento-Tormo, Mapping the temporal and
spatial dynamics of the human endometrium in vivo and in vitro. Nat. Genet. 53, 1698–
1711 (2021). doi:10.1038/s41588-021-00972-2 Medline

94. M. Setty, V. Kiseliovas, J. Levine, A. Gayoso, L. Mazutis, D. Pe’er, Characterization of cell
fate probabilities in single-cell data with Palantir. Nat. Biotechnol. 37, 451–460 (2019).
doi:10.1038/s41587-019-0068-4 Medline

95. M. Lange, V. Bergen, M. Klein, M. Setty, B. Reuter, M. Bakhti, H. Lickert, M. Ansari, J.
Schniering, H. B. Schiller, D. Pe’er, F. J. Theis, CellRank for directed single-cell fate
mapping. Nat. Methods 19, 159–170 (2022). Medline

96. J.-E. Park, S. Teichmann, M. Haniffa, T. Taghon, Collection of codes and annotated matrix
for the paper “A cell atlas of human thymic development defines T cell repertoire
formation” (2021), doi:10.5281/zenodo.5500511.

97. G. Palla, H. Spitzer, M. Klein, D. Fischer, A. C. Schaar, L. B. Kuemmerle, S. Rybakov, I. L.
Ibarra, O. Holmberg, I. Virshup, M. Lotfollahi, S. Richter, F. J. Theis, Squidpy: A
scalable framework for spatial omics analysis. Nat. Methods 19, 171–178 (2022).
doi:10.1038/s41592-021-01358-2 Medline

98. I. Virshup, S. Rybakov, F. J. Theis, P. Angerer, F. A. Wolf, anndata: Annotated data, bioRxiv

473007 [Preprint] (2021); https://doi.org/10.1101/2021.12.16.473007.

99. E. Dann, C. Suo, I. Goh, V. Kleshchevnikov, Teichlab/Pan_fetal_immune: Analysis code for
publication: Mapping the developing human immune system across organs, Zenodo
(2022); https://zenodo.org/record/6481461#.YnLK6drMKUk.

100. S. A. Dick, A. Wong, H. Hamidzada, S. Nejat, R. Nechanitzky, S. Vohra, B. Mueller, R.

Zaman, C. Kantores, L. Aronoff, A. Momen, D. Nechanitzky, W. Y. Li, P.
Ramachandran, S. Q. Crome, B. Becher, M. I. Cybulsky, F. Billia, S. Keshavjee, S.
Mital, C. S. Robbins, T. W. Mak, S. Epelman, Three tissue resident macrophage subsets
coexist across organs with conserved origins and life cycles. Sci. Immunol. 7, eabf7777
(2022). doi:10.1126/sciimmunol.abf7777 Medline

101. D. Gadala-Maria, G. Yaari, M. Uduman, S. H. Kleinstein, Automated analysis of high-

throughput B-cell sequencing data reveals a high frequency of novel immunoglobulin V
gene segment alleles. Proc. Natl. Acad. Sci. U.S.A. 112, E862–E870 (2015).
doi:10.1073/pnas.1417683112 Medline

102. T. Egawa, K. Kawabata, H. Kawamoto, K. Amada, R. Okamoto, N. Fujii, T. Kishimoto, Y.

Katsura, T. Nagasawa, The earliest stages of B cell development require a chemokine
stromal cell-derived factor/pre-B cell growth-stimulating factor. Immunity 15, 323–334
(2001). doi:10.1016/S1074-7613(01)00185-6 Medline

103. T. Nagasawa, S. Hirota, K. Tachibana, N. Takakura, S. Nishikawa, Y. Kitamura, N.

Yoshida, H. Kikutani, T. Kishimoto, Defects of B-cell lymphopoiesis and bone-marrow
myelopoiesis in mice lacking the CXC chemokine PBSF/SDF-1. Nature 382, 635–638
(1996). doi:10.1038/382635a0 Medline

