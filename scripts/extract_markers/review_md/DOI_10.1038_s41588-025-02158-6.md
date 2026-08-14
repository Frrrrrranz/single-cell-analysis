nature genetics
Article https://doi.org/10.1038/s41588-025-02158-6
Longitudinal single-cell multiomic
atlas of high-risk neuroblastoma
reveals chemotherapy-induced tumor
microenvironment rewiring
Received: 7 September 2024 A list of authors and their affiliations appears at the end of the paper
Accepted: 7 March 2025
High-risk neuroblastoma, a leading cause of pediatric cancer mortality,
Published online: 14 April 2025
exhibits substantial intratumoral heterogeneity, contributing to therapeutic
Check for updates resistance. To understand t um or m ic ro en vi ro nment evolution during
therapy, we longitudinally profiled 22 patients with high-risk neuroblastoma
before and after induction chemotherapy using single-nucleus RNA and
ATAC sequencing and whole-genome sequencing. This revealed profound
shifts in tumor and immune cell subpopulations after therapy and identified
enhancer-driven transcriptional regulators of neuroblastoma neoplastic
states. Poor outcome correlated with proliferative and metabolically active
neoplastic states, w h e re as m o r e differentiated neuronal-like states predicted
better prognosis. Proportions of mesenchymal neoplastic cells increased
after therapy and a high proportion correlated with a poorer chemotherapy
response. Macrophages significantly expanded towards pro-angiogenic,
immunosuppressive and metabolic phenotypes. We identified paracrine
signaling networks and validated the HB-EGF–ERBB4 axis between
macrophage and neoplastic subsets, which promoted tumor growth through
the induction of ERK signaling. These findings collectively reveal intrinsic
and extrinsic regulators of therapy response in high-risk neuroblastoma.
Neuroblastoma is a cancer of the sympathetic nervous system that of the intratumoral heterogeneity of neuroblastoma7–14. Neoplastic
mainly arises from the adrenal glands and sympathetic ganglia. It is neuroblastoma cells transcriptionally resemble normal fetal adre-
the most common extracranial solid tumor in children and accounts nal neuroblasts and recapitulate their developmental trajectory7,8.
for about one in six pediatric cancer deaths1,2. Neuroblastoma is strati- Additionally, epigenetic profiling has characterized two core neo-
fied into low-, intermediate- and high-risk categories3. Patients in the plastic states—adrenergic-like (ADRN-like) and mesenchymal-like
non-high-risk categories have an excellent prognosis with minimal (MES-like)15–17—which has subsequently been supported by tran-
therapy4. Despite substantial advances in the standard of care, the scriptomic profiling in both neuroblastoma preclinical models18–21
5-year survival of high-risk neuroblastoma remains <50%5. Clinical and and primary tumors9,20,22. Furthermore, single-cell profiling of the
genetic features, such as older age and MYCN amplification are associ- neuroblastoma tumor microenvironment has uncovered distinct
ated with worse prognosis. The poor prognosis of treatment-refractory immune subsets10–12,23. However, the interplay between neoplastic
and recurrent neuroblastoma stems from acquired treatment resist- and immune subtypes and the role of chemotherapy in rewiring the
ance in a heterogeneous tumor microenvironment6. tumor-immune microenvironment to promote treatment resist-
Recent advances in single-cell transcriptomic and epig- ance remain unclear due to the lack of study of matched pre- and
enomic profiling have significantly advanced our understanding post-therapy patient samples.
e-mail: tank1@chop.edu
Nature Genetics | Volume 57 | May 2025 | 1142–1154 1142

Article https://doi.org/10.1038/s41588-025-02158-6
a b c
Neuroblasts
Adrenal cortex cells
B cells
Kidney cells
Dendritic cells
Endothelial cells
Fibroblasts
Hepatocytes
Macrophages Schwann cells T cells
1.00
d
0.75
0.50
0.25
0 DX PTX
We present an integrated single-cell multimodal analysis of were observed at diagnosis in 11, four and one patient(s), respectively
paired newly diagnosed and post-induction chemotherapy high-risk (Fig. 1a and Supplementary Tables 1 and 2). Patient response to induc-
neuroblastoma using single-nucleus RNA sequencing (snRNA-seq), tion chemotherapy was evaluated by 123I-metaiodobenzylguanidine
single-nucleus assay for transposase-accessible chromatin with imaging plus anatomic imaging using computed tomography or mag-
sequencing (snATAC-seq) and whole-genome sequencing (WGS). We netic resonance imaging, bone marrow aspirate and biopsy24 (Supple-
identify tumor cell intrinsic and extrinsic therapy-induced shifts in the mentary Tables 1 and 2). After quality control, we obtained 372,619 and
neuroblastoma microenvironment and a pro-tumorigenic axis between 144,366 high-quality cells from snRNA-seq and snATAC-seq, respec-
tumor-associated macrophages (TAMs) and neoplastic cells, revealing tively (Extended Data Fig. 1a,b).
new therapeutic strategies for high-risk neuroblastoma. We identified eight major cell populations, including neuroblasts,
fibroblasts, Schwann cells, endothelial cells, macrophages, dendritic
Results cells, T cells and B cells (Fig. 1b–d, Extended Data Fig. 1c and Supplemen-
Single-cell longitudinal profiling reveals microenvironmental tary Table 3), consistent with the results from recent single-cell studies
shifts of patients with neuroblastoma7,8. We also detected three tissue-specific
We profiled neuroblastoma samples from 22 patients with high-risk cell populations (that is, hepatocytes, adrenal cortex cells and kidney
neuroblastoma obtained through an initial diagnostic biopsy followed cells) in a few patients (Extended Data Fig. 1d)—probably from adjacent
by a surgical resection after three to four cycles of induction chemo- normal tissue—and excluded them from subsequent analysis. The cell
therapy using snRNA-seq (22 pairs), snATAC-seq (13 pairs and seven type compositions were largely concordant between snRNA-seq and
unpaired) and WGS (22 pairs) (Fig. 1a). Patients were aged 6 months snATAC-seq data (Fig. 1e and Extended Data Fig. 1e). Interestingly, we
to 13 years at the time of diagnosis, 14 of whom were female and eight found several notable changes in the tumor microenvironment due to
of whom were male. MYCN amplification and ALK and TP53 mutations chemotherapy. The proportion of macrophages was significantly and
Nature Genetics | Volume 57 | May 2025 | 1142–1154 1143
noitcarF
snRNA-seq snRNA-seq snATAC-seq
Initial diagnosis (2 regions; 85 datasets)
22 patients with (biopsy) high-risk snATAC-seq
neuroblastoma (1 region; 38 datasets)
WGS
(1 region; 44 datasets)
Post-induction therapy
(surgical resection) CODEX
(4 datasets)
UMAP 1
e
snRNA-seq snATAC-seq
1.00
0.75
0.50
0.25
0
2 PAMU
Cells expressing
Neuroblasts
Fibroblasts gene (%)
T cells 25 Endothelial cells 50
Macrophages 75
Dendritic cells Avg. expression Adrenal cortex
Schwann cells 2
B cells 1
Hepatocytes 0
Kidney cells −1
P H OX2B ISL P 1 D GFRB D C N CD247 CD9 P 6 E CA M1 PTPRB CD163 CD86 IRF8 FLT3 CYP11A1 CYP11B1 PLP1 CD H19 PAX5 MS4A1 ALB D CD C2 PK HD1
Neuroblasts Fibroblasts Macrophages Endothelial cells Dendritic cells T cells B cells Schwann cells
P = 0.064 P = 0.088 P = 1.4 × 10–3 P = 0.39 P = 0.31 P = 0.27 P = 0.032 P = 2.1 × 10–3
1.00 0.04 0.20
0.6 0.15
0.15
0.75 0.2 0.03 0.15 0.2
0.50 0.4 0.10 0.02 0.10 0.10
0.1 0.1
0.2 0.05 0.01 0.05 0.05
0.25
0 0 0 0 0 0 0
DX PTX DX PTX DX PTX DX PTX DX PTX DX PTX DX PTX DX PTX
noitcarF
UMAP 1
f
2 PAMU
Macrophages Adrenal cortex cells
Schwann cells
Dendritic cells
B cells Neuroblasts
Endothelial cells
T cells
Schwann cells
Fibroblasts
Hepatocytes Kidney cells
Kidney cells Endothelial cells Neuroblasts Hepatocytes B cells Dendritic cells Fibroblasts Ag 2 e 0 (mon 14 th 0 s) Adrenal cortex cells T cells Macrophages
MYCN amplification No MYCN amplification ALK mutation
No ALK mutation TP53 mutation No TP53 mutation
DX PTX ATAC No ATAC
DX PTX
Fig. 1 | Longitudinal single-cell RNA and ATAC atlas of high-risk neuroblastoma. for each patient between initial diagnosis and post-therapy time points in the
a, Overview of the multiomics studies on patient-matched longitudinal snRNA-seq data. Central lines indicate median values, the box edges mark the
neuroblastoma specimens. b,c, UMAPs of the snRNA-seq data (b; n = 372,619 25th and 75th percentiles and the whiskers extend 1.5 times the interquartile
cells) and snATAC-seq data (c; n = 144,366 cells) annotated by major cell type range. Samples from the same patient between time points are connected by a
category. d, Dotplot showing the mean expression of marker genes and the gray line (n = 22 pairs). Statistical significance was assessed using a one-sided
percentage of cells expressing them for each annotated cell type. e, Stacked Wilcoxon signed-rank test. Avg., average; DX, diagnosis; PTX, post-induction
barplots of cell type proportions across the snRNA-seq (left) and snATAC-seq chemotherapy.
(right) datasets. The cell types are colored as in b. f, Shifts in cell type proportions

Article https://doi.org/10.1038/s41588-025-02158-6
consistently expanded after therapy in both snRNA-seq and snATAC-seq Extended Data Fig. 3d). As expected, the abundance of ADRN-baseline
data. Schwann cells—and fibroblasts to a lesser extent—also expanded and ADRN-proliferating populations decreased after therapy. Con-
after therapy, with large shifts noted in a subset of patients (Fig. 1f and versely, the ADRN-calcium, ADRN-dopaminergic and Interm-OXPHOS
Extended Data Fig. 1f). Taken together, these results demonstrate that populations exhibited significant increases after therapy (Fig. 2e).
neuroblastoma therapy results in large-scale alteration in the composi- MES cells made up <10% of neoplastic cells in most samples, but some
tion of the tumor-immune microenvironment. samples contained a high frequency of MES cells with significant
post-therapy changes (Fig. 2e and Extended Data Fig. 3e). Patients
Chemotherapy alters neoplastic cell state composition with mutated ALK demonstrated a significantly smaller decrease in
We sought to dissect the intratumoral heterogeneity by first character- the ADRN-baseline and ADRN-proliferating populations and a notable
izing neoplastic cell states. We identified neoplastic cells by combining decrease in the MES state after therapy (Fig. 2f), in contrast with the
the copy number variation (CNV) profiles derived from WGS data with overall trend (Fig. 2e). MYCN amplification did not affect neoplastic
inferred CNVs from the snRNA-seq data (Extended Data Fig. 2a–e and state shifts (Extended Data Fig. 3f).
Supplementary Methods). We restricted our neoplastic cell call to cells To better understand these cell states, we projected all inferred
derived from the neural crest lineage including neuroblasts, fibroblasts neoplastic cells onto a single-cell transcriptomic atlas of normal adre-
and Schwann cells, as these populations have been suggested to include nal medullary development7. Consistent with previous studies7,8, neo-
neoplastic cells16,21,25. Of note, the fibroblast population is heterogene- plastic cells mostly recapitulated neuroblasts and late neuroblasts,
ous and may include neural crest-derived endoneurial fibroblasts, indicating a developmentally arrested state. Interestingly, we found
which could harbor the same mutations as neoplastic neuroblasts a significant increase in additional developmentally arrested phe-
due to their shared precursors during differentiation26–28. Overall, we notypes in post-therapy samples, including late Schwann cell pre-
identified 205,253 neoplastic cells and the proportion of these cells was cursors, a bridge cell population, chromaffin cells, late chromaffin
correlated with a pathologist’s manual estimates based on histology cells and cycling neuroblasts (Extended Data Fig. 4a–c). Moreover,
(r = 0.6; P = 8.5 × 10-6; Extended Data Fig. 2e). We further validated our the cell states we identified were associated with different develop-
neoplastic cell call by confirming the presence of known neuroblastoma mental states (Extended Data Fig. 4c–f). The MES state was enriched
CNVs, such as 17q, 7q, 17 and 7 gains and 1p and 11q losses29 through in non-neuroblastic phenotypes. In contrast, the ADRN-calcium,
analysis with inferCNV30 (Extended Data Fig. 2f). ADRN-baseline and ADRN-proliferating states were almost entirely
Most putative neoplastic cells had a neuroblastic phenotype enriched in the neuroblast lineage, resembling late neuroblasts, neuro-
(Extended Data Fig. 3a). By reintegrating and clustering the neoplastic blasts and cycling neuroblasts, respectively. The ADRN-dopaminergic
cells from all samples, we found six distinct neoplastic cell states (Fig. 2a state projected mostly onto neuroblasts and late neuroblasts, but
and Supplementary Table 3). We annotated these populations by their partially resembled determined chromaffin cells, supporting its enrich-
ADRN and MES signature scores, differential gene expression and ment of dopaminergic pathways.
enriched transcriptional pathways. We identified one MES-high cluster, Finally, we assessed the clinical implication of these cell states. We
four ADRN-high clusters and one intermediate cluster with moderate examined the gene signature of each state in 498 diagnostic neuroblas-
ADRN and MES signatures (Fig. 2b,c). Furthermore, we examined the toma bulk transcriptomes (the Sequencing Quality Control project
enrichment of Kyoto Encyclopedia of Genes and Genomes pathways cohort)31. Interestingly, the samples with a higher gene signature for the
and Gene Ontology biological process terms of the differentially upreg- ADRN-proliferating, ADRN-baseline or Interm-OXPHOS state showed
ulated genes. ADRN-like cells exhibited four states, three of which were lower overall survival and event-free survival independent of age, sex
enriched in neurodevelopmental pathways (ADRN-calcium (calcium/ and MYCN amplification status (Fig. 2g and Extended Data Fig. 5a). In
synaptic signaling), ADRN-dopaminergic (dopamine metabolism) and contrast, higher scores of the two states resembling more differenti-
ADRN-baseline (few differentially expressed genes)) and one of which ated stages of the neuroblast and chromaffin lineage (ADRN-calcium
was enriched for proliferating cells (ADRN-proliferating) (Fig. 2d, and ADRN-dopaminergic) were associated with better prognoses
Extended Data Fig. 3b and Supplementary Table 4). The intermedi- (Fig. 2g and Extended Data Fig. 5b). The MES signature was not signifi-
ate state highly expressed many ribosomal genes and was uniquely cantly associated with prognosis in the diagnostic samples. Orthogo-
enriched in the oxidative phosphorylation pathway (Fig. 2a). It was nally, we utilized these signatures to stratify patients based on their
therefore annotated as Interm-OXPHOS. The MES state differen- highest neoplastic cell state signature score. Consistently, patients
tially expressed extracellular matrix-related pathways (Fig. 2b–d and assigned to the ADRN-proliferating and Interm-OXPHOS groups had
Extended Data Fig. 3b,c). the lowest survival, whereas those assigned to the ADRN-calcium and
Next, we sought to determine how these newly defined popula- ADRN-dopaminergic groups had the highest survival. Although the
tions shifted during therapy and found significant changes (Fig. 2e and MES state was only associated with an intermediate prognosis, a high
Fig. 2 | Therapy-induced neoplastic cell state shifts. a, UMAP of inferred lines indicate median values, the box edges mark the 25th and 75th percentiles
neoplastic cells from snRNA-seq data after integration and annotation of cell and the whiskers extend 1.5 times the interquartile range. g, Kaplan–Meier curves
states. b, UMAPs showing the MES, ADRN and cell cycle S-phase signature scores of overall survival based on neoplastic cell state using the Sequencing Quality
of neoplastic cells. c, Violin plots of MES − ADRN signature score difference Control project dataset. Patients were stratified into high and low groups based
(top) and cell cycle S-phase score (bottom) across different cell states. The on the median value of the cell state signature score. P values were calculated
short black bars represent the median value in each group and the red dashed based on the Cox proportional hazards model and adjusted by age, sex and
lines indicate y = 0. d, Heatmap of the top 15 enriched Kyoto Encyclopedia of MYCN amplification status. h, Kaplan–Meier curves of overall survival, with
Genes and Genomes pathways for each neoplastic cell state. The enrichment patients grouped into different neoplastic cell states based on maximum cell
was conducted based on Fisher’s exact test using enrichR without multiple state signature scores. The numbers of samples per group are indicated. P values
comparison adjustment. We highlighted in red some labels that are closely were calculated based on the Cox proportional hazards model and adjusted by
related to the naming of each cell state. e, Shifts in cell state proportion between age, sex and MYCN amplification status. The ADRN-calcium state was chosen as
diagnosis and post-therapy samples. A one-sided Wilcoxon signed-rank test was the baseline state. i, Proportions of neoplastic cell states in the initial diagnostic
used to calculate statistical significance. Samples from the same patient between samples. Patients are grouped according to their responses to induction
time points are connected by a gray line (n = 22 pairs). f, Differences in cell state chemotherapy (top) and clinical events (bottom). A one-sided t-test was
frequencies between paired post-therapy and diagnostic samples stratified by performed to compare the MES state proportion between two patient groups,
ALK mutation status. A one-sided Wilcoxon rank-sum test was used to calculate as indicated by the vertical dashed line (P = 0.02 (top) and 0.05 (bottom)). cAMP,
significance (n = 18 ALK wild type (WT) and 4 ALK mutated). In e and f, central cyclic AMP; ECM, extracellular matrix.
Nature Genetics | Volume 57 | May 2025 | 1142–1154 1144

| Article |     |     |     |     |     |     |     |     |     |     | https://doi.org/10.1038/s41588-025-02158-6 |     |     |     |     |
| ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------ | --- | --- | --- | --- |
percentage of the MES state in diagnostic samples correlated with a  419 bulk transcriptomes32, largely replicating these findings (Extended
worse response to chemotherapy and adverse clinical events (toxic  Data Fig. 5c–f). Additionally, deconvolution of the bulk expression data
death, progression or relapse) (Fig. 2h,i and Extended Data Fig. 5b).  revealed that ADRN-proliferating and ADRN-baseline states were more
We validated these two orthogonal analyses in an additional cohort of  common in patients with MYCN amplification and advanced-stage
| a   |                        |     |     |     | b   |           |     | d   |     |     |     |            |     |     |     |
| --- | ---------------------- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- |
|     | Neoplastic cell states |     |     |     |     | MES score |     |     |     |     |     | Cell cycle |     |     |     |
Mismatch repair
Homologous recombination
|              |                   | MES |               |     |     |     |     |     |     |     |     | DNA replication               |     |     |                 |
| ------------ | ----------------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------- | --- | --- | --------------- |
|              |                   |     |               |     |     |     |     |     |     |     |     | Nucleotide excision repair    |     |     | 10              |
|              |                   |     |               |     |     |     |     |     |     |     |     | p53 signaling pathway         |     |     | –log10[P value] |
| ADRN-calcium |                   |     |               |     |     |     |     |     |     |     |     | Ribosome                      |     |     |                 |
|              |                   |     |               |     |     |     |     |     |     |     |     | Pathways of neurodegeneration |     |     | 4               |
|              |                   |     | Interm-OXPHOS |     |     |     |     |     |     |     |     | Oxidative phosphorylation     |     |     |                 |
|              | ADRN-dopaminergic |     |               |     |     |     |     |     |     |     |     |                               |     |     | 0               |
Glutamatergic synapse
ADRN-baseline
Adrenergic signaling in cardiomyocytes Insulin secretion
Oxytocin signaling pathway
| 2 PAMU |     |                    |     |     |     |            |     |     |     |     |     | cAMP signaling pathway |     |     |     |
| ------ | --- | ------------------ | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | ---------------------- | --- | --- | --- |
|        |     |                    |     |     |     |            | 1.5 |     |     |     |     | Axon guidance          |     |     |     |
|        |     | ADRN-proliferating |     |     |     | ADRN score |     |     |     |     |     | Dopaminergic synapse   |     |     |     |
Phospholipase D signaling pathway
UMAP 1
−0.5
Calcium signaling pathway
ADRN-calcium ADRN-proliferating Transcriptional misregulation in cancer
|     | ADRN-baseline     |     | Interm-OXPHOS |     |     |     |     |     |     |     |     | Regulation of actin cytoskeleton |     |     |     |
| --- | ----------------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | -------------------------------- | --- | --- | --- |
|     | ADRN-dopaminergic |     | MES           |     |     |     |     |     |     |     |     | PI3K−AKT signaling pathway       |     |     |     |
Focal adhesion
ECM−receptor interaction
Cholesterol metabolism
| c   |     |     |     |     |     |     |     |     |     |     |     | Complement and coagulation cascades |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------- | --- | --- | --- |
Cellular senescence
| NRDA – erocs SEM | 4   |     |     |     |     |               |     | Cell state |               |                |     |                    |     |                |     |
| ---------------- | --- | --- | --- | --- | --- | ------------- | --- | ---------- | ------------- | -------------- | --- | ------------------ | --- | -------------- | --- |
|                  | 2   |     |     | -   |     |               |     | e          | ADRN-baseline |                |     | ADRN-proliferating |     | ADRN-calcium   |     |
| erocs            |     |     |     |     |     |               |     |            |               | P = 2.4 × 10–6 |     | P = 7.2 × 10–7     |     | P = 1.7 × 10–5 |     |
|                  | - - | -   | - - |     |     |               |     |            |               |                |     |                    |     |                |     |
|                  | 0   |     |     |     |     | S-phase score |     |            |               |                |     |                    |     |                |     |
|                  |     |     |     |     |     |               |     |            | 0.6           |                |     |                    |     | 0.6            |     |
0.4
|     | −2  |     |     |     |     |     |     |     | 0.4 |     |     |     |     | 0.4 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
0.2
|               |                       |     |     |                    |        |              |      |          | 0.2               |     |     |                |     | 0.2  |           |
| ------------- | --------------------- | --- | --- | ------------------ | ------ | ------------ | ---- | -------- | ----------------- | --- | --- | -------------- | --- | ---- | --------- |
| erocs esahp-S | 0.8                   |     |     |                    |        |              |      | noitcarF | 0                 |     |     | 0              |     | 0    |           |
|               | 0.4                   |     |     |                    |        |              | 0.2  |          | ADRN-dopaminergic |     |     | Interm-OXPHOS  |     |      | MES       |
|               |                       |     | -   |                    |        |              |      |          | P = 6.4 × 10–3    |     |     | P = 5.7 × 10–3 |     |      | P = 0.043 |
|               |                       |     |     |                    | 2 PAMU |              |      |          | 0.4               |     |     |                |     |      |           |
|               | -                     |     |     |                    |        |              |      |          |                   |     | 0.6 |                |     |      |           |
|               | 0 -                   | -   | -   | -                  |        |              | −0.2 |          | 0.3               |     |     |                |     | 0.75 |           |
|               |                       |     |     |                    |        |              |      |          |                   |     | 0.4 |                |     | 0.50 |           |
|               |                       |     |     |                    | UMAP 1 |              |      |          | 0.2               |     |     |                |     |      |           |
|               | Neoplastic cell state |     |     |                    |        |              |      |          |                   |     | 0.2 |                |     |      |           |
|               |                       |     |     |                    |        |              |      |          | 0.1               |     |     |                |     | 0.25 |           |
| f             | ADRN-baseline         |     |     | ADRN-proliferating |        | ADRN-calcium |      |          | 0                 |     |     | 0              |     | 0    |           |
|               | P = 0.017             |     |     | P = 0.027          |        | P = 0.24     |      |          | DX                | PTX |     | DX PTX         |     | DX   | PTX       |
|               | 0.25                  |     | 0   |                    |        | 0.6          |      |          |                   |     |     |                |     |      |           |
g
0 0.4 High cell state signature score Low cell state signature score
| )XD – XTP( egnahc noitcarF |       |     | −0.2 |     |     |     |     |      |               |     |                    |     |      |              |     |
| -------------------------- | ----- | --- | ---- | --- | --- | --- | --- | ---- | ------------- | --- | ------------------ | --- | ---- | ------------ | --- |
|                            | −0.25 |     |      |     |     | 0.2 |     |      | ADRN-baseline |     | ADRN-proliferating |     |      | ADRN-calcium |     |
|                            | −0.50 |     | −0.4 |     |     | 0   |     | 1.00 |               |     | 1.00               |     | 1.00 |              |     |
−0.2
|     |     |     |     |     |     |     |     | 0.75 |     |     | 0.75 |     | 0.75 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | ---- | --- | ---- | --- | --- |
−0.75
|     |     |     |     |     |     |     |     | 0.50 |     |     | 0.50 |     | 0.50 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | ---- | --- | ---- | --- | --- |
ADRN-dopaminergic Interm-OXPHOS MES P = 0.018   P < 0.001   P < 0.001
|     |          |     |     |          |     |           |     | lavivrus llarevO 0.25 |     |     | 0.25 |     | 0.25 |     |     |
| --- | -------- | --- | --- | -------- | --- | --------- | --- | --------------------- | --- | --- | ---- | --- | ---- | --- | --- |
|     | P = 0.45 |     | 0.4 | P = 0.39 |     | P = 0.033 |     |                       | 0   |     | 0    |     |      | 0   |     |
0.4
0.2 0.5 0 2,0004,0006,000 0 2,0004,0006,000 0 2,0004,0006,000
0.2
|     |     |     | 0    |     |     |      |     |      | ADRN-dopaminergic |     |      | Interm-OXPHOS |      |     | MES |
| --- | --- | --- | ---- | --- | --- | ---- | --- | ---- | ----------------- | --- | ---- | ------------- | ---- | --- | --- |
|     | 0   |     |      |     |     | 0    |     |      |                   |     |      |               | 1.00 |     |     |
|     |     |     | −0.2 |     |     |      |     | 1.00 |                   |     | 1.00 |               |      |     |     |
|     |     |     | −0.4 |     |     | −0.5 |     | 0.75 |                   |     | 0.75 |               | 0.75 |     |     |
−0.2
|     |      |         | −0.6 |     |         |             |     | 0.50 |                   |     | 0.50 |                   | 0.50 |                   |     |
| --- | ---- | ------- | ---- | --- | ------- | ----------- | --- | ---- | ----------------- | --- | ---- | ----------------- | ---- | ----------------- | --- |
|     |      |         |      |     |         |             |     |      | P < 0.001         |     |      | P = 0.002         |      | P = 0.103         |     |
|     | ALK  | Mutated |      | ALK | Mutated | ALK Mutated |     | 0.25 |                   |     | 0.25 |                   | 0.25 |                   |     |
|     | WT   |         |      | WT  |         | WT          |     |      |                   |     |      |                   |      |                   |     |
|     |      |         |      |     |         |             |     |      | 0                 |     | 0    |                   |      | 0                 |     |
| h   |      |         |      |     |         |             |     |      | 0 2,0004,0006,000 |     |      | 0 2,0004,0006,000 |      | 0 2,0004,0006,000 |     |
ADRN-dopaminergic (59; P = 0.36)
|     |      | ADRN-calcium (127) |     |     |     |                          |     |     |                   |     |     | Time (d)         |         |         |               |
| --- | ---- | ------------------ | --- | --- | --- | ------------------------ | --- | --- | ----------------- | --- | --- | ---------------- | ------- | ------- | ------------- |
|     | 1.00 |                    |     |     |     |                          |     |     |                   |     |     |                  |         | Pro     | g r e s s ive |
|     |      |                    |     |     |     |                          |     | i   | Complete response |     |     | Partial response |         | Stable  |               |
|     |      |                    |     |     |     | MES (97; P = 1.5 × 10–3) |     |     |                   |     |     |                  | disease |         | d is e a s e  |
1.00
| lavivrus llarevO | 0.75 |     |     | ADRN-baseline (7; P = 2.3 × 10–5) |     |     |     |     |     |     |     |     |     |     |     |
| ---------------- | ---- | --- | --- | --------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
0.50
Interm-OXPHOS (54; P = 5.6 × 10–6)
|     | 0.50 |     |     |     |     |     |     |     | 0   |     |     |     |     |     |     |
| --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
noitcarF
|     |      |     |     |     |                                          |     |     |     | 3058 3069 3105 | 3110 347 2 495 | 820 985 3489 305 | 1 053 3070 346 7 474 3491 751 | 765 807 | 3484 3078 | 825 |
| --- | ---- | --- | --- | --- | ---------------------------------------- | --- | --- | --- | -------------- | -------------- | ---------------- | ----------------------------- | ------- | --------- | --- |
|     |      |     |     |     | ADRN-proliferating (154; P = 1.6 × 10–6) |     |     |     |                | 3              |                  | 3 3                           |         |           |     |
|     |      |     |     |     |                                          |     |     |     |                |                |                  | Toxic                         | Progr-  |           |     |
|     | 0.25 |     |     |     |                                          |     |     |     |                | Censor         |                  | death                         |         | Relapse   |     |
|     |      |     |     |     |                                          |     |     |     | 1.00           |                |                  |                               | ession  |           |     |
0.50
0
|     | 0   |     | 2,000 |     | 4,000 | 6,000 |     |     | 0   |     |     |     |     |     |     |
| --- | --- | --- | ----- | --- | ----- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Time (d)
|     |     |     |     |     |     |     |     |     | 305 1 05 3 058 | 3069 3070 310 5 472 | 3474 349 1 495 820 | 985 765 825 837 | 3078 807 | 311 0 467 3484 3489 | 751 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------- | ------------------- | ------------------ | --------------- | -------- | ------------------- | --- |
|     |     |     |     |     |     |     |     |     | 3 3            | 3                   | 3                  |                 |          | 3                   |     |
Diagnostic sample ID
| Nature Genetics | Volume 57 | May 2025 | 1142–1154 |     |     |     |     |     |     |     |     |     |     |     |     |     |     | 1145 |
| -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |

Article https://doi.org/10.1038/s41588-025-02158-6
disease. The MES state is enriched in patients with MYCN amplifica- therapy, the expression of many state-specific genes (for example,
tion. Conversely, prognostically favorable states (ADRN-calcium and EZH2, TOP2A and MKI67) was unchanged or increased (Fig. 3c, Extended
ADRN-dopaminergic) are less prevalent in patients with MYCN ampli- Data Fig. 7d and Supplementary Table 6). These results indicate that
fication and advanced-stage disease (Extended Data Fig. 5g–j). These this clinically unfavorable population retains its phenotype during
results suggest that the presence of proliferative, metabolically active therapy, raising the possibility that these proliferating adrenergic cells
and developmentally arrested neoplastic cells at diagnosis portends are persistent and implicated in treatment resistance.
a less favorable clinical outcome, whereas a more differentiated state Beyond global transcription factors, we also identified
with neuronal expression patterns predicts a more favorable outcome. cis-regulatory enhancer–promoter interactions associated with key
Taken together, neuroblastoma neoplastic cells exhibit multiple dis- state-specific genes (Fig. 3d,e and Extended Data Figs. 6g and 7e).
tinct transcriptomic states that recapitulate developmental processes Focusing on the ADRN-proliferating state, we identified three EZH2
and can predict clinical outcomes. enhancers correlated with the EZH2 expression (Fig. 3d). EZH2, the
catalytic subunit of Polycomb repressive complex 2 (PRC2), is a prom-
Cooperative epigenetic regulation governs neoplastic cell states ising target in high-risk neuroblastoma19,35,36. It was highly expressed
After defining and characterizing neoplastic cell states, we sought to in this state, with the three enhancer peaks showing elevated acces-
determine how these cell states are transcriptionally regulated. We sibility and MAZ, CTCF and PHOX2A motifs, indicating state-specific
identified 11 distinct epigenetic clusters in putative neoplastic cells EZH2 activation. We also identified ADRN-proliferating-specific SMC4
in the snATAC-seq data (Extended Data Fig. 6a,b). The cells were then enhancers with MAZ and CTCF motifs (Extended Data Fig. 6g). SMC4
computationally mapped onto the transcriptional states to gener- is a core condensin subunit involved in genome organization and
ate high-confidence epigenetic profiles for each neoplastic state. We tumorigenesis37,38. These findings suggest that regulation of chro-
confirmed that canonical MES and ADRN marker genes, including YAP1 matin structure may help to maintain the proliferative state. Lastly,
and PHOX2B, were more accessible in their respective states and that we found that NECTIN2, recently implicated in T cell dysfunction in
the MYCN gene was more accessible in the clinically unfavorable states high-risk neuroblastoma11, was upregulated in the MES state and asso-
(Extended Data Fig. 6c–g). Consistent with the snRNA-seq data, the ciated with multiple enhancers (Extended Data Fig. 7e). Overall, this
ADRN-calcium and ADRN-dopaminergic states expanded after therapy, analysis uncovered extensive transcription factor cooperativity driv-
whereas the ADRN-proliferating and ADRN-baseline states retracted ing state-specific gene expression and enhancer-driven mechanisms
(Fig. 3a and Extended Data Fig. 7a). supporting high-risk neoplastic subsets.
We examined the differentially accessible transcription fac-
tor motifs for each state using chromVAR33 (Extended Data Fig. 7b Pro-tumorigenic macrophages are enriched after therapy
and Methods). We found that activator protein-1 (AP-1) motifs (for Macrophages were the largest immune component in the neuroblas-
example, FOS, BACH2 and JUN) and CREB motifs (for example, CREM toma microenvironment and expanded significantly after therapy
and CREB5) were differentially accessible in the ADRN-calcium, (Fig. 1b,f). TAMs have been shown to contribute to tumor prolifera-
ADRN-dopaminergic and MES states. Canonical adrenergic transcrip- tion and therapy resistance in high-risk neuroblastoma39,40. Therefore,
tion factor motifs15,16 (PHOX2A, PHOX2B and GATA3) were differentially we sought to delineate the effect of therapy on TAM subtypes. After
accessible specifically in the ADRN-proliferating and ADRN-baseline reintegration and clustering, we identified eight macrophage subsets
states. Likewise, known MES state transcription factor motifs15,16 (ETS2, and annotated them by the top differentially expressed genes (Fig. 4a,
ETV6, ELF1, KLF7 and RUNX1) were most accessible in the MES state and Extended Data Fig. 8a,b and Supplementary Table 9). Namely, we identi-
modestly accessible in the Interm-OXPHOS state. Transcription factor fied a proliferating state (MKI67 and TOP2A), a pro-inflammatory state
motifs associated with epithelial-to-mesenchymal transition34 (TWIST1, (IL18), two pro-angiogenic states (CCL4 and VCAN), an immunosup-
ZEB1 and SNAI1) were enriched in the ADRN-dopaminergic state. pressive state (C1QC and SPP1), a tissue-resident state with the highest
Next, we constructed a transcriptional regulatory network for expression of a phagocytosis gene (F13A1), a lipid-associated state
each state by integrating snRNA-seq and snATAC-seq data (Supplemen- (HS3ST2) and an undefined state expressing THY1 (Fig. 4b,c, Extended
tary Tables 5–8). We confirmed the significance of AP-1 transcription Data Fig. 8c and Supplementary Table 10). Notably, although they were
factors in the MES, ADRN-calcium and ADRN-dopaminergic states previously described as distinct phenotype markers across multiple
(Fig. 3b), as previously reported15–17. Interestingly, both AP-1 transcrip- solid tumors41, C1QC and SPP1 had the highest co-expression in one pop-
tion factor-encoding genes and many of their targets were upregulated ulation. In summary, this analysis confirmed that neuroblastoma TAMs
after therapy, suggesting a strengthened MES phenotype in response can adopt similar phenotypes to those found in other solid tumors.
to therapy (Fig. 3c and Extended Data Fig. 7c). Our analysis also nomi- Importantly, we observed significant shifts in macrophage
nated new transcription factors involved in regulating each state. For states between the paired diagnostic and post-therapy samples. The
example, ZNF148 and MAZ were predicted regulators of the MES and IL18+ population was the only state that was reduced after therapy,
ADRN-proliferating states, respectively (Fig. 3b,c). Strikingly, despite whereas all other states except the proliferating and THY1+ state were
a significant retraction in the ADRN-proliferating population after expanded (Fig. 4d and Extended Data Fig. 8d,e). A predominance of
Fig. 3 | Transcriptional regulation of neoplastic cell states. a, Stacked barplots rest of the cell states. The node color indicates the direction of gene expression
of neoplastic cell state proportions in the snATAC-seq data at the diagnosis change between diagnosis and post-therapy samples in each cell state. The edge
and post-therapy time points. The colors are as in b. b, Dotplot showing the weight is proportional to the linear regression coefficient for the predicted
top 15 transcription factors of the transcriptional regulatory network for each enhancer–promoter interaction and the fraction of cells that are accessible at
neoplastic cell state. The size of each dot represents the fraction of gene targets the enhancer peak. d, Coverage plot showing normalized chromatin accessibility
in the transcriptional regulatory network regulated by each transcription for neoplastic cell states at the EZH2 locus. The E–P link track represents the
factor. The color represents the chromVAR deviation z score. c, Transcriptional predicted enhancer–promoter links colored by the regression coefficient. The
regulatory networks for the ADRN-calcium, ADRN-proliferating and MES cell transcription factor (TF) motifs present at the enhancer peaks are indicated.
states. Diamonds represent transcription factors and circles represent target Differentially accessible peaks for the ADRN-proliferating state are highlighted.
genes. The size of a transcription factor node is proportional to the average e, Normalized chromatin accessibility of putative EZH2 enhancers across
difference in the motif chromatin accessibility z score between a given cell state neoplastic cell states. P values were calculated using edgeR on pseudo-bulk
and the rest of the cell states. The size of a target gene node is proportional to data without multiple comparison adjustment (Supplementary Methods). kb,
the average fold-change of gene expression between a given cell state and the kilobases.
Nature Genetics | Volume 57 | May 2025 | 1142–1154 1146

Article https://doi.org/10.1038/s41588-025-02158-6
IL18+ macrophages was linked to better treatment responses and fewer in patients with advanced-stage disease (Extended Data Fig. 9b).
adverse clinical events (Extended Data Fig. 8f,g). Deconvolution of Collectively, diverse macrophage subsets coexist and correlate with
bulk gene expression data showed that F13A1+, CCL4+ and proliferating genetic and clinical features. Longitudinally, pro-tumorigenic states
macrophages were more abundant in patients with MYCN amplifica- with immunosuppressive, angiogenic or metabolic potential were
tion, whereas THY1+ and IL18+ macrophages were fewer (Extended expanded, whereas pro-inflammatory populations were concomitantly
Data Fig. 9a). Additionally, proliferating macrophages were enriched reduced.
1.00
0.75
0.50
0.25
0
X X
D PT
c ADRN-calcium ADRN-proliferating MES
BACH2 BACH1 TCF3 MAZ PHOX2B ETV6ETS1 RREB1 FOS
CREB5 JUNB PHOX2A KLF6 SPARC RUNX1
GPC5 MEF2D ZGRF1 ANLN GTSE1 KIF4A SP1 NTM SNTB1
JUN F D OSL F P 2 O DE S 4 K D LHL2 G M 9 R A R I P K G 7 4 S P 6 C N B F A P V M 3 3 E N H N S N S 1 O A 3 Y 4 S L N C C T2 A N 2 C T A N P N A S K T 1 3 B 1 D UN O C C 5 S D K OR 3 CS1 S J N M U F A N E R 2 C L2 C1 Z M N E F3 L 6 K 7 N M B C U K A B P I A 1 H 6 S B P 7 M TP K B X I R E F 2 S I 1 P 8 P 1 B L1 FA C IQ R L P G S 1 P A N P S 3 M K X I R F C C 2 C C C 4 D 2 K C R IF 2 B 1 K 5 L 8 K I C 1 A F N C 14 L D 1 C RA 4 TA 5 D C 5 D 1 C N A 3 A P 2 1 H K R M I F F C G 11 3 C B2 T P T C E B F 2 F X D F 3 P 5 1 GL U I I L 3 S 1 P D R A D 5 O 1 P C 3 U O K S 8 L E P T F B 1 N S S P E 1 T 1 S R G K P P 3 3 A I L P N S U R Z E 7 S A P S R 1 Y 1 2 H A A 3 G B P A TB P 1 C 4 2 K 7 2 A I T T N P N K R 1 1 S ER P 1 G TP U T R A H M T C B E N Y A S S O 2 3 10 S Z P J M N U N U A F F R N R I C C 1 D E A 4 C L 1 8 F1
DY ER N C C 2 1I1 PAPPA EML6 KAZN TOP2A SPC25 TOX BIRC5 CENPUCDCA2 MYOFNECTIN C 2 RISPLD2 SLC2A3 JUN
KCNM M A A 1 MLD1 KCNQ3 EZH2 CDK5RAP2 ATAD2 POLQ STARD13 NNMTP3H2 COL4 C A O 1 L4A2
Up in PTX No change Down in PTX
d e
Nature Genetics | Volume 57 | May 2025 | 1142–1154 1147
noitcarF
a
EZH2
NUJ SOF BNUJ DNUJ 2LSOF 1CCRAMS 1HCAB D2FEM 2L2EFN 2HCAB A2FEM 1FBE 2FLE 3TATS 6LCB CIC 1A4RN 1TATS 1C3RN 1L2EFN 3L2EFN 7XFR 2RSE 2FBERS 1FBERS 3PEVIH 5BERC 4FTA MERC 1BEZ 1TSIWT 4FCT B2PAFT 2SIEM ZAM 1PS B2XOHP A2XOHP FCTC 3FCT BIFN 3XBP 45NIL CYFN 1TMND ZPBEC 2TUCENO 5XOS 3ATAG 7FLK 2STE 5DAMS 841FNZ CIFN ARUP 1XNUR 1BERR 3PS 2TATS XFZ BSOF 1PBUF A7BTBZ 2XNUR 6FLK C2FEM 2NXOF 1DAET 1RGE 2CTAFN 1PEVIH 1BKFN 1KXOF 1C2RN 1LGALP
b
ADRN-calcium
ADRN-dopaminergic
ADRN-proliferating
ADRN-baseline
Interm-OXPHOS
MES
Transcriptional regulator of neoplastic cell states
Motif deviation score Proportion of targets regulated
1 2 3 4 0.2 0.4 0.6
3
2
1
0
ytilibissecca
dezilamroN
chr7: 148,433,332−148,434,821
P = 2.6 × 10–3
chr7: 148,481,476−148,482,892
P = 5.1 × 10–3
2
1
0
chr7: 148,982,610−148,984,344
P = 1.1 × 10–2
2
1
0
ADRN-dopa min A e D r R g N ic -cal A c D iu R m N-pr M o E l A if S D er R a N ti - n r I i g n b t o e s r m o m - O e XPH OS
)004–0
egnar(
langis
dezilamroN
ADRN-dopaminergic
ADRN-calcium
MES
ADRN-proliferating
ADRN-baseline
Interm-OXPHOS 0 1 2 3
EZH2 expression
TF motifs M PH A O Z X , S 2 P B 1 , , T P F H D O P1 X2A, MAZ, CTCF, SP1
+450 kb +420 kb –99 Kb
1.0
E–P links
0
148400000 148600000 148800000 149000000
chr7 position (bp)
coefficient Regression

| Article |     |     |     |     |     |                  |     |         |     | https://doi.org/10.1038/s41588-025-02158-6 |     |     |     |     |
| ------- | --- | --- | --- | --- | --- | ---------------- | --- | ------- | --- | ------------------------------------------ | --- | --- | --- | --- |
| a       |     |     |     | b   |     | Cells expressing |     | Average |     | c                                          |     |     |     |     |
Macrophage subsets gene (%) expression Immunosuppressive Proinflammatory
1.0
|     |       | Proliferating |       |               |       | 025 | 5075 −1 | 2   |     |                  |     |       | 0.8 |               |
| --- | ----- | ------------- | ----- | ------------- | ----- | --- | ------- | --- | --- | ---------------- | --- | ----- | --- | ------------- |
|     |       |               |       | Proliferating |       |     |         |     |     | 0.5              |     |       |     |               |
|     |       |               |       | C1QC+SPP1+    |       |     |         |     |     |                  |     |       | 0.4 |               |
|     |       |               |       |               |       |     |         |     |     |  erocs erutangiS | - - | - - - | -   | -             |
|     | IL18+ |               |       |               | VCAN+ |     |         |     |     |                  | 0 - | -     | 0   | - - - - - - - |
|     |       |               | THY1+ |               | IL18+ |     |         |     |     |                  |     |       |     |               |
CCL4+
|     | C1QC+SPP1+ | F13A1+ |       |         | F13A1+ |     |     |     |     |     | Angiogenesis  |     |     | Phagocytosis  |
| --- | ---------- | ------ | ----- | ------- | ------ | --- | --- | --- | --- | --- | ------------- | --- | --- | ------------- |
|     |            |        |       |         |        |     |     |     |     | 1.0 |               |     | 1.0 |               |
|     |            |        | VCAN+ | HS3ST2+ |        |     |     |     |     |     |               |     |     |               |
|     |            |        |       |         | THY1+  |     |     |     |     |     |               |     | 0.5 | -             |
|     |            |        |       |         |        |     |     |     |     | 0.  | 5             |     |     | - - -         |
2 PAMU HS3ST2+ CCL4+ TOP2A MKI67 C1QC SPP1 VCAN VEGFA IL18 CCL4 F13A1 E1 T2 YP27A1 THY1 MRC1 CD163 CD68 0 - - - -
|     |     |     |     |     |     |     |     | LYV S3S |     |     |         | - - - | - − 0 . 5 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | ------- | ----- | --------- | --- |
|     |     |     |     |     |     |     |     | H       |     |     | 0 - - - | -     |           |     |
|     |     |     |     |     |     |     |     | C       |     |     |         |       | − 1. 0    |     |
UMAP 1
Macrophage subtype
| d   |       |     |       |     | e   |     |     |     |                              |     |     |     |     |     |
| --- | ----- | --- | ----- | --- | --- | --- | --- | --- | ---------------------------- | --- | --- | --- | --- | --- |
|     | VCAN+ |     | CCL4+ |     |     |     |     |     | Sending cell (ligand source) |     |     |     |     |     |
C1QC+SPP1+
P = 0.0013 0.4 P = 2.4 × 10–6 THY1+ HS3ST2+ F13A1+ CCL4+ IL18+ VCAN+ Proliferating
|     | 0.3 |     |     |     | VEGFA–GPC1   |     |     |     |     |     |     |     |     |             |
| --- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | ----------- |
|     |     |     | 0.3 |     |              |     |     |     |     |     |     |     |     | VCAN–ITGB1  |
|     |     |     |     |     | VCAN–EGFR    |     |     |     |     |     |     |     |     | THBS1–LRP5  |
|     | 0.2 |     |     |     | THBS1–ITGB1  |     |     |     |     |     |     |     |     |             |
|     |     |     | 0.2 |     | THBS1–ITGA2B |     |     |     |     |     |     |     |     | THBS1–ITGA3 |
|     |     |     |     |     | TGFA–ERBB4   |     |     |     |     |     |     |     |     | THBS1–CD47  |
|     | 0.1 |     | 0.1 |     |              |     |     |     |     |     |     |     |     | TFPI–VLDLR  |
|     |     |     |     |     | SYTL3–NRXN1  |     |     |     |     |     |     |     |     | OSM–OSMR    |
NPY–NPFFR2
|     | 0              |     | 0               |     | LPL–VLDLR    |     |     |     |     |     |     |     |     | NAMPT–INSR    |
| --- | -------------- | --- | --------------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | ------------- |
|     |                |     |                 |     | INHBA–ACVR1B |     |     |     |     |     |     |     |     | INHBA–ACVR2B  |
|     | HS3ST2+        |     | C1QC+SPP1+      |     |              |     |     |     |     |     |     |     |     | IL18–IL1RAPL1 |
|     | P = 2.6 × 10–5 |     |                 |     | IL16–KCND2   |     |     |     |     |     |     |     |     | IGF1–IGF1R    |
|     | 0.4            |     | 0.15 P = 0.0019 |     | ICAM1–EGFR   |     |     |     |     |     |     |     |     | HBEGF–ERBB4   |
HBEGF–EGFR
| noitcarF | 0.3            |     |                 |     | GZMB–CHRM3    |                    |                        |                   |                        |                         |                          |                |                   | HBEGF–CD9   |
| -------- | -------------- | --- | --------------- | --- | ------------- | ------------------ | ---------------------- | ----------------- | ---------------------- | ----------------------- | ------------------------ | -------------- | ----------------- | ----------- |
|          |                |     | 0.10            |     |               |                    |                        |                   |                        |                         |                          |                |                   | GNAI2–OPRM1 |
|          |                |     |                 |     | GNAI2–IGF1R   |                    |                        |                   |                        |                         |                          |                |                   | GNAI2–F2R   |
|          | 0.2            |     |                 |     | GNAI2–EGFR    |                    |                        |                   |                        |                         |                          |                |                   | GNAI2–DRD2  |
|          |                |     | 0.05            |     | GNAI2–ADCY1   |                    |                        |                   |                        |                         |                          |                |                   |             |
|          | 0.1            |     |                 |     | FN1–ITGB8     |                    |                        |                   |                        |                         |                          |                |                   | GAL–GALR1   |
|          |                |     |                 |     | FN1–ITGA2B    |                    |                        |                   |                        |                         |                          |                |                   | FN1–ITGA8   |
|          | 0              |     | 0               |     |               |                    |                        |                   |                        |                         |                          |                |                   | F13A1–ITGB1 |
|          |                |     |                 |     | EREG–ERBB4    |                    |                        |                   |                        |                         |                          |                |                   | EREG–EGFR   |
|          | F13A1+         |     | IL18+           |     | DCN–ERBB4     |                    |                        |                   |                        |                         |                          |                |                   |             |
|          |                |     |                 |     | COL1A1–ITGA11 |                    |                        |                   |                        |                         |                          |                |                   | COL3A1–DDR2 |
|          |                |     |                 |     | CALCA–RAMP1   |                    |                        |                   |                        |                         |                          |                |                   | COL1A1–DDR2 |
|          | 0.3 P = 0.0052 |     | 0.75 P = 0.0011 |     |               |                    |                        |                   |                        |                         |                          |                |                   | AREG–EGFR   |
|          |                |     |                 |     | APOE–VLDLR    |                    |                        |                   |                        |                         |                          |                |                   | APOE–SCARB1 |
|          |                |     |                 |     | APOE–LRP5     |                    |                        |                   |                        |                         |                          |                |                   | APOE–LDLR   |
|          | 0.2            |     | 0.50            |     |               |                    |                        |                   |                        |                         |                          |                |                   |             |
|          |                |     |                 |     |               | m n e O            | S i c ratin g E S in e | i c n g ES XPHO S | E S n e O S i c rating | E S m n e m             | n e O S i c in           | g E S inergi c | E S m in e nergic | MES         |
|          |                |     |                 |     |               | l c iu s e l i P H | n e r g M s e l n e r  | g rat i M         | M s e l i P H n e r g  | M l ci u s e li l c i u | s e l i P H n e r g ra t | M M            | al c i u as e l   |             |
0.1 0.25 ADRN - c a - b a O X m i l if e - b a m i l if e -O - b a O X m i l if e N - ca - b a N -c a - b a O X m i l if e m N - c - b m i
|     |     |     |        |     |     | D R N r m - o p a   | -p r o D R N o p a p r o | erm DR  | N r m - o p a p r o              | ADR D R N D R D R N | r m - o p a p r o | dop a DR | D R N o p a |         |
| --- | --- | --- | ------ | --- | --- | ------------------- | ------------------------ | ------- | -------------------------------- | ------------------- | ----------------- | -------- | ----------- | ------- |
|     |     |     |        |     |     | A I n t e N - d R N | A N - d R N -            | I n t A | I n t e N - d R N -              | A A A I n t e       | N - d R N - N     | - A A    | N - d       |         |
|     | 0   |     | 0      |     |     | A D R A D           | A D R A D                |         | A D R A D                        | A D                 | R A D A D R       | A        | D R         |         |
|     | DX  | PTX | DX PTX |     |     |                     |                          |         | Receiving cell (receptor source) |                     |                   |          |             | 0.2 0.8 |
Cross talk score
| f   |     |     | g   |     | h   |     |     |     |     |     | i   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
P = 8.4 × 10–4
50
|     |     |     |     |     | TGFA |     | CD68 |     | HB-EGF |     |     | Distance to CD163+ CD68hi macrophage |     |     |
| --- | --- | --- | --- | --- | ---- | --- | ---- | --- | ------ | --- | --- | ------------------------------------ | --- | --- |
P < 2.2 × 10–16
|     | 30  |     |     |     |     |     |     |     |     |     |     | 300 | P < 2.2 × 10–16 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- |
)mµ( ecnatsiD
FGE-BH fo ytisneD
200 P < 2.2 × 10–16
10
|     |                        |         | 20 µm |     | 20 µm  |     | 20 µm |     | 20 µm |     |     |     |     |     |
| --- | ---------------------- | ------- | ----- | --- | ------ | --- | ----- | --- | ----- | --- | --- | --- | --- | --- |
|     | Other                  | ERBB4hi |       |     |        |     |       |     |       |     |     |     |     |     |
|     | neuroblastsneuroblasts |         |       |     | PHOX2B |     | ERBB4 |     | GD2   |     |     | 100 |     |     |
P = 2.9 × 10–6
|     | 50  |     |     |     |     |     |     |     |     |     |     | 0           |     |                         |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ----------------------- |
|     |     |     |     |     |     |     |     |     |     |     |     | ADRN-like-1 | -2  | ADRN-like-3 Mesenchymal |
li k e 4hi)
ADRN - B B
( E R
|     | 30  |     | 20 µm |     | 20 µm |     | 20 µm |     | 20 µm |     |     |     |     |     |
| --- | --- | --- | ----- | --- | ----- | --- | ----- | --- | ----- | --- | --- | --- | --- | --- |
Neuroblast population
ERBB4hi neuroblasts Other neuroblasts
Macrophages
10
|     | DX  | PTX |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Fig. 4 | TAMs in the neuroblastoma microenvironment. a, UMAP of macrophage  red dashed line indicates recurrent interactions. f, Comparison of the density of
subsets (14,866 cells) from snRNA-seq data after integration and annotation.  HB-EGF protein quantified by CODEX between neighbors of ADRN-like-2 (ERBB4hi)
The colors are as in b. b, Dotplot of the average expression of marker genes and  neuroblasts and neighbors of other neuroblasts (top), as well as between
the percentage of cells expressing them for each annotated macrophage subset.  diagnosis and post-therapy samples (bottom). The density was defined as the
c, Violin plots of signature scores for immunosuppressive, pro-inflammatory,  mean expression of HB-EGF on cells within a 40-µm window, excluding the marker
angiogenesis and phagocytosis macrophages in our macrophage subsets. The  within the center cell. Significance was assessed using a two-sided Wilcoxon rank-
short black bars represent the median value in each group and the red dashed  sum test. The numbers of cells are: n = 655,573 (other neuroblasts), 17,532 (ERBB4hi
lines indicate y = 0. d, Shifts in macrophage subset proportions between   neuroblasts), 221,677 (DX) and 451,428 (PTX). g,h, Representative cell type mask
diagnosis and post-therapy samples. A one-sided Wilcoxon signed-rank test was  (g) and CODEX images (h). Arrows indicate macrophages (top) and neuroblasts
used to calculate significance. Samples from the same patient between time  (bottom). i, Distance from each neuroblast cell to the nearest CD163+CDCD68hi
points are connected by a gray line (n = 22 pairs). e, Dotplot showing predicted  macrophage across samples, stratified by neuroblast population. Numbers of
ligand–receptor interactions between neoplastic cells and macrophage subsets.   cells in each group (from left to right): n = 396,277, 17,532, 241,995 and 17,301.
The ligands are from macrophage subsets (top labels) and are listed first in each  Significance was assessed using a two-sided Wilcoxon rank-sum test. Outliers were
pair. The receptors are from neoplastic populations (bottom labels) and are  truncated for visualization purposes. In d, f and i, central lines indicate median
listed second in each pair. Both y axes have been used for labeling due to space  values, the box edges mark the 25th and 75th percentiles and the whiskers extend
constraints. Important interactions involving ERBB4 are highlighted in red; the  1.5 times the interquartile range.
| Nature Genetics | Volume 57 | May 2025 | 1142–1154 |     |     |     |     |     |     |     |     |     |     |     |     |     | 1148 |
| -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |

Article https://doi.org/10.1038/s41588-025-02158-6
Clusters Cell types
4 Macrophage
0 3
2 8 5 Neuroblast Fibroblast
7 1 6 Endothelial UMAP 1
Nature Genetics | Volume 57 | May 2025 | 1142–1154 1149
2 PAMU UMAP 1 2 PAMU
)mµ(
segahporcam
+fgebH
ot
ecnatsiD
a b c
(993,070 cells)
Macrophage: 3
Endothelial: 6
Fibroblast: 5
0
8
4
7
1
2
P h ox2 b Isl1 Ha n d2 Pe g1 0 T u b b 3 C h d 4 C bx 3 Pik 3r1 T S h lc1 8a2 A gtr A 2 t p2a2 Mki 67 C d 6 8 Gr n Vca m1 Csf P 1 e r ca m1 C d h 5 F n P 1 d gfr b C ol1a2
d
h j
Erbb4+ neuroblasts
Other neuroblasts
i
stsalborueN
Cells expressing
gene (%)
20406080 100
Mean expression
0 1
e Cells expressing
Cells expressing gene (%) Mean expression f g
Mean expression
gene (%)pressed
20 60 100 0 1 1.00
10 30 60 0 1
THY1+
ADRN-calcium HS3ST2+ 0.75
ADRN-baseline F13A1+
Interm-OXPHOS CCL4+ 0.50 ADRN-dopaminergic IL18+
ADRN-proliferating VCAN+ 0.25
MES
C1QC+SPP1+
Proliferating
A DR N A - D c R I a n N lc t - e D i b u r R a m m N s - e - O s A d l c i X o n D o p e P R r e H a N s m c O -p o i S n r r o e e s l r c i g f o e i r c r e a s t c in o g re s M co E r S e score T H H Y S 1+ 3 s S c T o 2 F + r 1 e 3 sc A o 1+ C r e C sc L o 4+ re I s L c 18 o V + C r C e 1 s Q A co C N P + + r r e o S s l P c if P o e 1 r + r e a s ti c n o g r e score C 0 ontro T l reated
A
VCAN+–MES Fold change
VCA V N C +– A A N D + R –I N n - t d e o rm pa -O m X in P e H rg O i S c 10.0 THY1+ V – C A A D N R + N – - A d D o R p N am -c i a n l e c r iu g m ic 7.5 300 P = 0.59 P = 0.01
THY1+–ADRN-baseline
Proliferating–MES
Proliferating–ADRN-dopaminergic 5.0
MES–VCAN+
MES–Pro M li E fe S r – a IL ti 1 n 8 g + 2.5 200
MES–HS3ST2+
HS3ST2+–ADRN-proliferating
CCL4+–MES
CCL4+–ADRN-proliferating –log 10 [P value]
AD A R D N R - N p - r p o r l o if l e if r e a r t a in ti g n – g F – 1 I 3 L A 18 1+ + 2 100
ADRN-calcium–F13A1+ 3
ADRN-baseline–THY1+
ADRN-baseline–IL18+ 4
Col1a1– E C re d g 4 – 4 E F r n b 1 b – 4 It F g n a 1 2 – b It F g n a 1 4 –I F t n g 1 a G – 9 P n l a a i u 2 G r – n D a rd i2 2 – G E G n g n a f i a r 2 i – 2 H F – 2 O b r e p g r m f– 1 Er I b g b f1 4 –I L g p f N l 1 – r a V m S ld e p l m S r t– e a I m 3 n a s a r – 3 N c S r – e p P m 1 lx a n 3 d d 1 – T N f T r p h p i– b 1 V s1 ld – T I l h t r g b a s 2 1 T – b h It b g s a 1 3 – V L c r a p n 5 –Egfr 5 0 Control Treated
DAPI Phox2b Erbb4 Cd68 Hbegf
10 µm 10 µm
noitcarF noitcarF
1.00
0.75 C1QC+SPP1+
ADRN-baseline CCL4+
ADRN-calcium
F13A1+
ADRN-dopaminergic 0.50 H IL S 18 3 + ST2+ ADRN-proliferating
Proliferating
Interm-OXPHOS 0.25 THY1+
MES VCAN+
0 Contro T l reated
Fig. 5 | Spatial transcriptomic analysis of murine neuroblastoma. the proportions of projected neoplastic cell states (f) and macrophage subsets
a,b, UMAP projection of Xenium transcriptomic data (993,070 cells) annotated (g) for treated mice and controls. h, Spatial co-localization analysis of ligand–
by cell cluster (a) and major cell type (b). c, Dotplot showing the normalized receptor interactions predicted between neoplastic cells and macrophage
expression levels of marker genes and the percentages of cells expressing subsets based on snRNA-seq data. The Hbegf–Erbb4 interaction is highlighted
them for each annotated cell type. Each row represents a cell cluster, with the in red. i, Representative image illustrating the spatial co-localization of Erbb4+
average gene expression for each cluster normalized to a range between 0 and neuroblasts and Hbegf+ macrophages. The dots represent individual transcripts.
1 across clusters. d,e, Dotplots showing the normalized signature scores for j, Comparison of spatial distances between Hbegf+ macrophages and Erbb4+
each neoplastic cell state (d) and macrophage subset (e). Each row represents a neuroblasts versus other neuroblasts. Significance was assessed by two-sided
predicted cell subpopulation, with the average signature score for each cell state (left) and one-sided (right) Wilcoxon rank-sum test.
normalized to a range between 0 and 1 across cell types. f,g, Barplots displaying

Article https://doi.org/10.1038/s41588-025-02158-6
Macrophages differentially interact with neoplastic cell states to both macrophage subsets and significantly closer to CD163+CD68hi
Next, we explored how these macrophage subtypes interact with macrophages than the other neuroblasts (Fig. 4i and Extended Data
neoplastic cells by performing a cell–cell interaction analysis using Fig. 10h). These results demonstrate the ability to spatially resolve
CytoTalk42. We identified numerous bidirectional ligand–receptor neoplastic and immune cells and support macrophage-induced ErbB
interactions (Fig. 4e and Extended Data Fig. 9c). Many of these interac- signaling as a potential pro-tumorigenic mechanism driving adrenergic
tions involved proteins that facilitate cell adhesion, cell migration and neoplastic cells.
angiogenesis, including the ligands VCAN (with the receptors ITGB1 and
EGFR), THBS1 (with the receptors ITGB1, LRP5, ITGA3, CD47 and ITG2B), Murine model recapitulates tumor–macrophage interactions
VEGFA (with the receptor GPC) and SEMA3A (with the receptor NRP1). To further investigate the predicted interactions between macrophages
We found that interactions between epidermal growth factor family and neuroblasts in vivo, we utilized Xenium spatial transcriptomics to
(ErbB) receptors (ERBB4 and EGFR) and multiple ligands (HB-EGF, TGFA, study tumors from the well-validated immunocompetent TH-MYCN
EREG, AREG and ICAM1) constituted the most frequently enriched sign- mouse model43, genetically engineered to overexpress MYCN in the
aling pathway. Notably, these interactions were preferentially predicted murine neural crest, resulting in spontaneous tumors. We profiled
between VCAN+ macrophages and all neoplastic populations (Fig. 4e treatment-naive and cyclophosphamide-treated mice with a panel
and Extended Data Fig. 9d,e). The THY1+ macrophages were involved of 5,000 genes and captured all of the major cell types identified in
in interactions related to collagen and integrin signaling, whereas the our multiomic cohort, including cells resembling all neoplastic and
HS3ST2+ macrophages expressed ligands related to lipid metabolism macrophage phenotypes (Fig. 5a–g). We then applied a spatial ligand–
(for example, APOE, LRP5 and LPL), interacting with multiple neoplastic receptor analysis (Supplementary Methods), which validated a broad
cell states (Fig. 4e and Extended Data Fig. 9c). range of the interactions predicted by snRNA-seq. This included the
To validate the intercellular interactions predicted via snRNA-seq, HB-EGF–ERBB4 interaction, which occurred predominantly between
we performed co-detection by indexing (CODEX) spatial pro- VCAN+ macrophages and Interm-OXPHOS neoplastic cells in the mouse
teomics using a 38-antibody panel on whole-slide formalin-fixed, model, consistent with the predicted interactions (Fig. 4e and Fig. 5h).
paraffin-embedded (FFPE) samples from two diagnostic–post-therapy We also observed that Erbb4+ neuroblasts are spatially closer to Hbegf+
pairs included in the single-cell transcriptomic atlas (Supplementary macrophages than other neuroblasts in the cyclophosphamide-treated,
Table 11 and Extended Data Fig. 10a). After single-cell segmentation but not treatment-naive, mice (Fig. 5i,j). Overall, these results demon-
and clustering, we resolved the major cell lineages, including neu- strate that the key microenvironmental phenotypes and cellular inter-
roblasts, macrophages and T cells, and discerned multiple distinct actions in human neuroblastoma are also present in a well-validated
neuroblasts and macrophage subsets (Extended Data Fig. 10b–f). We mouse model, providing a basis for the preclinical testing of therapeutic
found three subsets of adrenergic neuroblasts: an ISL1-high popula- strategies that module the tumor-immune microenvironment.
tion (ADRN-like-1), a PPP2R2C-high population (ADRN-like-2) and a
population with minimal PHOX2B expression (ADRN-like-3). We also Macrophage-secreted HB-EGF promotes tumor survival
identified a mesenchymal neuroblastic population expressing vimen- Given these ligand–receptor interactions, we hypothesized that
tin (Extended Data Fig. 10d,e). Notably, the immunotherapy target pro-tumorigenic macrophages contribute to therapeutic resistance
GD2 was exclusively expressed on ADRN-like-2 neuroblasts. Finally, via activation of ErbB receptor tyrosine kinases in adrenergic neoplastic
we found that all macrophages expressed CD163, but two populations states. We nominated several ligands of the ERBB4 growth factor recep-
were discriminated by the additional high expression of either CD206 tor, including HB-EGF, EREG and TGFA. Moreover, HB-EGF and EREG
or CD68 (Extended Data Fig. 10d), resembling F13A1+ and C1QC+SPP1+ consistently interacted with ERBB4 in all neoplastic states except the
macrophages in our transcriptomic data (Fig. 4b). MES state (Fig. 4e). We found that HBEGF, but not EREG or TGFA, was
Focusing on the epidermal growth factor-related pathways, we expressed more after therapy across the snRNA-seq dataset within multi-
first observed that the ERBB4 receptor was most highly expressed on ple macrophage subsets (Extended Data Fig. 9e). Therefore, we aimed to
ADRN-like-2 neuroblasts (Extended Data Fig. 10d). We then examined examine the coordinated roles of HB-EGF and the ErbB pathway in vitro
the ligand signal density on cells within a 40-µm radius surrounding by co-culturing five neuroblastoma cell lines with macrophages differ-
each neuroblastic cell. The densities of the secreted ERBB4 ligands entiated from the THP-1 monocyte cell line (THP-1 macrophages). First,
HB-EGF and TGFA were greater in the vicinity of ADRN-like-2 (ERBB4hi) we found that the surface expression of HB-EGF on THP-1 macrophages
cells compared with the other neuroblasts and both ligands were was increased when co-cultured with neuroblastoma cells in all five cell
broadly enriched after therapy (Fig. 4f–h and Extended Data Fig. 10g). lines (Fig. 6a,b). Furthermore, an enzyme-linked immunosorbent assay
We also found that the ADRN-like-2 (ERBB4hi) population was proximal (ELISA) performed with cell culture supernatant confirmed the exclusive
Fig. 6 | Macrophage-secreted HB-EGF activates ERK signaling and promotes co-culture and the HB-EGF inhibitor CRM197. h, Quantification of the results
proliferation. a, Representative western blot of cell-surface HB-EGF (pro- from g across replicates, normalized to total AKT (n = 3 for the treatment group
HB-EGF) from THP-1 macrophages in monoculture and co-culture with and n = 5 for the others). i, Representative images (left) and quantification
neuroblastoma cell lines. b, Quantification of the results from a across all (right) of the area of colony formation for neuroblastoma cells co-cultured with
replicates, normalized to β-actin (n = 3 for COG-N-297 and n = 4 for the others). THP-1 macrophages with or without treatment with CRM197 (from left to right:
Central lines indicate median values, the box edges mark the 25th and 75th n = 3, 3 and 2 per condition). j, Representative images (left) and quantification
percentiles and the whiskers extend 1.5 times the interquartile range. c, Ligand (right) of the area of colony formation for neuroblastoma cells co-cultured with
concentrations in the media of THP-1 macrophage monoculture and co-culture THP-1 macrophages with or without treatment with the pan-ERBB inhibitor
with neuroblastoma cell lines, measured by ELISA (n = 3). d, Phosphorylated afatinib (n = 4). The experiments in i and j were repeated two to four times with
ERBB4 (pERBB4) levels in neuroblastoma cells after co-culture with THP-1 two to four samples per condition and the averaged values across samples are
macrophages, measured by ELISA (n = 4 for CHLA15 and n = 3 for the others). shown. Significance was calculated using a one-sided paired t-test (f, i and j) or
Significance in b and d was calculated using a Welch’s two-sided t-test. two-sided paired t-test (h). The error bars in a–c, f and h–j represent means ± s.d.
e, Representative western blots showing ERK activation in neuroblastoma cells k, Neuroblastoma cells stimulate HB-EGF secretion from THP-1-derived
with and without macrophage co-culture and the HB-EGF inhibitor CRM197. macrophages, which reciprocally induce the phosphorylation of ERBB4 on
f, Quantification of the results from e across all replicates, normalized to total neuroblastoma cells. Activation of ERBB4 stimulates proliferation via the ERK
ERK (n = 5, 3 and 4, from left to right). g, Representative western blots showing pathway. Panel k was created with BioRender.com.
AKT phosphorylation in neuroblastoma cells with and without macrophage
Nature Genetics | Volume 57 | May 2025 | 1142–1154 1150

Article https://doi.org/10.1038/s41588-025-02158-6
secretion of HB-EGF ligand by THP-1 macrophages in the co-culture and ErbB signaling has been demonstrated to regulate cell prolifera-
the absence of EREG and TGFA expressions (Fig. 6c), further nominating tion, differentiation and apoptosis through the PI3K–AKT and RAS–
HB-EGF as the active ligand. In parallel, we noticed significant phospho- RAF–MEK–ERK pathways44. Therefore, we aimed to determine which
rylation increase of the ERBB4 receptor on neuroblastoma cells when downstream signaling pathways are induced by ErbB activation. We
co-cultured with macrophages, compared with monoculture, in three performed western blots of total and phosphorylated AKT and ERK
of the five cell lines examined (Fig. 6d). Taken together, these findings proteins after co-culture and monoculture using three neuroblastoma
implicate that HB-EGF/ERBB4 signaling mediates the neuroblast and cell lines. We found that ERK phosphorylation was increased whereas
macrophage interaction. AKT phosphorylation was unchanged or decreased in all three cell lines.
a b
Monoculture
C
HL A15 NB1643
C
HL
C
A
O
2 0
G-
N-
C
29
O
7
G-
N-59 0
d
Nature Genetics | Volume 57 | May 2025 | 1142–1154 1151
nitca-β/FGE-BH-orP
CHLA15 NB1643 COG-N-297 COG-N-590 CHLA20
4BBREp
evitaleR
P = 1.7 × 10–2
P = 4.4 × 10–3 P = 1.7 × 10–2 P = 4.7 × 10–3
Pro-HB-EGF P = 2.3 × 10–2
β-actin
Monoculture
C HL A15 NB1643 C H
C
L A
o
2 C
-
0
c
O
u
G
l
- N
tu
-2
r
9
e
7 C O G- N-59 0
e
P = 8.6 × 10–3 CHLA15 CHLA20 COG-N-297
P = 1.7 × 10–2 P = 4.6 × 10–3 P = 1.5 × 10–1 Macrophages – + + – + + – + +
CRM197 – – + – – + – – +
Phospho-ERK
Total ERK
Tubulin
CHLA15 CHLA20 COG-N-297
Co-culture + k
Monoculture Co-culture
CRM197
CHLA15
CHLA20
NB1643
Proliferation
Monoculture
j Co-culture
Co-culture +
Monoculture Co-culture afatinib Co-culture + CRM197 or afatinib
CHLA15 CHLA20 NB1643
CHLA15
CHLA20
NB1643
KRE
latot/-ohpsohP
TKA latot/-ohpsohP
c HBEGF EREG TGFA
THP-1 macro CHLA15 NB1643 CHLA20 COG-N-590
600
400
200 0
Co-culture
f g h CHLA15 CHLA20 COG-N-297
CHLA15 CHLA20 COG-N-297 THP1 + + + + CRM197 + + +
Phospho-AKT
Total AKT
Tubulin
noitartnecnoc
dnagiL
)1−lm
gp(
– – + – + – + – +
– – + – + – – – – – –
i
)2slexip(
aera
ynoloC
CHLA15 CHLA20 NB1643
)2slexip(
aera
ynoloC
2.0
1.5
1.0
0.5
2.0
1.5
P = 0.2
1.0
0.5
0
Monoculture Co-culture Co-culture + CRM197
P = 5.1 × 10–1 P = 6.0 × 10–1 P = 4.4 × 10–3
P = 3 P . = 0 1 × .0 10 × – 2 10–2 P = P 3 = .0 3 × .0 1 0 × – 1 2 0–2 P P = = 0 3 . . 3 0 × 10–2 P = 0 P .2 = 0.3 0.6 P P = = 4 2 .3 .0 × × 1 0 10 –1 –21.5 P = 2 P . 0 = 9 × . 1 6 0 × – 1 10–1 1.5 P = 5.9 × 10–3 0.75 P = 1.0 × 10–2 1.5 P = 2.0 × 10–2 0.9 1.0
0.4 1.0 0.50 1.0 0.6
0.5
0.3 0.2
0.5 0.25 0.5
0 0 0
0 0 0 Monoculture Co-culture
Co-culture + CRM197
Macrophage
0.20 P = P 7 = P . 0 7 = . 1 2 × . × 1 1 0 1 × 0 – 3 1 – 0 2 –2 0.15 P = 3 P P .7 = = × 0 2 1 . . 0 0 1 – × 2 10–3 0.08 P P = = P 4 8 = . . 0 0 1 . × 0 × 1 1 × 0 0 – 1 – 3 0 3 –2
0.06
0.15 ERBB4
P
0.10 0.10 0.04 HB-EGF
PERK
0.05 0.05 0.02 Neuroblastoma
cell
0 0 0
P = 2.0 × 10–2 P = 1.2 × 10–2 0.08 P = 1.6 × 10–2
P = 1.0 × 10–3 P = 8.1 × 10−5 P = 1.0 × 10–3
0.10 P = 2.0 × 10–2 0.15 P = 4.0 × 10–3 0.06 P = 7.0 × 10–3
0.10 0.04
0.05
0.05 0.02
0 0 0

| Article |     |     |     |     |     |     |     |     |     | https://doi.org/10.1038/s41588-025-02158-6 |     |     |     |     |
| ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------ | --- | --- | --- | --- |
| a       |     |     |     |     |     | c   |     |     |     |                                            |     |     |     |     |
Projected cell state
|     | PHOX2B |     |     |             |         |     | mTORC1 signaling         |            |     |     |     |                |     |     |
| --- | ------ | --- | --- | ----------- | ------- | --- | ------------------------ | ---------- | --- | --- | --- | -------------- | --- | --- |
|     |        |     |     | 1.00 0.050. |         |     |                          | Hypoxia    |     |     |     | MYC targets V1 |     |     |
|     |        |     |     |             | 18 0.17 |     | TNFα signaling via NF-κB |            |     |     |     |                |     |     |
|     |        |     |     |             | * 0.19  |     |                          | Glycolysis |     |     |     |                |     |     |
Epithelial-to-mesenchymal transition
|     |     |     |     | 0.75 | 0 . 1 9 0. 15 |     |     | p53 pathway |     |     | Estrogen response late |     |     |     |
| --- | --- | --- | --- | ---- | ------------- | --- | --- | ----------- | --- | --- | ---------------------- | --- | --- | --- |
|     |     |     |     | 0.52 | * * * 0.17 *  |     |     |             |     |     |                        |     |     |     |
Cholesterol homeostasis
| 2 PAMU |     |     | noitcarF |     |     |     | G 2 | /M   c h e c k p | o i n t |     |     | Apical surface |     |     |
| ------ | --- | --- | -------- | --- | --- | --- | --- | ---------------- | ------- | --- | --- | -------------- | --- | --- |
0. 290 .2 4 0.3 Unfolded  p ro te i n   r e s p o n s e −log [FDR] −lo g 10 [FDR]
|     |        | CHLA15 |     | 0.50      | * *           |     |                       | D N A   r e      | p a i r | 1 0   |     |                 |     |     |
| --- | ------ | ------ | --- | --------- | ------------- | --- | --------------------- | ---------------- | ------- | ----- | --- | --------------- | --- | --- |
|     |        |        |     |           | *             |     |                       | E 2 F   ta r g   | e t s   | 2. 5  |     |                 |     | 4   |
|     | UMAP 1 |        |     |           |               |     |                       |                  |         | 5 . 0 |     | E2F targets     |     | 6   |
|     |        |        |     |           |               |     |                       | IFN α  r e s p o | n s e   | 7. 5  |     |                 |     | 8   |
|     | CD68   |        |     | 0.25 0.32 |               |     |                       | Apoptosis        |         | 10.0  |     |                 |     | 10  |
|     |        |        |     |           | 0.34 0.4 0.38 |     | Inflammatory response |                  |         |       |     |                 |     |     |
|     |        |        |     |           | *** ** *      |     | IL-2/STAT5 signaling  |                  |         |       |     | G2/M checkpoint |     |     |
KRAS signaling up
|     |     |     | 3   | 0.11 |     |     |     |              |     |     |                    |     |     |     |
| --- | --- | --- | --- | ---- | --- | --- | --- | ------------ | --- | --- | ------------------ | --- | --- | --- |
|     |     |     | 2   | 0    |     |     |     | Adipogenesis |     |     | Hedgehog signaling |     |     |     |
Fatty acid metabolism
| 2 PAMU |        |     | 1   | r e                  | r e i b M197 | Oxidative phosphorylation |     |          |            |      |     |     |                   |     |
| ------ | ------ | --- | --- | -------------------- | ------------ | ------------------------- | --- | -------- | ---------- | ---- | --- | --- | ----------------- | --- |
|        |        |     |     | l t u l t            | u a t i n    |                           |     |          | e          | ib   |     |     | r e b M197        |     |
|        |        |     | 0   | Monocu -c u          |  a f  CR     |                           |     |          | u r in     | M197 |     |     | l t u i n i       |     |
|        |        |     |     | C o                  | e   + +      |                           |     |          | u lt at    |      |     |     | -c u fa t CR      |     |
| UMAP 1 |        |     |     | u r                  | r e          |                           |     | Up in co | -c in  a f |  CR  |     |     | wn in co n  a n   |     |
|        |        |     |     | u lt                 | u l t u      |                           |     |          | n    in    |      |     |     | p   i p   i       |     |
|        |        |     |     | o -c                 | - c          |                           |     |          | o w w n    |      |     |     | U U               |     |
|        |        |     |     | C C                  | o            |                           |     |          | D D o      |      |     | Do  |                   |     |
| b      |        |     |     |                      |              | d                         |     |          |            |      |     |     |                   |     |
|        | PHOX2B |     |     | Projected cell state |              | TNFα signaling via NF-κB  |     |          |            |      |     |     |                   |     |
MYC targets V1
|        |        |        |                    | 1.00 0.010    | . 0 6 0.090.08                       |                           |                       | Apoptosis    |              |                                      |                           | E2F targets      |                        |            |
| ------ | ------ | ------ | ------------------ | ------------- | ------------------------------------ | ------------------------- | --------------------- | ------------ | ------------ | ------------------------------------ | ------------------------- | ---------------- | ---------------------- | ---------- |
|        |        |        |                    |               | * * *                                |                           |                       | p53 pathway  |              |                                      |                           |                  |                        |            |
|        |        |        |                    |               | 0 . 0 7 0. * 160.07                  |                           | Androgen response     |              |              |                                      |                           | G2/M checkpoint  |                        |            |
|        |        |        |                    |               | * * * ***                            |                           |                       |              |              |                                      |                           | MYC targets V2   |                        |            |
|        |        |        |                    | 0.75 0.44     |                                      | Cholesterol homeostasis   |                       |              |              |                                      |                           |                  |                        |            |
|        |        |        |                    |               |                                      |                           | KRAS signaling up     |              |              |                                      |                           |                  | DNA repair             |            |
| 2 PAMU |        |        | noitcarF           |               | 0.52 0.47                            |                           |                       | Angiogenesis |              | −log [FDR]                           |                           |                  |                        | −log [FDR] |
|        |        |        |                    |               | ** 0.44 *                            |                           |                       |              |              | 10                                   | Oxidative phosphorylation |                  |                        | 10         |
|        |        | CHLA20 |                    |               |                                      |                           | Protein secretion     |              |              | 2.5                                  | PI3K/AKT/mTOR  signaling  |                  |                        | 4          |
|        |        |        |                    | 0.50          | **                                   | Estrogen response early   |                       |              |              | 5.0                                  |                           |                  |                        | 6          |
|        |        |        |                    |               |                                      |                           |                       | Coagulation  |              | 7.5                                  | Unfolded protein response |                  |                        | 8          |
|        | UMAP 1 |        |                    |               |                                      |                           |                       |              |              |                                      |                           | Mitotic spindle  |                        |            |
|        |        |        |                    | 0.43          |                                      | Oxidative phosphorylation |                       |              |              | 10.0                                 |                           |                  |                        | 10         |
|        | CD68   |        |                    | 0.25          |                                      |                           |                       | Hypoxia      |              |                                      |                           | mTORC1 signaling |                        |            |
|        |        |        |                    |               | 0.360.310.38                         |                           | IFNγ response         |              |              |                                      |                           |                  |                        |            |
|        |        |        |                    |               | *** *                                |                           |                       |              |              |                                      | TNFα signaling via NF-κB  |                  |                        |            |
|        |        |        |                    | 0.12          |                                      |                           | IL-2/STAT5 signaling  |              |              |                                      |                           |                  | Hypoxia                |            |
|        |        |        | 3                  | 0             |                                      |                           | Inflammatory response |              |              |                                      |                           |                  |                        |            |
|        |        |        |                    |               | Epithelial-to-mesenchymal transition |                           |                       |              |              | Epithelial-to-mesenchymal transition |                           |                  |                        |            |
|        |        |        | 2                  | e             | e ib                                 |                           |                       |              |              |                                      |                           | UV response down |                        |            |
| 2 PAMU |        |        | 1                  | ltu r         | u r in M197                          |                           | mTORC1 signaling      |              |              |                                      |                           |                  |                        |            |
|        |        |        |                    | Monocu c u lt | f a t                                |                           |                       |              | e b          |                                      |                           |                  | e b                    | M197       |
|        |        |        | 0                  | o -           |  +  a  CR                            |                           |                       |              | u r i n i    | M197                                 |                           |                  | lt u r i n i           |            |
|        |        |        |                    | C             | r e e  +                             |                           |                       |              | u lt fa t CR |                                      |                           |                  | wn in co-c u a fa t CR |            |
|        |        |        |                    | l t u         | u r                                  |                           |                       |              | o -c n   a   |                                      |                           |                  | in   n                 |            |
| UMAP 1 |        |        |                    | - c u         | u lt                                 |                           |                       | Up in c      | n  i   i n   |                                      |                           |                  | U p   p   i            |            |
|        |        |        |                    | C o           | o -c                                 |                           |                       |              | o w w n      |                                      |                           |                  | U                      |            |
|        |        |        |                    | C             |                                      |                           |                       |              | D D o        |                                      |                           |                  | Do                     |            |
|        |        |        | ADRN-calcium       |               | Interm−OXPHOS                        |                           |                       |              |              |                                      |                           |                  |                        |            |
|        |        |        | ADRN-proliferating |               | MES                                  |                           |                       |              |              |                                      |                           |                  |                        |            |
Fig. 7 | Transcriptomic analysis of mono- and co-cultured macrophages  hallmark pathways from the Molecular Signatures Database. Pathways in the
and neuroblasts. a, Left, UMAP plots showing cells from monoculture and  co-culture condition were compared versus the monoculture condition and
co-culture with THP-1 macrophages, colored by the normalized expression  pathways in the co-culture with treatment condition were compared versus the
levels of PHOX2B and CD68 for the CHLA15 cell line. Right, barplots depicting the  co-culture without treatment condition. d, Pathway analysis of co-cultured
proportions of projected neoplastic cell states across experimental conditions.  CHLA20 cells as in c. The P values in c and d were calculated based on Fisher’s
b, UMAP and neoplastic cell state inference of co-culture experiments with the  exact test using enrichR and corrected using the Benjamini–Hochberg
CHLA20 cell line as in a. The P values in a and b were calculated using a two-sided  procedure. *P < 0.1; **P < 0.01; ***P < 0.001. FDR, false discovery rate; IFN,
proportion test, comparing either co-culture versus monoculture or co-culture  interferon; IL-2, interleukin 2; mTORC1, mammalian target of rapamycin complex
with treatment versus co-culture without treatment. No multiple comparison  1; TNF, tumor necrosis factor.
adjustment was made. c, Differential pathway analysis of CHLA15 cells using the
Moreover, in the presence of the HB-EGF inhibitor CRM197, ERK phos- changes in neuroblast cell states. In both cell lines, the ADRN-calcium,
phorylation was significantly reduced whereas AKT phosphorylation  Interm-OXPHOS and MES states expanded upon co-culture, whereas
remained unchanged, suggesting that ERK activation is indeed induced  the ADRN-calcium state retracted (Fig. 7a,b), mirroring the cell state
by HB-EGF secreted from co-cultured macrophages (Fig. 6e–h). shifts that occur after standard therapy (Fig. 2e). Subsequently, treat-
We hypothesized that the activated ErbB pathway contributes to  ment with afatinib consistently led to a decrease in the Interm-OXPHOS
tumor cell survival. To test this, we treated three neuroblastoma cell  state. A pathway analysis of the tumor cells revealed that co-culture
lines co-cultured with THP-1 macrophages either with CRM197 or the  upregulated multiple pathways, including epithelial-to-mesenchymal
ERBB tyrosine kinase inhibitor afatinib. We quantified the resulting  transition, tumor necrosis factor alpha signaling and inflammatory
growth effect using a colony formation assay before and after pharma- response, and downregulated cell cycle pathways (Fig. 7c,d and Supple-
cological inhibition. We first confirmed that neuroblastoma cell growth  mentary Table 12). Treatment with afatinib or CRM197 reversed many
was increased with macrophage co-culture compared with monocul- of these pathways compared with the untreated co-culture condition.
ture in all three cell lines tested. Next, we found that neuroblastoma  For example, epithelial-to-mesenchymal transition was suppressed by
cell growth was consistently reduced by either CRM197 or afatinib  CRM197 in both cell lines after its initial upregulation upon co-culture
treatment (Fig. 6i,j). In summary, we conclude that neuroblastoma cells  (Fig. 7c,d). This experiment suggests that macrophage interaction
induce HB-EGF in TAMs, which in turn activates the ERBB4 receptor in  induces similar neoplastic state shifts that occur during standard
tumor cells, stimulates downstream ERK signaling and promotes tumor  therapy and implicates macrophage-driven ErbB signaling in modulat-
cell proliferation (Fig. 6k). ing various neoplastic cellular processes.
To assess the broad impact of tumor–macrophage interactions
| on neoplastic cell phenotypes, we performed scRNA-seq on the neu- |     |     |     |     |     |     |     | Discussion |     |     |     |     |     |     |
| ----------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- |
roblastoma cell lines CHLA15 (diagnostic) and CHLA20 (after therapy)  We present a single-cell multiomic analysis of patient-matched
co-cultured with THP-1 macrophages. Co-culture induced notable  longitudinal high-risk neuroblastoma. Through high-resolution
| Nature Genetics | Volume 57 | May 2025 | 1142–1154 |     |     |     |     |     |     |     |     |     |     |     |     |     | 1152 |
| -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |

Article https://doi.org/10.1038/s41588-025-02158-6
transcriptomic and epigenomic profiling of paired untreated and 8. Kildisiute, G. et al. Tumor to normal single-cell mRNA comparisons
induction chemotherapy-treated specimens, we uncovered diverse reveal a pan-neuroblastoma cancer cell. Sci. Adv. 7, eabd3311 (2021).
tumor and immune phenotypes and revealed profound shifts in the 9. Yuan, X. et al. Single-cell profiling of peripheral neuroblastic
tumor microenvironment during standard therapy. tumors identifies an aggressive transitional state that bridges an
We identified an adrenergic-to-mesenchymal phenotypic spec- adrenergic–mesenchymal trajectory. Cell Rep. 41, 111455 (2022).
trum of neoplastic cells. Moreover, we found that the proportion of 10. Verhoeven, B. M. et al. The immune cell atlas of human
proliferating adrenergic cells decreased after therapy, whereas more neuroblastoma. Cell Rep. Med. 3, 100657 (2022).
differentiated neuronal-like cells expanded. Mesenchymal neoplas- 11. Wienke, J. et al. Integrative analysis of neuroblastoma by
tic cells, resembling mixed developmental lineages, showed a slight single-cell RNA sequencing identifies the NECTIN2–TIGIT axis as a
increase after therapy. A higher mesenchymal state at diagnosis did target for immunotherapy. Cancer Cell 42, 283–300.e8 (2024).
not predict worse survival, but correlated with poorer chemotherapy 12. Costa, A. et al. Single-cell transcriptomics reveals shared
response. In contrast, a larger fraction of proliferating and metabolically immunosuppressive landscapes of mouse and human
active neoplastic cells at diagnosis predicted a worse clinical outcome, neuroblastoma. J. Immunother. Cancer 10, e004807 (2022).
highlighting the need for combinatorial therapies. Our analysis also 13. Fetahu, I. S. et al. Single-cell transcriptomics and epigenomics
uncovered important regulators, such as MAZ and CTCF, for the high-risk unravel the role of monocytes in neuroblastoma bone marrow
proliferating state to maintain its persistent transcriptomic program. metastasis. Nat. Commun. 14, 3620 (2023).
Beyond neoplastic cells, we identified a substantial increase 14. Bonine, N. et al. NBAtlas: a harmonized single-cell transcriptomic
in the macrophage population after therapy shifting towards reference atlas of human neuroblastoma tumors. Cell Rep. 43,
pro-tumorigenic phenotypes. Particularly, we found that HB-EGF 114804 (2024).
was upregulated in macrophages and interacted with all neoplastic 15. Boeva, V. et al. Heterogeneity of neuroblastoma cell identity defined
states. HB-EGF is a critical factor in multiorgan development and tis- by transcriptional circuitries. Nat. Genet. 49, 1408–1413 (2017).
sue remodeling45 and has been implicated in tissue response to injury 16. Van Groningen, T. et al. Neuroblastoma is composed of two
and metastatic progression46–48. In neuroblastoma, the ErbB tyrosine super-enhancer-associated differentiation states. Nat. Genet. 49,
kinases, such as EGFR and ERBB4, have been reported to promote cell 1261–1266 (2017).
growth and prevent apoptosis in preclinical models via the MAPK–ERK 17. Gartlgruber, M. et al. Super enhancers define regulatory subtypes
and PI3K–AKT49–51 pathways. Using multiple neuroblastoma cell lines, and cell identity in neuroblastoma. Nat. Cancer 2, 114–128 (2021).
we found that tumor cells induce macrophage HB-EGF secretion, which 18. Mañas, A. et al. Clinically relevant treatment of PDX models
in turn promotes neuroblast proliferation through activation of the ERK reveals patterns of neuroblastoma chemoresistance. Sci. Adv. 8,
pathway. Of note, our analysis also identified HB-EGF–EGFR signaling eabq4617 (2022).
between mesenchymal neoplastic cells and macrophages; however, 19. Mabe, N. W. et al. Transition to a mesenchymal state in
our experiment could not rule out the contribution of EGFR for ERK neuroblastoma confers resistance to anti-GD2 antibody via
activation. Future studies are expected to clarify this mechanism and to reduced expression of ST8SIA1. Nat. Cancer 3, 976–993 (2022).
assess differential responses of neoplastic states to HB-EGF signaling. 20. Thirant, C. et al. Reversible transitions between noradrenergic
In summary, our study sheds light on the molecular mechanisms and mesenchymal tumor identities define cell plasticity in
of therapeutic resistance in high-risk neuroblastoma and provides a neuroblastoma. Nat. Commun. 14, 2575 (2023).
valuable resource for further analytical inquiry. 21. Van Groningen, T. et al. A NOTCH feed-forward loop drives
reprogramming from adrenergic to mesenchymal state in
Online content neuroblastoma. Nat. Commun. 10, 1530 (2019).
Any methods, additional references, Nature Portfolio reporting sum- 22. Sengupta, S. et al. Mesenchymal and adrenergic cell lineage
maries, source data, extended data, supplementary information, states in neuroblastoma possess distinct immunogenic
acknowledgements, peer review information; details of author contri- phenotypes. Nat. Cancer 3, 1228–1246 (2022).
butions and competing interests; and statements of data and code avail- 23. Grossmann, L. D. et al. Identification and characterization of
ability are available at https://doi.org/10.1038/s41588-025-02158-6. chemotherapy-resistant high-risk neuroblastoma persister cells.
Cancer Discov. 14, 2387–2406 (2024).
References 24. Park, J. R. et al. Revisions to the International Neuroblastoma
1. Maris, J. M. Recent advances in neuroblastoma. N. Engl. J. Med. Response Criteria: a consensus statement from the National
362, 2202–2211 (2010). Cancer Institute Clinical Trials Planning Meeting. J. Clin. Oncol.
2. Johnsen, J. I., Dyberg, C. & Wickström, M. Neuroblastoma—a 35, 2580–2587 (2017).
neural crest derived embryonal malignancy. Front. Mol. Neurosci. 25. Mora, J. et al. Neuroblastic and Schwannian stromal cells of
12, 9 (2019). neuroblastoma are derived from a tumoral progenitor cell.
3. Cohn, S. L. et al. The International Neuroblastoma Risk Group Cancer Res. 61, 6892–6898 (2001).
(INRG) classification system: an INRG Task Force report. J. Clin. 26. Joseph, N. M. et al. Neural crest stem cells undergo multilineage
Oncol. 27, 289–297 (2009). differentiation in developing peripheral nerves to generate
4. Matthay, K. K. et al. Neuroblastoma. Nat. Rev. Dis. Prim. 2, 16078 endoneurial fibroblasts in addition to Schwann cells.
(2016). Development 131, 5599–5612 (2004).
5. Pudela, C., Balyasny, S. & Applebaum, M. A. Nervous system: 27. Chen, B., Banton, M. C., Singh, L., Parkinson, D. B. & Dun, X.-P.
embryonal tumors: neuroblastoma. Atlas Genet. Cytogenet. Single cell transcriptome data analysis defines the heterogeneity
Oncol. Haematol. 24, 284–290 (2020). of peripheral nerve cells in homeostasis and regeneration.
6. Louault, K., De Clerck, Y. A. & Janoueix-Lerosey, I. The Front. Cell. Neurosci. 15, 624826 (2021).
neuroblastoma tumor microenvironment: from an in-depth 28. Kastriti, M. E. et al. Schwann cell precursors represent a neural
characterization towards novel therapies. EJC Paediatr. Oncol. 3, crest-like state with biased multipotency. EMBO J. 41, e108780
100161 (2024). (2022).
7. Jansky, S. et al. Single-cell transcriptomic analyses provide 29. Körber, V. et al. Neuroblastoma arises in early fetal development
insights into the developmental origins of neuroblastoma. and its evolutionary duration predicts outcome. Nat. Genet. 55,
Nat. Genet. 53, 683–693 (2021). 619–630 (2023).
Nature Genetics | Volume 57 | May 2025 | 1142–1154 1153

Article https://doi.org/10.1038/s41588-025-02158-6
30. Kenny, P. A. InferCNV, a Python web app for copy number 44. Segers, V. F. M., Dugaucquier, L., Feyen, E., Shakeri, H. & De
inference from discrete gene-level amplification signals noted in Keulenaer, G. W. The role of ErbB4 in cancer. Cell. Oncol. 43,
clinical tumor profiling reports. F1000Res 8, 807 (2019). 335–352 (2020).
31. SEQC/MAQC-III Consortium. A comprehensive assessment of 45. Dao, D. T., Anez-Bustillos, L., Adam, R. M., Puder, M. &
RNA-seq accuracy, reproducibility and information content by Bielenberg, D. R. Heparin-binding epidermal growth factor-like
the Sequencing Quality Control Consortium. Nat. Biotechnol. growth factor as a critical mediator of tissue repair and
32, 903–914 (2014). regeneration. Am. J. Pathol. 188, 2446–2456 (2018).
32. Cangelosi, D. et al. Hypoxia predicts poor prognosis in 46. Wen, H.-J. et al. Myeloid cell-derived HB-EGF drives tissue
neuroblastoma patients and associates with biological recovery after pancreatitis. Cell. Mol. Gastroenterol. Hepatol. 8,
mechanisms involved in telomerase activation and tumor 173–192 (2019).
microenvironment reprogramming. Cancers 12, 2343 (2020). 47. Kuo, P.-L. et al. Synergistic effect of lung tumor-associated
33. Schep, A. N., Wu, B., Buenrostro, J. D. & Greenleaf, W. J. chromVAR: dendritic cell-derived HB-EGF and CXCL5 on cancer progression.
inferring transcription-factor-associated accessibility from Int. J. Cancer 135, 96–108 (2014).
single-cell epigenomic data. Nat. Methods 14, 975–978 (2017). 48. Ongusaha, P. P. et al. HB-EGF is a potent inducer of tumor growth
34. Van Staalduinen, J., Baker, D., Ten Dijke, P. & van Dam, H. and angiogenesis. Cancer Res. 64, 5283–5290 (2004).
Epithelial–mesenchymal-transition-inducing transcription factors: 49. Ho, R. et al. Proliferation of human neuroblastomas mediated by
new targets for tackling chemoresistance in cancer? Oncogene the epidermal growth factor receptor. Cancer Res. 65, 9868–9875
37, 6195–6211 (2018). (2005).
35. Qadeer, Z. A. et al. ATRX in-frame fusion neuroblastoma is 50. Tamura, S. et al. Induction of apoptosis by an inhibitor of EGFR
sensitive to EZH2 inhibition via modulation of neuronal gene in neuroblastoma cells. Biochem. Biophys. Res. Commun. 358,
signatures. Cancer Cell 36, 512–527.e9 (2019). 226–232 (2007).
36. Chen, L. et al. CRISPR–Cas9 screen reveals a MYCN-amplified neuro- 51. Richards, K. N. et al. Signaling of ERBB receptor tyrosine kinases
blastoma dependency on EZH2. J. Clin. Invest. 128, 446–462 (2018). promotes neuroblastoma growth in vitro and in vivo. Cancer 116,
37. Jiang, L. et al. Overexpression of SMC4 activates TGFβ/Smad 3233–3243 (2010).
signaling and promotes aggressive phenotype in glioma cells.
Oncogenesis 6, e301 (2017). Publisher’s note Springer Nature remains neutral with regard to
38. Zhou, B. et al. A novel miR-219–SMC4–JAK2/Stat3 regulatory jurisdictional claims in published maps and institutional affiliations.
pathway in human hepatocellular carcinoma. J. Exp. Clin. Cancer
Res. 33, 55 (2014). Open Access This article is licensed under a Creative Commons
39. Hadjidaniel, M. D. et al. Tumor-associated macrophages promote Attribution 4.0 International License, which permits use, sharing,
neuroblastoma via STAT3 phosphorylation and up-regulation of adaptation, distribution and reproduction in any medium or format,
c-MYC. Oncotarget 8, 91516–91529 (2017). as long as you give appropriate credit to the original author(s) and the
40. Fultang, L. et al. Macrophage-derived IL1β and TNFα regulate source, provide a link to the Creative Commons licence, and indicate
arginine metabolism in neuroblastoma. Cancer Res. 79, 611–624 if changes were made. The images or other third party material in this
(2019). article are included in the article’s Creative Commons licence, unless
41. Cheng, S. et al. A pan-cancer single-cell transcriptional atlas of indicated otherwise in a credit line to the material. If material is not
tumor infiltrating myeloid cells. Cell 184, 792–809.e23 (2021). included in the article’s Creative Commons licence and your intended
42. Hu, Y., Peng, T., Gao, L. & Tan, K. CytoTalk: de novo construction use is not permitted by statutory regulation or exceeds the permitted
of signal transduction networks using single-cell transcriptomic use, you will need to obtain permission directly from the copyright
data. Sci. Adv. 7, eabf1356 (2021). holder. To view a copy of this licence, visit http://creativecommons.
43. Weiss, W. A., Aldape, K., Mohapatra, G., Feuerstein, B. G. & org/licenses/by/4.0/.
Bishop, J. M. Targeted expression of MYCN causes neuroblastoma
in transgenic mice. EMBO J. 16, 2985–2995 (1997). © The Author(s) 2025
Wenbao Yu 1,2,17, Rumeysa Biyik-Sit1,17, Yasin Uzun3,17, Chia-Hui Chen 1,17, Anusha Thadi 1, Jonathan H. Sussman 4,5,
Minxing Pang 6, Chi-Yun Wu5,7, Liron D. Grossmann1,8,9, Peng Gao10,11, David W. Wu 4,5, Aliza Yousey12, Mei Zhang12,
Christina S. Turn1,2, Zhan Zhang13, Shovik Bandyopadhyay4,14, Jeffrey Huang13, Tasleema Patel1, Changya Chen1,16,
Daniel Martinez15, Lea F. Surrey 15, Michael D. Hogarty 1,2, Kathrin Bernt 1,2, Nancy R. Zhang 7, John M. Maris 1,2 &
Kai Tan 1,2,12
1Center for Childhood Cancer Research, Children’s Hospital of Philadelphia, Philadelphia, PA, USA. 2Department of Pediatrics, University of Pennsylvania
Perelman School of Medicine, Philadelphia, PA, USA. 3Department of Pediatrics, Pennsylvania State University College of Medicine, Hershey, PA, USA.
4Medical Scientist Training Program, University of Pennsylvania Perelman School of Medicine, Philadelphia, PA, USA. 5Graduate Group in Genomics
and Computational Biology, University of Pennsylvania Perelman School of Medicine, Philadelphia, PA, USA. 6Applied Mathematics and Computational
Science Graduate Group, University of Pennsylvania, Philadelphia, PA, USA. 7Department of Statistics and Data Science, University of Pennsylvania,
Philadelphia, PA, USA. 8Hemato-Oncology Division, Edmond and Lily Safra Children’s Hospital, Sheba Medical Center, Tel HaShomer, Israel. 9Cancer
Research Center, Sheba Medical Center, Tel HaShomer, Israel. 10Department of Hematology, The First Affiliated Hospital of Xi’an Jiaotong University,
Xi’an, China. 11Genome Institute, The First Affiliated Hospital of Xi’an Jiaotong University, Xi’an, China. 12Center for Single Cell Biology, Children’s Hospital
of Philadelphia, Philadelphia, PA, USA. 13Department of Bioengineering, University of Pennsylvania, Philadelphia, PA, USA. 14Cell and Molecular Biology
Graduate Group, University of Pennsylvania Perelman School of Medicine, Philadelphia, PA, USA. 15Department of Pathology and Laboratory Medicine,
University of Pennsylvania Perelman School of Medicine, Philadelphia, PA, USA. 16Present address: State Key Laboratory of Experimental Hematology,
Institute of Hematology and Blood Diseases Hospital, Chinese Academy of Medical Sciences and Peking Union Medical College, Tianjin, China.
17These authors contributed equally: Wenbao Yu, Rumeysa Biyik-Sit, Yasin Uzun, Chia-Hui Chen. e-mail: tank1@chop.edu
Nature Genetics | Volume 57 | May 2025 | 1142–1154 1154

Article https://doi.org/10.1038/s41588-025-02158-6
Methods The sample slides were then washed three times in 1× DPBS and stored
Human biospecimens and ethical approval in storage buffer before imaging.
Primary patient samples were obtained from the Children’s Hospital of
Philadelphia Center for Childhood Cancer Research Biobank. Biospeci- CODEX imaging
mens were obtained with informed consent from parents according to CODEX reporters were prepared according to Akoya’s
the Declaration of Helsinki and Institutional Review Board approval. PhenoCycler-Fusion user guide and added to a black 96-well plate.
All patient data were deidentified and written informed consent was The PhenoCycler-Fusion experimental template was set up for a
obtained to publish the indirect identifiers in the present manuscript. CODEX run using Akoya’s PhenoCycler Experiment Designer software
Patient sample information and relevant clinical metadata are provided according to Akoya’s PhenoCycler-Fusion user guide. Details on the
in Supplementary Table 1. order of fluorescent CODEX barcodes and microscope exposure times
are provided in Supplementary Table 9. The PhenoCycler-Fusion
snRNA-seq experimental run was performed using Akoya’s Fusion 1.0.8 software
Single-nucleus suspensions immediately underwent library prepara- according to Akoya’s PhenoImager Fusion user guide. Images were
tion following the 10x Genomics protocol using a Chromium Controller taken and preprocessed (stitching, registration and background
with Chromium Single Cell 3′ Reagent Kit V3 or V3.1, per the manu- subtraction) with Akoya’s PhenoImager Fusion microscope using
facturer’s instructions. Library quality was assessed using an Agilent the default settings. Final images were evaluated, then selected sam-
2100 Bioanalyzer with a High Sensitivity DNA chip (5067-4626; Agilent ples were reimaged with adjusted exposure times based on manual
Technologies). Indexed libraries were pooled and sequenced on an review. After imaging, slides were stained with hematoxylin and
Illumina NovaSeq 6000 using the sequencing parameters 28:8:0:87 eosin. Akoya’s Fusion 1.0.8 software was used to image hematoxy-
(read1:i5:i7:read2, bp) with an average sequencing depth of 50,000 lin and eosin-stained slides at 20× resolution in brightfield on the
read pairs per nucleus. PhenoCycler-Fusion system.
snATAC-seq Monocyte differentiation and co-culture with neuroblastoma
Single-nucleus suspensions immediately underwent library prepara- cells
tion following the 10x Genomics protocol using a Chromium Controller To obtain macrophages, 106 THP-1 monocytes in 4 ml complete media
with Chromium Next GEM Single Cell ATAC Reagent kit V1 or V1.1, per were seeded in 0.4 µm polyethylene cell inserts for six-well plates (930-
the manufacturer’s user manual. Library quality was assessed using an 04-12; cellQART) and treated with 100 ng ml−1 phorbol 12-myristate
Agilent 2100 Bioanalyzer with a High Sensitivity DNA chip (5067-4626; 13-acetate (P1585; Sigma–Aldrich) in complete media for 72 h. After
Agilent Technologies). Indexed libraries were pooled and sequenced on detaching the neuroblastoma cells with versene solution (0.02% EDTA
an Illumina NovaSeq 6000 using the sequencing parameters 49:8:16:49 in Hank’s Balanced Salt Solution), they were plated in six-well plates in
(read1:i5:i7:read2, bp) with an average sequencing depth of 50,000 complete media overnight and allowed to reach 70–75% confluence at
read pairs per nucleus. the time of co-culture. Co-culture media was prepared by mixing RPMI
1640 media plus 1% fetal bovine serum (FBS) and Iscove's Modified Dul-
CODEX antibody staining becco's Medium (IMDM) media plus 1% insulin- transferrin-selenium
CODEX staining was performed using a Sample Kit for (ITS) at a 1:1 ratio. THP-1 macrophages in the cell insert were washed
PhenoCycler-Fusion (7000017; Akoya) according to Akoya’s twice with Dulbecco’s phosphate-buffered saline (DPBS) (14190144;
PhenoCycler-Fusion user guide, with modifications to include a pho- Thermo Fisher Scientific) and transferred to neuroblastoma cell culture
tobleaching step and overnight incubation with antibodies at 4 °C. plates. Neuroblastoma cells and macrophages were co-cultured in 6 ml
FFPE samples were sectioned at 5-µm thickness and mounted onto co-culture media. Neuroblastoma cells cultured without an insert and
charged slides (3800080; Leica) by the Pathology Core at the Chil- THP-1 macrophages in inserts within empty plates were used as control
dren’s Hospital of Philadelphia. Sample slides were baked overnight at monocultures. To inhibit HB-EGF activity, 2 µg ml−1 CRM197 (23218;
65 °C for 3 h and allowed to cool to room temperature. They were then Cayman) was added to the co-culture media. After 48 h, monocultured
deparaffinized in HistoChoice clearing agent (H103-4L; VWR) twice and co-cultured macrophages and neuroblastoma cells with or without
and rehydrated in a graded series of ethanol concentrations (twice CRM197 were harvested for further analysis.
in 100, 90, 70, 50 and 30% and twice in ddHO). Antigen retrieval was
2
performed in 1× citrate buffer (C9999; Sigma–Aldrich) in a pressure ERBB ligand profiling
cooker for 20 min. After equilibrating to room temperature, sample THP-1-derived macrophages were plated and differentiated on
slides were washed twice with ddHO and once with 1× Dulbecco's inserts for six-well plates for 72 h. Neuroblastoma cells were plated
2
phosphate-buffered saline (DPBS) before being submerged in a petri on six-well plates in complete media. Then, neuroblastoma cells and
dish containing 4.5% HO and 20 mM NaOH in 1× DPBS (bleaching solu- THP-1 macrophages were co-cultured with 4 ml co-culture media
2 2
tion) for photobleaching. The petri dish was sandwiched between two (0.5% FBS-supplemented RPMI:IMDM mixture) for 48 h. Cell cul-
broad-spectrum LED light sources for 45 min at 4 °C. After 45 min, sam- ture supernatants were collected, centrifuged at 500g for 5 min
ple slides were transferred to a new petri dish with freshly made bleach- and filtered with a 0.22-µm polyethersulfone membrane. Super-
ing solution and photobleached for another 45 min at 4 °C. Sample natants were aliquoted into microcentrifuge tubes and stored at
slides were washed three times in 1× DPBS and then twice in hydration −80 °C for ELISA. The secreted form of ERBB receptor ligands was
buffer. Sample slides were equilibrated in staining buffer for 30 min and assessed by performing ELISAs for HB-EGF (Quantikine (DHBEG0;
incubated in the antibodies (Supplementary Table 9) diluted in staining R&D Systems)), TGFA (Quantikine (DTGA00; R&D Systems)) and EREG
buffer plus N Blocker, G Blocker, J Blocker and S Blocker overnight at (Epiregulin BioAssay ELISA kit (382783; USBiological Life Sciences))
4 °C. After antibody incubation, sample slides were washed twice in according to the manufacturers’ protocols. Absorbance at 450 nm
Staining Buffer and fixed for 10 min in 1.6% paraformaldehyde (15710; was measured using a FLUOstar Omega-BMG LABTECH' microplate
Electron Microscopy Sciences) in storage buffer. Sample slides were reader. The absorbance signal from co-culture media was utilized
washed three times in 1× DPBS and incubated in ice-cold methanol for for background correction. The standard curve was constructed by
5 min. After incubation in methanol, sample slides were washed three plotting the standards and used to calculate the ligand concentration
times in 1× DPBS and incubated in a final fixative solution (1 ml 1× DPBS in supernatant. Three biological replicates were used for each cell
+ 20 µl Akoya’s final fixation reagent) for 20 min at room temperature. line and treatment condition.
Nature Genetics

Article https://doi.org/10.1038/s41588-025-02158-6
Colony formation assay the FindVariableFeatures function. We also excluded genes that were
THP-1 cells were plated onto 0.4-µm polyethylene clear cell inserts highly patient specific from the highly variable genes by aggregating
for 24-well plates (9320412; cellQART) at 2 × 105 cells per well in pseudo-bulk count matrices across patients and then filtered out
500 µl complete media supplemented with 100 ng ml−1 phorbol genes with a Gini index value of >0.8. The data were scaled to compute
12-myristate 13-acetate and incubated for 72 h. Neuroblastoma cells PCA embeddings. UMAP embeddings and Louvain clustering with a
were plated onto 24-well plates at a density of 1,000 cells per well resolution of 0.2 were conducted based on the first 30 principal com-
(CHLA15 and NB1643) or 500 cells per well (CHLA20) in 1 ml co-culture ponents. The clusters mostly contained cells from a single patient,
media (2% FBS-supplemented RPMI and IMDM mixture plus1% except cluster 33 (1,804 cells), which contained a mixture of cells from
insulin-transferrin-selenium). After washing the THP-1 macrophages different patients. This cluster of cells was therefore suspected to
on the inserts with DPBS twice, they were transferred to neuroblastoma be non-neoplastic and removed from subsequent analysis. We then
plates with the addition of 500 µl co-culture media. Macrophages and integrated all of the malignant cells using Harmony56 along with the
neuroblastoma cells were co-cultured for 7 d, refreshing the media on patient identifier. The UMAP embeddings and Louvain clustering
day 4. Macrophages on inserts were discarded and neuroblastoma cells were computed on the first 20 components of the Harmony-derived
were fixed with 4% paraformaldehyde (15710-S; Electron Microscopy dimensional reduction with a resolution of 0.2.
Sciences) for 20 min at room temperature. After permeabilization
with 0.3% Triton X-100 (T8532; Sigma–Aldrich) in DPBS for 10 min, Integration and annotation of macrophage subsets in
cells were stained with 0.5% crystal violet (V5265; Sigma–Aldrich) snRNA-seq data
for 3 h at room temperature. Plates were air-dried, followed by the Macrophages were extracted from the full snRNA-seq data object and
removal of excess stain with Milli-Q water. To examine the role of the processed using the standard Seurat pipeline, as described above,
ErbB pathway on colony formation, 100 nM afatinib (S1011; Selleck and reintegrated with Harmony using the same protocol as for the
Chemicals) or 4 µg ml−1 CRM197 was added to the co-culture media. malignant cells. Cells were clustered in Seurat based on the first 20
Neuroblastoma cells without an insert served as monoculture controls. components of the Harmony-derived dimensional reduction using a
Images of colonies were obtained by scanning the whole plate with resolution of 0.4. Cell clusters with >5% of cells previously predicted
an at the highest resolution and analyzed with ImageJ as previously to be malignant by artificial neural network classifier were filtered out
described52. Briefly, the following steps were applied to obtain the total for downstream analysis. The remainder were reprocessed using the
colony area and average colony size: (1) enhance the local contrast; (2) same Seurat pipeline and Harmony integration. Briefly, the top 1,000
make binary; (3) apply Gaussian blur with a two-pixel radius; (4) make highly variable genes were used to scale the data and calculate PCA
binary; (5) watershed; (6) select the target well in the plate; (6) set the embeddings. Harmony integration was then performed on the first 20
measurements area and area fraction; and (7) analyze the particles. principal components along each patient identifier. Subsequently, all
macrophages were clustered and UMAP embeddings were calculated
snRNA-seq data processing and integration based on the first 20 components of the Harmony-derived dimensional
Raw reads were aligned to the Genome Reference Consortium Human reduction with a resolution of 0.4. Differentially expressed genes were
Build 38 patch release 13 (GRCh38.p13) assembly and quantified among calculated for each population using the FindAllMarkers function with
the genes using Cell Ranger version 3.1.0. High-quality cells were main- the parameters max.cells.per.ident = 500, min.pct = 0.05 and min.diff.
tained if their unique molecular identifier count was between 2,000 pct = 0.05. Each macrophage was manually annotated based on signifi-
and 40,000 and they expressed between 1,000 and 10,000 genes and cant differentially expressed genes41. Cells identified as dendritic cells
<10% of unique molecular identifiers mapped to mitochondrial genes. (cluster 6; Extended Data Fig. 6a) were removed before downstream
The filtered cells were normalized with log normalization using Seurat analysis. No discrete monocyte cluster was observed, so the remaining
version 3 (ref. 53). The doublets identified with DoubletFinder54 with cells were subsequently annotated as TAM subsets.
default parameters were also removed. Reads from ambient RNA were
removed from the raw counts using decontX55 and the decontaminated snATAC-seq data processing, integration and cell type
matrices were rounded up to the nearest integer and renormalized with annotation
log normalization using Seurat version 3. snATAC-seq data for each sample were preprocessed using Cell Ranger
The normalized expression matrices were integrated using recip- ATAC version 1.1.0 (10x Genomics) to generate FASTQ files, which
rocal principal component analysis (PCA) implemented in Seurat were then processed using the process module of scATAC-pro57 (ver-
version 3. Specifically, the Seurat object with all cells was first split sion 1.5.1) with the default parameters. We aligned the raw reads to
by patient identifier and the top 2,000 highly variable genes were the GRCh38.p13 assembly using the Burrows–Wheeler Aligner (ver-
identified using the SelectIntegrationFeatures function in Seurat. sion 0.7.17)58. Peaks were called using MACS2 (ref. 59). We defined
We excluded genes that were highly patient specific from the highly high-quality cells to have between 5,000 and 100,000 total fragments,
variable genes by aggregating pseudo-bulk count matrices across <15% mitochondrial reads and a >25% fraction of reads in peaks. The
patients. We then filtered out genes with a Gini index value of >0.8. peak-by-cell count matrix was constructed and used for downstream
Genes expressed in <0.2% of cells within all patients were further analyses. To integrate data from all patients, we first merged the peaks
removed from the highly variable gene list. Cells were subsequently from different samples if two peaks were within 500 base pairs of each
integrated using the FindIntegrationAnchors function in Seurat, with other using the mergePeaks module of scATAC-pro. The peak-by-cell
the parameter k.anchor set to 10. The integrated data were then scaled count matrix was then reconstructed based on the merged peaks using
for PCA. Uniform manifold approximation and projection (UMAP) the reConstMtx module of scATAC-pro. We pooled matrices from all
embeddings were computed using the first 50 PCA dimensions for samples and loaded them into Seurat with an extra ChromatinAssay
visualization. Louvain clustering was run using the first 50 principal added. The data were then integrated using Signac60 as follows. The
components with the resolution parameter set to 0.2. The cell types Seurat object was split by patient identifier and each patient subset
of clusters were manually assigned using marker genes. was then normalized using the RunTFIDF function. Top features were
identified using FindTopFeatures with the min.cutoff parameter set
Integration of neoplastic cells in snRNA-seq data to 1% of the number of cells present in the subset and a singular value
Putative neoplastic cells were first pooled and processed using the decomposition was computed using the RunSVD function. Data were
standard Seurat pipeline, as implemented above with minor modifica- then integrated using the FindIntegrationAnchors function with the
tions. Briefly, the top 2,500 highly variable genes were selected using parameters reduction = rlsi, anchor.features = 10000, k.anchor = 30
Nature Genetics

Article https://doi.org/10.1038/s41588-025-02158-6
and dims = 2:50, followed by the IntegrateEmbedding function with peak were included. However, since we only obtained a few differen-
the parameters k.anchor = 30 and dims = 2:50. A UMAP embedding tially accessible peaks for the Interm-OXPHOS state, instead of using
was constructed and the cells were clustered with Louvain clustering differentially accessible peaks to filter enhancer peaks, we utilized all
(at a resolution of 0.4) using the integrated latent semantic indexing peaks accessible in >20% of Interm-OXPHOS cells to filter enhancer
reduction and dimensions 2–50. peaks for this state. Transcription factors were incorporated into the
Cells in the integrated snATAC-seq were annotated using the network if they were either differentially expressed or had differential
Seurat label transfer pipeline. Briefly, the integrated and annotated motif activity and were expressed in at least 20% of the cells within a
snRNA-seq data were used as the reference. Gene activity scores were given cell state. Lastly, the target genes in a network were restricted to
calculated on the snATAC-seq data using the GeneActivity function in the differentially expressed genes in each cell state.
Signac. Subsequently, we normalized the gene activity matrix using
Seurat log normalization. We employed the FindTransferAnchors Survival analysis
function with the parameters reduction = cca and k.anchor = 20, fol- For survival analysis, we used bulk RNA-seq data generated for 498
lowed by the TransferData function with the parameters dims = 2:50 patients with clinical information in the Sequencing Quality Control
and k.weight = 50 in Seurat to predict the cell types for each cell in the project31 study and 419 patients with clinical information in a dataset
snATAC-seq data. Each cell cluster was then annotated as the cell type published by Cangelosi et al.32 downloaded from the R2 database.
most frequently predicted within the cluster. Overall and event-free survival data were retrieved from the published
clinical annotations and processed with the Surv function in the R
Neoplastic cell state identification in snATAC-seq data survival package64. We conducted two types of survival analyses. For
To understand the chromatin state of each neoplastic cell state iden- the first type of analysis, the signature score of a neoplastic cell state
tified via snRNA-seq, we identified the putative malignant cells in was dichotomized into high and low categories as greater than or less
snATAC-seq as follows. All snATAC-seq cells were initially pooled than the median. A Cox proportional hazards regression model was fit
and processed using the Seurat/Signac pipeline as described but to the survival object to access the significance of the dichotomized
without integration. After clustering and visualization on a UMAP signature using the coxph function in the R survival package. For the
projection, all cells within patient-specific clusters (>90% cells from second type of analysis, patients were grouped into different neoplastic
a single patient) previously annotated as neuroblasts, fibroblasts or cell states based on maximum cell state signature scores. Subsequently,
Schwann cells in the integrated snATAC-seq data were defined as puta- a Cox proportional hazards regression model was fit to the survival
tive neoplastic cells. Then, we reintegrated the putative neoplastic object to access the significance of the cell state assignment, with the
cells using the Signac pipeline, as described above, with the exception ADRN-calcium state as the baseline. In both cases, MYCN amplification
that Louvain clustering was performed using dimensions 2–30 of the event, sex and age were included as additional covariates in the model.
integrated latent semantic indexing embedding and a resolution of Kaplan–Meier survival curves were generated using the ggsurvplot
0.2. Lastly, to map individual cells in the snATAC-seq data to the tran- function in the R ggsurvfit package.
scriptionally defined cell states, we applied the Seurat label transfer
pipeline. We employed the FindTransferAnchors function with the Cell–cell interaction analysis
parameters reduction = cca and k.anchor = 15, followed by the Trans- We computed the crosstalk between subsets of the neoplastic and
ferData function with the parameters dims = 2:30 and k.weight = 50. macrophage cells using our recently developed method, CytoTalk42.
Cells with a maximum prediction score of <0.6 were removed from This algorithm predicts functionally significant ligand–receptor inter-
downstream analysis. actions in single-cell sequencing data by analyzing both intercellular
and intracellular gene networks downstream of receptor activation.
Transcriptional regulatory network analysis For each pair of neoplastic and macrophage states, we first randomly
The transcriptional regulatory network for each neoplastic cell state sampled 5,000 cells from the neoplastic subset and 2,000 cells from
was constructed as described previously61,62 with minor modifications. the macrophage subset for each combination. Subsequently, we
We first co-embedded the malignant cells in snATAC-seq and snRNA-seq executed CytoTalk for all cell state pairs, restricting the analysis to
data per sample using the Seurat multimodality co-embedding pipe- genes expressed in at least 10% (default) of either cell state. The cross-
line. Each snATAC- and snRNA-seq sample was processed separately, talk scores were visualized as a dotplot. To evaluate the robustness of
followed by application of the FindTransferAnchors function with ErbB signaling, we employed two additional approaches, CellChat65
the parameters reduction = cca and k.anchor = 30, followed by the and LIANA66, to analyze interactions between all neoplastic and mac-
TransferData function with default parameters. Then, we identified rophage states, as well as other normal cell types. Each population was
metacells using the R package hdWGCNA63 with the parameters k = 25, randomly downsampled to 5,000 cells when more than 5,000 cells were
max_shared = 3, min_cells = 100, reduction = pca and ident.group = seu- observed. For CellChat default parameters were applied, whereas for
rat_clusters. Metacells containing between 5 and 15 snRNA-seq cells LIANA we set the parameter resource = all.
were retained for further analysis. The gene-by-metacell expression
matrix and peak-by-metacell accessibility matrix were calculated as CODEX data processing
the average normalized expression and normalized accessibility of all Cell segmentation was conducted via Mesmer67 for each image. To
cells within the metacell, respectively. Metacells from different samples generate the necessary input of a two-channel tag image file format
were then combined and the enhancer–promoter interactions were (TIFF), we used DAPI for the nuclear channel and a fused channel of
predicted using a linear regression model for each gene on metacells, CD45, vimentin and NaK-ATPase for the membrane channel. The mean
with the gene expression in each metacell as the dependent variable pixel intensity was extracted from each cell segmentation mask, yield-
and the accessibility of the peaks within ±500 kilobases of the gene pro- ing a cell-by-protein matrix that was carried forward for analysis in
moter as the independent variables. Significant enhancer–promoter Scanpy68. Cells with a very low or high raw DAPI intensity (<10 or >250
interactions were defined based on a peak regression coefficient of >0.2 on a UINT8 scale) were removed. Each image was manually cropped to
and a Benjamini–Hochberg-adjusted P value of <0.01. Transcription exclude large areas of artifact including tissue folding and detachment,
factor–target gene pairs were defined if the transcription factor motif debris and edge artifact. Each sample was then internally normalized
was present at the enhancer of a predicted enhancer–promoter interac- using the centered log ratio across all features, which is recommended
tion. To obtain robust networks, only enhancer–promoter interactions for the analysis of protein expression, as in CITE-seq data. Samples
with differential accessibility across neoplastic states in the enhancer were then merged into one object and integrated using Harmony58.
Nature Genetics

Article https://doi.org/10.1038/s41588-025-02158-6
Subsequently, scaling, PCA, UMAP and Leiden clustering were per- References
formed on this combined object. Each cluster was manually annotated 52. Choudhry, P. High-throughput method for automated colony and
based on the top differentially expressed proteins. CODEX data were cell counting by digital image analysis based on edge detection.
visualized using QuPath version 0.4 and Napari version 0.4.18. PLoS ONE 11, e0148469 (2016).
53. Hao, Y. et al. Integrated analysis of multimodal single-cell data.
Xenium spatial transcriptomics on TH-MYCN mice Cell 184, 3573–3587.e29 (2021).
A Xenium spatial transcriptomic experiment was performed on six 54. McGinnis, C. S., Murrow, L. M. & Gartner, Z. J. DoubletFinder:
TH-MYCN+/+ mice (Supplementary Methods). FFPE mouse tissue sec- doublet detection in single-cell RNA sequencing data using
tions (5 µm) were prepared on Xenium slides using Xenium Prime artificial nearest neighbors. Cell Syst. 8, 329–337.e4 (2019).
Sample Preparation Reagents. Slides were deparaffinized, rehydrated 55. Yang, S. et al. Decontamination of ambient RNA in single-cell
and decrosslinked, followed by hybridization with Xenium 5K Mouse RNA-seq with DecontX. Genome Biol. 21, 57 (2020).
PTP Priming Oligos and probes targeting messenger RNA. Probes were 56. Korsunsky, I. et al. Fast, sensitive and accurate integration of
ligated, amplified and washed, with subsequent antibody staining for single-cell data with Harmony. Nat. Methods 16, 1289–1296 (2019).
cell segmentation. Autofluorescence quenching and nuclei staining 57. Yu, W., Uzun, Y., Zhu, Q., Chen, C. & Tan, K. scATAC-pro: a
were performed and slides the were stored in phosphate-buffered comprehensive workbench for single-cell chromatin accessibility
saline with tween-20 (PBS-T) at 4 °C. The Xenium Analyzer (version 3.1) sequencing data. Genome Biol. 21, 94 (2020).
was used for imaging, decoding, segmentation and cell assignment, 58. Li, H. & Durbin, R. Fast and accurate short read alignment with
following the manufacturer’s protocols. Burrows–Wheeler transform. Bioinformatics 25, 1754–1760 (2009).
59. Zhang, Y. et al. Model-based analysis of ChIP-seq (MACS).
Statistics and reproducibility Genome Biol. 9, R137 (2008).
No statistical method was used to predetermine sample size. All avail- 60. Stuart, T., Srivastava, A., Madad, S., Lareau, C. A. & Satija, R.
able longitudinal specimens at the Children’s Hospital of Philadelphia Single-cell chromatin state analysis with Signac. Nat. Methods 18,
meeting the inclusion criteria were profiled and all data meeting the 1333–1341 (2021).
standard quality control threshold were included. The investigators 61. Chen, C. et al. Single-cell multiomics reveals increased
were not blinded to allocation during genomics profiling and the plasticity, resistant populations, and stem-cell-like blasts in
assessment of patient data. Randomization and blinding were used for KMT2A-rearranged leukemia. Blood 139, 2198–2211 (2022).
all of the in vitro experiments. A one-sided Wilcoxon signed-rank test 62. Sussman, J. H. et al. A longitudinal single-cell and spatial
for paired samples was used to compare the percentages of cell type multiomic atlas of pediatric high-grade glioma. Preprint at bioRxiv
proportions between patient-matched samples. As the Wilcoxon test https://doi.org/10.1101/2024.03.06.583588 (2024).
is non-parametric, we did not formally test for normality of the data. 63. Morabito, S., Reese, F., Rahimzadeh, N., Miyoshi, E. & Swarup, V.
Statistical analysis of sequencing and imaging data was conducted in hdWGCNA identifies co-expression networks in high-dimensional
R version 4.2. Analysis of in vitro data was conducted using the Welch’s transcriptomics data. Cell Rep. Methods 3, 100498 (2023).
one-sided paired or unpaired t-test in R, as indicated in the correspond- 64. Therneau, T. A Package for Survival Analysis in R. R package
ing figure captions. The dose-response inhibition tool in GraphPad version 3.8-3 https://CRAN.R-project.org/package=survival
Prism was used to calculate drug half-maximum inhibitory concentra- (2024).
tion values. All representative images were replicated independently 65. Jin, S., Plikus, M. V. & Nie, Q. CellChat for systematic analysis of
at least twice to ensure reproducibility. In all cases, box plots indicate cell-cell communication from single-cell transcriptomics. Nat.
median values, hinges mark the 25th and 75th percentiles and whiskers Protoc. 20, 180–219 (2025).
extend 1.5 times the interquartile range. 66. Dimitrov, D. et al. Comparison of methods and resources for cell–
cell communication inference from single-cell RNA-seq data. Nat.
Reporting summary Commun. 13, 3224 (2022).
Further information on research design is available in the Nature 67. Greenwald, N. F. et al. Whole-cell segmentation of tissue images
Portfolio Reporting Summary linked to this article. with human-level performance using large-scale data annotation
and deep learning. Nat. Biotechnol. 40, 555–565 (2022).
Data availability 68. Wolf, F. A., Angerer, P. & Theis, F. J. SCANPY: large-scale single-cell
Data from this study have been deposited in the Human Tumor Atlas gene expression data analysis. Genome Biol. 19, 15 (2018).
Network data portal (https://humantumoratlas.org/publications/ 69. Tan, K. & Yu, W. Additional data: longitudinal single-cell multiomic
hta4_2025_nature-genetics_wenbao-yu). For the snRNA-seq, snATAC-seq atlas of high-risk neuroblastoma reveals chemotherapy-induced
and WGS data, this includes sequencing reads and processed data (read tumor microenvironment rewiring. Zenodo https://doi.
alignments, gene-by-cell or peak-by-cell matrices and variant call files). org/10.5281/zenodo.14261274 (2024).
We also deposited the processed snRNA-seq data in the CELLxGENE data- 70. Yu, W. & Pang, M. Wbaopaul/NBL_scMultiomics_Paper: V1.0.
base at https://cellxgene.cziscience.com/collections/cee845e3-ec04- Zenodo https://doi.org/10.5281/ZENODO.14728432 (2025).
4781-9e2a-28734bb4f7ba for easy interactive exploration. For the
CODEX data, this includes multi-channel images, segmentation masks Acknowledgements
and marker-by-cell matrices. For all data types, Seurat objects with We acknowledge staff at the Children’s Hospital of Philadelphia
annotations and dimensional reductions are provided. The linkage Center for Childhood Cancer Research Biobank for collecting tissue
between Human Tumor Atlas Network patient IDs and sample IDs is and curating clinical information used in this study and the Children’s
provided in Supplementary Table 2. The processed Xenium transcrip- Hospital of Philadelphia Pathology Core, Flow Cytometry Core,
tomic and scRNA-seq data in the mono- and co-culture experiments have High-Throughput Sequencing Core and Research Information Services
been deposited to the Zenodo repository at https://doi.org/10.5281/ for providing technical support. We are grateful to all of the patients
zenodo.14261274 (ref. 69). Source data are provided with this paper. and their families who volunteered to participate in this study. This
work was supported by a National Cancer Institute Human Tumor Atlas
Code availability Network grant under award number U2C CA233285 (K.T.). Additional
Source code created for this study is publicly available at https://github. support was provided by the National Institutes of Health (grants
com/tanlabcode/NBL_scMultiomics_Paper and ref. 70. U54 HL165442 (to K.T.) and T32 CA009140 (to R.B.-S.)) and American
Nature Genetics

Article https://doi.org/10.1038/s41588-025-02158-6
Cancer Society (Institutional Research Grant IRG-22-150-41-IRG to Competing interests
W.Y.). K.T. holds the Richard and Sheila Sanford Endowed Chair at the The authors declare no competing interests.
Children’s Hospital of Philadelphia.
Additional information
Author contributions Extended data is available for this paper at
W.Y., R.B.-S., Y.U., C.-H.C. and K.T. conceived of and designed the https://doi.org/10.1038/s41588-025-02158-6.
study. L.D.G., T.P., K.B. and J.M.M. provided patient samples. R.B.-S.,
C.-H.C., A.T., P.G., A.Y. and M.Z. performed the experiments and Supplementary information The online version contains supplementary
generated the data. W.Y., Y.U., M.P., C.-Y.W., D.W.W., J.H.S., Z.Z. and material available at https://doi.org/10.1038/s41588-025-02158-6.
C.C. performed the computational and statistical analyses.
W.Y., R.B.-S., Y.U., C.-H.C., J.H.S., L.F.S., D.M., C.S.T., M.D.H., S.B., Correspondence and requests for materials should be addressed
J.H. and C.T. performed the data interpretation and biological to Kai Tan.
analysis. W.Y., M.D.H., K.B., N.R.Z., J.M.M. and K.T. provided funding
and supervised the study. W.Y., R.B.-S., J.H.S. and K.T. wrote the Reprints and permissions information is available at
manuscript with input from all authors. www.nature.com/reprints.
Nature Genetics

Article https://doi.org/10.1038/s41588-025-02158-6
Extended Data Fig. 1 | Quality assessment of snRNA-seq and snATAC-seq in the snATAC-seq data. d) Cell type composition of each sample based on snRNA-
data. a) Bar plots showing the number of cells sequenced (top) and the number seq data. e) Scatter plot of cell type proportions in snRNA-seq and snATAC-seq
of genes detected per cell (bottom) in each snRNA-seq sample after quality data. Each dot represents a sample. Pearson correlation coefficient was indicated
control filtering. b) Bar plots showing the number of cells sequenced (top) and in the plot. f) Shifts in cell type proportion between diagnosis and post-therapy
the number of unique chromatin fragments detected per cell (bottom) in each samples in snATAC-seq data. Samples from the same patient between time points
snATAC-seq sample after quality control filtering. c) Dot plot showing the average were connected by a grey line (n = 22 pairs). Statistical significance was assessed
gene activity and percentage of cells with gene activity for cell type marker genes using a one-sided Wilcoxon signed-rank test.
Nature Genetics

Article https://doi.org/10.1038/s41588-025-02158-6
Extended Data Fig. 2 | See next page for caption.
Nature Genetics

Article https://doi.org/10.1038/s41588-025-02158-6
Extended Data Fig. 2 | Malignant cell calling by using whole genome the Curve (AUC) is shown inside the plot. e) Correlation between histologic
sequencing (WGS) and snRNA-seq data. a) Genome segmentation for two estimation of neoplastic cell percentage by pathologists (x-axis) and predicted
representative patients using whole genome sequencing (WGS). Black points malignant cell proportions (y-axis). Each dot represents an individual sample.
are equal sized bins. Red line shows the Hidden Markov Model (HMM) copy Linear regression line is shown in red. Pearson correlation coefficient (r) is shown.
number states. b) Heatmaps of copy number alteration profiles from samples in Significance was assessed using a two-sided test for association between paired
(a) using snRNA-seq data derived from Clonalscope. c) UMAP representation of samples. f) Heatmaps of inferCNV results of representative patient samples
cells from snRNA-seq data from samples in (a) colored by predicted malignant or after inference of putative normal cells (top panels) and neoplastic cells (bottom
non-malignant prediction. d) Receiver Operating Characteristics (ROC) curve for panels). Known recurrent neuroblastoma copy number variations (CNVs) are
supervised classification by artificial neural networks. Value of the Area Under highlighted with a magenta box.
Nature Genetics

Article https://doi.org/10.1038/s41588-025-02158-6
Extended Data Fig. 3 | Malignant cell annotation and survival analysis. and post-therapy timepoints. e) Malignant cell state proportions in snRNA-seq
a) Barplot of fraction of malignant cells in each cell type. b) Heatmap showing data of each patient across timepoints, ALK mutation, and MYCN amplification
normalized expression of top 15 up-regulated genes in each neoplastic cell state, status. f) The changes in cell state proportions between diagnosis and post-
down sampled to 100 cells per state for illustration purpose. c) Heatmap of top therapy samples stratified by MYCN amplification status. (n = 11 MYCN-amplified,
15 enriched Gene Ontology Biological Process terms for each neoplastic cell 11 MYCN-non-amplified). The one-sided Wilcoxon rank-sum test was used to
state. d) Stacked barplots of neoplastic cell state proportions between diagnosis calculate significance.
Nature Genetics

Article https://doi.org/10.1038/s41588-025-02158-6
Extended Data Fig. 4 | Projection of neoplastic cells onto normal adrenal d) Heatmap showing the enrichment of projected cell types for neoplastic cell
medullary developmental trajectories. a) Stacked barplots of projected cell states. Pearson residuals were first calculated based on the contingency table to
type proportions across initial diagnosis and post-therapy samples. b) Shifts in test the independence of the projected cell type from the neoplastic cell states.
projected cell type proportions for each patient between initial diagnosis and The p-value for each cell in the heatmap was calculated based on the assumption
post-therapy time points. Samples from the same patient at different time that the Pearson residual follows a normal distribution. The enrichment score
points were connected by a grey line (n = 22 pairs). Significance was assessed was defined as the -log10(p-value) multiplied by the sign of the Pearson residual.
using a one-sided Wilcoxon signed-rank test. SCPs, Schwann cell precursors. e) The reference UMAP of normal adrenal medullary developmental trajectories.
c) Heatmap showing projected cell type fractions for each neoplastic cell state. f) Visualization of neoplastic cells on the reference UMAP stratified by cell state.
Nature Genetics

Article https://doi.org/10.1038/s41588-025-02158-6
Extended Data Fig. 5 | See next page for caption.
Nature Genetics

Article https://doi.org/10.1038/s41588-025-02158-6
Extended Data Fig. 5 | Survival analysis of neoplastic cell state signatures. (c, e) and maximum cell state signature score (d, f) as in (a) and (b) respectively.
a) Kaplan-Meier curves of event free survival based on neoplastic cell states using P-values in a-f were calculated using the Cox proportional hazards model and
the Sequencing Quality Control project (SEQC) neuroblastoma RNA-seq dataset. adjusted by age, sex and MYCN amplification status with no multiple comparison
Patients were stratified into high and low groups based on the median value adjustment. g-h) Comparison of proportions of neoplastic cell states based on
of the cell state signature score. b) Kaplan-Meier curves of event free survival the deconvolution of SEQC (g) and Cangelosi et al. (h) datasets between MYCN-
based on the maximum cell state signature scores in the SEQC dataset. amplified and MYCN non-amplified samples. MYCN-amplified, non-amplified: n
Patients were grouped based on the cell state with the maximum signature = 96 and 401 (g); n = 84 and 333 (h). i-j) Comparison of proportions of neoplastic
score. The number of samples and p-value for each group are indicated in cell states based on the deconvolution of SEQC (i) and Cangelosi et al. (j) datasets
the parentheses. The ADRN-Calcium state was chosen as the baseline. between disease stages. Stage1, 2, 3, 4s, 4: n = 120, 78, 62, 52, 181 (i); n = 59, 70, 56,
c-f) Kaplan-Meier curves of overall survival (c-d) and event free survival 49, 184 (j).The one-sided Wilcoxon rank-sum test was used to calculate statistical
(e-f) using the Cangelosi et al. RNA-seq dataset based on patient stratification significance (g-j).
Nature Genetics

Article https://doi.org/10.1038/s41588-025-02158-6
Extended Data Fig. 6 | See next page for caption.
Nature Genetics

Article https://doi.org/10.1038/s41588-025-02158-6
Extended Data Fig. 6 | Neoplastic cell states in snATAC-seq data. a) UMAP of and associated chromatin peaks in each neoplastic cell state: SMC4 (ADRN-
integrated snATAC-seq data (93,261 cells) annotated by neoplastic cell clusters. Proliferating), APOE (MES), ZIC2 (ADRN-Baseline), KCNQ3 (ADRN-Calcium), DBH
b) Patient proportions in each of the snATAC-seq clusters. c-e) Coverage plots (ADRN-Dopaminergic), RPL32 (Interm-OxPhos) loci. The E-P link track represents
showing normalized chromatic accessibility for each neoplastic cell state at the the predicted enhancer-promoter links colored by the regression coefficient,
YAP1 (c), PHOX2B (d), and MYCN (e) loci. f) Dot plot of the average gene activity and the TF motifs present at the enhancer peaks are indicated. The differential
and percentage of accessible cells of the ADRN and MES genes for each predicted accessible peaks (DAPs) for the corresponding cell state are highlighted in blue
neoplastic population. g) Coverage plots for differentially expressed genes and yellow for promoter and enhancer peaks, respectively.
Nature Genetics

Article https://doi.org/10.1038/s41588-025-02158-6
Extended Data Fig. 7 | See next page for caption.
Nature Genetics

Article https://doi.org/10.1038/s41588-025-02158-6
Extended Data Fig. 7 | Epigenetic regulation of neoplastic cell states. a) Shifts color indicates direction of gene expression change between diagnosis and
in cell state proportions in snATAC-seq between diagnosis and post-therapy post-therapy samples in each cell state. The edge weight is proportional to the
samples. Samples from the same patient at different time points were connected linear regression coefficient for the predicted enhancer-promoter interaction
by a grey line (n = 13 pairs). Significance was assessed using a one-sided and the fraction of cells that are accessible at the enhancer peak. d) Fractions
Wilcoxon signed-rank test. b) Heatmap of top 20 transcription factors (TFs) with of state-specific genes in each TRN that were upregulated, downregulated, or
differential motif chromatin accessibility in each cell state. c) Transcriptional non-significantly changed post-therapy. e) Coverage plot showing normalized
regulatory networks (TRNs) for ADRN-Dopaminergic, ADRN-Baseline and chromatin accessibility and gene expression for the MES state-specific gene
Interm-OxPhos cell states. Diamond represents TF and circle represents target NECTIN2. The E-P link track represents the predicted enhancer-promoter links
gene. The size of a TF node is proportional to the average difference in motif colored by the regression coefficient, and the TF motifs present at the enhancer
chromatin accessibility z-score between a given cell state and the rest of cell peaks are indicated. The differential accessible peaks (DAPs) for the MES state are
states. The size of a target gene node is proportional to the average fold change highlighted in blue and yellow for promoter and enhancer peaks, respectively.
of gene expression between a given cell state and the rest of cell states. Node
Nature Genetics

Article https://doi.org/10.1038/s41588-025-02158-6
Extended Data Fig. 8 | Therapy-induced shifts in macrophage populations. Wilcoxon signed-rank test (n = 22 pairs). e) Macrophage subset proportions
a) UMAP plots of macrophages from snRNA-seq data clustered at different in snRNA-seq data of each patient across timepoints, ALK mutation, and
resolutions. b) Stacked bar plots of macrophage subset proportions in snRNA- MYCN amplification status. f-g) Proportions of macrophage subsets in initial
seq data at diagnosis and post-therapy timepoints. c) Representative signature diagnostic samples. Patients were grouped according to their responses to
genes for immunosuppressive (A2M, CD84, HLA-E, SPP1), angiogenic (VCAN, induction chemotherapy (f) and adverse clinical events (g). A one-sided t-test was
VEGFA, VAV2, CXCR4), phagocytic (MERTK, MRC1) and proinflammatory (IL18, performed to compare the proportion of IL18+ macrophages between two patient
CD80) macrophages. d) Proportions of THY1+ and proliferating macrophages in groups, as indicated by the vertical dashed line; p = 0.005 (f) and 0.02 (g).
diagnosis and post-therapy samples. Significance was assessed using a one-sided
Nature Genetics

Article https://doi.org/10.1038/s41588-025-02158-6
Extended Data Fig. 9 | See next page for caption.
Nature Genetics

Article https://doi.org/10.1038/s41588-025-02158-6
Extended Data Fig. 9 | Clinical correlation and transcriptomic validation of from macrophage subsets. d) Normalized gene expression of ERBB4 ligands
macrophage populations. a) Comparison of macrophage subset proportions (HB-EGF, EREG, TGFA) in different macrophage subsets from DX and PTX samples,
between MYCN amplified and non-amplified neuroblastoma patients using upregulated post-therapy using logistic regression with no multiple comparison
CIBERSORTx deconvolution of bulk RNA-seq data (SECQ and Cangelosi et adjustment (Methods) e) Cell-cell interaction analysis using CellChat and LIANA.
al. datasets). MYCN-amplified, non-amplified: n = 96 and 401 (SEQC); n = 84 Left, HB-EGF-ERBB4-mediated interactions among neoplastic cell states and
and 333 (Cangelosi et al.). b) Comparison of macrophage subset proportions non-neoplastic cells by CellChat. Macrophage subsets are colored in blue and
between disease stages in bulk RNA-seq data as in (a). Stage 1, 2, 3, 4s, 4: n = neoplastic populations are colored in red. Right, Top 10 ligand-receptor pairs
120, 78, 62, 52, 181 (SEQC); n = 59, 70, 56, 49, 184 (Cangelosi et al.). Significance identified between VCAN+ macrophages (ligand source) and neoplastic cell
was assessed in (a-b) using a one-sided Wilcoxon signed-rank test. c) Dot plot states (receptor source) by LIANA using three representative signaling pathway
showing predicted ligand-receptor interactions between neoplastic cell states databases. HB-EGF-ERBB4 interaction is highlighted in red.
and macrophage subsets. Ligands were from neoplastic cells and receptors were
Nature Genetics

Article https://doi.org/10.1038/s41588-025-02158-6
Extended Data Fig. 10 | See next page for caption.
Nature Genetics

Article https://doi.org/10.1038/s41588-025-02158-6
Extended Data Fig. 10 | Annotation and protein expression in CODEX spatial between neighbors of ADRN-like-2 (ERBB4hi) neuroblasts and the neighbors
imaging. a) List of CODEX panel markers for different cell types. b) UMAP of other neuroblasts (top), and between diagnosis and post-therapy samples
visualization of the ~841,000 cells in CODEX data. c) Stacked barplot of cell type (bottom). The density was defined as the mean expression of TGFA on cells within
proportions across samples in the CODEX dataset. d) Heatmap of normalized a 40 µm square, excluding the marker within the center cell. Significance was
protein expression across cell types in CODEX data. e) Representative images of assessed using a two-sided Wilcoxon rank-sum test. The numbers of cells are:
CODEX immunofluorescence, cell phenotype mask (CPM), and hematoxylin and n=655,573 and 17,532 (top); n = 221,677 and 451,428 (bottom). h) Distance from
eosin (H&E) stain for selected cell types. f) Hematoxylin and eosin (H&E) image each neuroblast cell to the nearest CD163+CD206hi macrophage across samples,
(left) and cell phenotype mask (right) of representative images for each CODEX stratified by neuroblast population. Significance was assessed using a two-sided
sample. g) Comparison of the density of TGFA protein quantified by CODEX Wilcoxon rank-sum test. Outliers were truncated for visualization purposes.
Nature Genetics

1
nature
portfolio
|
reporting
summary
April
2023
Kai Tan
Corresponding author(s):
Last updated by author(s): 02/03/2025
Reporting Summary
Nature Portfolio wishes to improve the reproducibility of the work that we publish. This form provides structure for consistency and transparency
in reporting. For further information on Nature Portfolio policies, see our Editorial Policies and the Editorial Policy Checklist.
Statistics
For all statistical analyses, confirm that the following items are present in the figure legend, table legend, main text, or Methods section.
n/a Confirmed
The exact sample size (n) for each experimental group/condition, given as a discrete number and unit of measurement
A statement on whether measurements were taken from distinct samples or whether the same sample was measured repeatedly
The statistical test(s) used AND whether they are one- or two-sided
Only common tests should be described solely by name; describe more complex techniques in the Methods section.
A description of all covariates tested
A description of any assumptions or corrections, such as tests of normality and adjustment for multiple comparisons
A full description of the statistical parameters including central tendency (e.g. means) or other basic estimates (e.g. regression coefficient)
AND variation (e.g. standard deviation) or associated estimates of uncertainty (e.g. confidence intervals)
For null hypothesis testing, the test statistic (e.g. F, t, r) with confidence intervals, effect sizes, degrees of freedom and P value noted
Give P values as exact values whenever suitable.
For Bayesian analysis, information on the choice of priors and Markov chain Monte Carlo settings
For hierarchical and complex designs, identification of the appropriate level for tests and full reporting of outcomes
Estimates of effect sizes (e.g. Cohen's d, Pearson's r), indicating how they were calculated
Our web collection on statistics for biologists contains articles on many of the points above.
Software and code
Policy information about availability of computer code
Data collection No software was used for data collection
Data analysis Publicly available tools were used for data analysis, statistics and visualization, with specific tools and versions described in the methods
section, and listed below.
Software:
R (v. 4.2.3)
Python (v.3.10.4)
GraphPad Prism 9
R packages:
Seurat (v4.0.5)
harmony (v0.1.1)
survival (v3.5.5 )
ggsurvfit (v0.3.1)
edgeR (v.3.40.2)
InferCNV v1.6.0
chromVAR (v1.12.0 )
Signac (v1.12.0)
enrichR (v3.2)

2
nature
portfolio
|
reporting
summary
April
2023
Sequence Analysis
cellranger v3.1.0 --patient cohort
cellranger v7.1.0-- in vitro experiment
cellranger-atac v1.1.0
scATAC-pro v1.5.1
chromVARmotifs (v0.2.0)
Clonalscope (v1.0.1)
CODEX and Xenium data analysis
Akoya’s-Fusion (v1.0.8)
Mesmer(v0.12.9)
QuPath (v0.4)
Napari (v0.4.18)
Scanpy (v1.10.3)
Xenium Analyzer (v 3.1)
Squipdy (v 1.6.1)
Custom Codes
https://github.com/tanlabcode/NBL_scMultiomics_Paper
For manuscripts utilizing custom algorithms or software that are central to the research but not yet described in published literature, software must be made available to editors and
reviewers. We strongly encourage code deposition in a community repository (e.g. GitHub). See the Nature Portfolio guidelines for submitting code & software for further information.
Data
Policy information about availability of data
All manuscripts must include a data availability statement. This statement should provide the following information, where applicable:
- Accession codes, unique identifiers, or web links for publicly available datasets
- A description of any restrictions on data availability
- For clinical datasets or third party data, please ensure that the statement adheres to our policy
Data from this study have been deposited at the Human Tumor Atlas Network (HTAN) data portal: https://humantumoratlas.org/publications/hta4_2025_nature-
genetics_wenbao-yu. For the snRNA-seq, snATAC-seq and WGS data this includes sequencing reads and processed data including read alignments, gene-by-cell or
peak-by-cell matrices, and variant call files. We also deposited the processed snRNA-Seq data to the CELLxGENE database at https://cellxgene.cziscience.com/
collections/cee845e3-ec04-4781-9e2a-28734bb4f7ba for easy interactive exploration. For the CODEX data, this includes multi-channel images, segmentation
masks, and marker-by-cell matrix. For all data types, Seurat objects with annotations and dimensional reductions are provided for each data type. The linkage
between HTAN patient IDs and sample IDs is provided in Supplementary Table 2. The processed Xenium transcriptomic and scRNA-seq data in the mono- and co-
culture experiments have been deposited to Zenodo repository: https://doi.org/10.5281/zenodo.14261274.
Research involving human participants, their data, or biological material
Policy information about studies with human participants or human data. See also policy information about sex, gender (identity/presentation),
and sexual orientation and race, ethnicity and racism.
Reporting on sex and gender All patients in the cohort were male or female according to biological sex when available, and no information on gender
identity was collected.
Reporting on race, ethnicity, or Race or ethnicity is reported when available, but is not relevant to the methods or findings of the present study. In our
other socially relevant computational models, each patient is considered as variable feature which accounts for confounding factors that may be
groupings specific to a particular patient. However, the cohort size is not large enough in order to conduct subgroup analyses based on
race.
Population characteristics 22 patients with pediatric high-risk neuroblastoma were enrolled in the study. The cohort’s age ranged from 6 months to 13
years and had a male-to-female ratio of 0.57. The tumor specimens were resected from multiple anatomic locations, detailed
in Supplementary Table 1.
Recruitment Primary samples were obtained from patients with high-risk neuroblastoma banked at the Children’s Hospital of Philadelphia
(CHOP) Childhood Cancer Research (CCCR) Registry. The patient selection was built based on specimen availability.
Ethics oversight Biorepositories were obtained with parent informed consent according to the Declaration of Helsinki and Institutional Review
Board approval from the Children's Hospital of Philadelphia
Note that full information on the approval of the study protocol must also be provided in the manuscript.
Field-specific reporting
Please select the one below that is the best fit for your research. If you are not sure, read the appropriate sections before making your selection.
Life sciences Behavioural & social sciences Ecological, evolutionary & environmental sciences

3
nature
portfolio
|
reporting
summary
April
2023
For a reference copy of the document with all sections, see nature.com/documents/nr-reporting-summary-flat.pdf
Life sciences study design
All studies must disclose on these points even when the disclosure is negative.
Sample size No sample size calculation was performed. The number of patient samples was primarily determined by the availability of tumor samples in
the biobank at the Children’s Hospital of Philadelphia (CHOP) Childhood Cancer Research (CCCR) Registry. Sample size was limited majorly due
to the rarity of neuroblastoma.
Data exclusions All sample with reasonable sample quality as assessed histologically and that passed standard QC filters after processing were included in the
analysis. Sample QC for scRNA-seq and scATAC-seq is summarized in Extended Data Figure 1.
Replication Two regions (replicates) per sample were used for each patient to perform snRNA-seq data. No replication was performed for WGS, snATAC-
seq and CODEX experiments due to lack of materials. The in vitro experiments were successfully done on 2-5 replicates (the detailed n for
each experiment was given in the legend of figure6). The in vivo experiment was successfully performed on 3 mice per condition.
Randomization Randomization was not applicable because this is retrospective study for clinical and genomic analyses. Therefore, patients were already
determined to have particular disease subtypes and/or treatments and could not be randomized into groups solely for the purpose of this
study.
Blinding Blinding was not applicable because this is retrospective study for clinical and genomic analyses. Therefore, patient metadata was already
available and known by researchers a priori in order to select appropriate samples for our cohort design. All sequencing and sample
preparations were blinded and randomized.
Reporting for specific materials, systems and methods
We require information from authors about some types of materials, experimental systems and methods used in many studies. Here, indicate whether each material,
system or method listed is relevant to your study. If you are not sure if a list item applies to your research, read the appropriate section before selecting a response.
Materials & experimental systems Methods
n/a Involved in the study n/a Involved in the study
Antibodies ChIP-seq
Eukaryotic cell lines Flow cytometry
Palaeontology and archaeology MRI-based neuroimaging
Animals and other organisms
Clinical data
Dual use research of concern
Plants
Antibodies
Antibodies used Antigen,Clone(s),Vendor,Catalogue Number,Dilution
Na/K-ATPase,EP1845Y,Abcam,ab167390,1:50
ERBB4,182803,R&D Systems,MAB1131,1:50
ALK,POLYCLONAL,Thermo Fisher Scientific,51-3900,1:50
NCAM-1/ CD56,POLYCLONAL,Novus Biologicals,AF2408,1:50
CD8,C8/144B,Akoya Biosciences,ab256584,1:200
aSMA,POLYCLONAL,Abcam,ab5694,1:50
HBEGF,POLYCLONAL,R&D Systems,AF-259-NA,1:29
MRP4,EPR20403,Abcam,ab235624,1:63
NLRP3,768319,Novus Biologicals,MAB7578,1:50
CD206,5C11,Novus Biologicals,H00004360-M02,1:50
Ki67,B56,Akoya Biosciences,4250019,1:200
GYPC,POLYCLONAL,Thermo Fisher Scientific,PA5-80680,1:50
TrKB,POLYCLONAL,Novus Biologicals,AF1494,1:50
TGFA,EPR15346,Abcam,ab224266,1:50
CD4,EPR6855,Akoya Biosciences,4550112,1:200
CD68,KP1,Akoya Biosciences,4550113,1:200
SERCA2,EPR9392,Abcam,ab238426,1:50
ISL1,EPR10362,Abcam,ab238919,1:50
CD45,D9M81,Akoya Biosciences,4550121,1:200
CD11c,EP1347Y,Abcam,ab216655,1:50
GD2,14G2a,Biolegend,357302,1:83
L1CAM,L1-OV198.5,Biolegend,371602,1:50
C1QC,EPR2984Y,Abcam,ab247391,1:50

4
nature
portfolio
|
reporting
summary
April
2023
CD105,EPR19911-220,Abcam,ab252345,1:50
CLSTN2,POLYCLONAL,Novus Biologicals,AF5480,1:50
CD3E,EP449E,Akoya Biosciences,4550119,1:200
PPP2R2C,6D1,Novus Biologicals,H00005522-M01,1:50
PHOX2B,EPR14423,Abcam,ab216456,1:50
BMP7,164311,R&D Systems,MAB3541,1:50
CD31,EP3095,Akoya Biosciences,4250009,1:200
MYCN,D4B2Y,Cell Signaling Technology,69006SF,1:50
CD20,L26,Akoya Biosciences,4450018,1:200
CD163,EDHu-1,Novus Biologicals,NB110-40686,1:50
Vimentin,RV202,Novus Biologicals,NBP1-97672,1:50
Nestin,196908,Novus Biologicals,MAB1259,1:50
IL1RAPL1,MM0353-3R16,Novus Biologicals,NBP2-11648,1:50
CD2,EPR6451,Abcam,ab131276,1:50
SV2C,3D8,Novus Biologicals,H00022987-M01,1:50
Akt, Not Applicable, Cell Signaling Tech (CST), 9272, 1:1000
Phospho-Akt (Ser473) (p-AKT), (D9E) XP, Cell Signaling Tech (CST), 4060, 1:1000
p44/p42 MAPK (Erk1/2), Not Applicable, Cell Signaling Tech., 9102, 1:1000
Phospho-p44/42 MAPK (Erk1/2) (Thr202/Tyr204), 197G2, Cell Signaling Tech.,4377, 1:1000
α-Tubulin, 11H10, Cell Signaling Tech., 2125, 1:1000
HBEGF, ARC0663, Invitrogen, MA5-35148, 1:1000
Beta-Actin, 15G5A11/E2, Invitrogen, MA1140, 1:10000
Anti-rabbit IgG-HRP linked, Not Applicable, Cell Signaling Tech., 7074, 1:5000
Anti-mouse IgG-HRP-linked, Not Applicable, Millipore Sigma, A5906, 1:10000
Validation All conjugated primary antibodies commercially available from Akoya Biosciences have been extensively validated for different
Human FFPE tissue samples on Phenocycler fusion (CODEX) by the manufacturer. Antibody dilution was used as recommended by
Akoya Biosciences. Further information on the validation and titration of these antibodies can be found or requested on the
manufacturer’s website.
Antibodies acquired from other manufacturers were conjugated in house and titrated on Phenocycler fusion to determine the
appropriate antibody dilutions for Human Neuroblastoma FFPE tissue samples. Validation using immunohistochemistry (IHC) for
these antibodies has been described on their respective manufacturer’s website as below:
Anti-human Sodium Potassium ATPase antibody, ab167390 (https://www.abcam.com/en-us/products/primary-antibodies/sodium-
potassium-atpase-antibody-ep1845y-bsa-and-azide-free-ab167390).
Potassium ATPase antibody has also been tested for CODEX in the below paper,
https://www.sciencedirect.com/science/article/pii/S0092867420308709#app2.
Anti-human ErbB4/Her4 antibody, MAB1131 (https://www.rndsystems.com/products/human-erbb4-her4-
antibody-182803_mab1131).
Anti-human ALK Polyclonal antibody, 51-3900 (https://www.thermofisher.com/antibody/product/ALK-Antibody-Polyclonal/51-3900).
Anti-human NCAM-1/CD56 antibody, AF2408 (https://www.novusbio.com/products/ncam-1-cd56-antibody_af2408).
Anti-human alpha smooth muscle Actin antibody, ab5694 (https://www.abcam.com/en-us/products/primary-antibodies/alpha-
smooth-muscle-actin-antibody-ab5694). Anti-human alpha smooth muscle Actin antibody has also been tested for CODEX in the
below paper,
https://www.sciencedirect.com/science/article/pii/S0092867420308709#app2.
Anti-human HB-EGF antibody, AF-259-NA (https://www.rndsystems.com/products/human-hb-egf-antibody_af-259-na).
Anti-human MRP4 antibody, ab235624 (https://www.abcam.com/en-us/products/primary-antibodies/mrp4-antibody-epr20403-bsa-
and-azide-free-ab235624).
Anti-human NLRP3/NALP3 antibody, MAB7578 (https://www.novusbio.com/products/nlrp3-nalp3-
antibody-768319_mab7578#PublicationSection).
Anti-human MMR/CD206/Mannose Receptor antibody, H00004360-M02 (https://www.novusbio.com/products/mmr-cd206-
mannose-receptor-antibody-5c11_h00004360-m02).
Anti-human GYPC Polyclonal antibody, PA5-80680 (https://www.thermofisher.com/antibody/product/GYPC-Antibody-Polyclonal/
PA5-80680).
Anti-human TrkB antibody, AF1494 (https://www.rndsystems.com/products/human-mouse-rat-trkb-antibody_af1494).
Anti-human TGF alpha antibody, ab224266 (https://www.abcam.com/en-us/products/primary-antibodies/tgf-alpha-antibody-
epr15346-bsa-and-azide-free-ab224266?srsltid=AfmBOorGXiBeh0prkP-rJgdyA4n82zilVZ2hjvDewlfUrmch2l50aayr).
Anti- human SERCA2 ATPase antibody, ab238426 (https://www.abcam.com/en-us/products/primary-antibodies/serca2-atpase-
antibody-epr9392-bsa-and-azide-free-ab238426?srsltid=AfmBOorA9v7g9pYj_MQatadg2TPo7hxeUTlO7zOj9z-dQq-twIRwfOLT).
Anti-Islet 1 (ISL1) antibody, ab238919 (https://www.abcam.com/en-us/products/primary-antibodies/islet-1-antibody-epr10362-bsa-
and-azide-free-ab238919?srsltid=AfmBOoru2DH_2ZKu-V3fBiT6qo3v1aab5MHeGukwoM9DdxFbu4sLBhLI).
Anti-human CD11c antibody, ab216655 (https://www.abcam.com/en-us/products/primary-antibodies/cd11c-antibody-ep1347y-bsa-
and-azide-free-ab216655?srsltid=AfmBOopbRbqbaHOfqGhlOftT37ypW5SWuVg2nsnN3-b2qzy0jI3Upy0I). Anti-human alpha smooth
muscle Actin antibody, ab5694 (https://www.abcam.com/en-us/products/primary-antibodies/alpha-smooth-muscle-actin-antibody-
ab5694). Anti-human CD11c antibody has also been tested for CODEX in the below paper,
https://www.sciencedirect.com/science/article/pii/S0092867420308709#app2.
Anti-human Ganglioside GD2 antibody, 357302 has been tested on Phenocyler fusion in house and has been shown to co-label with
PHOX2B.
Anti-human L1CAM antibody, 371602 (https://www.biolegend.com/fr-fr/products/purified-anti-human-cd171-l1cam-
antibody-13167).
Anti-human C1QC antibody, ab247391 (https://www.abcam.com/en-us/products/primary-antibodies/c1qc-antibody-epr2984y-bsa-
and-azide-free-ab247391?srsltid=AfmBOopLRh8fH89VLkFFwHjeH0m6x_cKWIOQAxFsYLxAm5K9-ayl01Qm).
Anti-human CD105 antibody, ab252345 (https://www.abcam.com/en-us/products/primary-antibodies/cd105-antibody-
epr19911-220-ab252345?srsltid=AfmBOop-v8-29jTnkqMsGGDqgDytKhmdjtby4j0XBwmKAV_RAHYD7cf1).
Anti- human Calsyntenin-2 (CLSTN2) antibody, AF5480 (https://www.novusbio.com/products/calsyntenin-2-antibody_af5480?
srsltid=AfmBOoqPhLsvygT4MHF91F9QJhXo5mqOn0Oluj0_2Nmt9W4gz5jLauPc).

5
nature
portfolio
|
reporting
summary
April
2023
Anti-human PPP2R2C Monoclonal antibody, H00005522-M01 (https://www.thermofisher.com/antibody/product/PPP2R2C-Antibody-
clone-6D1-Monoclonal/H00005522-M01).
Anti-human PHOX2B antibody, ab216456 (https://www.abcam.com/en-us/products/primary-antibodies/phox2b-antibody-epr14423-
bsa-and-azide-free-ab216456?srsltid=AfmBOooCV2yvCfVuAaP6z4bG3C7AxqL3bS2t9i7U3xuUktmY5DuiCJr2).
Anti-human BMP-7 antibody, MAB3541 (https://www.rndsystems.com/products/human-bmp-7-antibody-164311_mab3541).
Anti-human N-Myc antibody, 69006SF (https://www.cellsignal.com/products/primary-antibodies/n-myc-d4b2y-rabbit-mab-bsa-and-
azide-free/69006?srsltid=AfmBOoqi9Bgh0DIaZ17eAe2JqFe2s-Ghjp77l5H6HJWdu_GjwqNhvCQ4).
Anti-human CD163 antibody, NB110-40686 (https://www.novusbio.com/products/cd163-antibody-edhu-1_nb110-40686?
srsltid=AfmBOopNKfF2tzf6rO6VtWluC68ggNsGwn9V4ZtKGFReiRHyTbAKmt6g). Anti-human CD163 antibody has also been tested for
CODEX in the below paper,
https://www.sciencedirect.com/science/article/pii/S0092867420308709#app2.
Anti-human Vimentin antibody, NBP1-97672 (https://www.novusbio.com/products/vimentin-antibody-rv202_nbp1-97672?
srsltid=AfmBOoq2goGXvk04dqThrZ99VAHLqdtX0ySJ2tZvPv8DfBcZqdwA1JYO). The same clone RV202 has been validated on CODEX in
the below paper, Reference: https://www.sciencedirect.com/science/article/pii/S0092867420308709#app2.
Anti-human Nestin antibody, MAB1259 (https://www.rndsystems.com/products/human-nestin-antibody-196908_mab1259).
Anti-human IL1RAPL1 antibody, NBP2-11648PE has been tested on Phenocyler fusion in house and has been shown to co-label with
PHOX2B.
Anti-human CD2 antibody, ab131276 (https://www.abcam.com/en-us/products/primary-antibodies/cd2-antibody-epr6451-
ab131276?srsltid=AfmBOop9p874apaVyj-Veg0slT7rAmX0B0Gsw20Ae-zdzXEko3Kg7r2T#).
Anti-human SV2C antibody, H00022987-M01 (https://www.novusbio.com/products/sv2c-antibody-3d8_h00022987-m01?
srsltid=AfmBOork7csmRBm43OBGM7X0UnDULC3GmPJPDcVA-TiM-xZ3xm_Ipwsa).
Akt, 9272, https://www.cellsignal.com/products/primary-antibodies/akt-antibody/9272
Phospho-Akt (Ser473) (p-AKT), 4060, https://www.cellsignal.com/products/primary-antibodies/phospho-akt-ser473-d9e-xp-rabbit-
mab/4060
p44/p42 MAPK (Erk1/2), 9102, https://www.cellsignal.com/products/primary-antibodies/p44-42-mapk-erk1-2-antibody/9102
Phospho-p44/42 MAPK (Erk1/2) (Thr202/Tyr204), 4377, https://www.cellsignal.com/products/primary-antibodies/phospho-p44-42-
mapk-erk1-2-thr202-tyr204-197g2-rabbit-mab/4377
(cid:2)-Tubulin, 2125, https://www.cellsignal.com/products/primary-antibodies/a-tubulin-11h10-rabbit-mab/2125
HBEGF, MA5-35148, https://www.thermofisher.com/antibody/product/HBEGF-Antibody-clone-ARC0663-Recombinant-Monoclonal/
MA5-35148
Beta-Actin, MA1140, https://www.thermofisher.com/antibody/product/beta-Actin-Antibody-clone-15G5A11-E2-Monoclonal/
MA1-140
Anti-rabbit IgG-HRP linked, 7074, https://www.cellsignal.com/products/secondary-antibodies/anti-rabbit-igg-hrp-linked-
antibody/7074
Anti-mouse IgG-HRP-linked, A5906, https://www.sigmaaldrich.com/US/en/product/sigma/a5906?
msockid=39d4b736592f618a38dda470589f6008
Eukaryotic cell lines
Policy information about cell lines and Sex and Gender in Research
Cell line source(s) Neuroblastoma (NBL) cell lines, NB1643, CHLA15, CHLA20, COG-N-297 and COG-N-590
were requested from the COG/ALSF Childhood Cancer Repository (www.CCcells.org). THP-1
(Cat # TIB-202) cell line was purchased from American Type Culture Collection (ATCC).
Authentication All above cell lines were authenticated using STR profiling by the Penn Genomics and Sequencing Core at University of
Pennsylvania.
Mycoplasma contamination Mycoplasma test was done and no contamination was detected
Commonly misidentified lines No commonly misidentified cell lines were used.
(See ICLAC register)
Animals and other research organisms
Policy information about studies involving animals; ARRIVE guidelines recommended for reporting animal research, and Sex and Gender in
Research
Laboratory animals 129x1/SvJ mice transgenic for the TH-MYCN construct were originally obtained from Bill Weiss (University of California, San
Francisco). The six mice we used were aged 44,51,52, 52, 52,and 55 days, respectively.
TH-MYCN hemizygous mice were bred, and offspring were genotyped from tail-snip-isolated DNA using qPCR. Tumors are fully
penetrant and arise at autochthonous sites in an immunocompetent host with lethality by day 60 of life.
Mice were monitored for tumors by palpation by a single experienced animal technician and randomized to a treatment arm when
tumors were small to medium in size (~0.8 grams tumor by necropsy in n=3 control mice): vehicle (PBS) or 20 mg/kg dose of
cyclophosphamide by intraperitoneal injection (IP) three times (Monday/Wednesday/Friday) for 2 weeks. Mice were weighed and
assessed for tumor growth and symptoms at least three times weekly. Mice were euthanized for pre-defined humane endpoints
related to overall health or tumor burden (hunching, immobility, hindlimb paresis, weight loss, respiratory distress).
For all experiments, mice were maintained at three to four mice per cage under humidity and temperature-controlled conditions
with a light/dark cycle that is set at 12-hours. Animals were maintained under microisolator tops in a HEPA-filtered rack. Animals
were fed autoclaved Purina mouse chow and water ad libitum. Handling was performed with universal sterile precautions and

6
nature
portfolio
|
reporting
summary
April
2023
experienced personnel will perform all procedures. Mice were sacrificed, and tissues harvested, consistent with the recommendation
of the Panel of Euthanasia of the American Veterinary Medical Association. Animal sacrifice is performed by administration of
isoflurane or CO2 sedation followed by cervical dislocation. This methodology is consistent with the recommendations of the Panel
on Euthanasia of the American Veterinary Medical Association.
Wild animals No wild animals were used in this study.
Reporting on sex The use of male or female mice was randomly selected for each patient sample.
Field-collected samples No filed-collected samples were used in this study.
Ethics oversight Mice were purchased from the Jackson Laboratory to establish a breeding colony at the Children’s Hospital of Philadelphia (CHOP)
and mouse bred in the colony were used for experiments. All animals were housed in the laboratory animal facility (LAF) vivarium in
the Colket Translational Research Building (CTRB) at CHOP. The LAF is accredited by the American Association for Accreditation of
Laboratory Animal Care (AAALAC), registered with the USDA and complies with the Public Health Service Policy on Humane care and
Use of Laboratory Animals (Section: A3442-01). Additionally, the LAFs activities involving animals comply with the Guide for the Care
and use of Laboratory Animals. Animal work in our laboratory was reviewed and approved by our Institutional Animal Care and
Utilization Committee (21-000232, most recent re-approval 5/07/2024).
Note that full information on the approval of the study protocol must also be provided in the manuscript.
Clinical data
Policy information about clinical studies
All manuscripts should comply with the ICMJE guidelines for publication of clinical research and a completed CONSORT checklist must be included with all submissions.
Clinical trial registration No study protocol was provided for the current study because this is profiled study for clinical and genomic analyses of surgical
patients at the Children's Hospital of Philadelphia.
Study protocol No study protocol was provided for the current study because this is profiling study for clinical and genomic analyses of surgical
patients at the Children's Hospital of Philadelphia.
Data collection Patients received standard therapy and excess tissue samples were utilized for genomic profiling. No additional interventions were
performed and this study did not alter the clinical care of the patients in any way.
Outcomes No pre-determined primary and secondary outcomes because this is profiling study for clinical and genomic analyses.
Plants
Seed stocks N/A
Novel plant genotypes N/A
Authentication N/A