nature medicine
Article https://doi.org/10.1038/s41591-024-03215-z
A multi-modal single-cell and spatial
expression map of metastatic breast cancer
biopsies across clinicopathological features
Received: 13 November 2023 A list of authors and their affiliations appears at the end of the paper
Accepted: 25 July 2024
Published online: 30 October 2024 Although metastatic disease is the leading cause of cancer-related deaths,
its tumor microenvironment remains poorly characterized due to technical
Check for updates
and biospecimen limitations. In this study, we assembled a multi-modal
spatial and cellular map of 67 tumor biopsies from 60 patients with
metastatic breast cancer across diverse clinicopathological features and nine
anatomic sites with detailed clinical annotations. We combined single-cell
or single-nucleus RNA sequencing for all biopsies with a panel of four spatial
expression assays (Slide-seq, MERFISH, ExSeq and CODEX) and H&E staining
of consecutive serial sections from up to 15 of these biopsies. We leveraged
the coupled measurements to provide reference points for the utility and
integration of different experimental techniques and used them to assess
variability in cell type composition and expression as well as emerging spatial
expression characteristics across clinicopathological and methodological
diversity. Finally, we assessed spatial expression and co-localization features
of macrophage populations, characterized three distinct spatial phenotypes
of epithelial-to-mesenchymal transition and identified expression programs
associated with local T cell infiltration versus exclusion, showcasing the
potential of clinically relevant discovery in such maps.
Although malignant cells are the defining feature of cancers, tumors limitations, including availability, size and diversity. Moreover, the
comprise malignant and non-malignant cells interacting in complex panoply of available methods with distinct design parameters poses
ecosystems that shape disease progression1. Understanding these challenges for users in choosing methods4,5. As part of the Human
interactions has potential for clinical translation. For example, Tumor Atlas Network (HTAN)6, we used single-cell and single-nucleus
although tumor-infiltrating lymphocytes (TILs) are generally associ- RNA sequencing (sc/snRNA-seq) and four distinct spatial expression
ated with favorable prognosis, there is substantial heterogeneity2. methods (CODEX7,8, targeted ExSeq9, MERFISH10–12 and Slide-seq13) to
In primary breast cancer (BC), TILs are predictive of response to profile tumor biopsies from a cohort of patients with metastatic breast
neoadjuvant chemotherapy and improved survival in triple-negative cancer (MBC), the leading cause of cancer-related death among women
breast cancer (TNBC) and human epidermal growth factor receptor worldwide14, toward informing practical application of these methods
2-positive (HER2+) BC, but their impact in hormone receptor-positive and refining understanding of MBC.
(HR+) BC remains unclear and may depend on distinct states of malig-
nant cells or TILs3. Results
Recent advances in single-cell and spatial profiling enable inter- Single-cell and spatial expression profiling of clinical variables
rogation of tissue ecosystems at unprecedented resolution. However, To compare profiling methods and characterize cellular expression
few studies have focused on metastatic disease, likely due to sample profiles of MBC biopsies, we created a comprehensive dataset covering
e-mail: klughammer@genzentrum.lmu.de; daniel_abravanel@dfci.harvard.edu; regev.aviv@gene.com; wagle.nikhil@gene.com
Nature Medicine | Volume 30 | November 2024 | 3236–3249 3236

Article https://doi.org/10.1038/s41591-024-03215-z
relevant clinical variables and diverse profiling methods (Fig. 1a), along entire tissue section, CODEX yielded more observations per section
with an analysis framework to integrate the resulting data, by harmo- than the segmented version of MERFISH but fewer than the binned
nizing features, data formats, positional resolution, coordinates and version (Fig. 1c and Extended Data Fig. 2b). ExSeq, which captured
spatial registration (Fig. 1b and Methods), and we analyzed key fea- only a small field of view (FOV) (<1 mm2), yielded the lowest number of
tures, including cell composition, gene expression programs, immune observations per section in its segmented version, and this only slightly
phenotypes and co-localization (Fig. 1b). We profiled 67 biopsies from increased with binning (Fig. 1c and Extended Data Fig. 2b). Pseudobulk
60 patients with MBC (30: scRNA-seq, 37: snRNA-seq) across receptor sample-wise expression profiles were correlated between all methods
subtypes (44: HR+/HER2−, 3: HR+/HER2+, 3: HR−/HER2+, 16: HR−/HER2−) except ExSeq (Spearman ρ = 0.41 (CODEX versus scRNA-seq) to 0.75
and frequent sites of disease (37: liver, 9: axilla, 7: breast, 5: bone, 3: (Slide-seq versus scRNA-seq), ρ = −0.1 to 0.086 (ExSeq)) (Fig. 1d). As
chest wall, 3: neck, 1: brain, 1: lung, 1: skin; breast biopsies were collected expected, segmented and binned versions of MERFISH and ExSeq
from the primary site after MBC diagnosis) (Fig. 1a,c and Extended Data showed near-perfect correlations of 0.97 and 1, respectively (Fig. 1d).
Fig. 1a). For 15 biopsies, we collected matching spatial data from serial
sections of a second biopsy core from the same lesion/procedure, using Clinical features are associated with cell type composition
up to four spatial methods and hematoxylin and eosin (H&E) staining We annotated cell types in sc/snRNA-seq using a semi-automated
(Fig. 1c, Extended Data Fig. 1a,b and Supplementary Tables 1 and 2). approach (Methods and Fig. 2a), combined with examination of the
The spatial techniques represent a range of design parameters top five marker genes for each cell type (Extended Data Fig. 3a,b).
(Extended Data Fig. 1b). Slide-seq profiles the whole transcriptome Although most cell types were identified in snRNA-seq and scRNA-seq,
with near-cellular capture resolution using 10-μm beads (located inde- some were detected only in snRNA-seq (adipocytes, neurons, some
pendently of sample structure). CODEX, MERFISH and ExSeq target endothelial subsets, stellate cells and smooth and skeletal muscle cells)
selected panels of proteins (CODEX) or RNAs (MERFISH and ExSeq) or scRNA-seq (neutrophils, mast cells, erythrocytes and keratinocytes)
using imaging at single-cell, subcellular or super-resolution, respec- (Fig. 2a and Extended Data Fig. 3a,c), largely consistent with previous
tively. Although ExSeq can be targeted or untargeted and MERFISH can reports15,16. Several cell subtype signatures from scRNA-seq of primary
potentially target up to thousands of RNAs, we designed a dedicated BC17 scored highly in the expected cell types (Extended Data Fig. 3d).
panel of 297 genes for MERFISH and ExSeq based on sc/snRNA-seq data As expected, most of the scRNA-seq-derived signatures scored higher
and prior knowledge (Supplementary Table 3 and Methods). in scRNA-seq than in snRNA-seq.
We selected biopsies for tumor content and tissue quality and to Although most malignant cells displayed epithelial-like expression
cover a range of combinations of site and receptor status. We obtained profiles, in a few samples we observed chondroid (sample 586-8599),
high-quality Slide-seq and CODEX data from 15 of 15 and 13 of 13 biop- stem-like (sample 917-4531) or neuronal (samples 944-7479 and
sies, respectively, and MERFISH and ExSeq data from nine of 14 each 890-7299) expression profiles (Extended Data Fig. 3a–c). Interest-
(Fig. 1c and Extended Data Fig. 1b). The expert laboratories set sam- ingly, these were associated with unique clinicopathologic character-
ple quality control (QC) criteria individually (Methods). The com- istics. The sample with stem-like expression profiles came from the
paratively low success rate of MERFISH is explained by its stringent patient with the cohort’s shortest overall survival from initial diagnosis
inclusion criterion (Pearson’s r > 0.6 between MERFISH and matched (<2 years), despite presenting with stage I disease and receiving appro-
sc/snRNA-seq pseudobulk profiles); for ExSeq, it was attributed to priate treatment. The sample with a chondroid expression profile was
technical challenges (including tissue preservation, RNA quality and the only biopsy with metaplastic histology, and the clinical pathology
autofluorescence). independently described chondroid differentiation. Metaplastic BC
We analyzed single-molecule-resolution MERFISH and ExSeq is a rare and heterogenous subtype associated with poor prognosis
data in two ways: aggregating signal per cell after cell segmentation or overall18 and poor response to cytotoxic chemotherapy19,20 but in which
aggregating signal in 10 × 10-μm spatial bins. We analyzed Slide-seq by preliminary data suggest the possibility of responsiveness to immu-
its native 10-μm beads and CODEX at the level of segmented cells notherapy with frequent PD-L1 expression21 and a subset of patients
(Fig. 1b,c). Analyzing single-molecule data by 10 × 10-μm bins gener- with exceptional responses to combined checkpoint blockade on a
ated coarser data in silico but avoided segmentation biases and allowed phase 2 trial22. Although anecdotal, these vignettes demonstrate that
comparison to Slide-seq data while maintaining other method-specific expression features recovered by sc/snRNA-seq can be consistent with
properties (for example, detection sensitivity). rare clinicopathologic features and may warrant further investigation.
As expected, the methods varied in the captured number of Biopsy composition by four major compartments (malignant,
observations (cells/nuclei/beads/bins) and molecular features (genes/ stromal, myeloid and lymphoid) varied across samples but, overall,
proteins) per observation (Fig. 1c, Extended Data Fig. 2a,b and Sup- scRNA-seq captured a higher fraction of immune cells, and snRNA-seq
plementary Tables 1 and 2). There was a higher number of observa- had greater representation of malignant and stromal cells (Fig. 2b),
tions and features per observation using snRNA-seq than scRNA-seq, which are prone to death during dissociation15. To investigate sources
whereas Slide-seq had a similar number of observations but many of composition differences, we analyzed the biopsies from seven
fewer features per observation. By definition, the number of features patients with two biopsies each. In one, two cores from the same pro-
detected by approaches with predefined panels (MERFISH, ExSeq cedure were profiled with snRNA-seq and scRNA-seq. These showed
and CODEX) was lower per observation (Fig. 1c and Extended Data the expected bias toward enriched immune cells in scRNA-seq and
Fig. 2b). Between CODEX and MERFISH, which both captured the malignant and stromal cells in snRNA-seq (Fig. 2c). In three patients,
Fig. 1 | Profiling of MBC biopsies using scRNA-seq, snRNA-seq and four produced scRNA-seq, snRNA-seq and spatial expression data as well as exemplary
spatial expression methods. a, Schematic illustrating sample acquisition and H&E images for the core biopsies used in spatial profiling. Biopsy site and
data generation. Core biopsies dedicated to research were embedded in OCT receptor status for each of the profiled cores is indicated as well as the number of
or subjected to scRNA-seq. Per biopsy, one fresh or frozen core was used for profiled observations (cells, beads or bins) and the number of detected features
scRNA-seq or snRNA-seq, respectively. For matching spatial profiling, a second, (RNA species or proteins). The number of replicates for each spatial expression
OCT-embedded core from the same biopsy procedure was cut in two sets of method and biopsy is indicated in the respective blobs. HR, hormone receptor
five 10-μm serial sections for processing with four spatial expression methods (ESR1 and PGR). Biopsies from the same patient are indicated with bold font
(Slide-seq, CODEX, MERFISH and ExSeq) and H&E staining. b, Schematic and connected through lines. d, Clustered heatmap depicting the pair-wise
illustrating the properties of the different produced data types, the data Spearman correlation of methods based on sample-wise pseudobulk expression.
processing framework and the performed analysis. c, Overview statistics of the
Nature Medicine | Volume 30 | November 2024 | 3236–3249 3237

Article https://doi.org/10.1038/s41591-024-03215-z
the paired biopsies were obtained from the same lesion at different frequencies (two decrease, one increase). In contrast, in each of the
timepoints (70–220 days apart), and each pair showed relatively simi- three patients in whom the paired biopsies were from different lesions
lar compositions overall but with changes in T cell and macrophage or sites, we observed more substantial differences, largely driven by
Harmonize across methods
- Features: official gene alias
- Format: Expression matrix
(observations × features)
- Scale: 1 µm/pixel - Coordinates: Origin at (0|0)
100 µm
ExSeq (bin)
ExSeq
MERFISH (bin)
MERFISH
Slide-seq
CODEX
snRNA-seq
scRNA-seq
Receptor status
Biopsy site
M
R
e
e
a
c
n
e H H H
H
f
p R R R
R
e
t + + −
−
a
/
/ / / o
H
H H H
t
r
u
E
E E E s
r
R
R R R
e
t
2
2 2 2 a
s
+ − +
−
t
p
us
er cell
B
N
io
u
p
m
sy
b
s
e
i
r
t e
of observations 1 –0.1 –
–
0
0
.
.
0
0
9
2 –
–
6
4
0
0
.
.
0
0
2
2
–
–
4
1
0
0
0
.
.
.
0
0
5
1
3
5
–
–
8
4
0
0
0
.
.
.
0
0
5
5
4
8
– 0
7
6 0
0
0
. . 0
.
.
0
9
5
8 4
1
7
6 0 1
0
0
. E 0
.4 x
.7 2 S
2
7 e
0
0
0
q E
.
.
.
x
7
5
6
S
4
2
5
e
0
0
q C
.
.
(
6
6
O b
9
9
i D n
0
0
E ) M X
.
.
7
6
E
5
R
5
F
0
I
M
S
.7 H
E
3
RFI
N
S
S
l
H
A
id
(
e
b
-
i
s
s
n
e
c
)
q RNA
s
-
n
s
R
e
N
q A-seq
S c w g o p e is r n e e r e a e r p l e m a s x t e a i p o u n r n d e o s o s b f i u o s l a n k mple-
1 1 1 1 1 1 1 1
E1xSeq ExSeq
(bin)
CO DEX M ERFISH M ERFISH
(b
S
in
li
)
de-seq scRNA-seq snRNA-seq
Nature Medicine | Volume 30 | November 2024 | 3236–3249 3238
1693−547 178−903 1441−283 1861−414 1852−265 1804−387 0086−608 206−262 157−582 1201−123 2801−033 1471−324 2603−116 2423−726 2063−266 9538−957 1534−158 1834−358 9267−289 2243−946 1483−537 1231−463 9567−389 239−313 9328−218 2144−809 1771−524 1354−719 9958−685 9477−889 9996−538 9417−878 9327−788 8207−168 6576−522 9876−608 9507−268 0607−268 8576−132 9576−232 016−262 0682−985 1504−257 9786−418 9807−078 9717−088 9627−988 0727−988 9927−098 9537−598 9747−449 9057−749 9877−799 1582−985 5576−322 9117−378 0676−415 2676−915 0527−788 2576−312 1676−615 5676−525 1576−112 7357−322 7576−622 1474−369 3676−125
a b
Metastatic breast cancer scRNA-seq snRNA-seq Clinical annotation
sites of disease Data generation from biopsies
Observations:
cells|beads|bins Variance of cell type
2 Features: composition & expression
genes|proteins
1 Breast Malignant expression
3 2 3 B N r e a c in k 1 2 U 0 0 M k µ I m g c e o b n u e e n a s t d rep s A p re n a s t a i e l a y n l z t d e a a t d i t o a ns p I r m og m ra u m ne s
4 4 Chest wall phenotypes
5 6 1 6 5 A Lu xi n ll g a Biopsy 1 Biopsy 2 S 50 in g p l r e o t c e e in ll s Composition
7 8 7 Liver Intensity Co-localization
10-µm Expression
8 Skin
serial Single molecule
9 Bone
Single Single sections 300 genes
Molecule count
nuclei cell Spatial
(frozen) (fresh) (frozen) Primary SegmentedBinned (10 µm)
9 Available data representations
67 sc/snRNA-seq
samples HE staining QC Clustering Analysis
53 × 1 per patient Slide-seq
7 × 2 per patient CODEX Cross-method
15 matched M Ex E S R e F q ISH de novo comparison
spatial samples
Sample ID 10x sc/sn Spatio-molecular Registration Annotation
RNA-seq profiling
XXX-YYYY
Transfer 60 Patient ID
patients Reference
sc/snRNA-seq
c
100 µm
100 µm 100 µm 100 µm
100 µm 100 µm 100 µm 100 µm 100 µm 100 µm 100 µm 100 µm 100 µm 100 µm
1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1
1 2 1 1 1 1 1 3 1
1 2 1 1 1 1 1 3 1
2 1 2 1 2 2 2 1 2 2 1 1 2 2 2
1 1 1 1 1 1 1 1 1 1 1 1 1
d 1 Axilla Breast Lung Bone Chest wall Neck Brain Liver Skin 0
423 10,000
28 500 2,000
1,000 40,000
60 1,000 3,760 5,000 82,260

Article https://doi.org/10.1038/s41591-024-03215-z
UMAP1
n = 54 n = 66 n = 65 n = 153
Nature Medicine | Volume 30 | November 2024 | 3236–3249 3239
2PAMU
a b
UMAP1
d
2PAMU
c Same lesion & same method
snRNA seq 862 889
snRNA seq 1
Cell types
MBC 0.75 0.75 MBC_stem like
MBC_neuronal
MBC_chondroid 0.50 0.50 Endothelial
Endothelial_sinusoidal
Endothelial_angiogenic
Endothelial_vascular 0.25 0.25
Fibroblast
Chondrocyte
Smooth muscle_vascular 0 0
S S A H t k d e e e i p l p l l a e a o t t t c o a e y l c t m y e t s u e scle 211–6 21 7 3 5 – 2 1 6 2 7 3 5 – 2 2 6 2 7 3 5 – 5 7 2 5 2 3 5– 7 6 2 7 2 5 6 6 –6 2 7 3 5 1– 7 2 6 3 75 2– 8 6 2 7 6 5 2 9 – 5 6 14 10 –6 5 7 1 6 6 0 – 5 6 1 7 9 6 – 1 6 5 7 2 6 1– 2 6 52 7 5 6 – 3 5 6 8 7 9 6 5 – 5 2 8 8 9 5 – 1 2 7 8 5 6 2 0 8 – 0 40 6 5 – 1 6 8 7 1 8 4 9 – 8 6 3 8 5 7 – 9 6 8 9 6 9 1– 8 9 7 6 0 2 2 – 8 8 7 6 0 2 5 – 9 7 8 0 7 6 0 0 –7 8 0 7 8 3 9 – 8 7 7 1 8 19 – 8 7 8 14 0 9 8 –7 8 1 7 7 – 9 8 7 8 2 7 3 – 9 8 7 8 2 9 5 – 0 8 7 8 2 9 6 – 9 8 72 9 7 0 0 – 8 7 9 29 5– 9 9 73 4 5 4 9 – 9 7 4 4 7 7 – 9 7 9 5 6 0 3 9 – 9 4 9 7 7 4 – 1 7789 7059 7060 7269 7270
Keratinocyte
Neuron
Macrophage Different lesions | different methods
scRNA seq Monocyte scRNA seq 223 806 262
Neutrophil 1 1
Erythrocyte
Mast
B_plasma
0.75 0.75 B
T
NK
0.50 0.50
Compartments
Malignant 0.25 0.25
Stromal
Lymphoid 0 0
Myeloid 262–60 2 2 85–7 3 5 0 1 9–8 3 7 1 1 3–9 3 3 2 2 1–1 3 0 3 2 0 1 –10 3 8 6 2 4–1 3 3 8 21 2–14 4 4 14 1 –16 4 8 2 1 3–17 4 4 2 1 5–1 5 7 6 7 2 1 –2 5 5 8 8 6 1 –85 6 9 11 9 –30 62 6 7 2 –3 6 2 4 4 9 2 –3 6 4 6 2 2 2 –36 7 0 35 2 –3 7 8 4 4 5 1 –3 7 9 5 6 9 1 –83 78 5 3 9 – 8 4 0 0 6 8 – 1 68 8 0 1 0 2–82 8 3 5 9 1–4 8 3 5 5 3 1 –4 9 3 0 8 8 1 –44 9 1 1 2 7–4 9 5 8 3 2 1 –7 9 6 8 2 3 9 –7 9 6 8 5 8 9 –7749 6755 7537 6789 6800 610 602
sllec
fo noitcarF
sllec
fo
noitcarF
887
1
7239 7250 Breast Axilla Liver 220 days 200 days 70 days
sn sn sn
589
2851 2860 Liver Brain liver Breast Liver 300 days 75 days 470 days 0 days
sn sn sn/sc sn/sc
sllec
fo noitcarF
sllec
fo
noitcarF
e f
setycopidA
B
amsalp_B etycordnohC lailehtodnE cinegoigna_lailehtodnE ladiosunis_lailehtodnE ralucsav_lailehtodnE etycorhtyrE tsalborbiF etycotapeH etyconitareK CBM diordnohc_CBM lanoruen_CBM ekil−mets_CBM egahporcaM tsaM etyconoM
KN
norueN lihportueN elcsum latelekS ralucsav_elcsum htoomS etalletS
T
100 80 60 40 20
0
)%( denialpxe ecnairaV 100 75 50 25
0
erocs .qerf epyt lleC )%( denialpxe ecnairav Patient ID Residuals 8 Method sc/sn Biopsy 6 0.56 0.56 0.56 0.56 0.14 0.95 0.007 0.95 0.007 site Mo t s x t c r l e a c s e s nt 4 MΦ 2 Histology 0
Metastatic Distant Endo OtherChemo Immuno HR+ HR+ HR– HR– presentation adjuvant crine therapy therapy HER2+ HER2– HER2+ HER2–
eghaporcaM erocs .qerf Most recent tx class Receptor status FDR against all other groups: FDR against all other groups: Receptor
status
E E P T K K R K C R E R R P B R S P T T A G B T R S 1 1 H M R 9 8 8 2 R 1 1 +/ HER H 2 R + +/ HER H 2 R − −/ HER H 2 R + −/ HE H R2 R − +/ HER H 2 R + +/ HER H 2 R − −/ HER H 2 R + −/ HER2− M e F e x r x e p a p a c r 1 r n e t 0 0 0 e i s . . . n o s 2 5 7 s s o n 2 5 5 0 i i o r n o m n g f 3 a c l e iz 4 l e ls d B H L L s s n c u u a e R R m m s r a 2 N N A B l A A s s e e q q A B B H H H H o r x R R R R a i n + + – – l i / / l / / n e a H H H H E E E E R R R R 2 2 2 2 – + + – B C Li r h v e e e a r s s t t wall L N S u k e n i c n g k Pat M ie e n S t t h it R o e e d P c A ep M 22 t 5 o 3 2 0 r 2 − s 6 3 9 − 7 4 7 5 5 7 5 2 5 − 3 8 1 7 − 5 7 7 6 7 8 0 7 3 − 9 6 2 5 7 3 1 6 − 4 3 2 2 9 6 8 −6 8 2 4 − 5 1 1 0 6 2 3 3 0 − 5 1 4 2 − 8 3 6 3 9 8 7 2 − 1 5 8 1 2 − 8 0 8 1 2 5 6 0 2 1 − 2 5 8 6 1 − 6 7 6 7 1 8 − 8 7 9 7 5 6 3 0 6 − 4 2 8 4 9 8 1 0 − 4 6 3 8 − 2 4 1 6 8 7 2 8 − 9 2 3 7 9 5 9 2 8 − 6 4 7 2 3 1 2 − 1 7 7 5 − 4 6 9 3 9 5 2 0 − 4 9 6 8 3 4 2 9 9 − 8 6 0 7 8 4 1 − 8 9 7 7 8 9 2 − 4 0 7 9 2 2 9 − 8 3 7 7 0 5 − 17 7 1 1 7 − 9 5 4 4 2 2 1 3 − 8 4 5 6 5 1 0 6 − 7 7 5 2 5 5 − 1 9 8 1 3 6 − 6 8 8 2 0 6 3 − 2 9 7 5 2 0 9 − 9 9 7 7 5 0 8 − 9 0 9 7 3 6 0 0 7 6 − 0 8 5 7 3 . . . 9 1 6 − 5 6 2 2 7 4 5 − 1 9 7 0 0 3 6 5 5 5 4 − 7 1 1 6 4 6 8 7 − 1 8 5 6 8 7 2 7 8 − 6 4 7 7 0 2 B − 2 3 9 7 5 2 9 0 − a 5 9 1 8 7 0 1 s − 7 7 2 4 1 − 1 a 4 1 4 5 − 1 5 1 6 l 2 P 9 3 8 7 − 1 3 5 6 = 2 5 1 H 7 2 − 6 6 8 3 6 2 − 1 e 9 2 6 5 9 × − 2 7 r 9 8 3 5 5 1 2 2 1 − 7 P 3 3 0 6 9 − 7 9 – = 6 L 3 1 5 8 2 6 u m × 1 P 0 A = – 1 L 2 5 u × m 10 B –22
223−6 22 75 3 5 −7 9 5 4 3 7 7 − 5 75 2 0 1− 9 6 8 7 7 6 8 3 −7 7 1 3 4 5 9 −3 2 8 6 4 2 1 −6 26 10 2− 8 6 5 0 3 2 − 2 4 3 3 1 8 − 1 6 5 7 8 5 9 8 − 3 2 2 8 1 5 − 1 1 8 0 0 2 6 1 − 2 6 2 7 5 8 − 9 6 8 7 6 5 1− 6 7 7 0 8 2 3 8 − 6 4 4 0 9 8 − 1 8 3 1 4 4 2 − 2 6 6 8 2 7 7 9 −3 8 2 9 4 5 2 − 9 73 8 5 2− 9 7 6 6 11 2 − 9 3 7 0 4 6 5 2 − 9 3 4 9 4 6 − 1 8 7 9 4 0 79 − 8 7 8 2 9 9 − 9 8 7 8 27 0 0 − 4 71 2 7 3 9 − 8 17 5 4 1 1 −4 7 3 5 5 2− 1 4 2 0 8 5 5 1 − 6 7 6 5 2 1 − 7 3 5 6 9 0 − 2 8 8 3 6 5 2 9 − 8 70 62 5 − 9 9 70 97 6 − 0 9 77 8 8 3 9 − 9 76 6 5 3 9 − 5 4 1 7 6 4 − 1 6 21 7 3 6 − 1 6 5 7 1 5 4 2 −6 8 7 8 6 7 0 −7 8 2 8 3 7 9 −7 4 2 2 5 5 0 − 9 17 0 7 8 1 − 9 4 1 4 7 1 − 2 4 2 5 11 3 − 1 6 5 7 1 5 9 1 −6 8 7 3 6 5 2 − 2 6 2 9 6 9 − 9 6 81 7 2 5 − 7 8 5 2 2 3 5 9 −6 3 7 1 6 3 5 −932
noitalerroc nosraeP Method Biopsy site snRNA seq scRNA seq PAM50 Receptors Pearson correlation −0.200.20.40.60.81 srekraM srotpeceR h Pseudobulk expression across malignant cells g Expression in malignant cells
i
10
7
0
5
T C MR N TE P CM Y A1 3 58 RRR PPP SLL21 9 06
C P FC G ED G MC T 11C 1 1 B 2 TS AK E MT C R R AS B BT RB B RA D4 2 81 3X
APKZ 0IAN 0AF 004 6 43412 69.1 Z H FR3 AP
N
F NL
FC D
39
B
D
P U
A
X
3
N FOE A 3810 STA C GM R FDB 2 114 SGR E E MRKSC 1FI 2 P11 M S
M
P L H C
R
O 2
P
5
S
S A
3
P 3
5
H 7 6
TMH CEP CMG R2D 443 ZC SFM HA
H
S YN
NP
T D
C
D
CR
1 3
L
13
NB K PP1 2H3 GM TRL SER 4B1 A 011L S SRA EAP CD3 2 093 BAB P PFAT AFM MA2H9 D 611BA2
C
G
A
M
P
PG
Z
XP
A
7
2 RR RPP PSL L13 152 9A
MANP A PXP I 2AH K113 G S R R E P B 7 1 2 LC S H T C D D N A S M C P 3 1 2 C T CLMSD SMC B11 427 X 4 DCTN2
50
25 TPU PCD BDX AHK 1C1 TDXA ANC GRP LD2 B3 SKN DA P C RH EJTMR R DG A 7 11155 ADA A NARMK L R 8TDSA 1L2 ALS3T P5A T6R P4A D848.3 AML7 R G3 F A1 N 5T G 649B.1
0
)%(
denialpxe ecnairav
noisserpxE
n = 5 n = 28 n = 8 n = 22 n = 3 n = 3 n = 44 n = 3 n = 16
j
Sample wise pseudobulk expression across ... Patient ID Method Biopsy Most recent Histology Receptor Metastatic Residuals
sc/sn Site tx class status presentation
...Malignant ...Stromal ...Lymphoid ...Myeloid Malignant
PGR ESR1
ERBB2 Stromal PGR ESR1 ERBB2 Lymphoid
PGR
ESR1
ERBB2 Myeloid PGR ESR1
ERBB2
0 0.25 0.50 0.75 1.00
Variance explained (%)

Article https://doi.org/10.1038/s41591-024-03215-z
Fig. 2 | Cell type composition and expression variance in snRNA-seq and expression) and frequency (fraction of expressing cells) of malignant marker
scRNA-seq data. a, UMAP representation of snRNA-seq and scRNA-seq data, genes as well as disease-relevant BC biomarkers across malignant cells, grouped
colored by cell type. b, Stacked bar plots showing the cellular compartment by =profiling method and receptor status. h, Clustered heatmap of pair-wise
composition for each sample in the snRNA-seq and scRNA-seq data. Samples correlations between pairs of pseudobulk expression profiles representing
that come from the same patient are highlighted in bold. c, Stacked bar plots each sample’s malignant cell population, corrected for profiling method using
showing the cell type composition for pairs of samples from the same patient. ComBat (Methods). Inset: box plots overlaid with individual data points (=sample
sc, scRNA-seq; sn, snRNA-seq. d, Violin and box plots representing the percent combinations as in the heatmap) showing the pair-wise Pearson correlation
variance in cell type frequency explained by the indicated variable for each of across samples within PAM50 groups. The significance of differences between
the 26 annotated cell types (e). n = 26 cell types; tx, treatment. e, Stacked bar the basal and all other groups (two-sided Wilcoxon test) is indicated. i, Violin
plots showing the percent variance in cell type frequency explained by the and box plots representing for all genes the percent variance in normalized
indicated variables for each of the 26 annotated cell types. f, Box plots with expression levels across sample-wise and compartment-wise pseudobulk
overlaid data points (=samples), representing the normalized macrophage profiles, explained by the indicated variable. The top 3–5 genes are indicated.
frequency (Pearson’s contingency ratio) stratified by different properties n = 26,539 genes. j, Stacked bar plots showing the percent variance in normalized
of the two variables that explain variance in macrophage frequency (e). The expression levels across sample- and compartment-wise pseudobulk profiles,
significance of differences in ‘one against all others’ comparisons (two-sided explained by the indicated variables from i for the three receptor status defining
Wilcoxon test, Benjamini–Hochberg correction) is indicated. n indicates the genes, ESR1, PGR and ERBB2.
number of biopsy samples. g, Dot plots depicting the expression level (mean
hepatocytes and fibroblasts. Irrespective of method, biological factors, patient had congruent inferred CNAs across lesions (Extended Data
such as individual, time, lesion and site, can have substantial effects Fig. 4c), profiling method (Extended Data Fig. 4d) and time (Extended
on composition. Data Fig. 4e,f). Two biopsies taken 220 days apart (patient 862), with
We examined the impact of scRNA-seq (four biopsies) versus intervening therapy, retained the same subclonal structure, albeit with
snRNA-seq (one biopsy) in bone biopsies, a clinically relevant meta- varying proportions (Extended Data Fig. 4e).
static site that yields lower content biopsies (Extended Data Fig. 3e,f). As expected, inter-patient variability in the expression of ESR1,
Although scRNA-seq captured malignant cells in only two of four, PGR and ERBB2 aligned well with clinical receptor status. Nevertheless,
snRNA-seq captured the malignant compartment well but yielded among estrogen receptor–positive (ER+) samples, ESR1 expression was
fewer immune cells (Extended Data Fig. 3e), suggesting that snRNA-seq captured more robustly in snRNA-seq (Fig. 2g). Inter-patient variability
might be more suitable when prioritizing malignant cell profiling, in established epithelial BC marker genes (EPCAM, KRT8, KRT18, KRT19
and scRNA-seq might be more suitable when prioritizing associated and TRPS1) was minimally impacted by receptor status but notably by
immune cells. Notably, expression of genes previously reported to profiling method (Fig. 2g).
be implicated in bone metastasis23–28 was detected across all biopsy At the level of expression programs, clustering malignant profiles
sites (not bone specific) and was rather cell type specific (Extended by mean gene set enrichment analysis (GSEA) hallmark signature scores
Data Fig. 3f), with two exceptions (SPP1 and CCN2), which were more in malignant cells yielded clear grouping in snRNA-seq (for example,
highly expressed in axilla, bone and breast macrophages and fibro- interferon response, estrogen response and MYC/G2M checkpoint
blasts, respectively (Extended Data Fig. 3f). We also examined the groups) but less so in scRNA-seq, with few exceptions (for example, 414
ability of snRNA-seq to profile brain metastases, a clinically relevant and 586 scoring highly for epithelial-to-mesenchymal transition (EMT)
site underrepresented in genomic datasets. snRNA-seq captured and angiogenesis, respectively) (Extended Data Fig. 5). Clustering of 40
both malignant cells and tumor microenvironment well, anecdotally cross-sample malignant expression programs learned with integrative
supporting this approach (Extended Data Fig. 3e). non-negative matrix factorization (iNMF)30 separately from snRNA-seq
Next, we systematically quantified the contributions of biological, and scRNA-seq (Methods) revealed six clusters, five of which included
clinical and technical variables to variability in cell type composi- programs derived from both methods. Three of these had highly cor-
tion (Methods). Patient ID, profiling method and site explained the related programs and congruent biological processes: two associated
most variability overall (Fig. 2d), but other variables had considerable with cell cycle and the third with EMT (Extended Data Fig. 6). To further
effects on variation in particular cell types (Fig. 2e). Approximately compare malignant cell states, we clustered pseudobulk profiles gener-
20% of the variability in chondrocytes was explained by histology, ated from the malignant cells of each biopsy. This revealed two major
whereas variability in macrophages was explained by treatment class clusters: one predominantly comprised HR+ and LumA/B tumors and
(~50%) and receptor status (~10%) (Fig. 2e). Higher macrophage abun- was enriched in liver biopsies (P = 0.0185, two-sided Fisher’s exact
dance was associated with recent immunotherapy and with HR−/HER2− test), and the other predominantly comprised HR−/HER2− biopsies,
disease (Fig. 2f). which further separated into basal-like and HER2-like subsets and was
enriched in axilla biopsies (P = 4.92 × 10−4, two-sided Fisher’s exact
Clinical features explain variation in expression profiles test) (Fig. 2h). Basal-like biopsies formed a highly correlated exclu-
Although non-malignant cells clearly grouped by cell type across sive subcluster (Fig. 2h), suggesting higher expression stability of the
biopsies, malignant cells grouped first by patient (Fig. 2a) as previously basal subtype, consistent with previous reports31–33. Notably, biopsies
described in scRNA-seq of solid tumors17,29, consistent with diverse from the same patient grouped together, even in two cases where they
patterns of inferred copy number aberrations (CNAs) between changed from HR+ or HER2+ to HR−/HER2−, confirming the relative
patients (Extended Data Fig. 4a,b). Conversely, biopsies from the same stability and patient specificity of malignant cell-intrinsic expression
Fig. 3 | Spatial expression profiling of MBC biopsies. a, Overview of all spatial cell type composition within spatially corresponding 100 × 100-μm bins across
expression datasets covering all samples and methods included in this study. methods, within biopsies. An example for one bin (white star) within one biopsy
For each successful sample–method combination, a spatial scatter plot is shown is shown. c, Box plots displaying the correlations between cell type compositions
where each observation (cell, bead and bin) is displayed and colored by its OT within spatially corresponding 100 × 100-μm bins as measured by the indicated
annotated cell type. Data for the same biopsy are spatially aligned and depicted pairs of methods, displayed individually per biopsy. Correlations within the same
at the same scale. A more detailed view of individual samples for which data are method were calculated when technical replicates were available. The mean
available from all spatial profiling methods is provided in Supplementary Figs. 1–5. Pearson correlation for each pair of methods is indicated by the color-scaled
b, Schematic illustrating the comparison by Pearson correlation of high-resolution inset. n indicates the number of 100 × 100-μm bins.
Nature Medicine | Volume 30 | November 2024 | 3236–3249 3240

| Article |     |     |     |     |     |     |     |     |     | https://doi.org/10.1038/s41591-024-03215-z |     |     |     |     |     |
| ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------ | --- | --- | --- | --- | --- |
a
944– 895–7359 880–7179 878–7149 812– 514–6760 982– 997– 917– 853– 313– 330– 783–4081 364–1321 213–6752
| 7479 |     |     |     |     |     | 8239 |     | 7629 | 7789 | 4531 4381 | 932 | 1082 |     |     |     |
| ---- | --- | --- | --- | --- | --- | ---- | --- | ---- | ---- | --------- | --- | ---- | --- | --- | --- |
qes-edilS
1 mm 1 mm 1 mm 1 mm 1 mm 1 mm 1 mm 1 mm 1 mm 1 mm 1 mm 1 mm 1 mm 1 mm 1 mm
HSIFREM
MBC
| 1 mm |     |     | 1 mm | 1 mm |     | 1 mm 1 mm |     | 1 mm | 1 mm | 1 mm | 1 mm |     |     |     |     |
| ---- | --- | --- | ---- | ---- | --- | --------- | --- | ---- | ---- | ---- | ---- | --- | --- | --- | --- |
MBC_stem-like
| )nib( HSIFREM |     |     |     |     |     |     |     |     |     |     |     |     |     | MBC_neuronal |     |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- |
Endothelial
Endothelial_sinusoidal
Endothelial_angiogenic
Endothelial_vascular
Fibroblast
Smooth muscle_vascular
Stellate
| 1 mm |     |     | 1 mm | 1 mm |     | 1 mm 1 mm |     | 1 mm | 1 mm | 1 mm | 1 mm |     |     | Skeletal muscle |     |
| ---- | --- | --- | ---- | ---- | --- | --------- | --- | ---- | ---- | ---- | ---- | --- | --- | --------------- | --- |
Hepatocyte
Neuron
Macrophage
| qeSxE |     |     |     |     |     |     |     |     |     |     |     |     |     | Monocyte |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- |
Mast
B_plasma
B
T
NK
|     | 1 mm |     | 1 mm |     |     | 1 mm |     | 1 mm | 1 mm |     | 1 mm | 1 mm 1 mm | 1 mm |     |     |
| --- | ---- | --- | ---- | --- | --- | ---- | --- | ---- | ---- | --- | ---- | --------- | ---- | --- | --- |
)nib( qesxE
|     |     |     | 1 mm |     |     | 1 mm |     | 1 mm | 1 mm |     | 1 mm | 1 mm 1 mm | 1 mm |     |     |
| --- | --- | --- | ---- | --- | --- | ---- | --- | ---- | ---- | --- | ---- | --------- | ---- | --- | --- |
XEDOC
1 mm 1 mm 1 mm 1 mm 1 mm 1 mm 1 mm 1 mm 1 mm 1 mm 1 mm 1 mm 1 mm
| b   |     |     |     |     | c   | CODEX |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Samples
|     |     | MERFISH |     | Exseq |     | 1.0 |     |     |     |     |     |     |     |     |     |
| --- | --- | ------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Tissue CODEXMERFISH Slide-seq ExSeq 213−6752 783−4081 895−7359
|     |     | (bin) |     | (bin) |                                                              | 0.5           |          |       |     |     | 313−932                  |     | 812−8239 | 917−4531 |     |
| --- | --- | ----- | --- | ----- | ------------------------------------------------------------ | ------------- | -------- | ----- | --- | --- | ------------------------ | --- | -------- | -------- | --- |
|     |     |       |     |       | noitisopmoc epyt llec fo noitalerroc nosraeP esiw−nib mµ-001 |               | ExSeq    |       |     |     | 330−1082                 |     | 853−4381 | 944−7479 |     |
|     |     |       |     |       |                                                              | 0             |          |       |     |     | 364−1321                 |     | 878−7149 | 982−7629 |     |
|     |     |       |     |       |                                                              |               |          |       |     |     | 514−6760                 |     | 880−7179 | 997−7789 |     |
|     |     |       |     |       |                                                              | −0.5          | 99 45    |       |     |     |                          |     |          |          |     |
|     |     |       |     |       |                                                              | 321           | 421 0.55 |       |     |     | Mean Pearson correlation |     |          |          |     |
|     |     |       |     |       |                                                              | −1.0 95 95 55 | 75       | ExSeq |     |     |                          |     |          |          |     |
|     | * * | *     | *   | * *   |                                                              | 1.0           |          |       |     |     |                          |     |          |          |     |
ExSeq (bin)
|     |     |     |     |     |     | 0.5 |     |     |     |     | 0.55 0.60 | 0.65 0.70 0.75 0.80 | 0.85 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------------------- | ---- | --- | --- |
0
|       |     |     |     |     |     | −0.5          | 59 06     |              | 88 25       |     |         |     |     |     |     |
| ----- | --- | --- | --- | --- | --- | ------------- | --------- | ------------ | ----------- | --- | ------- | --- | --- | --- | --- |
|       |     |     |     |     |     | 421           | 0.54      | 321 321 0.83 |             |     |         |     |     |     |     |
| (0|0) |     |     |     |     |     | −1.0 85 06 75 | 55 721 66 | 36 55 45     | ExSeq (bin) |     | MERFISH |     |     |     |     |
1.0
Example
| 100 × 100 µm   |     |     |     |     |     | 0.5 |     |     |     |     |     | MERFISH |     |     |     |
| -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- |
| bin  *   (2|8) |     |     |     |     |     | 0   |     |     |     |     |     |         |     |     |     |
390,1
MBC 7/17 6/15 28/50 22/43 6/17 18/28 −0.5 994 546 89 701 39 211 892
| T   | 4/17 3/15 | 6/50 | 7/43 | 3/17 7/28 |     | 364 449 |     |     |     |     |     |     |     |     |     |
| --- | --------- | ---- | ---- | --------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Fibroblast 3/17 3/15 7/50 7/43 3/17 7/28 −1.0 962 612 816 142 0.72 26 55 39 0.75 16 75 69 0.75 0.8 MERFISH (bin)
| Macrophage | 3/17 3/15                           | 9/50 | 7/43 | 4/17 6/28 |     | 1.0 |     |     |     |     |     |     |     | MERFISH (bin) |     |
| ---------- | ----------------------------------- | ---- | ---- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |
|            | Correlations of cell type fractions |      |      |           |     | 0.5 |     |     |     |     |     |     |     |               |     |
|            | for each method combination         |      |      |           |     | 0   |     |     |     |     |     |     |     |               |     |
624,3
|     |         |     |     |     |     | −0.5  | 815 466 |     | 001 501 | 69  | 011 | 685 882,1 |     | 581,1 513 |     |
| --- | ------- | --- | --- | --- | --- | ----- | ------- | --- | ------- | --- | --- | --------- | --- | --------- | --- |
|     | r = 0.9 |     |     |     |     | 620,1 |         |     |         |     |     |           |     |           |     |
2 dohteM bins Summarize bin-wise −1.0 494 603 542 556 513 0.79 56 55 911 0.78 46 75 221 0.77 716 559 272 912 836 832 0.83 0.86 Slide-seq
|     |     |     | correlations as |              |     | 1.0 |     |     |     |     |     |     |     |     |           |
| --- | --- | --- | --------------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- |
|     |     |     |                 | box plot per |     |     |     |     |     |     |     |     |     |     | Slide-seq |
0.5
method combination
0
Method 1 422 203 001 413 925 892 262 348 954 422 926 033 523 755 333 982 868 595 032 266 533 611 831 09 113 661 761 461 393 303 441
|     |     |     |     |     |     | −0.5                | 761                         | 38                     | 35        | 69              | 75  |     |     |      |      |
| --- | --- | --- | --- | --- | --- | ------------------- | --------------------------- | ---------------------- | --------- | --------------- | --- | --- | --- | ---- | ---- |
|     |     |     |     |     |     | 613 123 742 632 575 | 703 743 633 719 436 0.57 99 | 401 77 07 011 642 0.67 | 79 501 97 | 27 601 252 0.65 |     | 0.7 |     | 0.74 | 0.83 |
−1.0
| Nature Medicine | Volume 30 | November 2024 | 3236–3249 |     |     |     |     |     |     |     |     |     |     |     |     |     |     | 3241 |
| ------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |

Article https://doi.org/10.1038/s41591-024-03215-z
a sc/snRNA-seq Slide-seq MERFISH MERFISH (bin) CODEX ExSeq ExSeq (bin)
epyt lleC
elpmas/tneitaP
sretsulc nedieL
| Cell type |     |     |     |     |     |     | b   | Congruence of Leiden clustering with |     |     |     |
| --------- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------ | --- | --- | --- |
MBC Endothelial Fibroblast Hepatocyte B_plasma Patient/sample Cell type
| MBC_stem-like | Endothelial_sinusoidal |     | Smooth muscle_vascular |     | Neuron     | B   |           |     |     |     |     |
| ------------- | ---------------------- | --- | ---------------------- | --- | ---------- | --- | --------- | --- | --- | --- | --- |
| MBC_neuronal  | Endothelial_angiogenic |     | Stellate               |     | Macrophage | T   | scRNA-seq |     |     |     |     |
snRNA-seq
|                | Endothelial_vascular |          | Skeletal muscle |     | Monocyte | NK  | Slide-seq     |     |           |               |     |
| -------------- | -------------------- | -------- | --------------- | --- | -------- | --- | ------------- | --- | --------- | ------------- | --- |
|                |                      |          |                 |     | Mast     |     | MERFISH       |     |           | All cells     |     |
| Patient/sample |                      |          |                 |     |          |     |               |     |           | Non-malignant |     |
| 944–7479       | 812–8239             | 917–4531 | 783–4081        |     |          |     | MERFISH (bin) |     |           |               |     |
| 895–7359       | 514–6760             | 853–4381 | 364–1321        |     |          |     | CODEX         |     |           | Malignant     |     |
| 880–7179       | 982–7629             | 313–932  | 213–6752        |     |          |     | ExSeq         |     |           |               |     |
| 878–7149       | 997–7789             | 330–1082 |                 |     |          |     | ExSeq (bin)   |     |           |               |     |
|                |                      |          |                 |     |          |     |               | 0   | 0.5 1.0 0 | 0.5 1.0       |     |
Adjusted Rand index
c
|     | Slide-seq |     | MERFISH |     | MERFISH (bin) |     | ExSeq |     | ExSeq (bin) | CODEX |     |
| --- | --------- | --- | ------- | --- | ------------- | --- | ----- | --- | ----------- | ----- | --- |
514–6760: Short-range accumulations
)).hpo 1.5
r c ) o 1.0
a M n n
| o nna(p(gol a ( p 0.5
0
–0.5
0 100200300400500 0 1002003004005000 1002003004005000 1002003004005000 1002003004005000 100200300400500
|     | Distance |     | Distance |     | Distance |     | Distance |     | Distance | Distance |     |
| --- | -------- | --- | -------- | --- | -------- | --- | -------- | --- | -------- | -------- | --- |
917–4531: Long-range accumulations
)).hporcaM|onna(p(gol
2
)onna(p
1
0
0 1002003004005000 1002003004005000 1002003004005000 1002003004005000 100200300400500 0 100200300400500
|     | Distance |     | Distance |     | Distance |     | Distance |     | Distance | Distance |     |
| --- | -------- | --- | -------- | --- | -------- | --- | -------- | --- | -------- | -------- | --- |
313–932: Intermixing
)).hpo 1.0
r c ) o
a M n n a 0.5
| o nna(p(gol ( p
0
–0.5
0 1002003004005000 1002003004005000 1002003004005000 1002003004005000 100200300400500 100200300400500
|     | Distance |     | Distance |     | Distance |     | Distance |     | Distance | Distance |     |
| --- | -------- | --- | -------- | --- | -------- | --- | -------- | --- | -------- | -------- | --- |
e
d Macrophage co-localization with... Macrophage co-localization with f 313–932
74% CD163+
|                     | NK          |                |                | htgnerts noitazilacol-oC |              |                            | Malignant cells       | Macrophages              |                 |                   |                                         |
| ------------------- | ----------- | -------------- | -------------- | ------------------------ | ------------ | -------------------------- | --------------------- | ------------------------ | --------------- | ----------------- | --------------------------------------- |
|                     | T           |                |                |                          | 997–7789     |                            |                       |                          |                 | 917–4531          | Macrophages in tissue context (MERFISH) |
|                     | B           |                |                |                          | 1            |                            |                       |                          |                 | 92% CD163+        |                                         |
|                     | B_plasma    |                |                |                          | 982–7629     |                            |                       |                          |                 |                   |                                         |
|                     | Mast        |                |                |                          | 0 944–7479   |                            |                       |                          |                 | CD163 expression: |                                         |
|                     | Monocyte    |                |                |                          | –1 917–4531  |                            |                       |                          |                 |                   |                                         |
|                     | Macrophage  |                |                |                          | 895–7359     |                            |                       |                          |                 | Low High          |                                         |
|                     | Neuron      |                |                |                          | –2 880–7179  |                            |                       |                          |                 |                   |                                         |
|                     | Hepatocyte  |                |                |                          | 878–7149     |                            |                       |                          |                 | 500 µm            |                                         |
| Skeletal muscle     |             |                |                |                          | –3 853–4381  |                            |                       |                          |                 | 514–6760          |                                         |
|                     | Stellate    |                |                |                          | 812–8239     |                            |                       |                          |                 | 89% CD163+        |                                         |
| Smooth muscle_vasc. |             |                |                | egnar noitazilacol-oC    | 100 783–4081 |                            |                       |                          |                 |                   |                                         |
|                     | Fibroblast  |                |                |                          | 514–6760     |                            |                       |                          |                 |                   |                                         |
|                     |             |                |                |                          | 200 364–1321 |                            |                       |                          |                 |                   |                                         |
| Endothelial_vasc.   |             |                |                |                          | 330–1082     |                            |                       |                          |                 |                   |                                         |
| Endothelial_angio.  |             |                |                |                          | 300 313–932  |                            |                       |                          |                 |                   |                                         |
| Endothelial_sinus.  |             |                |                |                          | 213–6752     |                            |                       |                          |                 |                   |                                         |
|                     | Endothelial |                |                |                          | 400          | CODEX eq                   | ) H ) de-seq          | CODEX eq                 | ) H ) de-seq    |                   |                                         |
| MBC_neuronal        |             |                |                |                          |              | S                          | eq (b in FI S H (b in | S eq (b                  | in FI S H (b in |                   |                                         |
| MBC_stem-like       |             |                |                |                          | 500          | Ex                         | E R                   | Ex                       | E R             |                   |                                         |
|                     | MBC         |                |                |                          |              | xS                         | M F IS S li           | xS                       | M F IS S li     |                   |                                         |
|                     | CODEX       | q              | ) H ) lide-seq |                          |              | E                          | ER                    | E                        | ER              |                   |                                         |
|                     |             | ExS e Seq (bin | I S ISH (bin   |                          |              |                            | M                     |                          | M               |                   |                                         |
|                     |             |                | E RF           |                          |              | Malignant subtypes         | Co-localization range | Co-localization strength |                 |                   |                                         |
|                     |             | x              | M F S          |                          |              | MBC                        |                       |                          |                 |                   |                                         |
|                     |             | E              | E R            |                          |              | MBC_neuronal MBC_stem-like |                       |                          |                 |                   |                                         |
|                     |             |                | M              |                          |              |                            | 500400300200100       | –1                       | 0 1 2 3         |                   |                                         |
Nature Medicine | Volume 30 | November 2024 | 3236–3249 3242

Article https://doi.org/10.1038/s41591-024-03215-z
Fig. 4 | Recovering spatial and molecular signals across spatial expression selected to represent three spatial co-localization phenotypes (short-range
profiling methods. a, UMAPs of all data across biopsies based on their accumulation, long-range accumulations and intermixing). The distance is
expression profiles, generated with the indicated methods, with observations measured in μm. d, Dot plot displaying aggregated (mean across samples)
colored by TACCO-OT annotated cell type, patient/sample and Leiden clusters co-localization range (size) and strength (color) of macrophages with all other
(resolution, 0.8). b, Error bar plot with mean ± s.d. showing the ARI quantifying cell types per method. Co-localization strength values lower than 0 indicate
cluster cohesion between Leiden clusters and patient/sample or cell type exclusion/repulsion. e, Dot plot displaying co-localization range (size) and
annotation across 10 bootstrapping iterations for each indicated method, as in strength (color) of macrophages with other macrophages or malignant cells for
a. ARI ranges between −1 and 1, where 1 indicates perfect agreement, 0 indicates all samples and methods. Co-localization strength values lower than 0 indicate
a random agreement and −1 indicates completely different groupings. n = 10 exclusion/repulsion. f, Spatial scatter plot of macrophages overlaid onto H&E
bootstrapping iterations. c, Line plots depicting co-localization strength (y axis) images showing the expression levels of CD163 in the depicted macrophages, for
of macrophages with all other measured cell types in dependence of distance the three example biopsies representing the three co-occurrence cases as in c,
(x axis), derived from the indicated data types in the indicated three biopsies, based on cell-segmented MERFISH data.
profiles through MBC disease progression, possibly due to the strong showed only low levels of explainable variance by these characteris-
effect of CNAs on expression34,35. tics. Additionally, although profiling methods have non-negligible
To dissect inter-patient expression variance in each compart- effects on all compartments, these can be mostly addressed by data
ment, we estimated, for each gene, the variability explained by clinical/ inte gration methods before comparing cell or gene profiles.
technical covariates (Methods and Fig. 2i). These variables explained
a large fraction of the inter-patient variance in intrinsic expression in Comparison of spatial expression profiling methods
the stromal (median, ~65%) and malignant (median, ~85%) compart- Our experimental design enabled profiling serial sections of the same
ments but much less in the immune compartments (median, ~30%). biopsy with up to four different methods (Fig. 1a). We used a common
Consistent with our other observations, patient ID explained the most observation × features format for analysis, where observations cor-
variance in the malignant compartment but played a negligible role in responded to segmented cells (MERFISH, ExSeq and CODEX), beads
the immune compartments. Conversely, histology explained approxi- (Slide-seq) or 10 × 10-μm bins (MERFISH (bin) and ExSeq (bin)), and
mately 10% variance in the myeloid compartment but was negligible features corresponded to RNA or protein sets denoted as the official
for all others. Across all compartments, profiling method explained a gene alias for all methods (Fig. 1b and Methods). We scaled to a 1-μm-per-
median of approximately 20–25% variance, consistent with previous pixel positional resolution (Methods), registered to a common
reports15,16 (Fig. 2i and Extended Data Fig. 5). ComBat36 adequately coordinate system, and applied quality filtering in a method-specific
corrected such ‘platform effects’ at the pseudobulk level, revealing manner (Fig. 1b and Methods). We annotated cell types by label trans-
relevant biology across methods (Fig. 2h), and Harmony37 (but not fer from the matching sc/snRNA-seq using RCTD43 and TACCO-OT44
BBKNN38) produced an aligned embedding at the single-cell level that (Methods). TACCO-OT was selected for downstream analyses as it
appropriately grouped non-malignant cells across patients/methods was better able to handle both count and non-count data (Extended
while maintaining biological variability in the malignant compartment Data Fig. 8a and Supplementary Figs. 1–5a,b).
(Extended Data Fig. 7). Spatial cell type maps appeared broadly congruent across serial
Although receptor status explained a sizeable fraction of the sections profiled by different methods (Fig. 3a and Supplementary
expression variation of PGR (~56%), ESR1 (~44%) and ERBB2 (~68%) Figs. 1–5) but ranged in their FOV from the whole biopsy (MERFISH
in the malignant compartment (Fig. 2j), it only explained substantial and CODEX) to a circular area with an approximately 3-mm diameter
variance (>44%) in 34 other genes (Supplementary Table 4), some of (Slide-seq) to approximately 1 mm2 (ExSeq). Binned MERFISH
which were reassuringly associated with one of the receptors. These and ExSeq patterns matched the segmented ones but were more
included STARD3, GRB7, MIEN1 and LASP1, which are adjacent to pronounced and less sparse, likely due to a combination of signal
ERBB2 on 17q12 and subject to co-amplification, and MTA2, whose included in binning but lost due to non-assignment in segmentation
expression is associated with ERα expression39. Others, including as well as signal filling of cell-proximal extracellular space in binning.
TMSB4X and BECN1, were previously associated with metastatic pro- To assess the agreement between methods in local cell type organiza-
gression but not with BC receptor expression40–42, suggesting the tion, we calculated pair-wise correlations between methods based
potential to uncover novel associations. on cell type composition in aligned 100 × 100-μm bins (Fig. 3b,c
These results show strong inter-patient variability of malignant and Extended Data Fig. 8b). Correlations were high across method
expression profiles, with patient-specific profiles maintained during combinations and samples (median Pearson’s r ≈ 0.9), except for
MBC progression through time, site and even changes in receptor status. three samples (330, 364 and 783) with no correlation (median, r ≈ 0)
In contrast, the expression profiles in the immune compartments among any of the three methods (CODEX, ExSeq and Slide-seq) (Fig. 3c).
Fig. 5 | Characterizing macrophage and malignant expression phenotypes is colored by its EMT score expression (capped at −1 and 1 for comparability).
across spatial expression profiling methods. a, UMAPs of all observations Samples are grouped into three spatial EMT phenotypes—EMT-high, EMT-low
confidently annotated as macrophages across biopsies based on their and EMT-patched—based on the distribution of the EMT signal across space.
expression profiles, colored by log-normalized expression of CD163, log- f, Dot plot depicting the differential expression significance (two-sided Welch’s
normalized expression of HLA-DRA or Leiden clusters. b, Dot plot depicting t-test, Benjamini–Hochberg correction) of genes overexpressed in one of the
the scaled expression (by gene, across clusters) and fraction of expressing cells three spatial EMT phenotypes (EMT-high, EMT-low and EMT-patched), as
of macrophage marker and function genes as well as marker genes for other detected in the cell-segmented MERFISH data (e). g, Scatter plot relating the log
cell types and differentially expressed genes between clusters as in a for cell- fold changes of gene expression between EMT-high and EMT-patched samples
segmented MERFISH data. Side bar plots indicate the number of cells in each as detected in cell-segmented MERFISH to the corresponding expression
cluster. c, Clustered heatmap depicting the pair-wise Spearman correlation of changes detected in the other indicated methods. The significance of differential
methods based on sample-wise pseudobulk expression of macrophage marker expression was calculated by a two-sided Welch’s t-test and Benjamini–Hochberg
and function genes as in b. d, UMAPs of all observations annotated as malignant correction. The Spearman correlation is indicated. Error bands indicate standard
cells across biopsies based on their expression profiles, colored by their EMT error. h, Clustered heatmap depicting the pair-wise Spearman correlation of
score expression (capped at −1 and 1 for comparability) or patient/sample. methods based on gene-wise log fold changes between EMT-high and EMT-
e, Spatial scatter plots of the cell-segmented MERFISH data where each cell patched samples, defined as in e and related to g. FC, fold change; man, manual.
Nature Medicine | Volume 30 | November 2024 | 3236–3249 3243

| Article |     |     |     |     |     |     |     |     |     | https://doi.org/10.1038/s41591-024-03215-z |     |     |     |     |
| ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------ | --- | --- | --- | --- |
a sc/snRNA-seq snRNA-seq scRNA-seq Slide-seq MERFISH MERFISH (bin) ExSeq ExSeq (bin) CODEX
|     |                                    | 4   |     |     | 4   |     |     | 8   | 8   |     |     |     | 6   |     |
| --- | ---------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | )PAMU dengila-ynomraH( segahporcaM |     |     | 3   |     | 4   |     |     |     |     | 6   |     |     |     |
|     | 361DC                              | 3   |     |     | 3   |     |     | 6   | 6   |     |     |     | 4   |     |
|     |                                    |     |     | 2   |     |     |     | 4   | 4   |     | 4   |     |     |     |
|     |                                    | 2   |     |     | 2   | 2   |     |     |     |     |     |     |     |     |
|     |                                    | 1   |     | 1   | 1   |     |     | 2   | 2   |     | 2   |     | 2   |     |
|     |                                    | 0   |     | 0   | 0   | 0   |     | 0   | 0   |     | 0   |     | 0   |     |
|     |                                    | 8   |     |     | 8   | 6   |     |     |     |     | 8   |     | 8   |     |
|     | ARD-ALH                            |     |     |     |     |     |     | 6   | 6   |     |     |     |     | 8   |
|     |                                    | 6   |     | 4   | 6   |     |     |     |     |     | 6   |     | 6   | 6   |
|     |                                    |     |     |     |     | 4   |     | 4   | 4   |     |     |     |     |     |
|     |                                    | 4   |     |     | 4   |     |     |     |     |     | 4   |     | 4   | 4   |
|     |                                    | 2   |     | 2   | 2   | 2   |     | 2   | 2   |     | 2   |     | 2   |     |
2
|     |     | 0   |     | 0   | 0   | 0   |     | 0   | 0   |     | 0   |     | 0   | 0   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
sretsulc nedieL
|     | Leiden clusters |     | 0 1 | 2 3 4 5 | 6 7 8 9 | 10 11 | 12 13 | 14 15 |     |     |     |     |     |     |
| --- | --------------- | --- | --- | ------- | ------- | ----- | ----- | ----- | --- | --- | --- | --- | --- | --- |
Seq
b Macrophage marker genes Macrophage function genes Other cell type markers Differentially expressed genes c Spearman correlation of x b i n ) 1 . 0
|                   |     |     |     |     |     |     |     |             |     | sample-wise mean MΦ |              | E             | Seq   (      |             |
| ----------------- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ------------------- | ------------ | ------------- | ------------ | ----------- |
|                   | 0   |     |     |     |     |     |     | 1 . 1 k     |     | marker & function   |              | 2 7           | x e q        | 0 . 5       |
| HSIFREM detnemgeS | 1   |     |     |     |     |     |     | 1 . 1 k     |     |                     |              | 0 . E         | e - s        |             |
|                   | 3 2 |     |     |     |     |     |     | 2 2 0 2 1 5 |     | expression          | .            | 0 7 3 0 . 1 7 | S l i d DE X | 0           |
|                   | 4   |     |     |     |     |     |     | 1 9 4       |     |                     | 6 0          | 3             | 5 O          | H )         |
| sretsulc          | 5   |     |     |     |     |     |     | 1 4 3       |     |                     | 0 . 0 7      | 0 .0 3 0 .    | 5 C ERF      | I S  (b i n |
|                   | 6 7 |     |     |     |     |     |     | 1 4 2       |     |                     | .1           | 9 5 5 1       | 6 4 M        | IS H        |
|                   | 8   |     |     |     |     |     |     | 1 1 3 4 4 2 |     |                     | 0 0 .        | 0 0 .         | 0 .          | RF q        |
|                   | 9   |     |     |     |     |     |     | 1 3 2       |     |                     | .0 3 6 0 . 1 | . 6 2 .       | 5 5 . 8 2    | M E A - s e |
10 1 2 2 F r a c t io n   o f   c e l ls 47– 0 35 0 0 0 RN A-seq
12 11 1 1 0 0 6 7 i n   g r o u p   ( % ) 0.0 –0 . 0 0 . 4 8 0 . 6 3 0 . 6 4 0 . 76 s c
|     | 13  |     |     |     |     |     |     | 9 8 1 0 3 0 | 5 0 7 0 9 0   | 0.87 | 0 3 .3 5 | 6 5     | 9 3 7 1 | A n R N |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------------- | ---- | -------- | ------- | ------- | ------- |
|     | 14  |     |     |     |     |     |     | 9 1 M e a n |   s c a l e d |      | 0 .0 0   | 0 . 0 . | 0 .     | N s     |
|     | 15  |     |     |     |     |     |     | 6 9 e x p   | r e s s i o n | 1 1  | 1        | 1 1     | 1 1     | 1       |
361DC 86DC 4DC 41DC A3RGCF ARD-ALH 1APD-ALH AQ1C BQ1C 1RSM 1FIA 1PPS CEFT 1NCF AR3LI 2LCC XAGTI 51GSI 02GSI 9PMM 21PMM ZYL 3TSC 8A001S 9A001S EOPA 1COPA 472DC A1FIH 76IKM FPNEC 91TRK 1BZM 91DC A8DC E3DC 2DC 1A3LOC 2A4LOC 1MACN BRPTP NPDP ARD-ALH 4LCC 1NCF NLNA 061RPG 9DC 1LCX 1FLUS 1CDS 6KDC 3DYXF 5CXXC 472DC 11PMM PAF 5DC ExSeq ExSeq (bin) Slide-seq CODEX MERFISH MERFISH (b s cR snRNA-seq
|     |     |     |     |     |     |     |     | 0   | 0.5 1.0 |     |     |     |     | NA-seq |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | ------ |
in )
d
sc/snRNA-seq Slide-seq MERFISH MERFISH (bin) ExSeq ExSeq (bin) CODEX
|     | )PAMU dengilanu( sllec tnangilaM |     |     |     |     |     |     |     |     |     |     |     |           | 1.0 |
| --- | -------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- |
|     | erocs TME                        |     |     |     |     |     |     |     |     |     |     |     | erocs TME | 0.5 |
0
–0.5
–1.0
944–7479
|     | elpmas/tneitaP |     |     |     |     |     |     |     |     |     |     |     |     | 880–7179 |
| --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- |
878–7149
812–8239
514–6760
982–7629
917–4531
853–4381
313–932
| e   |     |     |     |     |     |     |     |     |     | f   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
-----------------EMT-low---------------|-----------------EMT-patched----------------|---------------EMT-high-----------------
|     | 313–932      |          |          |                   |              |          |     |          |     | CDC20 |     |     |      |          |
| --- | ------------ | -------- | -------- | ----------------- | ------------ | -------- | --- | -------- | --- | ----- | --- | --- | ---- | -------- |
|     |              |          |          | 853–4381 917–4531 |              |          |     |          |     | CTSL  |     |     |      | Enriched |
|     |              | 812–8239 |          |                   | 944–7479 1-3 |          |     |          |     | SDC1  |     |     |      | Depleted |
|     | 982–7629 1-2 |          |          |                   |              | 878–7149 |     |          |     | BGN   |     |     |      |          |
|     |              |          |          |                   |              |          |     |          |     |       | RB1 |     | –log |  FDR     |
|     |              |          | 880–7179 |                   |              |          |     | 514–6760 |     |       |     |     |      | 10       |
|     |              |          |          |                   |              |          |     |          |     | ZEB1  |     |     |      | 1        |
CCND1
|     |     |     |     |     |     |     |     |     |     | NF1  |     |     |     | 2   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- |
|     |     |     |     |     |     |     |     |     |     | CD3G |     |     |     | 3   |
AGR2
|     |     |     |     |     |     |     | EMT score |       |     | SIAH2            |                         |         |       | 4    |
| --- | --- | --- | --- | --- | --- | --- | --------- | ----- | --- | ---------------- | ----------------------- | ------- | ----- | ---- |
|     |     |     |     |     |     |     | –1.0      | 0 1.0 |     |                  |                         |         |       |      |
|     |     |     |     |     |     |     |           |       |     |                  | Low                     | Patched | High  |      |
|     |     |     |     |     |     |     | 1 mm      |       |     |                  | EMT phenotype           |         |       |      |
|     |     |     |     |     |     |     |           |       |     |                  |                         |         | q     | 1    |
|     |     |     |     |     |     |     |           |       |     |                  |                         |         | - s e |      |
| g   |     |     |     |     |     |     |           |       | h   | S p e a r m a n  |   c o r r e l a t i o n | N A     |       | 0 .5 |
|     |     |     |     |     |     |     |           |       |     | o f  g e n e - w | i s e                   | sn R    | q )   |      |
s c / s n R N A-seq S li d e -seq M E R F IS H (bin)M E R F ISH (man) E x S eq E x S e q  (bin) CODEX lo g F C   ( h i g h / p a t c h e d ) c / s e b i n
|                     |     |     |     |     |     |     |     |     |     | 2   |     | s d e     | - H   ( | 0   |
| ------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------- | --- |
| )dehctap/hgih(CFgol |     |     |     |     |     |     |     |     |     |     |     | 0 3 S l i | I S     |     |
)dohtem detacidni( rs  =   0 .4 1 4 rs =  0 . 9 19 rs  =  0 .9 28 rs   =  1 rs = 0 . 0 26 rs  =   0 .0 1 rs = 0.102 − 0 . R F H n ) − 0 .5
|     | 5   |     |     |     |     |     |     |     |     |           | 0 . 0 2       | . 0 9           | M E F I S  | m a          |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------------- | --------------- | ---------- | ------------ |
|     |     |     |     |     |     |     |     |     |     |           | 3 −           | 3 0 3           | E R h      |  (           |
|     | 0   |     |     |     |     |     |     |     |     |           | 0 . 1         | 0 . 1 − 0 . 0   | M f i s    |              |
|     |     |     |     |     |     |     |     |     |     |           | 4 1 0 9       | . 0 1           | 0 1 M e r  | E X          |
|     |     |     |     |     |     |     |     |     |     |           | 0 . 0 .       | − 0             | 0 .        | O D          |
|     | −5  |     |     |     |     |     |     |     |     | 0         | . 4 1 0 . 9 2 | 0 . 1 1 0 . 0 3 | 0 . 0 1 C  | e q n )      |
|     |     |     |     |     |     |     |     |     |     | 7         | 2 2           | 0               | 3 2        | x S xSeq (bi |
|     |     |     |     |     |     |     |     |     |     | 0 .3      | 0 . 9 0 . 9   | 0 . 1           | 0 . 0 0 .0 | E            |
| 2   | −10 |     |     |     |     |     |     |     |     | .5 4      | 9 0 9 3       | .0 0 . 1 1      | 0 3 .9     | 9 E          |
|     |     |     |     |     |     |     |     |     |     | 0 0       | . 0 .         | 1 0             | 0 . 0      |              |
|     |     |     |     |     |     |     |     |     |     | 1.00 1.00 | 1.00 1.00     | 1.00            | 1.00 1.00  | 1.00         |
−6 −3 0 3 6−6 −3 0 3 6−6 −3 0 3 6−6 −3 0 3 6−6 −3 0 3 6 − 6 − 3 0 3 6 − 6 −3 0 3 6 sc/snRNA S M M M ExSeq ExSeq (bin)
|     |     |     |     |                     |     |          |           |                   |     |     | li d ERFISH | E R ERFISH  | C O |     |
| --- | --- | --- | --- | ------------------- | --- | -------- | --------- | ----------------- | --- | --- | ----------- | ----------- | --- | --- |
|     |     |     |     | logFC(high/patched) |     |          |           |                   |     |     | e-seq       | F ISH       | D E |     |
|     |     |     |     | 2 (MERFISH)         |     | D iv erg | i ng P <  | 0. 0 5 P  > 0 .05 |     |     |             |             | X   |     |
|     |     |     |     |                     |     |          |           |                   |     |     | -s e        |  ( b in     | (m  |     |
|     |     |     |     |                     |     |          |           |                   |     |     | q           | )           | a n |     |
)
| Nature Medicine | Volume 30 | November 2024 | 3236–3249 |     |     |     |     |     |     |     |     |     |     |     |     |     | 3244 |
| ------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |

Article https://doi.org/10.1038/s41591-024-03215-z
These three samples did not pass MERFISH QCs, suggesting that more Spatial profiling of tumor-associated macrophages
stringent pass/fail QC may be appropriate for other methods. Notably, Tumor-associated macrophages (TAMs) are implicated in multiple
cell type composition from spatial data also correlated well with stages of tumor progression and have prognostic implications in solid
sc/snRNA-seq across all methods (Pearson’s r ≈ 0.9) and slightly more tumors, including BC45–47. However, their role, diversity and therapeutic
highly with snRNA-seq than scRNA-seq (Extended Data Fig. 8c). This potential remain only partially understood48,49. For example, although
weakly supports snRNA-seq’s capacity to more faithfully represent CD68+ leukocyte density alone was not found to be a prognostic bio-
cell type composition. marker in primary treatment-naive BC, a CD68Hi, CD4Hi, CD8Lo immuno-
To assess each method’s cell or bin/bead-level profiles across sam- profile was associated with reduced overall survival and recurrence-free
ples, for each method (separately), we clustered all profiles, created a survival50, and the presence of TAMs expressing the CD163 scavenger
low-dimensional embedding for visualization and quantified the asso- receptor was associated with adverse prognostic features in BC51. In our
ciation of clusters with patient or cell type using the adjusted Rand data, macrophages were ubiquitous across samples and measurement
index (ARI) (Fig. 4a,b and Supplementary Figs. 1d, 2d, 3d, 4d and 5d). methods; their variable frequency across samples in our sc/sn composi-
sc/snRNA-seq and cell-segmented MERFISH grouped primarily by cell tion analysis was highly explained by the most recent treatment class
type and patient for normal and malignant cells, respectively (Fig. 4a,b). (with immunotherapy being weakly associated with higher macrophage
Conversely, binned or bead-based methods, where profiles are a compos- frequencies) (Fig. 2d–f), and their spatial organization varied between
ite across cells, reflected mostly a malignant cell, patient-specific signal, samples and measurement methods when chosen as the ‘anchor cell’
with less separation between clusters, and lower cell-type-driven separa- (Fig. 4c–f and Supplementary Figs. 1c, 2c, 3c, 4c and 5c).
tion of non-malignant cells, suggesting a dominating signal from preva- Macrophage co-localization phenotypes (Fig. 4c,e) were neither
lent malignant cells. CODEX clusters were also indistinct and mostly specifically enriched nor depleted with expression of CD163, a key
driven by patient, not cell type, possibly related to the antibody panel. macrophage marker, with the three representative samples show-
To assess each method’s capacity to capture local organization, we ing predominantly CD163+ macrophages (Fig. 4f). Moreover, most
quantified, for each method, the co-localization of each cell type (as an (73–93%) macrophages in the other biopsies profiled by MERFISH
‘anchor cell’) versus all other cell types within 50 μm, showing consist- were also CD163+, with few intermixing CD163− macrophages
ency across methods (Supplementary Figs. 1c, 2c, 3c, 4c and 5c). To (Fig. 4f and Extended Data Fig. 9a). In the two notable exceptions
assess a broader distance range of 0–500 μm and systematically com- (878 and 880), most macrophages were CD163− (Extended Data Fig. 9a).
pare methods, we focused on macrophages, as they are present in most Due to methodological limitations, these observations were only
samples and are captured well by all methods. In general, Slide-seq, possible with MERFISH.
MERFISH and CODEX all captured short-range and long-range accumu- To investigate broader macrophage expression states, we inte-
lations and intermixing of macrophages and other cell types similarly grated all observations identified as macrophages using Harmony37
(Fig. 4c–e). ExSeq was often the weakest at capturing accumulation pat- (within each method separately) and clustered them (Fig. 5a and
terns (Fig. 4c). Notably, across all biopsies, macrophages preferentially Extended Data Fig. 9b). Using the same clustering resolution for all
co-localized with other macrophages and weakly avoided malignant methods, we retrieved 4–15 clusters per method (Fig. 5a). Across
cells (Fig. 4e). Visual inspection of macrophage distributions relative all methods, there were two major clusters of highly correlated
to the matching H&E images showed a distinct long-range pattern with method-specific clusters: a CD163+ cluster with high expression of
macrophage islands and more homogenous short-range and intermix- macrophage markers as well as HIF1A and APOE/APOC1 and a CD163−
ing phenotypes (Fig. 4e). cluster associated with lower macrophage marker expression and
Overall, there was relatively high congruence among meth- expression of MKI67 (Extended Data Fig. 9c,d). ExSeq and Slide-seq
ods, but MERFISH showed several benefits: a large profiling area, had much lower signal for macrophage markers overall (Fig. 5a and
clear spatial patterns and clear, sc/snRNA-seq-like clustering of cell Extended Data Fig. 10a), but Slide-seq still showed moderate corre-
profiles. As our MERFISH experiments only measure the expression lation to other methods. MERFISH was the most correlated with sc/
of ~300 genes, we further assessed its ability to detect cell subsets snRNA-seq (ρ = 0.64–0.84; Fig. 5c) and demonstrated a similar pat-
without matching sc/snRNA-seq data. We compared clustering-based tern, with two large clusters along a single continuum (one CD163+,
cell annotations obtained from segmented MERFISH to those from the other CD163−; Fig. 5a) as well as 13 small clusters of approximately
RCTD and TACCO-OT (Extended Data Fig. 8d,e). Although most were in 100 cells each, expressing shared macrophage markers and distinct
agreement, MERFISH-based assignments lacked some granularity (only cluster-defining genes associated with different states or functions,
one endothelial cell label, joint T/NK labels) but captured other distinc- such as ANLN or CDK6 (proliferation), MMP11 (tissue remodeling) or
tions missing in sc/snRNA-seq, including a small cluster of B regulatory FCN1 (angiogenesis)52 (Fig. 5b and Extended Data Fig. 10b). Previous
cells jointly expressing FOXP3 and FCRL5 (Extended Data Fig. 8e). studies of primary BC described APOE-expressing macrophages as
Fig. 6 | Characterizing the cellular neighborhoods of malignant expression within samples, defined as in Fig. 5e, related to b. d, Spatial scatter plots of the
phenotypes across spatial expression profiling methods. a, Dot plots malignant cells within the cell-segmented MERFISH data where each cell is
depicting the log fold change (color) and significance (size) of differences in cell colored as to whether or not it resides in the same 100 × 100-μm bin as at least one
type frequencies between EMT-high and EMT-low neighborhoods (100 × 100-μm T/NK cell. e, Clustered binary heatmaps of whether or not a gene is among the
bins) within each section for MERFISH, Slide-seq and CODEX. ExSeq data did top 10 differentially expressed genes between malignant cells residing close to a
not yield any significant results. Replicates (serial sections) of the same biopsy T/NK cell and those that do not within each biopsy, measured by cell-segmented
are denoted with ‘_1–3’. P values were calculated using a two-sided Wilcoxon test MERFISH. Only genes that occur in at least two samples are shown. Genes are
and Benjamini–Hochberg multiple testing correction. b, Scatter plot relating colored by their directionality in the common differential expression analysis.
the log fold changes of cell type frequency between EMT-high and EMT-low Genes with different directionality between patient-specific and combined
neighborhoods within samples as detected in cell-segmented MERFISH to the analysis show discordant coloring. f, Volcano plot of differential gene expression
corresponding cell type frequency changes detected in the other indicated analysis (two-sided Wilcoxon test, Benjamini–Hochberg correction) between
methods. The significance of differential cell type frequencies was calculated by malignant cells residing close to a T/NK cell and those that do not across all
a two-sided Wilcoxon test and Benjamini–Hochberg correction. The Spearman biopsies, measured by cell-segmented MERFISH data. Genes are colored by their
correlation is indicated; error bands indicate standard error. c, Clustered directionality in the sample-specific differential expression analysis. Genes with
heatmap depicting the pair-wise Spearman correlation of methods based on cell different directionality between patient-specific and combined analysis show
type frequency log fold changes between EMT-high and EMT-low neighborhoods discordant coloring. FC, fold change; man, manual.
Nature Medicine | Volume 30 | November 2024 | 3236–3249 3245

| Article |     |         |     |     |           |     |     |     | https://doi.org/10.1038/s41591-024-03215-z |       |     |     |     |     |
| ------- | --- | ------- | --- | --- | --------- | --- | --- | --- | ------------------------------------------ | ----- | --- | --- | --- | --- |
| a       |     | MERFISH |     |     | Slide-seq |     |     |     |                                            | CODEX |     |     |     |     |
8 1 2 − 8 2 3 9 _ 1
8 1 2 − 8 2 3 9 _ 1 812−8239_2 E M T   h i g h   v s . E M T   lo w
5 1 4 − 6 7 6 0 _ 2 8 1 2 − 8 2 3 9 _ 2 c el l  t y p e   c o m p o si t io n
|            |     |     |     | 5 1 4 − 6 7 6 0 _ 1 |     |     | 514−6760_2 |     |     |     |     |     | change within sections |     |
| ---------- | --- | --- | --- | ------------------- | --- | --- | ---------- | --- | --- | --- | --- | --- | ---------------------- | --- |
| 878−7149_2 |     |     |     | 5 1 4 − 6 7 6 0 _ 2 |     |     |            |     |     |     |     |     |                        |     |
8 8 0 − 7 1 7 9 _ 2 8 7 8 − 7 1 4 9 _ 1 8 78 − 7 1 4 9 _ 2 log F C −log (P adj.)
|      |             |     |     | 8 7 8 − 7 1 4 9 _ 2 |     |     |     |     |     |     |     |     | 2     | 10  |
| ---- | ----------- | --- | --- | ------------------- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- |
| 3 13 | − 9 3 2 _ 1 |     |     |                     |     |     |     |     |     |     |     |     | 1 . 0 | 0   |
8 5 3 − 4 3 8 1 _ 1 8 8 0 − 7 1 7 9 _ 1 8 8 0 − 7 1 79 _ 2 0 . 5 1 0
|            |               |     |     | 8 8 0 − 7 1 7 9 _ 2 |     |     |            |                |     |     |     |     | 0        | 2 0 |
| ---------- | ------------- | --- | --- | ------------------- | --- | --- | ---------- | -------------- | --- | --- | --- | --- | -------- | --- |
| 9 8 2      | − 7 6 2 9 _ 1 |     |     | 3 1 3 − 9 3 2 _ 1   |     |     | 3          | 13 − 9 3 2 _ 1 |     |     |     |     |          |     |
| 9 8 2      | − 7 6 2 9 _ 2 |     |     | 3 1 3 − 9 3 2 _ 2   |     |     |            |                |     |     |     |     | − 0 .5   | 3 0 |
|            |               |     |     |                     |     |     | 85         | 3 − 4 3 8 1_ 1 |     |     |     |     | − 1 .0   | 4 0 |
| 9 1 7      | − 4 5 3 1 _ 2 |     |     | 8 5 3 − 4 3 8 1 _ 1 |     |     |            |                |     |     |     |     |          |     |
| 944−7479_1 |               |     |     | 8 5 3 − 4 3 8 1_ 2  |     |     |            |                |     |     |     |     |          |     |
|            |               |     |     | 9 8 2 − 76 2 9 _ 1  |     |     | 982−7629_2 |                |     |     |     |     | P < 0.05 |     |
| 9 4 4      | − 7 4 7 9 _ 2 |     |     | 9 1 7− 4 53 1_ 2    |     |     |            |                |     |     |     |     | P ≥ 0.05 |     |
| 9 4 4      | − 7 4 7 9 _ 3 |     |     | 9 4 4 − 74 79 _ 1   |     |     | 917−4531_2 |                |     |     |     |     |          |     |
C ke a l a l i c a r s t la r t e g e ocyte MastTNK B lasma C k e a l a l ic la r s t la r t e g e ocyte MastTNK B lasma C ik e ia l a r a l s t la r t e t e g e ocyte MastTNK B lasma
M B m − l i r o n h e l i g e n c u l b la c u o c y h a M B m − l i r o n h e l i g e n sc u b la c u o c y ha M B m − l h e l c u l o i d b la cu e l la o c y ha
t e n e u d o t g i o v a s b r o _v a s p a t r o p M o n B_p t e _n e u d o t g i o v a b r o _v a s p a t r o p M o n B_p t e d o t v a s n u s b r o _v a s S t p a t r o p M o n B_p
MBC_s C _ E n _ a n i a l _ F i c l e H e M a c MBC_s C E n _ a n l i a l _ F i c l e H e M a c MBC _s E n i a l _ l _ s i F i c l e H e M a c
M B e l i a l t h e l  m u s M B e l i a l t h e m u s t h e l e l i a m u s
|     | o t h n d o | t h |     | o t h n d o | t h   |     |     | n d o | o t h t h   |     |     |     |     |     |
| --- | ----------- | --- | --- | ----------- | ----- | --- | --- | ----- | ----------- | --- | --- | --- | --- | --- |
|     | n d E m o   | o   |     | n d E m     | o o   |     |     | E E n | d m o o     |     |     |     |     |     |
|     | E S         |     |     | E S         |       |     |     |       | S           |     |     |     |     |     |
| b   |             |     |     |             |       |     |     |       | c           |     |     |     |     |     |
Spearman correlation of cell type frequency
CODEX ExSeq ExSeq (bin) MERFISH (bin) MERFISH (man) Slide-seq X
|                     |     |     |     |     |     |     |     |     | log | F C ( E M T  h ig | h /lo w ) | DE  | q     | n ) |
| ------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --------- | --- | ----- | --- |
| )wol/hgih TME(CFgol |     |     |     |     |     |     |     |     |     | 2                 |           | C O | s e m | a   |
)dohtem detacidni( 4 rs = 0.338 rs = −0.295 rs = 0.011 rs = 0.67 rs = 0.535 rs = 0.338 1 1 d e- H   (
|     |     |     |     |     |     |     |     |     |     |           |               | 0 . 0 S l | i I S     |               |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------------- | --------- | --------- | ------------- |
|     |     |     |     |     |     |     |     |     |     |           | 1             | − 0       | E R F     | H )           |
|     | 3   |     |     |     |     |     |     |     |     |           | 0 . 0         | 0 . 3     | M I       | S b i n       |
|     |     |     |     |     |     |     |     |     |     | 0         | −             | 9 −       | 5 R F     | H  (          |
|     | 2   |     |     |     |     |     |     |     |     | – 0 . 4   | 0 . 5 7       | 0 . 0 0   | . 2 M E   | IS            |
|     |     |     |     |     |     |     |     |     |     |           | 4 9           | 8 −       |           | E R F         |
|     | 1   |     |     |     |     |     |     |     |     | 0         | . 3 0 . 6     | 0 . 4     | 0 . 0 1   | M             |
|     |     |     |     |     |     |     |     |     |     | 3         | 4             | 9 −       | 9 9       | Se q eq (bin) |
|     |     |     |     |     |     |     |     |     |     | 0 .4      | 0 . 3         | 0 . 4 0   | . 2 0 . 0 | E x           |
| 2   | 0   |     |     |     |     |     |     |     |     |           |               | −         | 0 −       | 3 S           |
|     |     |     |     |     |     |     |     |     |     | 0 . 71 0  | . 3 2 0 . 5 3 | 0 . 6 7   | 0 . 0     | 0 . 2 E x     |
|     | –1  |     |     |     |     |     |     |     |     |           |               |           | − −       |               |
|     |     |     |     |     |     |     |     |     |     | 1.00 1.00 | 1.00          | 1.00 1.00 | 1.00      | 1.00          |
−1 0 1 2 3 −1 0 1 2 3 −1 0 1 2 3 −1 0 1 2 3 −1 0 1 2 3 −1 0 1 2 3 CO Slide-seq M M M E ExSeq (bin)
|     |     |     |     |                       |     |           |          |          |     | DEX | ERFISH (m | E R  | ERFISH (b | x S |
| --- | --- | --- | --- | --------------------- | --- | --------- | -------- | -------- | --- | --- | --------- | ---- | --------- | --- |
|     |     |     |     | logFC(EMT high/low) 2 |     |           |          |          |     |     |           | FISH |           | eq  |
|     |     |     |     | (MERFISH)             |     | Diverging | P < 0.05 | P ≥ 0.05 |     |     |           |      |           |     |
i
|      |     |     |     |     |     |            |     |     |     |     |     | a n |     | n ) |
| ---- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
| d    |     |     |     |     |     |            |     |     |     |     |     | )   |     |     |
| High |     |     |     |     |     | T/NK cells |     |     |     |     |     |     |     | Low |
≥1 T/NK per 100-µm bin
0 T/NK per 100-µm bin
313–932
|     |     |     |     |     | 1 mm |     |     | 917–4531 |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | ---- | --- | --- | -------- | --- | --- | --- | --- | --- | --- |
812–8239
853–4381
|     | 944–7479 1–3 |     |     |     |     | 878–7149 |     |     |     |     |     |     |     |     |
| --- | ------------ | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
982–7629 1–2
|     |     |     |     | 514–6760 |     |     |     |     |     |     |     | 880–7179 |     |     |
| --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- |
| e   |     |     |     |          |     |     |     | f   |     |     |     |          |     |     |
Upregulated in malignant cells close to T/NK cells Upregulated in malignant cells not close to T/NK cells 300 JUN S O X 4
|     |     |     |          |     |     |     |          |                    | HLA C | D74 B2MTTC6   |     |         | ITGA6 N O T C | H1    |
| --- | --- | --- | -------- | --- | --- | --- | -------- | ------------------ | ----- | ------------- | --- | ------- | ------------- | ----- |
|     |     |     | 313–932  |     |     |     | 982–7629 |                    | -B    |               |     |         |               |       |
|     |     |     | 880–7179 |     |     |     | 878–7149 |                    |       |               |     |         | TTYH1         |       |
|     |     |     |          |     |     |     |          | )eulav P detsujda( |       |               |     |         | NDRG2 FGFR2   |       |
|     |     |     | 878–7149 |     |     |     | 880–7179 |                    |       |               |     |         |               |       |
|     |     |     | 982–7629 |     |     |     | 944–7479 |                    |       |               |     |         | ERBB3         |       |
|     |     |     | 812–8239 |     |     |     | 853–4381 |                    | 200   |               |     | AZGP1   | PHGDH         |       |
|     |     |     | 853–4381 |     |     |     | 812–8239 |                    |       |               |     |         |               |       |
|     |     |     |          |     |     |     |          |                    |       | FG F R 1 G AT | A 3 |         |               | LAMA1 |
|     |     |     | 917–4531 |     |     |     | 917–4531 |                    |       | L R P 2 FO X  | A 1 |         |               |       |
|     |     |     | 514–6760 |     |     |     | 313–932  |                    |       |               |     | MYO10   | ELF5          |       |
|     |     |     | 944–7479 |     |     |     | 514–6760 |                    |       |               |     | B CL2   |               |       |
|     |     |     |          |     |     |     |          | 01                 | 100   |               |     | TMSB1 0 | CD44 SOX10    |       |
E-ALH 81TRK 47DC 1BPSH 1CUM M2B 1HDC ARD-ALH 8TRK 1PGZA 2BBRE B-ALH 6CTT 51GSI 7TRK 1PBX 01BSMT FEDPS 4XOS 42DC MACPE 1RFGF MIV 1PBX 1CPBAP AKRUA 1DNCC 1AXOF 3ATAG 5PBFGI NUJ 2PRL HPLM 6LYM 91TRK 6A93CLS AC3KIP 1NMTS 1NAPST gol– H L A - DRA H L A-E ST M N 1 EIF 3 E
|     |     |     |     |     |     |     |     |     |     | HLA       | - C  | K R T 8 | K M I T Y B ESR1 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | ---- | ------- | ---------------- | --- |
|     |     |     |     |     |     |     |     |     |     | H L A - A | MYL6 | FOXC1   | T FF1            |     |
0
|                                                         |     |     |     |     |     |     |     |                          |                           | –2 –1 | 0                  | 1   | 2                             | 3    |
| ------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------------------------ | ------------------------- | ----- | ------------------ | --- | ----------------------------- | ---- |
|                                                         |     |     |     |     |     |     |     | Upregulated in malignant |                           |       | log(fold change) 2 |     | Upregulated in malignant      |      |
|                                                         |     |     |     |     |     |     |     |                          | cells close to T/NK cells |       |                    |     | cells not close to T/NK cells |      |
| Nature Medicine | Volume 30 | November 2024 | 3236–3249 |     |     |     |     |     |     |     |                          |                           |       |                    |     |                               | 3246 |

Article https://doi.org/10.1038/s41591-024-03215-z
lipid-associated macrophages (LAMs), comprising up to 30–40% of all limits the statistical power for analyses of clinicopathologic subsets,
myeloid cells17. In our MERFISH data, the fraction of APOE-expressing and unique aspects of individual methods could not always be rep-
macrophages varied from 24% to 85% of all macrophages (mean, 48%). resented, including ExSeq’s nanometer resolution and Slide-seq’s
potential for decomposed analysis. Nevertheless, in addition to
Spatial interaction and expression phenotypes providing insight into the architecture of MBC—including cell
We examined the spatial organization of malignant cells considering types, expression programs and their spatial relationships—and
their expression of the EMT program initially identified with scRNA-seq practical comparison across methods, we also leveraged the dataset to
(Extended Data Fig. 6a). We observed intra-patient and inter-patient explore sources of heterogeneity and spatial expression phenotypes.
variability in EMT signals among the malignant cells across all methods On a technical level, profiling method contributed to observed
(Fig. 5d). Although cells from samples with low and high EMT scores expression variability, including in key genes such as ESR1 and TRPS1,
showed little variation of EMT scores across space, intermediate scor- a finding with implications for marker gene-based approaches. Among
ing samples showed patches of high-scoring cells (Fig. 5e, segmented single-cell methods, snRNA-seq not only captured epithelial and stro-
MERFISH data), suggesting a spatially determined component. mal cells more efficiently but also more closely matched spatial data.
We partitioned the samples across three spatial EMT phenotypes— ComBat performed well for platform correction on a pseudobulk level,
EMT-low, EMT-patched and EMT-high—and identified genes that were dif- and Harmony integrated the data well at the single-cell level.
ferentially expressed between malignant cells in tumors from the three Spatial profiling methods generally showed high agreement,
spatial EMT phenotypes (Fig. 5f). EMT-patched and EMT-high pheno- and all recovered co-localization patterns within their profiling areas.
types were each characterized by distinct cell cycle genes (EMT-patched: ExSeq diverged the most from other methods, although local cell type
CCND1, RB1 and NF1; EMT-high: CDC20); EMT-low samples were further frequencies were still similar. MERFISH performed particularly favora-
characterized by AGR2, a potential biomarker of poor prognosis53,54. bly in terms of separable, single-cell molecular profiles and faithfully
The differential expression changes between EMT-patched and recovered patient-specific expression signals as the primary driver of
EMT-high phenotypes were largely congruent across MERFISH, malignant, but not non-malignant, cell-intrinsic variability.
Slide-seq and sc/snRNA-seq but not CODEX or ExSeq (Fig. 5g,h). The malignant compartment was characterized by substantial
EMT-high (> sample median) and EMT-low (< sample median) inter-patient heterogeneity but still revealed intriguing patterns:
local neighborhoods (100 × 100-μm bins) showed differences in cell basal-like biopsies formed a highly correlated exclusive subcluster;
type composition (Fig. 6a). Across all samples and methods (except EMT programs were robust among single-cell methods and demon-
ExSeq—no significant enrichments), malignant cells were depleted and strated inter-patient and intra-patient heterogeneity in three spatial
fibroblasts were enriched in EMT-high neighborhoods (Fig. 6a). Interest- phenotypes, complementing prior studies of EMT marker expression
ingly, in EMT-high neighborhoods of sample 917 (the one sample with heterogeneity both within primary BC56 and between matched primary
stem-like and non-stem-like malignant cells), stem-like malignant cells and metastatic biopsies57; and patient-specific CNA profiles and expres-
were depleted and non-stem-like malignant cells were slightly enriched sion programs were maintained across time, site and even changes in
(Fig. 6a; MERFISH and CODEX but not Slide-seq). Myeloid and lymphoid receptor subtypes, in contrast to prior orthogonal studies of genomic
cell types showed mostly sample-specific enrichments (Fig. 6a). Overall, evolution and diversity through disease progression and metastasis58–60.
replicate sections (Fig. 6a) and all methods except ExSeq showed rela- In the immune compartment, macrophages were the most fre-
tively good agreement (0.32 < ρ < 0.68) in terms of cell type composition quent cell type, although their frequency was influenced by the most
differences between EMT-low and EMT-high neighborhoods (Fig. 6b,c). recent treatment class and specifically increased with prior immu-
To recover spatial patterns related to interactions between malig- notherapy. Across methods, we identified two macrophage states
nant and lymphoid cells, we tested if differences in malignant cell characterized by CD163/CD68/APOE/HIF1A and MKI67, respectively.
expression profiles are associated with differences in their proximity Although APOE expression was reported to promote T cell effector
to T/NK cells (Methods). T/NK+ 100 × 100-μm bins generally formed functions61, we did not find a significant spatial correlation between
patches, regardless of the overall level of T/NK infiltration (Fig. 6d). expression of APOE in macrophages and PDCD1 or CTLA4 in T/NK cells.
Malignant cells in T/NK+ bins showed higher expression of MHC-I and While macrophages were ubiquitous, they weakly avoided malignant
MHC-II genes (HLA-E, CD74, B2M, HLA-DRA and HLA-B), as expected, cells; T/NK cells showed more variable infiltration levels. Notably,
but also luminal epithelial genes (KRT8, KRT18 and MUC1) and ISG15 T/NK localization relative to malignant cells was associated with
(Fig. 6e). On the other hand, genes upregulated in malignant cells in expression patterns in malignant cells— co-localization with higher
the T/NK− bins included SOX4 (in six of nine biopsies), consistent with expression of MHC components; exclusion with increased SOX4—
the association of SOX4 expression with lower CD8+ T cell infiltra- expanding on previous studies linking SOX4 expression to immune
tion in primary TNBC55. Thus, SOX4-expressing malignant cells that evasion in primary TNBC55. Future work will further investigate the
seemingly avoid T/NK contact coexist in the same biopsies with malig- molecular underpinnings of these cell states and spatial interactions
nant cells that engage in T/NK cell interactions. These patterns were and their translational significance.
also observed when analyzing malignant cells across all metastases
jointly (Fig. 6f), as were additional key genes (for example, GATA3 and Online content
FOXA1 in T/NK+ regions; TMSB10 and AZGP1 in T/NK− regions) that were Any methods, additional references, Nature Portfolio reporting sum-
recovered in different categories compared to the patient-specific maries, source data, extended data, supplementary information,
analysis. Thus, although combining different biopsies can increase acknowledgements, peer review information; details of author con-
the power to detect common signals, patient-specific signals might tributions and competing interests; and statements of data and code
be lost or even interpreted inversely. availability are available at https://doi.org/10.1038/s41591-024-03215-z.
Discussion References
We generated an integrated atlas of MBC based on single-cell and spatial 1. Egeblad, M., Nakasone, E. S. & Werb, Z. Tumors as organs: complex
expression profiling of 67 core needle biopsies from 60 patients. Span- tissues that interface with the entire organism. Dev. Cell 18,
ning the clinical and molecular heterogeneity of MBC and incorporating 884–901 (2010).
a careful experimental design that enables comparison across methods 2. Fridman, W. H., Zitvogel, L., Sautès-Fridman, C. & Kroemer, G. The
provide opportunities for advances across BC research as well as immune contexture in cancer prognosis and treatment. Nat. Rev.
method and algorithm development. This breadth-centered approach Clin. Oncol. 14, 717–734 (2017).
Nature Medicine | Volume 30 | November 2024 | 3236–3249 3247

Article https://doi.org/10.1038/s41591-024-03215-z
3. El Bairi, K. et al. The tale of TILs in breast cancer: a report from 27. Chen, A. et al. Reduction in migratory phenotype in a metastasized
The International Immuno-Oncology Biomarker Working Group. breast cancer cell line via downregulation of S100A4 and GRM3.
NPJ Breast Cancer 7, 150 (2021). Sci. Rep. 7, 3459 (2017).
4. Rao, A., Barkley, D., França, G. S. & Yanai, I. Exploring tissue 28. Westbrook, J. A. et al. Identification and validation of DOCK4 as
architecture using spatial transcriptomics. Nature 596, 211–220 a potential biomarker for risk of bone metastasis development in
(2021). patients with early breast cancer. J. Pathol. 247, 381–391 (2019).
5. Moses, L. & Pachter, L. Museum of spatial transcriptomics. 29. Pelka, K. et al. Spatially organized multicellular immune hubs in
Nat. Methods 19, 534–546 (2022). human colorectal cancer. Cell 184, 4734–4752 (2021).
6. Rozenblatt-Rosen, O. et al. The Human Tumor Atlas Network: 30. Welch, J. D. et al. Single-cell multi-omic integration compares and
charting tumor transitions across space and time at single-cell contrasts features of brain cell identity. Cell 177, 1873–1887 (2019).
resolution. Cell 181, 236–249 (2020). 31. Cejalvo, J. M. et al. Intrinsic subtypes and gene expression
7. Goltsev, Y. et al. Deep profiling of mouse splenic architecture with profiles in primary and metastatic breast cancer. Cancer Res. 77,
CODEX multiplexed imaging. Cell 174, 968–981 (2018). 2213–2221 (2017).
8. Black, S. et al. CODEX multiplexed tissue imaging with 32. Aftimos, P. et al. Genomic and transcriptomic analyses of breast
DNA-conjugated antibodies. Nat. Protoc. 16, 3802–3835 (2021). cancer primaries and matched metastases in AURORA, the Breast
9. Alon, S. et al. Expansion sequencing: spatially precise in situ International Group (BIG) molecular screening initiative. Cancer
transcriptomics in intact biological systems. Science 371, Discov. 11, 2796–2811 (2021).
eaax2656 (2021). 33. Jain, E. et al. The Metastatic Breast Cancer Project: leveraging
10. Chen, K. H., Boettiger, A. N., Moffitt, J. R., Wang, S. & Zhuang, X. patient-partnered research to expand the clinical and genomic
RNA imaging. Spatially resolved, highly multiplexed RNA profiling landscape of metastatic breast cancer and accelerate discoveries.
in single cells. Science 348, aaa6090 (2015). Preprint at bioRxiv https://doi.org/10.1101/2023.06.07.23291117
11. Moffitt, J. R. et al. High-throughput single-cell gene-expression (2023).
profiling with multiplexed error-robust fluorescence in situ 34. Curtis, C. et al. The genomic and transcriptomic architecture
hybridization. Proc. Natl Acad. Sci. USA 113, 11046–11051 (2016). of 2,000 breast tumours reveals novel subgroups. Nature 486,
12. Moffitt, J. R. et al. High-performance multiplexed fluorescence 346–352 (2012).
in situ hybridization in culture and tissue with matrix imprinting 35. Bhattacharya, A. et al. Transcriptional effects of copy number altera-
and clearing. Proc. Natl Acad. Sci. USA 113, 14456–14461 (2016). tions in a large set of human cancers. Nat. Commun. 11, 715 (2020).
13. Rodriques, S. G. et al. Slide-seq: a scalable technology for 36. Johnson, W. E., Li, C. & Rabinovic, A. Adjusting batch effects in
measuring genome-wide expression at high spatial resolution. microarray expression data using empirical Bayes methods.
Science 363, 1463–1467 (2019). Biostatistics 8, 118–127 (2007).
14. Sung, H. et al. Global Cancer Statistics 2020: GLOBOCAN 37. Korsunsky, I. et al. Fast, sensitive and accurate integration of
estimates of incidence and mortality worldwide for 36 cancers in single-cell data with Harmony. Nat. Methods 16, 1289–1296 (2019).
185 countries. CA Cancer J. Clin. 71, 209–249 (2021). 38. Polański, K. et al. BBKNN: fast batch alignment of single cell
15. Slyper, M. et al. A single-cell and single-nucleus RNA-seq toolbox transcriptomes. Bioinformatics 36, 964–965 (2020).
for fresh and frozen human tumors. Nat. Med. 26, 792–802 (2020). 39. Cui, Y. et al. Metastasis-associated protein 2 is a repressor of
16. Eraslan, G. et al. Single-nucleus cross-tissue molecular reference estrogen receptor α whose overexpression leads to estrogen-
maps toward understanding disease gene function. Science 376, independent growth of human breast cancer cells. Mol. Endocrinol.
eabl4290 (2022). 20, 2020–2035 (2006).
17. Wu, S. Z. et al. A single-cell and spatially resolved atlas of human 40. Morita, T. & Hayashi, K. Tumor progression is mediated by
breast cancers. Nat. Genet. 53, 1334–1347 (2021). thymosin-β4 through a TGFβ/MRTF signaling axis. Mol. Cancer Res.
18. Bae, S. Y. et al. The prognoses of metaplastic breast cancer 16, 880–893 (2018).
patients compared to those of triple-negative breast cancer 41. Cha, H.-J., Jeong, M.-J. & Kleinman, H. K. Role of thymosin β4
patients. Breast Cancer Res. Treat. 126, 471–478 (2011). in tumor metastasis and angiogenesis. J. Natl Cancer Inst. 95,
19. Lan, T. et al. The role of adjuvant chemotherapy in metaplastic 1674–1680 (2003).
breast carcinoma: a competing risk analysis of the SEER database. 42. Wijshake, T. et al. Tumor-suppressor function of Beclin 1 in breast
Front. Oncol. 11, 572230 (2021). cancer cells requires E-cadherin. Proc. Natl Acad. Sci. USA 118,
20. Wong, W. et al. Poor response to neoadjuvant chemotherapy in e2020478118 (2021).
metaplastic breast carcinoma. NPJ Breast Cancer 7, 96 (2021). 43. Cable, D. M. et al. Robust decomposition of cell type mixtures in
21. Joneja, U. et al. Comprehensive profiling of metaplastic breast spatial transcriptomics. Nat. Biotechnol. 40, 517–526 (2022).
carcinomas reveals frequent overexpression of programmed 44. Mages, S. et al. TACCO unifies annotation transfer and
death-ligand 1. J. Clin. Pathol. 70, 255–259 (2017). decomposition of cell identities for single-cell and spatial omics.
22. Adams, S. et al. A multicenter phase II trial of ipilimumab and Nat. Biotechnol. 41, 1465–1473 (2023).
nivolumab in unresectable or metastatic metaplastic breast cancer: 45. Zhang, Q.-W. et al. Prognostic significance of tumor-associated
cohort 36 of dual anti-CTLA-4 and anti-PD-1 blockade in rare tumors macrophages in solid tumor: a meta-analysis of the literature.
(DART, SWOG S1609). Clin. Cancer Res. 28, 271–278 (2022). PLoS ONE 7, e50946 (2012).
23. Guise, T. A. et al. Evidence for a causal role of parathyroid 46. Pittet, M. J., Michielin, O. & Migliorini, D. Clinical relevance of tumour-
hormone-related protein in the pathogenesis of human breast associated macrophages. Nat. Rev. Clin. Oncol. 19, 402–421 (2022).
cancer-mediated osteolysis. J. Clin. Invest. 98, 1544–1549 (1996). 47. Cassetta, L. & Pollard, J. W. A timeline of tumour-associated
24. Kang, Y. et al. A multigenic program mediating breast cancer macrophage biology. Nat. Rev. Cancer 23, 238–257 (2023).
metastasis to bone. Cancer Cell 3, 537–549 (2003). 48. Mantovani, A., Marchesi, F., Malesci, A., Laghi, L. & Allavena, P.
25. Jones, D. H. et al. Regulation of cancer cell migration and bone Tumour-associated macrophages as treatment targets in
metastasis by RANKL. Nature 440, 692–696 (2006). oncology. Nat. Rev. Clin. Oncol. 14, 399–416 (2017).
26. Johnson, R. W. et al. Induction of LIFR confers a dormancy 49. Mantovani, A., Allavena, P., Marchesi, F. & Garlanda, C.
phenotype in breast cancer cells disseminated to the bone Macrophages as tools and targets in cancer therapy. Nat. Rev.
marrow. Nat. Cell Biol. 18, 1078–1089 (2016). Drug Discov. 21, 799–820 (2022).
Nature Medicine | Volume 30 | November 2024 | 3236–3249 3248

Article https://doi.org/10.1038/s41591-024-03215-z
50. DeNardo, D. G. et al. Leukocyte complexity predicts breast cancer 59. Razavi, P. et al. The genomic landscape of endocrine-resistant
survival and functionally regulates response to chemotherapy. advanced breast cancers. Cancer Cell 34, 427–438 (2018).
Cancer Discov. 1, 54–67 (2011). 60. De Mattos-Arruda, L. et al. The genomic and immune landscapes
51. Mehta, A. K., Kadel, S., Townsend, M. G., Oliwa, M. & Guerriero, J. L. of lethal metastatic breast cancer. Cell Rep. 27, 2690–2708
Macrophage biology and mechanisms of immune suppression in (2019).
breast cancer. Front. Immunol. 12, 643771 (2021). 61. Tavazoie, M. F. et al. LXR/ApoE activation restricts innate immune
52. Ma, R.-Y., Black, A. & Qian, B.-Z. Macrophage diversity in cancer suppression in cancer. Cell 172, 825–840 (2018).
revisited in the era of single-cell omics. Trends Immunol. 43,
546–563 (2022). Publisher’s note Springer Nature remains neutral with regard
53. Tian, S.-B. et al. The prognostic value of AGR2 expression in solid to jurisdictional claims in published maps and institutional
tumours: a systematic review and meta-analysis. Sci. Rep. 7, affiliations.
15500 (2017).
54. Hrstka, R. et al. The pro-metastatic protein anterior gradient-2 Open Access This article is licensed under a Creative Commons
predicts poor prognosis in tamoxifen-treated breast cancers. Attribution 4.0 International License, which permits use, sharing,
Oncogene 29, 4838–4847 (2010). adaptation, distribution and reproduction in any medium or format,
55. Bagati, A. et al. Integrin αvβ6–TGFβ–SOX4 pathway drives as long as you give appropriate credit to the original author(s) and the
immune evasion in triple-negative breast cancer. Cancer Cell 39, source, provide a link to the Creative Commons licence, and indicate
54–67 (2021). if changes were made. The images or other third party material in this
56. Brown, M. S. et al. Phenotypic heterogeneity driven by plasticity article are included in the article’s Creative Commons licence, unless
of the intermediate EMT state governs disease progression and indicated otherwise in a credit line to the material. If material is not
metastasis in breast cancer. Sci. Adv. 8, eabj8002 (2022). included in the article’s Creative Commons licence and your intended
57. Grasset, E. M. et al. Triple-negative breast cancer metastasis use is not permitted by statutory regulation or exceeds the permitted
involves complex epithelial-mesenchymal transition dynamics use, you will need to obtain permission directly from the copyright
and requires vimentin. Sci. Transl. Med. 14, eabn7571 (2022). holder. To view a copy of this licence, visit http://creativecommons.
58. Brown, D. et al. Phylogenetic analysis of metastatic progression org/licenses/by/4.0/.
in breast cancer using somatic mutations and copy number
aberrations. Nat. Commun. 8, 14944 (2017). © The Author(s) 2024, corrected publication 2025
Johanna Klughammer 1,24,29 , Daniel L. Abravanel 2,3,29 , Åsa Segerstolpe1,29, Timothy R. Blosser 4,29,
Yury Goltsev 5,29, Yi Cui6, Daniel R. Goodwin6, Anubhav Sinha6, Orr Ashenberg1, Michal Slyper1, Sébastien Vigneau7,
Judit Jané‐Valbuena1, Shahar Alon6,8, Chiara Caraccio 5, Judy Chen7, Ofir Cohen2,9,25, Nicole Cullen 10,
Laura K. DelloStritto7, Danielle Dionne1, Janet Files2, Allison Frangieh7, Karla Helvie7, Melissa E. Hughes2, Stephanie Inga7,
Abhay Kanodia7, Ana Lako10, Colin MacKichan7, Simon Mages 1,24, Noa Moriel11, Evan Murray9, Sara Napolitano7,
Kyleen Nguyen2, Mor Nitzan 11,12,13, Rebecca Ortiz7, Miraj Patel7, Kathleen L. Pfaff10, Caroline B. M. Porter1, Asaf Rotem7,26,
Sarah Strauss2, Robert Strasser24, Aaron R. Thorner7, Madison Turner10,27, Isaac Wakiro 7, Julia Waldman1, Jingyi Wu7,
Jorge Gómez Tejeda Zañudo 2,9, Diane Zhang9, Nancy U. Lin 2, Sara M. Tolaney 2, Eric P. Winer2,
Edward S. Boyden 14,15,16,17,18,19,30, Fei Chen 9,20,30, Garry P. Nolan5,30, Scott J. Rodig10,21,22,30, Xiaowei Zhuang4,17,23,30,
Orit Rozenblatt-Rosen1,28,30, Bruce E. Johnson2,3,7,30, Aviv Regev1,28,30 & Nikhil Wagle 2,3,7,9,28,30
1Klarman Cell Observatory, Broad Institute of Harvard and MIT, Cambridge, MA, USA. 2Department of Medical Oncology, Dana-Farber Cancer Institute,
Boston, MA, USA. 3Harvard Medical School, Boston, MA, USA. 4Department of Chemistry and Chemical Biology, Harvard University, Cambridge, MA,
USA. 5Baxter Laboratory in Stem Cell Biology, Department of Microbiology and Immunology, Stanford University School of Medicine, Stanford, CA,
USA. 6Department of Media Arts and Sciences, McGovern Institute, Massachusetts Institute of Technology, Cambridge, MA, USA. 7Center for Cancer
Genomics, Dana-Farber Cancer Institute, Boston, MA, USA. 8Faculty of Engineering, Gonda Brain Research Center and Institute of Nanotechnology,
Bar-Ilan University, Ramat Gan, Israel. 9Broad Institute of Harvard and MIT, Cambridge, MA, USA. 10Center for Immuno-Oncology, Dana-Farber Cancer
Institute, Boston, MA, USA. 11School of Computer Science and Engineering, The Hebrew University of Jerusalem, Jerusalem, Israel. 12Racah Institute
of Physics, The Hebrew University of Jerusalem, Jerusalem, Israel. 13Faculty of Medicine, The Hebrew University of Jerusalem, Jerusalem, Israel.
14Department of Media Arts and Sciences, Massachusetts Institute of Technology, Cambridge, MA, USA. 15Department of Biological Engineering,
Massachusetts Institute of Technology, Cambridge, MA, USA. 16Department of Biology, Koch Institute for Integrative Cancer Research, Massachusetts
Institute of Technology, Cambridge, MA, USA. 17Howard Hughes Medical Institute, Chevy Chase, MD, USA. 18Department of Brain and Cognitive Sciences,
Massachusetts Institute of Technology, Cambridge, MA, USA. 19K. Lisa Yang Center for Bionics, Massachusetts Institute of Technology, Cambridge, MA,
USA. 20Department of Stem Cell and Regenerative Biology, Harvard University, Cambridge, MA, USA. 21Department of Pathology, Brigham and Women’s
Hospital, Boston, MA, USA. 22Department of Pathology, Dana-Farber Cancer Institute, Boston, MA, USA. 23Department of Physics, Harvard University,
Cambridge, MA, USA. 24Present address: Gene Center and Department of Biochemistry, Ludwig Maximilians Universität München, Munich, Germany.
25Present address: Department of Microbiology, Immunology and Genetics, Faculty of Health Sciences, Ben-Guiron University, Beersheba, Israel.
26Present address: AstraZeneca R&D, Boston, MA, USA. 27Present address: Department of Microbiology, Immunology, and Cancer Biology,
University of Virginia, Charlottesville, VA, USA. 28Present address: Genentech, Inc., South San Francisco, CA, USA. 29These authors contributed equally:
Johanna Klughammer, Daniel L. Abravanel, Åsa Segerstolpe, Timothy R. Blosser, Yury Goltsev. 30These authors jointly supervised this work:
Edward S. Boyden, Fei Chen, Garry P. Nolan, Scott J. Rodig, Xiaowei Zhuang, Orit Rozenblatt-Rosen, Bruce E. Johnson, Aviv Regev, Nikhil Wagle.
e-mail: klughammer@genzentrum.lmu.de; daniel_abravanel@dfci.harvard.edu; regev.aviv@gene.com; wagle.nikhil@gene.com
Nature Medicine | Volume 30 | November 2024 | 3236–3249 3249

Article https://doi.org/10.1038/s41591-024-03215-z
Methods spin setting with centrifugal force ramping up to, but not exceeding,
Ethics statement 11,000g. This procedure was repeated up to three times until the pellet
All samples included in this study were voluntarily donated by patients was no longer red or pink. To remove cell clumps, the pellet was
who provided informed consent under an institutional review board resuspended in 100 μl of TrypLE (Life Technologies, 12604013) and
(IRB)-approved protocol (DF/HCC no. 05-246), which includes permis- incubated while constantly pipetting at room temperature for 1 min
sion for sample acquisition, clinical data abstraction, sample analysis with a 200-μl pipette tip. TrypLE was inactivated by adding 200 μl
and data sharing. Analysis of biospecimens at the Broad Institute was of cold RPMI 1640 with 10% FBS. The cells were pelleted using short
performed under Broad Institute protocol number 15-370B. centrifugation as described above. The pellet was resuspended in
50 μl of 0.4% BSA (Ambion, AM2616) in PBS. To assess the single-cell
Sample acquisition, handling and annotation suspension, viability and cell count, 5 μl of Trypan blue (Thermo Fisher
Tissues were collected as described in detail previously15. Clinical anno- Scientific, T10282) was mixed with 5 μl of the sample and loaded onto
tations were generated from the electronic medical record under the an INCYTO C-Chip Disposable Hemocytometer, Neubauer Improved
supervision of a board-certified medical oncologist and a cancer regis- (VWR, 82030-468). The cell concentration was adjusted if necessary
trar following HTAN clinical data standards (https://humantumoratlas. to a range of 200–2,000 cells per microliter. A total of 8,000 cells were
org/standard/clinical), which are based on the National Cancer Institute loaded into each channel of the 10x Genomics Single Cell Chromium
Genomic Data Commons model (https://gdc.cancer.gov/about-data/ Controller for the Chromium Single Cell 3′ Library (V2 or V3) per the
gdc-data-processing/clinical-data-standardization). manufacturer’s instructions (10x Genomics).
For snRNA-seq and spatial expression assays, core needle biop-
sies were either snap frozen or frozen in optimal cutting temperature 10x library generation and sequencing
(OCT) compound (Tissue-Tek, Sakura) to preserve. Cores were pre- Single cells and nuclei were partitioned into droplets with gel beads
coated with OCT by putting a thin layer of OCT down in the cryo- in the Chromium Controller. After emulsions were formed, barcoded
mold before placing an individual core in the center of the OCT mold reverse transcription of RNA took place. This was followed by cDNA
in a straight line and adding additional OCT to fill the cryomold. amplification, fragmentation and adapter and sample index attach-
The cryomold was then placed on dry ice for 5–15 min until the ment, all according to the manufacturer’s recommendations. Librar-
block was opaque before storing it at −80 °C. For scRNA-seq, core ies from four 10x channels were pooled together and sequenced on
needle biopsies were transferred from interventional radiology into one lane of an Illumina HiSeq X, or on one flow cell of a NextSeq, with
DMEM medium and processed upon arrival at the Broad Institute. paired-end reads as follows: read 1, 26 nt; read 2, 55 nt; index 1, 8 nt;
index 2, 0 nt.
Generation of snRNA-seq data
snRNA-seq was performed as described previously15. Specifically, Processing and quality assurance of the sc/snRNA-seq data
frozen tissue was placed on ice and in one well of a plate (STEMCELL Raw sequencing reads were processed using the cellranger_cellbender_
Technologies, 38015), and 1 ml of TST buffer was added to the well. Tis- workflow snapshot 6 on TERRA (https://app.terra.bio/), using the
sue was kept on ice and cut into pieces with Noyes spring scissors (Fine human genome GRCh38 as reference and retaining intronic reads for
Science Tools, 15514-12) for 10 min. Tissue mixture was filtered through snRNA-seq but not for scRNA-seq. This workflow featured Cell Ranger
a 40-μm Falcon cell strainer (Thermo Fisher Scientific, 08-771-1). The version 3.0.2 and Cell Bender version 0.1.0. An initial processing of the
well was washed and filtered with 1 ml of detergent buffer solution, resulting count matrices, including quality assessment and automated
and 3 ml of 1× ST buffer was added to a total well volume of 5 ml. The cell type annotation (see below), and doublet detection with scrublet
solution was centrifuged in a 15-ml Eppendorf tube for 5 min at 500g version 0.2.1 was performed individually for each sample using Seurat
and 4 °C in a swinging bucket centrifuge. Pellet was resuspended in 1× version 3.1.162).
ST buffer with a resuspension volume of 100–200 μl based on pellet Quality filtering was performed simultaneously on all sam-
size. The single-nucleus suspension was filtered through a 35-μm Fal- ples, once all samples had been obtained and processed, to obtain
con cell strainer (Corning, 352235). In total, 8,000 (V3) or 10,000 (V2) data-driven quality filtering thresholds to account for biological and
nuclei were selected with a C-chip disposable hemocytometer (VWR, technical differences between samples. For example, immune cells
82030-468) and transferred to Chromium chips for the Chromium that tend to contain less RNA than malignant cells were filtered with
Single Cell 3′ Library (V2 or V3) per the manufacturer’s instructions more lenient thresholds.
(10x Genomics). Following this rationale, low-quality cells were filtered out based
on low or extremely high unique molecular identifier (UMI) counts, low
Generation of scRNA-seq data gene counts and high mitochondrial read contributions in a manner
scRNA-seq was performed as described previously15. Specifically, sam- dependent on cell type, protocol and chemistry (V2/V3).
ples were washed in cold PBS and transferred into a 2-ml Eppendorf The following algorithm was used to determine the thresholds
tube containing dissociation mixture (950-μl volume of RPMI 1640 for each filter group:
(Thermo Fisher Scientific, 11875093) + 10 μl of 10 mg ml−1 DNAse I High threshold filter: mitochondrial genes <50%, number of genes
(Sigma Aldrich, 11284932001) + 40 μl of 2.5 mg ml−1 Liberase (Sigma <8,000, number of UMIs <20,000.
Aldrich, 5401127001)). Next, the sample was minced in the Eppendorf Low threshold filter for genes per cell: If the median number of
tube using spring scissors (Fine Science Tools, 15514-12) into fragments genes per cell in the filter group of a given cell is >1,300, then cells with
less than approximately 0.4 mm and incubated at 37 °C while rotating >700 genes are retained; if the group median is <1,300 and >600, then
horizontally at approximately 14 r.p.m. for 10 min, followed by pipet- cells with >300 genes are retained; if the group median is <600, then
ting the sample 20 times with a 1-ml pipette tip at room temperature. cells with >100 genes are retained.
The incubation and pipetting were repeated a second time before Low threshold filter for UMIs per cell: If the median number of
transfer to a 1.7-ml Eppendorf tube and centrifugation at 300–580g UMIs per cell in the filter group of a given cell is >1,800, then cells with
for 4–7 min at 4 °C. The pellet was then resuspended in 200–500 μl >1,100 UMIs are retained; if the group median is <1,800 and >900, then
of ammonium–chloride–potassium (ACK) RBC lysis buffer (Thermo cells with >600 UMIs are retained; if the group median is <900, then
Fisher Scientific, A1049201) and incubated for 1 min on ice, followed cells with >300 UMIs are retained.
by the addition of cold PBS at twice the volume of the ACK. The cells Samples with extremely low numbers of recovered cells were
were pelleted by a short centrifugation for 8 s at 4 °C using the short excluded as failed.
Nature Medicine

Article https://doi.org/10.1038/s41591-024-03215-z
Cell type annotation in sc/snRNA-seq data. We ran this analysis separately for snRNA-seq and scRNA-seq data,
In an initial automated and sample-wise annotation, cells were anno- setting the k parameter to 20 to receive 20 expression programs and the
tated using the R package SingleR version 1.0.3 (https://bioconductor. lambda parameter to 40 to ensure sufficient integration and separation
org/packages/release/bioc/html/SingleR.html) with both its built-in of sample-specific signals. These parameters were found empirically.
reference datasets (HPCA and Blueprint) in a cell-wise and cluster-wise The thus-obtained 40 expression programs were then correlated by
annotation scheme, and annotations were then refined by harmonizing pair-wise Pearson correlation based on the gene importance for the
labels across the reference dataset and within clusters. respective programs as represented in the feature matrix W. This way,
After combining all snRNA-seq or scRNA-seq samples into one we were able to identify corresponding programs in the sc/snRNA-seq
anndata object each, as well as joint processing using the SCANPY data as highly correlated programs.
version 1.7.2 workflow, including normalization, log1p transformation,
scaling, highly variable gene selection, regression of total counts and Scoring of expression programs in sc/snRNA-seq and spatial
mitochondrial counts, principal component analysis (PCA), nearest data
neighbor finding, Leiden clustering and two-dimensional (2D) projec- Expression programs defined by specific sets of genes were performed
tion using uniform manifold approximation and projection (UMAP), using either Seurat’s version 3.1.1 or SCANPY’s version 1.7.2 built-in
the initial automated annotation was further refined using the context functions AddModuleScore or score_genes, respectively, with default
of all sc/snRNA-seq samples, respectively. parameters. Seurat was used to score the subcell-type marker genes17
Single cells that were annotated with a cell type label that was not as well as the hallmark gene sets in the Molecular Signatures Data-
compatible with their cluster’s annotation were removed as unreli- base (MSigDB)65,66, and SCANPY version 1.7.2 was used to score the
able. Clearly distinct clusters that were annotated with the same cell scRNA-seq-derived iNMF EMT program genes (IGFBP7, SPARC, COL1A2,
type label were investigated in detail using marker genes and assigned COL4A1, COL3A1, BGN, ACTA2, FN1, COL4A2, TAGLN, DCN, COL1A1, LUM,
more specific cell type labels. For a simplified annotation, all cells then COL6A3, POSTN, AEBP1, COL6A2, VIM, TIMP1, TPM2, COL5A1, CALD1,
received a second label based on their cell type label to be assigned COL6A1, A2M, SPARCL1, THY1, VCAN, CCN2, GNG11, PDGFRB, RGS5,
to one of the four compartments: malignant, stromal, myeloid and ITGA1, MYL9, COL5A2, COL18A1, THBS2, IGHA1, CAVIN1, ELN, NID1,
lymphoid. LHFPL6, APOE, IGLC3, HSPG2, CAV1, TCF4, NNMT, ASPN, FSTL1 and
MGP), of which 20 genes are represented in MERFISH and ExSeq (TCF4,
CNA in the sc/snRNA-seq data COL4A1, BGN, COL1A2, FN1, COL1A1, ACTA2, MYL9, HSPG2, TIMP1, VIM,
CNAs in the sc/snRNA-seq were scored using InferCNV version 1.2.0 THY1, APOE, COL3A1, DCN, LUM, TAGLN, TPM2, GNG11 and COL4A2)
(https://github.com/broadinstitute/inferCNV). Sample-wise analy- and three in CODEX (VIM, THY1 and COL4A2). Scoring was performed
sis was performed by assigning the following cell types as normal on all samples profiled with a given method. The choice of which tool
reference—T cells, NK cells, monocytes, macrophages, fibroblasts and to use was based purely on the environment (R versus Python) that
endothelial cells—and calling CNAs in all other cell types. In particular, the respective analysis branches were performed in.
we did not include hepatocytes as reference cells because they are
known to be polyploid and B/plasma cells because of disproportion- Integration of sc/snRNA-seq data or spatial data on a
ately high expression of certain genes related to antibody production. pseudobulk or single-cell/bead/bin level
The cross-sample combined analysis was performed by select- To compare malignant pseudobulk expression profiles, the pseudobulk
ing normal (non-malignant) reference cells across all samples in an expression matrix was corrected for profiling method effects using
even manner and calling CNAs in all malignant cells across all samples the ComBat function from the R package sva version 3.34.0 (ref. 67),
separately for the snRNA-seq and scRNA-seq data. InferCNV’s built-in with profiling method as batch variable and receptor status as well as
CNA heatmap was then assessed for interesting patterns and used for biopsy site as covariates.
presentation. To integrate snRNA-seq and scRNA-seq data at the single-cell level,
the function ‘harmonize’ from the Python package Harmony-pytorch
Variance analysis in the sc/snRNA-seq data version 0.1.4 (ref. 37) and SCANPY’s BBKN wrapper (external.pp.bbknn)
Variance analysis in the sc/snRNA-seq data was performed using the based on the Python package BBKNN version 1.5.1 (ref. 38) were used.
R package variancePartition version 1.14.0 (ref. 63), which uses linear Each function was run with profiling method as batch variable and
mixed models to quantify variation in gene expression that can be default parameters otherwise. After integration, Leiden clustering
attributed to different biological or technical variables (patient ID (indi- was performed using the SCANPY function ‘leiden’ with a resolution
vidual), method (sc/sn), site, most recent treatment class, histology, of 0.4. The integrated dataset was only used to demonstrate data inte-
metastatic presentation and receptor status). Apart from using this gration but not for other analyses. (These methods do not correct the
tool for the study of expression variability in pseudobulk data (average expression matrix but align the observations in a lower-dimensional
expression across all cells per sample and compartment), we also used space (Harmony: PCA; BBKNN: k-nearest neighbor graph)).
it to assess variability in cell type composition. The rationale behind this To analyze macrophage subsets in sc/snRNA-seq and spatial data,
approach is that both RNA-seq expression and cell type abundances are annotated macrophages were integrated separately for each measure-
primarily count data that are normalized to represent the frequency ment method using the function ‘harmonize’ from the Python package
or representation of one entity (gene or cell type) among all measure- Harmony-pytorch version 0.1.4 with patient as batch variable and
ments. However, to account for stronger expected interdependence default parameters otherwise. After integration, Leiden clustering
between cell types due to their lower number compared to genes (~20 was performed using the SCANPY function ‘leiden’ with a resolution
versus ~20,000), we used Pearon’s contingency ratios64 instead of nor- of 0.6. Small clusters expressing non-macrophage marker genes were
malization by total counts as used for the expression variance analysis. detected in all methods and removed from further analysis, followed
by re-intergation and re-clustering.
De novo characterization of malignant expression programs
using iNMF PAM50 molecular subtype assignment
To find de novo malignant expression programs in our sc/snRNA-seq To assign research-based PAM50 subtypes, log2 + 1-transformed counts
across all samples, we used iNMF as implemented in the R package from the full (including all cell types) pseudobulk data were rescaled
LIGER version 0.5.0.9000 (ref. 30), which identifies and separates relative to those of a receptor status-balanced version of this cohort,
common and sample-specific factors in high-dimensional single-cell in which samples were resampled to achieve the ER+ to ER− receptor
Nature Medicine

Article https://doi.org/10.1038/s41591-024-03215-z
status ratio in the UNC training set, from which the PAM50 subtype with 200 μl of wash buffer added directly to the exonuclease mixture.
centroids were derived68,69. The R package genefu version 2.20.0 After supernatant removal, the wash step was repeated twice for a total
(ref. 70) was used to call research-based PAM50 subtypes using the of three washes. The bead pellet was resuspended in 200 μl of freshly
rescaled expression values and Spearman correlation to the PAM50 prepared 0.1 N NaOH and incubated for 5 min at room temperature.
subtype centroids. Samples with a PAM50 centroid correlation less After the addition of 200 μl of wash buffer, the beads were centrifuged
than 0.10 for each centroid were not assigned a PAM50 subtype. for 2 min at 3,000g, and the wash was repeated a total of three times.
Second-strand synthesis was performed by the addition of 200 μl
Sectioning for spatial expression profiling and H&E staining (1× Maxima RT buffer, 1 mM of each dNTP, 10 μM dN-SMRT oligonucleo-
The tissue OCT blocks were acclimated to −20 °C inside the cryostat tide (IDT, 5′-AAGCAGTGGTATCAACGCAGAGTGANNNGGNNNB-3′) and
(Leica, CM1950) for 30 min before sectioning at 10-μm thickness. 0.125 U μl−1 Klenow enzyme (NEB, M0210)) to the bead pellet and incu-
Serial sections were placed on the required glass slides for each of bation at 37 °C for 1 h. Thereafter, 200 μl of wash buffer was added to the
the methods used. Sections were placed such that the same region of mixture and centrifuged for 2 min at 3,000g. The wash was repeated a
interest could be assessed across all methods. total of three times, followed by a final wash in RNase/DNase-free water.
The bead pellet was resuspended in 50 μl of PCR mix (1× Terra Direct
H&E staining and histopathological annotation PCR mix buffer, 2 μl Terra polymerase (Takara, 639270), 2 μM TruSeq
A slide adjacent to the experimental slides was stained for H&E with PCR handle primer (IDT, 5′-CTACACGACGCTCTTCCGATCT-3′) and 2 μM
standard histology techniques. H&E slides were scanned on an Aperio SMART PCR primer (IDT, 5′-AAGCAGTGGTATCAACGCAGAGT-3′)). PCR
Pathology AT2 Slide Scanner (Leica) using ×20 magnification. Each was performed with the following program: 98 °C for 2 min; four cycles
H&E slide was reviewed by a board-certified pathologist (S.J.R.) for QC of 98 °C for 20 s, 65 °C for 45 s and 72 °C for 3 min; 11 cycles of 98 °C
assessment and annotated to indicate the location of tumor regions for 20 s, 67 °C for 20 s and 72 °C for 3 min; 72 °C for 5 min; hold at 4 °C.
using standard pathological criteria. This review was conducted with The cDNA was incubated with 0.6× volumes of AMPure XP beads
a traditional bright-field microscope and included assessment of pres- for 10 min at room temperature. The AMPure XP beads were then pel-
ervation of tissue integrity and morphology after freezing and OCT leted using a magnetic separator for 5 min, followed by two washes
embedding, evaluation of tissue viability, assessment of tumor content with 80% ethanol for 30 s each, and the cDNA was eluted with 50 μl of
and fibrotic tissue content and scoring for inflammation on a 0–3 scale. EB solution. The bead purification was repeated at a 0.6× volume of
Samples that failed this QC step (9/25 samples) exhibited either very AMPure XP beads:cDNA with two washes with 80% ethanol and final
low sample viability (<2% viable cells) or extensive tissue damage or elution with 12 μl of EB. The size and concentration of the final cDNA
had less than 5% tumor content. were assessed on a Bioanalyzer high-sensitivity DNA chip (Agilent,
5067-4626) and on a Qubit high-sensitivity dsDNA kit (Invitrogen,
Slide-seq data generation Q32851), respectively. Thereafter, 600 pg of cDNA was tagmented
To generate Slide-seq data, the Slide-seq puck was placed on a micro- with a Nextera XT kit (Illumina, FC-131-1096) according to the manufac-
scope glass slide with the beads facing upwards and held in place with a turer’s instructions. The libraries were indexed with PCR amplification
drop of water between the glass slide and the puck coverslip. By turning with TruSeq5 (IDT, 5′- AATGATACGGCGACCACCGAGATCTACACTCTTT
the microscope glass slide upside down, the puck surface was aimed CCCTACACGACGCTCTTCCGATCT-3′) and the N700 series barcoded
at the region of interest in the tissue section by lowering the puck over index primers and the following PCR program: 72 °C for 3 min; 95 °C
the tissue section and allowing a quick melting of tissue and puck to for 30 s; 12 cycles of 95 °C for 10 s, 55 °C for 30 s, 72 °C for 30 s and 72 °C
occur before removing the puck:tissue sandwich outside the cryostat. for 5 min; hold at 4 °C.
The puck was moved with forceps to an Eppendorf tube pre-filled with Final purification of the DNA with AMPure XP beads at a 0.6:1
200 μl of hybridization buffer (6× SSC with 2 U μl−1 RNase inhibitor volume ratio of beads:DNA and elution with 12 μl of EB yielded
(Lucigen, 30281)) and incubated for 15 min at room temperature. A sequencing-ready libraries. The library concentrations were diluted
wash followed hybridization by dipping the puck once into 1× Maxima to 4 nM each, and three Slide-seq samples were pooled together. The
RT buffer. First-strand cDNA synthesis was performed by placing the samples were sequenced at a 1.8 pM concentration on an Illumina
puck in 200 μl of first-strand synthesis mixture (1× Maxima RT buffer, NextSeq high-output flow cell with the following settings: read1, 44
1 mM of each dNTP, 0.05 U μl−1 RNase inhibitor (Lucigen, 30281), 2.5 μM bases; read2, 39 bases; and index1, 8 bases.
template switch oligonucleotide (Integrated DNA Technologies (IDT), Raw data were processed using the Slide-seq pipeline (https://
5′-AAGCAGTGGTATCAACGCAGAGTGAATrG+GrG-3′) and 10 U μl−1 github.com/MacoskoLab/slideseq-tools).
Maxima H Minus Reverse Transcriptase (Thermo Fisher Scientific, The quality of all samples was evaluated, and samples with an aver-
EP0742)) and incubated at room temperature for 30 min followed by age read count per bead lower than 150 as well as those with an unrec-
52 °C for 90 min. ognizable shape (which prevented spatial alignment) were excluded
Tissue digestion was thereafter performed by the addition of from further analysis.
200 μl of 2× tissue digestion mix (200 mM Tris-Cl pH 7.5, 400 mM NaCl,
4% SDS, 10 mM EDTA) with 1:50 proteinase K (New England BioLabs CODEX data generation
(NEB), P8107S) to the first-strand reaction mixture with gentle pipette CODEX data generation was performed as described previously with-
mixing and incubation at 37 °C for 30 min. out major adjustment for the MBC tissue7,8. The detailed protocol
After the addition of 200 μl of wash buffer (10 mM Tris pH 8.0, is available on https://www.protocols.io/ (ref. 71). Specifically, anti-
1 mM EDTA, 0.01% Tween 20) to the tissue digestion mixture, the puck body panels for CODEX imaging were chosen to include targets that
beads were removed from the coverslip surface and released into sus- would be anticipated to identify MBC as well as cells of the innate and
pension by vigorously pipetting, and the glass was discarded. The beads adaptive immune system. Each antibody was conjugated to a unique
were pelleted by centrifugation at 3,000g for 2 min, and the superna- oligonucleotide barcode. Detailed panel information can be found in
tant was removed. The bead pellet was washed in 200 μl of wash buffer Supplementary Table 5. For panel validation, antibody–oligonucleotide
and centrifuged as before for a total of three washes, followed by a final conjugates were tested in low-plex fluorescence assays. Staining pat-
wash in 10 mM Tris-HCl, pH 7. Subsequent exonuclease treatment was terns were compared against the expected patterns already established
performed by resuspension of the bead pellet in 200 μl of Exonuclease for immunohistochemistry within positive control tissues of the human
I reaction mixture (1× ExoI buffer with 10 U μl−1 Exonuclease I (NEB, tonsil. Staining patterns were also compared against H&E morphology
M0293L)) and incubated at 37 °C for 50 min, followed by one wash staining to confirm the location of the markers. Signal-to-noise ratio
Nature Medicine

Article https://doi.org/10.1038/s41591-024-03215-z
was also evaluated at this step. Antibody–oligonucleotide conjugates approach to allow flexibility in the final number of selected genes. First,
were then tested altogether in a single CODEX multicycle. a preliminary list of 510 potentially relevant genes was assembled (col-
CODEX multiplexed imaging was executed according to the pre- lected) based on prior knowledge and literature as well as on our MBC
viously described protocols and imaging setup and instructions for sc/snRNA-seq data. Genes were chosen to represent various aspects
CODEX staining of frozen specimens from Akoya Biosciences. In brief, of BC biology, metastasis and the tumor immune microenvironment
after the sample acquisition and OCT embedding, 7-μm sections were as well as cell types and programs discovered from sc/snRNA-seq. The
cut in a cryostat after OCT blocks were equilibrated to the cryostat preliminary list was then filtered down to 300 genes (the experimental
temperature for at least 30–40 min. Tissue sections were dragged over size of the panel) based on expression statistics as measured in the MBC
the surface of cold poly-l-lysine-coated coverslips and spread inside the scRNA-seq dataset and manual priority (0–1) assignment. During probe
cryostat by transiently warming up the bottom surface of the coverslip design, three of the selected 300 genes were excluded as they did not
with a finger. Before staining, the sections removed from the freezer meet technical criteria (all three transcripts were too short), reducing
were dried for 5 min on the surface of Drierite. Dried coverslips with sec- the final gene set to 297 genes. Below, we describe in more detail the
tions on them were dipped for 10 min into room temperature acetone initial selection of 510 genes and their filtering down to 300.
and then fully dried for 10 min at room temperature. Sections were then
rehydrated for 5 min in S1 (5 mM EDTA (Sigma-Aldrich)), 0.5% w/v BSA Gene collection. To generate a preliminary list of genes likely to be
(Sigma-Aldrich and 0.02% w/v NaN (Sigma-Aldrich) in PBS (Thermo broadly relevant for characterization of cell types and programs in
3
Fisher Scientific)) and further re-fixed for 20 min at room temperature MBC lesions, we pursued three broad criteria: (1) prior knowledge based
in S1 with 1.6% formaldehyde. Formaldehyde was washed off twice on expertise and relevant scientific publications; (2) genes coding for
with S1, and sections were equilibrated in S2 (61 mM NaHPO ∙ 7 HO proteins targeted in CODEX proteomic assays also applied to the same
2 4 2
(Sigma-Aldrich), 39 mM NaHPO (Sigma-Aldrich) and 250 mM NaCl MBC HTAPP tumor samples; and (3) genes representing cell types and
2 4
(Sigma-Aldrich) in a 1:0.7 v/v solution of S1 and double-distilled water programs from preliminary sc/snRNA-seq data from 21 MBC biopsies.
(ddHO); final pH 6.8–7.0) for 10 min and blocked in blocking buffer The prior knowledge-driven gene selection (1) started by identify-
2
(ref. 2) for 30 min. All steps to follow were exactly as in Black et al.8 or ing categories of genes known to be important in MBC and in cancer
the Akoya CODEX instructions—this entails cyclic stripping, annealing in general and reviewing available literature to select representative
and imaging of fluorescently labeled oligonucleotides complementary genes of each category:
to the oligonucleotide on the conjugate. • Canonical cell-type-specific markers (for example, EPCAM for
Automated image acquisition and fluidics exchange were per- epithelial cells, CD19 for B cells, CD4 for T helper cells, CD8
formed using an Akoya CODEX instrument driven by CODEX driver for cytotoxic T lymphocytes, CD56 for NK cells and CD14 for
software (Akoya Biosciences) and a Keyence BZ-X710 fluorescence macrophages)
microscope configured with four fluorescent channels (DAPI, FITC, Cy3 • Clinical breast cancer biomarkers (for example, ESR1, PGR and
and Cy5) and equipped with a CFI Plan Apo λ ×20/0.75 objective (Nikon). ERBB2)
Hoechst nuclear stain (1:3,000 final concentration) was imaged in • Breast cancer intrinsic subtypes72,73
each cycle at an exposure time of 1/175 s. Biotinylated CD39 (clone • Hallmarks of cancer: evasion of apoptosis, for example, BCL2;
A1, Biolegend) was used at a dilution of 1:500 and visualized in the EMT, for example, VIM; immune evasion, for example, CD274;
last imaging cycle using DNA streptavidin-PE (1:2,500 final concen- senescence, for example, TP53; proliferation, for example,
tration). DRAQ5 nuclear stain (1:500 final concentration) was added MKI67, etc.71,72
and visualized in the last imaging cycle. Each tissue was imaged with a • Epithelial hierarchy in the normal breast74–77
×20 objective in a 7 × 9 tiled acquisition at 1,386 × 1,008 pixels per tile • ER signaling78
and 396-nm-per-pixel resolution and 13 z-planes per tile (axial resolu- • Genomic landscape of MBC and therapeutic resistance59,79–83
tion, 1,500 nm). Images were subjected to deconvolution to remove
out-of-focus light. The pre-defined CODEX target genes were included in the panel
Raw imaging data were processed using the CODEX Uploader to ensure congruence and subsequent integration with matching
(https://github.com/nolanlab/CODEX) for image stitching, drift com- CODEX data. To this end, we translated protein identifiers to gene
pensation, deconvolution and cycle concatenation. Processed data identifiers and assigned the resulting genes priority 1 to be included
were then segmented using CellVisionSegmenter, an open-source, in the panel (see the ‘Gene filtering’ subsection).
pre-trained nucleus segmentation and signal quantification software The data-driven gene selection was performed on the sc/snRNA-seq
based on the Mask region-convolutional neural network (R-CNN) archi- data available at that time using Seurat version 2.3.4. The data used
tecture. CellVisionSegmenter was trained on manually annotated for gene selection consisted of 21 MBC samples (six snRNA-seq,
CODEX multiplexed imaging data and can successfully segment both 15 scRNA-seq) and represent only a subset of the final dataset of 37
dense and diffuse cellular tissues (https://github.com/bmyury/CellVi- snRNA-seq and 30 scRNA-seq. Single-cell profiles with fewer than
sionSegmenter; https://github.com/michaellee1/CellSeg)68. As such, 500 genes and single-nucleus profiles with fewer than 200 genes were
only one parameter was altered for the segmentation of the HTAPP removed. Preliminary cell types were annotated using the R package
dataset: the growth pixels of the nuclear mask. This was experimentally SingleR version 1.0.1 (https://bioconductor.org/packages/release/
determined to be optimal at a value of 3. After the upload, the images bioc/html/SingleR.html) in single-cell mode with the built-in HPCA
were visualized in ImageJ (https://imagej.net/) and re-evaluated for reference and standard parameters. To identify cell-type-specific
specific signal. Any markers that produced a low signal-to-noise ratio or genes—that is, genes with high cell type predictive power—we trained
an untenable pattern were excluded from the ensuing analysis. Finally, a support vector machine (SVM) classifier (R package liblineaR version
all samples were manually checked for presence of obvious signs of 2.10-8) and used the assigned feature weights to select highly predic-
unexpected signal appearance or distribution indicative of device or tive genes for each cell type. Data were downsampled to 200 randomly
protocol error. None was detected, and all samples were considered selected cells per cell type to ensure class balance, and predictive power
fit for downstream image analysis. of the classifier was assessed through five-fold cross-validation and
prediction accuracy. In a first pass, baseline accuracy was determined
Gene panel design for MERFISH and ExSeq by training and testing a classifier on all variable genes. In a second
To select a set of genes for spatial profiling of MBC biopsies with MER- pass, per cell type, only genes with a ranked cumulative relative weight
FISH and targeted ExSEQ assays, we developed a ‘collect-and-filter’ below 0.4 (single-nucleus data) and 0.45 (single-cell data) (that is,
Nature Medicine

Article https://doi.org/10.1038/s41591-024-03215-z
all top weighted genes that together account for 40% or 45% of relative the case of genes selected due to their known relevance in MBC. Three
weight, respectively) were used to train a second classifier on a second genes were identified as being too short during the probe generation
independently downsampled dataset with the same specifications. step, because they did not have sufficient length to accommodate the
Again, accuracy was assessed in five-fold cross-validation and com- placement of a sufficient number of unique probes. The total number
pared to baseline accuracy to ensure that, by reducing the number of of genes assessed was, thus, 297, representing all nine categories and
genes and using a different subset of the data, accuracy was not sig- 82 of the 83 original gene types (Supplementary Table 3). This high
nificantly reduced. Additionally, we also determined the classification retention rate of represented gene types confirmed that we were still
error rate using a random forest classifier (R package randomForest covering all major cell types, subtypes and programs of interest with the
version 4.6-14) to confirm that the observed good performance was reduced gene set and allowed us to confidently move forward with it.
not classifier dependent. Of the thus-selected genes, all genes with a
ranked cumulative relative weight below 0.3 (single-nucleus data) or MERFISH data generation
0.35 (single-cell data) were assigned priority 1, whereas the remaining The detailed protocol for MERFISH data generation is available
genes were assigned priorities lower than 1 based on their relative total on https://www.protocols.io/ (ref. 84). The MERFISH protocol was
weights across all cell types (see the ‘Gene filtering’ subsection). divided into three parts: probe design/generation, tissue processing
To represent the BC-intrinsic subtypes, the PAM50 subtype- and imaging and analysis/segmentation.
defining genes64 were refined using a similar approach as the one In addition to the 297 genes selected for MERFISH as described
described above based on the single-cell and single-nucleus data. In above, two additional genes, ALB and LIPE, were added to the gene panel
a first pass, all 50 PAM50 genes were used to detect baseline accuracy for ready identification of the common host tissue cell types found in
of discriminating the PAM50 subtypes, and, in a second pass, all genes liver (hepatocytes) and adipose (adipocytes) tissues, respectively. For
with a ranked cumulative relative weight lower than 0.8 (single-cell and design and construction of encoding probes, each of the 291 genes
single-nucleus data) were used to determine classification accuracy imaged in the combinatorial imaging rounds was assigned to a unique
and assigned priority 1, whereas the remaining genes were assigned binary barcode drawn from a 22-bit, Hamming distance 4, Hamming
priorities lower than 1 based on their relative total weights across all weight 4 encoding scheme. Ninety-four extra ‘blank’ barcodes that
cell types (see the ‘Gene filtering’ subsection). were not assigned to any genes were included to provide a measure of
To select genes that represent cellular programs within cell types, the false-positive rate. Each bit of the 22-bit code was associated with
we applied topic modeling separately on the major cell types present a unique readout sequence, and, for each gene, the readouts corre-
in the single-cell dataset (malignant cells, T cells, NK cells, fibroblasts, sponded to the four ‘on-bit’ (bits that read ‘1’) of the gene’s assigned bar-
endothelial cells, monocytes/macrophages/dendritic cells, B cells code. For each gene, 60 encoding probes were generated, comprising
and plasma cells). We used the FitGoM() function of the R package a 30-mer target sequence, three readout sequences corresponding to
CountClust version 1.12.0 to fit a grade of membership (GoM) model the gene and PCR primer sequences for library amplification. Template
to the raw count data of up to 4,000 randomly sampled cells per cell DNA for the encoding probes used for the 291 multiplexed genes was
type. The tolerance value of the GoM model was set to 0.01 for all cell synthesized as a complex oligo pool and used to construct the final
types. The number of topics (K) to be fitted was empirically determined MERFISH probe set, as described previously85. Encoding probes for
for each cell type by fitting models with a range of sensible values for the eight genes measured as sequential single-molecule FISH (smFISH)
K and comparing the Bayesian information criterion (BIC) of the dif- rounds were designed in a similar fashion as described above, except:
ferent models. For each cell type, K was selected to be greater than or (1) 48 probes were generated for each gene; (2) one unique readout
equal to 3 and to represent a local minimum in BIC. Finally, separate sequence was used for each gene; and (3) PCR primers were omitted.
models were fit for each of the following cell types with the indicated Encoding probes were then synthesized in a 96-well plate format and
parameters after excluding ribosomal and mitochondrial genes: malig- mixed to suitable final concentration.
nant cells (K = 13), T cells (K = 3), NK cells (K = 3), fibroblasts (K = 4), Sliced samples were placed on poly-d-lysine-coated coverslips,
endothelial cells (K = 5), monocytes/macrophages/dendritic cells fixed with 4% formaldehyde, permeabilized in 70% ethanol, pho-
(K = 7), B cells (K = 3) and plasma cells (K = 10). For each topic, the top tobleached with white light and then hybridized with the MERFISH
30 genes were identified using the function ExtractTopFeatures() probe library and a poly(A) anchor probe. After hybridization, sam-
and subjected to GSEA using enrichR version 1.083 querying the ples were embedded in a 4% polyacrylamide gel, optically cleared in
GO_Biological_Process_2018 database. Topic loadings across cells a digestion buffer containing protease and mild detergent and stored
as well as Gene Ontology (GO) terms enriched with an adjusted at 4 °C until imaged.
P value false discovery rate (FDR) < 0.05 were manually inspected MERFISH imaging of samples was performed on a homemade
for interesting patterns. Of the genes defining topics and GO terms imaging platform. Before imaging, samples were stained with two
deemed interesting, the gene with the highest loading for each topic segmentation markers, DAPI and an Alexa Fluor 488–conjugated
was assigned priority 1, whereas the other genes were assigned priority readout probe complementary to the poly(A) anchor probe. For imag-
0 (see the ‘Gene filtering’ subsection). ing, samples were held inside a flow chamber to accommodate buffer
exchanges over the many rounds of MERFISH imaging. Each imaging
Gene filtering. To select 300 genes from the list of 510 assembled round consisted of readout probe hybridization, imaging each FOV
through the different approaches described above, we devised a filter- (220 μm × 220 μm per FOV) and readout probe fluorophore cleavage.
ing strategy to make sure that genes are expressed in, and are variable Imaging consisted of 17 rounds. After imaging the segmentation
across, the single-cell expression dataset while preserving the diver- markers in round 1, the barcode-encoded RNA species were imaged
sity of cellular and biomedical aspects represented by the 510 genes in rounds 2–12 (combinatorial smFISH rounds), and the individually
and summarized as nine categories and 83 selection types of genes. A labeled RNA species were imaged in rounds 13–16 (sequential smFISH
gene was included under the following conditions: (mean normalized rounds). In rounds 1–12, images of each FOV were acquired at seven
expression > 0.15 OR variability > 0.025 OR number of categories > 1) focal planes separated by 1.5 μm in z. In rounds 13–16, images of each
AND (mean normalized expression > 1.5 and < 4 OR variability > 0.25 OR FOV were acquired at one focal plane 3.5 μm above the glass surface.
priority = 1 OR number of categories > 1) with variability defined as the In addition, every imaging round included a single z-plane image of
fraction of cells with an absolute scaled expression value greater than the fiducial beads on the glass surface for image registration. The
1 across all cells and mean normalized expression calculated across all number of FOVs imaged for each sample varied based on the size of
cells of the highest expressing cell type or epithelial (malignant) cells in the sample.
Nature Medicine

Article https://doi.org/10.1038/s41591-024-03215-z
Subsequently, all MERFISH image analysis was performed using the barcodes). Designed padlock probes were then purchased in
the MERlin Python package (https://github.com/ZhuangLab/MERlin). plate-based format from IDT and pooled together.
First, for each FOV, the images from each imaging round were aligned The first experimental step was tissue preparation following the
to correct for x–y drift in the stage position. For the combinatorial ‘Targeted ExSeq–Tissue Preparation’ protocol, following path C in the
rounds, image stacks for each FOV were high-pass filtered, decon- flowchart in the protocol abstract. In this step, tissue sections were
volved using Lucy–Richardson deconvolution and, finally, low-pass fixed, expanded and prepared for targeted ExSeq library preparation. In
filtered. Individual RNA molecules were then identified by a pixel-based brief, after cryosectioning onto Superfrost Plus glass slides (described
decoding method as previously described11. All cell segmentation was above), tissue sections were fixed with ice-cold 10% formalin for 12 min
performed using the cellpose Python package (https://github.com/ and then washed three times for 5 min each wash with ice-cold 1× PBS.
MouseLand/cellpose) using the ‘nuclei’ model applied to the DAPI Slides were then stored in 70% ethanol and stored at 4 °C for up to
image for each FOV. Identified individual RNA molecules were then 1 week. To begin gel embedding, slides were briefly dried with a labo-
assigned to individual cells based on if they were located within ratory wipe, and a Bio-Rad Frame-Seal sticker was placed around the
the segmented boundaries. For the sequential smFISH rounds, images tissue section, forming a chamber for washes. The tissue was rehy-
were high-pass filtered and background subtracted, and the expres- drated by washing with 1× PBS and then treated with 0.1 mg ml−1 LabelX
sion of each gene in each cell was calculated as the sum of the fluores- overnight at 37 °C to enable nucleic acid anchoring into the expansion
cence intensity of all pixels within the segmentation boundary of the hydrogel. The tissue was then embedded into the expansion micros-
central z-plane of each cell. The signals from the eight sequential copy hydrogel and digested following the Robust Digestion Conditions
genes were merged with the RNA counts matrix from the 291 genes described in the protocol. After digestion, the sample was expanded
measured in the combinatorial smFISH rounds to generate a final and re-embedded into a non-expanding polyacrylamide gel to lock
expression matrix for each tissue slice. Each slice was then evaluated in the expansion factor. The fixed charge of the carboxylates in the
against QC criteria to determine if it would be included in further original expansion gel was then chemically passivated using EDC-NHS
analysis. The QC criteria for each slice consisted of (1) the average activation of carboxylate groups, followed by amide bond formation
number of RNA counts per cell (≥50 to pass) and (2) the Pearson cor- with ethanolamine. Gels were then trimmed to size.
relation of the average gene expression between the MERFISH dataset The second experimental step was library preparation following
and an scRNA-seq dataset derived from the same tumor (Pearson the ‘Targeted ExSeq–Sequencing Library Preparation’ protocol. In
correlation coefficient ≥ 0.60 to pass). Both criteria had to be met brief, padlock probes bearing barcode sequences are hybridized to RNA
to pass QC. transcripts. Padlock probes are then enzymatically circularized using
SplintR Ligase and then enzymatically amplified using rolling circle
Targeted ExSeq data generation amplification using Phi29 DNA Polymerase, forming amplicons (also
The detailed protocols for targeted ExSeq data generation are available called RCA colonies, or rolonies). The amplicons are then cross-linked
as a protocols collection on https://www.protocols.io/ (ref. 86). The to each other and the sample and are ready for in situ sequencing. For
overall structure of the work is in three parts: experimental design, these samples, the universal amplicon detection hybridization step was
experimental execution and analysis. In the experimental design step, skipped here and performed after in situ sequencing was completed.
padlock probes were designed that targeted the genes identified above. The third experimental step was in situ sequencing following the
In the experimental execution steps, tissue sections were fixed and ‘Targeted ExSeq–In Situ Sequencing (Illumina Chemistry)’ protocol. In
expanded, followed by targeted in situ sequencing library prepara- brief, samples (gel-embedded tissues with in situ sequencing libraries)
tion and in situ sequencing of the prepared library. Finally, in situ were covalently anchored to glass-bottom plates for imaging by func-
sequencing data were decoded to identify specific RNA transcripts tionalizing the plate surface with acryloyl groups, placing the speci-
in the specimen. men gel inside the well and casting a second re-embedding gel that
Padlock probes were designed that targeted the genes identified anchored the specimen gel to the glass-bottom plate. The sample
above, following the ‘Targeted ExSeq–Probe Generation’ protocol. In was then prepared for sequencing by capping free 3′ ends of DNA in
brief, logical barcode sequences of length 7, with each position in the the sample with dideoxy nucleotides using TdT tailing. The Illumina
barcode being a number between 0 and 3, were generated and ran- sequencing primer was hybridized to amplicons within the specimen,
domly assigned to the genes of interest. These barcodes were designed and seven rounds of Illumina sequencing-by-synthesis were performed
to have a minimum Hamming distance of 3, enabling error detection in situ using reagents collected from MiSeq version 3 sequencing kits.
and correction. These logical barcodes were then implemented as Each round of sequencing consisted of base incorporation (addition
nucleic acid sequences on the backbone of the padlock probe, with of the next base), four-color imaging of the amplicons on a spinning
one sequence for readout with the Illumina sequencing-by-synthesis disk confocal microscope and cleavage of the reversible terminator,
chemistry (used in this work) and another sequence for readout with enabling the next round of sequencing to be performed. After the
the SOLiD sequencing-by-ligation chemistry (not used here). Both final round of sequencing, the universal amplicon detection probe
sequences are included in the backbone of the probe adjacent to the was hybridized to the sample (see library preparation protocol), and
sequencing primer site. Probe homology sequences were then gener- a final round of imaging was performed.
ated by performing a sliding window search along each transcript. Data analysis to convert in situ sequencing images to localized
Candidate regions were excluded for sequence complexity (more than reads in space was performed using the established ExSeqProcess-
five consecutive repeated bases, containing three or fewer unique ing pipeline (https://github.com/dgoodwin208/ExSeqProcessing)
nucleotides, GC content outside of 40–65%), physical considerations using the Big Experiment (BigEXP) approach for image registration
(melting temperature (T ) of either arm of the padlock probe below a after color correction and normalization. After image registration
m
gene-specific T threshold, T difference between the two arms exceed- is puncta extraction and base calling, using the probe barcodes as
m m
ing 8 °C, presence of hairpins or dimers in the homology region) or the reference library. Manual cell segmentation was performed in 2D
significant homology to a different transcript that spans the ligation by using VASTLite version 1.3.0 (ref. 87) to manually annotate nuclei
junction. For each gene, the first 16 homology regions starting from boundaries of a 2D maximum intensity projection image of the DAPI
the 5′ end of the transcript were selected. If fewer than 16 homology channel. Reads localized within nuclei were assigned to that cell; reads
regions were identified, all were selected for use. Probes for each gene outside of segmented nuclei were discarded. The quality of each sample
were assembled by combining the homology regions with a back- was evaluated, and samples with an average read count per cell lower
bone sequence shared across all probes for that gene (containing than 50 were excluded from further analysis.
Nature Medicine

Article https://doi.org/10.1038/s41591-024-03215-z
Processing and quality assurance of the spatial expression section were removed, and observations were annotated according
data to the histopathological annotation that they overlapped.
All spatial expression data were received in their respective typical
formats. In a first step, all data types were transferred into a common Cell type annotation of the spatial expression data by
observation × feature matrix format following the format of scRNA-seq annotation transfer from the sc/snRNA-seq data
data. For single-molecule data (MERFISH and ExSeq), two matrices For all spatial expression data, cell types were annotated using the
were created, one cell × feature matrix using the accompanying cell TACCO framework version 0.0.1 (ref. 44) together with the matching
segmentation information and one bin × feature matrix where expres- sc/snRNA-seq data as reference. Specifically, we used two conceptu-
sion was represented per 10 μm × 10-μm bin, resembling Slide-seq data. ally different annotation methods wrapped in the TACCO framework
Additionally, spatial coordinates were adjusted to all start at [0 | 0] and that are both able to deconvolve cell type mixtures. We used RCTD
scaled to represent a positional resolution of 1 pixel per μm, which was version 1.2.0 (ref. 43) as a previously published, well-accepted tool that
the lowest original resolution of the data. Note that, in spatial expres- was designed for the annotation of Slide-seq data and that explicitly
sion data, we distinguish between ‘positional resolution’ and ‘capture models cell-type-specific read count distributions to determine the
resolution’: positional resolution is the resolution at which the posi- cell type composition of observations. We also used TACCOʼs own
tion in space of an observation or molecule is reported, whereas the annotation method, which is based on unbalanced optimal transport
capture resolution is the resolution at which molecules are distinctly (OT), which makes fewer assumptions about the properties of the input
captured. For example, in Slide-seq, the positional resolution (that data and, in particular, is not, per design, limited to count data, which is
is, the resolution at which the position of the beads is reported) is necessary for a coherent annotation, including the CODEX data. RCTD
0.65 μm per pixel, and the capture resolution is 10 μm (=diameter of was run with default parameters except for min_ct = 2. OT was run
a bead) because molecules that get captured by the same bead have with lamb = 0.001 and ‘boosted’ by using TACCO’s platform normaliza-
a maximum distance of 10 μm from each other. For single-molecule tion, multicenter (multi_center=4 ) and bisectioning (bisections = 4,
resolved methods, positional and capture resolution are identical. bisection_divisor = 3) functionalities. Per observation, compositional
Having brought all data into the same format allowed their as well as categorical (maximum cell type) annotations were stored
efficient processing together with the matching sc/snRNA-seq data for further use.
as an anndata object using SCANPY88. This way, for each patient
and method, one anndata object was created and processed indivi- Cell type frequency correlation analysis
dually. The same measures were applied on all data types as reasonable To assess the agreement of local cell type frequencies across the serial
given the differences in design parameters between the different sections of the same biopsies profiled with different methods, we
methods. defined, for each biopsy, a universal grid of 100 × 100-μm bins, and,
Quality filtering was applied using the SCANPY version 1.7.2 func- within each bin and section, the cell type composition was calculated
tions filter_cells with method-specific parameters and filter_genes based on the previously assigned categorical cell type annotations,
with the min_cells parameter set to 3. The following filter_cells param- yielding, for each bin and section, a vector of cell type frequencies with
eters were used: min_counts = 20 and min_genes = 1 (MERFISH and the length of the cell types seen in any of the sections of a given biopsy.
ExSeq), min_counts = 30 and min_genes = 30 (initial Slide-seq and sc/ Pair-wise Pearson correlations were then calculated per bin between
snRNA-seq). For Slide-seq and sc/snRNA-seq, an additional iterative the cell type composition vectors derived from each of the sections,
process of step-wise min_counts parameter increase was performed representing different profiling methods and/or replicates.
to ensure that the fraction of low-quality beads with fewer than 100
counts retained in the data did not surpass 35%. This adaptive proce- Analysis of cluster congruence using the ARI
dure ensured sufficient quality while retaining the maximum num- To assess congruence of expression-based Leiden clusters and cell
ber of observations possible. This procedure was also performed on type or patient/sample annotations, respectively, with the assessed
sc/snRNA-seq data that had already been quality filtered as described communities (Leiden clusters, patients/samples and cell types) con-
above to ensure equivalent filtering in the extremely unlikely case sisting of individual observations (single cells/beads/bins), the ARI was
that this procedure might prove to be more stringent in specific cases. calculated using the function adjusted_rand_score from the Python
For CODEX, the parameter settings min_counts = 1 and min_genes = 1 package scikit-learn version 0.24.1. Bootstrapping across 10 iterations
were used, translating into a requirement of a value of greater than 1 was used for statistical robustness, and results are reported as mean
in at least one gene, essentially disabling this filtering step for these and standard deviation.
intensity-based data, because cell quality filtering had already taken
place during the segmentation process. Cell type co-localization analysis
After filtering, the SCANPY workflow, including normalization, Cell type co-localization analysis was performed using TACCO’s
log1p transformation, scaling, highly variable gene selection, regres- version 0.2.2 co_occurrence function based on the compositional
sion of total counts and mitochondrial counts (where possible), PCA, OT annotations for a distance of up to 500 μm and using the ‘log_occ’
nearest neighbor finding, Leiden clustering and 2D projection using score. In brief, at each distance from a selected central cell type (here,
UMAP, was applied. For CODEX, normalization and regression were macrophages), the function calculates the probability of finding the
not performed given the intensity-based (not count-based) nature of other annotated cell types relative to the case where a central cell type
the data and the within-sample scope of this analysis. is not selected. Two scores were then derived from the co-localization
Finally, the spatial expression data and H&E images were aligned score: co-localization strength, defined as the score of the first distance
in a semi-manual process to honor their serial nature and allow effi- interval, and co-localization range, defined as the score at the distance
cient comparison as well as transfer of histopathological annotations interval where the score has decayed to 25% of the score in the first
from the H&E images. To this end, we devised custom functions that distance interval.
allow for all necessary transformations (rotation, translocation, flip-
ping and scaling) and, using Jupyter notebooks, manually found and De novo cell type annotation of the cell-segmented
recorded the respective parameters for each sample until all data MERFISH data
from one biopsy were adequately registered to a common coordinate Leveraging the single-cell-like behavior of the cell-segmented MERFISH
system in a reproducible manner. To filter out spurious measurements, data, in addition to the annotation transfer as described above, we
all observations that resided outside of the area covered by the H&E performed manual cluster-wise and marker gene-based annotation as
Nature Medicine

Article https://doi.org/10.1038/s41591-024-03215-z
is frequently done in scRNA-seq data. To this end, all cell-segmented Pearson correlation and Spearman correlation coefficients were
MERFISH data were combined into one anndata object and processed calculated using the cor or cor.test function from the R package ‘stats’
using SCANPY version 1.7.2 functions as described above. For con- or the corr function of the Python package ‘pandas’ version 1.1.3.
sistency, we used a similar level of resolution for the annotated cell All UMAPs were created using SCANPY’s version 1.7.2 umap func-
types as was used in the sc/snRNA-seq annotation and assigned new tion with default parameters.
cell type labels only when clusters clearly displayed features that did
not match to any previously annotated cell types, which was the case Reporting summary
for a small population of potentially regulatory B cells expressing Further information on research design is available in the Nature
FOXP3 in addition to the typical B cell marker FCRL5. Portfolio Reporting Summary linked to this article.
Characterization of macrophage subclusters Data availability
To characterize macrophage subclusters in each profiling method, All data can be retrieved from Synapse or the database of Genotypes
Leiden clusters were called on Harmony-aligned data (as described and Phenotypes (dbGaP) (accession number: phs002371) through
in the subsection ‘Integration of sc/snRNA-seq data or spatial data on the HTAN Portal at https://humantumoratlas.org and the associated
a pseudobulk or single-cell/bead/bin level’). Differentially expressed HTAN Publication Page https://humantumoratlas.org/publications/
genes were called using the function rank_genes_groups of the Python htapp_mbc_klughammer_2024. For convenience, processed data are
package SCANPY version 1.7.2 with the method parameter set to additionally available from the Single-Cell Portal (https://singlecell.
‘wilcoxon’ and default parameters otherwise. One or two of the top broadinstitute.org/single_cell/study/SCP2702) and interactively
five differentially expressed genes were selected for display. browsable through CELLxGENE (https://cellxgene.cziscience.com/
collections/a96133de-e951-4e2d-ace6-59db8b3bfb1d). The pre-built
Differential expression analysis between EMT phenotypes Cell Ranger reference GRCh38 version 3.0.0 (November 2016) in its
To detect differentially expressed genes among the three spatial spliced (scRNA-seq) and pre-mRNA (snRNA-seq) version was provided
pheno types (EMT-high, EMT-low and EMT-patched), the function by 10x Genomics (https://www.10xgenomics.com/support/software/
‘enrichments’ of the Python package TACCO version 0.2.2 was used in a cell-ranger/latest/release-notes/cr-reference-release-notes).
one-against-all-others or EMT-high versus EMT-patched setup with the
following relevant parameters: p_corr = ‘fdr_bh’ (multiple testing cor- Code availability
rection using Benjamini–Hochberg correction), position_split = (1,2) Code used to perform the presented analysis is available on GitHub:
(split sample in two parts along the y axis to capture within-sample https://github.com/klarman-cell-observatory/HTAPP-Pipelines/tree/
variability), method = ‘welch’ (Welch’s t-test for statistical significance master/HTAPP_MBC.
testing), direction = ‘both’ (test for increased/enriched or decreased/
depleted expression), reduction = ‘mean’ (measure to calculate pseu- References
dobulk values across sample splits) and normalization = ‘clr’ (use center 62. Stuart, T. et al. Comprehensive integration of single-cell data. Cell
log-ratio normalization). 177, 1888–1902 (2019).
63. Hoffman, G. E. & Schadt, E. E. variancePartition: interpreting
Differential cell type composition analysis between EMT drivers of variation in complex gene expression studies.
defined neighborhoods BMC Bioinformatics 17, 483 (2016).
To detect differences in cell type composition between EMT-high and 64. Greenacre, M. & Lewi, P. Distributional equivalence and
EMT-low neighborhoods, a two-sided Wilcoxon test and Benjamini– subcompositional coherence in the analysis of compositional
Hochberg multiple testing correction were applied on center log-ratio data, contingency tables and ratio-scale measurements. J. Classif.
normalized, cell type compositions in 100 × 100-μm bins. EMT-high 26, 29–54 (2009).
and EMT-low neighborhoods were defined as 100 × 100-μm bins with 65. Subramanian, A. et al. Gene set enrichment analysis: a knowledge-
a mean EMT score greater (high) or smaller (low) than the median EMT based approach for interpreting genome-wide expression
score for a given sample. profiles. Proc. Natl Acad. Sci. USA 102, 15545–15550 (2005).
66. Liberzon, A. et al. The Molecular Signatures Database (MSigDB)
MERFISH-based differential expression analysis between T/NK hallmark gene set collection. Cell Syst. 1, 417–425 (2015).
proximal and distal malignant cells 67. Leek, J. T., Johnson, W. E., Parker, H. S., Jaffe, A. E. & Storey, J. D.
To investigate differences in expression profiles of malignant cells that The sva package for removing batch effects and other unwanted
are located in proximity of T or NK cells and those that are not, we used variation in high-throughput experiments. Bioinformatics 28,
the cell-segmented and manually annotated MERFISH data and defined 882–883 (2012).
T/NK high-malignant cells as those that reside in a 100 × 100-μm bin 68. Parker, J. S. et al. Supervised risk predictor of breast cancer based
together with at least one T or NK cell and the T/NK low-malignant cells on intrinsic subtypes. J. Clin. Oncol. 27, 1160–1167 (2009).
as those that reside in a 100 × 100-μm bin that does not contain a T or 69. Prat, A. & Parker, J. S. Standardized versus research-based PAM50
NK cells. We then ran the SCANPY version 1.7.2 function rank_genes_ intrinsic subtyping of breast cancer. Clin. Transl. Oncol. 22,
groups using the Wilcoxon test and Benjamini–Hochberg correction 953–955 (2020).
to compare both groups of malignant cells and rank the genes by their 70. Gendoo, D. M. A. et al. Genefu: an R/Bioconductor package for
expression difference. This analysis was performed in a sample-specific computation of gene expression-based signatures in breast
setup as well as a combined setup across all samples. cancer. Bioinformatics 32, 1097–1099 (2016).
71. Goltsev, Y. et al. CODEX oligo-labeled antibody conjugation v.2.
Statistical analysis protocols.io https://doi.org/10.17504/protocols.io.3fugjnw
Box plots follow the standard format (center line corresponds to (2019).
the median; box limits correspond to the upper and lower quartiles; 72. Perou, C. M. et al. Molecular portraits of human breast tumours.
whiskers represent the 1.5× interquartile range; points represent out- Nature 406, 747–752 (2000).
liers). Where there were too many data points to show individually, 73. Sørlie, T. et al. Gene expression patterns of breast carcinomas
width-scaled violin plots were used to represent the distribution of data distinguish tumor subclasses with clinical implications. Proc. Natl
points, where graphically possible (otherwise only box plots are shown). Acad. Sci. USA 98, 10869–10874 (2001).
Nature Medicine

Article https://doi.org/10.1038/s41591-024-03215-z
74. Visvader, J. E. Keeping abreast of the mammary epithelial updated about the progress of this project and the manuscript
hierarchy and breast tumorigenesis. Genes Dev. 23, 2563–2577 preparation. The funders had no role in study design, data collection
(2009). and analysis, decision to publish or preparation of the manuscript.
75. Visvader, J. E. & Stingl, J. Mammary stem cells and the differentiation J.K. was supported by an EMBO Long-Term Fellowship (ALTF 738-
hierarchy: current status and perspectives. Genes Dev. 28, 1143–1158 2017), an HFSP long-term fellowship (LT000452/2019-L) and an EKFS
(2014). starting grant (2019_A70). D.L.A. was supported by the Cancer Couch
76. Nguyen, Q. H. et al. Profiling human breast epithelial cells using Foundation, the Catholic Health Foundation, the Conquer Cancer–
single cell RNA sequencing identifies cell diversity. Nat. Commun. Breast Cancer Research Foundation Young Investigator Award, a
9, 2028 (2018). Dana-Farber Cancer Institute Graduate Training in Cancer Research
77. Pellacani, D., Tan, S., Lefort, S. & Eaves, C. J. Transcriptional T32, the Friends of Dana-Farber Cancer Institute, Hope Scarves, the
regulation of normal human mammary cell heterogeneity and its Jamieson Family Fund for Early Career Breast Cancer Researchers, the
perturbation in breast cancer. EMBO J. 38, e100330 (2019). Terri Brodeur Breast Cancer Foundation Fellowship and the Saverin
78. Carroll, J. S. & Brown, M. Estrogen receptor target gene: an Family Fund. S.M. was supported by a DFG research fellowship
evolving concept. Mol. Endocrinol. 20, 1707–1714 (2006). (MA 9108/1-1). E.S.B. was supported by the Howard Hughes Medical
79. Yates, L. R. et al. Genomic evolution of breast cancer metastasis Institute (HHMI), Lisa Yang and John Doerr. X.Z. is an HHMI investigator.
and relapse. Cancer Cell 32, 169–184 (2017). We gratefully acknowledge LMU Klinikum for providing computing
80. Siegel, M. B. et al. Integrated RNA and DNA sequencing reveals resources on their Clinical Open Research Engine (CORE), the
early drivers of metastatic breast cancer. J. Clin. Invest. 128, Bioinformatic Core Facility of the Biomedical Center Munich for
1371–1383 (2018). providing computing resources on their HPC system, and the
81. Nayar, U. et al. Acquired HER2 mutations in ER+ metastatic breast German Research Foundation (DFG) funded CRC237 and CRC274 for
cancer confer resistance to estrogen receptor-directed therapies. additional support.
Nat. Genet. 51, 207–216 (2019).
82. Wander, S. A. et al. The genomic landscape of intrinsic and Author contributions
acquired resistance to cyclin-dependent kinase 4/6 inhibitors J.K., D.L.A., O.R.-R., B.E.J., A. Regev and N.W. conceived and led the
in patients with hormone receptor–positive metastatic breast study. D.L.A., N.U.L., S.M.T. and E.P.W. provided samples and shared
cancer. Cancer Discov. 10, 1174–1193 (2020). clinical insights, directed by N.W. D.L.A. managed biospecimen
83. Mao, P. et al. Acquired FGFR and FGF alterations confer resistance selection, collection and clinical annotation, with contributions from
to estrogen receptor (ER) targeted therapy in ER+ metastatic K.H., L.K.D., A.F., J.F., M.E.H., S.S., K.N., C.M., R.O., M.P., J.C. and S.I.,
breast cancer. Clin. Cancer Res. 26, 5974–5989 (2020). directed by N.W. M.S. and S.V. generated sc/snRNA-seq data, together
84. Blosser, T. R. & Zhuang, X. MERFISH protocols for HTAPP. with J. Wu., I.W., S.N., A.K. and J. Waldman, directed by A. Rotem, A.R.T.
protocols.io https://doi.org/10.17504/protocols.io.bujrnum6 and O.R.-R. Å.S. sectioned tissue blocks and prepared slides for spatial
(2021). profiling, with contributions from K.L.P., A.L., N.C. and M.T., directed
85. Moffitt, J. R. et al. Molecular, spatial, and functional single-cell by O.R.-R. and S.J.R. K.L.P. generated H&Es, with contributions from
profiling of the hypothalamic preoptic region. Science 362, A.L., N.C. and M.T., directed by S.J.R., who also generated pathology
eaau5324 (2018). annotations. Å.S. generated Slide-seq data, with contributions from
86. Sinha, A. et al. Targeted expansion sequencing protocols v.3. E.M., directed by F.C. J.K. and D.L.A. developed the gene panels
protocols.io https://doi.org/10.17504/protocols.io.b2e4qbgw for MERFISH and ExSeq, with input from A. Regev. and N.W. T.R.B.
(2021). generated MERFISH data, directed by X.Z. Y.C. and D.R.G. generated
87. Berger, D. R., Seung, H. S. & Lichtman, J. W. VAST (Volume ExSeq data, with contributions from A.S. and S.A., directed by E.S.B.
Annotation and Segmentation Tool): efficient manual and semi- Y.G. generated CODEX data, with contributions from C.C., directed
automatic labeling of large 3D image stacks. Front. Neural Circuits by G.P.N. J.K. designed and performed the computational analysis,
12, 88 (2018). with contributions from O.A., O.C., S.M., N.M., M.N, C.B.M.P., R.S.,
88. Wolf, F. A., Angerer, P. & Theis, F. J. SCANPY: large-scale single-cell J.G.T.Z. and D.Z., directed by A. Regev, with biological and translational
gene expression data analysis. Genome Biol. 19, 15 (2018). insights from D.L.A. and N.W. J.J.-V., D.L.A. and J.K. managed the study
logistics, with contributions from O.A., K.H., L.K.D., A.F., A. Rotem, A.T.
Acknowledgements and D.D., directed by O.R.-R. J.K., D.L.A., B.E.J., A. Regev and N.W. wrote
We are grateful to all the patients who volunteered for our tumor the manuscript, with input from all authors.
biopsy protocol and generously provided the tissue analyzed in this
study. We thank L. Gaffney for help with figure preparation; E. Gelfand Competing interests
for administrative assistance; K. Bifolck for editorial assistance; and A. Regev, J.K. and D.L.A. are co-inventors on patent application
J. Chien for curating and depositing the data on CELLxGENE; as well number 17/156,392, filed by the Broad Institute, for inventions relating
as the scientific team at Leidos Biomedical Research; the Frederick to work in this manuscript. A. Regev is a co-founder and equity holder
National Laboratory for Cancer Research, especially R. Agarwal and of Celsius Therapeutics, an equity holder in Immunitas and, until 31
Y. Mori; the team at the National Cancer Institute (NCI), especially S. July 2020, a scientific advisory board (SAB) member of Thermo Fisher
Hughes, P. Oberdoerffer and D. Singer; and the Human Tumor Atlas Scientific, Syros Pharmaceuticals, Neogene Therapeutics and Asimov.
Network for helpful discussions. This project has been funded, in From 1 August 2020, A. Regev is an employee of Genentech and
part, by federal funds from the NCI; National Institutes of Health Task has equity in Roche. A. Rotem is an employee of AstraZeneca since
Order HHSN261100039 under contract HHSN261201500003I; as well September 2020 and has equity in AstraZeneca. E.S.B. co-founded
as the DF/HCC Breast Specialized Program in Research Excellence a company that is exploring commercial applications of expansion
(SPORE), grant 1P50CA168504. The content of this publication microscopy. G.N. holds equity in and consults for Akoya Biosciences.
does not necessarily reflect the views or policies of the Department J.G.T.Z. owns stocks in the biotechnology exchange-traded funds
of Health and Human Services, nor does mention of trade names, CNCR, IDNA, IBB and XBI, owns stock in Novo Nordisk and owns
commercial products or organizations imply endorsement by the US stock in Adaptive Biotechnologies, 2seventy bio and bluebird bio.
Government. R. Agarwal and Y. Mori from Leidos Biomedical Research J.J-V. is a contractor at Genentech since 2021. M.S. is a contractor at
and S. Hughes and P. Oberdoerffer from the NCI were periodically Genentech since November 2020. O.R.-R. is a co-inventor on patent
Nature Medicine

Article https://doi.org/10.1038/s41591-024-03215-z
applications filed by the Broad Institute for inventions related to Supplementary information The online version contains supplementary
single-cell genomics. She has given numerous lectures on the subject material available at https://doi.org/10.1038/s41591-024-03215-z.
of single-cell genomics to a wide variety of audiences and, in some
cases, has received remuneration to cover time and costs. O.R.-R. is Correspondence and requests for materials should be addressed to
an employee of Genentech since 19 October 2020 and has equity in Johanna Klughammer, Daniel L. Abravanel, Aviv Regev or Nikhil Wagle.
Roche. S.J.R. is a member of the SAB of Immunitas Therapeutics and
receives research funding from Bristol Myers Squibb and Kite/Gilead. Peer review information Nature Medicine thanks Daniel Stover and the
X.Z. is a co-founder of and consultant for Vizgen. The other authors other, anonymous, reviewer(s) for their contribution to the peer review
declare no competing interests. of this work. Primary Handling Editor: Ulrike Harjes, in collaboration
with the Nature Medicine team.
Additional information
Extended data is available for this paper at Reprints and permissions information is available at
https://doi.org/10.1038/s41591-024-03215-z. www.nature.com/reprints.
Nature Medicine

Article https://doi.org/10.1038/s41591-024-03215-z
Extended Data Fig. 1 | Overview of biopsy sample handling and profiling methods. a) Flow diagram outlining biopsy enrollment and allocation. b) Table outlining
the key characteristics and design parameters of the profiling methods employed in this study.
Nature Medicine

Article https://doi.org/10.1038/s41591-024-03215-z
Extended Data Fig. 2 | Quality statistics overview for sc/snRNA-Seq and distribution of the indicated quality measures for the indicated spatial methods,
spatial methods. a) Box- and violin plots depicting the distribution of the stratified by cell type compartment (malignant, stromal, lymphoid, myeloid).
indicated quality measures for snRNA-Seq and scRNA-Seq data, stratified by cell N indicates observations (cells, beads, or bins) or tissue sections according to
type compartment (malignant, stromal, lymphoid, myeloid). N indicates cells or the axis labels.
biopsy samples according to the axis labels. b) Box- and violin plots depicting the
Nature Medicine

Article https://doi.org/10.1038/s41591-024-03215-z
Extended Data Fig. 3 | See next page for caption.
Nature Medicine

Article https://doi.org/10.1038/s41591-024-03215-z
Extended Data Fig. 3 | Cell type characterization of the sc/snRNA-Seq data. published cell subtype signatures17 across cells of the annotated broader cell types.
a, b) Stacked violin plots depicting the expression of the top 5 cell type marker e) Stacked barplot showing the cell type composition for biopsies of bone and
genes for each of the indicated cell types, detected by 1 vs. all differential brain metastasis. f) Dot plots depicting the expression of genes reported to be
expression analysis for the snRNA-Seq data (panel a) and scRNA-Seq data implicated in bone metastasis (Che.: Chen201727, Kang200324, Jo.:Jones200625,
(panel b). c) Heat map depicting the number of cells of each cell type detected G.:Guise199623, W.:Westbrook201828, Joh.:Johnson201626) across cell types and
in each of the samples. The color scale corresponds to the indicated respective metastatic sites covered in the snRNA-Seq (left) and scRNA-Seq (right) dataset,
number of cells. d) Dot plots depicting the expression level (mean expression) respectively.
and frequency (fraction of expressing cells) of the indicated previously
Nature Medicine

Article https://doi.org/10.1038/s41591-024-03215-z
Extended Data Fig. 4 | Copy number aberration (CNA) detected in the sc/ same time but processed with snRNA-Seq and scRNA-Seq respectively.
snRNA-Seq data. a,b) CNA heatmaps across malignant cells, grouped by sample, e) CNA heatmaps for both samples from patient 862. Samples were taken from
for snRNA-Seq data (panel a) and scRNA-Seqdata (panel b) c) CNA heatmaps for the same breast lesion but 220 days apart, and processed with snRNA-Seq. f) CNA
both samples from patient 223. Samples were taken from different liver lesions, heatmaps for both samples from patient 887. Samples were taken from the same
300 days apart and processed with snRNA-Seq. d) CNA heatmaps for both axilla lesion but 200 days apart, and processed with snRNA-Seq.
samples from patient 262. Samples were taken from the same liver lesion at the
Nature Medicine

Article https://doi.org/10.1038/s41591-024-03215-z
Extended Data Fig. 5 | Expression of malignant hallmark signatures in the malignant sc/snRNA-Seq data. a, b) Dot plots depicting the expression level
(mean expression) and variability (standard deviation) of the indicated hallmark gene sets in MSigDB65,66 across the malignant cells in each of the indicated samples,
separately for snRNA-Seq (panel a) and scRNA-Seq data (panel b).
Nature Medicine

Article https://doi.org/10.1038/s41591-024-03215-z
Extended Data Fig. 6 | Malignant expression programs as identified by iNMF. a) Clustered heatmap of pairwise correlations across all 20 malignant expression
programs, represented by relative gene importance, detected by iNMF in the snRNA-Seq data (frozen) and scRNA-Seq data (fresh), each.
Nature Medicine

Article https://doi.org/10.1038/s41591-024-03215-z
Extended Data Fig. 7 | Integration of snRNA-Seq and scRNA-Seq data in low-dimensional space. a) UMAPs depicting all observations from the sc/snRNA-Seq data
based on their unaligned, BBKNN integrated, or Harmony integrated, dimensionality-reduced transcriptomes. Colored by method, Leiden clusters (resolution: 0.4),
samples, and cell types. Samples from the same patient are marked.
Nature Medicine

Article https://doi.org/10.1038/s41591-024-03215-z
Extended Data Fig. 8 | Correspondence of cell type composition across method (snRNA-Seq or sc RNAseq). The individual data points are overlaid.
profiling methods and annotations. a) Boxplots depicting the correlation d) Heatmap depicting for the segmented MERFISH data, the congruence of
of cell type composition between sc/snRNA-Seq and spatial methods, for each cell type annotations based on manual cluster analysis/marker expression
biopsy, stratified by annotation method (TACCO-OT or RCTD). The individual (de-novo) and automated sn/scRNA-Seq-based annotation by TACCO-OT or
data points are overlaid. N indicates number of sample-pairs. b) Spatial scatter RCTD, respectively. Numbers indicate the number of cells with the respective
plots displaying the correlation between cell type compositions within 100×100 annotation combination. e) UMAPs of all cell-segmented MERFISH data based
μm bins as measured by the indicated pairs of methods in the 514-6760 biopsy. on their expression profiles, with observations colored by cell type as annotated
c) Boxplots depicting the correlation of cell type composition between sc/snRNA- based on cluster analysis/marker expression (de-novo), or annotation transfer
Seq and spatial methods, for each biopsy, stratified by single-cell profiling from sc/snRNA-Seq using TACCO-OT or RCTD respectively.
Nature Medicine

Article https://doi.org/10.1038/s41591-024-03215-z
Extended Data Fig. 9 | Characterization of macrophage subsets based Pearson correlation of scaled Leiden cluster-wise expression profiles across
on expression states across methods. a) Spatial scatter plot overlaid onto methods. Method and cluster ID (as in panel b) are indicated. d) Boxplots
H&E images depicting the expression levels of CD163 in macrophages for all depicting the expression of macrophage marker and function genes in the
biopsies, based on cell-segmented MERFISH data. b) UMAPs of all observations method-specific macrophage clusters grouped in cross-method cluster 1 (N = 15)
confidently annotated as macrophages across biopsies based on their unaligned and 2 (N = 20) according to panel c). Genes are ordered by the median difference
or harmony sample-integrated expression profiles, colored by sample/patient between cross-method cluster 1 and 2. N = method-specific clusters.
or Leiden clusters (resolution: 0.6). c) Clustered heatmap depicting the pairwise
Nature Medicine

Article https://doi.org/10.1038/s41591-024-03215-z
Extended Data Fig. 10 | Macrophage subset marker gene expression. a) Dot as in Extended Data Fig. 9b for all methods as indicated. Side-barplots indicate
plots depicting the scaled expression (by gene, across clusters) and fraction of the number of cells in each cluster. b) Heatmap of scaled (across clusters) gene
expressing cells of macrophage marker and function genes as well as marker expression showing the top up to five differentially expressed genes (FDR < 0.05,
genes for other cell types and differentially expressed genes between clusters log-fold change > 1.5) between the indicated cell-segmented MERFISH clusters.
Nature Medicine