http://www.jhltonline.org
ORIGINAL TRANSLATIONAL SCIENCE
Human lung allografts experience persistent
]]
]] ]]]]]]
fibrogenic shift following acute cellular rejection
Andrew S. Potter, MS,a Nirmal S. Sharma, MD,b Yasufumi Goda, MD,b
Kapil N. Patel, MD,c Muhammad R. Qureshi, MD,d Kieran Halloran, MD, MS,e
Philip F. Halloran, MD, PhD,f Carolyn Wallace, MHA, RRT-NPS,g
Awais Ashfaq, MD,a,h David L.S. Morales, MD,a,h and
Don Hayes Jr. MD, MS, MEd, MBAa,g,i
From the aThe Heart Institute, Cincinnati Children’s Hospital Medical Center, Cincinnati, OH; bBaylor College of
Medicine, Houston, TX; cWake Forest University School of Medicine, Winston-Salem, NC; dCenter for Advanced Lung
diseases, Tampa General Hospital/University of South Florida, Tampa, FL; eDepartment of Medicine, University of
Alberta, Edmonton, Canada; fAlberta Transplant Applied Genomics Center, University of Alberta, Edmonton, Canada;
gDivision of Pulmonary Medicine, Cincinnati Children’s Hospital Medical Center, Cincinnati, OH; hDepartment of
Cardiothoracic Surgery, Cincinnati Children's Hospital, Cincinnati, OH; and the iDepartment of Pediatrics, University of
Cincinnati College of Medicine, Cincinnati, OH.
KEYWORDS: RATIONALE: Acute cellular rejection (ACR) remains a significant challenge in lung transplantation,
Acute cellular rejection; with incomplete understanding of its molecular mechanisms and pathways linking ACR to chronic
Cell atlas; lung allograft dysfunction (CLAD).
Chronic lung allograft OBJECTIVES: To characterize the cellular and molecular mechanisms underlying ACR in lung allo-
dysfunction; grafts using single cell genomics and identify potential therapeutic targets for CLAD.
Donor-derived cells; METHODS: Single cell RNA-sequencing of freshly collected lung tissue was performed across 8 pe-
Interferon signaling; diatric and adult patients with ACR, Resolved ACR, and surveillance biopsies without ACR.
Lung transplant; Validation included gene microarray analysis, immunofluorescence, and single cell ATAC-seq.
Natural killer cells; MEASUREMENTS AND MAIN RESULTS: Gene set enrichment analysis revealed persistent TGF-β sig-
Single-cell RNA naling and PI3K/AKT/mTOR pathway activation in both ACR and Resolved samples, validated by
sequencing immunofluorescence showing sustained elevation of mTOR activation marker phosphorylated-S6 ri-
bosomal protein and COL3A1. Fibrogenic cells exhibited myofibroblast gene signatures via me-
senchymal state transitions rather than epithelial- or endothelial-to-mesenchymal transition. Cell
communication analysis showed increased Type II Interferon signaling, with Jak/Stat pathway acti-
vation in endothelial and basal cells, and reduced VE-Cadherin staining in ACR. Compositional
Abbreviations: ACR, acute cellular rejection; APC, antigen-presenting cell; ATAC-seq, assay for transposase-accessible chromatin sequencing; BAL,
bronchoalveolar lavage; BCR, B cell receptor; CLAD, chronic lung allograft dysfunction; CAP, cold-active protease; HLA, human leukocyte antigen; IFN-γ,
interferon gamma; ISHLT, International Society for Heart and Lung Transplantation; log2FC, log2 fold change; LTx, lung transplantation; MAIT, mucosal-
associated invariant T cell; NK, natural killer; NF-κB, nuclear factor kappa-light-chain-enhancer of activated B cells; PI3K/AKT/mTOR, phosphatidyli-
nositol 3-kinase/protein kinase B/mammalian target of rapamycin; RNA-seq, RNA sequencing; scRNA-seq, single-cell RNA sequencing; TF, transcription
factor; TGF-β, transforming growth factor beta; TNF, tumor necrosis factor; IFN-II, type 2 interferon; UMAP, uniform manifold approximation and
projection; VEGF, vascular endothelial growth factor
Corresponding author: Don Hayes Jr., MD, MS, MEd, MBA, Cincinnati Children’s Hospital Medical Center, University of Cincinnati College of
Medicine, 3333 Burnet Ave, MLC 7041, Cincinnati, OH 45229.
E-mail address: don.hayes@cchmc.org.
1053-2498/© 2026 The Authors. Published by Elsevier Inc. on behalf of International Society for Heart and Lung Transplantation. This is an open access
article under the CC BY license (http://creativecommons.org/licenses/by/4.0/).
https://doi.org/10.1016/j.healun.2026.02.1666

1150 The Journal of Heart and Lung Transplantation, Vol 45, No 7, July 2026
analysis revealed increased cytotoxic, memory T cells and dendritic cells, with persistent reduction of
natural killer cells in ACR and Resolved. Donor/recipient analysis revealed predominantly recipient-
derived immune cells in ACR.
CONCLUSIONS: Persistent TGF-β and mTOR pathway activation following histologic ACR resolution
provides molecular insight into ACR-CLAD linkage and suggests mTOR inhibition and TGF-β
blockade as potential therapeutic mechanisms to prevent CLAD.
J Heart Lung Transplant 2026;45:1149–1161
© 2026 The Authors. Published by Elsevier Inc. on behalf of International Society for Heart and Lung
Transplantation. This is an open access article under the CC BY license (http://creativecommons.org/
licenses/by/4.0/).
Introduction Materials and methods
For patients with end-stage lung failure, lung transplant Patient characteristics
(LTx) remains the only viable treatment option. However,
compared to other solid organ transplants, LTx recipients The study was approved by the Institutional Review Board of
have higher rates of acute cellular rejection (ACR).1 ACR Cincinnati Children’s Hospital Medical Center, and informed
increases the risk for developing chronic lung allograft consent/assent was obtained from all participants. Over a 3-year
dysfunction (CLAD), which affects approximately 50% of period, LTx recipients undergoing transbronchial biopsy were
recipients by 5 years post-LTx, limiting long-term sur- recruited. Lung allograft tissue was assessed histologically ac-
vival.1–11 The International Society for Heart and Lung cording to ISHLT guidelines.12 Our cohort included patients
Transplantation (ISHLT) defines A-grade ACR as perivas- with ACR (ISHLT Grade A2-A4), Resolved ACR (A0 at time
cular mononuclear infiltration, graded A1 to A4, with up to of biopsy with prior ACR history), and Never (no ACR within
half of LTx recipients experiencing ACR within the first 2 years post-transplant). A1-grade ACR was not observed
year post-transplant.3,12 during the study period. Histological resolution was observed
The standard treatment for ACR has remained un- after one treatment course of intravenous high-dose methyl-
changed, relying on high-dose systermic corticosteroids. prednisolone (10mg/kg daily for 3 days) except for Patient 1,
With ACR strongly linked to later CLAD development, this who died due to refractory ACR despite 2 corticosteroid
suggests that current treatments are inadequate to prevent courses and antithymocyte globulin. Maintenance im-
long-term complications.2–4Thus, there is a critical need to munosuppression included tacrolimus, mycophenolate, and
identify molecular mechanisms and targeted therapies prednisone for all patients (Tables 1–2, Supplemental Table 1,
linking ACR and CLAD. Supplement A).
The hallmark of chronic, progressive lung disease with
Single-cell RNA sequencing
associated fibrosis is an aberrant wound-healing response
characterized by myofibroblast activation and excessive, sus-
tained excessive extracellular matrix (ECM) deposition.11,13,14 Excess biopsy tissue was dissociated using cold-active protease
Transforming growth factor beta (TGF-β) signaling drives (CAP) methodology as previously described, with 5–20 mg
total weighed tissue used for dissociation.17 Cell suspensions
myofibroblast activation and ECM production, playing a
central role in fibrotic remodeling.14,15 Myofibroblast origins were processed with 10X Genomics (3’v3.1 or 5’v1.1/v2
chemistry) and sequenced on NovaSeq 6000. FASTQ files
in fibrotic disease remains debated, including tissue-resident
were processed with Cell Ranger, with analysis in Seurat with
fibroblasts, pericytes, or epithelial/endothelial transdiffer-
entiation (EMT/EndoMT).14 Type II Interferon (IFN-γ) sig- batch correction for chemistry differences. Cell types were
annotated using reference atlases18–20 and subclustering. Dif-
naling also plays a critical role in allograft rejection through
HLA class II induction and immune cell activation.16 Identi- ferential composition was assessed with scCODA21 and
Speckle. Differential expression used pseudobulk aggregation
fying persistent fibrotic and inflammatory pathways after
with DESeq2 comparing ACR and Resolved to Never. Cell-
histological ACR resolution can help explain the link between
Chat analyzed cell signaling. Donor/recipient annotation used
ACR and CLAD.
SNP genotyping with CellSNP-lite and Vireo (Supplement A).
Single-cell RNA-sequencing (scRNA-seq) addresses this
need by facilitating cellular-level analysis of patient biop-
sies.11 Using an unbiased approach with scRNA-seq of Validation studies
freshly collected transbronchial biopsies from pediatric and
adult LTx recipients with ACR, Resolved ACR after Single-cell ATAC-seq was processed using Signac and
treatment with high-dose systemic corticosteroid therapy chromVAR. Historical microarray data22was analyzed with
(Resolved) and Never ACR (Never), we created a com- limma for cell type enrichment validation. Immuno-
prehensive cellular atlas and identified novel molecular fluorescence images were acquired on an Olympus VS200,
changes specific to ACR that persisted after histological analyzed in QuPath, with significance determined by
resolution despite being treated. mixed-effects logistic regression (Supplement A).

| Potter et al. | Human Lung ACR and Fibrogenic Shift  |     |     |     |     |     |     | 1151   |
| ------------- | ------------------------------------ | --- | --- | --- | --- | --- | --- | ------ |
Results
 hctamssorC
|     | evitageN evitageN evitageN | evitageN evitageN evitageN evitageN evitageN |     |     |     |     |     |     |
| --- | -------------------------- | -------------------------------------------- | --- | --- | --- | --- | --- | --- |
Cell atlas of lung allograft tissue
)B/T(
Eight patients were enrolled in the study, 4 experiencing
elbaliavA toN A2-A4-grade ACR. We analyzed 56,676 cells from fresh
 sucoL RD hctamsiM
|     |     |     | transbronchial  | biopsies  | across  | 3  conditions:  |     | 23,054  |
| --- | --- | --- | --------------- | --------- | ------- | --------------- | --- | ------- |
Resolved, 16,654 Never and 16,968 ACR. Using reference
|     | 2 2 3 | 3 3 4 4 |     |     |     |     |     |     |
| --- | ----- | ------- | --- | --- | --- | --- | --- | --- |
mapping and iterative clustering of lymphoid cells, 59 un-
elbaliavA toN ique cell clusters (≥10 cells each) were identified across
hctamsiM major  lung  compartments:  lymphoid,  myeloid,  stromal,
 sucoL B
|     |       |         | epithelial  | and  endothelial.  | (Figure  |     | 1,  Supplemental  |     |
| --- | ----- | ------- | ----------- | ------------------ | -------- | --- | ----------------- | --- |
|     | 2 1 1 | 2 2 2 2 | Figure 1).  |                    |          |     |                   |     |
elbaliavA toN SNP genotyping revealed immune infiltrates were pre-
dominantly recipient-derived in ACR biopsies (0–1.94%
 sucoL A hctamsiM
donor-derived lymphoid cells), with higher donor-derived
2 2 2 2 1 2 1 immune fractions in Never biopsies obtained within the first
6 months post-LTx (Supplemental Figure 2, Supplemental
elbaliavA toN
|  ALH latoT |     |     | Table 2). |     |     |     |     |     |
| ---------- | --- | --- | --------- | --- | --- | --- | --- | --- |
hctamsiM
Cell-type marker information is available through the
|     |         |             | Lung  AlloMap  | web  portal  | (https://lungallomap.net)  |     |     | and  |
| --- | ------- | ----------- | -------------- | ------------ | -------------------------- | --- | --- | ---- |
|     | 11 21 9 | 41 21 61 41 |                |              |                            |     |     |      |
Supplemental Table 3.
ecaR ronoD
cinapsiH cinapsiH
etihW etihW etihW etihW kcalB etihW TGF-β-mediated pathways persistently activated
following ACR
xeS ronoD
elameF elameF elameF elameF elameF Comparative analysis of ACR, Resolved, and Never con-
|     | elaM | elaM elaM |     |     |     |     |     |     |
| --- | ---- | --------- | --- | --- | --- | --- | --- | --- |
ditions revealed a shared set of upregulated > 1 log2 fold
change (log2FC) genes in ACR and Resolved across mul-
tiple (≥8) cell clusters, indicating persistent gene expression
egA ronoD
changes. Enrichr analysis of shared upregulated genes using
14 61 03 23 71 61 51 05 the Hallmark gene set identified significant enrichment in
TGF-β
 gm 0001 enosinderplyhteM Signaling  and  downstream  pathways,  including
nilubolg etycomyhtitnA nilubolg etycomyhtitnA nilubolg etycomyhtitnA nilubolg etycomyhtitnA nilubolg etycomyhtitnA phosphatidylinositol 3-kinase/protein kinase B/mammalian
poartnI  >  >  1 x VI target of rapamycin (PI3K/AKT/mTOR) and G2/M check-
 dna 1 x bamixilisaB
point (Figure 2A, Supplemental Table 4). TGF-β1, known
bamixilisaB to activate mTOR pathway and modulate cell cycle,23,24
noitcudnI
 scitsiretcarahC tnalpsnarT dna scihpargomeD tneitaP remained upregulated in multiple cell types after resolution,
enoN
with maximum log2FC (MaxFC) of 2.5 in Alveolar Epi-
thelial Type 2 in ACR, along with key mTOR activation
 raloevla yranomluP
|     | xTL rof noitacidnI | esaesid gnul citsyC DLI detaler PISN |     |     |     |     |     |     |
| --- | ------------------ | ------------------------------------ | --- | --- | --- | --- | --- | --- |
 niev yranomluP genes AKT1 (MaxFC 2.6, Airway Smooth Muscle ACR)
|     | sisorbfi citsyC sisorbfi citsyC | sisorbfi citsyC |     |     |     |     |     |     |
| --- | ------------------------------- | --------------- | --- | --- | --- | --- | --- | --- |
 sitiloihcnorB snanretilbo sisonietorp and HRAS (MaxFC 3, Pericyte ACR) (Figure 2B). Notably,
sisonets
|     |     |     | these  molecular  | changes  | persisted  | in  Resolved  |     | biopsies  |
| --- | --- | --- | ----------------- | -------- | ---------- | ------------- | --- | --------- |
collected from weeks to months after histologic resolution
(median 166 days post-ACR). Stratification by ACR grade
cinapsiH cinapsiH demonstrated consistent pathway activation regardless of
cibarA
ecaR etihW etihW etihW etihW kcalB severity for key genes (TGFB1, AKT1, MAPK1, HRAS, and
MARCKS): high-grade (A3-A4), mild (A2) and Resolved
|     |               |                      | showed  similar  | upregulation  | (median  |     | 1.5–1.8  | log2FC)  |
| --- | ------------- | -------------------- | ---------------- | ------------- | -------- | --- | -------- | -------- |
|     | elameF elameF | elameF elameF elameF |                  |               |          |     |          |          |
elaM elaM elaM across 21–28 cell types (Supplemental Figure 3A). Gene
xeS
|     |     |     | score  enrichment  | analysis  | (UCell)  | indicated  |     | increased  |
| --- | --- | --- | ------------------ | --------- | -------- | ---------- | --- | ---------- |
 xTL ta egA PI3K/AKT/mTOR activation in stromal cells across ACR
)sraeY(
grades (high-grade and mild) and Resolved compared to
|     | 71 31 72 | 51 51 51 31 14 | Never (Supplemental Figure 3B). |     |     |     |     |     |
| --- | -------- | -------------- | ------------------------------- | --- | --- | --- | --- | --- |
Immunofluorescence analysis confirmed increased TGF-
| 1 elbaT | 1 tneitaP 2 tneitaP 3 tneitaP | 4 tneitaP 5 tneitaP 6 tneitaP 7 tneitaP 8 tneitaP |                    |           |     |            |      |           |
| ------- | ----------------------------- | ------------------------------------------------- | ------------------ | --------- | --- | ---------- | ---- | --------- |
|         |                               |                                                   | β/mTOR  signaling  | activity  | in  | both  ACR  | and  | Resolved  |
tneitaP
groups compared to Never. Using mixed-effects logistic
regression (n=4 ACR, n=3 Resolved, n=3 Never biopsies),

semoctuO
dna
ataD
lacinilC
yspoiB
2
elbaT
tnerruC
enilesaB
enilesaB
tesnO
DALC
tesnO
DALC
litnU
emiT
%1VEF
CVF
tnerruC
mumixaM
mumixaM
ecniS
syaD
fo
rebmuN
emiT
egatS
%1VEF
%
CVF
tesnO
DALC
detciderP
detciderP
%
%1VEF
%
CVF
RCA
tsaL
fo
sedosipE
xTL-tsoP
RCA(
RCA
detciderP
detciderP
)shtnoM(
DALC
xBBT
ta
xBBT
ta
detciderP
detciderP
d4ClenaP
lariV
ygoloiborciM
edosipE
RCA
suoiverP
)shtnoM(
)sutatS
edarG
yrtsimehC
refiitnedI
lebaL
tneitaP
morf
deid(
oN
%95
%37
%57
%29
evitageN
evitageN
sanomoduesP
891
1
:sedosipe
2
81
ereveS
4A
1.3v'3
4A_10
10b_10tP
1
tneitaP
RCA
yrotcarfer
asonigurea
3A
1
,2A
gniwollof
)yspoib
3A_30
%46
%87
%57
%29
evitageN
evitageN
sanomoduesP
53
91
etaredoM
3A
1.3v'3
3A_30
20b_10tP
asonigurea
%25
%26
9
seY
%65
%76
%78
%88
evitageN
evitageN
smsinagro
oN
enoN
19
etaredoM
3A
1.3v'3
3A_40
10b_20tP
2
tneitaP
8
%07
%38
%78
%88
evitageN
evitageN
smsinagro
oN
53
3A
:edosipe
1
29
devloseR
0A
1.3v'3
0A_50
20b_20tP
A/N
A/N
A/N
oN
%67
%17
%87
%27
evitageN
evitageN
smsinagro
oN
enoN
1
enoN
0A
1.1v'5
0A_60
10b_30tP
3
tneitaP
A/N
%37
%07
%87
%27
evitageN
evitageN
smsinagro
oN
2
enoN
0A
1.1v'5
0A_70
20b_30tP
A/N
%17
%07
%87
%27
evitageN
evitageN
smsinagro
oN
3
enoN
0A
1.1v'5
0A_80
30b_30tP
A/N
%47
%57
%67
%87
evitageN
evitageN
smsinagro
oN
5
enoN
0A
1.1v'5
0A_11
40b_30tP
%15
%96
12
seY
%65
%65
%26
%26
evitageN
evitageN
smsinagro
oN
enoN
1
enoN
0A
1.1v'5
0A_90
10b_40tP
4
tneitaP
02
%95
%26
%26
%26
evitageN
evitageN
smsinagro
oN
2
enoN
0A
1.1v'5
0A_01
20b_40tP
61
%87
%28
%87
%28
evitageN
evitageN
smsinagro
oN
6
enoN
0A
1.1v'5
0A_81
30b_40tP
A/N
A/N
A/N
oN
%27
%27
%67
%67
evitageN
evitageN
smsinagro
oN
471
:sedosipe
2
21
devloseR
0A
1.1v'5
0A_21
10b_50tP
5
tneitaP
3A
htob
%34
%35
41
seY
%66
%46
%27
%96
evitageN
evitageN
smsinagro
oN
enoN
24
enoN
0A
1.1v'5
0A_31
10b_60tP
6
tneitaP
%74
%26
6
seY
%06
%86
%27
%57
evitageN
evitageN
smsinagro
oN
enoN
6
RCA
dliM
2A
2v'5
2A_24
10b_70tP
7
tneitaP
7
%07
%47
%27
%57
evitageN
evitageN
smsinagro
oN
33
2A
:edosipe
1
7
devloseR
0A
2v'5
0A_54
20b_70tP
21
%27
%67
%57
%87
evitageN
evitageN
smsinagro
oN
661
2A
:edosipe
1
21
devloseR
0A
2v'5
0A_94
30b_70tP
41
%86
%37
%57
%87
evitageN
eivtageN
smsinagro
oN
462
2A
:edosipe
1
41
devloseR
0A
2v'5
0A_15
40b_70tP
%97
%87
7
seY
%07
%77
%18
%18
evitageN
evitageN
evitageN
63
1
:sedosipe
4
01
dliM
2A
2v'5
2A_10F
10b_80tP
8
tneitaP
1A
3
,2A
1152 The Journal of Heart and Lung Transplantation, Vol 45, No 7, July 2026

Potter et al. Human Lung ACR and Fibrogenic Shift 1153
Figure 1 A) UMAP plot of integrated dataset (n=18 biopsies from 8 patients) with cell type annotations. B) Feature plot of key marker
genes in integrated dataset. C) Heatmap of lymphoid cell clusters from integrated single cell data, with top markers for each cluster.
we identified robust cell-level statistical signals. COL3A1+ TGF-βR1 and TGF-βR2 were also increased across multiple
cells showed significant enrichment in ACR (36.0%, Odds mesenchymal clusters along with key downstream effector
Ratio (OR) 3.0, 95% Confidence Interval (CI) 2.8–3.2) and SMAD3.23 Broad upregulation of THY1, which modulates
Resolved samples (44.4%, OR 4.4, 95% CI 3.8–5.2) com- myofibroblast lineage, across fibroblast subtypes and VSM cells
pared to Never (16.5%). p-S6RP+ cells, indicating mTOR (MaxFC 6.9, Alveolar Fibroblast Resolved), suggests state
pathway activation, also significantly increased in ACR transition within the fibrogenic compartment, accompanied by
(45.0%, OR 11.2, 95% CI 10.0–12.5) and Resolved (48.4%, upregulation of myofibroblast markers α-SMA (ACTA2) and
OR 13, 95% CI 7.6–22.1) compared to Never (7.9%). TAGLN27 (Figure 3A). Stratification by ACR grade confirmed
Double-positive COL3A1+/p-S6RP+ cells, representing consistent fibrogenic gene upregulation (median 1.6–1.8
activated collagen-matrix secreting cells with mTOR ac- log2FC) across conditions (Supplemental Figure 4A).
tivity, were elevated in ACR (17.5%, OR 4.9, 95% CI Gene signature scoring confirmed enrichment of myofi-
3.8–6.4) with Resolved showing higher levels (33.5%, OR broblast markers within fibroblast subtypes and VSM cells
10.8, 95% CI 7.2–16.2) relative to Never (4.3%). All in ACR, along with activation of key ECM remodeling
comparisons achieved adjusted p (P ) < 0.001, demon- pathways, including collagen biosynthesis, collagen cross-
adj
strating strong significance signals despite the modest linking, and ECM organization (Figure 3B,
sample sizes (Figure 2C/D, Table 3, Supplement B). Supplemental Figure 4B). Partial fibrogenic activation was
observed in epithelial and endothelial compartments, with
increased expression of several ECM genes within en-
Fibrogenic shift driven by mesenchymal state dothelial and epithelial (alveolar epithelial type 1 (AT1) and
transition basal) clusters, including COL4A1 and TNC, with myofi-
broblast marker TAGLN also increasing in AT1
Collagen-fibril gene expression was increased in both ACR and (Supplemental Figure 5A). However, analyzing cluster
Resolved in fibrogenic cells, including fibroblast subtypes and markers as gene signature scores, these compartments re-
vascular smooth muscle (VSM) cells, with upregulation of key tained expression of their canonical cluster markers without
ECM genes (TNC, FN1, VCAN, and LUM). RCN3, which full transdifferentiation to myofibroblast phenotypes in
drives persistent fibroblast activation through a TGF-β1-RCN3- ACR or Resolved (Supplemental Figure 5B).
TGF-βR1 feedback loop, showed upregulation in myofibro- We analyzed the subset of non-immune cells and iden-
blasts from ACR and Resolved (both 1.1 log2FC).25ASPN, an tified no significant changes in overall fibroblast proportion
extracellular protein that induces myofibroblast differentiation, (including all subtypes) (Never: 5.6%, ACR: 8.9%,
was increased in adventitial fibroblasts, VSM and myofibro- Resolved: 6.1%, ANOVA p = 0.55, FDR = 0.93).
blasts in both ACR and Resolved (MaxFC 3.4, adventitial fi- Examining fibroblast subtypes, ACR and Resolved showed
broblast Resolved).26 Expression of TGF-β1 and its receptors decreased proportions of alveolar (ACR: 55.3%, Resolved:

1154 The Journal of Heart and Lung Transplantation, Vol 45, No 7, July 2026
Figure 2 A) Enrichr plot of most significant pathways from the shared upregulated genes (≥8 cell clusters) in ACR (n=5 biopsies from 4
patients) and Resolved (n=5 biopsies from 3 patients) compared to Never (n=8 biopsies from 3 patients), using MSigDB Hallmark Enrichr
library. B) Stacked violin plot showing differential gene expression for select TGF-β/mTOR pathway genes in lung compartments (from
integrated dataset, n=18 biopsies). C) Representative immunofluorescence images (20x) from Never (06_A0), ACR (42_A2), and Resolved
(05_A0) samples showing DAPI (blue, nuclei), COL3A1 (green), p-S6RP (red), and merged channels. Images exported from QuPath. D)
Percentage of cells positive for COL3A1 (TGF-β-induced collagen), p-S6RP (mTOR activation marker), and double-positive cells
(COL3A1+/p-S6RP+) in Never (n=3), ACR (n=4), and Resolved (n=3) samples. Box plots show individual biopsy data points with sig-
nificance determined by mixed-effects logistic regression with Benjamini-Hochberg correction ***p < 0.001 vs Never).
Table 3 Mixed-effects Logistic Regression Results Comparing ACR or Resolved to Never (reference). P-values Adjusted Using
Benjamini-Hochberg Method. Significance: * p < 0.05, ** p < 0.01, *** p < 0.001
Marker Comparison Odds Ratio (95% CI) P-Value Adjusted P-Value Significance
COL3A1 ACR vs Never 3.02 (2.81-3.24) < 0.001 < 0.001 ***
COL3A1 Resolved vs Never 4.40 (3.75-5.16) < 0.001 < 0.001 ***
PS6 ACR vs Never 11.20 (10.03-12.50) < 0.001 < 0.001 ***
PS6 Resolved vs Never 12.98 (7.62-22.12) < 0.001 < 0.001 ***
Combined ACR vs Never 4.94 (3.80-6.42) < 0.001 < 0.001 ***
Combined Resolved vs Never 10.80 (7.19-16.22) < 0.001 < 0.001 ***
48.4% vs Never: 62.9%) and increased adventitial (ACR: Compositional shift to cytotoxic T and dendritic
28.3%, Resolved: 27.5% vs Never: 17.6%) (Supplemental APCs in ACR
Figure 6A-C). Trajectory analysis showed distinct fibro-
genic cell partitions that excluded epithelial and endothelial Differential cell composition analysis revealed significantly
cells but included pericytes, indicating potential pericyte-to- reduced NK cells in both ACR and Resolved compared to
myofibroblast differentiation (Supplemental Table 5). Never, with significant increase in T effector (Teff) cells

Potter et al. Human Lung ACR and Fibrogenic Shift 1155
Figure 3 A) Stacked violin plot illustrating differential expression of ECM, TGF-β signaling, and myofibroblast marker genes in
mesenchymal cells in ACR (n=4 patients) and Resolved (n=3 patients) compared to Never (n=3 patients). B) Gene signature heatmap with
scaled scores (UCell, SCPubr) of cluster markers (top 20 markers for each cell type) and select fibrogenic gene sets (Enrichr) in fibrogenic
cells across conditions.
and decreases in macrophages and monocytes in ACR. IF analysis of phospho-STAT1 (pSTAT1-Y701) using
Additional trends included increased proportions of T re- mixed-effects logistic regression (n=4 ACR, n=3 Never) re-
sident memory (Trm), T exhausted (Texhaust), T follicular vealed decreased pSTAT1+ cells specifically within VE-
helper (Tfh), T regulatory (Treg), plasma cells, and den- Cadherin+ cells (5.1% vs 10.6%, OR 0.49, 95% CI 0.28–0.87,
dritic cell clusters in ACR (Figure 4A-D). P = 0.02), which may reflect feedback inhibition by SOCS3,
adj
To validate these findings, we analyzed historical gene which was upregulated in ACR (MaxFC 4.8, proliferating
array data comparing ACR (n=44) to No ACR biopsies basal). However, VE-cadherin expression was reduced in ACR
(n=70).22 Using cell-type specific markers from our single (14.1% vs 30.2%, OR 0.25, 95% CI 0.09–0.74, P = 0.02),
adj
cell dataset to generate composite scores, we confirmed consistent with IFN-γ-mediated endothelial injury and adherens
significantly elevated Teff, Trm, Texhaust, Tfh, Treg, B junction disruption. Notably, Patient 1 showed progressive VE-
cell, plasma cell, and dendritic cell signatures in ACR cadherin loss from 29.6% to 2.2% over 35 days (93% reduc-
biopsies, with nonsignificant reductions in NK cells and tion), despite histological improvement from A4 to A3 ACR,
macrophages. These findings confirm a compositional shift and subsequently died due to refractory ACR (Supplement C,
toward cytotoxic and memory T lymphocytes and dendritic Supplemental Figure 8A-B).
APCs during ACR (Figure 4E).
IFN-γ-mediated signaling and inflammation in ACR Discussion
Cell signaling analysis identified significantly increased IFN-γ signaling and endothelial cell injury
IFN-II pathway activity in ACR (Figure 5A/B). IFN-γ
signaling was upregulated in Trm and Teff cells, with key ACR is characterized by elevated IFN-II signaling, which
downstream receivers including monocytes, macrophages, persisted in Resolved samples. IFN-II facilitates immune
dendritic cells, and lung structural cells—particularly en- invasion but may also protect against early microvascular
dothelial and basal (Figure 5C). Key IFN-II pathway gene damage.28 TNF signaling, also increased in ACR and Re-
STAT1 (MaxFC 3.6, differentiating basal) and downstream solved, may act synergistically with IFN-γ to drive in-
HLA class II genes, including HLA-DQB1 (MaxFC 6.8, flammation through gene expression and cell death
proximal basal) were elevated. Gene signature scoring induction.29 Endothelial cells, which serve as the immune
confirmed endothelial cells had the highest IFN-γ response entryway into allografts and actively recruit lymphocytes,
among resident lung cells in ACR (Supplemental Figure had the highest IFN-γ response in ACR.30 HLA-II expres-
7A-C). scATAC analysis of a biopsy with A3 ACR sion increased in several structural lung cells, consistent
(Pt01_b02) confirmed enriched STAT1/3 accessibility in with IFN-γ-stimulated Jak/Stat activation, potentially pre-
endothelial and basal clusters (Figure 5D). Additional in- senting alloantigen to helper T cells.28Immunofluorescence
flammatory pathways were dysregulated in ACR, including revealed reduced VE-cadherin expression in ACR, con-
VEGF, TNF, and TGF-β, with elevated signaling persisting sistent with IFN-γ-mediated disruption of endothelial ad-
in Resolved (Figure 5A/B). herens junctions.31

1156 The Journal of Heart and Lung Transplantation, Vol 45, No 7, July 2026
Figure 4 A-B) Stacked bar charts illustrate differential cell composition of A) lymphoid B) myeloid cell types, by condition, for
integrated dataset (n=18 biopsies). C) Stacked bar chart illustrating different contribution of cell compartments, by condition, for integrated
dataset. D) Box and whisker plot (scCODA) show distribution, based on the natural log of counts (y-axis) in immune cell clusters by
condition; significant change (up or down) relative to Never indicated with asterisk. E) Violin/box plots showing cell-type specific z-score-
based composite scores in ACR (n=44) versus No ACR (n=77) biopsies (Microarray data), using marker genes for each cell type. Individual
biopsies are shown as points: *p < 0.05, **p < 0.01, ***p < 0.001.

Potter et al. Human Lung ACR and Fibrogenic Shift 1157
Figure 5 A-B) Stacked bar charts (CellChat) illustrate relative information flow comparing Never (n=8 biopsies from 3 patients) versus
A) ACR (n=5 biopsies from 4 patients) or B) by ACR condition (high grade ACR: n=3 biopsies from 2 patients, mild ACR: n=2 biopsies
from 2 patients and Resolved: n=5 biopsies from 3 patients compared to Never: n=8 biopsies from 3 patients), for select signaling pathways.
C) Chord diagram (CellChat) of IFN-II pathway in Never (n=3 patients) and ACR (n=4 patients) conditions. D) Heatmap of transcription
factor motif accessibility across cell clusters from single-cell ATAC-seq data. Rows show top marker motifs per cluster (n=3, ranked by p-
value from FindAllMarkers). Values represent row-scaled chromVAR deviation z-scores (Patient 01, biopsy 02, A3 ACR).
Compositional shift in ACR NK cells were persistently reduced in lymphoid clusters,
which could impair immune surveillance and tolerance.33
Accompanying these signaling changes, we identified sig- This finding in our predominantly pediatric cohort is no-
nificant shifts in immune cell composition. Using scCODA, table given that pediatric NK cells exhibit greater pheno-
a Bayesian framework that accounts for negative correla- typic diversity and distinct receptor expression compared to
tion bias in single cell data,21 we identified changes in adults,34 though whether this developmental variation in-
myeloid composition, with reduced macrophages and fluences NK cell dynamics during rejection remains un-
monocytes, and increased mast and dendritic cells, aligning clear. Halloran et al. did not observe similar NK reduction
with studies linking mast cells to ACR severity.32 in an entirely adult study cohort,22suggesting potential age-

1158   The Journal of Heart and Lung Transplantation, Vol 45, No 7, July 2026
related differences in NK cells in response to allograft in- transition of mesenchymal cells, rather than transdiffer-
jury. TGF-β and SMAD3 repress NK cell differentiation,35
|     |     |     |     |     |     |     | entiation  | from  | endothelial  | or  | epithelial  | cells,  | which  is  |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ----- | ------------ | --- | ----------- | ------- | ---------- |
suggesting  an  alternative  mechanistic  link  between  the  consistent with previous lineage tracing and imaging stu-
persistent TGF-β signaling observed in our study and NK  dies.41,42The evidence supporting this includes 1) increased
cell depletion. myofibroblast marker expression within the fibrogenic cells
These immune infiltrates were predominantly recipient-  (fibroblast subtypes, VSM); 2) stable fibroblast proportions
derived (0–1.94% donor-derived lymphoid cells), consistent  within the non-immune fraction; 3) trajectory analysis in-
with gradual replacement of donor-derived memory T cells  dicating separation of fibrogenic mesenchymal cells from
and increasing importance of indirect allorecognition.36,37
|     |     |     |     |     |     |     | epithelial  | and  | endothelial  | partitions.  |     | While  | some  en- |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ---- | ------------ | ------------ | --- | ------ | --------- |
dothelial and epithelial clusters showed increased fibro-
genic gene expression (COL4A1, TNC), their cluster marker
Persistent fibrogenic activation links ACR to CLAD
|     |     |     |     |     |     |     | gene  signatures  |     | remained  | stable,  | suggesting  |     | incomplete  |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | --------- | -------- | ----------- | --- | ----------- |
transdifferentiation.
While these inflammatory and compositional changes in the
current study characterize ACR, our most striking finding
was the persistence of fibrogenic programs after histolo-
Therapeutic implications: targeting mTOR and
gical resolution. We identified a sustained activation of
TGF-β
TGF-β and PI3K/AKT/mTOR pathway in lung allografts
after clinical ACR resolution. TGF-β1 levels are elevated in
|     |     |     |     |     |     |     | Collectively,  | our  | findings,  | including  |     | persistent  | mTOR  |
| --- | --- | --- | --- | --- | --- | --- | -------------- | ---- | ---------- | ---------- | --- | ----------- | ----- |
bronchoalveolar lavage (BAL) fluid of patients with re-
|     |     |     |     |     |     |     | pathway  | activation  | and  | fibrotic  | gene  | expression  | despite  |
| --- | --- | --- | --- | --- | --- | --- | -------- | ----------- | ---- | --------- | ----- | ----------- | -------- |
strictive allograft syndrome (RAS), and TGF-β1 can induce
histological ACR resolution, indicate a shift toward meta-
myofibroblast differentiation, contributing to fibrosis.38The
bolically active, myofibroblast-like fibroblasts and VSM
persistent upregulation of TGF-β1, its receptors (TGFBR1/
that is not addressed by standard corticosteroid therapy.
TGFBR2), and downstream effector SMAD3 aligns with
TGF-β’s  These findings suggest that standard surveillance broncho-
|     | established  | role  | as  a  "master  | regulator"  |     | of  fi- |     |     |     |     |     |     |     |
| --- | ------------ | ----- | --------------- | ----------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
scopy with histopathology may not adequately assess on-
| brosis.39,40 | Immunofluorescence confirmed sustained upre- |     |     |     |     |     |     |     |     |     |     |     |     |
| ------------ | -------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
going fibrosis and risk of CLAD, highlighting the need for
| gulation  | of  | p-S6RP  (mTOR  | activation  |     | marker)  | and  |            |             |      |        |               |               |     |
| --------- | --- | -------------- | ----------- | --- | -------- | ---- | ---------- | ----------- | ---- | ------ | ------------- | ------------- | --- |
|           |     |                |             |     |          |      | molecular  | biomarkers  | and  | early  | antifibrotic  | intervention  |     |
COL3A1, with increased double-positive cells in Resolved
strategies. Elevated TGF-β1 levels in BAL during primary
compared to ACR.
graft dysfunction have been associated with increased risk
Previously, TGF-Β1 was found to activate mTORC1 in
|     |     |     |     |     |     |     | of CLAD,43 | and our findings of persistent TGF-β pathway  |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --------------------------------------------- | --- | --- | --- | --- | --- |
fibroblasts, but not epithelial cells, via a PI3K-Akt-TSC2-
activation post-ACR suggest that BAL TGF-β1 or tissue-
| dependent pathway.23 |     | This finding may explain why the  |     |     |     |     |     |     |     |     |     |     |     |
| -------------------- | --- | --------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
level markers such as p-S6RP may serve as indicators of
fibrotic response was concentrated in stromal cells in our
fibrogenic risk, warranting further investigation.
analysis. Furthermore, mTORC1 activation, in coordination
Considering potential therapeutic options that target fi-
with SMAD3, is critical for key fibroblast functions, reg-
|     |     |     |     |     |     |     | brogenesis,  | mTOR  | inhibitors  |     | function  | as  | both  im- |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ----- | ----------- | --- | --------- | --- | --------- |
ulating anchorage-independent growth, and is necessary for
munotherapy and antifibrotic, depending on context and
TGF-β to stimulate collagen protein production at a trans-
disease treated. Clinical trials of first-generation mTOR
| lational  | level,  | likely  through  | its  | substrate  | Eukaryotic  |     |     |     |     |     |     |     |     |
| --------- | ------- | ---------------- | ---- | ---------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
inhibitors (everolimus, sirolimus) in LTx recipients showed
Translation Initiation Factor 4E Binding Protein 1 (4E-
BP1).13,23 variable outcomes and high discontinuation rates due to
RCN3, upregulated in myofibroblasts in ACR
|     |     |     |     |     |     |     | adverse effects.44,45 |     | Registry data demonstrated that sir- |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------------------- | --- | ------------------------------------ | --- | --- | --- | --- |
and Resolved, creates sustained TGF-β sensitivity through a
olimus paired with tacrolimus reduced CLAD incidence
TGF-β1-RCN3-TGFBR1 feedback loop that amplifies re-
ceptor transcription.25 and improved survival compared to mycophenolate-based
ASPN, increased in adventitial fi-
|             |      |              |                  |     |       |        | regimens.46 | These benefits may stem from antifibrotic ra- |     |     |             |            |     |
| ----------- | ---- | ------------ | ---------------- | --- | ----- | ------ | ----------- | --------------------------------------------- | --- | --- | ----------- | ---------- | --- |
| broblasts,  | VSM  | cells,  and  | myofibroblasts,  |     | acts  | post-  |             |                                               |     |     |             |            |     |
|             |      |              |                  |     |       |        | ther  than  | immunosuppressive                             |     |     | properties  | depending  | on  |
translationally, by stabilizing TGFBR1 receptor at the pro-
whether ACR was the primary factor for CLAD onset in
tein level, further potentiating the fibrotic feedback loop.26
these previous study cohorts. TGF-β1 activates mTORC1
Elevated THY1 expression within mesenchymal cells likely
|     |     |     |     |     |     |     | via  PI3K-Akt-TSC2  |     | in  | fibroblasts,  |     | and  mTORC1,  | co- |
| --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | --- | ------------- | --- | ------------- | --- |
reflects a transition to myofibroblast phenotype, as previous
ordinating with SMAD3, drives collagen production through
research reported that only THY1+ fibroblasts can develop
4E-BP1.13
into myofibroblasts.27 First-generation mTOR inhibitors incompletely
inhibit this 4E-BP1 axis, potentially explaining clinical trial
|     |     |     |     |     |     |     | limitations.13,47 |     | In contrast, next-generation ATP-competi- |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | ----------------------------------------- | --- | --- | --- | --- |
Mesenchymal state transitions drive myofibroblast
tive mTOR inhibitors are highly effective at blocking col-
formation lagen synthesis in pulmonary fibrotic-derived fibroblasts
and live lung tissue slices.13,48
Although TGF-β drives mesenchymal transition to myofi- Nintedanib, a multi-tyrosine kinase inhibitor approved
broblasts, the contribution of epithelial and endothelial cells  for idiopathic pulmonary fibrosis, targets pathways identi-
via EMT/EndoMT remains controversial.39,40
|     |     |     |     |     | Our study  |     | fied in our study by inhibiting TGF-β1-induced myofibro- |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | ---------- | --- | -------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
results indicate that the fibrogenic remodeling observed in  blast differentiation and downstream SMAD3 activation and
signaling.49
ACR and Resolved is primarily driven by a phenotypic state  p38  MAPK  In  a  mouse  model  of  CLAD,

Potter et al. Human Lung ACR and Fibrogenic Shift 1159
nintedanib significantly reduced fibrotic occlusion in tra- Conflict of Interest
cheal allografts.50 Our findings suggest the post-ACR
period, before irreversible fibrotic remodeling, may re- The authors declare no conflicts of interest.
present a favorable therapeutic window. Prospective studies
are needed to further investigate whether antifibrotic
therapy initiated after ACR resolution can prevent or delay Declaration of Generative AI and AI-assisted
onset of CLAD.. technologies in the writing process
Claude (Anthropic) was used to refine writing. After using
Limitations
this tool, the authors reviewed and edited the content as
needed and assume full responsibility for the content of the
Sample size of our study was constrained by the low frequency
publication.
of ACR in our predominantly pediatric LTx recipient cohort.
We also integrated data with 3’ and 5’ chemistry from 10X
Genomics, employing batch correction for chemistry differ-
Data availability
ences. Clinical heterogeneity of our study cohort may influence
our molecular findings; of the 5 patients who developed CLAD,
Single-cell RNA and ATAC sequencing data are available
3 previously had ACR, and there were temporal differences in
at GEO accession GSE274199 (https://www.ncbi.nlm.nih.
time post-LTx between conditions. Induction immunosuppres-
gov/geo/query/acc.cgi?acc=GSE274199). Code is available
sion varied between patients, with 2 Never patients receiving
at https://github.com/hayes-potter-lab/fibro-changes-acr.
antithymocyte globulin, with biopsy sampling within 1–6
months post-LTx; we cannot exclude that cytolytic induction
therapy influenced Never transcriptomic profiles..
Acknowledgments
Conclusion The authors thank the patients for their participation in the
study. We would also like to thank the Cincinnati Children’s
This study reveals persistent TGF-β and mTOR-driven fi- Hospital Medical Center Single Cell Genomics Facility
Children’s (RRID: SCR_022653), Genomics Sequencing
brogenic activation following histologic ACR resolution,
Facility (RRID:SCR_022630), and Integrated Pathology
suggesting a potential molecular mechanism linking ACR
Research Facility (RRID: SCR_022637). The authors thank
to CLAD that warrants further investigation. These findings
Kathryn Wikenheiser-Brokamp, MD, PhD for clinical patho-
provide rationale for exploring early anti-fibrotic interven-
logic review of the lung transplant biopsies as well as thank
tion post-ACR and identify candidate molecular biomarkers
Pathologists’ Assistants Cheryl Talbott, MHS CT(ASCP)CM,
that may inform future risk stratification and treatment
PACM and Amy Fortener, MS PA(ASCP)CM for assessment
monitoring studies.
for sample adequacy and processing of the lung biopsies for
single cell analysis, and Drew Smith, Lori Miller and Betsy A.
Funding source DiPasquale, HT, ASCP for performing IF staining and imaging.
We would also like to acknowledge the assistance of Kelly
Heart Institute, Cincinnati Children’s Hospital Medical Rangel, MS and Shawn Smith, MS in experimental design,
Center, Cincinnati, OH. processing single cell samples and preparing libraries for se-
quencing.
Author contribution
Appendix A. Supporting information
A.S.P.: Conception/design, performed experiments, bioinfor-
Supplemental data associated with this article can be found
matic analysis/interpretation, drafted manuscript. N.S.S.:
in the online version at doi:10.1016/j.healun.2026.02.1666.
Performed experiments, bioinformatic interpretation, edited
manuscript. Y.G.: Bioinformatic interpretation, edited manu-
script. K.N.P.: Bioinformatic interpretation, edited manuscript.
References
M.R.Q.: Bioinformatic interpretation, edited manuscript. K.H.:
Provided data for validation analyses, edited manuscript.
1. Todd JL, Neely ML, Kopetskie H, et al. Risk factors for acute rejection
P.F.H.: Provided data for validation analyses, edited manu- in the first year after lung transplant. a multicenter study. Am J Respir
script. C.W.: Performed experiments, edited manuscript. A.A.: Crit Care Med 2020;202(4):576-85. https://doi.org/10.1164/rccm.
Bioinformatic interpretation, edited manuscript. D.L.S.M.: 201910-1915OC.
2. Burton CM, Iversen M, Carlsen J, et al. Acute cellular rejection is a
Bioinformatic interpretation, edited manuscript. D.H.:
risk factor for bronchiolitis obliterans syndrome independent of post-
Conception/design, performed experiments, bioinformatic in-
transplant baseline FEV1. J Heart Lung Transpl 2009;28(9):888-93.
terpretation, drafted manuscript. https://doi.org/10.1016/j.healun.2009.04.022.

1160 The Journal of Heart and Lung Transplantation, Vol 45, No 7, July 2026
3. Hopkins PM, Aboyoun CL, Chhajed PN, et al. Association of minimal 22. Halloran KM, Parkes MD, Chang J, et al. Molecular assessment of
rejection in lung transplant recipients with obliterative bronchiolitis. rejection and injury in lung transplant biopsies. J Heart Lung Transpl
Am J Respir Crit Care Med 2004;170(9):1022-6. https://doi.org/10. 2019;38(5):504-13. https://doi.org/10.1016/j.healun.2019.01.1317.
1164/rccm.200302-165OC. 23. Rahimi RA, Andrianifahanana M, Wilkes MC, et al. Distinct roles for
4. Khalifah AP, Hachem RR, Chakinala MM, et al. Minimal acute re- mammalian target of rapamycin complexes in the fibroblast response
jection after lung transplantation: a risk for bronchiolitis obliterans to transforming growth factor-b. eta Cancer Res 2009;69(1):84-93.
syndrome. Am J Transpl 2005;5(8):2022-30. https://doi.org/10.1111/j. https://doi.org/10.1158/0008-5472.CAN-08-2146.
1600-6143.2005.00953.x. 24. Giarratana AO, Prendergast CM, Salvatore MM, Capaccione KM.
5. Glanville AR, Aboyoun CL, Havryk A, Plit M, Rainer S, Malouf MA. TGF-β signaling: critical nexus of fibrogenesis and cancer. J Transl
Severity of lymphocytic bronchiolitis predicts long-term outcome after Med 2024;22:594. https://doi.org/10.1186/s12967-024-05411-4.
lung transplantation. Am J Respir Crit Care Med 25. Wu M, Wang Z, Shi X, et al. TGFβ1-RCN3-TGFBR1 loop facilitates
2008;177(9):1033-40. https://doi.org/10.1164/rccm.200706-951OC. pulmonary fibrosis by orchestrating fibroblast activation. Respir Res
6. Perch M, Hayes D, Cherikh WS, et al. The International Thoracic 2023;24(1):222. https://doi.org/10.1186/s12931-023-02533-z.
Organ Transplant Registry of the International Society for Heart and 26. Huang S, Lai X, Yang L, et al. Asporin promotes TGF-β-induced lung
Lung Transplantation: Thirty-ninth adult lung transplantation report- myofibroblast differentiation by facilitating Rab11-dependent re-
2022; focus on lung transplant recipients with chronic obstructive cycling of TβRI. Am J Respir Cell Mol Biol 2022;66(2):158-70.
pulmonary disease. J Heart Lung Transpl 2022;41(10):1335-47. https://doi.org/10.1165/rcmb.2021-0257OC.
https://doi.org/10.1016/j.healun.2022.08.007. 27. Koumas L, Smith TJ, Feldon S, Blumberg N, Phipps RP. Thy-1 ex-
7. Hayes D, Cherikh WS, Harhay MO, et al. The International Thoracic pression in human fibroblast subsets defines myofibroblastic or lipo-
Organ Transplant Registry of the International Society for Heart and Lung fibroblastic phenotypes. Am J Pathol 2003;163(4):1291-300. https://
Transplantation: Twenty-fifth pediatric lung transplantation report - 2022; doi.org/10.1016/S0002-9440(10)63488-8.
focus on pulmonary vascular diseases. J Heart Lung Transpl 28. Halloran PF, Miller LW, Urmson J, et al. IFN-γ alters the pathology of
2022;41(10):1348-56. https://doi.org/10.1016/j.healun.2022.07.020. graft rejection: protection from early necrosis1. J Immunol
8. Lund LH, Edwards LB, Kucheryavaya AY, et al. The Registry of the 2001;166(12):7072-81. https://doi.org/10.4049/jimmunol.166.12.7072.
International Society for Heart and Lung Transplantation: Thirty- 29. van Loo G, Bertrand MJM. Death by TNF: a road to inflammation.
second Official Adult Heart Transplantation Report–2015; Focus Nat Rev Immunol 2023;23(5):289-303. https://doi.org/10.1038/
Theme: early graft failure. J Heart Lung Transpl 2015;34(10):1244-54. s41577-022-00792-3.
https://doi.org/10.1016/j.healun.2015.08.003. 30. Cross AR, Glotz D, Mooney N. The role of the endothelium during
9. Pavlisko EN, Neely ML, Kopetskie H, et al. Prognostic implications of antibody-mediated rejection: from victim to accomplice. Front
and clinical risk factors for acute lung injury and organizing pneu- Immunol 2018;9. https://doi.org/10.3389/fimmu.2018.00106.
monia after lung transplantation: data from a multicenter prospective 31. Langer V, Vivi E, Regensburger D, et al. IFN-γ drives inflammatory
cohort study. Am J Transpl 2022;22(12):3002-11. https://doi.org/10. bowel disease pathogenesis through VE-cadherin-directed vascular
1111/ajt.17183. barrier disruption. J Clin Invest 2019;129(11):4691-707. https://doi.
10. Valapour M, Lehr CJ, Schladt DP, et al. OPTN/SRTR 2022 Annual org/10.1172/JCI124884.
Data Report: lung. Am J Transpl 2024;24(2S1):S394-456. https://doi. 32. Benson HL, Suzuki H, Lott J, et al. Donor lung derived myeloid and
org/10.1016/j.ajt.2024.01.017. plasmacytoid dendritic cells differentially regulate T cell proliferation
11. Silva T de, Voisey J, Hopkins P, Apte S, Chambers D, O’Sullivan B. and cytokine production. Respir Res 2012;13(1):25. https://doi.org/10.
Markers of rejection of A lung allograft: state of the art. Biomark Med 1186/1465-9921-13-25.
2022;16(6):483-98. https://doi.org/10.2217/bmm-2021-1013. 33. Jungraithmayr W, Codarri L, Bouchaud G, et al. Cytokine complex-ex-
12. Stewart S, Fishbein MC, Snell GI, et al. Revision of the 1996 working panded natural killer cells improve allogeneic lung transplant function via
formulation for the standardization of nomenclature in the diagnosis of depletion of donor dendritic cells. Am J Respir Crit Care Med
lung rejection. J Heart Lung Transpl 2007;26(12):1229-42. https://doi. 2013;187(12):1349-59. https://doi.org/10.1164/rccm.201209-1749OC.
org/10.1016/j.healun.2007.10.017. 34. Mahapatra S, Mace EM, Minard CG, et al. High-resolution pheno-
13. Platé M, Guillotin D, Chambers RC. The promise of mTOR as a ther- typing identifies NK cell subsets that distinguish healthy children from
apeutic target pathway in idiopathic pulmonary fibrosis. Eur Respir Rev adults. PLoS One 2017;12(8):e0181134. https://doi.org/10.1371/
2020;29(157). https://doi.org/10.1183/16000617.0269-2020. journal.pone.0181134.
14. Fernandez IE, Eickelberg O. The Impact of TGF-β on lung fibrosis. 35. Tang PMK, Zhou S, Meng XM, et al. Smad3 promotes cancer pro-
Proc Am Thorac Soc 2012;9(3):111-6. https://doi.org/10.1513/pats. gression by inhibiting E4BP4-mediated NK cell development. Nat
201203-023AW. Commun 2017;8:14677. https://doi.org/10.1038/ncomms14677.
15. Chen F, Lyu L, Xing C, et al. The pivotal role of TGF-β/Smad 36. de Leur K, Dieterich M, Hesselink DA, et al. Characterization of
pathway in fibrosis pathogenesis and treatment. Front Oncol 2025;15. donor and recipient CD8+ tissue-resident memory T cells in transplant
https://doi.org/10.3389/fonc.2025.1649179. nephrectomies. Sci Rep 2019;9(1):5984. https://doi.org/10.1038/
16. Hidalgo LG, Halloran PF. Role of IFN-gamma in allograft rejection. s41598-019-42401-9.
Crit Rev Immunol 2002;22(4):317-49. 37. Ingulli E. Mechanism of cellular rejection in transplantation. Pedia Nephrol
17. Guo M, Yu JJ, Perl AK, et al. Single-cell transcriptomic analysis 2010;25(1):61-74. https://doi.org/10.1007/s00467-008-1020-x.
identifies a unique pulmonary lymphangioleiomyomatosis cell. Am J 38. Sacreas A, von der Thüsen JH, van den Bosch TPP, et al. The pleural
Respir Crit Care Med 2020;202(10):1373-87. https://doi.org/10.1164/ mesothelium and transforming growth factor-β1 pathways in restrictive
rccm.201912-2445OC. allograft syndrome: A pre-clinical investigation. J Heart Lung Transpl
18. THE TABULA SAPIENS CONSORTIUM. The Tabula Sapiens: a 2019;38(5):570-9. https://doi.org/10.1016/j.healun.2019.02.001.
multiple-organ, single-cell transcriptomic atlas of humans. Science 39. Frangogiannis NG. Transforming growth factor–β in tissue fibrosis. J Exp
2022;376(6594):eabl4896. https://doi.org/10.1126/science.abl4896. Med 2020;217(3):e20190103. https://doi.org/10.1084/jem.20190103.
19. Travaglini KJ, Nabhan AN, Penland L, et al. A molecular cell atlas of 40. Biernacka A, Dobaczewski M, Frangogiannis NG. TGF-β signaling in
the human lung from single-cell RNA sequencing. Nature fibrosis. Growth Factors 2011;29(5):196-202. https://doi.org/10.3109/
2020;587(7835):7835. https://doi.org/10.1038/s41586-020-2922-4. 08977194.2011.595714.
20. Domínguez Conde C, Xu C, Jarvis LB, et al. Cross-tissue immune cell 41. Rock JR, Barkauskas CE, Cronce MJ, et al. Multiple stromal popu-
analysis reveals tissue-specific features in humans. Science lations contribute to pulmonary fibrosis without evidence for epithelial
2022;376(6594):eabl5197. https://doi.org/10.1126/science.abl5197. to mesenchymal transition. Proc Natl Acad Sci USA
21. Büttner M, Ostner J, Müller CL, Theis FJ, Schubert B. scCODA is a 2011;108(52):E1475-83. https://doi.org/10.1073/pnas.1117988108.
Bayesian model for compositional single-cell data analysis. Nat Commun 42. Yamada M, Kuwano K, Maeyama T, et al. Dual-im-
2021;12(1):6876. https://doi.org/10.1038/s41467-021-27150-6. munohistochemistry provides little evidence for epithelial-

Potter et al. Human Lung ACR and Fibrogenic Shift 1161
mesenchymal transition in pulmonary fibrosis. Histochem Cell Biol transplant recipients. Ann Thorac Surg 2014;97(1):268-74. https://doi.
2008;129(4):453-62. https://doi.org/10.1007/s00418-008-0388-9. org/10.1016/j.athoracsur.2013.07.072.
43. DerHovanessian A, Weigt SS, Palchevskiy V, et al. The role of TGF-β 47. O’Leary EM, Tian Y, Nigdelioglu R, et al. TGF-β promotes metabolic
in the association between primary graft dysfunction and bronchiolitis reprogramming in lung fibroblasts via mTORC1-dependent ATF4
obliterans syndrome. Am J Transpl 2016;16(2):640-9. https://doi.org/ activation. Am J Respir Cell Mol Biol 2020;63(5):601-12. https://doi.
10.1111/ajt.13475. org/10.1165/rcmb.2020-0143OC.
44. Glanville AR, Aboyoun C, Klepetko W, et al. Three-year results of an 48. Mercer PF, Woodcock HV, Eley JD, et al. Exploration of a potent PI3
investigator-driven multicenter, international, randomized open-label de kinase/mTOR inhibitor as a novel anti-fibrotic agent in IPF. Thorax
novo trial to prevent BOS after lung transplantation. J Heart Lung Transpl 2016;71(8):701-11. https://doi.org/10.1136/thoraxjnl-2015-207429.
2015;34(1):16-25. https://doi.org/10.1016/j.healun.2014.06.001. 49. Rangarajan S, Kurundkar A, Kurundkar D, et al. Novel mechanisms
45. Strueber M, Warnecke G, Fuge J, et al. Everolimus versus myco- for the antifibrotic action of nintedanib. Am J Respir Cell Mol Biol
phenolate mofetil de novo after lung transplantation: a prospective, 2016;54(1):51-9. https://doi.org/10.1165/rcmb.2014-0445OC.
randomized, open-label trial. Am J Transpl 2016;16(11):3171-80. 50. Oliver J, Martinu T, Tikkanen J, et al. Nintedanib as an anti-fibrotic
https://doi.org/10.1111/ajt.13835. therapy in a mouse model of chronic lung allograft dysfunction. J
46. Sacher VY, Fertel D, Srivastava K, et al. Effects of prophylactic use of Heart Lung Transplant 2022;41(4):S84. https://doi.org/10.1016/j.
sirolimus on bronchiolitis obliterans syndrome development in lung healun.2022.01.193.