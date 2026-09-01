Europe PMC Funders Group
Author Manuscript
Science. Author manuscript; available in PMC 2020 July 08.

Published in final edited form as:

Science. 2019 September 27; 365(6460): 1461–1466. doi:10.1126/science.aat5031.

E
u
r
o
p
e
P
M
C
F
u
n
d
e
r
s
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
s

E
u
r
o
p
e
P
M
C
F
u
n
d
e
r
s
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
s

Spatio-temporal immune zonation of the human kidney

Benjamin J Stewart#1,2,3, John R Ferdinand#1, Matthew D Young3, Thomas J Mitchell2,3,4,
Kevin W Loudon1,2, Alexandra M Riding1,2, Nathan Richoz1, Gordon L Frazer1, Joy UL
Staniforth1, Felipe A Vieira Braga3, Rachel A Botting5, Dorin-Mirel Popescu5, Roser Vento-
Tormo3, Emily Stephenson5, Alex Cagan3, Sarah J Farndon3,6,7, Krzysztof Polanski3,
Mirjana Efremova3, Kile Green5, Martin Del Castillo Velasco-Herrera3, Charlotte Guzzo3,
Grace Collord2,3,8, Lira Mamanova3, Tevita Aho2, James N Armitage2, Antony CP Riddick2,
Imran Mushtaq6, Stephen Farrell2, Dyanne Rampling6, James Nicholson2,8, Andrew Filby5,
Johanna Burge2, Steven Lisgo9, Susan Lindsay9, Marc Bajenoff10, Anne Y Warren2, Grant
D Stewart2,4, Neil Sebire6,7, Nicholas Coleman2,11, Muzlifah Haniffa3,5,12,*, Sarah A
Teichmann3,13,*, Sam Behjati2,3,8,*, Menna R Clatworthy1,2,3,*
1Molecular Immunity Unit, University of Cambridge Department of Medicine, Cambridge, CB2
0QQ, UK

2Cambridge University Hospitals NHS Foundation Trust, and NIHR Cambridge Biomedical
Research Centre, Cambridge, CB2 0QQ, UK

3Wellcome Sanger Institute, Wellcome Genome Campus, Hinxton, CB10 1SA, UK

4Department of Surgery, University of Cambridge, CB2 0QQ, UK

5Institute of Cellular Medicine, Newcastle University, Newcastle upon Tyne, NE2 4HH, UK

6Great Ormond Street Hospital for Children NHS Foundation Trust, London, WC1N 3JH, UK

7UCL Great Ormond Street Hospital Institute of Child Health, London WC1N 1E, UK

8Department of Paediatrics, University of Cambridge, Cambridge, CB2 0QQ, UK

9Human Developmental Biology Resource, Institute of Genetic Medicine, Newcastle University,
Newcastle upon Tyne, NE1 3BZ, UK

10Centre d’Immunologie de Marseille-Luminy, Marseille, France

11Department of Pathology, University of Cambridge, Cambridge, CB2 1QP, UK

*Corresponding authors. Correspondence to: mrc38@cam.ac.uk, sb31@sanger.ac.uk, st9@sanger.ac.uk, m.a.haniffa@newcastle.ac.uk.
Author contributions:
B.J.S. and J.R.F. analyzed the data, with contributions from M.D.Y., S.B., T.J.M. F.V.B., M.D.C.V.H., and M.R.C. Samples were
curated and/or experiments performed by: F.V.B., J.R.F., B.J.S., R.A.B., D.M.O., R.V-T., E.S., K.W.L., A.M.R., J.L.F., J.U.L.S., S.J.F.,
C.G., N.R., L.M., T.A., J.N.A., A.C.P.R., I.M., S.F., C.J., D.R., J.N., A.F., J.B., S.Lis., S.Lin. and G.D.S. Pathological expertise was
provided by A.Y.W., N.S.. B.J.S., J.R.F and M.R.C. wrote the manuscript. M.H., S.T., M.R.C. and S.B. co-directed the study.

Competing interests: Authors declare no competing interests.

Data and materials availability: Sequencing data and metadata is available via the Human Cell Atlas Data Portal (https://
data.humancellatlas.org/explore/projects/abe1a013-af7a-45ed-8c26-f3793c24a1f4).
Data is available to download and in an interactive browser format at www.kidneycellatlas.org
Code is uploaded to https://github.com/bjstewart1/kidney_sc_immune and archived at zenodo (DOI:10.5281/zenodo.3245841).

E
u
r
o
p
e
P
M
C
F
u
n
d
e
r
s
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
s

E
u
r
o
p
e
P
M
C
F
u
n
d
e
r
s
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
s

Stewart et al.

Page 2

12Department of Dermatology and NIHR Newcastle Biomedical research Centre, Newcastle
Hospitals NHS Foundation Trust, Newcastle upon Tyne NE2 4LP, UK

13Theory of Condensed Matter Group, Cavendish Laboratory/Department of Physics, University
of Cambridge, Cambridge CB3 0HE, UK

# These authors contributed equally to this work.

Abstract

Tissue-resident immune cells are important for organ homeostasis and defense. The epithelium
may contribute to these functions directly, or via crosstalk with immune cells. We used single cell
RNA sequencing to resolve the spatio-temporal immune topology of the human kidney. We reveal
anatomically-defined expression patterns of immune genes within the epithelial compartment, with
anti-microbial peptide transcripts evident in pelvic epithelium in the mature, but not fetal kidney.
A network of tissue-resident myeloid and lymphoid immune cells was evident in both fetal and
mature kidney, with post-natal acquisition of transcriptional programs that promote infection-
defense capabilities. Epithelial-immune crosstalk orchestrated localization of anti-bacterial
macrophages and neutrophils to the regions of the kidney most susceptible to infection. Overall,
our study provides a global overview of how the immune landscape of the human kidney is
zonated to counter the dominant immunological challenge.

The kidneys play a vital role in organism homeostasis but can be affected by a number of
prevalent and life-limiting conditions where recognition and response to pathogen and
danger signals is critical (1). These responses are mediated by a network of immune cells (1)
but our understanding of human kidney-resident immune cells and their cell signaling
circuitry is limited. Anatomically, each kidney is comprised of the cortex containing
glomeruli (where filtrate is generated), and medulla where urine is concentrated (Fig. 1A).
The functional subunit of the kidney is the nephron, made up of a glomerulus, proximal
tubule (PT) (where filtered electrolytes are reabsorbed), loop of Henle (LOH) (that generates
the intrarenal sodium gradient required for urine concentration) and collecting ducts (CD)
that coalesce in the kidney pelvis. Urine subsequently flows into the ureter and on to the
bladder (2) (Fig. 1A). The principal infectious challenge arises from bacteria ascending the
ureter into the kidney pelvis, and we have previously shown that the hypersaline
environment within the medulla may promote anti-microbial responses (3).

Here, we used droplet encapsulation high throughput single cell RNA sequencing
(scRNAseq) (10x Genomics platform) and flow and mass cytometry to define the global
immune landscape of the human kidney. We studied single cell suspensions from 14 mature
human kidneys and 6 fetal kidneys (Table S1, S2, and Fig. S1). We captured 114,113
droplets from mature kidneys, yielding 40,268 cells following rigorous quality control, as
described previously (4, 5) (Fig. S2A). We loaded 739 highly variable genes into a principal
component analysis and identified clusters that were manually curated into four major
cellular compartments based on canonical marker expression; endothelial, immune,
fibroblast/myofibroblast, and epithelium (Figs. 1B, S3A-F).

Science. Author manuscript; available in PMC 2020 July 08.

E
u
r
o
p
e
P
M
C
F
u
n
d
e
r
s
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
s

E
u
r
o
p
e
P
M
C
F
u
n
d
e
r
s
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
s

Stewart et al.

Page 3

Within the endothelial cell clusters, glomerular endothelial cells (GE), vasa recta (VR), and
peritubular capillaries (PCap) were identified (Figs. 1B, S3E-F). Nephron epithelial cells
were evident, including podocytes (Podo), PT, LOH, connecting nephron tubule (CNT),
intercalated cells (IC) and principal cells (PC) of the collecting duct, as well as pelvic
epithelium (PE) (Fig. 1B). Immune cell populations included mononuclear phagocytes
(MNPs), B cells, T cells and NK cells (Fig. 1B), and their presence confirmed by mass
cytometry in n=3 additional adult kidney samples (Fig. S4) that were flushed to minimise
intravascular contamination.

To explore the spatial distribution of these cells across the kidney, we sought to assign a
depth-estimate of the sample from which the cells originated, termed ‘Pseudodepth’ (Fig.
S5, Table S3, Supp. methods). We observed enrichment of GE, Podo and PT cells in samples
predicted to be cortical/cortico-medullary in pseudodepth, whilst PE and transitional
epithelium were limited to medulla/pelvic pseudodepth (Fig. 1C), as predicted by their
known arrangement. This analysis revealed an asymmetrical distribution of immune cells,
with B cells almost exclusively located in cortical samples, whilst MNPs were enriched in
deeper samples (Figs. 1C-D, S4G, S5D).

We next analysed single cell transcriptomes from fetal kidneys obtained at 7-16 post-
conception weeks (PCW). Based on the analyses of 33,865 droplets, yielding 27,203
annotated cells after rigorous quality control (Fig. S1A and S2B), we identified immune,
endothelial, developing nephron epithelium and stromal cell clusters based on canonical
marker expression and informed by previous transcriptional analyses of fetal kidney (6, 7)
(Figs. 1E, S6, S7, Table S10). Cells from various developmental stages of nephrogenesis (8)
(Fig. 1F) were evident in our single cell data (Fig. 1E, G-H), with cap mesenchyme (CM)
dominating at 7-8 PCW (Fig. 1G-H). From 9 PCW, podocytes were more evident, and by 12
weeks, cells from across nephrogenesis were present, including PT, LOH, CD and PE (Fig.
1E, G-H).

Much of the knowledge about the developing immune system in the human fetus is inferred
from murine studies. Fetal kidneys at the gestational age captured in our study (7-16 PCW),
would be expected to contain macrophages with potentially three developmental origins;
yolk sac progenitors, aorta-gonad-mesonephros (AGM) hematopoetic stem cells (HSCs) and
fetal liver HSCs (9, 10). The extent to which other myeloid and lymphoid cells populate the
human fetal kidney is unclear. In our fetal kidney dataset (representing 7-16 PCW), several
immune cell clusters were evident (Fig. 1E). Macrophages and some dendritic cells (DCs)
were present at the earliest developmental stage (Fig. 1H). Monocytes, T cells and NK cells
appeared from 9 PCW, whilst B cells were present at later developmental stages from 12
PCW (Fig. 1H). These data demonstrate that immune cell subsets exhibit different temporal
patterns of localization to the human fetal kidney.

Terminally differentiated fetal nephron epithelial cells (Fig. S7) showed transcriptional
similarity to their mature counterparts (Figs. S8-9), particularly in proximal nephron
components, whilst CNT and PE showed less similarity (Fig. 2A). Immune gene ontology
(GO) terms were enriched across the mature nephron, particularly in the pelvic epithelium,
including ‘innate immune’ and ‘anti-microbial response’ genes (Figs. 2B, S10B). We

Science. Author manuscript; available in PMC 2020 July 08.

E
u
r
o
p
e
P
M
C
F
u
n
d
e
r
s
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
s

E
u
r
o
p
e
P
M
C
F
u
n
d
e
r
s
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
s

Stewart et al.

Page 4

verified this pattern of gene expression in bulk transcriptomic data, which similarly
demonstrated highest expression of immune genes in the pelvis (Fig. S10C). In contrast,
there was little or no expression of immune genes in fetal kidney epithelium (Fig. 2B).

We hypothesized that these spatially distinct immune gene expression patterns may be
related to the dominant infection threat in the post-natal renal tract, which occurs via
bacteria ascending the ureter from the bladder, most commonly uropathogenic Escherichia
coli (UPEC). UPEC-associated molecules such as flagellin are sensed by extracellular toll-
like receptors (TLRs) (11). In mature kidneys, we observed higher expression of the flagellin
receptor TLR5, and its down-stream signalling molecule MyD88, in the PE compared with
the proximal nephron epithelium (Fig. S10D). Epithelial cells may directly contribute to
organ defense by secreting antimicrobial peptides (AMPs). AMP expression was highest in
the mature pelvic epithelium (Fig. 2B), including serum amyloid A1 (SAA1), which inhibits
biofilm formation in UPEC (12), and Lipocalin 2 (LCN2), an iron chelator with
bacteriostatic effects (13), the deficiency of which results in susceptibility to recurrent
urinary tract infections (UTI) (14).

To validate the differential expression and functional significance of these AMPs in kidney
epithelium, we measured transcripts in bulk human kidney samples ex vivo, and
demonstrated high expression of LCN2 and SAA1 in medulla/pelvis samples that increased
following the addition of UPEC (Fig. 2C). Similarly, in vivo in a murine model of
pyelonephritis (3), Lcn2 and Saa1 were more highly expressed in the medulla/pelvis
compared with cortex, and expression upregulated 24 hours following urethral challenge
with UPEC (Fig. 2C). Thus, the distinct expression patterns of AMPs in human kidney
likely facilitate protective epithelial responses in the region most vulnerable to ascending
bacterial infection. This zonated epithelial innate immune capability is acquired post-natally
and was not evident in fetal kidney.

Analysis of the immune compartment in mature kidney identified, and delineated the
defining markers of, resident MNP, neutrophil, mast, pDC, B, CD4 T, CD8 T, NK and NKT
cell clusters (Figs. 3A, S11, Supp data 7, 8). Lymphocyte subsets expressed molecules
associated with tissue-residency (15) (Fig. S12A) and a recently defined Hobit/Blimp1-
containing murine resident-lymphocyte signature (16) (Fig. S12B), consistent with the
conclusion that the mature human kidney houses bona-fide tissue-resident lymphocytes. The
B cell cluster included IgM, IgG and IgA-expressing cells (Fig. S12C). Cytokine and
transcription factor expression did not indicate any specific polarization of CD4 T cells (Fig.
S12D). Within the NK cluster were cells with dual expression of γ and δ TCR, and markers
typically associated with mucosal-associated invariant T cell (MAIT) (Fig. S12D).

Within the myeloid compartment, we identified 4 distinct clusters of MNPs (Fig. 3B and
S13A-D). MNPs comprise monocytes, macrophages and DCs with several subsets described
based on surface markers, function and ontogeny (17); expression of CD11c, major
histocompatibility complex (MHC) class II molecules and CD14 identifies monocyte-
derived macrophages with an avid phagocytic capacity, whilst CD11c+/MHCII+/CD14- are
classical myeloid DC (cDC) with the ability to migrate and present or cross-present antigen
to T cells (17, 18). cDC can be further subdivided into cDC1 that are CD141(THBD) + and

Science. Author manuscript; available in PMC 2020 July 08.

E
u
r
o
p
e
P
M
C
F
u
n
d
e
r
s
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
s

E
u
r
o
p
e
P
M
C
F
u
n
d
e
r
s
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
s

Stewart et al.

Page 5

XCR1+, and cDC2 that express CD1c. CD11c+/MHCII+/CD14+ macrophages, cDC1 and
cDC2 have previously been described in the human kidney (3). In our scRNAseq dataset, all
four MNP clusters expressed ITGAX (CD11c) and HLA-DRA (an MHCII gene), with the
highest expression of MHCII in MNPc (Fig. 3C). Some cells in this cluster expressed
CD1C, XCR1, CLEC9A and CD141 (THBD) (Fig. 3C) indicating that it included cDC1 and
cDC2 cells (Fig. S13E-F). MNPa and MNPd contained cells expressing CD14, whilst MNPb
expressed CD16 (FCGR3A) (Fig. 3C). MNPa was transcriptionally similar to ‘classical’
monocytes, and MNPb to ‘non-classical’ monocytes (Fig. S13C-D), and both showed
transcriptional overlap with intestinal macrophages (Fig. S13G), which are predominantly
monocyte-derived (19). MNPd showed little transcriptional similarity to circulating
monocytes or monocyte-derived macrophages in intestine or skin (Fig. S13C-D, G)
suggesting that these cells may have a different origin or that their transcriptome is re-
programmed by the tissue environment. Of note, RUNX1, a TF used to fate-map yolk sac-
derived cells (20), was differentially expressed in MNPd (Fig. S13H), raising the possibility
that they may populate the kidney pre-natally.

Macrophages and cDCs are functionally distinguished by their capacity to phagocytose and
destroy ingested material or to process and present antigen to CD4 T cells respectively. In
mature kidneys, ‘Antigen processing and presentation’ and ‘T cell co-stimulation’ were the
top GO terms associated with MNPc (Fig. S13I), consistent with their identity as cDC.
‘Defense response to bacterium’ and ‘Neutrophil degranulation’ genes were expressed by
monocyte-derived MNP subsets, MNPa and MNPb (Fig. S13I), including anti-microbial
genes such as S100A8 and S100A9, IL1B and lysozyme (LYZ) (Fig. S13J).

CD11c+MHCII+CD14+ MNPs in mature human kidney are enriched in inner regions of the
kidney and specialized for defense against UPEC (3). However, in the current scRNAseq
experiment two subsets of MNP were found to express CD14, MNPa and MNPd (Fig. 3C),
with the single cell transcriptomes indicating functional diversity, with MNPa alone
specialized in anti-bacterial activities (Fig. S13I). Using marker genes identified by our
scRNAseq dataset (Table S6), we confirmed the presence of MNPa-d in adult kidney by
flow cytometry (Fig. S14A-B) and compared the phagocytic capacity of MNPa and MNPd
(Fig. S14B). MNPa demonstrated avid uptake of fluorescently labeled UPEC, in contrast to
MNPd (Fig. 3D), in keeping with the GO term analysis.

In the fetal kidney, the lymphoid compartment contained CD4 T cells, with few CD8 T cells
detectable (in contrast to the mature kidney), as well as B, NK, and innate lymphoid cells
(Fig. 3E). There were several subsets of myeloid cells, including monocytes, two subsets of
macrophages (MPhage1 and MPhage2), cDC1 and cDC2, pDCs and mast cells (Fig. 3E).
We also observed proliferating counterparts of MPhage1, cDC2, monocytes, B cells and NK
cells (Figs. 3E, S15). The MPhage 1 population showed transcriptional similarity to murine
kidney F4/80high yolk sac-derived macrophages (21) (Fig. S16A). The MPhage 2 subset had
transcriptional overlap with MPhage 1 but also expressed pro-inflammatory genes (Figs. 3C,
E, S16B). MPhage 1, dominated the resident-immune cell population in fetal kidneys at 7-10
PCW (Fig. 3F) but at later stages, MPhage 2 increased in number along with other immune
cells (Fig. 3F). The emergence of MPhage 2 at later time-points may reflect a different
origin, or increasing exposure of the same precursor cell to a pro-inflammatory stimulus.

Science. Author manuscript; available in PMC 2020 July 08.

E
u
r
o
p
e
P
M
C
F
u
n
d
e
r
s
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
s

E
u
r
o
p
e
P
M
C
F
u
n
d
e
r
s
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
s

Stewart et al.

Page 6

Fetal kidney DCs were predominantly cDC2 with few cDC1 (Fig. 3F), as observed in
mature kidneys (Figs. 3B, S13E-F). The emergence of kidney CD4, CD8 T cells and B cells
at >10 PCW mirrors the development of fetal thymus and spleen.

To investigate the relationship between immune cell subsets in fetal and mature human
kidney, we quantified their transcriptional similarity (Figs. S16C, S17A). MNPd was the
only mature kidney MNP cluster with similarity to fetal kidney Mphage1 (S16C), and both
clusters expressed MRC1, C1QC, CD163, and MAF (Figs. 3C, S16D). Trajectory analysis
demonstrated a temporal progression of the MPhage1 transcriptome towards that of MNPd
(Fig. S16F). Mature kidney MNPa and MNPb were highly transcriptionally similar to fetal
kidney monocytes (Fig. 3C, S16C).

We next asked how the transcriptome of kidney immune cells changed over developmental
time. Previous studies indicate that fetal monocytes may be less ‘pro-inflammatory’ (22) and
fetal DCs less effective at stimulating CD4 T cells than their mature counterparts (23). We
found that fetal kidney monocytes were less enriched for ‘pro-inflammatory’ M1 gene
expression than mature kidney MNPa and MNPb (Fig. 3G). Both fetal macrophage subsets,
as well as MNPd in the mature kidney, were skewed towards an anti-inflammatory M2
transcriptome (Fig. 3G). Monocyte-derived macrophages in the mature kidney showed
increased expression of ‘Phagocytosis’ and ‘Defense response to bacterium’ genes compared
with fetal monocytes (Fig. S16G). Similarly, ‘antigen processing and presentation’ genes
and HLA-DRA were more highly expressed in mature kidney DCs compared with those in
the fetus (Figs. 3C, S16G, F). In the lymphoid compartment, fetal kidney B cells showed no
evidence of class switching (in contrast to their mature counterparts) (Fig. S17B), whilst
fetal CD8 T cells expressed little GZMH, a cytotoxic effector molecule (Fig. S17B).
Functionally, fetal kidney CD8 T cells and NK cells showed reduced enrichment for ‘T cell
receptor signalling’ and ‘NK cell mediated immunity’ relative to mature kidney CD8 and
NK cells respectively (Fig. S17C).

Epithelial and endothelial cells can communicate with immune cells via chemokines that
orchestrate immune cell position, and cytokines that promote immune cell function. To
investigate epithelial-immune cross-talk in the kidney, we assessed chemokine ligand-
receptor interactions (Figs. 4A and Fig S18A) (24). CX3CL1 was expressed in CNT and PE,
and its receptor CX3CR1 on monocyte-derived macrophages (MNPa-b) and DCs. Analysis
of bulk RNA sequencing data demonstrated two peaks of CX3CL1 expression across kidney
pseudodepth, in keeping with the single cell analysis (Fig. 4A, S18B). Using a CX3CL1
reporter mouse, we confirmed high expression of CX3CL1 protein in the kidney pelvis, with
the potential to position CX3CR1-expressing MNPs (Fig. S18C). Analysis of CX3CR1
expression across kidney pseudodepth similarly showed some transcripts in the cortex, but
greatest expression in the deeper regions of the kidney (Fig. S18B). Given the marked
bacterial phagocytic capacity of MNPa (Fig. 3D), this pattern of chemokine expression
would place them in a pelvic position to combat ascending UPEC. Notably, MNPd showed
little expression of CX3CR1, and in human kidney sections there were few CD206/163
positive cells in the medulla and pelvis compared to the cortex (Fig. S18D).

Science. Author manuscript; available in PMC 2020 July 08.

E
u
r
o
p
e
P
M
C
F
u
n
d
e
r
s
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
s

E
u
r
o
p
e
P
M
C
F
u
n
d
e
r
s
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
s

Stewart et al.

Page 7

The ligand-receptor analysis also highlighted interactions between PE and neutrophils via
expression of CXCL1-3, CXCL5-6 and CXCL8 and their receptors on neutrophils (Fig. 4A).
We validated this, demonstrating that CK17 (KRT17)+ cells (a marker of PE) in human
kidney pelvis express CXCL8 and LCN2 (Fig. 4B, S19A). This finding is clinically
important since genetic variants of CXCL8 and CXCR1 are associated with susceptibility to
pyelonephritis in humans (25). To determine if this epithelial-immune cross-talk may
promote neutrophil recruitment to the pelvis during UTI, samples of human kidney were
incubated with UPEC. At baseline, CXCL8 levels were significantly higher in the medulla/
pelvis samples compared with the cortex (Fig. 4C), with a marked increase observed
following UPEC challenge (Fig. 4C). Similarly, in vivo, in a mouse model of pyelonephritis,
Cxcl1 and Cxcl2 (murine orthologues of human CXCL8) were higher in the medulla/pelvis
samples and in PE at baseline and further increased during infection (Fig. 4C, S19B). The
functional importance of this response to promote neutrophil chemotaxis during infection
was evident by the accumulation of LysMhigh/CD11b+ neutrophils in the PE (Fig. 4D,
S19C). Overall, expression of neutrophil-recruiting chemokines was highest in PE, with
some expression of CXCL2/CXCL3 in principal cells, in line with previous murine studies
(26). In the fetal kidney, there was little expression of any neutrophil-recruiting chemokine
in the distal nephron and PE (Fig. 4E).

Here we investigated immune capability in the human kidney and determined how it changes
over developmental time and anatomical space. We found that anti-microbial immunity is
spatially zonated but this feature was not evident pre-natally. Fetal kidney epithelium
showed little immune gene expression, in line with the view that it occupies a relatively
sterile environment, where anatomically polarized anti-microbial defense is redundant. We
show that a variety of immune cell populations are established in the human kidney in the
first trimester with distinct temporal patterns, but they differ from mature kidney immune
cells, with post-natal acquisition of transcriptional programmes that promote pro-
inflammatory and infection defense capabilities. The mature kidney MNP compartment was
dominated by two monocyte-derived macrophage populations, specialised for anti-bacterial
function, but also contained a smaller M2-enriched macrophage population that was
transcriptionally similar to fetal kidney macrophages, potentially indicating pre-natal
seeding, consistent with mouse studies (21).

In summary, our study provides a comprehensive description of immune topology in the
human kidney, providing a resource, which adds to the recently published murine kidney
dataset (27), to facilitate the future study of pathogenic mechanisms and the identification of
therapeutic targets in immune and infectious kidney diseases.

Supplementary Material

Refer to Web version on PubMed Central for supplementary material.

Acknowledgments

We thank M. A. Knepper (National Institutes of Health, USA) for expert advice on mature kidney nephron cell type
annotations.

Science. Author manuscript; available in PMC 2020 July 08.

E
u
r
o
p
e
P
M
C
F
u
n
d
e
r
s
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
s

E
u
r
o
p
e
P
M
C
F
u
n
d
e
r
s
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
s

Stewart et al.

Funding

We thank J. Eliasova for her assistance with illustrations.

Page 8

These experiments were principally funded by the St Baldrick’s Foundation (Robert J Arceci International Award to
S.B.). Additional funding was received from the Wellcome Trust (S.B.: 110104/Z/15/Z; M.H.: 107931/Z/15/Z;
studentships to B.J.S., G.C., A.M.R., and C.G.). Kidney cancer bio-sampling was funded by core infrastructural
funding from the Cambridge Biomedical Research Campus (CBRC) and Cancer Research UK Cambridge Centre.
Additional funding in support of individual authors was provided as follows: B.J.S (CRUK predoctoral bursary,
C63442/A25230); M.R.C. (CBRC; NIHR Blood and Transplant Research Unit, RG75628; MRC New Investigator
Research Grant, MR/N024907/1; Arthritis Research UK Cure Challenge Research Grant, 21777; NIHR Research
Professorship RP-2017-08-ST2-002); M.H. (The Lister Institute for Preventative Medicine; NIHR and Newcastle-
Biomedical Research Centre); A.F. (ISAC SRL-EL program); S.Lis, S.Lin. (joint Wellcome Trust/MRC,
099175/Z/12/Z); K.W.L (Kidney Research UK Clinical Training Fellowship, TF_013_20171124). R.V-T is
supported by an EMBO Long-Term Fellowship and a Human Frontier Science Program Long-Term Fellowship.
S.J.F is supported by a grant from children with cancer UK.

References

1. Kurts C, Panzer U, Anders HJ, Rees AJ. The immune system and kidney disease: basic concepts and

clinical implications. Nat Rev Immunol. 2013; 13:738–753. [PubMed: 24037418]

2. Giebisch G. Coupled ion and fluid transport in the kidney. N Engl J Med. 1972; 287:913–919.

[PubMed: 4561670]

3. Berry MR, et al. Renal Sodium Gradient Orchestrates a Dynamic Antibacterial Defense Zone. Cell.

2017; 170:860–874 e819. [PubMed: 28803730]

4. Young MD, et al. Single-cell transcriptomes from human kidneys reveal the cellular identity of renal

tumors. Science. 2018; 361:594–599. [PubMed: 30093597]

5. Young MD, Behjati S. SoupX removes ambient RNA contamination from droplet based single cell

RNA sequencing data. BioRxiv. 2018; doi: 10.1101/303727

6. Wang P, et al. Dissecting the Global Dynamic Molecular Profiles of Human Fetal Kidney

Development by Single-Cell RNA Sequencing. Cell reports. 2018; 24:3554–3567 e355. [PubMed:
30257215]

7. Menon R, et al. Single-cell analysis of progenitor cell dynamics and lineage specification in the

human fetal kidney. Development. 2018; 145

8. Rosenblum ND. Developmental biology of the human kidney. Semin Fetal Neonatal Med. 2008;

13:125–132. [PubMed: 18096451]

9. Julien E, El Omar R, Tavian M. Origin of the hematopoietic system in the human embryo. FEBS

Lett. 2016; 590:3987–4001. [PubMed: 27597316]

10. Mass E, et al. Specification of tissue-resident macrophages during organogenesis. Science. 2016;

353

11. Hayashi F, et al. The innate immune response to bacterial flagellin is mediated by Toll-like receptor

5. Nature. 2001; 410:1099–1103. [PubMed: 11323673]

12. Erman A, et al. Uropathogenic Escherichia coli induces serum amyloid a in mice following urinary

tract and systemic inoculation. PLoS One. 2012; 7:e32933. [PubMed: 22427910]

13. Yang J, et al. An iron delivery pathway mediated by a lipocalin. Mol Cell. 2002; 10:1045–1056.

[PubMed: 12453413]

14. Forster CS, et al. Urinary NGAL deficiency in recurrent urinary tract infections. Pediatr Nephrol.

2017; 32:1077–1080. [PubMed: 28210838]

15. Mackay LK, Kallies A. Transcriptional Regulation of Tissue-Resident Lymphocytes. Trends

Immunol. 2017; 38:94–103. [PubMed: 27939451]

16. Mackay LK, et al. Hobit and Blimp1 instruct a universal transcriptional program of tissue

residency in lymphocytes. Science. 2016; 352:459–463. [PubMed: 27102484]

17. Guilliams M, et al. Dendritic cells, monocytes and macrophages: a unified nomenclature based on

ontogeny. Nat Rev Immunol. 2014; 14:571–578. [PubMed: 25033907]

18. McGovern N, et al. Human dermal CD14(+) cells are a transient population of monocyte-derived

macrophages. Immunity. 2014; 41:465–477. [PubMed: 25200712]

Science. Author manuscript; available in PMC 2020 July 08.

E
u
r
o
p
e
P
M
C
F
u
n
d
e
r
s
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
s

E
u
r
o
p
e
P
M
C
F
u
n
d
e
r
s
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
s

Stewart et al.

Page 9

19. Bain CC, et al. Constant replenishment from circulating monocytes maintains the macrophage pool

in the intestine of adult mice. Nat Immunol. 2014; 15:929–937. [PubMed: 25151491]
20. Ginhoux F, et al. Fate mapping analysis reveals that adult microglia derive from primitive

macrophages. Science. 2010; 330:841–845. [PubMed: 20966214]

21. Schulz C, et al. A lineage of myeloid cells independent of Myb and hematopoietic stem cells.

Science. 2012; 336:86–90. [PubMed: 22442384]

22. Serushago B, Issekutz AC, Lee SH, Rajaraman K, Bortolussi R. Deficient tumor necrosis factor

secretion by cord blood mononuclear cells upon in vitro stimulation with Listeria monocytogenes.
J Interferon Cytokine Res. 1996; 16:381–387. [PubMed: 8727078]

23. Hunt DW, Huppertz HI, Jiang HJ, Petty RE. Studies of human cord blood dendritic cells: evidence

for functional immaturity. Blood. 1994; 84:4333–4343. [PubMed: 7994049]

24. Vento-Tormo R, et al. Single-cell reconstruction of the early maternal-fetal interface in humans.

Nature. 2018; 563:347–353. [PubMed: 30429548]

25. Godaly G, Ambite I, Svanborg C. Innate immunity and genetic determinants of urinary tract

infection susceptibility. Curr Opin Infect Dis. 2015; 28:88–96. [PubMed: 25539411]
26. Bens M, et al. Flagellin/TLR5 signalling activates renal collecting duct cells and facilitates
invasion and cellular translocation of uropathogenic Escherichia coli. Cell Microbiol. 2014;
16:1503–1517. [PubMed: 24779433]

27. Park J, et al. Single-cell transcriptomics of the mouse kidney reveals potential cellular targets of

kidney disease. Science. 2018; 360:758–763. [PubMed: 29622724]

28. Lun A, Riesenfeld S, Andrews T, Gomes T, bioRxiv JM. Distinguishing cells from empty droplets

in droplet-based single-cell RNA sequencing data. biorxiv org. 2018; doi: 10.1101/234872

29. McCarthy DJ, Campbell KR, Lun A, W Q. Scater: pre-processing, quality control, normalization

and visualization of single-cell RNA-seq data in R. Bioinformatics. 2017; 33:1179–1186.
[PubMed: 28088763]

30. Butler A, Hoffman P, Smibert P, Papalexi E, Satija R. Integrating single-cell transcriptomic data
across different conditions, technologies, and species. Nature Biotechnology. 2018; 36:411–420.
31. Haghverdi L, Lun ATL, Morgan MD, Marioni JC. Batch effects in single-cell RNA-sequencing
data are corrected by matching mutual nearest neighbors. Nature Biotechnology. 2018; 36:421–
427.

32. Becht E, McInnes L, Healy J, Dutertre C-A, Kwok IWH, Ng LG, Ginhoux F, Newell EW.

Dimensionality reduction for visualizing single-cell data using UMAP. Nature Biotechnology.
2019; 37:38–45.

33. Waltman L, van Eck NJ. A smart local moving algorithm for large-scale modularity-based

community detection. Eur Phys J B. 2013; 86:471.

34. Villani A-C, Satija R, Reynolds G, Sarkizova S, Shekhar K, Fletcher J, Griesbeck M, Butler A,

Zheng S, Lazo S, Jardine L, et al. Single-cell RNA-seq reveals new types of human blood dendritic
cells, monocytes, and progenitors. Science. 2017; 356:eaah4573. [PubMed: 28428369]
35. Lindgren D, Eriksson P, Krawczyk K, Nilsson H, Hansson J, Veerla S, Sjölund J, Höglund M,

Johansson ME, Axelson H. Cell-Type-Specific Gene Programs of the Normal Human Nephron
Define Kidney Cancer Subtypes. CellReports. 2017; 20:1476–1489.

36. Hung CS, Dodson KW, Hultgren SJ. A murine model of urinary tract infection. Nat Protoc. 2009;

4:1230–1243. [PubMed: 19644462]

37. Anderson KG, Mayer-Barber K, Sung H, Beura L, James BR, Taylor JJ, Qunaj L, Griffith TS,

Vezys V, Barber DL, Masopust D. Intravascular staining for discrimination of vascular and tissue
leukocytes. Nat Protoc. 2014; 9:209–222. [PubMed: 24385150]

38. Breton G, Zheng S, Valieris R, Tojal da Silva I, Satija R, Nussenzweig MC. Human dendritic cells
(DCs) are derived from distinct circulating precursors that are precommitted to become CD1c +or
CD141 +DCs. J Exp Med. 2016

39. Cildir G, Pant H. A. L. J. O. Experimental, 2017, The transcriptional program, functional

heterogeneity, and clinical targeting of mast cells. J Exp Med. 2017; 214:2491–2506. [PubMed:
28811324]

40. Collin M, McGovern N, Haniffa M. Human dendritic cell subsets. Immunology. 2013; 140:22–30.

[PubMed: 23621371]

Science. Author manuscript; available in PMC 2020 July 08.

E
u
r
o
p
e
P
M
C
F
u
n
d
e
r
s
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
s

E
u
r
o
p
e
P
M
C
F
u
n
d
e
r
s
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
s

Stewart et al.

Page 10

41. Wong KL, Tai J-YJ, Wong W-C, Han H, Sem X, Yeap W-H, Kourilsky P, Wong SC. Gene

expression profiling reveals the defining features of the classical, intermediate, and nonclassical
human monocyte subsets. Blood. 2011; 118:e16–31. [PubMed: 21653326]

42. Crinier A, Milpied P, Escalière B, Piperoglou C, Galluso J, Balsamo A, Spinelli L, Cervera-Marzal
I, Ebbo M, Girard-Madoux M, Jaeger S, et al. High-Dimensional Single-Cell Analysis Identifies
Organ-Specific Signatures and Conserved NK Cell Subsets in Humans and Mice. Immunity. 2018;
49:971–986.e5. [PubMed: 30413361]

43. See P, Dutertre C-A, Chen J, Günther P, McGovern N, Irac SE, Gunawan M, Beyer M, Händler K,

Duan K, Sumatoh HRB, et al. Gea-Mallorquí, Mapping the human DC lineage through the
integration of high-dimensional techniques. Science. 2017; 66:eaag3009.

44. Nimmerjahn F, Ravetch JV. Fcgamma receptors: old friends and new family members. Immunity.

2006; 24:19–28. [PubMed: 16413920]

45. Nimmerjahn F, Ravetch JV. Fcgamma receptors as regulators of immune responses. Nat Rev

Immunol. 2008; 8:34–47. [PubMed: 18064051]

46. Palmer C, Diehn M, Alizadeh AA, Brown PO. Cell-type specific gene expression profiles of
leukocytes in human peripheral blood. BMC Genomics. 2006; 7:115. [PubMed: 16704732]
47. Björklund ÅK, Forkel M, Picelli S, Konya V, Theorell J, Friberg D, Sandberg R, Mjösberg J. The
heterogeneity of human CD127+ innate lymphoid cells revealed by single-cell RNA sequencing.
Nat Immunol. 2016; 17:451–460. [PubMed: 26878113]

48. Zheng GXY, Terry JM, Belgrader P, Ryvkin P, Bent ZW, Wilson R, Ziraldo SB, Wheeler TD,

McDermott GP, Zhu J, Gregory MT, et al. Massively parallel digital transcriptional profiling of
single cells. Nature Communications. 2017; 8:1–12.

49. Habuka M, Fagerberg L, Hallström BM, Kampf C, Edlund K, Sivertsson Å, Yamamoto T, Pontén

F, Uhlén M, Odeberg J, Mischak H. The Kidney Transcriptome and Proteome Defined by
Transcriptomics and Antibody-Based Profiling. PLoS ONE. 2014; 9:e116125–19. [PubMed:
25551756]

50. Chabardès-Garonne D, Mejéan A, Aude J-C, Cheval L, Di Stefano A, Gaillard M-C, Imbert-
Teboul M, Wittner M, Balian C, Anthouard V, Robert C, et al. A panoramic view of gene
expression in the human kidney. Proc Natl Acad Sci USA. 2003; 100:13710–13715. [PubMed:
14595018]

51. Clark JZ, Chen L, Chou C-L, Jung HJ, Lee JW, Knepper MA. Cell-Type Selective Markers

Represented in Whole-Kidney RNA-Seq Data. bioRxiv. 2018

52. Higgins J, Wang L, Kambham N. Gene expression in the normal adult human kidney assessed by
complementary DNA microarray. Molecular Biology of the Cell. 2004; 15:649–656. [PubMed:
14657249]

53. Metsuyanim S, Harari-Steinberg O, Buzhor E, Omer D, Pode-Shakked N, Ben-Hur H, Halperin R,
Schneider D, Dekel B. Expression of stem cell markers in the human fetal kidney. PLoS ONE.
2009; 4:e6709. [PubMed: 19696931]

54. Yu ASL. Claudins and the kidney. J Am Soc Nephrol. 2015; 26:11–19. [PubMed: 24948743]
55. Philippeos C, Telerman SB, Oulès B, Pisco AO, Shaw TJ, Elgueta R, Lombardi G, Driskell RR,
Soldin M, Lynch MD, Watt FM. Spatial and Single-Cell Transcriptional Profiling Identifies
Functionally Distinct Human Dermal Fibroblast Subpopulations. Journal of Investigative
Dermatology. 2018; 138:811–825. [PubMed: 29391249]

56. Wang W, Morales-Nebreda L, Feng G, Wu M, Zhou X, Lafyatis R, Lee J, Hinchcliff M, Feghali-
Bostwick C, Lakota K, Budinger GRS, et al. Tenascin-C drives persistence of organ fibrosis.
Nature Communications. 2016; 7:1–14.

57. Aird WC. Phenotypic heterogeneity of the endothelium: II. Representative vascular beds. Circ Res.

2007; 100:174–190. [PubMed: 17272819]

58. Heliot C, Desgrange A, Buisson I, Prunskaite-Hyyryläinen R, Shan J, Vainio S, Umbhauer M,

Cereghini S. HNF1B controls proximal-intermediate nephron segment identity in vertebrates by
regulating Notch signalling components and Irx1/2. Development. 2013; 140:873–885. [PubMed:
23362348]

59. O’Brien LL, McMahon AP. Induction and patterning of the metanephric nephron. Seminars in Cell

and Developmental Biology. 2014; 36:31–38. [PubMed: 25194660]

Science. Author manuscript; available in PMC 2020 July 08.

Stewart et al.

Page 11

60. Brunskill EW, Aronow BJ, Georgas K. B. R. D. cell: 2008, Atlas of gene expression in the

developing kidney at microanatomic resolution. Developmental Cell. 2008; 15:781–791. [PubMed:
19000842]

61. Michos O. Kidney development: from ureteric bud formation to branching morphogenesis. Curr

Opin Genet Dev. 2009; 19:484–490. [PubMed: 19828308]

62. Reginensi A, Clarkson M, Neirijnck Y, Lu B, Ohyama T, Groves AK, Sock E, Wegner M,

Costantini F, Chaboissier M-C, Schedl A. SOX9 controls epithelial branching by activating RET
effector genes during kidney development. hmg. 2011; 20:1143–1153.

63. Costantini F, Kopan R. Patterning a complex organ: branching morphogenesis and nephron

segmentation in kidney development. Dev Cell. 2010; 18:698–712. [PubMed: 20493806]

64. Valerius MT, Patterson LT, Feng Y, Potter SS. Hoxa 11 is upstream of Integrin α8 expression in the

developing kidney. Proc Natl Acad Sci USA. 2002; 99:8090–8095. [PubMed: 12060755]

65. Schell C, Wanner N, Huber TB. Glomerular development--shaping the multi-cellular filtration unit.

Seminars in Cell and Developmental Biology. 2014; 36:39–49. [PubMed: 25153928]
66. Harding SD, Armit C, Armstrong J, Brennan J, Cheng Y, Haggarty B, Houghton D, Lloyd-

MacGilp S, Pi X, Roochun Y, Sharghi M, et al. The GUDMAP database--an online resource for
genitourinary research. Development. 2011; 138:2845–2853. [PubMed: 21652655]

E
u
r
o
p
e
P
M
C
F
u
n
d
e
r
s
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
s

E
u
r
o
p
e
P
M
C
F
u
n
d
e
r
s
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
s

Science. Author manuscript; available in PMC 2020 July 08.

Stewart et al.

Page 12

Single cell RNA sequencing defines the immune landscape of the human kidney

One Sentence Summary

E
u
r
o
p
e
P
M
C
F
u
n
d
e
r
s
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
s

E
u
r
o
p
e
P
M
C
F
u
n
d
e
r
s
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
s

Science. Author manuscript; available in PMC 2020 July 08.

Stewart et al.

Page 13

E
u
r
o
p
e
P
M
C
F
u
n
d
e
r
s
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
s

E
u
r
o
p
e
P
M
C
F
u
n
d
e
r
s
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
s

Fig. 1. Mapping the spatial and temporal architecture of the mature and developing human
kidney
A. Anatomy of the human kidney.
B. UMAP plot of 40,268 human mature kidney cells. Compartments illustrated in colors
(red, immune; blue, vasculature; green, nephron; mauve, stroma). Annotations derived from
compartment-specific analysis (Fig. S8, 11, 13).
C. UMAP plots illustrating the contribution made by cells from biopsies at inferred biopsy
depths, with density contours colored according to compartments [B].
D. Barplots showing the proportion of immune cells at each inferred biopsy depth.
E. UMAP plot of 27,203 human fetal kidney cells. Compartments illustrated in colors (red,
immune; blue, vasculature; green, developing nephron; mauve, stroma). Annotations derived
from compartment-specific analysis (Fig. S7, 15).

Science. Author manuscript; available in PMC 2020 July 08.

Stewart et al.

Page 14

F. Diagram illustrating steps in development of the nephron through early fetal life. The
ureteric bud (UB) undergoes branching and instructs development of cap mesenchyme (CM)
into renal vesicle (RV) and subsequently S-shaped body (SSB). UB forms distal nephron
structures, whilst SSB forms proximal structures.
G. Proportional contribution of fetal developing nephron cell types at distinct developmental
time points. Cell types are colored as in Fig S7F.
H. UMAP plots illustrating the contribution made by cells from kidneys at discrete
developmental time points, with density contours colored according to compartments [E].
PCW, post-conception weeks. Annotations: MNP, mononuclear phagocyte; MPhage,
macrophage; NØ, neutrophil; Mast, mast cell; pDC, plasmacytoid dendritic cell; B, B cell;
NK, natural killer cell; NKT, natural killer T cell; CD4 T, CD8 T, CD4 and CD8 T cell; MK,
megakaryocyte; AVRE, ascending vasa recta endothelium; DVRE, descending vasa recta
endothelium; PCE, peritubular capillary endothelium; GE, glomerular endothelium; PE,
pelvic epithelium; TE, transitional epithelium of ureter; LOH, loop of Henle; CNT,
connecting tubule; PC, principal cell; IC (A+B), type A and B intercalated cells; Podo,
podocyte; PT, proximal tubule; dPT, distinct proximal tubule; EPC, epithelial progenitor
cell; Fib, fibroblast; MFib, myofibroblast; CM, cap mesenchyme; Prl-CM, proliferating cap
mesenchyme; RV, renal vesicle; SSB, S shaped body; UB, ureteric bud.

E
u
r
o
p
e
P
M
C
F
u
n
d
e
r
s
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
s

E
u
r
o
p
e
P
M
C
F
u
n
d
e
r
s
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
s

Science. Author manuscript; available in PMC 2020 July 08.

Stewart et al.

Page 15

E
u
r
o
p
e
P
M
C
F
u
n
d
e
r
s
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
s

E
u
r
o
p
e
P
M
C
F
u
n
d
e
r
s
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
s

Fig. 2. Gene expression patterns in the developing and mature nephron
A. Heatmap of mean similarity scores between fetal and mature nephron cell types.
B. Upper panel: heatmap of mean scaled scores for immune process genesets (Innate
immune response, GO:0045087; Defense response, GO:0006952; Immune response,
GO:0006955; Antimicrobial humoral response, GO:0019730). Lower panel: heatmap of
mean expression values of antimicrobial peptides (AMPs) amongst pelvic epithelium marker
genes. Point size shows the fraction of cells with non-zero expression.
C. Log10 transformed relative expression levels of LCN2 and SAA1 (human) and Lcn2 and
Saa1/2 (murine) in kidneys following UPEC challenge (measured by qPCR, values relative
to unstimulated cortical samples (n = 3 (human), n = 6 (murine), ANOVA - ***. p < 0.0005;
**, p <0.005; *, p < 0.05; NS, not significant). Boxplots show median values and
interquartile range. C, cortex; M/P, medulla/pelvis.

Science. Author manuscript; available in PMC 2020 July 08.

Stewart et al.

Page 16

E
u
r
o
p
e
P
M
C
F
u
n
d
e
r
s
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
s

E
u
r
o
p
e
P
M
C
F
u
n
d
e
r
s
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
s

Fig. 3. Myeloid cell populations in the mature and developing kidney
A. UMAP plot illustrating the cell populations identified in 7803 mature kidney immune
cells. The myeloid sub-compartment is circled and lymphoid cells de-colored.
B. UMAP plot illustrating four subsets of mononuclear phagocyte (MNPa-d), neutrophils,
mast cells, and plasmacytoid dendritic cells, after reanalysis of 1347 cells of the mature
kidney myeloid sub-compartment.
C. Violin plots showing expression levels of canonical myeloid population markers.

Science. Author manuscript; available in PMC 2020 July 08.

Stewart et al.

Page 17

D. Efficiency of FITC-labelled UPEC phagocytosis by CD14+ HLA-DR+ CD36+ (MNPa)
and CD14+ HLA-DR+ CD206+ (MNPd) cells from adult human kidney, by flow cytometry
(n = 4; *, p < 0.05 (Wilcoxson rank sum test)). Representative plot showing technical
replicates.
E. UMAP plot illustrating the cell populations identified in 6847 fetal immune cells.
Lymphoid cells are decolored.
F. Plot showing proportional contribution of cell types identified in [3E] to the fetal immune
compartment over developmental time. PCW, post-conception weeks. Lymphoid cells are
decolored.
H. Plot showing geneset scores of M1 and M2 macrophage polarisation signatures (derived
from GSE5099 - LPS vs Il4 stimulated bone marrow derived macrophages) amongst fetal
and mature MNP. Grey points, single cell geneset scores; colored points, mean scores for
each cell type.

E
u
r
o
p
e
P
M
C
F
u
n
d
e
r
s
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
s

E
u
r
o
p
e
P
M
C
F
u
n
d
e
r
s
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
s

Science. Author manuscript; available in PMC 2020 July 08.

Stewart et al.

Page 18

E
u
r
o
p
e
P
M
C
F
u
n
d
e
r
s
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
s

E
u
r
o
p
e
P
M
C
F
u
n
d
e
r
s
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
s

Fig. 4. Spatial topology of myeloid cell populations in the mature kidney
A. Heatmap of chemokine ligand-receptor interactions between mature myeloid and nephron
cell types arranged by proximal to distal nephron organization. Point size indicates
permutation p value (CellPhoneDB). Color indicates the scaled mean expression level of
ligand and receptor (Mol1/2).
B. Confocal microscopy images illustrating co-expression of CK17 (white), CXCL8 (green),
and LCN2 (red) in human medullary and pelvic epithelium. M/P, medulla/pelvis. Scale bars
20 μm.

Science. Author manuscript; available in PMC 2020 July 08.

Stewart et al.

Page 19

C. Plots illustrating Log10 transformed relative expression of CXCL1 and CXCL8 (human)
and Cxcl1 and Cxcl2 (murine) in response to UPEC at distinct kidney depths, by qPCR.
Values relative to unstimulated cortex (n = 3 (human), n = 6 (murine), ANOVA - ***, p <
0.0005; **, p <0.005; *, p < 0.05; NS, not significant). Boxplots show median values and
interquartile range. C, cortex; M/P, medulla/pelvis.
D. Confocal microscopy images of kidneys from LysM-GFP transgenic reporter mice
stained with anti-GFP (green), phalloidin (white), and anti-CD11b (red) after catheterisation
with UPEC or PBS control. Left panels: full depth tiles from cortex to pelvis. Right panels:
zoom of the region highlighted (yellow). Scale bars 70 μm.
E. Heatmap of mean expression values of neutrophil recruiting chemokines. Point size
shows the fraction of cells with non-zero expression.

E
u
r
o
p
e
P
M
C
F
u
n
d
e
r
s
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
s

E
u
r
o
p
e
P
M
C
F
u
n
d
e
r
s
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
s

Science. Author manuscript; available in PMC 2020 July 08.

