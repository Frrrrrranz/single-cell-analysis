Article
A molecular single-cell lung atlas of lethal
COVID-19
https://doi.org/10.1038/s41586-021-03569-1 Johannes C. Melms1,2,33, Jana Biermann1,2,33, Huachao Huang3,4,5,33, Yiping Wang1,2,33,
Ajay Nair5,33, Somnath Tagore6,33, Igor Katsyv7,33, André F. Rendeiro8,9,33, Amit Dipak Amin1,2,33,
Received: 16 November 2020
Denis Schapiro10,11, Chris J. Frangieh11,12, Adrienne M. Luoma13, Aveline Filliol5,
Accepted: 19 April 2021 Yinshan Fang3,4,5, Hiranmayi Ravichandran9,14,15, Mariano G. Clausi16, George A. Alba17,
Meri Rogava1,2, Sean W. Chen1,2, Patricia Ho1,2, Daniel T. Montoro18,19, Adam E. Kornberg2,
Published online: 29 April 2021
Arnold S. Han2, Mathieu F. Bakhoum20, Niroshana Anandasabapathy9,21,22,
Check for updates Mayte Suárez-Fariñas23,24, Samuel F. Bakhoum25,26, Yaron Bram27, Alain Borczuk28,29,
Xinzheng V. Guo16, Jay H. Lefkowitch7, Charles Marboe7, Stephen M. Lagana7,
Armando Del Portillo7, Emily J. Tsai5, Emmanuel Zorn2, Glen S. Markowitz7,
Robert F. Schwabe5,30, Robert E. Schwartz27,34, Olivier Elemento8,9,15,34, Anjali Saqi7,34,
Hanina Hibshoosh7,34, Jianwen Que3,4,5,31,34 ✉ & Benjamin Izar1,2,31,32,34 ✉
Respiratory failure is the leading cause of death in patients with severe SARS-CoV-2
infection1,2, but the host response at the lung tissue level is poorly understood. Here
we performed single-nucleus RNA sequencing of about 116,000 nuclei from the lungs
of nineteen individuals who died of COVID-19 and underwent rapid autopsy and seven
control individuals. Integrated analyses identified substantial alterations in cellular
composition, transcriptional cell states, and cell-to-cell interactions, thereby
providing insight into the biology of lethal COVID-19. The lungs from individuals with
COVID-19 were highly inflamed, with dense infiltration of aberrantly activated
monocyte-derived macrophages and alveolar macrophages, but had impaired T cell
responses. Monocyte/macrophage-derived interleukin-1β and epithelial cell-derived
interleukin-6 were unique features of SARS-CoV-2 infection compared to other viral
and bacterial causes of pneumonia. Alveolar type 2 cells adopted an inflammation-
associated transient progenitor cell state and failed to undergo full transition into
alveolar type 1 cells, resulting in impaired lung regeneration. Furthermore, we
identified expansion of recently described CTHRC1+ pathological fibroblasts3
contributing to rapidly ensuing pulmonary fibrosis in COVID-19. Inference of protein
activity and ligand–receptor interactions identified putative drug targets to disrupt
deleterious circuits. This atlas enables the dissection of lethal COVID-19, may inform
our understanding of long-term complications of COVID-19 survivors, and provides
an important resource for therapeutic development.
Globally, the pandemic of COVID-19, which results from infection SARS-CoV-2 at the level of the lung tissue remain unclear. A series of
with SARS-CoV-2, has led to more than 145 million cases (32 million autopsy studies that examined formalin-fixed, paraffin-embedded
in the USA) and 3.1 million deaths (570,000 in the USA; figures as of (FFPE) tissue sections from individuals who died of COVID-19 extended
26 April 2021)1. Approximately 15% of infected individuals develop our understanding of virus organotropism, but these studies were
severe disease, which can manifest as acute respiratory distress limited in their discovery potential by low-plex assays (for example,
syndrome (ARDS) and is associated with substantial morbidity and immunohistochemistry) and/or prolonged post-mortem intervals
mortality2,4. (PMIs), which adversely affect RNA quality13–15.
Previously, single-cell RNA sequencing (scRNA-seq) analyses We established a rapid autopsy program and, under Institutional
of healthy individuals have revealed the tissue distribution of host Review Board approved protocols, collected snap-frozen organ speci-
receptors that are required for SARS-CoV-2 entry5–7, and examination mens from individuals with COVID-19 within hours of death. We per-
of bronchoalveolar lavage fluid and blood from patients with COVID-19 formed single-nucleus RNA-seq (snRNA-seq) on lung samples from
of varying severity has identified the effects of SARS-CoV-2 infection individuals who died from COVID-19 and control individuals to build
on immune responses and cytokine dysregulation8–12. However, owing an atlas that provides insight into the pathophysiology of COVID-19
to the practical limitations of accessing patient tissues, the effects of and provides a key resource for further investigation.
A list of affiliations appears at the end of the paper.
114 | Nature | Vol 595 | 1 July 2021

a Cell-type assignment and differential genes
| Fatal COVID-19 (n = 19) |     | Single-nucleus RNA transcriptomics |     |         |          |
| ----------------------- | --- | ---------------------------------- | --- | ------- | -------- |
|                         |     |                                    |     | Control | COVID-19 |
Tissue nucleus extraction Droplet snRNA-seq Unique COVID-19 Control
cell and viral reads (cid:313) seneG
Short PMI
(~4 h)
116,000
QC-passed (cid:315) seneG
nuclei
Cell-type and protein-level validation Cells
Control (n = 7) Cell–cell interactions Inferred protein activity
Additional lung tissue
|     |           | cohort (n = 23)          | Tissue mass      |         |          |
| --- | --------- | ------------------------ | ---------------- | ------- | -------- |
|     |           |                          | cytometry        | Control | COVID-19 |
|     | Resection | (cid:139) Healthy donors |                  |         |          |
|     |           | (cid:139)COVID-19        | Key cytokines or |         |          |
(cid:139)Other viral/bacteria pneumonia cell-type validation Putative
target ID
|     |     | Matched cohort | Immuno- |     |     |
| --- | --- | -------------- | ------- | --- | --- |
fluoresence
(cid:139) Uninfected
(cid:139)COVID-19
| b   |            | c Control | COVID-19 | d Control | COVID-19     |
| --- | ---------- | --------- | -------- | --------- | ------------ |
|     | Mast cells |           |          | 0.8       | P = 5 × 10–4 |
P = 0.26 P = 0.04 P = 9 × 10–6 P = 1.00
Endothelial cells
P = 0.24 P = 0.39 P = 0.003
| 10  |     | 10  |     | 0.6 |     |
| --- | --- | --- | --- | --- | --- |
P = 0.010
|     | Neuronal  Fibroblasts |     |     | ycneuqerF |     |
| --- | --------------------- | --- | --- | --------- | --- |
Macrophages
|        | cells       |        |     | 0.4 |     |
| ------ | ----------- | ------ | --- | --- | --- |
| 2 PAMU | DCsB cells  | 2 PAMU |     |     |     |
Smooth muscle
| 0 Monocytes |     | 0   |     | 0.2 |     |
| ----------- | --- | --- | --- | --- | --- |
Plasma
cells
|     | NK cells Cycling          |     |     |     |     |
| --- | ------------------------- | --- | --- | --- | --- |
|     | Airway                    |     |     | 0   |     |
|     | CD8+ NK/T cells epithelia |     |     |     |     |
T cells CPA amsalp/B muilehtodnE ailehtipE stsalborbiF sllec tsaM dioleyM lanorueN KN/T
Treg cells
| –10 | CD4+ AT1      | –10     |           |     |     |
| --- | ------------- | ------- | --------- | --- | --- |
|     | T cells AT2   |         |           |     |     |
| –15 | –10 –5 0 5 10 | –15 –10 | –5 0 5 10 |     |     |
Cell type
|     | UMAP 1 |     | UMAP 1 |     |     |
| --- | ------ | --- | ------ | --- | --- |
Fig. 1 | Study design and cellular landscape. a, Overview of study design.   (n = 7) and COVID-19 lungs (n = 19). Middle line, median; box edges, 25th and
b, Major clusters and respective cell-type assignments in UMAP. c, Origins of  75th percentiles; whiskers, most extreme points that do not exceed ±1.5 × the
cells with same embedding as in b. d, Fraction of major cell types in control  interquartile range (IQR). Wilcoxon rank-sum test.
We found significant differences in cell fractions between COVID-19
The lung cellular landscape in COVID-19 and control lungs both globally (Fig. 1d) and within the immune and
The COVID-19 cohort consisted of 19 patients (12 males and 7 females)  non-immune compartments (Extended Data Fig. 2a-c). There was a
who died at a median age of 72 years (range, 58 to more than 89) (Sup- reduction in the epithelial cell compartment, due to loss of both alveo-
plementary Table 1, Extended Data Fig. 1a) and underwent rapid autopsy  lar type II (AT2) and type I (AT1) cells, and an increase in monocytes/
with a median post-mortem interval (PMI) of 4 h (range, 2–9 h). All  macrophages, fibroblasts, and neuronal cells; these observations were
had underlying co-morbidities that are associated with increased risk  independent of donor sex (Extended Data Fig. 3a, b).
of severe COVID-1916 (Supplementary Table 1). The control cohort  We found no major differences in the expression of ACE2, CD147 (also
comprised 7 individuals (4 males and 3 females) with a median age of  known as BSG), NPR1, TMPRSS2, FURIN or CTSL between COVID-19 and
70 years (range, 67 to 79 years) who underwent lung resection or biopsy  control lungs (Extended Data Fig. 3c–f). This indicates that changes in
in the pre-COVID-19 era (Supplementary Table 1). cell-type proportions were unrelated to the expression of receptors
Using snRNA-seq17 and an integrated quality control pipeline  or putative proteases that are important for viral entry, although we
(see Methods), we generated a lung atlas that profiled 116,314 nuclei,  cannot exclude the possibility that virus-mediated cell death selec-
including 79,636 from COVID-19-infected lungs and 36,678 from con- tively depletes cells with high expression of these genes. We detected
trol lungs (Fig. 1a). We used a three-pronged approach for cell-type  SARS-CoV-2 reads in two patients (Supplementary Table 3), one of
identification: unbiased identification of cluster markers, discovery  whom had HIV/AIDS (CD4+ T cell count 29 per mm3 on hospital admis-
of cell types using signatures from reported atlases, and manual  sion; 662 unique molecular identifiers detected in 28 cells), which
curation to sub-stratify cell populations and cell states using expert  suggests that viral reads can, in principle, be captured.
knowledge (see Methods). We report cell-type assignment with three
levels of granularity: major cell types, intermediate granularity, and
fine granularity (Supplementary Table 2). We visualized data with  Aberrant activation of myeloid cells
dimensionality reduction using uniform manifold approximation and  Myeloid cells represented a major cellular constituent in COVID-19
projection (UMAP) (Fig. 1b, c, Extended Data Fig. 1b–d). We identified  lungs and were more prevalent there than in control lungs (Fig. 1d,
nine major cell types: epithelial cells (n = 30,070 cells), myeloid cells  Extended Data Figs. 2a, c, 4a). We identified monocytes (n = 3,176),
(n = 29,632), fibroblasts (n = 22,909), endothelial cells (n = 5,386), T and  monocyte-derived macrophages (MDMs; n = 9,534), transitioning
natural killer (NK) lymphocytes (n = 16,751), B lymphocytes and plasma  MDMs (n = 4,203), and resident alveolar macrophages (AMs; n = 12,511),
cells (n = 7,236), neuronal cells (n = 2,017), mast cells (n = 1,464), and  which were recovered as distinct trajectories in diffusion component
antigen-presenting cells (APCs; primarily dendritic cells) (n = 849).  (DC) analysis and were more frequent in COVID-19 lungs (Fig. 2a–c,
At the most granular level, we identified 41 different cell types   Extended Data Fig. 4b–i, Supplementary Tables 2, 4, 5). Myeloid cells
(Supplementary Table 2). from individuals with COVID-19 were highly and aberrantly activated.
Nature | Vol 595 | 1 July 2021 | 115

Article
| a   |             |     | b   |           |                  | c                     | P = 0.019 |           | d                                                                                                                                                                                                                                                                                                        | Control | COVID-19 |
| --- | ----------- | --- | --- | --------- | ---------------- | --------------------- | --------- | --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | -------- |
|     | Mast cells  |     |     |           | Control COVID-19 |                       | 0.4       |           |                                                                                                                                                                                                                                                                                                          |         |          |
|     |             |     |     |           |                  |                       |           | P = 0.019 | LXA !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"""""""""""""""""""""""""""""""""""######################################################################$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%""""""&&&&&&&&&&&&&&&&&&&& |         |          |
|     |             |     |     | Monocytes |                  |                       |           | P = 0.026 |                                                                                                                                                                                                                                                                                                          |         |          |
| 10  |             |     |     |           |                  | sllec lla fo noitcarF | 0.3       |           | P = 0.0013                                                                                                                                                                                                                                                                                               |         |          |
|     | Macrophages |     |     |           |                  |                       |           |           | 961DC                                                                                                                                                                                                                                                                                                    |         |          |
Transitioning
| 2 PAMU |     |     |     | MDMs |     |     | 0.2 |     |     |     |     |
| ------ | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
DCs B cells
IPAD
| 0   | Monocytes          | Plasma cells  |     |                |                 |     |                      |                              |                    |        |            |
| --- | ------------------ | ------------- | --- | -------------- | --------------- | --- | -------------------- | ---------------------------- | ------------------ | ------ | ---------- |
|     |                    |               | 3CD |                | Alveolar        |     | 0.1                  |                              |                    |        |            |
|     | NK cells           | Cycling       |     |                | macrophages     |     |                      |                              |                    |        |            |
|     | CD8+               | NK/T cells    |     |                |                 |     |                      |                              |                    |        |            |
|     | T cells Treg cells |               |     |                |                 |     |                      |                              |                    |        |            |
|     |                    |               |     | M o n o c y te | - d e rived  C2 |     | 0                    |                              |                    |        |            |
| –10 | CD4+               |               |     | ma c r o p h   | a g e s D       |     |                      | setyconoM                    |                    |        |            |
|     | T cells            |               |     |                |                 |     | raloevlA segahporcam | devired-etyconoM segahporcam | gninoitisnarT sMDM |        |            |
| –15 | –10 –5             | 0 5 10        |     | DC1            |                 |     |                      |                              |                    | h GZMB |            |
|     |                    | UMAP 1        |     |                |                 |     |                      |                              |                    |        | Expression |
| e   |                    |               | f   |                |                 |     | g                    |                              |                    |        | 3.0        |
2 PAMU
|             | IGLV1-40          |     |             | IGLV1-40          |     |        |         |            |                         |        | 2.5        |
| ----------- | ----------------- | --- | ----------- | ----------------- | --- | ------ | ------- | ---------- | ----------------------- | ------ | ---------- |
|             | IGLV2-14 IGLV1-47 |     |             | IGLV2-14          |     |        |         |            |                         |        |            |
|             | IGLV2-23          |     |             | IGLV1-47          |     |        |         |            |                         |        | 2.0        |
|             | IGLV3-10          |     |             | IGLV2-23          |     |        |         |            |                         |        |            |
|             | IGLV3-21          |     |             | IGLV3-10 IGLV3-21 |     |        | CD4+    |            |                         |        | 1.5        |
| niahc thgiL | IGLV2-11          |     | niahc thgiL | IGLV2-11          |     |        | T cells |            |                         |        |            |
|             | IGKV3-11          |     |             | IGKV3-11          |     |        | 4       |            |                         |        |            |
| IGKV1D-13   |                   |     |             | IGKV1D-13         |     |        |         |            |                         | UMAP 1 |            |
|             | IG K V 1 -3 9     |     |             | IGKV1-39          |     |        |         | Treg cells |                         |        |            |
|             | IG K V 4 -1       |     |             | IGKV4-1           |     | 2 PAMU |         |            |                         | i      |            |
|             | IG K V 3 - 1 5    |     |             | IGKV3-15          |     |        | 0       |            | C y c lin g             | MKI67  |            |
|             | I G LV 3 -1       |     |             | IGLV3-1           |     |        |         |            | N K /T  c e lls Control |        |            |
| *IGKV3-20   | IG L V 1 0 - 5 4  | *   |             | IGLV10-54         |     |        |         |            |                         |        | Expression |
|             | IGKV1-5           |     |             | *IGKV3-20         | *   |        |         |            | COVID-19                |        |            |
|             | I G L V 3 - 2 5   |     |             | IGKV1-5           |     |        |         |            |                         | 2 PAMU | 2.0        |
|             | I G L V 1 - 5 1   |     |             | IGLV3-25 IGLV1-51 |     |        | –4 CD8+ |            |                         |        | 1.5        |
|             | IGLV3-19          |     |             | IGLV3-19          |     |        | T cells |            |                         |        |            |
|             | IGLV3-27          |     |             | IGLV3-27          |     |        |         |            |                         |        | 1.0        |
Occurences 43-4VHGI 51-3VHGI 15-5VHGI 7-3VHGI 1-4-7VHGI D96-1VHGI 32-3VHGI 93-4VHGI 03-3VHGI 81-1VHGI* 84-3VHGI 12-3VHGI 42-1VHGI 11-3VHGI 33-3VHGI 64-1VHGI 1-6VHGI 2-1VHGI 47-3VHGI 35-3VHGI Group 43-4VHGI 51-3VHGI 15-5VHGI 7-3VHGI 1-4-7VHGI D96-1VHGI 32-3VHGI 93-4VHGI 03-3VHGI 81-1VHGI* 84-3VHGI 12-3VHGI 42-1VHGI 11-3VHGI 33-3VHGI 64-1VHGI 1-6VHGI 2-1VHGI 47-3VHGI 35-3VHGI –8 NK cells 0.5
Control
| 12345 |     |     |     | COVID-19 |     |     | –5  | 0      | 5 10 |     |     |
| ----- | --- | --- | --- | -------- | --- | --- | --- | ------ | ---- | --- | --- |
|       |     |     |     | Shared   |     |     |     | UMAP 1 |      |     |     |
UMAP 1
|     |     | Heavy chain |     |     | Heavy chain |     |     |     |     |     |     |
| --- | --- | ----------- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- |
Fig. 2 | Immune responses in COVID-19. a, UMAP projection highlighting  selected area with overlay; bottom, individual channels. Scale bar, 20 μm.
immune cell clusters. b, Visualization of myeloid cells using the first three DCs.  e, f, Top 20 recurrently detected IGHV–IGLV combinations in COVID-19 (e) and
Inset indicates group assignment. c, Fraction of myeloid cells in control (n = 7)  corresponding group annotation (f). *Combination for previously described
and COVID-19 lungs (n = 19). Middle line, median; box edges, 25th and 75th  anti-RBD antibody21. g, UMAP of T/NK cells; inset, group assignments.
percentiles; whiskers: most extreme points that do not exceed ±1.5 × IQR.  h, i, RNA expression (log-normalized) of GZMB (h) and MKI67 (i) in the same
| Wilcoxon rank-sum test. d. Representative immunofluorescence staining for  |     |     |     |     |     | embedding as g. |     |     |     |     |     |
| -------------------------------------------------------------------------- | --- | --- | --- | --- | --- | --------------- | --- | --- | --- | --- | --- |
CD169, AXL and DAPI (large image) in control and COVID-19 lung tissue; top,
For example, MDMs in COVID-19 lungs differentially expressed genes  and only modest upregulation of cytokines and programs associated
of activation (for example, CTSB, CTSD, CTSZ, PSAP) and two long  with activation and tissue residency of T cells (Fig. 2g–i, Extended Data
non-coding RNAs, NEAT1 and MALAT1, that are associated with aber- Fig. 7a–i). Although immune response patterns were highly variable
rant macrophage activation and impaired T cell immunity18 (Extended
(Extended Data Fig. 7j, k), these data suggest that an impaired T cell
Data Fig. 5a, Supplementary Table 5). AMs, which arise from fetal  response might contribute to lethal outcomes in COVID-19 in the con-
monocytes and can self-renew19, were enriched and highly activated  text of a principally preserved humoral immune response.
in COVID-19 lungs (Fig. 2c, Extended Data Fig. 5a). Notably, COVID-
19 AMs showed strongly decreased mRNA and protein expression of
the tumour-associated macrophage receptor AXL (Fig. 2d, Extended  Impaired alveolar epithelial regeneration
Data Fig. 5b, c), a receptor tyrosine kinase that is important for coor- Within the epithelial compartment, we identified alveolar epithelial
dinated clearance of apoptotic cells (efferocytosis) and subsequent  cells (AT1 and AT2 cells; n = 20,949), airway epithelial cells (basal, cili-
anti-inflammatory regulation during tissue regeneration20. These data  ated, club, goblet, and mucous cells; n = 7,223), a cluster characterized
suggest that myeloid cells are a major source of dysregulated inflam- by the expression of inflammatory and cell cycle genes, including IRF8,
mation in COVID-19. B2M, MKI67 and TOP2A (‘cycling epithelium’; n = 609), and a cluster
showing high expression of the extracellular matrix (ECM) components
COL6A3, COL1A2, and COL3A1 (‘ECMhigh epithelium’; n = 1,179) (Fig. 3a,
Plasma and T cell responses
b, Extended Data Fig. 8a–c, Supplementary Tables 2, 7).
AT2 cells serve as progenitors for AT1 cells during lung regeneration22.
To gain insights into humoral immunity against SARS-CoV-2 infection
in the lung, we identified plasma cells (Extended Data Fig. 6a–c) and  AT2 and T1 cells in control lungs formed distinct clusters (Fig. 3a, b) and
reconstructed immunoglobulins by determining mRNA co-expression  demonstrated the expected changes in differential gene expression
of the variable heavy (IGHV) and light (IGLV) chains and isotypes on a  (DGE) analysis, including expression of the lineage markers SFTPC
per cell basis (see Methods; Extended Data Fig. 6d–k, Supplementary  and SFTPB in AT2 cells, and CLIC5 and AGER in AT1 cells (Fig. 3c, Sup-
Table 6). IGHV1-18–IGLV3-20, which gives rise to a neutralizing antibody  plementary Table 7). By contrast, clustering of AT2 and AT1 cells in
(S309)21 against the receptor binding domain (RBD) of the SARS-CoV-2
COVID-19 lungs was less discrete, with a substantial portion of cells
spike protein, was among the commonly identified IGHV–IGLV combi- not overlapping with their control counterparts (Fig. 3b). Both AT2 and
nations, which suggests that a coordinated antibody response occurred  AT1 cells from COVID-19 lungs showed decreased overall expression
(Fig. 2e, f, Extended Data Fig. 6l, m). In the T/NK cell compartment  of defining markers (Fig. 3c). COVID-19 AT2 cells displayed decreased
(Fig. 2g), we distinguished CD8+ T cells (n = 3,561), T regulatory (T )  expression of ETV5 (Fig. 3d), a transcription factor that is required for
reg
cells (n = 649), other CD4+ T cells (n = 7,586), and NK cells (n = 2,141). We  maintaining AT2 cell identity. Decreased ETV5 expression is associated
with differentiation towards AT1 cells23, indicating that AT2 cells had
found no significant increase in T cell abundances in COVID-19 lungs,
116 | Nature | Vol 595 | 1 July 2021

| a      |                   |         |        | c            |     |     |     | AT1 exp.                | Cell-type signature expression |                |          |          | d                 | e                 |          |
| ------ | ----------------- | ------- | ------ | ------------ | --- | --- | --- | ----------------------- | ------------------------------ | -------------- | -------- | -------- | ----------------- | ----------------- | -------- |
|        |                   |         |        |              |     |     |     | AT2 exp.                | AT1                            | AT2 Primed AT2 |          | DATP sig | ETV5              |                   | CAV1     |
|        |                   |         |        |              |     |     |     | P r im e d   A T 2 exp. | 3                              | 4              | 2        | 1.5      | P = 8.18 × 10–100 | P = 1.03 × 10–125 |          |
|        |                   | ECMhigh | AT1    |              |     |     |     | D A TP   e x p .        |                                |                |          |          |                   |                   |          |
|        | Cycling           |         |        |              |     |     |     | Cell type Group         |                                |                |          |          |                   | 5                 |          |
|        | epithelialAirway  |         |        | seneg rekraM |     |     |     | SFTPB                   |                                |                |          |          | 4                 | 91-DIVOC          | 91-DIVOC |
|        | 5                 | mucous  |        | 2TA          |     |     |     | SFTPC                   | 0                              | 0              | –0.5     | 0        |                   |                   |          |
|        |                   |         |        |              |     |     |     | SFTPD                   |                                |                |          |          | noisserpxE        | noisserpxE 4      |          |
|        |                   |         |        |              |     |     |     | ETV5 Expression         |                                | Cell-type      |          |          | 3                 |                   |          |
| 2 PAMU |                   |         |        | 1TA          |     |     |     | AGER CLIC5              |                                | assignme n t   | Group    |          |                   | 3                 |          |
|        |                   |         | A i rw | ay           |     |     |     | PDPN                    | 2                              |                |          |          | 2                 |                   |          |
|        | 0 Airway          |         | cl u   | b            |     |     |     | LRRK2                   |                                | A T 1          | Control  |          |                   | 2                 |          |
|        | ciliatedAirway    |         |        |              |     |     |     | AGBL1                   | 1                              | AT2            | COVID-19 |          |                   | lortnoC           | lortnoC  |
|        |                   | goblet  |        |              |     |     |     | SFTPA2 SFTPA1           | 0                              |                |          |          | 1                 | 1                 |          |
DLG2
|     |     | Airway  |     |     |     |     |     | AFF3           | −1 f |     | AT1 |     | 0   | 0          |     |
| --- | --- | ------- | --- | --- | --- | --- | --- | -------------- | ---- | --- | --- | --- | --- | ---------- | --- |
|     | –5  |         |     |     |     |     |     | AUTS2          |      |     |     |     |     |            |     |
|     |     | basal   |     |     |     |     |     | ACOXL          |      | AT2 |     |     | AT2 |            | AT1 |
|     |     |         |     |     |     |     |     | AC096531.2 TTN | 2.5  |     |     |     |     | g          |     |
|     |     | AT2     |     |     |     |     |     | DLGAP1         |      |     |     |     |     | P = 0.0014 |     |
)2TA  susrev 1TA( noisserpxe eneg laitnereffiD TMEM163 noisserpxe erutangis PTAD
|        | –10      | –5     | 0 5 |     |     |     |     | LHFPL3             | 2 PAMU 0 |               |         |           | Control  | 2.0            | 91-DIVOC |
| ------ | -------- | ------ | --- | --- | --- | --- | --- | ------------------ | -------- | ------------- | ------- | --------- | -------- | -------------- | -------- |
|        |          | UMAP 1 |     |     |     |     |     | ERBB4 CCDC141      |          |               |         |           |          |                |          |
|        |          |        |     |     |     |     |     | ABCA3              |          |               |         |           | COVID-19 | 1.5            |          |
| b      |          |        |     |     |     |     |     | ZNF385B            |          |               |         |           |          |                |          |
|        | Control  |        |     |     |     |     |     | DMBT1              | –2.5     |               |         |           |          |                |          |
|        |          |        |     |     |     |     |     | PTPRG ROS1         |          |               |         |           |          | 1.0            |          |
|        | COVID-19 |        |     |     |     |     |     | ANK3               |          |               | DATP    |           |          |                |          |
|        |          |        |     |     |     |     |     | STEAP4             |          |               |         |           |          | 0.5            | lortnoC  |
|        |          |        |     |     |     |     |     | TOX                | –5.0     |               |         |           |          |                |          |
|        |          |        |     |     |     |     |     | WIF1 NCKAP5        |          |               |         |           |          | 0              |          |
|        |          |        |     |     |     |     |     | NTM                |          | –5            | 0       | 5 10      |          |                |          |
|        | 5        |        |     |     |     |     |     | RTKN2              |          | UMAP 1 UMAP 1 |         |           |          |                |          |
|        |          |        |     |     |     |     |     | KHDRBS2            | h        |               |         |           |          |                |          |
|        |          |        |     |     |     |     |     | ATF7IP2 ST6GALNAC5 |          |               | AT1 AT1 |           |          | AT cells       |          |
| 2 PAMU |          |        |     |     |     |     |     | EMP2               |          | AT2 AT2       |         |           | DATP     | p = 4.1 × 10–4 |          |
|        |          |        |     |     |     |     |     | GPM6A              |          |               |         | signature |          | i              |          |
|        | 0        |        |     |     |     |     |     | AC027288.3         |          |               |         | –0.38     | 2        |                | 91-DIVOC |
|        |          |        |     |     |     |     |     | DST AC022325.2     |          |               |         |           |          | 0.6            |          |
|        |          |        |     |     |     |     |     | COL4A2             |          |               |         |           |          | sllec TA/PTAD  |          |
AL355499.1
|     |     |        |     |     |     |     |     | LINC01290 |         |     |          |       | Control  |       |         |
| --- | --- | ------ | --- | --- | --- | --- | --- | --------- | ------- | --- | -------- | ----- | -------- | ----- | ------- |
|     | –5  |        |     |     |     |     |     | MAP2 CAV1 |         |     |          |       | COVID-19 | 0.4   |         |
|     |     |        |     |     |     |     |     | KCNT2     | 3CD 3CD |     |          |       |          |       |         |
|     |     |        |     |     |     |     |     | SCEL      |         |     |          |       |          |       | lortnoC |
|     |     |        |     |     |     |     |     | TIMP3     |         |     |          |       |          | 0.2   |         |
|     |     |        |     |     |     |     |     | NRG1 GRK5 |         |     |          | C2 C2 |          |       |         |
|     | –10 | –5     | 0 5 |     |     |     |     | SEM5A     |         |     | DATP D D |       |          |       |         |
|     |     | UMAP 1 |     |     |     |     |     | ARHGEF26  |         |     |          |       |          | 0     |         |
|     |     |        |     |     |     |     |     | RBMS3     |         |     |          |       |          | Group |         |
DC1 DC1
| j   |     |     |     |     | k   |     |     |     | l   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Control COVID-19 Macrophages Monocytes Macrophages Epithelial cells
| 8TRKCPS-orP |     |     |     |     | 160 |           |     |                 |     | 350 |            |     | 300 |                  |     |
| ----------- | --- | --- | --- | --- | --- | --------- | --- | --------------- | --- | --- | ---------- | --- | --- | ---------------- | --- |
|             |     |     |     |     |     | P = 0.031 | 175 | P = 1.19 × 10–9 |     |     | P = 0.0010 |     |     | P = 1.46 × 10–10 |     |
2mm rep sllec +β1-LI 140 P =  0 .0 3 6 2mm rep sllec +β1-LI P  =   0 . 0 0 8 3 2mm rep sllec +6-LI 300 P = 0.153 2mm rep sllec +6-LI 250 P = 0.095
|      |     |     |     |     |     | P  =  0 . 196 | 150 | P   =   0 . 0 0 86 |     |     | P = 0.141 |     |     | P = 9.27 × 10–8 |     |
| ---- | --- | --- | --- | --- | --- | ------------- | --- | ------------------ | --- | --- | --------- | --- | --- | --------------- | --- |
|      |     |     |     |     | 120 | P = 0.026     |     | P = 0.00053        |     | 250 | P = 0.064 |     |     | P = 0.0015      |     |
|      |     |     |     |     | 100 |               | 125 |                    |     |     |           |     | 200 |                 |     |
|      |     |     |     |     |     |               | 100 |                    |     | 200 |           |     |     |                 |     |
|      |     |     |     |     | 80  |               |     |                    |     |     |           |     | 150 |                 |     |
|      |     |     |     |     | 60  |               | 75  |                    |     | 150 |           |     |     |                 |     |
| IPAD |     |     |     |     |     |               |     |                    |     | 100 |           |     | 100 |                 |     |
|      |     |     |     |     | 40  |               | 50  |                    |     |     |           |     |     |                 |     |
|      |     |     |     |     | 20  |               | 25  |                    |     | 50  |           |     | 50  |                 |     |
|      |     |     |     |     | 0   |               | 0   |                    |     | 0   |           |     | 0   |                 |     |
Healthy Flu ARDS Pneumonia COVID-19 Healthy Flu ARDS Pneumonia COVID-19
Fig. 3 | Impaired lung regeneration and sources of inflammation. a, b, UMAP  AT2 and AT1 cells and DATPs, expression of DATP signature and group
of investigated alveolar and airway epithelial cells (a) and corresponding group  assignment (inset). i, Fractions of DATP and AT cells in control (n = 7) and
assignments (b). c, Differential gene expression (log-normalized, scaled;  COVID-19 lungs (n = 19). Middle line, median; box edges, 25th and 75th
see Methods) of AT1 and AT2 cells from COVID-19 and control lungs. Columns,  percentiles; whiskers, most extreme points that do not exceed ±1.5 × IQR.
single cells; rows, expression of top-regulated genes. Left bar, lineage markers  Wilcoxon rank-sum test. j, Representative immunofluorescence staining for
for AT1 (purple) and AT2 (pink) cells. Colour-coded top lanes indicate  pro-SPC, KRT8 and DAPI in control and COVID-19 lung tissue; top,
expression strength of signatures (log-normalized; see Methods) and group  representative area with overlay; bottom, small images with individual
assignment as indicated on the right. exp., expression. d, e, Violin plots of ETV5  channels of selected area. Scale bar, 50 μm. k, l, Tissue mass cytometric
and CAV1 mRNA expression (log-normalized) in AT2 and AT1 cells, respectively;  quantification of IL-1β (k) and IL-6 (l) in healthy lung tissue and samples from
Wilcoxon rank-sum test with Bonferroni correction. f, UMAP embedding of AT1  donors with different infectious aetiologies. Each dot represents
and AT2 cells and identified DATPs; inset indicates group assignments.   quantification of IL-1β and IL-6 in a region of interest (ROI); two-sided Mann–
g, Violin plots of DATP signature expression (log-normalized) in AT1 and AT2  Whitney U-test with Benjamini–Hochberg false discovery rate (FDR)
| cells. Wilcoxon rank-sum test. h, First three DCs showing main trajectories of  |     |     |     |     |     |     |     | adjustment. |     |     |     |     |     |     |     |
| ------------------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
initiated a regeneration program (Fig. 3d, Extended Data Fig. 8d). CAV1,  for the hypoxia response via HIF-1α (Extended Data Fig. 8o), consistent
a marker of late AT1 maturation24, was expressed at significantly lower  with pathways that have been implicated in DATP in mouse models27.
levels in AT1 cells from COVID-19 lungs (Fig. 3e). Overall, these data  Consistent with overrepresentation of p53 signalling, the majority of
suggest incomplete transition of AT2 to AT1 cells in COVID-19 lungs. DATPs did not undergo cell division (Extended Data Fig. 8p), suggesting
Recent studies have shown that inflammation can induce a cell state  that they arrest in the DATP cell state.
that is characterized by failure to fully transition to AT1 cells; this has  DATPs were more frequent in COVID-19 than control lungs (Fig. 3i).
been termed ‘damage-associated transient progenitors’ (DATPs), ‘alveo- Immunofluorescence staining of corresponding tissues showed that
lar differentiation intermediate’ (ADI), or ‘pre-AT1 transitional cell state’  the frequency of KRT8+ and CLDN4+ DATPs was higher in COVID-19
(PATS)25–27 (hereafter referred to as DATPs). We used expression of the  lungs (Fig. 3j, Extended Data Fig. 8r, s), and we observed progressive
DATP marker genes (KRT8, CLDN4 and CDKN1A)25 to develop a DATP sig- loss of AT1 cell abundance with increasing time from symptom onset to
nature (see Methods; Extended Data Fig. 8e–h, Supplementary Table 8)  death (Extended Data Fig. 8t). Overall, these data suggest that, in addi-
and found that alveolar epithelial cells from COVID-19 lungs scored  tion to direct destruction of the alveolar epithelium by viral infection,
significantly higher for expression of this signature than those from  lung-regenerative processes are impaired in individuals with COVID-19.
control lungs (Fig. 3f, g, Extended Data Fig. 8i). DC analysis separated a  We next determined the sources of inflammation that contribute
main trajectory from AT2 to AT1 cells, while DATPs were primarily local- to the DATP cell state, and more generally, to the hyperinflammatory
ized between AT2 and AT1 cells (Fig. 3h, Extended Data Fig. 8j–n). Gene  environment in COVID-19 lungs. Capture of the inflammatory cytokine
set enrichment analysis (GSEA) of DATPs compared to differentiated  interleukin (IL)-1β (and others) at an mRNA level may be limited, as the
bioactive form of IL-1β, which has a major role in triggering DATPs25, is
AT2 or AT1 cells showed enrichment for TNFα and p53 signalling, and
Nature | Vol 595 | 1 July 2021 | 117

Article
a
Pathological fibroblasts and lung fibrosis 20 There were significantly more fibroblasts in COVID-19 lungs than in
15 control lungs (Fig. 1d); immunohistochemistry staining for α-smooth
muscle actin (α-SMA) validated this finding (Extended Data Fig. 12a– 10 d). The degree of fibrosis (determined by a Sirius red fibrosis score,
5 see Methods) was correlated with disease duration (Fig. 4a), indicat-
ing that lung fibrosis increases over time in COVID-19. We identified 0 20 40 60 five fibroblast subtypes: alveolar (n = 4,670), adventitial (n = 3,773), Days from symptom
onset to death pathological (n = 2,322), intermediate pathological (n = 8,779), and
other (n = 1,099) (Fig. 4b, Extended Data Fig. 12e). The main driver of
differences in the fibroblast cluster was the increased frequency of
pathological or intermediate pathological fibroblasts (henceforth
collectively referred to as pFBs) in COVID-19 lungs compared to control
lungs (Fig. 4c, Extended Data Fig. 12f). pFBs strongly expressed CTHRC1,
a recently described hallmark gene that defines these cells, and genes
of pathological ECM3, including COL1A1 and COL3A1 (Extended Data
Fig. 12e, Supplementary Table 9). pFBs are key drivers of lung fibrosis
in mouse models and in patients with idiopathic pulmonary fibrosis
(IPF) or scleroderma3. Their increased frequency suggests that pFBs
promote rapidly evolving lung fibrosis in individuals with COVID-19.
Given the importance of fibroblasts in remodelling of the lung
generated by cleavage from pro-IL-1β upon inflammasome activation; ecosystem, we next investigated ligand–receptor interactions across
thus, protein-level assessment provides complementary information. all major cell types, including fibroblasts (see Methods). Among the
For this purpose, we leveraged a recently released high-plex imaging enriched inferred ligand–receptor interactions across all cells were
mass-cytometry dataset that profiled 237 tissue regions from 23 individ- TGFβ1–TGFβ receptor 2 and BMP6–ACVR1 (Extended Data Fig. 12g–i,
uals, including healthy controls; patients with influenza pneumonia, bac- Supplementary Table 10), which belong to the TGFβ family and super-
terial pneumonia, or ARDS; and ten patients who died from COVID-1928. family, respectively. TGFβ signalling has an important role in promoting
IL-1β was more strongly expressed in monocytes and macrophages from lung fibrosis and has been implicated in fibroblast-mediated mainte-
individuals with COVID-19 than from healthy individuals or patients in nance of the ADI27, which is closely related to the DATP cell state. To
the other disease groups (Fig. 3k, Extended Data Fig. 9a–c). IL-6, another investigate potential therapeutic strategies directed against pFBs, we
key inflammatory cytokine invoked in the pathophysiology of COVID-19, inferred protein activity from single-nucleus transcriptomes followed
was more abundant in epithelial cells from patients with COVID-19, but by comparison of pFBs with other fibroblasts. This analysis predicted
was not differentially expressed in macrophages from these patients that pFBs would show increased activity of JunB and JunD (Extended
compared to patients in other disease groups (Fig. 3l, Extended Data Data Fig. 12j, Supplementary Table 11), which induce lung fibrosis in
Fig. 9d–f). Finally, we found that the expression of type I interferons mouse models via enhanced TGFβ and STAT3 signalling and are associ-
and interferon response genes in various cell types, including AT2 cells, ated with increased production of IL-1β30. Finally, we inferred drugga-
monocytes, and macrophages, was stronger in patients with COVID-19 ble targets in pFBs (see Methods) and identified MMP14 and STAT3 as
than in control donors (Extended Data Fig. 9g, h). Together, these data potential targets to abrogate detrimental programs in pFBs (Extended
suggest that myeloid-derived IL-1β might be a distinguishing feature of Data Fig. 12j, Supplementary Table 11).
COVID-19 compared to other viral or bacterial pneumonias and may
contribute to the induction and maintenance of the DATP cell state.
Discussion
We generated a single-cell transcriptome lung atlas of COVID-19 using
Ectopic tuft-like cells in COVID-19
short-PMI autopsy specimens and control lung samples. Our analysis
Among captured airway epithelial cells, we recovered four distinct provides a broad census of the cellular landscape, cell programs, and
trajectories: KRT5+TP63+ basal (n = 534), club (n = 1,232), and goblet cells cell circuits of lethal COVID-19. The additional inference of protein activ-
(n = 1,757), and one trajectory with fewer cells (n = 110) that was primarily ity and cell-to-cell interactions, and analysis of inflammatory cytokines
found in COVID-19 lungs, which we identify as putative tuft-like cells across various cell types using imaging mass cytometry data, provide a
(Extended Data Fig. 10a–e). Tuft cells are involved in airway inflamma- granular perspective of the detrimental consequences of SARS-CoV-2
tion and intestinal tissue regeneration29, but their role in viral pneumo- infection in the lung.
nia remains unclear. The numbers of tuft cells (CHAT+ or POU2F3+) were Our analyses suggest interactions among aberrantly activated
increased threefold in the upper airways of individuals with COVID-19, monocytes/macrophages that produce IL-1β, inflammation-induced
and they were ectopically present in the lung parenchyma of COVID-19 impairment of alveolar epithelial regeneration, and expansion of patho-
but not control lungs (Extended Data Fig. 10f–k). To begin to elucidate a logical fibroblasts that promote fibrosis and may impair regeneration
putative role of tuft cells in viral pneumonia, we infected both wild-type (Extended Data Fig. 12f, k, Supplementary Discussion). In addition to
and Pou2f3−/− mice, which lack tuft cells, with PR8, a laboratory-adapted these deleterious events, our data suggest that despite a potentially
strain of H1N1 influenza virus (see Methods). Compared to controls, the sufficient humoral immune response (Supplementary Discussion),
lungs of Pou2f3−/− mice showed decreased infiltration of macrophages there was an inadequate T cell response in the lungs of individuals who
and decreased expression of chemotaxis genes (including Ccl3 and died of COVID-19. A recent study showed that impaired B cell function
Ccl8) that are also involved in the recruitment of myeloid cells to the in patients with cancer who contracted COVID-19 was not associated
lungs of individuals who died of COVID-19 (Extended Data Figs. 9g, h, with increased mortality31, but that lack of an adequate CD8+ T cell
11a–l). Although their role needs to be further examined, these ectopic response (even in the presence of adequate humoral immunity) was
tuft-like cells may contribute to the pathophysiology of COVID-19 (Sup- associated with worse viral control and increased mortality31. Although
plementary Discussion). our COVID-19 cohort did not include patients with cancer, these data
118 | Nature | Vol 595 | 1 July 2021
)der
suiriS(
erocs
sisorbiF
R2 = 0.386 P = 0.010 8
00
–8 –5 0 5 10
UMAP 1
2 PAMU
Adventitial Pathological FB FB 0.75
4
Vascular
Intermediate smooth muscle 0.50 path. FB Pericytes Other FB
Airway 0.25
–4 Alveolar smooth muscle
FB Mesothelial FB 0
stsalborbfi
gnoma
noitcarF
b Control c P = 0.022
COVID-19
Pathological
fibroblasts
91-DIVOC
lortnoC
Fig. 4 | Pathological fibroblasts and ensuing fibrosis in COVID-19.
a, Coefficient of determination (R2) of days from symptom onset to death
and fibrosis score in COVID-19 samples (n = 16, see Methods). Error bands,
95% s.e. interval on the Pearson correlation. b, UMAP of fibroblast (FB)
sub-populations; inset indicates group assignments. path., pathological.
c, Fractions of pathological fibroblasts among all fibroblasts in control (n = 7)
and COVID-19 lungs (n = 19). Middle line, median; box edges, 25th and 75th
percentiles; whiskers, most extreme points that do not exceed ±1.5 × IQR.
Wilcoxon rank-sum test.

suggest that whereas humoral immunity may be dispensable in the 19. Hoeffel, G. et al. C-Myb+ erythro-myeloid progenitor-derived fetal monocytes give rise to
context of adequate T cell immunity against SARS-CoV-2, a lack of adult tissue-resident macrophages. Immunity 42, 665–678 (2015).
20. Doran, A. C., Yurdagul, A. Jr & Tabas, I. Efferocytosis in health and disease. Nat. Rev.
appropriate T cell responses in our patients is likely to have contrib- Immunol. 20, 254–267 (2020).
uted to fatal outcomes. 21. Pinto, D. et al. Cross-neutralization of SARS-CoV-2 by a human monoclonal SARS-CoV
antibody. Nature 583, 290–295 (2020).
Although our study provides insight into host responses to lethal
22. Barkauskas, C. E. et al. Type 2 alveolar cells are stem cells in adult lung. J. Clin. Invest. 123,
SARS-CoV-2 infection, it is limited by a small sample size. However, 3025–3036 (2013).
through coordinated efforts, our work will contribute to a collection 23. Zhang, Z. et al. Transcription factor Etv5 is essential for the maintenance of alveolar type
of studies, including the companion paper by T. M. Delorey et al.32, with II cells. Proc. Natl Acad. Sci. USA 114, 3903–3908 (2017).
24. Little, D. R. et al. Transcriptional control of lung alveolar type 1 cell development and
streamlined protocols and harmonized metadata to enable integra- maintenance by NK homeobox 2-1. Proc. Natl Acad. Sci. USA 116, 20545–20555 (2019).
tion and combined analyses, and will help to account for important 25. Choi, J. et al. Inflammatory signals induce AT2 cell-derived damage-associated transient
progenitors that mediate alveolar regeneration. Cell Stem Cell 27, 366–382.e7 (2020).
co-variables. Furthermore, because our analysis is focused on lung
26. Kobayashi, Y. et al. Persistence of a regeneration-associated, transitional alveolar
tissue from patients who died of COVID-19, we have examined only a epithelial cell state in pulmonary fibrosis. Nat. Cell Biol. 22, 934–946 (2020).
subset of potential disease phenotypes. Nonetheless, several observa- 27. Strunz, M. et al. Alveolar regeneration through a Krt8+ transitional stem cell state that
persists in human lung fibrosis. Nat. Commun. 11, 3559 (2020).
tions, such as the rapid development of pulmonary fibrosis (Supple-
28. Rendeiro, A. F. et al. The spatial landscape of lung pathology during COVID-19
mentary Discussion), are likely to be relevant for patients who survive progression. Nature https://doi.org/10.1038/s41586-021-03475-6 (2021).
severe COVID-19, and may inform our understanding of the long-term 29. Westphalen, C. B. et al. Long-lived intestinal tuft cells serve as colon cancer-initiating
complications seen in these individuals33. cells. J. Clin. Invest. 124, 1283–1295 (2014).
30. Cui, L. et al. Activation of JUN in fibroblasts promotes pro-fibrotic programme and
In conclusion, we have generated a molecular single-cell lung atlas modulates protective immunity. Nat. Commun. 11, 2795 (2020).
from short-PMI tissue specimens and identified pathological circuits of 31. Bange, E. M. et al. CD8 T cells compensate for impaired humoral immunity in COVID-19
patients with hematologic cancer. Preprint at https://doi.org/10.21203/rs.3.rs-162289/v1
lethal COVID-19. This atlas establishes an important resource for inves-
(2021).
tigating host responses to SARS-CoV-2 and understanding potential 32. Delorey, T. M. et al. COVID-19 tissue atlases reveal SARS-CoV-2 pathology and cellular
long-term pulmonary sequelae resulting from COVID-19, and provides targets. Nature https://doi.org/10.1038/s41586-021-03570-8 (2021).
33. Nalbandian, A. et al. Post-acute COVID-19 syndrome. Nat. Med. 27, 601–615 (2021).
a basis for therapeutic development for severe disease.
Publisher’s note Springer Nature remains neutral with regard to jurisdictional claims in
published maps and institutional affiliations.
Online content
© The Author(s), under exclusive licence to Springer Nature Limited 2021, corrected
Any methods, additional references, Nature Research reporting sum- publication 2021
maries, source data, extended data, supplementary information,
acknowledgements, peer review information; details of author con- 1Department of Medicine, Division of Hematology/Oncology, Columbia University Irving
tributions and competing interests; and statements of data and code Medical Center, New York, NY, USA. 2Columbia Center for Translational Immunology,
availability are available at https://doi.org/10.1038/s41586-021-03569-1. Columbia University Irving Medical Center, New York, NY, USA. 3Columbia Center for Human
Development, Columbia University Irving Medical Center, New York, NY, USA. 4Division of
Digestive and Liver Diseases, Columbia University Irving Medical Center, New York, NY, USA.
1. Dong, Y. et al. Epidemiology of COVID-19 among children in china. Pediatrics 145, 5Department of Medicine, Columbia University Irving Medical Center, New York, NY, USA.
e20200702 (2020). 6Department of Systems Biology, Columbia University Irving Medical Center, New York, NY,
2. Zhou, F. et al. Clinical course and risk factors for mortality of adult inpatients with USA. 7Department of Pathology and Cell Biology, Columbia University Irving Medical Center,
COVID-19 in Wuhan, China: a retrospective cohort study. Lancet 395, 1054–1062 (2020). New York, NY, USA. 8Institute for Computational Biomedicine, Weill Cornell Medicine, New
3. Tsukui, T. et al. Collagen-producing lung cell atlas identifies multiple subsets with distinct
York, NY, USA. 9Caryl and Israel Englander Institute for Precision Medicine, Weill Cornell
localization and relevance to fibrosis. Nat. Commun. 11, 1920 (2020).
4. Bellani, G. et al. Epidemiology, patterns of care, and mortality for patients with acute Medicine, New York, NY, USA. 10Laboratory of Systems Pharmacology, Harvard Medical
respiratory distress syndrome in intensive care units in 50 countries. J. Am. Med. Assoc. School, Boston, MA, USA. 11Klarman Cell Observatory, Broad Institute of MIT and Harvard,
315, 788–800 (2016). Cambridge, MA, USA. 12Department of Electrical Engineering and Computer Science,
5. Muus, C. et al. Single-cell meta-analysis of SARS-CoV-2 entry genes across tissues and Massachusetts Institute of Technology, Cambridge, MA, USA. 13Department of Cancer
demographics. Nat. Med. 27, 546–559 (2021). Immunology and Virology, Dana-Farber Cancer Center, Boston, MA, USA. 14Department of
6. Sungnak, W. et al. SARS-CoV-2 entry factors are highly expressed in nasal epithelial cells Physiology and Biophysics, Weill Cornell Medical College, New York, NY, USA. 15WorldQuant
together with innate immune genes. Nat. Med. 26, 681–687 (2020). Initiative for Quantitative Prediction, Weill Cornell Medicine, New York, NY, USA. 16Human
7. Ziegler, C. G. K. et al. SARS-CoV-2 receptor ACE2 is an interferon-stimulated gene in
Immune Monitoring Core, Columbia University Irving Medical Center, New York, NY, USA.
human airway epithelial cells and is detected in specific cell subsets across tissues. Cell
17Department of Medicine, Division of Pulmonary and Critical Care, Massachusetts General
181, 1016–1035.e19 (2020).
8. Schulte-Schrepping, J. et al. Severe COVID-19 is marked by a dysregulated myeloid cell Hospital, Boston, MA, USA. 18Cell Circuits, Broad Institute of MIT and Harvard, Cambridge, MA,
compartment. Cell 182, 1419–1440.e23 (2020). USA. 19Systems Biology, Harvard Medical School, Boston, MA, USA. 20Department of
9. Wilk, A. J. et al. A single-cell atlas of the peripheral immune response in patients with Ophthalmology, University of California San Diego, La Jolla, CA, USA. 21Department of
severe COVID-19. Nat. Med. 26, 1070–1076 (2020). Dermatology, Weill Cornell Medical College, New York, NY, USA. 22Meyer Cancer Center, Weill
10. Xu, G. et al. The differential immune responses to COVID-19 in peripheral and lung Cornell Medical College, New York, NY, USA. 23Department of Genetics and Genomic
revealed by single-cell RNA sequencing. Cell Discov. 6, 73 (2020). Science, Icahn School of Medicine at Mount Sinai, New York, NY, USA. 24Department of
11. Hadjadj, J. et al. Impaired type I interferon activity and inflammatory responses in severe
Population Health Science and Policy, Icahn School of Medicine at Mount Sinai, New York, NY,
COVID-19 patients. Science 369, 718–724 (2020).
USA. 25Human Oncology and Pathogenesis Program, Memorial Sloan Kettering Cancer
12. Blanco-Melo, D. et al. Imbalanced host response to SARS-CoV-2 drives development of
COVID-19. Cell 181, 1036–1045.e9 (2020). Center, New York, NY, USA. 26Department of Radiation Oncology, Memorial Sloan Kettering
13. Ackermann, M. et al. Pulmonary vascular endothelialitis, thrombosis, and angiogenesis in Cancer Center, New York, NY, USA. 27Division of Gastroenterology and Hepatology,
Covid-19. N. Engl. J. Med. 383, 120–128 (2020). Department of Medicine, Weill Cornell Medicine, New York, NY, USA. 28Department of
14. Puelles, V. G. et al. Multiorgan and renal tropism of SARS-CoV-2. N. Engl. J. Med. 383, Pathology and Laboratory Medicine, Weill Cornell Medicine, New York, NY, USA. 29Department
590–592 (2020). of Medicine, Weill Cornell Medicine, New York, NY, USA. 30Institute of Human Nutrition,
15. De Michele, S. et al. Forty postmortem examinations in COVID-19 patients. Am. J. Clin. Columbia University, New York, NY, USA. 31Herbert Irving Comprehensive Cancer Center,
Pathol. 154, 748–760 (2020). Columbia University Irving Medical Center, New York, NY, USA. 32Program for Mathematical
16. Goyal, P. et al. Clinical characteristics of Covid-19 in New York City. N. Engl. J. Med. 382,
Genomics, Columbia University, New York, NY, USA. 33These authors contributed equally:
2372–2374 (2020).
17. Slyper, M. et al. A single-cell and single-nucleus RNA-seq toolbox for fresh and frozen Johannes C. Melms, Jana Biermann, Huachao Huang, Yiping Wang, Ajay Nair, Somnath
human tumors. Nat. Med. 26, 792–802 (2020). Tagore, Igor Katsyv, André F. Rendeiro, Amit Dipak Amin. 34These authors jointly supervised
18. Hewitson, J. P. et al. Malat1 suppresses immunity to infection through promoting this work: Robert E. Schwartz, Olivier Elemento, Anjali Saqi, Hanina Hibshoosh, Jianwen Que,
expression of Maf and IL-10 in Th cells. J. Immunol. 204, 2949–2960 (2020). Benjamin Izar. ✉e-mail: jq2240@cumc.columbia.edu; bi2175@cumc.columbia.edu
Nature | Vol 595 | 1 July 2021 | 119

Article
Methods San Diego, CA) using paired-end, single-index sequencing with 28 cycles
for read 1, 8 cycles for i7 index, and 91 cycles for read 2.
Tissue collection
All tissue specimens from individuals with lethal COVID-19 (with Generating single-nucleus gene expression matrices
SARS-CoV-2 infection confirmed by reverse transcription polymerase Raw 3′ snRNA-seq data were demultiplexed using Cell Ranger (v5.0)
chain reaction (RT–PCR)) and control individuals were collected at New ‘mkfastq’ followed by ‘count’ to align the sequencing reads and gener-
York Presbyterian Hospital or Columbia University Medical Center ate a counts matrix. Transcripts were aligned to the human GRCh38
under IRB approved protocols (AAAB2667, AAAT0785, AAAS7370). reference genome, which was appended with the entire SARS-CoV-2
Appropriate consent was obtained from patients or their next of kin. genome (severe acute respiratory syndrome coronavirus 2 isolate
All procedures performed on patient samples were in accordance with Wuhan-Hu-1, complete genome, GenBank MN908947.3) as an addi-
the ethical standards of the IRB and the Helsinki Declaration and its tional chromosome to the human reference genome. Subsequently,
later amendments. Samples were selected on the basis of pathologi- the customized ‘GRCh38_SARSCoV2’ reference genome was indexed
cal review of corresponding haematoxylin and eosin (H&E)-stained using ‘cellranger_mkref’.
FFPE tissue slides showing pathological involvement of the selected
biopsy region from donors with a post-mortem incision time of less Removal of background noise in gene expression matrices
than 10 h. The donor age was 59 to more than 89 years. Tissue samples We used the ‘remove-background’ function of CellBender (v.0.2.0)
of ~1 cm3 were snap-frozen embedded in Tissue-Tek optimal cutting to remove technical ambient RNA counts and empty droplets from
temperature (OCT) compound (Sakura Finetek USA Inc., Torrance, the gene expression matrices34. Cell Ranger-generated ‘raw_feature_
CA) and stored at −80 °C until processing. For all decedents included bc_matrix.h5’ files served as input for CellBender. The parameter
in this study, affected lung tissues were removed, and additionally, for ‘expected-cells’ was obtained from the Cell Ranger metric ‘Estimated
a subset of individuals, matching tissues from kidney and heart were Number of Cells’, while the parameter ‘total-droplets-included’ was set
collected32. Seven control lung samples were collected from patients to a value between 18,000 and 24,000 to represent a point within the
without COVID-19. The dataset analysed and presented here focuses plateau of the barcode rank plot in all samples.
on lung specimens from 19 individuals who died of COVID-19 (profiled
in 20 experiments) and 7 control (non-COVID-19) individuals. Quality control and filtering
The resulting expression matrices were processed individually in R
Sample processing and preparation of single-nucleus suspensions (v.4.0.2) using Seurat (v.3.2.3)35. Filters were applied to keep nuclei with
All samples were processed in a biosafety cabinet equipped to comply 200–7,500 genes, 400–40,000 unique molecular identifiers (UMIs),
with Columbia University safety measures established for working with and less than 10% mitochondrial reads. In addition, Scrublet was applied
COVID-19 specimens. Samples were processed as described previously17 to identify and remove doublets with an expected doublet rate ranging
with the following specifications and modifications. For tissue dissociation from 4 to 9.6% based on the loading rate36. Samples containing fewer
we used Tween with salts and Tris (TST) buffer. For all wash steps we used than 1,000 nuclei after filtering were excluded from further analyses.
salt and Tris (ST) buffer, and all buffers were supplemented with 40 U/ml Filtered gene–barcode matrices were normalized with the ‘Normalize-
RNase inhibitor (Thermo Fisher Scientific, Waltham, MA). All buffers were Data’ function using ‘LogNormalize’ and the top 2,000 variable genes
pre-chilled on ice and samples were kept on ice throughout the process to were identified using the ‘vst’ method in ‘FindVariableFeatures’. Gene
further prevent RNA degradation. In brief, a fraction of the OCT-embedded expression matrices were scaled and centred using the ‘ScaleData’
snap-frozen tissue was broken off and put into a pre-cooled 50-ml tube function. Next, we performed principal component analysis (PCA)
(Corning, NY) in a large volume of ice-cold phosphate buffered saline (PBS) as well as UMAP using the first 30 principal components. UMAPs of
and inverted until the OCT was fully dissolve. Tissue was then collected by individual samples were inspected before integration.
centrifuging at 300g for 2 min at 4 °C. PBS was decanted, and the tissue was
resuspended in 2 ml cold TST buffer, mechanically dissociated using fine Integration of individual samples
scissors and pipettes with decreasing orifice size, and incubated on ice for Individual samples were integrated in Seurat using the reciprocal PCA
5–10 min. The TST was quenched with 8 ml ST buffer, and the suspension (RPCA) pipeline to remove batch effects in large datasets. The ‘SelectIn-
was filtered through a 70-μm cell strainer. The tissue/nucleus suspension tegrationFeatures’ function was applied to choose the features ranked
was pelleted by centrifuging at 500g for 5 min at 4 °C. The supernatant was by the number of datasets they were detected in. Next, the ‘FindInte-
decanted, and the nuclei were resuspended in 200–1,000 μl ST buffer, grationAnchors’ function selected a set of anchors between different
filtered through a 40-μm cell strainer attached to a fluorescence-activated samples using the top 50 dimensions from the RPCA to specify the
cell sorting (FACS) tube (Corning, NY), counted, and immediately pro- neighbour search space. Six samples were specified as a reference,
cessed for single-nucleus RNA sequencing. including three controls (C51ctr, C52ctr, C53ctr) and three COVID-19
(L01cov, L12cov, L16cov) samples. ‘IntegrateData’ was then applied to
Single-nucleus RNA library preparation and sequencing integrate the datasets using the pre-computed anchors and the inte-
Single-nucleus suspensions were counted using disposable counting grated dataset was scaled using ‘ScaleData’. PCA and UMAP dimension
chambers (Bulldog Bio, Portsmouth, NH) on a Leica DMi 1 microscope reduction based on the top 30 principal components were performed.
by a second investigator not involved in tissue processing. A total of Nearest-neighbour graphs using the top 30 dimensions of the PCA
15,000–20,000 nuclei were loaded per channel on a Chromium control- reduction were calculated and clustering was applied with a resolu-
ler using Chromium Next GEM Single Cell 3ʹ v3.1 reagents (10X Genomics, tion of 0.8. Harmony37 was run on the PCA matrix above using default
Pleasanton, CA) placed inside the bio-safety cabinet, and single-nucleus parameters with patient ID as the batch key and 10 iterations.
RNA-seq libraries were prepared per the manufacturer’s instructions
(increasing the recommended initial cDNA amplification cycles by one Cell-type identification
to account for lower amounts of RNA from nuclei compared to whole The main cell types were identified by manual annotation of differ-
cells). Single-nucleus RNA libraries were analysed and quantified using ential gene expression (DGE) between clusters. The ‘FindAllMarkers’
TapeStation D1000 screening tapes (Agilent, Santa Clara, CA) and Qubit function identified positive markers for each cluster with a minimal
HS DNA quantification kit (Thermo Fisher Scientific). Libraries were fraction of 25% and a log-transformed fold change threshold of 0.25.
pooled equimolarly and quantified using quantitative PCR. Librar- This initial labelling resulted in the identification of epithelial, endothe-
ies were sequenced on a NovaSeq 6000 with S4 flow cell (Illumina, lial, fibroblast, neuronal, myeloid, APC, mast, T/NK and B/plasma cell

populations as well as one low-quality cluster, which we removed. Next, three-gene signature and cells with a module score >0.7 were prelimi-
we split the Seurat object into subsets of the main labels and reran scal- narily labelled as DATPs. Next, we used DGE to identify additional mark-
ing, PCA, UMAP dimension reduction, clustering and DGE analysis on ers that define the DATP program. We then scored our resulting DATP
each subset. The resulting clusters were annotated manually or by using signature, including 163 genes, to the AT1 and AT2 cells and labelled all
cell-type-specific single-cell signatures from respective cell atlases, and cells with a module score of >0.4 as DATPs. T cell scores were obtained
labels were added to the main object. In addition, cell cycle phases were by using the Seurat implementation of gene set scoring with 50 bins
scored in the subsets using the ‘CellCycleScoring’ function, adjusted and a control size equal to the number of genes in the set. Upregulation
for individual cut-offs and added to the main object. Within the mye- and downregulation programs (TRM, Tact, Tmem Texh), defined by
loid subpopulation, two low-quality clusters (characterized by higher K. S. P. Devi et al. (unpublished), were used to infer T cell phenotypes.
expression of mitochondrial reads) were observed and removed, leaving The upregulation and downregulation signatures were scored sepa-
a total of 116,314 cells for downstream analyses (of 119,535 initial cells rately, and the downregulation score was subtracted cell-wise from
after QC). Signatures and canonical markers (Supplementary Table 4) the upregulation score to obtain the composite score. Effect size was
to identify airway basal, club, ciliated, goblet, mucous, AT1, and AT2 calculated using Cohen’s D (that is, the difference of means divided by
cells were obtained from Travaglini et al.38. Alveolar macrophages were the pooled standard deviation).
scored using a signature based on DGE obtained from Travaglini et al.38
and identified as AMs39 with a module score >0.15. A tuft-cell signature Diffusion component analysis
was obtained from Deprez et al.40. To further characterize the fibro- We applied diffusion maps as a nonlinear dimensionality reduction
blast population, fibroblast cells were selected using Seurat’s ‘subset’ technique to examine the major components of variation across subsets
function and reanalysed to identify the different fibroblast subtypes. of cells. We computed DCs using the ‘DiffusionMap’ function of the
The reanalysis included the standard Seurat workflow with ‘RunPCA,’ Destiny R-package (v3.3.0) with the top 30 principal components used
‘FindNeighbours,’ ‘FindClusters,’ and ‘RunUMAP’ performed on the in the k-nearest neighbours algorithm (k-NN)45. The epithelial subset
‘integrated’ assay. The number of PCA dimensions used was 15, with a consisting of airway basal, club, and goblet cells was reintegrated for
resolution parameter of 0.5. After the fibroblast cell clusters had been the DC analysis using the Seurat standard integration with 30 dimen-
obtained, the DGE in each cluster was computed with ‘FindAllMarkers’ sions and a k-neighbours filter of 50 in the ‘FindIntegrationAnchors’
on ‘RNA’ assay (Supplementary Table 9). The fibroblast subtypes were function. Samples with <50 cells were excluded from reintegration,
identified by manually curating the cluster DGE with the reported litera- which removed a total of 10 samples (one control sample and nine
ture, such as the single-cell lung atlas38, lung fibroblast atlas3, single-cell COVID-19 samples). Tuft-like cells were identified as cells with DC1
database PanglaoDB41, and Human Protein Atlas42–44. However, these values >0.015 based on an overlap with the tuft-cell signature in the
resources were based on scRNA-seq or bulk studies. Therefore, the few diffusion trajectory that dominated the first DC.
reported fibroblast subtype markers were usually not specific or had low
expression in snRNA-seq data. Therefore, we compared our subcluster Differential gene expression
DGE with the literature reported subtype DGE with shared high expres- DGE was identified by using the Seurat function ‘FindAllMarkers’ on
sion in snRNA-seq or scRNA-seq data. These manually curated lists of normalized count data to identify positive (overexpressed) markers
fibroblast-subtype-specific marker genes were used to identify fibro- in each population. The Wilcoxon rank-sum test (two-sided) was used
blast subtypes in our dataset (Supplementary Table 4). This procedure to identify differentially expressed genes between two groups of cells
was used to identify alveolar fibroblasts, adventitial fibroblasts, peri- and the log-transformed fold change was set to 0.25. The parameter
cytes, airway smooth muscle, vascular smooth muscle, and mesothelial ‘min.pct’ was set to 0.25 to assure that genes were detected at a mini-
fibroblasts. Cell clusters with high expression of COL1A1 and CTHRC1 mum fraction of 25% of cells in either of the populations. P values were
were annotated as ‘pathological fibroblasts’ because they have been adjusted using Bonferroni correction unless otherwise stated. Differen-
reported to contribute to the leading edge of fibrosis3. Clusters with tially expressed genes were plotted in violin plots using log-normalized
lower expression of COL1A1 and CTHRC1 compared to pathological expression values (natural logarithm ln(1 + x)). For heatmaps and dot
fibroblasts, but without any markers for other fibroblast subtypes in plots, expression values were log-normalized (natural logarithm
their DGE, were annotated as ‘intermediate pathological fibroblasts’. ln(1 + x)) and furthermore centred on 0 with a variance of 1 (scaled).
One cell cluster without distinct DGE was annotated as ‘other fibroblasts’.
For visualization purposes, expression scores were plotted in UMAP Differential expression of signature scores
embeddings or violin plots as log-normalized values (natural logarithm To test differential expression of three immune pathway signatures
ln(1 + x)), and in dot plots as log-normalized values (natural logarithm (type I interferon abbreviated, inflammasome receptors, and chemot-
ln(1 + x)) that were furthermore centred on 0 with a variance of 1 (scaled). axis, Supplementary Table 4), we obtained log-normalized expression
values (ln(1 + x)) for each gene in the signatures, and summed them
Cell-type frequency comparison for each signature. We then used a two-sided Wilcoxon rank-sum test
Unless otherwise noted, we calculated frequencies of cell types in each to test for differential expression of signatures in each cell type, and
sample from COVID-19 and control lungs, and compared the medians calculated log(fold change).
2
of the two groups to identify differences in frequency. Significance
was assessed using a Wilcoxon rank-sum test. Geneset enrichment
Geneset enrichment analyses were performed using the hypeR
Module scores for feature expression R-package46. The background population of genes was set to all
The ‘AddModuleScore’ function was applied to calculate the average detected genes. Geneset over-representation was determined by
expression levels of gene signatures on a single-cell level. Mouse-based hypergeometric test.
signatures to identify DATPs and primed and cycling AT2 cells were
obtained from Choi et al.25 and converted to human homologue genes. B cell chain analysis
Three genes (CLDN4, KRT8, CDKN1A) comprised the initial DATP signa- To analyse the distribution of heavy and light chains in B cells, the dataset
ture thus derived. AT1 and AT2 cells were subset from the main Seurat was subset to include only B cells. For the identification of variable chain
object and reintegrated using the Seurat standard integration with regions, we selected the highest expressed heavy and light chain gene
30 dimensions and a k-neighbours filter of 60 in the ‘FindIntegratio- of each cell that expressed both heavy (starting with IGHV) and light
nAnchors’ function. First, all AT1 and AT2 cells were scored for the (starting with IGLV or IGKV) chain-encoding genes. Next, we identified

Article
the highest expressed constant chain region among expressed genes
following the pattern ‘IGH[G, M, A, or E][number]’. The resulting pairs Differential enrichment of ligand–receptor interactions
of heavy and light chains were visualized as a heatmap using average between COVID-19 and control samples
linkage for hierarchical clustering analysis and cross-referenced with CellPhoneDB analysis of each sample identified the significantly
previously described recurrently observed combinations47. enriched ligand–receptor interactions in that sample by computing
a mean of the ligand and receptor gene expression for each ligand–
Master regulator analysis and drug target identification receptor interaction together with a corresponding P value. To find
The fibroblast regulatory network in this study was reverse-engineered ligand–receptor interactions that were differentially regulated between
from snRNA-seq data using the ARACNe-AP48,49 algorithm. We generated COVID and control conditions, we first identified the common inter-
networks for each sub-cluster and integrated the networks by taking a actions across all samples. In brief, we consolidated ligand–receptor
union of the predictions of all networks. P values of Master regulator expression for controls and COVID-19 separately by taking the median
(MR)–target interactions predicted by the networks were integrated of ligand–receptor mean expressions from 7 control samples or 20
using Fisher’s method. The final fibroblast network contained pre- COVID-19 samples (from 19 donors). The minimum value of consoli-
dictions for 1,341 transcription factors regulating 9,770 target genes dated ligand–receptor expression in COVID-19 and control samples was
through 295,546 interactions. The relative activity of each transcrip- set to 0.001 to prevent noise in low expression values from affecting
tion factor represented in the fibroblast network was inferred using the log(fold change) calculations. log(control median expression)
2
the VIPER50,51 algorithm, available as a package through Bioconduc- was subtracted from log(COVID-19 median expression) to obtain
2
tor. Conceptually, the VIPER algorithm is similar to the master regu- the log(fold change) of ligand–receptor expression in COVID-19. To
2
lator inference algorithm (MARINA)49,52, which uses the MR targets compute the P value of the log(fold change) for each interaction, we
2
inferred by the ARACNe48,49 algorithm to predict drivers of changes used an unpaired two-sided Wilcoxon rank-sum test for each interac-
in cellular phenotypes. In addition to calculating the enrichment of tion between COVID-19 and control samples. Adjusted P values were
ARACNe-predicted targets in the signature of interest, VIPER also con- obtained using th eBenjamini–Hochberg procedure. Interactions with
siders the regulator mode of action, regulator–target gene interaction log(fold change) ≥ |2| and FDR P < 0.1 were reported as the top differ-
2
confidence, and the pleiotropic nature of each target gene’s regulation. entially enriched interactions in COVID-19.
Statistical significance, including P value and normalized enrichment
score (NES), was estimated by comparison to a null model generated by Tissue preparation and processing for imaging
permuting the samples uniformly at random 1,000 times. Druggable Lung tissues (human and mouse) were fixed with 4% paraformaldehyde
proteins with VIPER-predicted50,51,53 aberrant increases in activity were (PFA) at 4 °C overnight with rotation. For paraffin sections, tissues were
ranked by their −log (Bonferroni adjusted P value). dehydrated through a 70–100% ethanol gradient and then embedded
10
in paraffin. For cryosections, tissues were sequentially incubated with
Ligand–receptor interaction inference in individual samples 20% and 30% sucrose and subsequently embedded in OCT compound.
CellPhoneDB54 is a curated repository of ligand–receptor interactions We obtaind 8–10-μm-thick cryosections using a cryostat.
along with their subunit architectures, integrated in a statistical frame-
work to infer cell-type-enriched ligand–receptor interactions between Microscopic imaging and quantification
cell types in single-cell or single-nucleus transcriptomics data. We used Paraffin sections were dewaxed and rehydrated. Antigen retrieval
CellPhoneDB to identify ligand–receptor interactions between cell types was performed by high-pressure heating with a commercial antigen
in each individual control (n = 7) and COVID-19 (n = 19) snRNA-seq dataset. unmasking retrieval solution followed by blocking with 5% normal
The ligand–receptor interactions were inferred in each patient sepa- donkey serum. For immunofluorescence staining, the sections were
rately, as by definition cell-to-cell interactions are biologically mean- then incubated with the primary antibodies listed in Supplementary
ingful only within an individual. Moreover, separate inference also Table 12 at 4 °C overnight. Cryosections were washed twice with PBS,
prevents spurious interactions from being inferred between patients and blocked with 5% normal donkey serum, followed by incubation
with heterogeneous disease or health statuses. After identifying and with primary antibodies shown in Supplementary Table 12 at 4 °C
annotating different cell types in our snRNA-seq datasets, we followed overnight. Conjugated secondary antibodies (1:500) were added to
the recommended procedures for the preparation of input files for local the sections and incubated for 2 h at room temperature. Nucleus were
implementation of CellPhoneDB v.2.0.054. In brief, for each individual stained with DAPI, and images were captured with a Zeiss LSM T-PMT
sample, QC-filtered raw counts matrices were normalized to counts per confocal laser-scanning microscope (Carl Zeiss) and Zen 2012 SP1
10,000 and metadata files were obtained from the respective cell-type (black edition) software (Zeiss). Immunohistochemistry for C4d was
annotations. CellPhoneDB analysis was performed with the ‘cellphonedb performed on a Leica Bond 3 automated staining platform. In brief,
method statistical_analysis’ command with default parameters. paraffin sections including both healthy control lung and COVID-19
lung tissues were treated with BOND Epitope Retrieval Solution 2 (Leica)
Cell–cell interaction differences between COVID-19 and control for 20 min and they were incubated with a C4d antibody for 30 min.
samples Immunohistochemistry signals were developed with the Bone Polymer
CellPhoneDB analysis of each sample identified the number of ligand– Refine Detection kit (Leica) with treatment with post primary polymer
receptor interactions between all nine major cell-types in that sample. for 20 min and DAB chromogen for 10 min. For quantification, cells
We analysed these cell–cell interaction counts between control donors were counted by a blinded investigator using tiled stitched 20× images
(n = 7) and individuals with COVID-19 (19 individuals, 20 samples) to iden- from more than five sections per mouse and included at least three
tify the differences in cellular cross-talk between COVID-19 and control individual lobes or were from representative areas of at least three
lungs. The median cell–cell interaction values from all the control samples human control lungs and COVID-19 lungs. Images were processed and
formed the overall control lung cell–cell interaction counts. Similarly, analysed using ZEN blue 2.3 (Zeiss) and Adobe Photoshop Creative
the overall COVID-19 lung cell–cell interaction counts were the median Suite 6 (Adobe) software in a blinded fashion. DATPs were detected
from all the COVID-19 samples. The overall control and COVID-19 lung with co-immunostaining for pro-SPC and KRT8 or HTII-280 and CLDN4.
interaction counts were visualized as an interactome using the ‘igraph’ R DATP percentages were determined by counting KTR8hi pro-SPC+ cells
package with circle layout, where the edge width between two cell types over pro-SPC+ cells or CLDN4+ cells over HTII-280+ cells. Macrophages
was proportional to the number of interactions between them and the size were quantified by counting the total number of CD45+CD64+ cells
of a cell-type circle was proportional to its frequency in the snRNA-seq. over CD45+ cells. CHAT+ tuft cells were quantified by counting the total

number of CHAT+ cells over DAPI+ airway nuclei (for airway tuft cells) package (version 0.3.9)58. Representative regions within the ROIs were
or per mm2 of lung parenchyma. displayed as false-colour images by normalizing the signal intensity
to the unit scale after clipping the signal below and above the 3rd and
Multiplexed immunofluorescence 98th percentiles, respectively. Finally, a Gaussian filter with sigma of
Multiplexed immunofluorescence staining of lung tissue from patients one pixel (one micrometre) was applied to the images.
who died of COVID-19 and control individuals was performed using
CD4, CD8, CD19, CD103, CD163 and granzyme B (GZMB) antibodies Sirius red staining and fibrosis scoring
(Supplementary Table 12) with the Opal 7-colour IHC kit (Akoya Biosci- Paraffin-embedded lung sections were dewaxed, rehydrated and stained
ence) on a Leica Bond RX automated stainer (Leica Biosystems). FFPE for 1.5 h with a picrosirius red solution (1.3% picric acid, 1% fast red and
tissue sections (5 μm) were baked for 2 h at 60 °C, followed by automatic 1% fast green). Four or five fields at 4× magnification were taken using
deparaffinization, rehydration, and antigen retrieval in BOND Epitope a polarized light filter on an Olympus IX71S1F-3 microscope with QCap-
Retrieval Solution 2, pH 9 (Leica Biosystems) for 30 min at 95 °C. Immu- ture Suite Plus (v3.1.3.10) software. Images were quantified (percentage
nofluorescence staining with Opal and tyramide signal amplification of Sirius red area/total area) using Adobe Photoshop (v 11.0). Pearson
(TSA) were performed in six cycles. In each cycle, the tissue was incu- correlations between fibrosis score and days from symptom onset to
bated sequentially with a primary antibody for 30 min at room tem- death were calculated for 16 of 19 patients with COVID-19 for whom sam-
perature, the secondary antibody conjugated to polymeric horseradish ples were available and time from symptom onset to death was reported.
peroxidase (HRP), an Opal fluorophore in TSA buffer, and BOND Epitope
Retrieval Solution 1, pH 6 (Leica Biosystems) for 20 min at 95 °C to strip αSMA immunohistochemistry
the tissue-bound primary–secondary antibody complexes before the Antigen retrieval of dewaxed and rehydrated paraffin-embedded lung
next staining cycle. After nuclear counterstaining with DAPI, slides were sections was performed with citrate pH 6, blocked with 3% BSA and incu-
coverslipped with Vectrashield HardSet Antifade mounting medium bated with anti-αSMA-FITC (Sigma, F3777) overnight at 4 °C. After incu-
(Vector Laboratories) and 12–15 areas per slide were imaged using the bation with a biotin-anti-FITC antibody (Abcam, ab6655), detection was
Vectra 3 automated multispectral microscope (Akoya/PerkinElmer) with performed using the Vectastatin Elite ABC-HRP kit (Vector Laboratories,
Vectra 3.0.5 software. Regions of interest were chosen by the patholo- SP-2001) with the DAB Peroxidase Substrate kit (Vector Laboratories,
gist for multispectral imaging (MSI) at 20× magnification and spectral SK-4100), followed by counterstaining with haematoxylin. All reagents
unmixing using the InForm v2.4.6 software (Akoya). Demultiplexed and dilutions are listed in Supplementary Table 12. All 7 control slides
images were exported as 32-bit TIFF files for further analysis. and 17 available slides from COVID-19 lungs were included in the analysis.
Slides were scanned using a Leica SCN400 slide scanner with Leica Scanner
Multiplexed image analysis Console software (v102.0.7.5) and quantified using the Leica Aperio Imag-
All images were analysed and visualized using QuPath55. We used the eScope software (v12.4.3.5008) on at least five fields at 10× magnification.
highest resolution for all described steps. The QuPath project files
and additional scripts are available at https://github.com/IzarLab/ Mice
CUIMC-NYP_COVID_autopsy_lung/tree/main/code/Vectra_image_ Mouse studies were approved by the Columbia University Medical
analysis. First, images were loaded, renamed and segmented using Center (CUMC) Institutional Animal Care and Use Committees (IACUC).
‘WatershedCellDetection’ based on DAPI intensity with a cell expansion The Pou2f3−/− mouse strain was described previously59. All mice were
of 4 μm. Further parameter settings for these steps can be found in maintained on a C57BL/6 and 129SvEv mixed background and housed
the ‘Load_and_segmentation.groovy’ script. Next, we created classes in the mouse facility at Columbia University according to institutional
and the corresponding classifiers for each of the six markers of inter- guidelines. The facility provides a 12-h light–dark cycle, 18–23 °C room
est: CD4, CD19, GZMB, CD103, CD8 and CD163. The thresholds for temperature and 40–60% humidity. All animal studies used a minimum
the individual classifiers (‘ClassifyByMeasurementFunction’) were of three mice per group and sample size was based on pilot experiments
automatically calculated and adjusted for each patient on the basis of and previous experience. Mice were randomized to experiments and
visual inspection of the mean marker expression. If no patient-specific 8–12-week-old animals of both sexes were used in equal proportions.
classifier was created, the classifier with the ending ‘_04_A6.json’ was The investigators were not blinded to allocation during experiments.
used. All classifiers can be found in the object classifiers folder as json
files. Once performed for all images, the individual assignments for Influenza infection mouse model
each single cell were exported to a CSV file for downstream analysis A total of 260 plaque forming units (pfu) of influenza A/Puerto
and boxplot visualization. Rico/8/1934 H1N1 (PR8) virus (a gift from Dr. Jie Sun at Mayo Clinics,
Cleveland) dissolved in 40 μl RPMI medium was pipetted onto the
Imaging mass cytometry nostrils of anaesthetized mice, whereupon mice aspirated the fluid
Imaging mass cytometry data from post-mortem lung tissue of patients directly into their lungs. For all procedures, administration of the same
with lung infections and otherwise healthy donors was used28. The data- volumes of vehicle (RPMI medium) was used as control.
set comprised 237 images from 23 donors, containing 664,006 single
cells for which cell-type identities were derived from the intensity of 36 Flow cytometry analysis
markers. All analyses were conducted in Python v3.8.2 with the follow- Fourteen days after infection, mice were euthanized and transcardially
ing programs: numpy v1.18.5, scipy v1.4.1, Tifffile 2020.6.3, Networkx perfused with 10 ml cold PBS. The lungs were then perfused with 1 ml
v2.5, Scikit-image v0.17.2, Pingouin v0.3.7, and Scanpy v1.6.0. Single PBS with 2 mg/ml Dispase I and 0.5 mg/ml DNase I and incubated in
cells were labelled as positive for IL-6 or IL-1β based on their z-score 5 ml of the above buffer for digestion with gentle shaking for 60 min
of intensity using Gaussian mixture models (scikit-learn56, version at room temperature. Lung lobes were removed and physically dis-
0.23.0) using model selection based on the Davies–Bouldin index57. sociated, followed by filtering through a 40-μm cell strainer. Cells
The number of cells positive for a marker in each ablated region of were pelleted and resuspended in 1 ml lyse RBC buffer followed by
interest (ROI) was normalized by its area, and mean values per disease incubation on ice for 5 min to remove red blood cells. After washing
group and cell type across all ROIs were visualized as bar charts. To with FACS buffer (5% FBS, 0.2 mM EDTA in PBS), single cells were col-
assess the significance of changes across both disease groups and cell lected and immunostained with Fc blocking antibody (5 μg/ml) and a
types, we used a two-sided Mann–Whitney U-test and adjusted P values live/dead cell stain kit at room temperature for 10 min. Cells were then
with the Benjamini–Hochberg FDR adjustment using the pingouin washed and incubated with the following antibodies for one hour: PE/

Article
cyanine7 anti-mouse CD45 (1:100), FITC anti-mouse CD64 (1:100), and 40. Deprez, M. et al. A single-cell atlas of the human healthy airways. Am. J. Respir. Crit. Care
APC anti-mouse F4/80 (1:100). Samples were analysed on LSR II (BD, Med. 202, 1636–1645 (2020).
41. Franzén, O., Gan, L. M. & Björkegren, J. L. M. PanglaoDB: a web server for exploration of
Biosciences) with four lasers (405 nm, 488 nm, 561 nm, and 635 nm). mouse and human single-cell RNA sequencing data. Database 2019, baz046 (2019).
Data were analysed using FlowJo software (Treestar). 42. Uhlén, M. et al. Tissue-based map of the human proteome. Science 347, 1260419 (2015).
43. Thul, P. J. et al. A subcellular map of the human proteome. Science 356, eaal3321 (2017).
44. Uhlen, M. et al. A pathology atlas of the human cancer transcriptome. Science 357,
Quantitative RT–PCR (qRT–PCR)
eaan2507 (2017).
To quantitively measure the indicated cytokines, human lung tissue 45. Angerer, P. et al. destiny: diffusion maps for large-scale single-cell data in R.
Bioinformatics 32, 1241–1243 (2016).
samples (three donors for both healthy and COVID-19 samples) or
46. Federico, A. & Monti, S. hypeR: an R package for geneset enrichment workflows.
mouse lungs (a minimum of three mice per genotype) were individually Bioinformatics 36, 1307–1308 (2020).
homogenized in Trizol and total RNA was extracted using an RNeasy 47. Yuan, M. et al. Structural basis of a shared antibody response to SARS-CoV-2. Science
369, 1119–1123 (2020).
Plus Mini Kit (Qiagen) following the manufacturer’s instructions. cDNA
48. Basso, K. et al. Reverse engineering of regulatory networks in human B cells. Nat. Genet.
was synthesized using the Superscript-IV First-Strand Synthesis System 37, 382–390 (2005).
(Invitrogen) and the gene-specific primers were mixed with cDNA tem- 49. Lachmann, A., Giorgi, F. M., Lopez, G. & Califano, A. ARACNe-AP: gene network reverse
engineering through adaptive partitioning inference of mutual information.
plates and iTaq Universal SYBRR Green supermix (Bio-Rad). qPCR was
Bioinformatics 32, 2233–2235 (2016).
carried out on a CFX Connect real-time PCR detection system (Bio-Rad) 50. Alvarez, M. J. et al. Functional characterization of somatic mutations in cancer using
in a total volume of 20 μl. Three technical and biological replicates were network-based inference of protein activity. Nat. Genet. 48, 838–847 (2016).
51. Ding, H. et al. Quantitative assessment of protein activity in orphan tissues and single
performed. Relative fold change was determined by normalizing to
cells using the metaVIPER algorithm. Nat. Commun. 9, 1471 (2018).
Actb mRNA for mouse or to GAPDH mRNA for human. The primers for 52. Lefebvre, C. et al. A human B-cell interactome identifies MYB and FOXM1 as master
qPCR are listed in Supplementary Table 13. regulators of proliferation in germinal centers. Mol. Syst. Biol. 6, 377 (2010).
53. Alvarez, M. J. et al. A precision oncology approach to the pharmacological targeting of
mechanistic dependencies in neuroendocrine tumors. Nat. Genet. 50, 979–989 (2018).
Statistical analysis of imaging and qRT–PCR data 54. Efremova, M., Vento-Tormo, M., Teichmann, S. A. & Vento-Tormo, R. CellPhoneDB:
Imaging and qPCR data are presented as means with s.d. of meas- inferring cell–cell communication from combined expression of multi-subunit ligand–
receptor complexes. Nat. Protocols 15, 1484–1506 (2020).
urements unless stated otherwise. Individual values are plotted and
55. Bankhead, P. et al. QuPath: open source software for digital pathology image analysis.
represent independent biological samples unless stated otherwise. Sci. Rep. 7, 16878 (2017).
Statistical differences between samples were assessed with unpaired 56. Pedregosa, F. et al. Scikit-learn: machine learning in Python. J. Mach. Learn. Res. 12,
2825–2830 (2011).
Student’s t-test using GraphPad Prism 9.0 (GraphPad Software Inc.,
57. Davies, D. L. & Bouldin, D. W. A cluster separation measure. IEEE Trans. Pattern Anal. Mach.
San Diego, CA). P values below 0.05 are considered significant. Intell. 1, 224–227 (1979).
For multiplexed immunofluorescent images, cell fractions (percent- 58. Vallat, R. Pingouin: statistics in Python. J. Open Source Softw. 3, 1026 (2018).
59. Gerbe, F. et al. Intestinal epithelial tuft cells initiate type 2 mucosal immunity to helminth
age of total or percentage of parental population) were computed
parasites. Nature 529, 226–230 (2016).
for each field of view individually using Excel 16.45 (Microsoft). After
calculating the mean on a per sample basis, we plotted values using
GraphPad Prism 9.0 (GraphPad Inc. San Diego, CA) and presented them Acknowledgements We are grateful to all donors and their families. This work is part of the
Human Cell Atlas (www.humancellatlas.org/publications). We thank J. Bhattacharya, I. Tabas,
as means with s.d. of measurements. Statistical differences between A. Tall and S. Roth for discussions. B.I. is supported by National Institute of Health (NIH)
samples were assessed with unpaired Student’s t-test using GraphPad National Cancer Institute (NCI) grants K08CA222663, R37CA258829 and U54CA225088, a
Prism 9.0 (GraphPad Software Inc., San Diego, CA). P values below 0.05 FastGrant, the Burroughs Wellcome Fund Career Award for Medical Scientists and the Louis V.
Gerstner, Jr. Scholars Program. J.Q. is supported by R01HL152293 and R01HL132996. H. Huang
are considered significant. is supported by the Department of Defense (DoD) Discovery Award W81XWH-21-1-0196. A.R. is
supported by an NCI T32CA203702 grant. O.E. is supported by Volastra, Janssen and Eli Lilly
Reporting summary research grants, NIH grants UL1TR002384, R01CA194547, and Leukemia and Lymphoma
Society SCOR 7012-16, SCOR 7021-20 and SCOR 180078-02 grants. R.E.S. is supported by NIH
Further information on research design is available in the Nature grants NCI R01CA234614, NIAID R01AI107301, NIDDK R01DK121072 and RO3DK117252, and is
Research Reporting Summary linked to this paper. an Irma Hirschl Trust Research Award Scholar. D.S. is a Damon Runyon Fellow supported by the
Damon Runyon Cancer Research Foundation (DRQ-03-20). This research was funded in part
through the NIH Support Grant S10RR027050 for flow cytometry analysis and the NIH/NCI
Cancer Center Support Grant P30CA013696 at Columbia University Genetically Modified
Data availability Mouse Model Shared Resource, Molecular Pathology Shared Resource and its Tissue Bank.
Processed data are available via the single-cell portal: https://singlecell.
broadinstitute.org/single_cell/study/SCP1219. Processed data are also Author contributions B.I. provided overall supervision. J.C.M., H. Huang, J.Q. and B.I. conceived
this project. J.C.M., H. Huang, A.D.A., A.F., Y.F., H.R., M.G.C., Y.B., X.V.G., M.R., S.W.C., P.H., A.E.K.
deposited in GEO with accession number GSE171524. Raw data are
and A.S.H performed experiments. J.C.M., J.B., H. Huang, Y.W., A.N., S.T., A.F.R., D.S., C.J.F.,
available on the Broad Data Use and Oversight System: https://duos. A.D.A., A.M.L. and G.A.A. performed analyses. I.K., A.B., J.H.L., C.M., S.M.L., A.D.P., E.Z., G.S.M.,
broadinstitute.org (study ID DUOS-000130). Source data are provided A.S. and H. Hibshoosh oversaw and performed tissue collection, and performed pathological
review of tissues. E.J.T. facilitated rapid autopsy specimen collection. D.T.M., M.F.B., N.A., M.S.-F.,
with this paper.
S.F.B., R.E.S. and O.E. provided signatures, materials and data. R.F.S., R.E.S., O.E. and J.Q.
performed coordination of specific analyses and experiments. R.F.S. oversaw fibroblast
experiments and analyses. R.E.S. and O.E. oversaw tissue mass cytometry analysis. J.Q. oversaw
Code availability in vivo studies. D.S., C.J.F. and A.M.L. contributed equally. J.C.M., H. Huang, A.D.A., J.Q. and B.I.
wrote the manuscript. All authors reviewed and approved the final manuscript.
Code is publicly available at https://github.com/IzarLab/CUIMC-NYP_
COVID_autopsy_lung.
Competing interests B.I. is a consultant for Merck and Volastra Therapeutics. O.E. is a scientific
advisor and equity holder in Freenome, Owkin, Volastra Therapeutics and OneThree Biotech.
R.E.S. is a member of the scientific advisory board of Miromatrix Inc. and is a speaker and
34. Fleming, S. J., Marioni, J. C. & Babadi, M. CellBender remove-background: a deep
consultant for Alnylam Inc. D.T.M. is a consultant for LASE Innovation, Inc. S.F.B. owns equity in,
generative model for unsupervised removal of background noise from scRNA-seq
receives compensation from, and serves as a consultant for and on the Scientific Advisory
datasets. Preprint at https://doi.org/10.1101/791699 (2019).
Board and Board of Directors of Volastra Therapeutics Inc. The other authors declare no
35. Stuart, T. et al. Comprehensive integration of single-cell data. Cell 177, 1888–1902.e21 (2019).
competing interests.
36. Wolock, S. L., Lopez, R. & Klein, A. M. Scrublet: computational identification of cell
doublets in single-cell transcriptomic data. Cell Syst. 8, 281–291.e9 (2019).
37. Korsunsky, I. et al. Fast, sensitive and accurate integration of single-cell data with Additional information
Harmony. Nat. Methods 16, 1289–1296 (2019). Supplementary information The online version contains supplementary material available at
38. Travaglini, K. J. et al. A molecular cell atlas of the human lung from single-cell RNA https://doi.org/10.1038/s41586-021-03569-1.
sequencing. Nature 587, 619–625 (2020). Correspondence and requests for materials should be addressed to J.Q. or B.I.
39. Mould, K. J., Jackson, N. D., Henson, P. M., Seibold, M. & Janssen, W. J. Single cell RNA Peer review information Nature thanks Christopher Mason, Michael Matthay and the other,
sequencing identifies unique inflammatory airspace macrophage subsets. JCI Insight 4, anonymous, reviewer(s) for their contribution to the peer review of this work.
126556 (2019). Reprints and permissions information is available at http://www.nature.com/reprints.

Extended Data Fig. 1 | Patient information and alternative batch b, Effect of PMI on clustering. c, Cell-type labels overlaid on UMAP embedding
correction. a, Basic demographics of patients with COVID-19 and control resulting from the batch-corrected PCA matrix using Harmony (see Methods).
donors. *Decedents with concurrently profiled heart and/or kidney tissue in d, Same embedding as in c with annotation of COVID-19 and control groups.
companion study32. †Decedent with two independent lung specimens profiled.

Article
Extended Data Fig. 2 | Changes in cellular composition. a, Fraction of cell cells only. Control, n = 7 donors; COVID-19, n = 19 donors examined over 20
types in COVID-19 and control lungs across all cells (intermediate granularity). experiments. Middle line, median; box edges, 25th and 75th percentiles;
b, Fraction of cell types in COVID-19 and control lungs among non-immune cells whiskers, most extreme points that do not exceed ±1.5 × IQR. Wilcoxon
only. c, Fraction of cell types in COVID-19 and control lungs among immune rank-sum test.

Extended Data Fig. 3 | Effect of sex on cellular composition and host rank-sum test. c, d, log-normalized and scaled expression (see Methods) of
receptor expression. a, b, Cell fractions in female and male individuals for selected receptors or putative receptors and proteases or putative proteases
control (a; n = 7 donors) and COVID-19 lungs (b; n = 19 donors examined over 20 involved in SARS-CoV-2 entry in different cell types in control samples from
experiments). Middle line, median; box edges, 25th and 75th percentiles; female and male donors. Dot size indicates fraction of cells and colour
whiskers, most extreme points that do not exceed ±1.5 × IQR. Wilcoxon indicates expression level. e, f, As in c, d for from COVID-19 lungs.

Article
Extended Data Fig. 4 | Global changes in myeloid cells. a, Quantification of DCs with annotation of control and COVID-19 lung samples. h, First three DCs
cells with CD163+ staining as percentage of all cells in a subset of control and with expression of the alveolar macrophage signature. i, Heatmap of top
COVID-19 samples (n = 4 donors per group). Mean ± s.d., t-test. b, c, UMAP differentially regulated genes among indicated myeloid sub-populations. Left
embedding with myeloid cell-type assignment (b) and group assignment (c). bar indicates genes that were differentially regulated in the respective cell
d–f, Expression scores (log-normalized) for monocyte, macrophage and types. Top lanes indicate cell type and group. Rows indicate log-normalized
alveolar macrophage signatures in same UMAP embedding as b, c. g, First three and scaled expression of genes (see Methods).

Extended Data Fig. 5 | Differential gene expression in alveolar (log-normalized) in alveolar macrophages from controls and COVID-19 tissues.
macrophages. a, Heatmap of top differentially regulated genes Wilcoxon rank-sum test with Bonferroni adjusted P value indicated on top.
(log-normalized and centred, see Methods) among indicated alveolar c, Expression of AXL (log-normalized) among major cell types. Expression of
macrophages in COVID-19 and control samples. Top lane indicates cell type and this gene was nearly exclusive to fibroblasts and myeloid and epithelial cells.
group. Rows indicate expression of genes. b, Violin plot of AXL expression

Article
Extended Data Fig. 6 | See next page for caption.

Extended Data Fig. 6 | Inferred immunoglobulins in plasma cells. a, b, UMAP control donors alone (Supplementary Table 6). g, As in e, but demonstrating
embedding of cells within the B/plasma cell cluster (a) and corresponding isotype usage in patients with COVID-19 (corresponding to Fig. 3e, f; shown are
group assignment (b). c, Selected genes that define cells within the B/plasma the top 20 commbinations; complete list in Supplementary Table 6).
cell cluster. Dot size indicates fraction of cells and colour indicates log- h, Frequency (y-axis) of variable heavy chains (x-axis) in COVID-19 and control
normalized and scaled expression level (see Methods). d, Heatmap illustrating samples. i, As in h, but for variable light chain usage. j, Frequency (y-axis) of
the number of cells with combinations of variable heavy (x-axis) and light variable heavy chains (x-axis) on a per-donor basis. k, As in j, but for variable
(y-axis) chains recovered in plasma cells across all patients. Average linkage light chain usage. l, Exemplary H&E-stained image (n = 19 donors evaluated)
was used for hierarchical clustering analysis. The colour of each square with coloured outlines indicating different immune cell types. Scale
indicates the number of cells detected for each specific pair (colour key). e, As bar, 100 μm. m, C4d immunohistochemistry in representative control (left)
in d, but indicating the number of control samples with each combination and COVID-19 (right) samples (n = 6 donors per group). Scale bar, 100 μm.
detected (Supplementary Table 6). f, As in e, but indicating isotype usage in

Article
Extended Data Fig. 7 | Activation, residency and dysfunction cell states in COVID-19. Middle line, median; box edges, 25th and 75th percentiles; whiskers,
T cells. a, Expression of selected genes in cells of the T/NK cell compartment. most extreme points that do not exceed ±1.5 × IQR. Wilcoxon rank-sum test.
Dot size indicates fraction of cells and colour indicates expression level. Cohen’s D is indicated between the whiskers for each comparison (COVID-19
b, Quantification of cells with CD4+ staining as percentage of all cells (y-axis) in versus control). h, Quantification of CD4+GZMB+ T cells as percentage of CD4+
control and COVID-19 lungs (n = 4 donors per group). c, As in b, but for CD8+ T cells (y-axis) in control and COVID-19 lungs (n = 4 donors per group). i, As in h,
T cells. Mean ± s.d., t-test. d–g, Expression of different program scores (tissue but for CD8+ T cells. Mean ± s.d., t-test. j, k, Representative multiplexed
residency memory program, activation score, memory score and exhaustion immunofluorescence of lung tissue from a patient with COVID-19 with a pure
score, all from K. S. P. Devi et al. (unpublished); see Methods) in CD4+ T cells myeloid infiltrate (j) or with a mixed myeloid and lymphoid infiltrate (k; n = 4
(left) and CD8+ T cells (right) among control donors and individuals with donors per group). Scale bars, 200 μm.

Extended Data Fig. 8 | See next page for caption.

Article
Extended Data Fig. 8 | DATPs and lung regeneration. a, Expression of see Methods), and effect of PMI (n). o, Gene set enrichment analysis in DATPs
selected, previously established cell-type-specific signatures (y-axis) in cell (compared to AT1 and AT2 cells). Rows indicate pathways in descending order
types defined in this study (x-axis). Dot size indicates fraction of cells and of enrichment or significance (see key); x-axis indicates FDR. p, Inference of
colour indicates expression level. b, c, Expression of selected genes (y-axis) in G2/M and S phase of individual DATPs (dots) (see Methods). q, Representative
different cell types (x-axis), highlighting high expression of B2M in cycling immunofluorescence staining (DATP marker CLDN4 and AT2 cell marker
epithelial cells (b) and collagen genes in ECMhigh epithelial cells (c). d, Fraction HTII-280) in control and COVID-19 lung tissue sections. Dashed boxes indicate
of KI67+ cells among pro-SPC+ cells in structurally preserved versus damaged areas highlighted to the right of each image. Scale bar, 50 μm. r, s, Quantification
areas (n = 3 distinct areas each) from a COVID-19 lung. Mean ± s.d., t-test. of KRT8+ (r) and CLDN4+ (s) cells in a subset of tissue sections from control and
e–g, UMAP embedding of alveolar epithelium and expression of selected genes COVID-19 lungs. Mean ± s.d., t-test. q–s, Control, n = 3 donors; COVID-19, n = 4
that define the DATP signature. h, Composite expression of the three-gene donors. t, Coefficient of determination (R2) of days from symptom onset to
DATP signature. i, Expression of the refined DATP signature (see Methods). death and AT2/AT1 ratio. Error bands, 95% standard error interval on the
j–n, First three DCs showing group assignment (j), cell or cell-state assignment Pearson correlation (n = 18 donors).
(k), expression of AT2 signature (l), AT1 signature (m; log-normalized,

Extended Data Fig. 9 | See next page for caption.

Article
Extended Data Fig. 9 | Cellular sources of inflammatory cytokines. f, Quantification of IL-6 across across healthy and disease conditions and cell
a, Average frequency of cell types expressing IL-1β across healthy and disease types, including separation of patients with early death (within 14 days of onset
conditions. b, Quantification of IL-1β across cell types in healthy and disease of COVID-19 symptoms) and late death (within 30 days of onset of COVID-19
conditions. Each dot represents a single region of interest (ROI). symptoms). g, Expression of selected manually curated gene sets of
c, Quantification of IL-1β across healthy and disease conditions and cell types, chemotaxis, inflammasome receptors and type I interferon (response) genes
including separation of patients with early death (within 14 days of onset of across different cell types (y-axis). Dot size indicates significance and colour
COVID-19 symptoms) and late death (within 30 days of onset of COVID-19 indicates expression level (log(fold change)). h, qRT–PCR comparing IFNA1,
2
symptoms). d, Average frequency of cell types expressing IL-6 across healthy IFNA2, IFNB1, and IL-6 mRNA levels in COVID-19 and control lungs (n = 3 donors
and disease conditions. e, Quantification of IL-6 across cell types in healthy and for each group). Mean ± s.d., t-test.
disease conditions. Each dot represents a single region of interest (ROI).

Extended Data Fig. 10 | Identification of ectopic tuft-like cells. a–c, First f, g, Representative immunofluorescence staining of control lungs (f; two
three DCs of airway epithelial cells with group annotation with cell-type areas) and COVID-19 (g; airway and parenchyma) for KRT5 and CHAT. Arrows
assignment (a), group assignment (b) and indicating expression of tuft cell indicate CHAT+ cells. Scale bar, 50 μm. h, Quantification of CHAT+ cells in the
signature (c) in the same projections. d, Expression of previously established upper airway epithelium of control and COVID-19 lungs. Mean ± s.d., t-test.
signatures identifying cell types in cell types assigned in this study. Dot size i, Quantification of CHAT+ cells in the alveolar epithelium of control and
indicates fraction of cells and colour indicates expression level COVID-19 lungs. Mean ± s.d., t-test. j, k, Immunofluorescence staining for KRT5
(log-normalized and scaled, see Methods). e, Expression of selected and POU2F3 of control lungs (j) and COVID-19 lungs (k), including upper airway
cell-type-specific signatures of airway and alveolar epithelium from previous (left) and parenchyma (right). White arrows indicate POU2F3+ cells. Scale
studies in cells identified as tuft-like cells in this study. Signatures in bars, 50 μm. f–k, n = 3 donors per group.
descending order of enrichment or significance. Colour indicates significance.

Article
Extended Data Fig. 11 | See next page for caption.

Extended Data Fig. 11 | Role of tuft cells in macrophage infiltration in CD45+CD64+F4/80+ cells. g, Identification of CD64+F4/80+ cells (based on
mouse viral pneumonia model. a, Immunofluorescence staining for SCGB1A1 gating strategy in f) in wild-type (left) and Pou2f3−/− mice (right) 14 days after
and DCLK1 of proximal (left) and distal (right) airway from wild-type (WT) mice infection with H1N1. h, Quantification of flow-cytometric determination of
at baseline. n = 3 mice per group. Arrow, DCLK1+ cell. Scale bar, 50 μm. b, As in a, CD45+CD64+F4/80+ cells as percentage of CD45+ cells in Pou2f3−/− relative to
but in wild-type (left) and Pou2f3−/− mice 14 days after infection with H1N1 (PR8). wild-type mice (n = 3 per group). Mean ± s.d., t-test. i, qRT–PCR comparing
c, Quantification of tuft cells as percentage of DCLK1+ cells in Pou2f3−/− relative mRNA expression of indicated chemokines and cytokines in Pou2f3−/−
compared to wild-type mice. Mean ± s.d., t-test. b, c, n = 4 mice per group. and wild-type mice 14 days after infection with H1N1 (n = 3 per group).
d, Immunofluorescence staining for CD45 and CD64 of lung parenchyma from Mean ± s.d., t-test. j, As in i, but 44 days after infection with H1N1 (n = 3 per
wild-type (left) and Pou2f3−/− (right) mice 14 days after infection with H1N1 group). k, Exemplary immunofluorescence staining (n = 3 mice per group) for
(PR8). Arrows indicate CD45+CD64+ macrophages. Scale bar, 50 μm. KRT5 and DCLK1 in wild-type mouse 90 days after infection. Arrows indicate
e, Quantification (CD45+CD64+ cells among CD45+ cells) as percentage in DCLK1+ cells. Scale bar, 50 μm. l, As in i, j, but comparing expression of
Pou2f3−/− mice compared to wild-type mice 14 days after infection with H1N1. indicated chemokines and cytokines in control donors and patients with
Mean ± s.d., t-test. d, e, n = 3 mice per group. f, Gating strategy to identify COVID-19 (n = 3 donors per group). Mean ± s.d., t-test.

Article
Extended Data Fig. 12 | See next page for caption.

Extended Data Fig. 12 | Role of fibroblasts, potential drug targets and lung samples. The size of the circle corresponds to the frequency of the
model of lethal COVID-19. a, b, Exemplary αSMA immunohistochemical respective cell type and the thickness of the lines connecting circles indicates
staining of tissue from control (a; sample C56; n = 7 donors) and COVID-19 the absolute number of interactions. i, Differential enrichment (COVID-19
samples (b; samples L05cov and L06cov; n = 17 donors). Scale bars, 500 μm. versus control samples) of specific ligand–receptor interactions (rows)
c, Percentage of α-SMA+ cells per total area (n as in a, b). Mean ± s.d., t-test. between two different cell types (columns). Dot colour indicates
d, Exemplary Sirius red staining of control (left, n as in a) and COVID-19 (right, n log(fold change) of inferred ligand–receptor expression in COVID-19
2
as in b) samples. Scale bar, 600 μm. e, Detailed annotation of fibroblasts in this compared to control lungs (unpaired two-sided Wilcoxon rank-sum test); dot
study and selected marker genes. Dot size indicates fraction of cells and colour size is inversely correlated with Benjamini–Hochberg adjusted P
indicates expression level (log-normalized and scaled). f, Fractions of cell types (see Methods). j, Inferred protein activity (rows) among cells corresponding to
among all cells in COVID-19 (n = 19 donors examined over 20 experiments) and pathological fibroblasts, intermediate pathological fibroblasts, and non-
control lungs (n = 7 donors). Middle line, median; box edges, 25th and 75th pathological fibroblasts (columns). Proteins with high activity in pathological
percentiles; whiskers, most extreme points that do not exceed ±1.5 × IQR. fibroblasts are highlighted. k, Model summarizing potential mechanisms that
Wilcoxon rank-sum test. g, h, Inferred cell-to-cell interactions among major cell contribute to morbidity and mortality in patients with COVID-19, focusing on
types (indicated as circles connected by lines) in control (g) and COVID-19 (h) impaired cellular regeneration and rapidly ensuing fibrosis.