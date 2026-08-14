Article
Dysregulation of brain and choroid plexus
cell types in severe COVID-19
https://doi.org/10.1038/s41586-021-03710-0 Andrew C. Yang1,2,3,11, Fabian Kern4,11, Patricia M. Losada3, Maayan R. Agam3,
Christina A. Maat3, Georges P. Schmartz4, Tobias Fehlmann4, Julian A. Stein5,
Received: 20 October 2020
Nicholas Schaum3, Davis P. Lee3, Kruti Calcuttawala3, Ryan T. Vest3, Daniela Berdnik3,
Accepted: 7 June 2021 Nannan Lu3, Oliver Hahn3, David Gate3, M. Windy McNerney6, Divya Channappa3,
Inma Cobos3,7, Nicole Ludwig8, Walter J. Schulz-Schaeffer5, Andreas Keller3,4,12 ✉ &
Published online: 21 June 2021
Tony Wyss-Coray2,3,9,10,12 ✉
Check for updates
Although SARS-CoV-2 primarily targets the respiratory system, patients with and
survivors of COVID-19 can suffer neurological symptoms1–3. However, an unbiased
understanding of the cellular and molecular processes that are affected in the brains
of patients with COVID-19 is missing. Here we profile 65,309 single-nucleus
transcriptomes from 30 frontal cortex and choroid plexus samples across 14 control
individuals (including 1 patient with terminal influenza) and 8 patients with COVID-19.
Although our systematic analysis yields no molecular traces of SARS-CoV-2 in the
brain, we observe broad cellular perturbations indicating that barrier cells of the
choroid plexus sense and relay peripheral inflammation into the brain and show that
peripheral T cells infiltrate the parenchyma. We discover microglia and astrocyte
subpopulations associated with COVID-19 that share features with pathological cell
states that have previously been reported in human neurodegenerative disease4–6.
Synaptic signalling of upper-layer excitatory neurons—which are evolutionarily
expanded in humans7 and linked to cognitive function8—is preferentially affected in
COVID-19. Across cell types, perturbations associated with COVID-19 overlap with
those found in chronic brain disorders and reside in genetic variants associated with
cognition, schizophrenia and depression. Our findings and public dataset provide a
molecular framework to understand current observations of COVID-19-related
neurological disease, and any such disease that may emerge at a later date.
Patients with COVID-19 can suffer neurological and psychiatric symp- Here we characterized the transcriptomes of 65,309 nuclei isolated
toms that range from loss of smell and headache to encephalitis and from the brains of 14 control individuals and 8 patients with COVID-
stroke1–3,9–11. These symptoms are more prevalent in patients who are 19 (Fig. 1a, Supplementary Table 1). We created an interactive data
hospitalized1,12,13 and may persist as ‘long COVID’, which consists of browser (https://twc-stanford.shinyapps.io/scRNA_Brain_COVID19)
‘brain fog’, difficulty in concentrating and fatigue14,15. to provide researchers with a comprehensive resource to further
Cellular and molecular approaches are required to understand the investigate the molecular mechanisms of the effects of SARS-CoV-2
neurological changes that may contribute to symptoms reported in on the brain.
patients with COVID-19. Neuropathology may arise from direct virus
neuroinvasion or indirectly from peripheral infection and its attendant
immune response16. Thus, much attention has been paid to whether Cortex and choroid plexus cell types
SARS-CoV-2 can be detected in the brain, which has yielded inconsist- We generated 38,217 single-nucleus gene-expression profiles from the
ent results9,17–21. Critically, a comprehensive assessment across specific medial frontal cortex (8 control individuals and 8 patients with COVID-
cell types in the brain affected by severe COVID-19 is missing. This is in 19) and detected a median of 1,918 genes per nucleus, consistent with
part because the high-quality, fresh-frozen human brain tissue from recent studies5,8,24,25 (Fig. 1b, Extended Data Fig. 1a). Our sample sizes
patients with COVID-19 needed for single-cell transcriptomic studies is were similar to or greater than those reported in previous COVID-19
largely inaccessible, and methods to isolate human brain barrier cells or brain single-nucleus RNA-sequencing (snRNA-seq) studies24–26. The
have only recently emerged22,23. samples in the control and COVID-19 groups were from individuals
1Department of Bioengineering, Stanford University School of Medicine, Stanford, CA, USA. 2ChEM-H, Stanford University, Stanford, CA, USA. 3Department of Neurology and Neurological
Sciences, Stanford University School of Medicine, Stanford, CA, USA. 4Chair for Clinical Bioinformatics, Saarland University, Saarbrücken, Germany. 5Institute for Neuropathology, Saarland
University Hospital and Medical Faculty of Saarland University, Homburg, Germany. 6Department of Psychiatry, Stanford University School of Medicine, Stanford, CA, USA. 7Department of
Pathology, Stanford University School of Medicine, Stanford, CA, USA. 8Department of Human Genetics, Saarland University, Homburg, Germany. 9Wu Tsai Neurosciences Institute, Stanford
University, Stanford, CA, USA. 10Paul F. Glenn Center for the Biology of Aging, Stanford University School of Medicine, Stanford, CA, USA. 11These authors contributed equally: Andrew C. Yang,
Fabian Kern. 12These authors jointly supervised this work: Andreas Keller, Tony Wyss-Coray. ✉e-mail: andreas.keller@ccb.uni-saarland.de; twc@stanford.edu
Nature | Vol 595 | 22 July 2021 | 565

Article
CHI3L1 B2M
GFAP CRYAB
IFITM3 JAK1
CD14 Ast. Oli. B2M
CD74 TNC
CTSB HAP1
Exc. n.In. n.
VAMP2 CHL1
ATP6V0C RBMS3
STMN2 DNAJB1
Macrophage
(2%)
Endothelial PRLRhigh
(1%)
Glial (1%) MThigh
GPX3high Epithelial
Mesenchymal (12%) (78%)
SLC26A3high
Ependymal
Neural (2%)
(4%)
between 55 and 91 years of age and matched for tissue dissection or influenza was interstitial pneumonia after more than two weeks of
area, tissue and RNA quality (Extended Data Fig. 1b, c, Supplemen- mechanical ventilation. Samples were not confounded by technical or
tary Table 1). The cause of death for nearly all patients with COVID-19 batch artefacts (Extended Data Fig. 2).
566 | Nature | Vol 595 | 22 July 2021
.caM/.ciM
OPC
a c
Medial
frontal
gyrus
Choroid
plexus
Age 50 95
200
0
snoitcesretnI
Ast.
Mic.
Oli.
OPC
Exc. n.
Interneuron
sGED
tcnitsiD
b d
e
10
5
0
–5
−10 −5 0 5
2
PAMU
OPC
(7%) SV2C
in. neuron (2%)
VIP in. neuron Microglia
(5%) (5%)
10 Oligodendrocyte
(27%) SST in. PV in. NRGN
neuron neuron neuron
(2%) (3%) (5%)
Endothelial 0
(1%)
L2/3 exc. L5/6 CC exc.
neuron neuron (2%)
(14%)
−10 Astrocyte
(15%) L5/6 exc. L4 exc. neuron (1%)neuron (10%)
−10 −5 0 5 10
UMAP 1
2
PAMU
0 250
f
UMAP 1
2ECA GSB 1PRN 2PRN 2SSRPMT
A11SSRPMT B11SSRPMT
NIRUF BSTC LSTC E6YL 1MTIFI 2MTIFI 3MTIFI 1RANFI 2RANFI
Docking Processing Viral defence
Endothelial
Epithelial
Mesenchymal
Ependymal
Glial
Macrophage
Neural
Astrocyte
Endothelial
Oligodendrocyte
OPC
Microglia
L2/3
L4
L5/6
L5/6 CC
NRGN neuron
PV
SST
SV2C
VIP
suxelp
diorohC
xetroC yrotaticxE snoruen
snoruenretnI
Tissue
preparation
snRNA-seq
30 samples (22 patients) IHC Controls (14) Flu
COVID-19 (8)
Total DEGs
Avg log FC CPM
≥1.0 0
0.5 300 0 600 –0.5 900
≤–1 1,200
Fig. 1 | Overview of diverse brain and choroid plexus cell types captured correction). d, Cell-type specificity of cortical DEGs. UpSet plot showing a
from post-mortem tissue from patients with COVID-19. a, Study design. matrix layout of DEGs shared across and specific to each cell type. Each matrix
Coloured triangles denote the brain regions that were studied for each patient. column represents either DEGs specific to a cell type (single circle with no
IHC, immunohistochemistry. b, Uniform manifold approximation and vertical lines) or DEGs shared between cell types, with the vertical line
projection (UMAP) of 38,217 nuclei from the medial frontal cortex of 8 control indicating the cell types that share that given DEG. Top, bar graph displays the
individuals (including 1 patient with influenza) and 8 patients with COVID-19. number of DEGs in each combination of cell types. Right, bar graph displays the
As in previous reports5,25,46, the ‘endothelial’ cluster also exhibits vascular total number of DEGs for a given cell type. e, UMAP of 27,092 nuclei from the
mural cell markers and perivascular cells (perivascular fibroblast-like cells and lateral choroid plexus of 14 individuals (n = 7 control individuals (including 1
perivascular macrophages) are not efficiently captured. exc., excitatory; in., patient with influenza); n = 7 patients with COVID-19; MAST with default
inhibitory; OPC, oligodendrocyte precursor cell. c, Examples of DEGs in settings). f, Expression profiles (counts per million reads mapped (CPM))
COVID-19 (n = 7 control individuals (without viral infection); n = 8 patients with (circle size) and differential expression in patients with COVID-19 (average
COVID-19; MAST with default settings): excitatory neurons (exc. n.), inhibitory log-transformed fold change (avg log FC)) (colour) for genes relevant to
neurons (in. n.), astrocytes (ast.), oligodendrocytes (oli.), OPCs, and microglia SARS-CoV-2 entry into the brain16. The highlighted region indicates the
and macrophages (mic./mac.). DEGs defined as log-transformed fold consistent upregulation of the antiviral defence gene IFITM3 in choroid and glia
change > 0.25 (absolute value) and adjusted P value < 0.05 (Bonferroni limitans brain-barrier cells.

| a   |            |        |       | c                |         |     |        |                     |     |        |
| --- | ---------- | ------ | ----- | ---------------- | ------- | --- | ------ | ------------------- | --- | ------ |
|     |            |        |       |                  | Choroid |     | Cortex | Choroid             |     | Cortex |
|     | Epithelial | IFITM3 | STAT3 |                  |         |     |        |                     |     |        |
|     |            |        |       | sdaer 2-VoC-SRAS | 10      | 10  |        | sdaer 2-VoC-SRAS 10 | 10  |        |
NQO1 SDC4
|         |             |     |           |      | 8              | 8       |            | 8        | 8      |        |
| ------- | ----------- | --- | --------- | ---- | -------------- | ------- | ---------- | -------- | ------ | ------ |
|         |             |     |           |      | 6              | 6       |            | 6        | 6      |        |
|         | IFITM3      | Up  | C3        |      |                |         |            |          |        |        |
|         |             |     |           |      | 4              | 4       |            | 4        | 4      |        |
|         | C1S         |     | STAT3     |      |                |         |            |          |        |        |
|         |             |     |           |      | 2 0            | 0 2     | 0 0        | 2 0      | 0 2    | 0 0    |
|         | ZFP36       |     | OSMR      |      |                |         |            |          |        |        |
|         |             |     |           |      | 0              | 0       |            | 0        | 0      |        |
|         |             |     |           |      | l D-19         |         | l D-19     | l D-19   |        | l D-19 |
| Choroid |             |     |           |      | Contro         | Contro  |            | Contro   | Contro |        |
|         |             |     |           |      | VI             |         | VI         | VI       |        | VI     |
| plexus  | Mesenchymal |     | Ependymal |      | O              |         | O          | O        |        | O      |
|         |             |     |           |      | C              | C       |            | C        |        | C      |
| b       |             |     |           | d    |                | Control |            | COVID-19 |        |        |
|         | IFITM3      |     | C7        |      |                |         | CXCL       |          |        |        |
|         | egnahc dloF | 5   |           |      | Epi. Mes.Epen. |         | signalling |          |        |        |
|         | 10          | 4   |           |      |                | Glial   |            |          |        |        |
|         |             | 3   |           |      |                |         | Mac.       |          |        |        |
|         |             |     |           |      | Endo.          |         | Neural     |          |        |        |
|         | 5           | 2   |           |      |                |         |            |          |        |        |
|         |             | 1   |           | NRGN |                |         |            |          |        |        |
|         |             |     |           |      |                |         | Ast.       |          |        | Ast.   |
|         | 0           | 0   |           | VIP  |                |         |            |          |        |        |
|         |             |     |           |      |                |         | Oli.       |          |        | Oli.   |
|         | STAT3       |     | NQO1      | SV2C |                |         |            |          |        |        |
|         | egnahc dloF | 4   |           |      | SST            |         | OPC        |          |        | OPC    |
|         | 2           |     |           |      |                |         | Endo.      |          |        |        |
|         |             | 3   |           |      | PV             |         |            |          |        |        |
|         |             | 2   |           |      |                |         | Mic.       |          |        |        |
|         | 1           |     |           |      | L5/6           |         | L2/3       |          |        |        |
|         |             | 1   |           |      |                | L5/6 L4 |            |          |        |        |
CC
|     | 0   | 0   |     |     |     |     | CCL |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
signalling
ZFP36
SDC4
|     | egnahc dloF 5 | 8   |     |     |     |     |     |     |     |     |
| --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
4
6
3
|     | 2   | 4   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
2
1
|     | 0            | 0   |              |     |     |     |       |              |     |       |
| --- | ------------ | --- | ------------ | --- | --- | --- | ----- | ------------ | --- | ----- |
|     | Control D-19 |     | Control D-19 |     |     |     | C h o | r o i d      |     | M ic. |
|     | OVI          |     | OVI          |     |     |     |       |              |     | L2/ 3 |
|     | C            |     | C            |     |     |     | C o   | r t e x L5/6 | L4  |       |
Fig. 2 | Brain-barrier inflammation in patients with COVID-19 does not  n = 7 control, n = 7 COVID-19 (cortex). Bulk RNA-seq (after viral RNA isolation):
require direct replicative infection. a, Examples of inflammation-related  n = 7 control, n = 4 COVID-19 (choroid plexus); n = 5 control, n = 4 COVID-19
DEGs in the choroid plexus of patients with COVID-19 (n = 6 control individuals  (cortex). d, Circle plot showing the number of statistically significant
(without viral infection); n = 7 patients with COVID-19; MAST with default  intercellular signalling interactions for the CXCL and CCL pathway family of
settings). DEGs defined as log-transformed fold change > 0.25 (absolute value)  molecules in control individuals compared to patients with COVID-19
and adjusted P value < 0.05 (Bonferroni correction). b, Validation of predicted  (permutation test, CellChat32; n = 8 control individuals (including patients with
choroid plexus DEGs by RT–qPCR (n = 6 control individuals (without viral  influenza); n = 8 patients with COVID-19 (cortex); and n = 7 control individuals
infection), n = 7 patients with COVID-19; two-sided Mann–Whitney t-test;  (including patients with influenza); n = 7 patients with COVID-19 (choroid
mean ± s.e.m.). Genes chosen for validation are either immediately related to  plexus)). Each circle (colour) represents one cell type; edges connecting circles
SARS-CoV-2 (IFITM3) or genes with log-transformed fold changes similar to  represent significant intercellular signalling inferred between those cell types.
those of IFITM3 (NQO1), to assess the robustness of snRNA-seq thresholds.   Circles and edges are normalized to the number of cells for a given cell type and
P values P = 0.0023 (IFITM3), 0.0484 (C7), 0.0350 (STAT3), 0.0140 (NQO1),  inferred strength of signalling, respectively. Cell types labelled on the right
0.0082 (ZFP36) and 0.0734 (SDC4). c, snRNA-seq (left) or bulk RNA-seq (right)  correspond to signalling pathways increased in COVID-19. Endo., endothelial;
of choroid plexus and cortex from control individuals or patients with  epen., ependymal; epi., epithelial; mes., mesenchymal.
COVID-19 (no reads). snRNA-seq, n = 7 control, n = 7 COVID-19 (choroid plexus);
Our unsupervised clustering of nuclear transcriptomes yielded 14 cell  the human choroid plexus, in health or disease22. We thus developed a
types, including subtypes of excitatory neurons and interneurons that  method (Methods) that yielded 27,092 nuclei across 7 major epithelial,
express previously established marker genes (Extended Data Fig. 3) and  mesenchymal, immune, ependymal and glial cell types (7 control indi-
proportional to previous snRNA-seq data from adult human cortex5,8,24,25  viduals and 7 patients with COVID-19) (Fig. 1e, Extended Data Fig. 3b,
(Extended Data Figs. 1–3, Supplementary Table 2). Supplementary Table 4). With capture of both brain parenchymal and
We collapsed nuclei into 6 broad cell types, and identified 786 unique  barrier cell types, we assessed the expression and disease perturbation
of genes related to SARS-CoV-2 entry, docking and defence16. Similar
differentially expressed genes (DEGs) that implicated all major cell types
(Fig. 1c, Extended Data Fig. 4). DEGs strongly correlated with alternative  to brain vascular cells, choroid barrier cells robustly expressed several
pseudobulk methods (but with greater statistical power (Extended  genes that are relevant to SARS-CoV-2 brain entry (Fig. 1f, Extended
Data Fig. 5)); and showed no significant overlap with genes affected by  Data Fig. 7). We observed a broad upregulation of the antiviral defence
post-mortem delay to autopsy27 (Extended Data Fig. 6). Broadly, the strong- gene IFITM3 across choroid and glia limitans barrier cells in patients
est effects were seen in astrocytes and other glia, marked by inflammatory  with COVID-19, consistent with potential SARS-CoV-2 infection. IFITM3
serves as the first line of defence against viral infection28 and its upregu-
and dysregulated homeostatic pathways (Fig. 1c, Extended Data Fig. 4).
The majority of DEGs were perturbed in only a single cell type (about 80%)  lation is a marker of SARS-CoV-2 infection across public datasets29.
(Fig. 1d). Several DEGs upregulated in one cell type were downregulated in
others (Supplementary Tables 3, 5). Overall, these data demonstrate that
all major brain parenchymal cell types are affected in COVID-19. Brain barriers relay inflammation
Recent reports have found SARS-CoV-2 infection of cultured choroid  We observed a broad upregulation of inflammatory genes across vari-
plexus organoids20,21 but to our knowledge no snRNA-seq study exists on
ous interferon (IFITM3 and STAT3), complement (C1S, C3 and so on) and
Nature | Vol 595 | 22 July 2021 | 567

Article
| a   | Control |     | COVID-19 |     | d   |     | Control     |     | COVID-19 |           |
| --- | ------- | --- | -------- | --- | --- | --- | ----------- | --- | -------- | --------- |
|     | Cluster |     |          |     |     |     | Homeostatic |     |          | COVID-19- |
|     | 4       |     |          |     |     |     | markers     |     |          | enriched  |
0
|     |     |     |     |     |     | 2.5 | P2RY12 |     |     | C1QC |
| --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | ---- |
|     |     |     |     |     |     |     | IRAK3  |     |     | FTL  |
CX3CR1
| 2 PAMU | 0   |     |     |     | 2 PAMU |     |       |     |     | CD14 |
| ------ | --- | --- | --- | --- | ------ | --- | ----- | --- | --- | ---- |
|        |     |     |     |     |        | 0   | MEF2C |     |     | FTH1 |
RIPK1
|     | 4   |     |     |     |     | –2.5 |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- |
Cluster 1
–5.0
|     | –5 0   | 5   | –5 0   | 5   |     | –6 –3 | 0 3    | 6–6 | –3 0   | 3 6 |
| --- | ------ | --- | ------ | --- | --- | ----- | ------ | --- | ------ | --- |
|     | UMAP 1 |     | UMAP 1 |     |     |       | UMAP 1 |     | UMAP 1 |     |
| b   |        | c   |        |     | e   |       | f      |     |        |     |
1
|     |     |     | sllec enummi fo tnec reP 2.5 |     |     | 100 |     |     |     | Pseudotime |
| --- | --- | --- | ---------------------------- | --- | --- | --- | --- | --- | --- | ---------- |
sllec enummi fo tnec reP 80
|     |     |     |     |     | ailgorcim fo tnec reP |     |        |     |     | 10  |
| --- | --- | --- | --- | --- | --------------------- | --- | ------ | --- | --- | --- |
|     |     |     | 2.0 |     |                       | 80  |        |     |     |     |
|     | 60  |     |     |     |                       |     |        |     |     | 5   |
|     |     |     | 1.5 |     |                       | 60  | 2 PAMU | 1   |     | 0   |
40
|     |     |     | 1.0 |     |     | 40  |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
20
|     |     |     | 0.5 |     |     | 20 Flu |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- |
|     | Flu |     | Flu |     |     |        |     |     |     |     |
2
|                   | 0            |     | 0        |      |     | 0       |      |     |          |     |
| ----------------- | ------------ | --- | -------- | ---- | --- | ------- | ---- | --- | -------- | --- |
|                   | Control D-19 |     | Control  | D-19 |     | Control | D-19 |     |          |     |
|                   | OVI          |     | OVI      |      |     | OVI     |      |     |          |     |
|                   | C            |     | C        |      |     | C       |      |     | UMAP 1   |     |
| g                 | Control      |     | COVID-19 |      |     | h       |      |     |          |     |
|                   |              |     |          |      |     | DAM,    |      |     | COVID-19 |     |
| 86DC nilyxotameaH |              |     |          |      |     | ARM,    | 484  | 340 |          |     |
41
|     |     |     |     |     |     | Mic1 |           |       |     | Overlap  |
| --- | --- | --- | --- | --- | --- | ---- | --------- | ----- | --- | -------- |
|     |     |     |     |     |     |      | APOE CD14 | RIPK1 |     |          |
Enrich = 4.4×
|     |     |     |     |     |     |     | TREM2 C1QC | LRP1B |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ----- | --- | --- |
P = 2.3 × 10–15
|     |     |     |     |     |     |     | CD9 FTH1 | PTPN1 |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | ----- | --- | --- |
Fig. 3 | A neuroinflammatory COVID-19 milieu marked by disease-  cluster associated with COVID-19 are shown in light blue. f, Pseudotime
associated microglia. a, UMAP of immune cells captured in the human frontal  trajectory (Methods) indicated in graded purple (low) to yellow (high), plotting
cortex, split by control individuals (including a patient with influenza) (n = 8)  the emergence of the microglial cluster associated with COVID-19. Numbers
(red) and patients with COVID-19 (n = 8) (light blue). Cells are coloured by  indicate original source population (1) and the newly emerged population in
cell-type subcluster (red cluster defined by homeostatic markers; light blue  COVID-19 (2). g, Immunohistochemical staining for the microglial activation
cluster defined by activation markers). b, Quantification of immune cell cluster  marker CD68 (brown) in the frontal medial cortex of a patient with COVID-19,
1 as a proportion of total immune cells (n = 8 control individuals (including a  immediately adjacent to that used for snRNA-seq. Haematoxylin counterstain
patient with influenza (circle marked as ‘flu’)); n = 8 patients with COVID-19,  (blue). Scale bars, 20 μm. Immunohistochemical stains are representative of at
two-sided Mann–Whitney t-test P = 0.0098; mean ± s.e.m.). c, As in b, but for  least two independent experiments. h, Overlap (hypergeometric test) between
T cells. P = 0.0003. d, e, As in a, b, respectively, but for MRC1− parenchymal
marker genes of Alzheimer’s-disease-associated microglia (DAM, ARM and
Mic1)4–6 and genes that are upregulated in the microglial cluster associated
microglia. P = 0.0343. Unlike macrophages, microglia express low levels of
MRC1 (CD206)34. Examples of genes that are upregulated in the microglial
with COVID-19.
related pathways across choroid plexus cell types (Fig. 2a). Quantitative  qPCR using US Centers for Disease Control and Prevention Emergency
PCR with reverse transcription (RT–qPCR) corroborated significant dif- Use Authorization primers against the N1 and N2 genes of the virus,
ferential expression of tested inflammatory genes as well as other genes  again finding no enrichment in the brains of individuals with COVID-19
predicted to be upregulated by a similar magnitude in COVID-19 (for  (Extended Data Fig. 9b). Some of the samples from the control individu-
example, NQO1 and ZFP36) (Fig. 2b). Immunohistochemical staining  als without viral infection have high cycle counts (between 37 and 40),
also confirmed choroid plexus inflammation (Extended Data Fig. 8).  which in previous work (without such controls) has been interpreted as
Together, these data reveal substantial brain barrier inflammation in  evidence of neuroinvasion9,18. Finally, with the anti-SARS-CoV-2 spike
COVID-19 and validate the reliability of the DEGs that we identified in  (3A2) antibody used for immunohistochemistry (as in previous pub-
our snRNA-seq analysis. lications17,18), we observed signal across the barrier-forming cortical
Brain and choroid cell types express several SARS-CoV-2 entry genes  vasculature, meninges and choroid plexus (Extended Data Fig. 9c,
(Fig. 1f, Extended Data Fig. 7) but claims of neuroinvasion in the litera- d). Specific signal was retained across secondary detection methods
ture have thus far been inconsistent9,17–20. To detect molecular evidence
(Extended Data Fig. 9e, Methods). However, no other antibody—includ-
of SARS-CoV-2, we systematically performed four RNA-based and four  ing those also used in recent publications9,30—yielded specific signal
antibody-based assays across our samples. RNA assays included search- over controls. Therefore, the 3A2 antibody may bind a specific, but
ing for virus-specific reads (Methods) in our snRNA-seq dataset as  non-SARS-CoV-2, antigen.
well as in custom-generated bulk RNA-seq datasets with and without  The inflamed choroid plexus has previously been shown to send
viral RNA enrichment. In no case did we detect SARS-CoV-2-specific  inflammatory signals into the brain, thereby activating parenchymal
glia and impairing cognitive function31. To assess whether similar
RNA in the brain (Fig. 2c, Extended Data Fig. 9a). We confirmed this via
568 | Nature | Vol 595 | 22 July 2021

a
| L2/3 |     |     |     |     | log (FDR) |
| ---- | --- | --- | --- | --- | --------- |
10
| yrotaticxE L4 |     |     |     |     | 25  |
| ------------- | --- | --- | --- | --- | --- |
noruen
| L5/6 |     |     |     |     | 20  |
| ---- | --- | --- | --- | --- | --- |
15
| L5/6 CC |     |     |     |     | 10  |
| ------- | --- | --- | --- | --- | --- |
| VIP     |     |     |     |     | 5   |
noruenretnI
| SV2C |     |     |     |     | 0               |
| ---- | --- | --- | --- | --- | --------------- |
| SST  |     |     |     |     | log-transformed |
FC
PV
0
NRGN neuron
| 0 C 0D 1 AT 1 IP 3 M | 3 1 0 N 1 P1 X1 X 2 BP 1 M 1 A 1 G | 2 AB 2 IF1A MT 3 AP B RGN NS F INK 1 A | P 1A 1B AB3 A C 1 17 1 7 2 5 X1 | B UN 2 V2 A N 1 P 1 MP2 | – 0 . 2    |
| -------------------- | ---------------------------------- | -------------------------------------- | ------------------------------- | ----------------------- | ---------- |
| 6 V V 4G B N A L CH  | D S T N A PL PL T D N AB R B R     | N K N N P P S                          | B 1 B1 R A 2A 6 A A P T         | S S S Y A M A           |            |
| ATP T P 6 B C H      | C L N T C C C G G A K C            | R A                                    | R A R L C 2 S LC S N S          | V V                     | – 0 . 4    |
| A C                  | C                                  |                                        | S                               |                         |            |
| b                    |                                    | d                                      |                                 |                         |            |
|                      | I                                  | ALS                                    |                                 |                         | –log (FDR) |
10
|             | II    | AD           |     |     | 12  |
| ----------- | ----- | ------------ | --- | --- | --- |
|             |       | Brain ageing |     |     | 9   |
| L2/3 IN-VIP |   III |              |     |     |     |
|             |       | MSA          |     |     | 6   |
|             | IV    |              |     |     | 3   |
| L4IN-SV2C   |       | MS           |     |     |     |
|             | V     |              |     |     | 0   |
PD
L5/6 CC
|        | VI   | Narcolepsy |     |     | No. of DEGs |
| ------ | ---- | ---------- | --- | --- | ----------- |
| Cortex | L5/6 | ADHD       |     |     | among GWAS  |
IN-SST
| IN-PVOther | Subcortical | Autism |     |     |     |
| ---------- | ----------- | ------ | --- | --- | --- |
| hemisphere | regions     |        |     |     | 20  |
Bipolar disorder
|     |     | Depression |     |     | 10  |
| --- | --- | ---------- | --- | --- | --- |
Psychosis
| c   |     |     |     |     | 0   |
| --- | --- | --- | --- | --- | --- |
PTSD
Schizophrenia
| –log 10 | (FDR)  |         |     |     |              |
| ------- | ------ | ------- | --- | --- | ------------ |
|         |        | Anxiety |     |     | Neurological |
| 0 10 20 | 80 100 |         |     |     |              |
Suicidality
| Astrocyte |     |     |     |     | Psychiatric |
| --------- | --- | --- | --- | --- | ----------- |
Insomnia
Oli. 10.0 < RDF
Traits
| OPC |     | Neuroticism |     |     |     |
| --- | --- | ----------- | --- | --- | --- |
Risk behaviour
Microglia
Intelligence
Exc. neuron
Cognitive
Interneuron
|     |     | a l       | a l ge li a trocyte | Oli. C o n rneuron |     |
| --- | --- | --------- | ------------------- | ------------------ | --- |
|     |     | e li hy   | m pha icrog         | O P u r            |     |
|     |     | Ep it h c | o                   |  ne                |     |
|     |     | e n       | cr M A s            | c. t e             |     |
|     |     | e s M     | a                   | E x I n            |     |
M
Fig. 4 | Molecular dysfunction in upper-layer neurons and links to long-  P value < 0.05, false-discovery rate (FDR) correction, cumulative
term symptoms. a, Dot plot showing downregulation of synaptic vesicle  hypergeometric test). d, Heat map showing the number of DEGs per cell type
components, especially in L2/3 excitatory neurons in patients with COVID-19  that overlap as GWAS risk variants across psychiatric and neurological diseases
(n = 7 control individuals (without viral infection); n = 8 patients with COVID-19;  and traits from the GWAS catalogue (NHGRI-EBI)43. Significance of overlap is
MAST with default settings). FC, fold change. b, Diagram of cortical neurons  based on FDR-corrected cumulative hypergeometric P values (Benjamini–
captured in this study that have known layer localization. Neuron labels are  Hochberg correction) < 0.05; MAST with default thresholds). AD, Alzheimer’s
colour-coded by layer localization as shaded in a. Figure layout adapted with  disease; ADHD, attention deficit hyperactivity disorder; ALS, amyotrophic
permission from ref. 8. c, Overlap between COVID-19 DEGs and those in chronic  lateral sclerosis; MS, multiple sclerosis; MSA, multiple system atrophy; PD,
CNS diseases (Methods). Dotted line indicates statistical significance (adjusted  Parkinson’s disease; PTSD, post-traumatic stress disorder.
pro-inflammatory relay mechanisms occur in the brains of patients
with COVID-19, we performed cell–cell communication analysis32. We  Disease-associated microglia and astrocytes
observed a strong increase in the choroid-to-cortex network across  We thus sought to evaluate the immune landscape of the brain in
key inflammatory pathways, such as the CCL and CXCL family of  individuals with COVID-19. We first analysed cortical immune cells,
chemokines from the choroid plexus epithelium to brain astrocytes,  which contain mostly microglia but also lesser fractions of perivascular
oligodendrocytes, microglia and layer (L) 2/3 and L4 excitatory neurons  macrophages (MRC1+, which encodes macrophage-specific mannose
(Fig. 2d, Extended Data Fig. 10). Complement pathway signalling from  receptor CD20634) and T cells (CD247+, which encodes the T cell recep-
the choroid plexus to brain microglia (the resident immune cells of  tor CD3ζ protein). Our unsupervised clustering revealed the pres-
the brain) was also predicted to increase in the brains of patients with  ence of a subpopulation of immune cells associated with COVID-19
COVID-19. Excessive complement signalling in microglia has previously  (Fig. 3a), which was significantly enriched at both the per-nucleus and
been linked to premature neuronal synapse pruning in neurodegen- per-patient level (Fig. 3b). The emergence of disease-associated clus-
erative disease33. Together, although we could not specifically detect  ters reflects strong perturbations across the transcriptome. Similarly,
virus RNA or protein in our brain samples, these results suggest that  although we did not find cortical T cells in any of our samples from
peripheral SARS-CoV-2 infection inflames brain-barrier cells such as  control individuals (without viral infection or with terminal influenza),
those of the choroid plexus; and that this inflammation is then relayed  we detected them in all but one of the patients with COVID-19 (Fig. 3c).
into the brain parenchyma. Aberrant T cell infiltration into the mouse brain has previously been
Nature | Vol 595 | 22 July 2021 | 569

Article
reported to be sufficient to promote neuroinflammation and impair To investigate the potential pathologies that underlie reported
neurogenesis35. neurological symptoms of long COVID, we analysed the intersection
To study microglia, we focused on the MRC1−CD247− immune cell between COVID-19 DEGs across brain cell types with those that have
subset to eliminate confounds from perivascular macrophages and previously been described in chronic CNS diseases, such as Alzhei-
T cells. Library quality was not affected upon restricting analyses to the mer’s disease5, multiple sclerosis26, Huntington’s disease42 and autism
MRC1− subset of microglia (Methods). We clustered 1,814 MRC1− micro- spectrum disorder8. Although neuronal perturbations in COVID-19
glia, which revealed a distinct microglial subpopulation associated were unique compared to those in chronic CNS diseases, the overlap
with COVID-19 (Fig. 3d) that was significant at both the per-nucleus in glial cells was particularly strong (Fig. 4c, Supplementary Table 7).
and per-patient level (Fig. 3e). This subpopulation was marked by To further determine the enrichment of COVID-19 DEGs within
expression of microglial activation genes previously associated with genetic variants associated with complex traits and diseases in a
human disease4,5, such as complement C1QC, CD74, FTL and FTH1, and cell-type-specific fashion, we obtained genome-wide association study
downregulation of the homeostatic markers including P2RY12 (Fig. 3d, (GWAS) summary statistics for neurological and psychiatric disorders
Supplementary Table 6). Trajectory analysis revealed that the microglia and neurobehavioural traits43 (Supplementary Table 8). We found a
cluster associated with COVID-19 emerged from the parent homeostatic strong enrichment of DEGs residing within GWAS hits of neurological
population (Fig. 3f), which further suggests that these microglia emerge disorders and traits, especially in cognition, schizophrenia and depres-
in response to an increasingly inflamed central nervous system (CNS) sion (Fig. 4d). Together, these data suggest that COVID-19 may partially
environment. Our in situ staining confirmed the enriched presence recapitulate the pathological processes of various CNS diseases.
of activated CD68+ parenchymal microglia in the brains of patients
with COVID-19 as compared to those of control individuals (Fig. 3g,
Discussion
Extended Data Fig. 11); at times, these microglia form nodules that have
previously been linked to viral encephalitis36 and myelin degeneration Previous snRNA-seq studies have begun to elucidate the
in ageing mice37. cell-type-specific perturbations and interactions involved in several
Microglial subclusters that are associated with disease have been CNS disorders5,8,25,26,42. Here, by combining sequencing of 65,309 nuclei
identified for various neurodegenerative diseases4,5. A fraction of in both the frontal cortex and choroid plexus, along with confirma-
the genes enriched in the COVID-19-associated microglia cluster tory immunohistochemistry and RT–qPCR, we reveal several major
overlap (P = 2.3 × 10−15, hypergeometric test) with those enriched in neuropathological mechanisms in severe COVID-19. However, there
neurodegenerative-disease-associated microglia (Fig. 3h), including are limitations to consider. Most post-mortem brain tissue from indi-
C1QC and CD14 (which mark microglia associated with Alzheimer’s viduals with COVID-19 is inadequately preserved or immediately fixed
disease). Yet, several genes that have been implicated in neuroinflam- for safety and regulatory reasons, so there is a scarcity of high-quality
mation38 (such as RIPK1) were seen specifically in microglial states tissue available for molecular studies. Also, although we did not detect
associated with COVID-19. Our observations suggest that the micro- SARS-CoV-2 in the choroid plexus or cortex, we cannot exclude the pos-
glial subpopulation enriched in patients with COVID-19 represents a sibility of earlier neuroinvasion that had subsequently been cleared.
distinct microglial state that shares features with—but is ultimately dif- Indeed, the mouse choroid plexus has recently been reported to express
ferent from—microglial cell states that have previously been reported several SARS-CoV-2 entry factors22, which we corroborate in humans
in human neurodegenerative disease. (Supplementary Discussion).
In addition to abnormally activated microglia, we uncovered an astro- There is a precedent for acute viral infections causing long-term
cyte cluster associated with COVID-19 that is marked by established inflammation and dysfunction that predisposes individuals to neu-
inflammation and astrogliosis genes (such as IFITM3 and GFAP) and rodegenerative disease44,45, although not at the scale of the COVID-19
upregulated expression of the secreted neurotoxic factor chitinase pandemic. It will be important to study how the molecular processes
3-like 1 (CHI3L1)39 (Extended Data Fig. 12a–c). Within this astrocyte elucidated here contribute to the COVID-19 neurological symptoms
cluster, we also observed significant dysregulation of genes that sup- and deficits of which we are aware now, and to those that may emerge
port neurotransmission and synaptic organization. By contrast, we did in the years to come.
not observe any new subpopulations for oligodendrocyte lineage cells
(Extended Data Fig. 12d–g). Together, we identify the robust emergence
Online content
of disease-associated microglia and astrocyte subpopulations with dis-
tinct transcriptional profiles in the brains of individuals with COVID-19. Any methods, additional references, Nature Research reporting sum-
maries, source data, extended data, supplementary information,
acknowledgements, peer review information; details of author contri-
Links to long-term CNS dysfunction
butions and competing interests; and statements of data and code avail-
Given the predicted astrocytic impairments in supporting neurotrans- ability are available at https://doi.org/10.1038/s41586-021-03710-0.
mission, we next sought to identify the neuronal subtypes that are
most affected in COVID-19. Although we captured neurons from all
1. Mao, L. et al. Neurologic manifestations of hospitalized patients with coronavirus disease
cortical layers, we found gene-expression changes linked to synaptic 2019 in Wuhan, China. JAMA Neurol. 77, 683–690 (2020).
deficits particularly in L2/3 excitatory neurons and L2/3-residing VIP 2. Yang, X. et al. Clinical course and outcomes of critically ill patients with SARS-CoV-2
pneumonia in Wuhan, China: a single-centered, retrospective, observational study.
interneurons40 (Fig. 4a, b). Specifically, the downregulation of synaptic
Lancet Respir. Med. 8, 475–481 (2020).
genes that mediate neurotransmission (for example, VAMP2, SNAP25 3. Helms, J. et al. Neurologic features in severe SARS-CoV-2 infection. N. Engl. J. Med. 382,
and ATP6V0C) in L2/3 excitatory neurons alongside a concomitant 2268–2270 (2020).
4. Keren-Shaul, H. et al. A unique microglia type associated with restricting development of
upregulation in proximal VIP inhibitory neurons suggests dysfunction
Alzheimer’s disease. Cell 169, 1276–1290 (2017).
in upper-layer cortical circuitry. Such a pattern of dysfunction has pre- 5. Mathys, H. et al. Single-cell transcriptomic analysis of Alzheimer’s disease. Nature 570,
viously been reported in an snRNA-seq study of autism and correlated 332–337 (2019).
6. Sala Frigerio, C. et al. The major risk factors for Alzheimer’s disease: age, sex, and
with cognitive deficits8. L2/3 excitatory neurons are cortico-cortical
genes modulate the microglia response to Aβ plaques. Cell Rep. 27, 1293–1306
projecting and already exhibit sparse action potential firing to gener- (2019).
ate a simple and reliable neural code for associative learning41. Thus, 7. Gidon, A. et al. Dendritic action potentials and computation in human layer 2/3 cortical
neurons. Science 367, 83–87 (2020).
this neuronal population may be particularly sensitive to deficits in
8. Velmeshev, D. et al. Single-cell genomics identifies cell type-specific molecular changes
neurotransmission by COVID-19. in autism. Science 364, 685–689 (2019).
570 | Nature | Vol 595 | 22 July 2021

9. Matschke, J. et al. Neuropathology of patients with COVID-19 in Germany: a post-mortem 29. Hachim, M. Y. et al. Interferon-induced transmembrane protein (IFITM3) is upregulated
case series. Lancet Neurol. 19, 919–929 (2020). explicitly in SARS-CoV-2 infected lung epithelial cells. Front. Immunol. 11, 1372 (2020).
10. Varatharaj, A. et al. Neurological and neuropsychiatric complications of COVID-19 in 153 30. Rockx, B. et al. Comparative pathogenesis of COVID-19, MERS, and SARS in a nonhuman
patients: a UK-wide surveillance study. Lancet Psychiatry 7, 875–882 (2020). primate model. Science 368, 1012–1015 (2020).
11. Ellul, M. A. et al. Neurological associations of COVID-19. Lancet Neurol. 19, 767–783 31. Baruch, K. et al. Aging-induced type I interferon response at the choroid plexus
(2020). negatively affects brain function. Science 346, 89–93 (2014).
12. Romero-Sánchez, C. M. et al. Neurologic manifestations in hospitalized patients with 32. Jin, S. et al. Inference and analysis of cell-cell communication using CellChat. Nat.
COVID-19: the ALBACOVID registry. Neurology 95, e1060–e1070 (2020). Commun. 12, 1088 (2021).
13. Liotta, E. M. et al. Frequent neurologic manifestations and encephalopathy-associated 33. Hong, S. et al. Complement and microglia mediate early synapse loss in Alzheimer
morbidity in Covid-19 patients. Ann. Clin. Transl. Neurol. 7, 2221–2230 (2020). mouse models. Science 352, 712–716 (2016).
14. Office for National Statistics. The prevalence of long COVID symptoms and COVID-19 34. Prinz, M., Erny, D. & Hagemeyer, N. Ontogeny and homeostasis of CNS myeloid cells. Nat.
complications, Office for National Statistics, https://www.ons.gov.uk/news/ Immunol. 18, 385–392 (2017).
statementsandletters/theprevalenceoflongcovidsymptomsandcovid19complications 35. Dulken, B. W. et al. Single-cell analysis reveals T cell infiltration in old neurogenic niches.
(2020). Nature 571, 205–210 (2019).
15. Carfì, A., Bernabei, R. & Landi, F. Persistent symptoms in patients after acute COVID-19. 36. Tröscher, A. R. et al. Microglial nodules provide the environment for pathogenic T cells in
J. Am. Med. Assoc. 324, 603–605 (2020). human encephalitis. Acta Neuropathol. 137, 619–635 (2019).
16. Iadecola, C., Anrather, J. & Kamel, H. Effects of COVID-19 on the nervous system. Cell 183, 37. Safaiyan, S. et al. White matter aging drives microglial diversity. Neuron 109, 1100–1117 (2021).
16–27 (2020). 38. Yuan, J., Amin, P. & Ofengeim, D. Necroptosis and RIPK1-mediated neuroinflammation in
17. Cantuti-Castelvetri, L. et al. Neuropilin-1 facilitates SARS-CoV-2 cell entry and infectivity. CNS diseases. Nat. Rev. Neurosci. 20, 19–33 (2019).
Science 370, 856–860 (2020). 39. Matute-Blanch, C. et al. Chitinase 3-like 1 is neurotoxic in primary cultured neurons. Sci.
18. Meinhardt, J. et al. Olfactory transmucosal SARS-CoV-2 invasion as a port of central Rep. 10, 7118 (2020).
nervous system entry in individuals with COVID-19. Nat. Neurosci. 24, 168–175 (2021). 40. Tremblay, R., Lee, S. & Rudy, B. GABAergic interneurons in the neocortex: from cellular
19. Song, E. et al. Neuroinvasion of SARS-CoV-2 in human and mouse brain. J. Exp. Med. 218, properties to circuits. Neuron 91, 260–292 (2016).
e20202135 (2021). 41. Petersen, C. C. H. & Crochet, S. Synaptic computation and sensory processing in
20. Jacob, F. et al. Human pluripotent stem cell-derived neural cells and brain organoids neocortical layer 2/3. Neuron 78, 28–48 (2013).
reveal SARS-CoV-2 neurotropism predominates in choroid plexus epithelium. Cell Stem 42. Al-Dalahmah, O. et al. Single-nucleus RNA-seq identifies Huntington disease astrocyte
Cell 27, 937–950 (2020). states. Acta Neuropathol. Commun. 8, 19 (2020).
21. Pellegrini, L. et al. SARS-CoV-2 infects the brain choroid plexus and disrupts the 43. Buniello, A. et al. The NHGRI-EBI GWAS catalog of published genome-wide association
blood-CSF barrier in human brain organoids. Cell Stem Cell 27, 951–961 (2020). studies, targeted arrays and summary statistics 2019. Nucleic Acids Res. 47, D1005–D1012
22. Dani, N. et al. A cellular and spatial map of the choroid plexus across brain ventricles and (2019).
ages. Cell 184, 3056–3074 (2021). 44. Hosseini, S. et al. Long-term neuroinflammation induced by influenza a virus infection
23. Yang, A. C. et al. A human brain vascular atlas reveals diverse cell mediators of and the impact on hippocampal neuron morphology and function. J. Neurosci. 38,
Alzheimer’s disease risk. Preprint at https://doi.org/10.1101/2021.04.26.441262 (2021). 3060–3080 (2018).
24. Lake, B. B. et al. Integrative single-cell analysis of transcriptional and epigenetic states in 45. Deleidi, M. & Isacson, O. Viral and inflammatory triggers of neurodegenerative diseases.
the human adult brain. Nat. Biotechnol. 36, 70–80 (2018). Sci. Transl. Med. 4, 121ps3 (2012).
25. Grubman, A. et al. A single-cell atlas of entorhinal cortex from individuals with 46. Zhou, Y. et al. Human and mouse single-nucleus transcriptomics reveal
Alzheimer’s disease reveals cell-type-specific gene expression regulation. Nat. Neurosci. TREM2-dependent and TREM2-independent cellular responses in Alzheimer’s disease.
22, 2087–2097 (2019). Nat. Med. 26, 131–142 (2020).
26. Jäkel, S. et al. Altered human oligodendrocyte heterogeneity in multiple sclerosis. Nature
566, 543–547 (2019). Publisher’s note Springer Nature remains neutral with regard to jurisdictional claims in
27. Dachet, F. et al. Selective time-dependent changes in activity and cell-specific gene published maps and institutional affiliations.
expression in human postmortem brain. Sci. Rep. 11, 6078 (2021).
28. Bailey, C. C., Zhong, G., Huang, I. C. & Farzan, M. IFITM-family proteins: the cell’s first line © The Author(s), under exclusive licence to Springer Nature Limited 2021, corrected
of antiviral defense. Annu. Rev. Virol. 1, 261–283 (2014). publication 2021
Nature | Vol 595 | 22 July 2021 | 571

Article
Methods protocol (10x Genomics), targeting 10,000 nuclei per sample after
counting with a TC20 Automated Cell Counter (Bio-Rad). Thirteen
No statistical methods were used to predetermine sample size. The cycles were applied to brain parenchyma samples to generate cDNA,
experiments were not randomized, and investigators were not blinded and 15 for choroid plexus samples. All samples underwent 15 or 16
to allocation during experiments and outcome assessment. cycles for final library generation. Generated snRNA-seq libraries
were sequenced across two S4 lanes on a NovaSeq 6000 (150 cycles,
Isolation of nuclei from frozen post-mortem medial frontal Novogene).
gyrus
Frozen medial frontal cortex tissue from post-mortem control individu- snRNA-seq quality control
als and patients with COVID-19 was obtained from the Stanford/VA/NIA Raw gene counts were obtained by aligning reads to the hg38 genome
Ageing Clinical Research Center (ACRC) and the Saarland University (refdata-gex-GRCh38-2020-A) using CellRanger software (v.4.0.0)
Hospital Institute for Neuropathology, with approval from local ethics (10x Genomics). To account for unspliced nuclear transcripts, reads
committees. Group characteristics are presented in Supplementary mapping to pre-mRNA were also counted. As previously published, a
Table 1. The protocol for the isolation of nuclei was adapted from previ- cut-off value of 200 unique molecular identifiers was used to select
ous studies5,25,46–48, and performed in a BSL2+ biosafety cabinet wearing nuclei of sufficient complexity for further analysis5. As initial reference,
personal protective equipment (PPE). All procedures were carried the entire dataset was projected onto two-dimensional space using
out on ice or at 4 °C. In brief, 50 mg of post-mortem brain tissue was UMAP on the top 20 principal components50. Three approaches were
dounce-homogenized in 2 ml of Nuclei EZ Prep Lysis Buffer (Sigma, combined for quality control: (1) ambient cell free mRNA contamina-
NUC101) spiked with 0.2 U μl−1 RNase inhibitor (Takara, 2313A) and tion was removed using SoupX51 for each individual sample; (2) outli-
EDTA-free protease inhibitor Cocktail (Roche, 11873580001) before ers with a high ratio of mitochondrial (>5%, <200 features) relative to
incubating on ice for 5 min in a final volume of 5 ml. Homogenized endogenous RNAs and homotypic doublets (>5,000 features) were
tissue was filtered through a 100-μm cell strainer (Falcon, 352360), removed in Seurat 3.2.152; and (3) after scTransform normalization and
mixed with an equal volume of 50% iodixanol density gradient medium integration, doublets and multiplets were filtered out using Doublet-
in PBS (OptiPrep, Sigma-Aldrich, D1556) to make a final concentration Finder with subsequent manual inspection and filtering on the basis
of 25% iodixanol. Thirty per cent iodixanol was layered underneath the of cell-type-specific marker genes53. Similarly, genes detected in fewer
25% mixture. Similarly, 40% iodixanol was layered underneath the 30% than four cells were excluded from the analysis. The core statistical
iodixanol. In a swinging-bucket centrifuge, nuclei were centrifuged for parameters of DoubletFinder (nExp and pK) used to build artificial
20 min at 3,000 r.c.f. After centrifugation, the nuclei were present at the doublets for true doublet classification were determined automatically
interface of the 30% and 40% iodixanol solutions. Isolated nuclei were using recommended settings. The computed nExp and pK values for
resuspended in 1% BSA with 0.2 U μl−1 RNase inhibitor, filtered twice each sample are provided in Supplementary Table 1. After applying
through a 40-μm strainer (Flowmi) and counted on an TC20 automated these filtering steps, the dataset contained 65,309 high-quality nuclei.
cell counter (Bio-Rad) after the addition of Trypan blue. We did not use
statistical methods to predetermine sample sizes, but our sample sizes Cell annotations
are similar to those reported in previous publications24,25,49. The SCTransform-based integration workflow of Seurat54 was used to
align data, using default settings. In brief, the integration workflow
Isolation of nuclei from frozen post-mortem choroid plexus searches for common gene modules (anchors) in cells with similar
Frozen choroid plexus tissue was extracted from the lateral ventricles transcriptomes. Individual samples after undergoing quality control
of post-mortem tissue obtained from the Stanford University Pathol- (described in ‘snRNA-seq quality control’) are integrated in a step-wise
ogy department and the Saarland University Hospital Institute for fashion, using cellular sequencing depth as a covariate to mitigate
Neuropathology, with approval from local ethics committees. Group technical artefacts. After combining the samples into a single data-
characteristics are presented in Supplementary Table 1. All procedures set or Seurat object, genes were projected into principal component
were carried out on ice or at 4 °C, and in a BSL2+ biosafety cabinet space using the principal component analysis (RunPCA). The first
while wearing PPE. Dounce homogenization or enzymatic dissocia- 80 (for global object), 30 (choroid plexus) or 25 (specific cell types)
tion resulted in loss of nuclei integrity and low nuclei complexity (<50 dimensions were used as inputs into the FindNeighbours, FindClus-
median genes per nuclei). We hypothesized that, similar to shaking ters (at 0.2 resolution) and RunUMAP functions of Seurat. In brief, a
an apple tree, gentle pipetting of choroid plexi tissue in lysis buffer shared-nearest-neighbour graph was constructed on the basis of the
could liberate nuclei without needing to physically disintegrate the Euclidean distance metric in principal component space, and cells were
fibrous choroid matrix—and thus avoid collateral physical damage to clustered using the Louvain method. RunUMAP functions with default
nuclei. Specifically, 40 mg of choroid plexus tissue was thawed in 250 μl settings was used to calculate 2D UMAP coordinates and search for dis-
of 1% BSA with 0.2 U μl−1 RNase inhibitor until the tissue settled. Five tinct cell populations. The positive differential expression of each clus-
ml of lysis buffer (10 mM Tris, 10 mM NaCl, 3 mM MgCl, 0.1% Nonidet ter against all other clusters (MAST) was used to identify marker genes
2
P40 substitute (Roche/Sigma, 11754599001), 0.2 U μl−1 RNase inhibi- for each cluster55. We annotated cell types using previously published
tor, and protease inhibitor) was added and tissue incubated on ice for marker genes5,8,24,46. To distinguish between confounding (perivascular)
10 min with gentle swirling every 2 min. Five ml of 1% BSA was added macrophages and T cells and pure microglia in the larger cortex immune
and the tissue triturated 10 times with a 5-ml serological pipette. After population, we subset the cluster and repeated the standard steps of
centrifugation (500g, 5 min), pelleted nuclei were resuspended in 1% Seurat for dimension reduction and unsupervised clustering. Then,
BSA with 0.2 U μl−1 RNase inhibitor, gently triturated 10 times with a to yield pure microglia by requiring the normalized expression of the
1-ml regular-bore pipette tip and filtered twice through a 70-μm and specific cell-type markers MRC1 and CD247 to be strictly less than 1.
then a 40-μm strainer (Flowmi). Debris was inspected on a brightfield As choosing a threshold involves a sensitivity–specificity trade-off, we
microscope and nuclei were counted on an TC20 automated cell coun- sought to set strict cut-offs as to yield pure microglia at a high speci-
ter (Bio-Rad) after the addition of Trypan blue. ficity. The MRC1+ cell population did not form separate clusters in an
unsupervised clustering of the larger immune population and was
Droplet-based snRNA-seq not associated with better or lower library quality scores, as assessed
For droplet-based snRNA-seq, libraries were prepared using the Chro- through the number of detected unique molecular identifiers, num-
mium Next GEM Single Cell 3ʹ v.3.1 according to the manufacturer’s ber of detected RNAs (genes) and percentage of mitochondrial reads.

(forward) and 5′-GCTGATGCACTGACCTGAAAA-3′ (reverse); NQO1:
Differential gene expression and subcluster analysis 5′-GAAGAGCACTGATCGTACTGGC-3′ (forward) and 5′-GGATACTGAA
Differential gene expression of genes comparing control individu- AGTTCGCAGGG-3′ (reverse); ZFP36: 5′-GACTGAGCTATGTCGGACCTT-3′
als and patients with COVID-19—or comparing cell-type subcluster (forward) and 5′-GAGTTC CGTCTTGTATTTGGGG-3′ (reverse);
markers—was done using the MAST55 algorithm (v.1.12.0), which imple- SDC4: 5′-GGACCTCCTAGAAGGCCGATA-3′ (forward) and 5′-AGGGC
ments a two-part hurdle model, and has demonstrated superior type-I CGATCATGGAGTCTT-3′ (reverse); ACTB: 5′-CACCATTGGCAA
error control without significantly sacrificing sensitivity56–59. First, TGAGCGGTTC-3′ (forward) and 5′-AGGTCTTTGCGGATGTCCACGT-3′
we ensured that our data did not exhibit signs of confounding effects (reverse); and (housekeeping performed in duplicate):
(Extended Data Fig. 2). For example, although sex imbalance of patient 5′-GGAGAAGAGCTACGAGCTGCCTGAC-3′ (forward) and
cohorts can influence some genes in single-cell analysis and is a general 5′-AAGGTAGTTTCGTGGATGCCACAGG-3′ (reverse)
issue in the field, we balanced genders by group, mitigating variance
due to sex (Extended Data Fig. 2a, Supplementary Tables 3, 5). Default Monocle trajectory analysis
Seurat thresholds of log-transformed fold change > 0.25 (absolute Monocle3 (v.0.2.1.) was used to generate the pseudotime trajectory
value), adjusted P value (Bonferroni correction) < 0.05 and expression in analysis in microglia77. Cells were reclustered as described in ‘Cell
greater than 10% of cells were required to consider a gene differentially annotations’ and used as input into Monocle to infer cluster and line-
expressed, as similarly done in previous studies of the brain5,8,25,26,46,60–63 age relationships within a given cell type. Specifically, UMAP embed-
and COVID-1964–70. Sex and batch were set as latent variables. Our sensi- dings and cell subclusters generated from Seurat were converted to a
tivity to detect DEGs for a given cell type was not driven by the number cell_data_set object using SeuratWrappers (v.0.2.0) and then used as
of nuclei isolated (Extended Data Fig. 4c). input to perform trajectory graph learning and pseudotime measure-
Cell-quality-associated markers were removed and biological path- ment through reversed graph embedding with Monocle.
way and gene ontology enrichment analysis were performed using
Enrichr71, Metascape72 or GeneTrail 373 with input species set to Homo Viral transcript analysis
sapiens and using standard parameters. Docking, processing and viral Four RNA-based approaches were applied to systematically probe for
defence genes relevant to SARS-CoV-2 were chosen on the basis of the presence of SARS-CoV-2 RNA in the brain: analysis by snRNA-seq,
a previous publication16. To identify microglia subcluster markers, bulk RNA-seq after viral isolation (QIAamp Viral RNA Mini Kit, Qia-
differential expression analysis of cells grouped in each subcluster gen, manufacturer’s instructions), bulk RNA-seq after whole tran-
was performed against the remaining cells within the given cell-type. scriptome isolation and RT–PCR using US Centers of Disease Control
Markers were defined based on the MAST algorithm using only posi- and Prevention (CDC) Emergency Use Authorization primers against
tive values with log-transformed fold change > 0.25 (absolute value) the SARS-CoV-2 N1 and N2 genes (IDT 10006770). Both bulk RNA-seq
and adjusted P value (Bonferroni correction) < 0.05. Enrichment or RNA underwent established cDNA and library generation: in brief,
over-representation of the overlap between markers defining the mRNA was transcribed into full-length cDNA by using the Smart-Seq
COVID-19 microglia 2 cluster and the Mathys5 Alzheimer’s disease v.4 Ultra-Low-Input RNA kit from Clontech according to the manu-
Mic1 cluster followed the hypergeometric probability, using the set facturer’s instructions. Samples were validated with an Agilent 2100
of 17,926 protein-coding genes as background. To assess alternative Bioanalyzer. Full-length cDNA was processed with the Nextera XT kit
differential expression approaches, raw gene counts were aggregated from Illumina for library preparation according to the manufacturer’s
for each sample and cell-type cluster separately. For the subsequent protocol. Library quality was verified with an Agilent 2100 Bioanalyzer.
pseudobulk analysis, we used the pbDS function of the muscat pack- Sequencing was carried out on a NovaSeq 6000 (150 cycles, Novogene).
age74 with limma-voom75 selected as differential state method, and the For RT–PCR analysis, bulk choroid whole transcriptome mRNA samples
parameters min_cells, and filter set to 20 and gene, respectively, where were diluted and mixed with SYBR green master mix before loading as
we configured sample sex and batch as latent variables in the design technical duplicates on a LightCycler 480 (Roche) for 40 cycles.
matrix. All other parameters were kept as default. To search for SARS-CoV-2 reads in either the snRNA-seq or bulk
RNA-seq datasets, raw .fastq files were subjected to read alignment
RT–qPCR validation of snRNA-seq differential gene expression via Viral-Track78, VIRTUS79 or centrifuge80 using the human (GRCh38)
For RT–qPCR validation of our snRNA-seq DEG analysis, we focused genome reference. For Viral-Track, both a collection of 12,163 consensus
on choroid plexus tissue because of its relative homogeneity com- virus sequences from Virusite81 (release 2020.3) and 17,133 curated
pared to cortex: epithelium and mesenchymal cells form over 90% of SARS-CoV-2 genomes from NCBI (downloaded on 29 September 2020)
all nuclei and, hence, DEGs in those cell types can be assessed even in were used. For centrifuge, a preprocessed virus index compiled by
bulk choroid plexus mRNA samples with only an approximately 10% genexa containing among other viruses 138 SARS-CoV-2 genomes
potential confound from other cell types. This is not the case with cortex was used. We also adopted a complementary approach82 focusing on
samples consisting of various cell types and subtypes (for example, SARS-CoV-2 reads, in which barcoded but unmapped BAM reads were
neuronal subtypes). In brief, choroid plexus nuclei were isolated as aligned using STAR to the SARS-CoV-2 reference genome, with a less
in ‘Isolation of nuclei from frozen post-mortem choroid plexus’, and stringent mapping parameter (outFilterMatchNmin 25-30) than the
bulk mRNA isolated using the RNeasy Micro Kit (Qiagen). cDNA was original Viral-Track pipeline.
generated using the qScript cDNA SuperMix (Quantabio) and then
mixed with SYBR green master mix before loading as technical dupli- Cell–cell communication
cates on a LightCycler 480 (Roche). ΔΔC values normalized to ACTB Cell–cell interactions based on the expression of known ligand–recep-
T
were used to assess relative gene expression between samples. The tor pairs in different cell types were inferred using CellChat32 (v.0.02).
following validated primer pairs were used (PrimerBank, human)76 to To identify potential cell–cell communication networks perturbed
assess major inflammatory genes predicted upregulated in COVID-19 as or induced in brains of patients with COVID-19, we followed the offi-
well as other genes predicted upregulated at a similar log-transformed cial workflow and loaded the normalized counts into CellChat and
fold change to confirm the validity of default snRNA-seq DEG MAST applied the preprocessing functions identifyOverExpressedGenes,
thresholds: IFITM3: 5′-CTGGGCTTC ATAGCATTCGCCT-3′ (forward) and identifyOverExpressedInteractions and projectData with standard
5′-AGATGTTCAGGCACTTGGCGGT-3′ (reverse); STAT3: 5′-CAGCA parameters set. As database, we selected the Secreted Signalling path-
GCTTGACACACGGTA-3′ (forward) and 5′-AAACACCAAAGTGG ways and used the precompiled human Protein–protein-Interactions as
CATGTGA-3′ (reverse); C7: 5′-AATGGCTGTACCAAGACTCAGA-3′ a priori network information. For the main analyses the core functions

Article
computeCommunProb, computeCommunProbPathway and aggre- at 51 for the age. We set the cut-off for the minimal variance out of the
gateNet were applied using standard parameters and fixed randomi- total variance being explained to be 95%. For each single annotation
zation seeds. Finally, to determine the senders and receivers in the variable, or first higher-order combinations of such, a cut-off of 0.005
network, the function netAnalysis_signallingRole was applied on the was applied to consider them explanatory. All variables (or combina-
netP data slot. tions of such) not passing the threshold were summarized as Other in
the analysis. The residual was then defined as the remaining propor-
Overlap with GWAS hits tion of variance not being associated with any of the variables that
From the GWAS catalogue43, we obtained GWAS risk genes for neuro- are explanatory nor informative to a minor proportion. To conduct
logical disorders (Alzheimer’s disease, amyotrophic lateral sclerosis, principal component analysis, we aggregated the log-normalized cell
brain ageing, multiple system atrophy, multiple sclerosis, Parkinson’s counts from Seurat for each gene and sample using the aggregateData
disease and narcolepsy), psychiatric disorders (attention deficit hyper- function from muscat and centred the gene expression vectors before
activity disorder, autism, bipolar disorder, depression, psychosis, computing eigenvectors.
post-traumatic stress disorder and schizophrenia) and neurobehaviour
traits (anxiety, suicidality, insomnia, neuroticism, risk behaviour, intel- Computational analysis, statistics and schematics
ligence and cognitive function). We removed gene duplicates and GWAS Analysis of the data was performed with the statistical programming
loci either not reported or in intergenic regions, and used a P < 9 × 10−6 language R (v.3.6.3) using the following general-purpose package for
to identify significant associations25. Then, as GWAS signals can point loading, saving and manipulating data, as well as generating plots,
to multiple candidate genes within the same locus, we focused on the and fitting statistical models: dplyr (v.1.0.0), ggplot2 (v.3.2.2.), patch-
‘Reported Gene(s)’ (genes reported as associated by the authors of work (v.1.0.1), openxlsx (v.4.1.5), bioconductor-scater (v.1.14.6)83,
each GWAS study). Disorders and traits exhibiting a significant number bioconductor-dropletutils (v1.6.1)84,85, bioconductor-complexheatmap
of genes that were also perturbed in patients with COVID-19 are high- (v.2.2.0)86, tidyverse (v.1.3.0)87 and lsa (v.0.73.2). All other tasks were
lighted. Following gene symbol extraction, we curated the gene set by performed on an x86_64-based Ubuntu (4.15.0-55-generic kernel)
(1) removing unknown or outdated gene names using the HGNChelper server cluster. We did not use statistical methods to predetermine
package (v.0.8.6), (2) converting remaining Ensembl gene identifiers to sample sizes, but they are similar to those reported in previous publica-
actual gene names using the packages ensembldb (v.2.10.0) and EnsDb. tions24,25,49. Data in graphs are always presented as mean ± s.e.m. Statisti-
Hsapiens.v86 (v.2.99.0) and (3) removing any remaining duplicates. cal tests used for group or cluster comparisons in bulk or single-nucleus
We then calculated the overlap between each set of GWAS genes with RNA-seq experiment analysis are specified in the respective sections
the cell-type-specific DEGs. Finally, a statistical enrichment of each in Methods. Schematic diagrams were created with BioRender.com.
overlap against background was calculated using a hypergeometric
test with the total background size set equal to the number of unique Immunohistochemistry
RNAs mapped in our dataset (29,431). Overlaps between GWAS DEGs Paraffin-embedded human brain tissue (medial frontal cortex, menin-
and disease GWAS genes expressed were calculated separately for ges and choroid plexus) adjacent to tissue processed for snRNA-seq
each cell type. was subjected to immunohistochemistry.
After deparaffinization and rehydration of 1–3-μm sections, per-
Comparison of DEGs in chronic CNS disease oxidases were blocked by incubation in 1% HO for 15 min at room
2 2
We compiled cell type-specific DEGs reported in published datasets for temperature. Heat antigen retrieval was performed by steaming at
Alzheimer’s disease5, autism spectrum disorder8, Huntington’s disease42 98 °C in target retrieval solution pH 6.1 (Dako, no. S1699) for 30 min.
and multiple sclerosis26. Lists of gene symbols were curated using the Sections were allowed to cool down at room temperature. Following
aforementioned approach. COVID-19 DEGs that overlap with those antigen retrieval, sections were incubated for 45 min at room tem-
found across the selected CNS diseases were called shared, whereas perature with the anti-SARS spike glycoprotein antibody 3A2 (rabbit,
those not previously reported were called unique to COVID-19. Statis- Abcam ab272420, 1:100), which has been used in previous publica-
tical significance calculations of over-representation in DEG overlaps tions17,18, anti-SARS-CoV-2 spike antibody (mouse, GeneTex GTX632604,
are based on cumulative hypergeometric P values analogous to the 1A9 clone, 1:100) used in a previous publication19, anti-SARS-CoV-2
procedures described in ‘Differential gene expression and sub-cluster spike antibody (rabbit, Sino Biological 40150-T62-CoV2, 1:100),
analysis’ and ‘Overlap with GWAS hits’, with the total background size anti-SARS-CoV-2 nucleoprotein antibody (rabbit, Sino Biological
set equal to the number of unique RNAs mapped in our dataset (29,431). 40143-T62, 1:100) used in a previous publication30, and anti-human
Using the smaller set of 17,926 protein-coding genes as background CD68 (mouse, Dako M0876, PG-M1 clone, 1:100) for determining micro-
does not change the qualitative statistical significance of the overlaps. glial reactivity. Both antibodies were diluted in Dako REAL antibody dil-
Similar to the analysis of GWAS hits, we determined the overlap and uent no. S2022. After three washes with wash buffer (Dako no. S3006),
tested its significance for each cell type separately. the Dako REAL EnVision HRP kit (no. K5007) or alkaline phosphatase/
RED kit (no. K500511) was used for the visualization of the antibody
Principal variance component and principal component reaction according to the manufacturer’s instructions. Sections were
analyses counterstained with Mayer’s haemalum (Sigma-Aldrich no. 1.09249).
In brief, to conduct the principal variance component analysis (PVCA), After dehydration, coverslips were mounted with Entellan (Merck no.
we aggregated the SoupX corrected raw counts for each gene and each 1.07961). Images were acquired with an Olympus BX 40 microscope,
biological sample using the aggregateData function of the muscat equipped with an Olympus SC30 digital microscope camera using
package (v.1.2.1)74. The resulting matrix was normalized by dividing the Olympus cellSens software. To assess disease-associated innate
each feature of a sample by the total counts from that sample, multi- immune activation in brains of individuals with COVID-19, slides were
plied by 100,000 and scaling the result using the function log(x + 1). screened at low magnification and areas with the most pronounced
As variables we considered the sample annotation fields ‘Sample-ID’, changes were used for quantification. Spatial context was used to deter-
‘Patient-ID’, ‘Sex’, ‘Brain-region’, ‘Disease’, ‘ageBin’, ‘nNucleiBin’ and mine the myeloid cell type—for example, the meninges are evident in
‘Batch’. As PVCA is designed to support factors, we assigned the values a brain slice, enabling confident identification of resident CD68+ cells
for numeric variables into ordered bins, more specifically, into six as meningeal, and likewise for the brain vasculature. A semiquantita-
half-open (left-closed) intervals of size 1,000 starting at 1,000 for the tive categorization for activation, as typical in pathology, was used:
number of nuclei and five similarly defined intervals of size 10 starting mild = detectable microgliosis, atypical for healthy tissue; moderate = a

pathological process typical of pathological changes; severe = a marked 68. Meckiff, B. J. et al. Imbalance of regulatory and cytotoxic SARS-CoV-2-reactive CD4+
pathological process. Several clusters of microglia or macrophages T cells in COVID-19. Cell 183, 1340–1353 (2020).
69. Lee, J. S. et al. Immunophenotyping of COVID-19 and influenza highlights the role of type
were characterized as excessive beyond the severe category.
I interferons in development of severe COVID-19. Sci. Immunol. 5, eabd1554 (2020).
70. Su, Y. et al. Multi-omics resolves a sharp disease-state shift between mild and moderate
Reporting summary COVID-19. Cell 183, 1479–1495 (2020).
71. Chen, E. Y. et al. Enrichr: interactive and collaborative HTML5 gene list enrichment
Further information on research design is available in the Nature
analysis tool. BMC Bioinformatics 14, 128 (2013).
Research Reporting Summary linked to this paper. 72. Zhou, Y. et al. Metascape provides a biologist-oriented resource for the analysis of
systems-level datasets. Nat. Commun. 10, 1523 (2019).
73. Gerstner, N. et al. GeneTrail 3: advanced high-throughput enrichment analysis. Nucleic
Acids Res. 48, W515–W520 (2020).
Data availability
74. Crowell, H. L. et al. muscat detects subpopulation-specific state transitions from
Raw sequencing data are deposited under NCBI Gene Expression Omni- multi-sample multi-condition single-cell transcriptomics data. Nat. Commun. 11, 6077
(2020).
bus (GEO) GSE159812. Normalized count data are also available for
75. Law, C. W., Chen, Y., Shi, W. & Smyth, G. K. voom: precision weights unlock linear model
download at https://twc-stanford.shinyapps.io/scRNA_Brain_COVID19. analysis tools for RNA-seq read counts. Genome Biol. 15, R29 (2014).
Any other relevant data are available from the corresponding authors 76. Spandidos, A., Wang, X., Wang, H. & Seed, B. PrimerBank: a resource of human and
mouse PCR primer pairs for gene expression detection and quantification. Nucleic Acids
upon reasonable request. Source data are provided with this paper.
Res. 38, D792–D799 (2010).
77. Trapnell, C. et al. The dynamics and regulators of cell fate decisions are revealed by
pseudotemporal ordering of single cells. Nat. Biotechnol. 32, 381–386 (2014).
Code availability 78. Bost, P. et al. Host-viral infection maps reveal signatures of severe COVID-19 patients. Cell
181, 1475–1488 (2020).
All analyses have been carried out using freely available software pack- 79. Yasumizu, Y., Hara, A., Sakaguchi, S. & Ohkura, N. VIRTUS: a pipeline for comprehensive
ages. Custom code used to analyse the RNA-seq data and datasets virus analysis from conventional RNA-seq data. Bioinformatics btaa859 (2020).
80. Kim, D., Song, L., Breitwieser, F. P. & Salzberg, S. L. Centrifuge: rapid and sensitive
generated and/or processed in the current study is available from the classification of metagenomic sequences. Genome Res. 26, 1721–1729 (2016).
corresponding authors upon request. 81. Stano, M., Beke, G. & Klucar, L. viruSITE-integrated database for viral genomics. Database
2016, baw162 (2016).
82. Wauters, E. et al. Discriminating mild from critical COVID-19 by innate and adaptive
47. Swiech, L. et al. In vivo interrogation of gene function in the mammalian brain using
immune single-cell profiling of bronchoalveolar lavages. Cell Res. 31, 272–290 (2021).
CRISPR-Cas9. Nat. Biotechnol. 33, 102–106 (2015).
83. McCarthy, D. J., Campbell, K. R., Lun, A. T. L. & Wills, Q. F. Scater: pre-processing, quality
48. Corces, M. R. et al. An improved ATAC-seq protocol reduces background and enables
control, normalization and visualization of single-cell RNA-seq data in R. Bioinformatics
interrogation of frozen tissues. Nat. Methods 14, 959–962 (2017).
33, 1179–1186 (2017).
49. Zhong, S. et al. A single-cell RNA-seq survey of the developmental landscape of the
84. Griffiths, J. A., Richard, A. C., Bach, K., Lun, A. T. L. & Marioni, J. C. Detection and removal
human prefrontal cortex. Nature 555, 524–528 (2018).
of barcode swapping in single-cell RNA-seq data. Nat. Commun. 9, 2667 (2018).
50. McInnes, L., Healy, J., Saul, N. & Großberger, L. UMAP: uniform manifold approximation
85. Lun, A. T. L. et al. EmptyDrops: distinguishing cells from empty droplets in droplet-based
and projection. J. Open Source Softw. 3, 861 (2018).
single-cell RNA sequencing data. Genome Biol. 20, 63 (2019).
51. Young, M. D. & Behjati, S. SoupX removes ambient RNA contamination from
86. Gu, Z., Eils, R. & Schlesner, M. Complex heatmaps reveal patterns and correlations in
droplet-based single-cell RNA sequencing data. Gigascience 9, giaa151 (2020).
multidimensional genomic data. Bioinformatics 32, 2847–2849 (2016).
52. Satija, R., Farrell, J. A., Gennert, D., Schier, A. F. & Regev, A. Spatial reconstruction of
87. Wickham, H. et al. Welcome to the Tidyverse. J. Open Source Softw. 4, 1686 (2019).
single-cell gene expression data. Nat. Biotechnol. 33, 495–502 (2015).
https://doi.org/10.21105/joss.01686.
53. McGinnis, C. S., Murrow, L. M. & Gartner, Z. J. DoubletFinder: doublet detection in single-cell
88. Lan, X., Han, X., Li, Q., Yang, Q. W. & Wang, J. Modulators of microglial activation and
RNA sequencing data using artificial nearest neighbors. Cell Syst. 8, 329–337 (2019).
polarization after intracerebral haemorrhage. Nat. Rev. Neurol. 13, 420–433 (2017).
54. Hafemeister, C. & Satija, R. Normalization and variance stabilization of single-cell RNA-seq
data using regularized negative binomial regression. Genome Biol. 20, 296 (2019).
55. Finak, G. et al. MAST: a flexible statistical framework for assessing transcriptional changes Acknowledgements We thank N. Khoury, T. Iram, E. Tapp and other members of the
and characterizing heterogeneity in single-cell RNA sequencing data. Genome Biol. 16, laboratories of T.W.-C. and A.K. for feedback and support, and H. Zhang and K. Dickey for
278 (2015). laboratory management. This work was funded by the NOMIS Foundation (T.W.-C.), the
56. Soneson, C. & Robinson, M. D. Bias, robustness and scalability in single-cell differential National Institute on Aging (T32-AG0047126 to A.C.Y. and 1RF1AG059694 to T.W.-C.), Nan
expression analysis. Nat. Methods 15, 255–261 (2018). Fung Life Sciences (T.W.-C.), the Bertarelli Brain Rejuvenation Sequencing Cluster (an
57. Wang, T., Li, B., Nelson, C. E. & Nabavi, S. Comparative analysis of differential gene initiative of the Stanford Wu Tsai Neurosciences Institute) and the Stanford Alzheimer’s
expression analysis tools for single-cell RNA sequencing data. BMC Bioinformatics 20, 40 Disease Research Center (P30 AG066515). A.C.Y. was supported by a Siebel Scholarship.
(2019). F.K., G.P.S., T.F., W.J.S.-S. and A.K. are a part of the CORSAAR study supported by the State of
58. Mou, T., Deng, W., Gu, F., Pawitan, Y. & Vu, T. N. Reproducibility of methods to detect Saarland, the Saarland University and the Rolf M. Schwiete Stiftung.
differentially expressed genes from single-cell RNA sequencing. Front. Genet. 10, 1331
(2020).
Author contributions A.C.Y., F.K., A.K. and T.W.-C. conceptualized the study. M.W.M., N. Ludwig,
59. Dal Molin, A., Baruzzo, G. & Di Camillo, B. Single-cell RNA-sequencing: assessment of
I.C., W.J.S.-S., N.S., D.C., D.B. and A.C.Y. provided and organized tissue samples. A.C.Y.
differential expression analysis methods. Front. Genet. 8, 62 (2017).
performed tissue dissociations. A.C.Y., N.S., D.P.L., R.T.V., D.G., N. Lu, O.H. and K.C. prepared
60. Ximerakis, M. et al. Single-cell transcriptomic profiling of the aging mouse brain. Nat.
libraries for sequencing. A.C.Y. and M.R.A. performed RT–PCR. F.K., G.P.S., T.F. and A.C.Y.
Neurosci. 22, 1696–1708 (2019).
performed computational analysis, with F.K. leading advanced analysis and data management.
61. The Tabula Muris Consortium. A single-cell transcriptomic atlas characterizes ageing
P.M.L. developed the searchable web interface (Shiny app). J.A.S. and W.J.S.-S. performed
tissues in the mouse. Nature 583, 590–595 (2020).
immunohistochemical stains and antibody tests. A.C.Y., F.K. and C.A.M. assembled figures.
62. Yang, A. C. et al. Physiological blood–brain transport is impaired with age by a shift in
A.C.Y. wrote the manuscript with input from all authors. F.K. and T.W.-C. edited the manuscript.
transcytosis. Nature 583, 425–430 (2020).
T.W.-C. and A.K. supervised the study.
63. Chen, M. B. et al. Brain endothelial cells are exquisite sensors of age-related circulatory
cues. Cell Rep. 30, 4418–4432 (2020).
64. Wilk, A. J. et al. A single-cell atlas of the peripheral immune response in patients with Competing interests T.W.-C. is a co-founder and scientific advisor of Alkahest Inc.
severe COVID-19. Nat. Med. 26, 1070–1076 (2020).
65. Xu, G. et al. The differential immune responses to COVID-19 in peripheral and lung Additional information
revealed by single-cell RNA sequencing. Cell Discov. 6, 73 (2020). Supplementary information The online version contains supplementary material available at
66. Schulte-Schrepping, J. et al. Severe COVID-19 is marked by a dysregulated myeloid cell https://doi.org/10.1038/s41586-021-03710-0.
compartment. Cell 182, 1419–1440 (2020). Correspondence and requests for materials should be addressed to A.K. or T.W.-C.
67. Guo, C. et al. Single-cell analysis of two severe COVID-19 patients reveals a Peer review information Nature thanks the anonymous reviewers for their contribution to the
monocyte-associated and tocilizumab-responding cytokine storm. Nat. Commun. 11, peer review of this work.
3924 (2020). Reprints and permissions information is available at http://www.nature.com/reprints.

Article
Extended Data Fig. 1 | Characterization of human cortical and choroid plexi medial frontal cortex (n = 8 control; n = 8 COVID-19, two-sided Mann-Whitey
nuclei sequenced. a, Total number of nuclei and median number of genes of t-test; mean ± s.e.m.) and choroid plexus (n = 7 control; n = 7 COVID-19,
each human sample sequenced in medial frontal cortex and choroid plexus. two-sided Mann-Whitey t-test; mean ± s.e.m.). d, e, Bar graph presenting
b, c, Quantification of the median number of genes detected per nuclei (b) and frequency of nuclei for control and COVID-19 medial frontal cortex (d) and
patient ages (c) in control (non-viral and influenza) and COVID-19 samples in choroid plexus (e) sample groups.

Extended Data Fig. 2 | Gene expression variance analysis. a, PVCA, visualization of all samples, based on unscaled counts. c, UMAP projections of
displaying the gene expression variance explained by residuals (biological and nuclei isolated from the medial frontal cortex (top) or choroid plexus (bottom),
technical noise) or experimental factors such as brain region, age, sex and and split by disease group, showing no systematic batch effects.
respective combinations. n = 30 samples. b, Principal component (PC) analysis

Article
Extended Data Fig. 3 | Human brain cell-type markers. a, Top cell-type- b, Example of top cell-type-specific genes across the types of cells captured in
specific genes across the types of cells captured in the human cortex. The the human choroid plexus. Violin plots are centred around the median, with
colour bar indicates gene expression from low (blue) to high (yellow). their shape representing cell distribution.

Extended Data Fig. 4 | Cell-type-specific changes in gene expression and black (low) to yellow (high). b, Example upregulation of inflammatory and
intercellular signalling in the brain of individuals with COVID-19. a, Heat dysregulation of homeostatic genes in COVID-19 astrocytes. c, Comparison of
map displaying the number of significant biological pathways among the set of the number of nuclei isolated per cell type and the number of predicted DEGs.
DEGs in each cell type (FDR < 0.05, Benjamini–Hochberg adjustment, Two-sided P-value indicates the significance of the correlation (Pearson, not
hypergeometric test). Number of significant pathways is indicated in graded significant).

Article
Extended Data Fig. 5 | Overlap between alternative snRNA-seq differential cell types in the human medial frontal cortex (a) and choroid plexus (b). Orange
expression analysis methods. a, b, Scatter plots demonstrating the strong line denotes the trend line fitted with a generalized linear model, surrounded
correlation between the calculated effect sizes of two differential gene by a 95% confidence interval in purple. Spearman correlation is shown along
expression analysis methods (MAST55 (used here) and pseudobulk74,75) across with the significance by two-sided P-values.

Extended Data Fig. 6 | DEGs in the brains of individuals with COVID-19 show neural genes downregulated. Minimal overlap is seen with COVID-19 changes of
no significant overlap with brain PMI-sensitive genes. a, Comparison of the same category (for example, glial genes upregulated in COVID-19 versus
post-mortem interval (PMI)-sensitive genes (left column, from a previous glial genes upregulated with extended PMI). c, Heat map showing that
publication27) and COVID-19 DEGs (all other columns). No statistically PMI-sensitive genes are not the DEGs in COVID-19 and thus not driving
significant overlap is observed (Fisher’s exact test). b, The previous study27 the DEG-based findings of our study.
categorized PMI-sensitive genes in two categories: glial genes upregulated and

Article
Extended Data Fig. 7 | Expression of SARS-CoV-2 virus entry genes across plexus (b). Violin plots are centred around the median, with their shape
cell types. a, b, Expression of SARS-CoV-2 entry receptors, established and representing cell distribution.
putative, across cell types in the human medial frontal cortex (a) and choroid

Extended Data Fig. 8 | Choroid plexus inflammation in COVID-19. Immunohistochemical staining for the macrophage activation marker CD68 (brown) in the
choroid plexus of patients with COVID-19 and control individuals. Haematoxylin counterstain (blue). Scale bars, 20 μm.

Article
Extended Data Fig. 9 | No conclusive detection of SARS-CoV-2 the frontal medial cortex of two patients with COVID-19 in tissue immediately
neuroinvasion. a, Summary of RNA-based assays to detect SARS-CoV-2 in the adjacent to that used for snRNA-seq. Haematoxylin counterstain (purple).
human cortex and choroid plexus. Aside from the 3A2 antibody, no other Scale bar, 20 μm. d, As in c, but for the choroid plexus and meninges in two
anti-SARS-CoV-2 antibody detected viral protein antigen in the brain or choroid patients with COVID-19. Scale bar, 20 μm. e, As in c, but using a different
plexus. b, qPCR detection of the SARS-CoV-2 genes N1 and N2 via CDC secondary antibody detection method (biotin–alkaline phosphatase (red)),
Emergency Use Authorization primers on choroid plexus samples (n = 6 recapitulating the specific vascular-localized signal. Scale bar, 20 μm.
non-viral control, n = 7 COVID-19; two-sided Mann–Whitney t-test; mean ± Immunohistochemical stains are representative of at least two independent
s.e.m.). c, Aberrant anti-SARS-CoV-2 spike (3A2) antibody reactivity (brown) in experiments.

Extended Data Fig. 10 | Cell communication analysis results for integrated COVID-19 for choroid plexus). Each circle (colour) represents one cell type, and
choroid plexus and brain parenchyma cell types. Circle plot showing the edges connecting circles represent significant intercellular signalling inferred
number of statistically significant intercellular signalling interactions for total between those cell types. Circles and edges were normalized and scaled to
signalling (over 30 ligand–receptor pathways) and the complement family of display relative sizes, with the former proportional to the number of cells from
molecules in control individuals (non-viral and influenza) compared to a given cell type and the latter according to the inferred strength of signalling.
patients with COVID-19 (permutation test, CellChat34; n = 8 control, including Cell type labels correspond to signalling pathway increased in COVID-19.
influenza; n = 8 COVID-19 for cortex; and n = 7 control, including influenza; n = 7

Article
Extended Data Fig. 11 | Activation of parenchymal microglia and infiltration by brown stained macrophages into the leptomeninges is visible.
perivascular macrophages in COVID-19. Immunohistochemical staining of Scale bar, 20 μm. d, Summary of innate immune reactivity across eight patients
microglia and macrophages by an antibody against the pro-inflammatory with COVID-19, typically not observed in healthy brains at these levels,
marker CD6888 (immunoreaction in brown). Counterstained with colour-coded and labelled by severity. A semiquantitative categorization for
haematoxylin for cell nuclei in blue. a, The frontal medial gyrus of patients with changes, as usual in the field of pathology, is used: mild = detectable
COVID-19 immediately adjacent to that used for snRNA-seq. A cluster of microgliosis, atypical for healthy tissue; moderate = a pathological process
activated microglia up to single macrophages is immunostained in the typical of pathological changes; severe = a marked pathological process.
parenchyma of the gyrus (subcortical white matter). Scale bar, 20 μm. Several clusters of microglia or macrophages were characterized as excessive
b, A vessel of the medial frontal gyrus is surrounded by activated perivascular beyond the severe category. Immunohistochemical stains are representative
macrophages. Scale bar, 20 μm. c, The cortical surface is shown. The upper of at least two independent experiments.
third of the figure contains the leptomeninges that cover the cortex. A dense

Extended Data Fig. 12 | See next page for caption.

Article
Extended Data Fig. 12 | Evaluation of COVID-19-enriched subpopulations in (Metascape54) amongst upregulated gene markers of COVID-19 astrocytes.
other parenchymal glia. a, UMAP of astrocytes captured in the human frontal Enrichment is based on FDR-corrected cumulative hypergeometric P values
cortex, split by control individuals (including influenza, n = 8) and patients (Bonferroni correction FDR < 0.05; MAST with default thresholds). d, UMAP
with COVID-19 (n = 8). Cells are coloured by cell-type subcluster. Genes projection of OPCs and trending but not significant emergence of a COVID-19-
upregulated in the COVID-19-enriched astrocyte cluster are labelled in green. enriched subcluster. e, Quantification of the frequency of the COVID-19-
b, Quantification of astrocyte cluster 1 as a proportion of total astrocytes (n = 8 enriched OPC subcluster as a proportion of all OPCs (n = 8 control, including 1
control, including influenza; n = 8 COVID-19, two-sided Mann–Whitney t-test influenza and n = 8 COVID-19, two-sided Mann–Whitney t-test, P = 0.083; mean
P = 0.0041; mean ± s.e.m.). Example genes upregulated in the COVID-19- ± s.e.m., not significant). f, g, As in d, e, respectively, but for mature
associated astrocyte cluster are shown. c, Enriched biological pathways oligodendrocytes with P = 0.9591.