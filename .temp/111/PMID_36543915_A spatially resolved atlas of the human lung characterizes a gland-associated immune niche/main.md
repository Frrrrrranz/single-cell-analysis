nature genetics
Article https://doi.org/10.1038/s41588-022-01243-4
A spatially resolved atlas of the human
lung characterizes a gland-associated
immune niche
| Elo Madissoon1,2,11, Amanda J. Oliver  |     |     |   1,11, Vitalii Kleshchevnikov1,  |     |     |     |
| -------------------------------------- | --- | --- | --------------------------------- | --- | --- | --- |
Received: 26 July 2022
| Anna Wilbrey-Clark1, Krzysztof Polanski  |     |     |     |   1, Nathan Richoz3,  |     |     |
| ---------------------------------------- | --- | --- | --- | --------------------- | --- | --- |
Accepted: 25 October 2022
|     |   1,4, Lira Mamanova  |     |   1, Liam Bolt1, Rasa Elmentaite  |     |     |   1,  |
| --- | --------------------- | --- | --------------------------------- | --- | --- | ----- |
Ana Ribeiro Orsi
Published online: 21 December 2022 J. Patrick Pett    1, Ni Huang1, Chuan Xu1, Peng He    1,2, Monika Dabrowska1,
| Sophie Pritchard1, Liz Tuck  |     |   1, Elena Prigmore  |     |   1, Shani Perera1,  |     |     |
| ---------------------------- | --- | -------------------- | --- | -------------------- | --- | --- |
 Check for updates
| Andrew Knights1, Agnes Oszlanczi1, Adam Hunter1, Sara F. Vieira  |                              |     |                                         |                               |   1,    |       |
| ---------------------------------------------------------------- | ---------------------------- | --- | --------------------------------------- | ----------------------------- | ------- | ----- |
| Minal Patel1, Rik G. H. Lindeboom                                |                              |     |   1, Lia S. Campos1, Kazuhiko Matsuo5,  |                               |         |       |
| Takashi Nakayama                                                 |   5, Masahiro Yoshida        |     |                                         |   6, Kaylee B. Worlock        |   6,    |       |
| Marko Z. Nikolić                                                 |   6, Nikitas Georgakopoulos  |     |                                         |   7, Krishnaa T. Mahbubani    |         |   7,  |
| Kourosh Saeb-Parsy                                               |   7, Omer Ali Bayraktar      |     |                                         |   1, Menna R. Clatworthy1,3,  |         |       |
| Oliver Stegle1,8,9, Natsuhiko Kumasaka                           |                              |     |   1, Sarah A. Teichmann                 |                               |   1,10  |       |
| & Kerstin B. Meyer                                               |   1                          |     |                                         |                               |         |       |
Single-cell transcriptomics has allowed unprecedented resolution of
cell types/states in the human lung, but their spatial context is less well
defined. To (re)define tissue architecture of lung and airways, we profiled
five proximal-to-distal locations of healthy human lungs in depth using
multi-omic single cell/nuclei and spatial transcriptomics (queryable at
lungcellatlas.org). Using computational data integration and analysis,
we extend beyond the suspension cell paradigm and discover macro
and micro-anatomical tissue compartments including previously
unannotated cell types in the epithelial, vascular, stromal and nerve bundle
micro-environments. We identify and implicate peribronchial fibroblasts in
lung disease. Importantly, we discover and validate a survival niche for IgA
plasma cells in the airway submucosal glands (SMG). We show that gland
epithelial cells recruit B cells and IgA plasma cells, and promote longevity
and antibody secretion locally through expression of CCL28, APRIL and
IL-6. This new ‘gland-associated immune niche’ has implications for
respiratory health.
A comprehensive understanding of cells and micro-environments  adaptive immunity through well-defined mucosa-associated lymphoid
that define lung function is important for reducing the impact of lung  tissue (MALT), such secondary lymphoid structures have not been
diseases, which currently rank third for mortality causes worldwide1.  reported in the healthy human lung2. The LungMAP and human lung cell
In addition to its main role in gas exchange, the lung has an impor- atlas (HLCA) consortia3,4 have harnessed recent advances in single-cell
tant barrier function. While other mucosal barrier tissues orchestrate  and single-nucleus RNA sequencing (scRNA-seq and snRNA-seq)5 and
A full list of affiliations appears at the end of the paper.   e-mail: st9@sanger.ac.uk; km16@sanger.ac.uk
Nature Genetics | Volume 55 | January 2023 | 66–77 66

Article https://doi.org/10.1038/s41588-022-01243-4
generated a number of atlases characterizing lung cell types across new subsets, including a rare cell type, termed immune recruiting
species, health and disease6–10,11. fibroblasts (IR-fibro). IR-fibro cells expressed the chemokines CCL19
Current atlases have prioritized parenchyma tissue, with few and CCL21 and other marker genes of fibroblast reticular cells and fol-
studies examining the full depth of the airways. Here we carried out licular dendritic cells (fDC), which together are responsible for T and
deep tissue profiling from deceased organ donors’ healthy lungs and B cell positioning in secondary lymphoid organs (Fig. 2c)14–16. These
airways, allowing characterization of cell types along the proximal to cells were mapped to rare immune infiltrates in the bronchus with
distal axis of the respiratory tree. We use unbiased spatial transcrip- ST and were validated by multiplexed single molecule FISH (smFISH)
tomics (ST) approach to contextualize cell types and states within (Fig. 2d and Extended Data Fig. 3a, b). The amount of immune infil-
tissue micro-environments in the healthy human lung and airways, trates present in our healthy donors was consistent with a previous
adding a key dimension to the HLCA. In total, we sequenced 129,340 study17. The gene signature of germinal center fibroblasts from Peyer’s
single cells and 63,768 single nuclei and performed Visium ST on 20 Patches18 also mapped to the immune infiltrate captured by Visium
tissue sections from human trachea, bronchi, and upper and lower ST, further supporting the similarity of IR-fibros to lymphoid organ
parenchyma. These data and CellTypist automated annotation mod- stromal cells (Extended Data Fig. 3b). In conclusion, we describe an
els are available at lungcellatlas.org as a resource for data download, IR-fibro population with a likely role in immune cell recruitment. Using
suspension and spatial gene expression analysis, as well as automated its newly defined marker genes, this population can also be detected in
annotation of new datasets. Overall, we distinguished 80 cell types and the HLCA10.
states, including 11 populations not annotated in previous lung atlas
studies. Many of these populations express disease-associated genes Peribronchial and perichondrial fibroblasts. Two fibroblast popu-
highlighted by functional genome-wide association studies (fGWAS) lations, both enriched in the airways, were annotated based on their
analysis. Our in-depth tissue profiling coupled with spatial genomics specific mapping around the airway epithelium (peribronchial fibro-
reconstructs known tissue micro-environments in the lungs and air- blasts—PB-fibro) and the cartilage (perichondrial fibroblasts—PC-fibro)
ways at full molecular breadth. Going beyond known units of cellular (Fig. 2b,e,g and Extended Data Fig. 2b). We uncover the transcriptome
organization, we identify a previously undefined immune niche for IgA for human PB-fibro, consistent with the key protein markers COL15A1
plasma cells at the airway submucosal glands (SMG). and ENTPD1 (Extended Data Fig. 4a,b). fGWAS analysis, which quanti-
fies systematic associations between cell-type-specific genes and
Results disease-associated SNPs18, revealed that PB-fibros are linked to lung
A spatial, multi-omics atlas of human lung and airways function measured by FEV1/FVC ratio, the decrease of which is associ-
We applied scRNA-seq and snRNA-seq, VDJ-seq and ST to deep tissue ated with lung diseases such as chronic obstructive pulmonary disease
samples from five locations across the human lung and airway (Fig. 1a (COPD) (Fig. 2f and Supplementary Table 8). We annotated PB-fibros in
and Supplementary Tables 1–3 and 9) to capture structures such as a single-cell dataset of COPD and idiopathic pulmonary fibrosis (IPF)
cartilage, muscle and the SMG (Extended Data Fig. 1a; ‘Methods’). patients8,10 and found a number of COPD-upregulated genes that had
In total, 193,108 cells and nuclei were annotated into broad cell previously been associated with lung function (FEV1/FVC) and emphy-
type groups as follows: epithelial, immune, erythroid, endothelial and sema/COPD (Extended Data Fig. 4c and Supplementary Table 10)19–21.
stromal cells. Cells were annotated according to consensus marker In addition, we found that PB-fibros were reproducibly enriched in
genes and naming from other lung studies including the integrated IPF patients compared to healthy controls in the Adams et al. (ref. 8)
HLCA10 and LungMAP12 (Fig. 1b, Extended Data Fig. 1b and Supplemen- dataset and the HLCA10, further implicating them as a key cell type in
tary Table 4). Using Visium ST on 20 tissue sections from five locations lung disease (Extended Data Fig. 4d,e).
and the cell2location13 algorithm (Supplementary Fig. 1), we assessed PC-fibros, like chondrocytes, were enriched in single nuclei data
the spatial distribution of cells in distinct tissue micro-environments (Fig. 2b). We found analogous marker expression of COL12A1 around
(Supplementary Table 5). Essentially, the tool determines which cell the cartilage in the Human Protein Atlas (HPA) (Extended Data Fig. 4f),
types from suspension data in which abundance could explain the supporting cell2location mapping of PC-fibro (Fig. 2g). We identified
mRNA counts observed in the Visium data. As expected, well-described bone development genes LRG4/6 (ref. 22) along with fibroblast markers
cell types mapped to their known locations such as ciliated epithelial in PC-fibros, placing these as an intermediate cell type in a trajectory
cells to the lumen of the airway surrounded by basal cells and alveolar from adventitial fibroblasts to chondrocytes (Extended Data Fig. 4g,h).
type 1 (AT1) and 2 (AT2) cells to lung parenchyma (Fig. 1c,d). To exam- PC-fibros express genes causing skeletal abnormalities in humans
ine differential cell composition related to the sampling locations, (Extended Data Fig. 4i), including FLNB and FGFR2, suggesting the
donors and protocols used, we used a Poisson linear mixed model to relevance of PC-fibros in supporting cartilage functions and related
identify the contribution of each technical variable (Methods; Fig. 1e abnormalities23,24.
and Supplementary Fig. 2). Different dissociation protocols enriched
for specific cell type groups but had little effect (less than 1% of the total Four distinct cell types in airway peripheral nerves. Finally, we
variance) on gene expression (Extended Data Fig. 1c). identified the following four new clusters relating to airway periph-
Highlighting our comprehensive approach, we transcriptionally eral nerves: myelinating Schwann cells (mSchwann) (NFASC, NCMAP,
defined chondrocytes in human lungs (ACAN, CHAD, COL9A3, HAPLN1 MBP and PRX), nonmyelinating Schwann cells (nmSchwann) (NGFR,
and CYTL1; Extended Data Fig. 1d,e) and mapped them to airway car- SCN7A, CHD2, L1CAM and NCAM1)25–28, endoneurial nerve-associated
tilage (Fig. 1c,d). Chondrocytes were mostly released using single fibroblasts (NAF) (SOX9 and OSR2)25 and perineurial NAF (SLC2A1 and
nuclei sequencing from trachea (Fig. 1e, Extended Data Fig. 1e,f and ITGA6)25,29 (Extended Data Fig. 5a). nmSchwann and mSchwann cell
Supplementary Table 7) and were not present at all in the integrated marker genes were enriched in cell adhesion and myelination gene sets,
HLCA10, demonstrating the utility of our multi-omics, multilocation respectively (Extended Data Fig. 5b,c), with EVX1, a key gene in spinal
human lung atlas. cord development, identified as a potential regulator of mSchwann
cells in the airways. Both mSchwann and nmSchwann expressed periph-
Rare fibroblasts with immune recruiting properties. The sequen- eral nervous system disease genes (Extended Data Fig. 5d). Localiza-
tial clustering of fibroblasts identified 11 distinct fibroblast clusters tion of these populations in peripheral nerves was validated with bulk
(Fig. 2a,b and Extended Data Fig. 2a,b). We annotated previously RNA-seq across tissues (Extended Data Fig. 5e), Visium ST (Extended
described myofibroblasts, mesothelial, adventitial and alveolar fibro- Data Fig. 5f), protein staining (Extended Data Fig. 5g–i) and smFISH
blasts11 (Extended Data Fig. 2c–e and Supplementary Table 4) and seven (Fig. 2i and Extended Data Fig. 5j). We show perineurial NAFs
Nature Genetics | Volume 55 | January 2023 | 66–77 67

| Article |     |     |     |     |     |     |     |     |     | https://doi.org/10.1038/s41588-022-01243-4 |     |     |     |     |
| ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------ | --- | --- | --- | --- |
| a       |     |     |     |     |     |     |     |     |     | b                                          |     |     |     |     |
Mesenchyme
|     |     |           |     | Dissociation  | Enrichment |           |     |         |     |            |     |     |     |             |
| --- | --- | --------- | --- | ------------- | ---------- | --------- | --- | ------- | --- | ---------- | --- | --- | --- | ----------- |
|     |     |           |     | enzyme        |            |           |     |         |     | n = 52,749 |     |     | LE  |             |
|     |     |           |     |               | CD45+ /    |           |     |         |     |            |     | VE  |     |             |
|     |     |           |     | Liberase /    |            | scRNA-seq |     | VDJ-seq |     |            |     |     |     |             |
|     |     |           |     | trypsin /     | CD45– /    |           |     |         |     |            |     |     |     | Epithelium  |
|     |     | Top left  |     | collagenase   | none       |           |     |         |     |            |     |     | AT1 | n = 51,809  |
Fibroblast
|     | Trachea | parenchyma | Fresh |     |     |     |     | +   |     |     |     |     |     |     |
| --- | ------- | ---------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Chondrocyte
SMG
Muscle
Location
|     | Bronchi 2–3 |     |     | 1   | 2 3 4 5 |     |     |     |     |     |     | AT2 |     |     |
| --- | ----------- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Basal
|     |           |     |     | 1       |        |           |     |     |     |           |         |             | Secretory |          |
| --- | --------- | --- | --- | ------- | ------ | --------- | --- | --- | --- | --------- | ------- | ----------- | --------- | -------- |
|     | Bronchi 4 |     |     | ronoD 2 | Pool 1 |           |     |     |     |           |         |             |           |          |
|     |           |     |     |         | Pool 2 |           |     |     |     |           |         | Erythrocyte |           |          |
|     |           |     |     | 3       |        |           |     |     |     |           | Myeloid |             |           |          |
|     |           |     |     | 4       | Pool 3 | snRNA-seq |     | ST  |     | Mast cell |         |             |           | Ciliated |
Pool 4
|     | Lower left  |     |        | 5   |        |     |     |     |     |     |          |     |     |     |
| --- | ----------- | --- | ------ | --- | ------ | --- | --- | --- | --- | --- | -------- | --- | --- | --- |
|     | parenchyma  |     |        |     | Pool 5 |     |     |     |     |     |          |     |     |     |
|     |             |     | Frozen |     |        |     | +   |     |     |     | B plasma |     |     |     |
T & NK
|     |     |     |     |     |     |     |     |     |     |     | B cell |     |     | UMAP2 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | ----- |
Immune
n = 85,164
| c   |     |     |     |     |     |     | d   |     |     |     |     |     |     | UMAP1 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |
Cell type group abundance in
|     |  H&E, small airway |     | Ciliated |      | Basal |     | manually annotated regions |     |     |     |     |     |              |     |
| --- | ------------------ | --- | -------- | ---- | ----- | --- | -------------------------- | --- | --- | --- | --- | --- | ------------ | --- |
|     |                    |     |          | 20.0 |       |     |                            |     |     | e   |     |     |              |     |
|     |                    |     |          |      |       |     | Fibroblast                 |     |     |     |     |     | Dissociation |     |
LE
|            |     |                      |     | 15.0 |     | 3.0 Density score |           |         |      |                    |             | Material   | method | Location |
| ---------- | --- | -------------------- | --- | ---- | --- | ----------------- | --------- | ------- | ---- | ------------------ | ----------- | ---------- | ------ | -------- |
|            |     | EEppiitthheelliiuumm |     |      |     |                   | Muscle    |         |      |                    |             | Muscle     |        |          |
|            |     |                      |     |      |     | 2.0               | Mast cell |         |      |                    |             | Fibroblast |        |          |
|            |     |                      |     | 10.0 |     |                   |           | VE      |      | Cell type loadings |             | LE         |        |          |
|            |     |                      |     |      |     |                   | Eryth ro  | c y t e |      |                    |             | VE         |        |          |
| Parenchyma |     |                      |     |      |     | 1.0               | T  &      |   N K   | 10–1 |                    |             | AT1        |        |          |
|            |     |                      |     | 5.0  |     |                   | Myeloid   |         |      |                    |             | AT2        |        |          |
| 500 µm     |     |                      |     |      |     |                   |           | AT1     |      |                    | Erythrocyte |            |        |          |
|            |     | Cartilage            |     | 0    |     | 0                 |           | AT2     |      | Fold change        |             | Myeloid    |        |          |
T & NK
|     | AT1 |     | AT2 |     | Chondrocyte |               |             | Basal                                                |                                 |     | >1/3        | Mast cell |     |     |
| --- | --- | --- | --- | --- | ----------- | ------------- | ----------- | ---------------------------------------------------- | ------------------------------- | --- | ----------- | --------- | --- | --- |
|     |     |     |     | 4.0 |             |               | C i l       | ia t e d                                             |                                 |     |             | B cell    |     |     |
|     |     | 1.6 |     |     |             | 0.05          | Se c r      | e t o r y                                            | 10–2                            |     | 0           | B plasma  |     |     |
|     |     |     |     |     |             | Density score | Chondrocyte |                                                      |                                 |     |             | Ciliated  |     |     |
|     |     | 1.2 |     | 3.0 |             | 0.04          |             | SMG                                                  |                                 |     | <1/3        | Secretory |     |     |
|     |     |     |     |     |             |               | B plasma    |                                                      |                                 |     |             | Basal     |     |     |
|     |     |     |     |     |             | 0.03          | B cell      |                                                      |                                 |     | Chondrocyte |           |     |     |
|     |     | 0.8 |     | 2.0 |             |               |             |                                                      |                                 |     | LTSR        | SMG       |     |     |
|     |     |     |     |     |             | 0.02          |             | sGMS egalitraC muilehtipe reyalitluM lessev lairetrA | elcsum htooms yawriA amyhcneraP |     |             |           |     |     |
0.4 1.0 >0.9999 slleC ielcuN llAloC llAbiL –54DCbiL tsegidnUbiLpyrT_–54DCbiL +54DCbiL ielcuN tsegidnUbiLpyrT aehcarT 3–2 ihcnorB 4 ihcnorB raPrewoL raPreppU
|     |     |     |     |     |     | 0.01 |     |     |     |     | 0.999 |     |     |     |
| --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | ----- | --- | --- | --- |
0.99
|     |     | 0   |     | 0   |     | 0   |     |     |     |     | 0.9 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
0.5
Fig. 1 | Spatial multi-omics atlas of the human lung allows the identification  (green) and cartilage (brown). d, Cell type groups are enriched in expected
of cell types and their location. a, Multi-omics spatial lung atlas experimental  micro-anatomical tissue environments on Visium ST across sections from five
design included fresh and frozen sampling from five locations for scRNA-seq  donors. Cell type loadings are represented by both dot size and color for cell
(seven donors), sc VDJ-seq (four donors), snRNA-seq (seven donors) and Visium  types annotated in b across the manually annotated micro-environments in the
ST (seven donors). Five donors (D) from the frozen samples were pooled into  Visium data. e, Cell type capture is affected by protocol and location. Cell type
five reactions, each containing different locations (Loc) from donors. b, UMAP  proportion analysis with fold changes and LTSR score for all cell type groups with
of all scRNA-seq/snRNA-seq from 193,108 cells/nuclei in total from ten donors.  regard to the material, protocol and location. Dashed boxes highlight the greatest
Cells from all major subsets were captured. c, cell2location mapping on Visium  changes. AT1, alveolar type 1; AT2, alveolar type 2; LE, lymphatic endothelium;
ST from a bronchi section shows matching of cell types to expected structures.  VE, vascular endothelium. The number of cells in each cell type group is shown
H&E staining and cell abundance estimated by cell2location (density score) for  in Supplementary Table 7 and online: https://www.lungcellatlas.org as variable
ciliated, basal epithelium, AT1, AT2 and chondrocyte cell types with histology  Celltypes_master_high.
image in the background. Dotted lines circle the epithelium (pink), parenchyma
surrounding and endoneurial NAFs alongside Schwann cells within  tissue locations, we distinguished further endothelial arterial cell
the nerve bundle in human airway samples. In conclusion, we have  types (systemic arterial endothelia (E-Art-syst) and pulmonary arte-
detected and mapped rare stromal cells of airway peripheral nerves. rial endothelia (E-Art-pulm)) (Fig. 3a,c and Extended Data Fig. 6b),
nonvascular airway smooth muscle (ASM) cells, and both pulmonary
Vascular cell types in systemic and pulmonary circulation. Focus- and systemic smooth muscle/perivascular cells (pulmonary smooth
ing on vasculature, we could distinguish clusters of pulmonary and  muscle (SM-pulm) and pulmonary pericyte (Peri-pulm), systemic
systemic circulation by the specific enrichment in parenchyma  arterial smooth muscle (SM-Art-syst), systemic pericyte (Peri-syst)
(pulmonary vasculature, where gas exchange occurs) and trachea  and venous perivascular cells, that is, immune recruiting perivascular
cells (IR-Ven-Peri))11 (Fig. 3a–c,f). ASM cells lined the airways (Extended
(systemic vasculature, providing oxygen to the tissue) (Fig. 3a,b).
We also distinguished further cell types in distinct tissue locations  Data Fig. 6c), were mainly captured in single nuclei data (Fig. 3d) and
using ST: endothelial arterial cells (systemic E-Art-syst and pulmo- had marker genes aligned across tissues with smooth muscle in the
nary E-Art-pulm), smooth muscle cells (non-vascular airway (ASM),  HPA and GTEx (Extended Data Fig. 6d, e).
pulmonary (SM-pulm) and systemic (SM-syst)) and pericytes (pulmo- The IR-Ven-Peri expressed ABCC9 and ICAM1 but not CSPG4, similar
nary (Peri-pulm), systemic (Peri-syst) and venous immune recruiting  to postcapillary venous perivascular cells important for immune cell
(IR-Ven-Peri)11; Fig. 3a-f, Extended data fig. 6b). Using ST in different  homing to peripheral lymph nodes30,31 (Fig. 3d,e). IR-Ven-Peri expressed
| Nature Genetics | Volume 55 | January 2023 | 66–77 |     |     |     |     |     |     |     |     |     |     |     |     |     | 68  |
| -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

| Article |     |     |     |     |     |     |     | https://doi.org/10.1038/s41588-022-01243-4 |     |     |     |     |     |
| ------- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------ | --- | --- | --- | --- | --- |
| a       |     |     |     |     | b   |     |     |                                            |     | c   |     |     |     |
C e l l s
|           |     |                 |     |     |     | Cell-type composition |                   |     |     |     | det e c t e d  % | Mean e x p r e ssion in  |     |
| --------- | --- | --------------- | --- | --- | --- | --------------------- | ----------------- | --- | --- | --- | ---------------- | ------------------------ | --- |
| Fibro-adv |     |                 |     |     |     |                       |                   |     |     |     |                  | g r o u p                |     |
|           |     | Perineurial NAF |     |     |     |                       | Location Material |     |     |     |                  |                          |     |
|           |     |                 |     |     |     |                       |                   |     |     |     | 20 40 60 80      | 0 Max                    |     |
Endoneurial NAF
|     |     | Endoneurial NAF |     |     |     | mSchwann    |     | Cells: n = 59 |     | CXCL12 |     |                      |     |
| --- | --- | --------------- | --- | --- | --- | ----------- | --- | ------------- | --- | ------ | --- | -------------------- | --- |
|     |     |                 |     |     |     | IR-fibro    |     |               |     | CCL21  |     | Fibroblast reticular |     |
|     |     |                 |     |     |     | Mesothelial |     | Nuclei: n = 0 |     | CCL19  |     | cell markers         |     |
GREM1
| IIRR--FFiibbrroo |     | PC-fibro   |     |     |                 | PB-fibro  |                                     | Cells: n = 0    |              | CXCL13 |                                                     | fDC                                                  |     |
| ---------------- | --- | ---------- | --- | --- | --------------- | --------- | ----------------------------------- | --------------- | ------------ | ------ | --------------------------------------------------- | ---------------------------------------------------- | --- |
|                  |     |            |     |     |                 | PC-fibro  |                                     | Nuclei: n = 411 |              | FDCSP  |                                                     | markers                                              |     |
|                  |     |            |     |     | Perineurial NAF |           |                                     |                 |              |        | tsalborbifoyM vda-orbiF orbif-RI vla-orbiF orbif-BP | ailehtoseM FAN lairuenodnE FAN lairuenireP nnawhcSmn |     |
|                  |     | Mesothelia |     |     |                 | nmSchwann |                                     |                 |              |        |                                                     |                                                      |     |
| Myofibroblast    |     |            |     |     |                 | Fibro-adv |                                     | Fold change     |              |        |                                                     |                                                      |     |
|                  |     |            |     |     |                 | Fibro-alv |                                     | >3              |              |        |                                                     |                                                      |     |
|                  |     |            |     |     | Myofibroblast   |           |                                     |                 | >0.9999 LTSR |        |                                                     |                                                      |     |
|                  |     | PB-fibro   |     |     |                 |           | 3–2 ihcnorB                         | 1               | 0.999        |        |                                                     |                                                      |     |
|                  |     |            |     |     |                 |           | aehcarT 4 ihcnorB raPrewoL raPreppU | slleC ielcuN    | 0.99         |        |                                                     |                                                      |     |
<1/3 0 . 9
0 . 5
d
|     |     | nmSchwann |     |     |     |     |     |     | H&E, bronchus |     |     | IR-fibro |     |
| --- | --- | --------- | --- | --- | --- | --- | --- | --- | ------------- | --- | --- | -------- | --- |
Immune
|     |     | mSchwann |     |     |     |     |     |     |     |     | infiltrate |     | 0.3 |
| --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- |
f
Fibro-alv fGWAS analysis for association with lung function 0.2
| UMAP2 |     |     |                         |               | Fibro-alv |     |     |     | 500 µm |                                           |     |     | 0.1 |
| ----- | --- | --- | ----------------------- | ------------- | --------- | --- | --- | --- | ------ | ----------------------------------------- | --- | --- | --- |
|       |     |     | Pulmonary smooth muscle |               |           |     |     |     |        |                                           |     |     | 0   |
|       |     |     |                         | Myofibroblast |           |     |     | h   |        | elcsum htooms yawriA ygolohprom denifednU |     |     |     |
Previously described muilehtipe reyalitluM
| UMAP1 New transcriptome in humans |     |     |     |     | PB-fibro |     |     |     |     |     |     |     |     |
| --------------------------------- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
New cell type in lungs/airway Pulmonary pericyte etartlifni enummI lessev yranomluP
|     |     |     |     |     | Fibro-adv |     |     |     |               | lessev lairetrA | eldnub evreN muirdnohcireP | lessev suoneV           |             |
| --- | --- | --- | --- | --- | --------- | --- | --- | --- | ------------- | --------------- | -------------------------- | ----------------------- | ----------- |
|     |     |     |     |     | AT2       |     |     |     | Enrichment of |                 |                            | yawria llamS amyhcneraP | muilehtoseM |
Airway Smooth Muscle cell types in egalitraC Cell-type loadings
|     |     |     |     |     | PC-fibro |       |             |     | region      |     | sdnalG | eussiT |      |
| --- | --- | --- | --- | --- | -------- | ----- | ----------- | --- | ----------- | --- | ------ | ------ | ---- |
|     |     |     |     |     | ...      |       |             |     |             |     |        |        | 10–1 |
| e   |     |     |     |     | –0.2     | 0 0.2 | 0.4 0.6 0.8 |     |             |     |        |        | 10–2 |
|     |     |     |     |     |          |       |             |     | m S c h w a | n n |        |        |      |
H&E, bronchus PB-fibro Fibro-adv log OR nm S c h w a n n 10–3
10–4
|     | 0.3 |     | 5             |     |     |     |     | Endoneurial NAF |                 |     |     |     |     |
| --- | --- | --- | ------------- | --- | --- | --- | --- | --------------- | --------------- | --- | --- | --- | --- |
|     |     |     | Density score |     |     |     |     |                 | Perineurial NAF |     |     |     |     |
4
0.2
|            |     |     | 3   | i            |     |              |              |     |     |     | j   |              |     |
| ---------- | --- | --- | --- | ------------ | --- | ------------ | ------------ | --- | --- | --- | --- | ------------ | --- |
| Epithelium | 0.1 |     | 2   | Nerve bundle |     | Endoneurial  | Endoneurial  |     |     |     |     |              |     |
|            |     |     |     |              |     | NAF          | NAF          |     |     |     |     | Nerve bundle |     |
| 500 µm     |     |     | 1   |              |     |              |              |     |     |     |     |              |     |
|            | 0   |     | 0   |              |     |              |              |     |     |     |     | nmSchwann    |     |
mSchwann
g
H&E, bronchus PC-fibro Chondrocyte 50 µm All channels ANGPTL7 THBS4 Endoneurial
500 µm
|     | 1 . 2 |     | 0 . 8 |     |     | Perineurial NAF |     |     |     |     | NAF |     |     |
| --- | ----- | --- | ----- | --- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- |
Cartilage 1 . 0 0 . 7 Density score Nerve bundle nmSchwann nmSchwann
0.6
|     | 0.8 |     | 0.5 |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Perineurial
|     | 0.6 |     | 0.4 |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | 0.4 |     | 0.3 |     |     |     |     |     |     |     | NAF |     |     |
0.2
|     | 0.2 |     | 0 .1 | 50 µm |              |     |        |       |     |       |     |     |     |
| --- | --- | --- | ---- | ----- | ------------ | --- | ------ | ----- | --- | ----- | --- | --- | --- |
|     | 0   |     |      |       | All channels |     | SLC2A1 | SOX10 |     | SCN7A |     |     |     |
0
Fig. 2 | Lung and airway fibroblasts and their spatial location. a, Sequential  intervals (n = 19,414 genes) for several cell types. Substantially enriched cell
clustering reveals 11 fibroblast populations in airways and lungs on UMAP,  types are marked in red (Wald test, BH multiple testing correction over 76 cell
colored by novelty as shown. b, Sample collection location and processing  types, FDR < 0.1). g, Visium ST mapping of PC-fibro around the airway cartilage
method affect cell type proportions. Poisson linear mixed model analysis of cell  showing cell2location density scores. h, Schwann cells and NAF colocalize with
type composition within the fibroblast compartment, accounting for location,  peripheral nerve bundles in annotated Visium ST sections by cell2location. Cell
material, dissociation protocol and donor in the model. Cell type numbers are  type loadings are represented by both dot size and color. i, Nerve-associated cell
shown in Supplementary Table 7 and in online portal. c, Dot plot of IR-fibro  type markers have distinct locations in the airway nerve bundles identified by
marker genes that overlap with Fibroblast reticular cell and fDC markers.   smFISH staining. Donors used for replicas are shown in Supplementary Table 9.
d,e, Cell2location density scores demonstrate that (d) IR-fibro colocalizes with a  The marker gene probes for each cell type are given in each panel. Dashed lines
manually annotated immune infiltrate microenvironment in the airways, and (e)  surround the nerve bundles. j, Schematic representation of the described nerve-
PB-fibro localizes around the airway epithelium. f, PB-fibro are associated with  associated populations in the peripheral nerves of the airway. Fibro-alv, alveolar
lung function (FEV1/FVC) in fGWAS analysis (logOR, 0.53; FDR, 0.014). Shown  fibroblasts; fibro-adv, adventitial fibroblasts.
are the log odds ratios (logOR) obtained from fGWAS and their Wald confidence
Extended Data Fig. 7a,b,c), enriched in the trachea32,33 and previously
chemokines (Fig. 3e) and colocalized with a venous endothelial vessel
(ACKR1+), validated in a bronchial section by Visium ST (Fig. 3f) and  only characterized in mice at the single cell level34–36. smFISH stain-
in smFISH microscopy (Fig. 3g and Extended Data Fig. 6f). Venous  ing for ALDH1A3, MIA and RARRES1 validated localization at the SMG
endothelial cells expressed leukocyte binding receptors (Extended Data  and distinguished these cells from other epithelial cells (Fig. 4b and
Fig. 6g), similar to lymph node postcapillary venules, suggesting a role  Extended Data Fig. 7e,f). Cell2location distinguished distinct locations
for venous endothelia and IR-Ven-Peri in extravasation in airway veins. of SMG duct cells compared to SMG mucous and serous cells, providing
In summary, we distinguish cells of the systemic and pulmonary  orthogonal evidence of the identification of a new, distinct cell type
circulation, describe new IR-Ven-Peri cells and further define the rela- (Extended Data Fig. 7f). In addition, Velocyto analysis suggested that
tionship between the endothelial and perivascular cells (Fig. 3h and  these cells may lie on a trajectory toward surface epithelial populations
Supplementary Fig. 3). (Extended Data Fig. 7g), consistent with the regenerative role of SMG
duct cells in mice37,38.
Identification of duct cells in airway SMG We also identified myoepithelial cells in snRNA-seq, expressing
In the epithelial compartment, we identified known and rare cell  basal epithelium (TP63 and KRT14) and muscle (ACTA2, TAGLN and
types and transcriptionally define human SMG duct cells (Fig. 4a and  CNN1 positive, but DES negative) markers (Fig. 4a and Extended Data
| Nature Genetics | Volume 55 | January 2023 | 66–77 |     |     |     |     |     |     |     |     |     |     |     |     | 69  |
| -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

| Article |                     |     |     |     |               |     |     |     |     | https://doi.org/10.1038/s41588-022-01243-4 |     |     |     |
| ------- | ------------------- | --- | --- | --- | ------------- | --- | --- | --- | --- | ------------------------------------------ | --- | --- | --- |
| a       |                     |     |     |     |               |     |     | b   |     |                                            |     | e   |     |
|         | Vascular Endothelia |     |     |     | Smooth Muscle |     |     |     |     |                                            |     |     |     |
LTSR
Cap-a
|     |            |     |                      |     |           |             |     | detelped yawriA |       |     | >0.9999 |                   |      |
| --- | ---------- | --- | -------------------- | --- | --------- | ----------- | --- | --------------- | ----- | --- | ------- | ----------------- | ---- |
|     |            |     |                      |     |           | IR-Ven-Peri |     |                 | Cap-g |     |         |                   |      |
|     |            |     | EE--AArrtt--ppuullmm |     |           | Peri-syst   |     |                 |       |     | 0.999   | senikomehC CXCL12 |      |
|     | CCaapp--aa |     |                      |     |           |             |     | Peri-pulm       |       |     |         |                   |      |
|     |            |     | E-Art-syst           |     |           |             |     |                 |       |     | 0.99    |                   | CCL2 |
|     |            |     |                      |     | Peri-pulm |             |     | SM-pulm         |       |     |         | CCL21             |      |
0.9
|     |     |            |     |     |     |             |     | E-Art-pulm |     |     |     | CCL19 |     |
| --- | --- | ---------- | --- | --- | --- | ----------- | --- | ---------- | --- | --- | --- | ----- | --- |
|     |     | CCaapp--gg |     |     |     |             |     |            |     |     | 0.5 | ICAM1 |     |
|     |     |            |     |     |     | SM-Art-syst |     | E-Ven-pulm |     |     |     |       |     |
VCAM1
| Location |     |     | EE--VVeenn--ssyysstt |     |     |     |     | E-Art-syst |     |     |     |     |     |
| -------- | --- | --- | -------------------- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- |
SSMM--ppuullmm dehcirne  yawriA Fold change MSA ireP-neV-RI mlup-ireP tsys-ireP mlup-MS tsys-trA-MS
|     |     |     |     | Location |     |     |     | E-Ven-syst |     |     |     |     |     |
| --- | --- | --- | --- | -------- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- |
>3
|     |             |     |                      |     |     |     |     | IR-Ven-Peri |     |     |     | Mean expression  |     |
| --- | ----------- | --- | -------------------- | --- | --- | --- | --- | ----------- | --- | --- | --- | ---------------- | --- |
|     | Trachea     |     | EE--VVeenn--ppuullmm |     |     |     |     | Peri-syst   |     |     |     | in group         |     |
|     | Bronchi 2–3 |     |                      |     |     |     |     |             |     |     | 1   |                  |     |
|     |             |     |                      |     |     |     |     |             | ASM |     |     | 0                | Max |
Bronchi 4
| 2PAMU | LowerPar |     |     |       |     | ASM                  |     | SM-Art-syst |                     |                                   | <1/3   |     | Cells             |
| ----- | -------- | --- | --- | ----- | --- | -------------------- | --- | ----------- | ------------------- | --------------------------------- | ------ | --- | ----------------- |
|       | UpperPar |     |     | 2PAMU |     |                      |     |             |                     |                                   |        |     | detected %        |
|       |          |     |     |       |     | Previously described |     |             | aehcarT 3–2 ihcnorB | 4 ihcnorB raPrewoL raPreppU slleC | ielcuN |     |                   |
| UMAP1 |          |     |     |       |     | New transcriptome    |     |             |                     |                                   |        |     | 01 02 03 04 05 06 |
UMAP1
New cell type in lungs/airway
| c             |            |     |            |             |         | f   |     |     |     |     |     |     |     |
| ------------- | ---------- | --- | ---------- | ----------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
| H&E, bronchus | E-Art-syst |     | E-Art-pulm | SM-Art-syst | SM-pulm |     |     |     |     |     |     |     |     |
Arterial  0.8 0.16 3.0 Density score H&E, bronchus E-Ven-syst  E-Ven-pulm IR-Ven-Peri Peri-syst
| vessel |        | 0.6 |     |      | 3.0 |                                |              |     |     |     |     |     | Density score |
| ------ | ------ | --- | --- | ---- | --- | ------------------------------ | ------------ | --- | --- | --- | --- | --- | ------------- |
|        |        |     |     | 0.12 |     | 2.0 VVeennoouuss  vveesssseell |              |     |     |     | 1.0 | 0.8 | 0.8           |
|        |        | 0.4 |     | 0.08 | 2.0 |                                |              |     | 2.0 |     |     |     |               |
|        |        |     |     |      | 1.0 | 1.0                            |              |     |     |     | 0.5 | 0.4 | 0.4           |
|        |        | 0.2 |     | 0.04 |     |                                | 220000  µµmm |     | 1.0 |     |     |     |               |
|        | 200 µm |     |     |      |     |                                |              |     | 0   |     | 0   | 0   | 0             |
|        |        | 0   |     | 0    | 0   | 0                              |              |     |     |     |     |     |               |
| d      |        |     |     |      |     |                                | h            |     |     |     |     |     |               |
Mean expression in
|     |        |     |     |     |     | group |     |  Airway, systemic circulation |     |     |     |     |     |
| --- | ------ | --- | --- | --- | --- | ----- | --- | ----------------------------- | --- | --- | --- | --- | --- |
|     | Cells  |     |     |     |     | 0     | Max |                               |     |     |     |     |     |
detected (%)
5PAKCN B1LRUEN 11A83CLS 2NTSLC 2ADLHP 2SBROS 3TS6SH E3AMES 2ENURP 6A4LOC 2ENURP SM-Art-syst Peri-syst E-Ven-syst IR-Ven-Peri
|     |              | 3DMRF 2A7CLS 4PAETS 4PBAF 3YSHC | 3KNCK 3CMAL   | 2I4XOC B1DGIH 4GPSC 9CCBA 2TNNT 2MGT | 1A1LOC MNYS A6MPG | 3KCOD 7HDCP 2ESPH 1EBUCS 2GTCA | 2ATCA NLGAT |     |     |     |     |     |     |
| --- | ------------ | ------------------------------- | ------------- | ------------------------------------ | ----------------- | ------------------------------ | ----------- | --- | --- | --- | --- | --- | --- |
| 02  | 04 06 08 001 |                                 | CNT 7FGF TSEM | NTP 5SGR                             | NLE 1TEN          | 2PRN EHCB 6RGL SED             | 1NNC 2MPT   |     |     |     |     |     |     |
ASM
IR-Ven-Peri
Peri-pulm
|             | Peri-syst |     |     |     |     |     |     |        |     |            |       | Extravasating  |     |
| ----------- | --------- | --- | --- | --- | --- | --- | --- | ------ | --- | ---------- | ----- | -------------- | --- |
|             | SM-pulm   |     |     |     |     |     |     |        |     |            | Cap-g |                |     |
| SM-Art-syst |           |     |     |     |     |     |     |        |     | E-Art-syst |       | leukocyte      |     |
|             |           |     |     |     |     |     |     | Artery |     | Capillary  |       | Venule/vein    |     |
g
DAPICCL21 DAPICCL21 DAPICCL19  Parenchyma, pulmonary circulation
CCL19  ACKR1
|     |     |     |     |            |     |           |     |         |       |     | Peri-pulm | SM-pulm |     |
| --- | --- | --- | --- | ---------- | --- | --------- | --- | ------- | ----- | --- | --------- | ------- | --- |
|     |     |     |     |            |     |           |     | SM-pulm | Cap-a |     |           |         |     |
|     |     |     |     | 100 µm     |     | 100 µm    |     |         |       |     |           |         |     |
|     |     |     |     | DAPI ACKR1 |     | DAPICCL21 |     |         |       |     |           |         |     |
CCL19
ACKR1
|     |     |     |     |     |     |     |     |     |     | Alveolus |     | E-Ven-pulm |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | ---------- | --- |
E-Art-pulm
|     |        |     |     |        |     |        |     | Artery |     |    Capillary  |     | Vein |     |
| --- | ------ | --- | --- | ------ | --- | ------ | --- | ------ | --- | ------------- | --- | ---- | --- |
|     | 500 µm |     |     | 100 µm |     | 100 µm |     |        |     |               |     |      |     |
Fig. 3 | Cell types of systemic and pulmonary circulation. a, UMAP  cell–cell adhesion molecules shown by marker gene dot plot. f, E-Ven-syst and
visualization of scRNA-seq data from the vascular endothelia and smooth muscle  IR-Ven-Peri colocalize at a venous vessel in the airway in Visium ST sections shown
compartments. Color of the dots shows cell type or location. Color of the text  by cell2location density scores at venous vessel. g, IR-Ven-Peri markers CCL21 and
reflects novelty. b, Cell type proportion analysis with fold changes and LTSR score  CCL19 localize adjacent to the venous vessel marker ACKR1 in the airway. Donors
for the cell types with regard to the location and material. Cell type numbers are  used for replicas are shown in Supplementary Table 9. Dashed lines in c, f and
shown in Supplementary Table 7 and lungcellatlas.org. c, E-Art-syst colocalize  g represent vessel structures as relevant for each figure panel. h, Schematic of
with arterial vessel and SM-Art-syst in the airway in Visium ST. Cell2location  transcriptionally defined vascular cells in the systemic and pulmonary circulation.
density scores are shown for arterial endothelial and smooth muscle cell types  Created with BioRender. E = endothelial, SM = smooth muscle, Cap = capillary,
localizing at arterial vessel. d, Marker gene dot plot of the smooth muscle  Ven = venous, Art = arterial, Syst = systemic, Pulm = pulmonary, Peri = pericyte,
compartment. e, IR-Ven-Peri expresses immune recruiting chemokines and  ASM = airway smooth muscle, IR = immune recruiting.
Fig. 7a,h) with localization around the glands (Extended Data Fig. 7f,i,j)9.
consistent with their positions at the base of the surface epithelium
We identified markers for cell–cell adhesion (FHOD3 and LAMA1) and  (Extended Data Fig. 7k and Supplementary Fig. 4). AT1 cells colocal-
nerve synapse signaling (NTRK2 and PLD5) and validated marker genes  ized with capillaries, alveolar macrophages and fibroblasts and were
by smFISH (Extended Data Fig. 7i) and in the HPA (Extended Data Fig. 7j).   separate from AT2 cells (Extended Data Fig. 7k and Supplementary
Interestingly, mouse myoepithelial cells have also been shown to  Fig. 4). This analysis revealed further spatial heterogeneity beyond
regenerate the surface airway epithelium37. However, in humans,  manual annotations, enhancing the spatial resolution and highlighting
myoepithelial cells are not well defined, potentially due to difficulties  colocating cell types.
in dissociating this cell type. Taking advantage of our multilocation data, we compared cells
Spatially, lung and airway epithelial cells were enriched in their  across the five locations (Extended Data Fig. 7c) and observed the
expected manually annotated locations (Fig. 1c,d). Unbiased analysis  expected enrichment of SMG epithelial cells and depletion of club cells
with cell2location nonnegative matrix factorization (NMF) was able to  in trachea (Extended Data Fig. 7c). Using our pooled snRNA-seq data, to
further distinguish hidden epithelial factors. We found that basal and  avoid batch effects from location-specific ambient RNA contamination
suprabasal cells colocate separately from apical surface epithelial cells,  (Fig. 1a, pooling scheme), we also analyzed gene expression signatures.
| Nature Genetics | Volume 55 | January 2023 | 66–77 |     |     |     |     |     |     |     |     |     |     |     |     | 70  |
| -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Article https://doi.org/10.1038/s41588-022-01243-4
Using a linear mixed model39 (Methods), we detected 80 differentially were found in multiple locations of the lung within a given donor
expressed genes in tracheal ciliated cells, including nasopharyngeal (Extended Data Fig. 8f). The T and NK cell proportions displayed dis-
carcinoma genes FBXL7, TSHZ2 and RAET1E (Extended Data Fig. 7l)40–42. tinct donor-to-donor variability compared to myeloid cells (Extended
As previously reported, we found reduced ACE2 expression in distal Data Fig. 8g–i), consistent with higher interindividual variability in
lung ciliated cells, where expression of ACE2 is more relevant in AT2 lymphocytes.
cells (Extended Data Fig. 7m)43. Overall, we define immune cells of the human lung and airway with
Overall, we uncover the full complement of SMG epithelial cells unprecedented resolution.
along with their spatial contexts in the human SMG.
Colocalization of IgA plasma cells with the SMG. B cells included
Immune cells in the lung and airways naive and memory B cells, IgA and IgG plasma cells, and plasmablasts
Myeloid cells show previously undescribed heterogeneity. We iden- (Fig. 4c and Extended Data Fig. 9a,b). These annotations were sup-
tified all major immune populations (Fig. 4c and Extended Data Fig. 8a) ported by VDJ-seq B cell receptor (BCR) isotype analysis. IgA, which
which were analyzed separately to reveal previously undescribed het- is important for mucosal immunity66,67, was most frequent in the air-
erogeneity, especially in myeloid cells. We found known macrophage way samples, while only the third most abundant in the parenchyma
subsets, including intravascular (expressing LYVE1 and MAF)44,45, (Fig. 4d and Extended Data Fig. 9c). Distinguishing markers for IgA
CXC3CR+ airway44,46–48, CHIT1+11,49 and interstitial macrophages45. We plasma cells included CCR10 and B cell maturation antigen BCMA
identified a previously undefined cluster expressing monocyte (CD14) (TNFRSF17; Extended Data Fig. 9b), which are important for plasma
and macrophage markers, termed macro-intermediate (Extended Data cell localization and survival, respectively67–69.
Fig. 8b). Among alveolar macrophages, the following two more clusters In Visium ST data, IgA plasma cells mapped to the airway SMG,
appeared: dividing cells (Macro-alv-dividing) and a cluster expressing colocalizing with duct, mucous and serous cells, while IgG mapped
metallothioneins (Macro-alv-MT), including MT1G, MT1X and MT1F. to immune infiltrates (Fig. 4e). Enrichment of plasma cells (MZB1+) at
Metallothioneins have a role in binding and metabolizing metal ions50, the SMG was confirmed in the HPA (Extended Data Fig. 9d,e), building
and in immunity and stress responses51,52. Finally, we identified a rare on a study in the 1970s that first showed IgA plasma cells in human
undescribed population of macrophages expressing chemokines, airway SMG70. We further distinguished enrichment of IgA plasma
including CXCL8, CCL4 and CCL20, which we named Macro-CCL45. cells in the serous glands with cell2location NMF, showing two distinct
The expression of CXCL8 and CCL20 distinguishes this subset from gland factors, one with SMG serous cells colocalizing more with IgA
interstitial macrophages which express CCL4. CXCL8 is associated with plasma cells than a second distinct factor with other SMG epithelial cells
lung infection, asthma, IPF and COPD53 and was identified in psoriatic (Fig. 4f, Extended Data Fig. 9f and Supplementary Fig. 4). This pref-
skin macrophages54. erential localization of IgA plasma cells was confirmed by manual
annotation of gland areas in ST on formalin-fixed paraffin-embedded
T and NK cell subsets in the lung and airways. T lymphocytes and (FFPE) preserved tissue samples, which allowed better distinction of
natural killer (NK) cells included CD4 T, CD8 T, mucosal-associated serous and mucous glands (Extended Data Fig. 9g).
invariant T (MAIT), NK, NKT, innate lymphoid cells and their subsets To dissect this niche at single-cell resolution, we used multiplex IHC
(Fig. 4c and Extended Data Fig. 8c). In the CD4 compartment, we dis- to confirm the presence of IgA2 but the absence of IgG cells in the SMG
tinguished naive/central memory (CD4-naive/CM), effector memory/ (Fig. 4g and Extended Data Fig. 9h), consistent with Visium ST (Fig. 4e,f).
effector (CD4-EM/Effector), regulatory T cell (Treg) and tissue-resident We also detected IgD+ naive B cells and CD3+ CD4+ T helper cells in the
memory (CD4-TRM) cells. Within CD8 cells, we found gamma-delta human SMG (Fig. 4g). We hypothesize that together these different
T cells (γδT), TRMs (CD8-TRM)55 and two distinct clusters analogous to cell types constitute an immune niche with relevance in disease, which
populations found in the lung in cross tissue analysis56: CD8-EM/EMRA we term the gland-associated immune niche (GAIN). Mucosal IgA is
and CD8-TRM/EM. The CD8-TRM cells specifically localized to airway important for protection against respiratory infections2, and we found
epithelium in our spatial data (Extended Data Fig. 8d)57,58. NK subsets that proportions of IgA plasma cells were increased in coronavirus
included NK-CD11d, NK-CD16hi and NK-CD56 bright59,60. CD11d+ NK cells disease 2019 (COVID-19) patients versus healthy controls in single-cell
are activated in response to infection in both mice and humans61–63, data from published nasal, tracheal and bronchial brush samples
were previously shown in human blood64 and here for the first time in (Methods) (Fig. 4h)71. In addition, increased plasma cell numbers
healthy human lungs. have been shown in smokers70, patients with cystic fibrosis72, COPD73
T cell receptor (TCR) VDJ-seq data confirmed MAIT cell type and Kawasaki disease74, warranting further study of the GAIN in these
annotation (with preferential use of TRAJ33 and TRAV1-2)65 and showed conditions. In C57/BL6 mouse tracheal sections, we did not identify
low clonal expansion in naive and Treg populations compared to IgA+ cells in the SMG of two independent cohorts of mice despite IgA+
memory and effector subsets (Extended Data Fig. 8e). As expected, staining in the colon as expected75 (Extended Data Fig. 9i), suggesting
there was no clonal sharing between individuals, but expanded clones that the GAIN should be studied in humans.
Fig. 4 | IgA plasma cells in human airways colocalize with SMGs. a, UMAP of ST cell2location results for 11 factors, showing NMF factor loadings normalized
scRNA-seq and snRNA-seq data from epithelial cells (excluding alveolar AT1 per cell type (dot size and color). Factors 3 and 6 identify two separated factors
and AT2) colored by cell type, with a dot plot for the marker genes of SMG duct in the SMG colocalizing IgA plasma cells, specifically with SMG serous cells
cells. b, smFISH staining of mucous (MUC5B), serous (LPO) and duct (ALDH1A3/ (factor 3), but less with other SMG cell types (factor 6). Other factors and cell
RARRES1) cells in human bronchus. c, UMAP plots of myeloid, T/NK and types are shown in Supplementary Fig. 4. g, Multiplex IHC staining of human
B lineage cells, colored by cell type. d, Number of B lineage cells with different trachea for the SMG structure (Hoechst for nuclei, EpCAM for epithelium,
Ig isotypes in airway (trachea and bronchi) from the analysis of VDJ amplified Phalloidin for actin, CD31 for vessels), B lineage markers (IgD, IgA2 and IgG) and
libraries. e, Visium ST results show IgA plasma cells specifically localize in the CD4 T cells (CD45, CD3 and CD4). Arrowheads point to CD45+ CD3+ CD4+ cells.
glands. Normalized average cell abundance (dot size and color) are shown from Scale bar 100 µm. h, Percentages of different isotypes of 470 B plasma cells
cell2location for SMG and B lineage cell types across the manually annotated from nasal, tracheal and bronchial brushes of two COVID-19 positives and three
micro-anatomical tissue environments. H&E section of bronchi with manually healthy control patients71. Patients with over 20 plasma cells were considered.
annotated glands shown in blue (top panel), cell2location density scores for IgA Donors used for replicas in b and g are shown in Supplementary Table 9. Macro,
plasma cells and SMG serous cells shown in lower panels. Cell type loadings are macrophage; CM, central memory; EM, effector memory; EMRA, effector
represented by both dot size and color. f, Unsupervised NMF analysis of Visium memory re-expressing CD45RA.
Nature Genetics | Volume 55 | January 2023 | 66–77 71

| Article |     |     |     |     |     |     |     |     |     | https://doi.org/10.1038/s41588-022-01243-4 |     |     |     |     |
| ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------ | --- | --- | --- | --- |
Cell–cell interactions and the SMG immune cell niche. To under- the GAIN. Expression of PIGR, which transcytoses polymeric Ig across
stand colocalization of B cells, IgA plasma cells and T cells in the SMG  the surface epithelium, was high across SMG epithelial cells, as was
(Fig. 4e–g), we explored the molecular mechanisms underpinning  CCL28, known to recruit IgA plasma cells through CCR10 (Fig. 5a–d and
| a          |                  |                  |     |     |                       |                 |       | b            |     |       |     |     |         |     |
| ---------- | ---------------- | ---------------- | --- | --- | --------------------- | --------------- | ----- | ------------ | --- | ----- | --- | --- | ------- | --- |
|            | Airway epithelia |                  |     |     | SMG-duct marker genes |                 |       |              |     |       |     |     |         |     |
|            |                  |                  |     |     |                       |                 |       | All channels |     | MUC5B |     | LPO |         |     |
|            |                  |                  |     |     |                       | 1SERRAR 3A1HDLA |       |              |     |       |     |     |         |     |
|            |                  | Neuroendocrine   |     |     |                       |                 | 32TRK |              |     |       |     |     | ALDH1A3 |     |
| SMG-mucous |                  |                  |     |     |                       | 7TRK            |       |              |     |       |     |     |         |     |
|            |                  | Ionocyte & brush |     |     |                       | 3IP             | AIM   |              |     |       |     |     |         |     |
|            |                  | SMG-duct         |     |     | Basal                 |                 |       |              |     |       |     |     |         |     |
Cells detected (%)
| Goblet |     | SMG-serous |              |                | Ciliated |     |     |     |     |     |     |     |     |     |
| ------ | --- | ---------- | ------------ | -------------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|        |     |            |              | Deuterosomal   |          |     | 100 |     |     |     |     |     |     |     |
|        |     |            | Deuterosomal |                |          |     | 80  |     |     |     |     |     |     |     |
|        |     |            |              | Dividing basal |          |     | 60  |     |     |     |     |     |     |     |
Ionocyte & brush
|            | DDiivviiddiinngg |      |          |                |           |     | 40              |     |     |     |     |     | RARRES1 |     |
| ---------- | ---------------- | ---- | -------- | -------------- | --------- | --- | --------------- | --- | --- | --- | --- | --- | ------- | --- |
| Suprabasal | bbaassaall       |      |          | Myoepithelial  |           |     | 20              |     |     |     |     |     |         |     |
|            |                  | Club |          | Neuroendocrine |           |     | Mean expression |     |     |     |     |     |         |     |
|            |                  |      | Ciliated |                | SMG-basal |     | in group        |     |     |     |     |     |         |     |
SMG-duct
|     |     | Myoepithelial |     | SMG-mucous |     |     | 0 Max |     |     |     |     |     |     |     |
| --- | --- | ------------- | --- | ---------- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
Basal
| 2PAMU |     |     |     | SMG-serous |     |     |     |     |     |     |     |     |     |     |
| ----- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Secretory club
SMG-basal
|       |     |     |     | Secretory goblet |     |     |     |     |     | Mucous  |     | Serous | Duct |     |
| ----- | --- | --- | --- | ---------------- | --- | --- | --- | --- | --- | ------- | --- | ------ | ---- | --- |
| UMAP1 |     |     |     | Suprabasal       |     |     |     |     |     |         |     |        |      |     |
c
T & NK
|     | Myeloid | cDC1 | DC-activated |     |     |     | Treg | ILC |     |     |     | B lineage |     |     |
| --- | ------- | ---- | ------------ | --- | --- | --- | ---- | --- | --- | --- | --- | --------- | --- | --- |
CD4-naive/
|           |      |        |                 |     |         |     |      | NK-CD56 bright |     |            | IgG-plasma |     |     |         |
| --------- | ---- | ------ | --------------- | --- | ------- | --- | ---- | -------------- | --- | ---------- | ---------- | --- | --- | ------- |
|           |      | cDC2   |                 |     |         | CM  |      |                |     |            |            |     |     |         |
| Monocyte  |      | Macro- | Macro-AW-CX3CR1 |     |         |     |      |                |     |            |            |     |     |         |
|           | CD16 | CCL    |                 |     | CD4-EM/ |     |      |                |     |            |            |     |     |         |
|           |      |        |                 |     |         |     | MAIT | NK-CD16hi      |     | IgA-plasma |            |     |     | B-naive |
effector
|     | Monocyte  | MMaaccrroo--             |         |     |         |     |     |     |     |     |             |     |     |     |
| --- | --------- | ------------------------ | ------- | --- | ------- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- |
|     | CD14      | iinntteerrmmeeddiiaattee | Macro-  |     | CD4-TRM |     |     |     |     |     |             |     |     |     |
|     |           |                          |         |     |         |     | NKT |     |     |     | Plasmablast |     |     |     |
intravascular
|     |     | M a c r o -     |     |     |     |         |         |          |     | 2PAMU |     |     | B-memory |     |
| --- | --- | --------------- | --- | --- | --- | ------- | ------- | -------- | --- | ----- | --- | --- | -------- | --- |
|     | in  | te r st i ti al |     |     |     | CD8-TRM | CD8-TRM | NK-CD11d |     |       |     |     |          |     |
|     |     | MMaaccrroo--    |     |     |     |         | TRM/EM  |          |     |       |     |     |          |     |
pcDC
|     |     | CCHHIITT11 |     |     |     | CD8-EM |     |     |     | UMAP1 |     |     |     |     |
| --- | --- | ---------- | --- | --- | --- | ------ | --- | --- | --- | ----- | --- | --- | --- | --- |
CD8-EM/EMRA
γδT
|     |     | Macro-alv |     |     | 2PAMU |     |     |     |     |     |     |     |     |     |
| --- | --- | --------- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Macro-alv-MT
f
2PAMU
|     |     |     |     |     | UMAP1 |     |     |     |     | Visium H&E |     |     | Cell2Location  |     |
| --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | ---------- | --- | --- | -------------- | --- |
factorization analysis
UMAP1
Myoepithelial
| d               |                          |     |     |     | e   |                              |     |                    |     |     |     |            |     |                    |
| --------------- | ------------------------ | --- | --- | --- | --- | ---------------------------- | --- | ------------------ | --- | --- | --- | ---------- | --- | ------------------ |
|                 | Ig isotypes from VDJ-seq |     |     |     |     |                              |     |                    |     |     |     | SMG-duct   |     | Cell-type loadings |
|                 |                          |     |     |     |     | Cell2location density scores |     |                    |     |     |     | IgA-plasma |     |                    |
|                 | Trachea & bronchi        |     |     |     |     |                              |     |                    |     |     |     | SMG-serous |     | 1.0                |
|                 |                          |     |     |     | SMG |                              |     | Cell-type loadings |     |     |     | SMG-mucous |     |                    |
| sllec fo rebmuN |                          |     |     |     |     |                              |     | 10–1               |     |     |     |            |     |                    |
SMG-basal
|     | 200 |     |     |     | Muyltilayer |     |     |      |     |     |     |            |     |     |
| --- | --- | --- | --- | --- | ----------- | --- | --- | ---- | --- | --- | --- | ---------- | --- | --- |
|     |     |     |     |     | epithelium  |     |     | 10–2 |     |     |     | IgG-plasma |     | 0   |
Immune
100 infiltrate 10–3 Manual annotation: Glands Factor 6 Factor 3
|     |     |             |            |     |     | lasab-GMS suocum-GMS suores-GMS | amsalp-AgI tcud-GMS lailehtipeoyM tsalbamsalP amsalp-GgI yromem-B | evian-B |            |     |     |            |     |     |
| --- | --- | ----------- | ---------- | --- | --- | ------------------------------- | ----------------------------------------------------------------- | ------- | ---------- | --- | --- | ---------- | --- | --- |
|     | 0   |             | B-memory   |     |     |                                 |                                                                   |         |            |     |     |            |     |     |
|     | IgA | IgM IgG IgD | B-naive    |     |     |                                 |                                                                   |         |            |     |     |            |     |     |
|     |     |             | IgA-plasma |     |     |                                 |                                                                   |         | SMG serous |     |     | IgA plasma |     |     |
BCR isotype
IgG-plasma
|     |     |     | Plasmablast |     |     |     |     |     |     |     | 3.5 |     |     | 1.4 |
| --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |             |     |     |     |     |     |     |     | 3.0 |     |     | 1.2 |
g
|     |       |            |     |      |     |          |     |     |     |     | 2.5 |     |     | Density score |
| --- | ----- | ---------- | --- | ---- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | ------------- |
|     | EpCAM | Phalloidin |     | CD31 |     | Merged + |     |     |     |     |     |     |     | 1.0           |
Hoechst
|     |     |     |     |     |     |     |     |     |     |     | 2.0 |     |     | 0.8 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     |     |     |     |     |     | 1.5 |     |     | 0.6 |
|     |     |     |     |     |     |     |     |     |     |     | 1.0 |     |     | 0.4 |
|     |     |     |     |     |     |     |     |     |     |     | 0.5 |     |     | 0.2 |
0
| 100 µm |     |      |     |     |     |          |     |     |     |     |     |     |     | 0   |
| ------ | --- | ---- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
|        | IgD | IgA2 |     | IgG |     | Merged + |     |     |     |     |     |     |     |     |
|        |     |      |     |     |     | EpCAM    |     |     | h   |     |     |     |     |     |
Plasma cells from nasal, trachea
and bronchial brushes
100%
Immunoglobulin
type
|     |     |     |     |     |     |     |     |     | egatnecreP 75% |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- |
IgA
|      |     |     |     |     |     |          |     |     | 50% |     |     |     | IgD |     |
| ---- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
| CD45 |     | CD3 |     | CD4 |     | Merged + |     |     |     |     |     |     |     |     |
|      |     |     |     |     |     | EpCAM    |     |     |     |     |     |     | IgM |     |
25%
IgG
0%
|     |     |     |     |     |     |     |     |     |     | Healthy |  COVID+ |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------- | --- | --- | --- |
COVID status
| Nature Genetics | Volume 55 | January 2023 | 66–77 |     |     |     |     |     |     |     |     |     |     |     |     |     | 72  |
| -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

| Article |     |     |     |     |     |     |     |     |     | https://doi.org/10.1038/s41588-022-01243-4 |     |     |     |     |
| ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------ | --- | --- | --- | --- |
| a       |     |     |     | b   |     |     | c   |     | d   |                                            |     |     | e   |     |
CCL
4
|      |     |     |     |       | B - plasm |         |       | Chemokines                    |                       |          | Receptors            |                                        | DAPI IgA2CCL28 |     |
| ---- | --- | --- | --- | ----- | --------- | ------- | ----- | ----------------------------- | --------------------- | -------- | -------------------- | -------------------------------------- | -------------- | --- |
| RGIP |     |     |     | iv e  |           | a       |       |                               |                       |          |                      |                                        |                |     |
|      | 2   |     |     | B-n a | CC R1 0   |         | CCL2  |                               |                       | CCR2     |                      |                                        |                |     |
|      |     |     |     | C R 6 |           | C CR2   |       |                               |                       |          |                      |                                        |                |     |
|      |     |     |     | ory C |           | C       | CCL20 |                               |                       | CCR6     |                      |                                        |                |     |
|      |     |     |     | m     |           | D       |       |                               |                       |          |                      |                                        |                |     |
|      | 0   |     |     | e CR6 |           | C 4     |       |                               |                       |          |                      |                                        |                |     |
|      |     |     |     | m     |           | C R6 -T | CCL28 |                               | CCR10                 |          |                      |                                        |                |     |
|      | 4   |     |     | B- C  |           |         |  c    |                               |                       |          |                      |                                        |                |     |
|      |     |     |     |       |           |         | e lls | detavitca-CD ireP-RI tcud-GMS | suocum-GMS suores-GMS | yromem-B | evian-B AgI-amsalp-B | GgI-amsalp-B tsalbamsalp-B sllec T-4DC |                |     |
82LCC
|     | 2   |     |     |       |     |      | noisserpxe naeM | xaM |     |     |     |     |     |     |
| --- | --- | --- | --- | ----- | --- | ---- | --------------- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     | S C C |     | CL28 |                 |     |     |     |     |     |     |     |
|     |     |     |     | e L28 |     |      |  puorg ni       |     |     |     |     |     |     |     |
|     | 0   |     |     | ro    |     | C    |                 |     |     |     |     |     |     |     |
us
lailehtipeoyM suocum-GMS suores-GMS tcud-GMS lasaB lasabarpuS telboG detailiC C 0 Cells detected (%) Cells detected (%)
|     |     |     |     | M u C L 28 |      | CC L 2 c t |     |             |          |       |       |     |        |     |
| --- | --- | --- | --- | ---------- | ---- | ---------- | --- | ----------- | -------- | ----- | ----- | --- | ------ | --- |
|     |     |     |     | c o u      |      | D u        |     |  0 01 02 03 | 04 05 06 |  5 01 | 51 02 |     |        |     |
|     |     |     |     | s          | CCL2 |            |     |             |          |       |       |     | 100 µm |     |
B-memory
B-naive
B-plasma
|     |        |      | CD4-T cells |             |     |                   | g                      |        |     |     | h           |             |                 |           |
| --- | ------ | ---- | ----------- | ----------- | --- | ----------------- | ---------------------- | ------ | --- | --- | ----------- | ----------- | --------------- | --------- |
|     |        |      | SMG-duct    |             |     |                   |                        |        |     |     | MHCII       |             | CD4-T cells     |           |
|     |        |      | SMG-mucous  |             |     |                   | DAPI TNFSF13/APRILIgA2 |        |     |     |             |             |                 |           |
|     |        |      | SMG-serous  |             |     |                   |                        |        |     |     |             |             | CD4             |           |
| f   |        |      |             |             | CD  | 4 - n a i v e /cm |                        |        |     |     |             |             |                 |           |
|     | o r y  |      | B-plasm     |             |     |                   |                        |        |     |     |             |             |                 |           |
|     | m      | BCMA |             |             |     | IL 6 R _ IL 6 S   |                        |        |     |     |             |             |                 |           |
|     | me     |      |             |             |     | T                 |                        |        |     |     | H           |             |                 |           |
|     | B- C I |      |             | a           |     |                   |                        |        |     |     | L A - D P   | B 1         |                 |           |
|     | TA     |      |             |             |     |                   |                        |        |     |     | H L A - D Q | B 1         |                 |           |
|     |        |      |             |             |     |                   |                        | 100 µm |     |     | H L A - D P | A 1         |                 |           |
|     |        |      | TA          | a ST        |     |                   |                        |        |     |     | D M         | A           |                 |           |
|     |        |      | C           | m           |     |                   |                        |        |     |     | H L A -     | B 5         |                 |           |
|     |        |      |             | I a s _IL 6 |     |                   |                        |        |     |     | H L A - D R |             |                 | H LA-DRB1 |
|     |        |      |             | p l         |     |                   | DAPIIL6IgA2            |        |     |     |             | 1           |                 |           |
|     |        |      |             | B- 6 R      |     |                   |                        |        |     |     | D           | R B         |                 |           |
|     |        |      |             | IL          |     |                   |                        |        |     |     | S H L A -   | A           |                 |           |
|     |        |      |             |             |     |                   |                        |        |     |     | e           | D R A       |                 |           |
|     |        |      |             | S I L       |     |                   |                        |        |     |     | ro          | A - D M B 1 |                 | H LA      |
|     |        |      |             | e 6         |     |                   |                        |        |     |     | u H         | L A - D R M | B A 1 B1 B1 A1A | H         |
|     |        |      |             | r o         |     |                   |                        |        |     |     | s           | H L A - D   | D Q Q P M       | LA -D     |
|     |        |      |             | u           |     |                   |                        |        |     |     | M           | H L A-      | A- D D D P D    | -D R A    |
|     | S A PR |      | IL          | s           |     |                   |                        |        |     |     | u c         | H L         | L A- A- A- -A   | R ct      |
|     | ero IL |      | APR uct     |             |     |                   |                        |        |     |     |             | o u H       | HL HL HL LH     | B 5 Du    |
s
|     | u s |     | D   |     |     | IL6 |     | 100 µm |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- |
APRIL
|     | Mucous |     |     |         |     | Duct |        |     |        |     |     |       |     |     |
| --- | ------ | --- | --- | ------- | --- | ---- | ------ | --- | ------ | --- | --- | ----- | --- | --- |
| i   |        |     |     | j       |     |      |        |     |        |     |     |       |     |     |
|     |        |     |     | Hoechst |     |      | HLA-DR |     | Merged |     |     | EpCAM |     |     |
ARD-ALH 4
2
0
1BRD-ALH 4
SMG
|     | 2   |     |     |     |     |        |     |     |     |     | Surface   |     |     | Surface   |
| --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --------- | --- | --- | --------- |
|     |     |     |     |     |     | 150 µm |     |     | SMG |     | epithelia |     |     | epithelia |
0
k
| 04DC | 4   |     |     | CD4 |     | CD45RO |     | HLA-DR |     | Merged +  |     |     |     |     |
| ---- | --- | --- | --- | --- | --- | ------ | --- | ------ | --- | --------- | --- | --- | --- | --- |
|      | 2   |     |     |     |     |        |     |        |     | EpCAM     |     |     |     |     |
0
|     | yromem-B evian-B detailiC | tcud-GMS suocum-GMS | suores-GMS |        |     |        |     |        |     |        |     |     |       |     |
| --- | ------------------------- | ------------------- | ---------- | ------ | --- | ------ | --- | ------ | --- | ------ | --- | --- | ----- | --- |
|     |                           |                     |            | 100 µm |     | 100 µm |     | 100 µm |     | 100 µm |     |     | 25 µm |     |
Fig. 5 | Cell–cell signaling at the SMG for B cell recruitment and survival.   and IHC (IgA2) staining in tracheal SMG. h, CellChat analysis as in f showing
a, Expression of PIGR and CCL28 in epithelial cells by violin plot. b, CellChat  signaling from HLA genes expressed by SMG epithelial cells, signaling to CD4
cell–cell interaction analysis pathways for CCL chemokines produced by SMG  on CD4 T cells. i, RNA expression of HLA-DRA, HLA-DRB1 and CD40 in B cells (as
epithelial cells and received by B cells (memory, naive and IgA/IgG/plasmablast  professional antigen-presenting cells for comparison) on violin plot, ciliated and
combined) or CD4 T cells (CD4-naive/CM, CD4-EM/Effector and CD4-TRM  SMG epithelial cells from scRNA-seq/snRNA-seq. j, IHC of HLA-DR and EpCAM in
combined) within airway tissue (trachea and bronchi). Arrow direction denotes  human airways showing strong expression of HLA-DR in the SMG (white dashed
chemokine-receptor pairs on specific cell types, arrowhead thickness reflects   line) compared to the surface epithelium (yellow dashed line). k, IHC staining
the relative expression of chemokine signal from each cell type. c,d, Expression  of CD4, CD45RO, HLA-DR and EpCAM, as indicated, in the airway SMG showing
localization and close contact of CD4+ CD45RO+ T cells with HLA-DR+ glands as
dot plot of relevant chemokines and corresponding receptors as shown in
b. e, smFISH (CCL28) and IHC (IgA2) staining in tracheal SMG. f, CellChat analysis  shown in the enlargement. Dotted lines enclose HLA-DR negative or low regions
of glands, yellow arrowheads denote CD4+ CD45RO+ T cells, white arrowheads in
as in b showing signaling of TNFSF13/APRIL and IL-6 from SMG epithelial cells to
the zoom-in show CD4+ CD45RO+ cells interacting with HLA-DR+ gland epithelial
relevant B cell subsets and CD4-naive/CM. The proportion of the circle for each
gene/cell type reflects the relative expression. g, smFISH (IL-6, TNFSF13/APRIL)  cells. Donors used for replicas in e, g, j and k are shown in Supplementary Table 9.
Extended Data Fig. 10a)68,76. We confirmed expression of CCL28 in SMG  to distal axis, where CCL28 is highest in SMG duct and serous cells of
by smFISH, and at the protein level by IHC (Fig. 5e and Extended Data  the trachea (Extended Data Fig. 10b,c). This gradient in serous cells
Fig. 10b), and observed a gradient of expression along the proximal  was statistically significant (P < 0.05) with Spearman’s two-tailed rank
Nature Genetics | Volume 55 | January 2023 | 66–77 73

Article https://doi.org/10.1038/s41588-022-01243-4
CD4 T cell
| SMG | CD4 0 D40LG |             |     |
| --- | ----------- | ----------- | --- |
|     | C IL6       | IR-Ven-Peri |     |
B-naive/
Venous
IL6R memory
|     | T                |      | endothelial |
| --- | ---------------- | ---- | ----------- |
|     | MHC C R+CD4 CCR6 | CCR6 | cell        |
 I
I
| Duct  |       | CCL20       |     |
| ----- | ----- | ----------- | --- |
|       | CCL20 | TACI        |     |
| cells |       | ICAM1/      |     |
|       |       | APRIL VCAM1 |     |
IL6
APRIL
|     |     | B C M A/  | Chemo-                  |
| --- | --- | --------- | ----------------------- |
|     |     | APRIL IL6 | a tt ra c ti o n  o f   |
|     |     | TA C I    | i m m u n e   ce ll s   |
|     |     | CCR10     | by IR-Ven-Peri          |
CCL28 IL6R
| Mucous |     | CCL28 |     |
| ------ | --- | ----- | --- |
cells
IgA
| Serous |     | B-plasma | SELE/ |
| ------ | --- | -------- | ----- |
| cells  |     | (IgA+)   | SELP  |
plgR
IL6
T-cell
Fig. 6 | Schematic of the human airway GAIN. Schematic of the GAIN showing  patterns between SMG epithelial cells, CD4 T cells, B naive/B memory cells and
immune cell recruitment and extravasation facilitated by venous endothelial  B plasma cells to attract immune cells and promote antigen-specific T cell-
cells and IR-Ven-Peri (immune recruiting venous perivascular cells) and signaling  dependent and T cell-independent pathways, leading to IgA secretion at the SMG.
correlation analysis. Cell–cell interaction analysis using CellChat77 on
presentation directly by the SMG epithelial cells. The expression of
cells from the airways again confirmed the CCL28-CCR10 axis between  HLA-DRA and HLA-DRB1 in SMG duct/SMG serous cells was compa-
SMG epithelial cells and B plasma cells (combined IgA, IgG and plas- rable to ciliated cells at the RNA level (Fig. 5i), but much higher at the
mablasts) and predicted SMG duct cells to recruit memory and naive   protein level (Fig. 5j). Similarly, the costimulatory gene CD40 was
B cells and CD4 T cells (combined CD4 subsets, excluding Tregs)  expressed in SMG epithelial cells (Fig. 5i). CD4 T cells also localized to
through CCL20 (refs. 78–80) (Fig. 5b–d). HLA-DRhigh nonmucous regions of glands (Fig. 5k and Extended Data
Fig. 10g,h). CD4 T cells in the glands were CD45RO+ (memory) cells,
In addition to immune cell recruitment, we explored signals sup-
porting B and plasma cell function in the GAIN. A proliferation-inducing  and could be seen closely interacting with HLA-DRhigh SMG epithelial
ligand (APRIL), a factor important for B cell survival, differentiation and  cells, suggesting direct cell–cell contact (Fig. 5k and Extended Data
class switching, was expressed by SMG duct/serous cells interacting  Fig. 10i–k). Overall, our data suggest that SMG Serous/duct cells can
with the receptors TACI and BCMA on B cells (Fig. 5f and Extended Data  present antigen to CD4 T cells, similar to airway and nasal epithe-
Fig. 10a). smFISH for APRIL in tissue confirmed expression in glands,  lial cells, which can promote T cell proliferation in vitro90–94. Antigen
especially in serous cells (LPO+RARRES1−APRILhigh), confirming the  presentation by SGPlowMHCIIhigh epithelial cells in the parenchyma of
specific B and IgA colocalization from our ST analysis in the APRILhigh
mice has been shown to regulate CD4-TRM responses, contributing
serous glands (Fig. 5g and Extended Data Fig. 10d,e). Interestingly,  to immune homeostasis95. MHCIIhigh SMG epithelial cells may have a
APRIL expression can be induced on intestinal epithelial cells leading  similar function in the airways.
to IgA2 class-switch recombination (CSR) in the local tissue environ- In conclusion, we identified the colocalization of IgA plasma cells,
ment81. We found activation-induced cytidine deaminase (AICDA)  naive/memory B cells and T cells at the serous glands and described
expression in a few B memory cells, suggesting the possibility of local  molecular signaling pathways for the recruitment and maintenance
CSR at the SMG (Extended Data Fig. 10f). of immune cells at the SMG. The described pathways are functional
In combination with APRIL, IL-6 induces and supports long-lived  in secondary lymphoid structures such as MALT, and we now suggest
plasma cells, potently induces IgA secretion82,83 and increases IgA secre- they can establish the GAIN (Fig. 6) of the human airways.
tion in COPD84. In our data, SMG duct/SMG serous cells expressed IL-6
(Fig. 5g), which was predicted to interact with IL-6R/IL-6ST on B plasma  Discussion
and CD4-naive/CD4-CM T cells (Fig. 5f and Extended Data Fig. 10a). IL-6  By integrating scRNA-seq/snRNA-seq with ST, we provide fine-grained
has been shown as a required factor for CD4 T cell memory formation  resolution of 80 cell types/states in the human lung and airways. Eleven
and for overcoming Treg mediated suppression85. Salivary gland epi-
previously unannotated cell types/states were identified and mapped to
thelial cells are known to induce B cell responses via IL-6 both directly  distinct micro-anatomical tissue environments. Our data have contrib-
(T cell-independent) and via T cell-dependent mechanisms86. IL-6 is  uted to the HLCA10, which provides means for assessing intraindividual
also upregulated in serum and bronchoalveolar lavage fluid in asthma  variation and effects of clinical covariates. Our in-depth study reveals
and COPD patients, suggesting the importance of GAIN in disease87–89. airway tissue niches encompassing previously unresolved cell types
CellChat also predicted interactions between HLA genes expressed  and their interactions, as well as unexpected properties of cell signal-
by SMG epithelial cells, and CD4 T cells (Fig. 5h,i) that indicate antigen  ing relationships. We provide transcriptomic profiles of human airway
Nature Genetics | Volume 55 | January 2023 | 66–77 74

Article https://doi.org/10.1038/s41588-022-01243-4
chondrocytes, cells of the peripheral nerve bundles, SMG duct cells, 8. Adams, T. S. et al. Single-cell RNA-seq reveals ectopic and
enhanced resolution in fibroblast, macrophage and lymphocyte sub- aberrant lung-resident cell populations in idiopathic pulmonary
sets and distinguish between pulmonary versus systemic vasculature fibrosis. Sci. Adv. 6, eaba1983 (2020).
and pericytes. We highlight potential disease associations for some 9. Goldfarbmuren, K. C. et al. Dissecting the cellular specificity of
of these new populations, such as PB-fibro for COPD and IPF. Finally, smoking effects and reconstructing lineages in the human airway
we discover the GAIN with likely relevance in inflammatory and infec- epithelium. Nat. Commun. 11, 2485 (2020).
tious diseases. We present these data as a resource to the community 10. Sikkema, L. et al. An integrated cell atlas of the human
as open-access downloadable files and through our interactive web lung in health and disease. Preprint at bioRxiv https://doi.
portal (lungcellatlas.org). org/10.1101/2022.03.10.483747 (2022).
The GAIN defines an immunomodulatory role for SMG epithelial 11. Travaglini, K. J. et al. A molecular cell atlas of the human
cells, which are central to signaling circuits for local IgA responses. lung from single-cell RNA sequencing. Nature 587, 619–625
Specifically, we highlight that IgA plasma cells, B cells and CD4 T cells (2020).
are recruited via chemokines secreted by IR-pericytes and SMG duct/ 12. Sun, X. et al. A census of the lung: CellCards from LungMAP. Dev.
serous cells. The survival, maturation and, potentially, class switching Cell 57, 112–145 (2022).
of B lineage cells are supported by APRIL and IL-6, providing T cell inde- 13. Kleshchevnikov et al. Cell2location maps fine-grained cell types
pendent factors. Additionally, SMG duct/serous cells have the potential in spatial transcriptomics. Nat Biotechnol 40, 661–671 https://doi.
to induce and/or modulate antigen-specific responses through the org/10.1038/s41587-021-01139-4 (2022).
expression of MHC-II and CD40. Many of these pathways have been 14. Kapoor, V. N. et al. Gremlin 1+ fibroblastic niche maintains
observed in other tissues, particularly in the salivary glands and within dendritic cell homeostasis in lymphoid tissues. Nat. Immunol. 22,
secondary lymphoid tissues such as Peyer’s patches. No such second- 571–585 (2021).
ary lymphoid structures have been observed within healthy airways. 15. Wang, X. et al. Follicular dendritic cells help establish follicle
We hypothesize that GAIN is an important site for local induction of identity and promote B cell retention in germinal centers. J. Exp.
immune responses and homeostasis. Med. 208, 2497–2510 (2011).
This newly defined IgA immune niche is likely to play an important 16. Marshall, A. J. et al. FDC-SP, a novel secreted protein expressed by
role in common lung diseases as well as respiratory infections—IgA plasma follicular dendritic cells. J. Immunol. 169, 2381–2389 (2002).
cells are increased in the airways of COPD84 and patients with cystic 17. Elliot, J. G. et al. Aggregations of lymphoid cells in the airways of
fibrosis72, and pIgR-mediated IgA transport is dysregulated in asthma96 nonsmokers, smokers, and subjects with asthma. Am. J. Respir.
and pulmonary fibrosis97. In patients with COVID-19, early severe acute Crit. Care Med. 169, 712–718 (2004).
respiratory syndrome coronavirus 2 (SARS-CoV-2) neutralization was 18. Elmentaite, R., Kumasaka, N., Roberts, K. et al. Cells of the human
more closely correlated with IgA than IgM or IgG98 and we report higher intestinal tract mapped across space and time. Nature 597,
proportions of IgA plasma cells in the airways of patients with COVID-19. 250–255 (2021). https://doi.org/10.1038/s41586-021-03852-1
Nasal vaccines can induce a strong local sIgA response and prevent viral 19. Baarsma, H. A. et al. Noncanonical WNT-5A signaling impairs
shedding99 in the respiratory tract100. A better understanding of the GAIN endogenous lung repair in COPD. J. Exp. Med. 214, 143–163 (2017).
is therefore highly relevant for maintaining lung health and providing 20. Castaldi, P. J. et al. Genome-wide association identifies
immunity to respiratory infections such as COVID-19. regulatory loci associated with distinct local histogram
emphysema patterns. Am. J. Respir. Crit. Care Med. 190,
Online content 399–409 (2014).
Any methods, additional references, Nature Portfolio reporting sum- 21. Spira, A. et al. Gene expression profiling of human lung tissue
maries, source data, extended data, supplementary information, from smokers with severe emphysema. Am. J. Respir. Cell Mol.
acknowledgements, peer review information; details of author contri- Biol. 31, 601–610 (2004).
butions and competing interests; and statements of data and code avail- 22. Doherty, L. & Sanjay, A. LGRs in skeletal tissues: an emerging
ability are available at https://doi.org/10.1038/s41588-022-01243-4. role for Wnt-associated adult stem cell markers in bone. JBMR 4,
e10380 (2020).
References 23. Bochukova, E. G. et al. Rare mutations of FGFR2 causing Apert
1. Angelidis, I. et al. An atlas of the aging lung mapped by single cell syndrome: identification of the first partial gene deletion, and
transcriptomics and deep tissue proteomics. Nat. Commun. 10, an Alu element insertion from a new subfamily. Hum. Mutat. 30,
963 (2019). 204–211 (2009).
2. Kato, A., Hulse, K. E., Tan, B. K. & Schleimer, R. P. B-lymphocyte 24. Adam, M. P. et al. (eds.) Gene Reviews (University of Washington,
lineage cells and the respiratory system. J. Allergy Clin. Immunol. 2008).
131, 933–957 (2013). 25. Chen, B., Banton, M. C., Singh, L., Parkinson, D. B. & Dun, X.-P.
3. Schiller, H. B. et al. The human lung cell atlas: a high-resolution Single cell transcriptome data analysis defines the heterogeneity
reference map of the human lung in health and disease. Am. J. of peripheral nerve cells in homeostasis and regeneration. Front.
Respir. Cell Mol. Biol. 61, 31–41 (2019). Cell. Neurosci. 15, 624826 (2021).
4. Ardini-Poleske, M. E. et al. LungMAP: the molecular atlas of lung 26. Gerber, D. et al. Transcriptional profiling of mouse peripheral
development program. Am. J. Physiol. Lung Cell. Mol. Physiol. 313, nerves to the single-cell level to build a sciatic nerve ATlas
L733–L740 (2017). (SNAT). eLife 10, e58591 (2021).
5. Wilbrey-Clark, A., Roberts, K. & Teichmann, S. A. Cell atlas 27. Renthal, W. et al. Transcriptional reprogramming of distinct
technologies and insights into tissue architecture. Biochem. J. peripheral sensory neuron subtypes after axonal injury. Neuron
477, 1427–1442 (2020). 108, 128–144 (2020).
6. Plasschaert, L. W. et al. A single-cell atlas of the airway epithelium 28. Wolbert, J. et al. Redefining the heterogeneity of peripheral nerve
reveals the CFTR-rich pulmonary ionocyte. Nature 560, 377–381 cells in health and autoimmunity. Proc. Natl Acad. Sci. USA 117,
(2018). 9466–9476 (2020).
7. Vieira Braga, F. A. et al. A cellular census of human lungs 29. Adameyko, I. & Ernfors, P. Nerves do it again: donation of
identifies novel cell states in health and in asthma. Nat. Med. 25, mesenchymal cells for tissue regeneration. Cell Stem Cell 24,
1153–1163 (2019). 195–197 (2019).
Nature Genetics | Volume 55 | January 2023 | 66–77 75

Article https://doi.org/10.1038/s41588-022-01243-4
30. Murfee, W. L., Skalak, T. C. & Peirce, S. M. Differential arterial/ 52. Takano, H. et al. Protective role of metallothionein in acute lung
venous expression of NG2 proteoglycan in perivascular cells injury induced by bacterial endotoxin. Thorax 59, 1057–1062
along microvessels: identifying a venule-specific phenotype. (2004).
Microcirculation 12, 151–160 (2005). 53. Mukaida, N. Pathophysiological roles of interleukin-8/CXCL8 in
31. Proebstl, D. et al. Pericytes support neutrophil subendothelial cell pulmonary diseases. Am. J. Physiol. Lung Cell. Mol. Physiol. 284,
crawling and breaching of venular walls in vivo. J. Exp. Med. 209, L566–L577 (2003).
1219–1234 (2012). 54. Reynolds, G. et al. Developmental cell programs are
32. Madissoon, E. et al. scRNA-seq assessment of the human lung, co-opted in inflammatory skin disease. Science 371,
spleen, and esophagus tissue stability after cold preservation. eaba6500 (2021).
Genome Biol. 21, 1 (2019). 55. Hadley, G. A., Bartlett, S. T., Via, C. S., Rostapshova, E. A. &
33. Nowicki-Osuch, K. et al. Molecular phenotyping reveals the Moainie, S. The epithelial cell-specific integrin, CD103 (alpha
identity of Barrett’s esophagus and its malignant transition. E integrin), defines a novel subset of alloreactive CD8+ CTL. J.
Science 373, 760–767 (2021). Immunol. 159, 3748–3756 (1997).
34. Widdicombe, J. H. & Wine, J. J. Airway gland structure and 56. Dominguez-Conde et al. Cross-tissue immune cell analysis
function. Physiol. Rev. 95, 1241–1319 (2015). reveals tissue-specific features in humans. Science (2022)Vol 376,
35. Meyrick, B., Sturgess, J. M. & Reid, L. A reconstruction of the Issue 6594. https://doi.org/10.1126/science.abl5197
duct system and secretory tubules of the human bronchial 57. Piet, B. et al. CD8 T cells with an intraepithelial phenotype
submucosal gland. Thorax 24, 729–736 (1969). upregulate cytotoxic function upon influenza infection in human
36. Hegab, A. E. et al. Isolation and in vitro characterization lung. J. Clin. Invest. 121, 2254–2263 (2011).
of basal and submucosal gland duct stem/progenitor cells 58. Wu, T. et al. Lung-resident memory CD8 T cells (TRM) are
from human proximal airways. Stem Cells Transl. Med. 1, indispensable for optimal cross-protection against pulmonary
719–724 (2012). virus infection. J. Leukoc. Biol. 95, 215–224 (2014).
37. Tata, A. et al. Myoepithelial cells of submucosal glands can 59. Ghilas et al. Natural killer cells and dendritic epidermal γδ T cells
function as reserve stem cells to regenerate airways after injury. orchestrate type 1 conventional DC spatiotemporal repositioning
Cell Stem Cell 22, 668–683 (2018). toward CD8+ T cellsiScience. 2021 Sep 24; 24(9): 103059. https://
38. Hegab, A. E. et al. Novel stem/progenitor cell population from doi.org/10.1016/j.isci.2021.103059
murine tracheal submucosal gland ducts with multipotent 60. Böttcher, J. P. et al. NK cells stimulate recruitment of cDC1 into the
regenerative potential. Stem Cells 29, 1283–1293 (2011). tumor microenvironment promoting cancer immune control. Cell
39. Young, A. M. H. et al. A map of transcriptional heterogeneity and 172, 1022–1037 (2018).
regulatory variation in human microglia. Nat. Genet. 53, 861–868 61. Ma, M. et al. NKG2CNKG2A natural killer cells are associated with
(2021). a lower viral set point and may predict disease progression in
40. Borchers, M. T. et al. The role of T cells in the regulation of individuals with primary HIV infection. Front. Immunol. 8, 1176
acrolein-induced pulmonary inflammation and epithelial-cell (2017).
pathology. Res. Rep. Health Eff. Inst.(146), 5–29 (2009). 62. Fang, M. et al. CD94 is essential for NK cell-mediated resistance
41. Motz, G. T. et al. Chronic cigarette smoke exposure primes NK cell to a lethal viral disease. Immunity 34, 579–589 (2011).
activation in a mouse model of chronic obstructive pulmonary 63. Triebel, F. et al. LAG-3, a novel lymphocyte activation gene closely
disease. J. Immunol. 184, 4460–4469 (2010). related to CD4. J. Exp. Med. 171, 1393–1405 (1990).
42. Wortham, B. W., Eppert, B. L., Flury, J. L., Morgado Garcia, S. 64. Siegers, G. M., Barreira, C. R., Postovit, L.-M. & Dekaban, G. A.
& Borchers, M. T. TLR and NKG2D signaling pathways mediate CD11d β2 integrin expression on human NK, B, and γδ T cells. J.
CS-induced pulmonary pathologies. PLoS ONE 8, e78735 (2013). Leukoc. Biol. 101, 1029–1035 (2017).
43. Deprez, M. et al. A single-cell atlas of the human healthy airways. 65. Treiner, E. et al. Selection of evolutionarily conserved
Am. J. Respir. Crit. Care Med. 202, 1636–1645 (2020). mucosal-associated invariant T cells by MR1. Nature 422, 164–169
44. Chakarov, S. et al. Two distinct interstitial macrophage (2003).
populations coexist across tissues in specific subtissular niches. 66. Corthésy, B. Multi-faceted functions of secretory IgA at mucosal
Science 363, eaau0964 (2019). surfaces. Front. Immunol. 4, 185 (2013).
45. Evren, E. et al. Distinct developmental pathways from blood 67. Kunkel, E. J. & Butcher, E. C. Plasma-cell homing. Nat. Rev.
monocytes generate human lung macrophage diversity. Immunol. 3, 822–829 (2003).
Immunity 54, 259–275 (2021). 68. Morteau, O. et al. An indispensable role for the chemokine
46. Pirzgalska, R. M. et al. Sympathetic neuron-associated receptor CCR10 in IgA antibody-secreting cell accumulation. J.
macrophages contribute to obesity by importing and Immunol. 181, 6309–6315 (2008).
metabolizing norepinephrine. Nat. Med. 23, 1309–1318 (2017). 69. O’Connor, B. P. et al. BCMA is essential for the survival of
47. Wolf, Y. et al. Brown-adipose-tissue macrophages control tissue long-lived bone marrow plasma cells. J. Exp. Med. 199, 91–98
innervation and homeostatic energy expenditure. Nat. Immunol. (2004).
18, 665–674 (2017). 70. Soutar, C. A. Distribution of plasma cells and other cells
48. Hulsmans, M. et al. Macrophages facilitate electrical conduction containing immunoglobulin in the respiratory tract of normal
in the heart. Cell 169, 510–522 (2017). man and class of immunoglobulin contained therein. Thorax 31,
49. Chang, D., Sharma, L. & Dela Cruz, C. S. Chitotriosidase: a marker 158–166 (1976).
and modulator of lung disease. Eur. Respir. Rev. 29, 190143 71. Yoshida et al. Local and systemic responses to SARS-CoV-2
(2020). infection in children and adults. Nature 602, 321–327 (2022).
50. Artur Krężel, W. M. The functions of metamorphic https://doi.org/10.1038/s41586-021-04345-x
metallothioneins in zinc and copper metabolism. Int. J. Mol. Sci. 72. Collin, A. M. et al. Lung immunoglobulin A immunity
18, 1237 (2017). dysregulation in cystic fibrosis. EBioMedicine 60, 102974 (2020).
51. Subramanian Vignesh, K. & Deepe, G. S. Jr. Metallothioneins: 73. Zhu, J. et al. Plasma cells and IL-4 in chronic bronchitis and
emerging modulators in immunity and infection. Int. J. Mol. Sci. chronic obstructive pulmonary disease. Am. J. Respir. Crit. Care
18, 2197 (2017). Med. 175, 1125–1133 (2007).
Nature Genetics | Volume 55 | January 2023 | 66–77 76

Article https://doi.org/10.1038/s41588-022-01243-4
74. Rowley, A. H. et al. IgA plasma cell infiltration of 90. Rossi, G. A. et al. Human ciliated bronchial epithelial cells:
proximal respiratory tract, pancreas, kidney, and expression of the HLA-DR antigens and of the HLA-DR alpha gene,
coronary artery in acute Kawasaki disease. J. Infect. Dis. 182, modulation of the HLA-DR antigens by gamma-interferon and
1183–1191 (2000). antigen-presenting function in the mixed leukocyte reaction. Am.
75. Matsuo, K. et al. CCL28-deficient mice have reduced IgA J. Respir. Cell Mol. Biol. 3, 431–439 (1990).
antibody-secreting cells and an altered microbiota in the colon. J. 91. Kalb, T. H., Chuang, M. T., Marom, Z. & Mayer, L. Evidence for
Immunol. 200, 800–809 (2018). accessory cell function by class II MHC antigen-expressing airway
76. Wilson, E. & Butcher, E. C. CCL28 controls immunoglobulin (Ig) epithelial cells. Am. J. Respir. Cell Mol. Biol. 4, 320–329 (1991).
A plasma cell accumulation in the lactating mammary gland and 92. Cagnoni, F. et al. CD40 on adult human airway epithelial cells:
IgA antibody transfer to the neonate. J. Exp. Med. 200, 805–809 expression and proinflammatory effects. J. Immunol. 172,
(2004). 3205–3214 (2004).
77. Jin, S. et al. Inference and analysis of cell-cell communication 93. Gormand, F. et al. CD40 expression by human bronchial epithelial
using CellChat. Nat. Commun. 12, 1–20 (2021). cells. Scand. J. Immunol. 49, 355–361 (1999).
78. Lee, A. Y. S. et al. Expression of membrane-bound CC chemokine 94. Tanaka, H. et al. CD40 and IFN-gamma dependent T cell
ligand 20 on follicular T helper cells in T–B-cell conjugates. Front. activation by human bronchial epithelial cells. J. Med. Invest. 48,
Immunol. 8, 1871 (2017). 109–117 (2001).
79. Elgueta, R. et al. CCR6-dependent positioning of memory B cells 95. Shenoy, A. T. et al. Antigen presentation by lung epithelial cells
is essential for their ability to mount a recall response to antigen. directs CD4+ TRM cell function and regulates barrier immunity.
J. Immunol. 194, 505–513 (2015). Nat. Commun. 12, 1–16 (2021).
80. Bowman, E. P. et al. Developmental switches in chemokine 96. Ladjemi, M. Z. et al. Bronchial epithelial IgA secretion is impaired
response profiles during B cell differentiation and maturation. J. in asthma. Role of IL-4/IL-13. Am. J. Respir. Crit. Care Med. 197,
Exp. Med. 191, 1303–1318 (2000). 1396–1409 (2018).
81. He, B. et al. Intestinal bacteria trigger T cell-independent 97. Planté-Bordeneuve, T. et al. The pIgR-IgA system as a new player
immunoglobulin A(2) class switching by inducing epithelial-cell in lung fibrosis. Eur. Respir. J. 58, PA867 (2021).
secretion of the cytokine APRIL. Immunity 26, 812–826 (2007). 98. Sterlin, D. et al. IgA dominates the early neutralizing antibody
82. Beagley, K. W. et al. Interleukins and IgA synthesis. response to SARS-CoV-2. Sci. Transl. Med. 13, eabd2223 (2021).
Human and murine interleukin 6 induce high rate IgA 99. Bleier, B. S., Ramanathan, M. & Lane, A. P. COVID-19 vaccines
secretion in IgA-committed B cells. J. Exp. Med. 169, may not prevent nasal SARS-CoV-2 infection and asymptomatic
2133–2148 (1989). transmission. Otolaryngol. Head. Neck Surg. 164, 305–307 (2021).
83. Hirano, T. et al. Complementary DNA for a novel human 100. Tiboni, M., Casettari, L. & Illum, L. Nasal vaccination against
interleukin (BSF-2) that induces B lymphocytes to produce SARS-CoV-2: synergistic or alternative to intramuscular vaccines?
immunoglobulin. Nature 324, 73–76 (1986). Int. J. Pharm. 603, 120686 (2021).
84. Ladjemi, M. Z. et al. Increased IgA production by B-cells in COPD
via lung epithelial interleukin-6 and TACI pathways. Eur. Respir. J. Publisher’s note Springer Nature remains neutral with regard to
45, 980–993 (2015). jurisdictional claims in published maps and institutional affiliations.
85. Nish, S. A. et al. T cell-intrinsic role of IL-6 signaling in primary and
memory responses. eLife 3, e01949 (2014). Open Access This article is licensed under a Creative Commons
86. Gong, Y.-Z. et al. Differentiation of follicular helper T cells by Attribution 4.0 International License, which permits use, sharing,
salivary gland epithelial cells in primary Sjögren’s syndrome. J. adaptation, distribution and reproduction in any medium or format,
Autoimmun. 51, 57–66 (2014). as long as you give appropriate credit to the original author(s) and the
87. Mercedes Rincon, C. G. I. Role of IL-6 in asthma and other source, provide a link to the Creative Commons licence, and indicate
inflammatory pulmonary diseases. Int. J. Biol. Sci. 8, if changes were made. The images or other third party material in this
1281 (2012). article are included in the article’s Creative Commons licence, unless
88. Savelikhina, I., Ostrovskyy, M., Ostrovska, K., Kulynych-Miskiv, M. indicated otherwise in a credit line to the material. If material is not
& Varunkiv, O. Proinflammatory cytokine IL-6 detetion in severe included in the article’s Creative Commons licence and your intended
COPD patients: focus on roflumilast. Eur. Respir. J. 52, OA3267 use is not permitted by statutory regulation or exceeds the permitted
(2018). use, you will need to obtain permission directly from the copyright
89. Tillie-Leblond, I. et al. Balance between proinflammatory holder. To view a copy of this licence, visit http://creativecommons.
cytokines and their inhibitors in bronchial lavage from patients org/licenses/by/4.0/.
with status asthmaticus. Am. J. Respir. Crit. Care Med. 159,
487–494 (1999). © The Author(s) 2022, corrected publication 2025
1Wellcome Sanger Institute, Wellcome Genome Campus, Cambridge, UK. 2European Molecular Biology Laboratory, European Bioinformatics Institute
(EMBL-EBI), Wellcome Trust Genome Campus, Cambridge, UK. 3Molecular Immunity Unit, University of Cambridge Department of Medicine, MRC
Laboratory of Molecular Biology, Francis Crick Ave, Cambridge, UK. 4Department of Genetics and Evolutionary Biology, Institute of Biosciences,
University of São Paulo, São Paulo, Brazil. 5Kindai University Faculty of Pharmacy, Higashi-osaka, Japan. 6UCL Respiratory, Division of Medicine, University
College London Hospitals NHS Foundation Trust, London, UK. 7Department of Surgery, University of Cambridge, and Cambridge NIHR Biomedical
Research Centre, Cambridge, UK. 8European Molecular Biology Laboratory (EMBL), Heidelberg, Germany. 9Deutsches Krebsforschungszentrum (DKFZ),
Heidelberg, Germany. 10Theory of Condensed Matter, Cavendish Laboratory/Department of Physics, University of Cambridge, Cambridge, UK.
11These authors contributed equally: Elo Madissoon, Amanda J. Oliver. e-mail: st9@sanger.ac.uk; km16@sanger.ac.uk
Nature Genetics | Volume 55 | January 2023 | 66–77 77

Article https://doi.org/10.1038/s41588-022-01243-4
Methods amplification and 3′ gene expression library construction were per-
Experimental methods formed according to the user guide and libraries were sequenced on
Access to human tissue and ethics oversight. Samples were obtained the Novaseq platform.
from deceased transplant organ donors by the Collaborative Bioreposi-
tory for Translational Medicine (CBTM) with informed consent from Spatial transcriptomics. Samples ≤0.5 cm2 were cut from the five lung
the donor families and approval from the National Research Ethics and airway locations outlined above. Most of the parenchyma tissue was
Services (NRES) Committee of East of England, Cambridge South removed from bronchi samples, which were embedded in OCT and flash
(15/EE/0152). CBTM operates in accordance with UK Human Tissue frozen in −60 °C isopentane (for six donors; Supplementary Table 9)
Authority guidelines. or fixed for 24 h in 10% neutral buffered formalin and processed into
wax (FFPE, for one donor; Supplementary Table 9). H&E staining was
Tissue dissociation and single-cell sequencing. Tissue was collected used to determine the morphology of tissue blocks before proceed-
from 13 donors from five lung locations including trachea, bronchi at ing with ST. Sections of 10 µm (fresh frozen samples) or 5 µm (FFPE)
the second/third generation, bronchi at the fourth generation, upper were then cut from the blocks onto Visium slides (10X Genomics) and
left lobe parenchyma and lower left lobe parenchyma (Fig. 1a and Sup- processed according to the manufacturer’s protocol. Further details
plementary Tables 1–3). In total, 11 donors were profiled for fresh and on samples are in Supplementary Table 3 and Supplementary Fig. 1.
frozen transcriptomic analysis with two additional donors used for H&E images generated during the Visium protocol were captured at
FFPE ST and smFISH/IHC validation (summarized in Supplementary ×20 magnification on a Hamamatsu Nanozoomer S60.
Table 9). Following collection at the clinic, samples (range: 1–4 cm3) Dual-indexed libraries were prepared as in the 10X Genomics
were immediately placed into cold Hypothermasol FRS32. Within 12 h protocol, pooled at 2.25 nM and sequenced (four samples/Illumina
after circulation ceased, samples were dissociated (seven donors; Novaseq SP flow cell) with read lengths 28 bp R1, 10 bp i7 index, 10 bp
Supplementary Tables 1 and 9) and/or preserved in optimal cutting i5 index, 90 bp R2 for fresh frozen samples or 50 bp R2 for FFPE.
temperature (OCT) compound and frozen in isopentane at −60 °C for
later spatial analysis (six donors; Supplementary Table 3) and nuclei smFISH. smFISH was performed in multiple sections from at least
isolation (seven donors; Supplementary Tables 2 and 9). Most samples two donors (Supplementary Table 9). Tissue blocks for smFISH
(n = 5) were digested using liberase and trypsin, and CD45 positive (RNAScope) in situ hybridization were chosen based on H&E staining.
cells loaded on 10X as a separate fraction (protocols.io.39ygr7w). One Ten micron-thick cryosections cut onto superfrost plus slides were
donor was digested with collagenase D for comparison (protocols. processed using the RNAScope 2.5 LS multiplex fluorescent assay
io.34kgquw; Supplementary Tables 1 and 2). Briefly, tissue dissociation (ACD, Bio-Techne) on the Leica BOND RX system (Leica). Fresh frozen
used (for five donors) 1 g of lung tissue washed with PBS, minced finely lung sections were fixed for 90 min with chilled 4% paraformaldehyde,
with scalpels, before treatment with 13 U ml−1 liberase TL and 0.1 mg ml−1 washed twice with PBS and dehydrated through an ethanol series (50%,
DNase I for 30 min at 37 °C with rocking. Cells were filtered through a 70% and 100% ethanol) before processing according to the manufac-
70 µm strainer, washed with neutralization media (RPMI+ 20% FBS) and turer’s protocol with protease IV treatment. Samples were first tested
pelleted (sample P1). Tissue remaining in the cell strainer was digested with RNAScope positive and negative control probes before proceed-
with 0.25% trypsin-EDTA with DNase I for 30 min at 37 °C with rocking, ing to run probes of interest. Slides were stained for DAPI (nuclei) and
filtered and washed with neutralization media. Meanwhile, sample three to four probes of interest, with fluorophores Opal 520, Opal 570,
P1 was treated with red blood cell lysis buffer before being separated Opal 650 and ATTO 425 at between 1:500 and 1:1,000 concentration.
into CD45 positive and negative fractions using MACS (Miltenyi, as These were then imaged on a Perkin Elmer Opera Phenix high-content
according to the manufacturer’s protocol). The CD45 negative fraction screening system with water immersion at ×20 magnification. Imaging
was pooled with cells from trypsin treatment, resulting in the follow- data were processed using Omero (Open Microscopy Environment).
ing two samples for loading on 10X: CD45 positive cells from liberase
TL digestion (to enrich for immune cells) and pooled CD45 negative Mouse samples. Wild-type C57/BL6 mouse samples were obtained
liberase-treated cells with trypsin-treated cells (nonimmune fraction). from Kindai University, Japan (courtesy of T. Nakayama) and Charles
Both fractions were resuspended in 0.04% BSA/PBS, counted and River, USA (AMSbio). Male (colon samples) and female (all other sam-
loaded on the 10X Genomics Chromium Controller, aiming to capture ples) mice were maintained in specific pathogen-free conditions and
5,000 cells, according to the manufacturer’s protocol. The 10X Genom- used at 8- to10-week old. All animal experiments for mice obtained from
ics chemistry is included in Supplementary Table 1. Kindai University were approved by the Centre of Animal Experiments
at Kindai University. Mouse tissue from Charles River was purchased
Single-nucleus sequencing. Our single nuclei isolation method101 from a certified animal supplier through AMSbio, with an internal ethi-
from frozen tissue (Supplementary Table 2) used 8 × 50 µm thick sec- cal approval process for broadly defined research use.
tions which were homogenized using a glass Dounce homogenizer
(Sigma) in nuclei isolation buffer (NIM; 0.25 M sucrose, 0.005 M MgCl, Tissue preservation and antibody staining. For IBEX staining, the
2
0.025 M KCl, 0.01 M Tris (buffer pH7.4), 0.001 M DTT and 0.1% Triton fresh airway tissue was received in cold Hypothermasol, fixed with
X-100) in the presence of Complete protease inhibitors (Roche) and 1% PFA solution for 24 h at 4 ˚C and transferred to cold 10% and 30%
RNAse inhibitors RNasin (Promega)—0.4 U µl−1 and SUPERase-In (Inv- sucrose gradient for ~8 and ~12 h, respectively, before freezing in OCT.
itrogen) 0.2 U µl−1). Tissue was homogenized using ~15 strokes with The fixed tissue was sectioned at 10–30 µm thickness. Iterative staining
pestle A (clearance 0.0028–0.0047 in.) and then pestle B (clearance of human trachea sections was performed as described by Radtke et al.
0.0008–0.0022 in.). Isolated nuclei were filtered through a 40 µM (ref. 102). Sections were permeabilized and blocked in 0.1 M Tris, con-
filter, collected at 2,000g and resuspended in 0.5 ml of storage buffer taining 0.1% Triton (Sigma), 1% normal mouse serum, 1% normal goat
(PBS containing 4% BSA and RNasin (Promega)—0.2 U µl−1). Nuclei were serum and 1% BSA (R&D). Primary antibodies were incubated for 2 h at
incubated with NucBlue (ThermoFisher) and purified from debris by room temperature and secondary for 1 h at room temperature in a wet
FACs sorting, stained with Trypan blue and counted. Five thousand chamber, washed three times in PBS and mounted in Fluoromount-G
nuclei from five different samples were pooled and all 25,000 nuclei (Southern Biotech). Images were acquired using a TCS SP8 (Leica)
were loaded onto the 10X chromium controller using the 3’ v3.1 kit as inverted confocal microscope. The coverslip was removed, slides were
per the Chromium Single Cell 3’ Reagent Kits v3 User Guide, targeting washed three times in PBS and fluorochromes were then bleached using
to recover ~3,000 nuclei per sample. Post-GEM-RT cleanup, cDNA a 1 mg ml−1 solution of lithium borohydride in water (Acros Organics) for
Nature Genetics

Article https://doi.org/10.1038/s41588-022-01243-4
15 min at room temperature. Slides were washed in PBS (three times) different donors. The distribution of cell types with respect to loca-
before repeating staining, up to a total of five rounds of staining. Raw tion, material and donor variables are shown in Supplementary Table 7
imaging data were processed using Imaris (Bitplane) using Hoechst as and visualized by the contribution of donor in Supplementary Fig. 2.
fiducial for the alignment of subsequent images. The staining setup and
antibody information are in Supplementary Table 6. Spatial mapping of cell types using Visium ST and cell2location.
For human airway samples and mouse trachea/colon samples, Visium ST data was analyzed by integrating scRNA-seq/snRNA-seq and
costained for CCL28 and IgA2/IgA (Supplementary Table 6), 10 µm spatial transcriptomes with the cell2location method (v0.1)13. Cell2loca-
thick OCT embedded fresh frozen sections were fixed with cold ace- tion estimates reference gene expression signatures of cell types from
tone (human) or room temperature acetone:ethanol (1:1) (mouse) for scRNA-seq using Negative Binomial regression that accounts for batch
20 min, followed by blocking in the buffer above (human) or 2% BSA/ effects. In Extended Data Fig. 3b, we extended the cell type reference
PBS with 1:800 rat serum (Abcam) (mouse) for 1 h at room temperature. to germinal center cell types from a published human gut dataset18.
Primary antibodies were incubated in blocking buffer for 1 h at room Cell2location uses the reference signatures to estimate absolute spatial
temperature and washed three times in PBS. Secondary antibodies were abundance of cell types, integrating and normalizing data across 11
incubated for 1 h at room temperature followed by another three times fresh frozen Visium sections (five were excluded based on quality con-
PBS washes and 5 µg ml−1 DAPI (Invitrogen) for 5 min before coverslip- trol metrics). 10X Visium data were processed to untransformed and
ping with ProLong Gold Antifade Mountant (LifeTechnologies). Slides unnormalized mRNA counts, filtered to genes shared with scRNA-seq,
were imaged using Hamamatsu S60 slide scanner at ×40 magnifica- with hyperparameters in cell2location based on the tissue and experi-
tion. Imaging data were processed using Omero (Open Microscopy ment quality as follows:
Environment).
(1) Expected cell abundance per location Nˆ=20
(2) Regularization of within-experiment variation in RNA detection
Computational analysis
sensitivity of αy=20
Mapping of gene expression libraries. scRNA-seq and snRNA-seq
gene expression libraries were mapped with Cell Ranger 3.0.2, and The model was trained until convergence (40,000 iterations).
Visium libraries were mapped with Space Ranger 1.1.0 from 10X Genom- Loss function (ELBO) scaling by locations × genes was used. Pearson
ics (https://support.10xgenomics.com). Both types of libraries were correlation between log (x + 1)-transformed observed mRNA counts
10
mapped to an Ensembl 93-based reference (10X-provided GRCh38 and expected mRNA amount from the cell2location model assessed
reference, version 3.0.0). For nuclei samples, the reference was altered the model quality (Pearson R = 0.745).
into a pre-mRNA reference as per 10X instructions. TCR/BCR libraries Micro-anatomical tissue environments were labeled from the
were mapped with Cell Ranger 4.0.0 to the 10X-provided VDJ reference, H&E images. Only Visium spots aligned and annotated as ‘tissue’ were
version 4.0.0. used for analysis (manual annotation). Specific tissue environments
are listed in Supplementary Table 5 and at lungcellatlas.org loupe
scRNA-seq and snRNA-seq analysis. The CellRanger unfiltered matri- browser. Visium FFPE (four sections) allowed better conservation of
ces were used as an input for the SoupX v1.0.0 algorithm103 to remove morphology and therefore had more detailed manual annotations
ambient RNA contamination, according to the tutorial (https://github. including the separation of mucous glands from the seromucous/
com/constantAmateur/SoupX). For each snRNA-seq library, CellRanger other glands. The annotation of mucous-only glands was conserva-
filtered nuclei subjected to QC filters, pass QC nuclei were processed tive to distinctly separate mucous-only glands, as the transcripts from
using standard scanpy pipeline and were clustered to form five to ten high-count serous cells contaminated neighboring spots. The manual
clusters. Nuclei that did not pass QC were assigned to those clusters by annotations were used to compute cell abundance of each cell type
logistic regression. This clustering was then passed to SoupX, to derive across micro-environments.
a set of cluster-specific genes for automatic estimation of contamina- We further used NMF of cell abundance estimated by cell2lo-
tion rate. Default values were used for SoupX’s functions, except for cation for unbiased microenvironment identification. Scikit-learn
‘autoEstCont()’ where ‘soupQuantile’ was set to 0.8. The single-cell NMF implementation from cell2location package was used. NMF was
and nuclei libraries with SoupX correction were analyzed using the trained with a range of factor numbers (8–24). NMF factor loadings
standard scanpy 1.7.1 workflow104. The cells with >4,000 counts in nuclei for cell types are reported in the paper as dot plot normalized per cell
and 20,000 counts in the cells were removed. In the cells, droplets with type by the sum of NMF loadings, which can be interpreted as a propor-
>10,000 features were removed. Lower threshold of 1,000 features tion of cells of each cell type present in each tissue zone. NMF factor
was applied to donor A37 due to difficulty to remove ambient RNA loadings across locations are reported as the total cell abundance of
contamination. Master cell types were annotated and extracted for constituent cell types.
reanalysis with scanpy workflow, including new highly variable genes
(HVGs) detection. Between 1,000 and 3,000 HVGs were used to define Postprocessing analysis. Gene set enrichment analysis was performed
40 principal components for calculating the UMAP. Data integration in GSEA online tool (https://www.gsea-msigdb.org/gsea/index.jsp)108
via Harmony v1.0 (ref. 105), BBKNN v1.4.1 (ref. 106) or scVI-tools v0.9.0 for specific gene sets and in gProfileR e106_eg53_p16_65fcd97 (https://
(ref. 107) was used with either ‘material’ (cells versus nuclei), or ‘material biit.cs.ut.ee/gprofiler/gost). The analysis of gene expression in GTEx tis-
and donor’. Doublet clusters, identified by observing markers from sues was performed in the GTEx portal (https://gtexportal.org/home/).
multiple cell types and higher counts in snRNA-seq, were removed. Cell–cell interaction analysis was performed with CellChat (http://www.
An iterative clustering approach was used to derive clusters for less cellchat.org/)77. To reduce donor-to-donor differences, the dataset was
abundant cell types. In addition to known marker genes, new ones were downsampled to a set number of cells per donor per cell type.
derived using the scanpy rank_genes_groups function. Cell types and The code used for marker gene dot plots with mean group expres-
master clusters were annotated according to known and newly derived sions and expression of TCR regions was previously published with
markers as in Supplementary Note 1 and in consensus with other studies code available at https://doi.org/10.5281/zenodo.3711134.
in Supplementary Table 4. The UMAP of the airway epithelial cell types Pseudotime analysis for selected cell populations was performed
was achieved by integrating the data with published human airway with Monocle3 (ref. 109), its functionality to infer a pseudotime based
epithelial cells9, including previously unannotated serous and mucous on UMAP coordinates. The root was identified as the cell with the
cells identified from the unprocessed data of their study. Altogether highest combined expression of canonical progenitor markers (VCAN
we detected all cell types from at least two different locations and five for chondrocytes; TGM2, HMCN2 and SULF1 for smooth muscle).
Nature Genetics

Article https://doi.org/10.1038/s41588-022-01243-4
Cell trajectory analysis was performed using the scVelo package for differentially expressed genes between PB-fibros in COPD, fibro-
(v0.2.1)110 and specifying the stochastic model. blast labels were transferred from the HLCA (which annotates PB-fibro
Label transfer was performed via Azimuth tool v0.4.1 (https://azi- based on our work) to Adams et al.8 dataset. Differential genes were
muth.hubmapconsortium.org/) with the lung reference data11 v1.0.0. identified by Wilcoxon rank-sum test (P < 0.05). PB-fibros were rare, 74
CellTypist56 v1.2.0 was used to train a logistic regression model from our in COPD and 20 in controls, but represented across 21 individuals (12
dataset for label transfer using the celltypist.train function (tag-value patients with COPD and 9 healthy controls). Genes displayed are a por-
pairs: use_SGD=True, feature_selection=True). HPA (https://www.pro- tion of the top-upregulated genes, which are implicated in Lung func-
teinatlas.org/humanproteome/tissue) was used for extracting images tion (FEV1/FVC). The abundance of PB-fibros in disease was assessed
of protein stainings with antibodies on human tissues. in the HLCA and Adams et al.8 datasets using PLMM as described above
and MiloPy, which tests differential abundances on the KNN graph115.
BCR and TCR analysis from VDJ-data. VDJ analysis was done with For PLMM analysis, covariates from the HLCA accounted for were
Scirpy 0.6.0 (https://icbi-lab.github.io/scirpy/)111. For TCR data, clono- ‘sample’, ‘study’, ‘subject ID’, ‘sex’, ‘ethnicity’, ‘smoking status’, ‘condi-
types were defined based on CDR3 nucleotide sequence identity. For tion’ (disease, manually harmonized), ‘subject type’, ‘sample type’,
BCR data, clonotypes were defined based on the Hamming distance ‘sequencing platform’, ‘cells or nuclei’ and ‘anatomical region detailed
between CDR3 amino acid sequences with a cutoff of two and orphan unharmonized’. MiloPy analysis was performed using the standard
VJ chains removed. In both cases, V gene identity was required and workflow, the KNN graph was generated from the latent space already
the CDR3 sequence similarity was evaluated across all of a cell pair’s available in the extended HLCA (X_scanvi_emb) and ‘study’ was used
V(D)J chains. as a covariate.
Statistics and reproducibility. Spearman rank correlation test (two COVID-19 data analysis. To assess the impact of infection on IgA
tailed) was performed for zonation analysis of the SMG serous cells abundance, we used a dataset71, with tracheal, bronchial and nasal epi-
across trachea, bronchi 2–3 and bronchi 4 locations for the three thelium brushings from children and adults. Although these samples
donors (A37, A41 and A42) with at least 20 cells in at least two loca- differed from the deep airway biopsies taken in this study, they still
tions. Correlation coefficients and P values were calculated per every contained some SMG epithelial cells and IgA plasma cells, showing a
donor separately. A Poisson linear mixed model was used for cell type level of compatibility with the healthy samples used in our study. A total
composition analysis. Poisson regression with various metadata as of 470 plasma cells from five donors (three healthy and two COVID+),
covariates was applied to adjust confounding effects on the cell type each with at least 20 plasma cells, were pooled, clustered and classified
count data as previously described112,113. We used location as a biologi- into IgA, IgD, IgH and IgM isotypes based on expression levels of IGHA1,
cal factor, and protocol, material (scRNA-seq versus snRNA-seq) and IGHA2, IGHD, IGHG1, IGHG2, IGHG3, IGHG4 and IGHM. Proportions were
donor as technical factors in the model as random effects to overcome calculated across cells for healthy and COVID+ donors separately.
the collinearity (see Supplementary Notes in ref. 113 for more details).
Gene set enrichment analysis was done with g:GOSt method and Cell–cell interaction analysis. Cell–cell interaction from scRNA-seq
g:SCS threshold with flat list in the gProfiler webpage https://biit.cs.ut. data was predicted using CellChat77. B plasma subsets were combined
ee/gprofiler/gost. GOSt uses Fisher’s one-tailed test, also known as (B-plasma) and cell types of interest (B-naive, B-memory, SMG duct,
cumulative hypergeometric probability. SMG mucous, SMG serous, CD4-naive/CD4-CM, CD4-EM/CD4-effector
Donors used for smFISH, IHC and Visium experiments are shown and CD4-TRM) were downsampled to 200 cells per cell type per donor.
in Supplementary Table 9, smFISH and Visium experiments were per- Analyses were performed both with individual CD4 T cell subsets and
formed once for each donor often across multiple sections, IHC stain- all CD4 subsets combined. Normalized count matrix along with cell
ing was repeated at least twice depending on the markers used. Full annotation metadata was processed through the standard CellChat
staining figures, reproducibility and antibodies for protein staining pipeline, except that the communication probability was calculated
from HPA can be queried online at https://www.proteinatlas.org/. with a truncated mean of 10%.
Variance in gene expression. To determine the effects of the metadata Reporting summary
features on the expression data, a linear mixed model was used39. Genes Further information on research design is available in the Nature Port-
expressed in less than 5% of the samples were filtered out. The count folio Reporting Summary linked to this article.
matrix was then normalized and log transformed. The percentages of
variance in gene expression data explained by each metadata feature Data availability
were obtained by fitting the linear mixed model. The Bayes factor All transcriptomic datasets generated as part of the study are publicly
was then computed to determine the gene-specific effects of some available. The processed scRNA-seq, snRNA-seq and Visium ST data are
metadata features in the expression data, assigning an effect size and available for browsing and download via our website www.lungcellatlas.
a local true sign rate (LTSR) for all genes analyzed. Genes presenting org. The dataset (raw data and metadata) is available on the Human Cell
an LTSR value greater than 0.9 were considered substantially affected Atlas Data Portal and on the European Nucleotide Archive (ENA) under
by the metadata feature analyzed. See Supplementary Notes in ref. 39 accession number PRJEB52292 and BioStudies accession S-SUBS17. The
for more details. Visium data are publicly available on ArrayExpress with the accession
number E-MTAB-11640. Imaging data can be downloaded from Euro-
fGWAS analysis. The fGWAS approach to determine disease-relevant pean Bioinformatics Institute (EBI) BioImage Archive under accession
cell types is described elsewhere18. Summary statistics for the selected number S-BIAD570. Additional data were accessed to support analysis
GWAS study of Lung function (FEV1/FVC)114 were obtained via Open and conclusions, which can be accessed through National Centre for
Targets Genetics (https://genetics.opentargets.io/study/GCST007431; Biotechnology Information Gene Expression Omnibus GSE136831, and
https://www.ebi.ac.uk/gwas/studies/GCST007431). The code used for GSE134174 and the HLCA integration, which can be accessed through
fGWAS plots and for cell type proportion analysis is available here: github https://github.com/LungCellAtlas/HLCA.
https://github.com/natsuhiko/PHM.
Code availability
HLCA, COPD and IPF data analysis. To assess PB-fibros in lung disease, The majority of the analysis was carried out using published and freely
we used both the HLCA extended10 and Adams et al.8 datasets. To look available software and code as stated in the Methods. Custom code
Nature Genetics

Article https://doi.org/10.1038/s41588-022-01243-4
was used for Extended Data Figs. 1c and 8f and are available at https:// Z/18/Z and Sanger core grant WT206194). E.M. is supported by ESPOD
github.com/elo073/5loclung/ (DOI: 10.5281/zenodo.7125810). fellowship of EMBL-EBI and Sanger Institute. A.J.O. was supported by
the European Respiratory Society and the European Union’s H2020
References research and innovation program under Marie Sklodowska-Curie grant
101. Krishnaswami, S. R. et al. Using single nuclei for RNA-seq to agreement number 847462. K.T.M. is supported by an award from the
capture the transcriptome of postmortem neurons. Nat. Protoc. Chan Zuckerberg Foundation. The project has received funding from
11, 499–524 (2016). the European Union’s Horizon 2020 research and innovation program
102. Radtke, A. J. et al. IBEX: a versatile multiplex optical imaging under grant agreement 874656. M.Z.N. acknowledges funding from
approach for deep phenotyping and spatial analysis of cells in an MRC Clinician Scientist Fellowship (MR/W00111X/1) and an MRC
complex tissues. Proc. Natl Acad. Sci. USA 117, 33455–33465 Rutherford Fellowship (MR/5005579/1). M.Z.N. and K.B.M. have been
(2020). funded by the Rosetrees Trust (M944) and Action Medical Research
103. Young, M. D. & Behjati, S. SoupX removes ambient RNA (GN2911). K.B.W. acknowledges funding from University College
contamination from droplet-based single-cell RNA sequencing London, Birkbeck MRC Doctoral Training Programme. This project
data. Gigascience 9, giaa151 (2020). has been made possible in part by grant 2019-202654 from the Chan
104. Wolf, F. A., Angerer, P. & Theis, F. J. SCANPY: large-scale single-cell Zuckerberg Foundation. This publication is part of the Human Cell
gene expression data analysis. Genome Biol. 19, 15 (2018). Atlas (www.humancellatlas.org/publications).
105. Korsunsky, I. et al. Fast, sensitive and accurate integration of
single-cell data with Harmony. Nat. Methods 16, 1289–1296 (2019). Author contributions
106. Polański, K. et al. BBKNN: fast batch alignment of single cell K.B.M., E.M. and A.J.O. conceived and designed the experiments;
transcriptomes. Bioinformatics 36, 964–965 (2020). E.M., A.J.O., K.P., A.R.O., J.P.P., C.X., R.E., N.H. and R.G.H.L. carried out
107. Lopez, R., Regier, J., Cole, M. B., Jordan, M. I. & Yosef, N. Deep computational analysis; V.K. performed and optimized cell2location
generative modeling for single-cell transcriptomics. Nat. Methods analysis; A.W-C. helped with experimental planning, sample
15, 1053–1058 (2018). management and spatial gene expression; L.M., L.B., A.K., E.P.,
108. Subramanian, A. et al. Gene set enrichment analysis: a A.H. and A.O. carried out tissue dissociation and sc and snRNA-seq
knowledge-based approach for interpreting genome-wide experiments; M.D., L.T., S.P. and S.F.V. performed Visium ST and M.P.
expression profiles. Proc. Natl Acad. Sci. USA 102, 15545–15550 supervised RNAScope analysis; S.P. provided histology support. L.S.C
(2005). provided pathology support. N.R., S.P. and A.J.O. carried out IHC and
109. Cao, J. et al. The single-cell transcriptional landscape of protein staining; K.M. and T.N. provided mouse tissue. P.H. and R.E.
mammalian organogenesis. Nature 566, 496–502 (2019). contributed to cell types annotation; K.M., N.G., K.S-P. provided human
110. Bergen, V., Lange, M., Peidli, S., Wolf, F. A. & Theis, F. J. tissue samples; N.K. carried out statistical analysis and M.Y., K.B.W.,
Generalizing RNA velocity to transient cell states through R.G.H.L. and M.Z.N. shared unpublished data. O.A.B., M.C., O.S., S.A.T.
dynamical modeling. Nat. Biotechnol. 38, 1408–1414 (2020). and K.B.M provided funding, discussion and supervision and E.M.,
111. Sturm, G. et al. Scirpy: a Scanpy extension for analyzing A.J.O., A.W-C., S.A.T. and K.B.M. wrote the manuscript.
single-cell T-cell receptor-sequencing data. Bioinformatics 36,
4817–4818 (2020). Competing interests
112. Stephenson, E. et al. Single-cell multi-omics analysis of the In the past three years, SAT has received remuneration for consulting
immune response in COVID-19. Nat. Med. 27, 904–916 (2021). and Scientific Advisory Board Membership from Genentech,
113. Elmentaite, R. et al. Single-cell sequencing of developing human Roche, Biogen, GlaxoSmithKline, Foresite Labs and Qiagen. SAT is a
gut reveals transcriptional links to childhood Crohn’s disease. cofounder, board member and holds equity in Transition Bio. OS is a
Dev. Cell 55, 771–783 (2020). paid member of the Scientific Advisory Board of Insitro. The remaining
114. Shrine, N. et al. New genetic signals for lung function highlight authors declare no competing interests.
pathways and chronic obstructive pulmonary disease
associations across multiple ancestries. Nat. Genet. 51, 1067 Additional information
(2019). Extended data is available for this paper at
115. Dann, E., Henderson, N. C., Teichmann, S. A., Morgan, M. D. & https://doi.org/10.1038/s41588-022-01243-4.
Marioni, J. C. Differential abundance testing on single-cell data
using k-nearest neighbor graphs. Nat. Biotechnol. 40, 245–253 Supplementary information The online version contains supplementary
(2022). material available at https://doi.org/10.1038/s41588-022-01243-4.
Acknowledgements Correspondence and requests for materials should be addressed to
We thank J. Eliasova for the graphical illustrations. L. Yang supported Sarah A. Teichmann or Kerstin B. Meyer.
with a draft for graphical illustrations in BioRender. C. Dominguez
Conde supported with a script for TCR clonotype sharing analysis. M. Peer review information Nature Genetics thanks Shalev Itzkovitz,
Prete’s and Cellgen IT’s computational support has been central to the Bethany Moore and David Schwartz for their contribution to the
analysis. J.E., L.Y., C.D.C, M.P. are affiliated with the Wellcome Sanger peer review of this work. Peer reviewer reports are available.
Institute. We are grateful to the organ donors, their families and the
Collaborative Biorepository for Translational Medicine for the gift of Reprints and permissions information is available at
human tissue. K.B.M. and S.A.T. are supported by Wellcome (WT211276/ www.nature.com/reprints.
Nature Genetics

Article https://doi.org/10.1038/s41588-022-01243-4
Extended Data Fig. 1 | See next page for caption.
Nature Genetics

Article https://doi.org/10.1038/s41588-022-01243-4
Extended Data Fig. 1 | Overview of human lung dataset across five locations. combined sc/snRNA-seq dataset, scRNA-seq and snRNA-seq datasets. The
(a) H&E sections of full depth human tissue samples from multiple regions whiskers correspond to 95% confidence intervals and the number of genes tested
showing all major structures of the lungs and airways. (b) Expression of cell was 8,666 in cells/nuclei combined, 7,977 in cells, 7,260 in nuclei. 129,340 cells
type marker genes in the master cell type groups, from both single cell and and 63,768 nuclei were analysed. (d) Protein staining of chondrocyte markers in
single nuclei RNA-seq combined. Color represents maximum normalised mean the cartilage of human bronchus from the HPA. (e) Proportion of mesenchyme
expression of marker genes in each cell group, and size indicates the proportion cell type groups in the airways from cells and nuclei. Numbers indicate
of cells expressing marker gene. Dashed box highlights chondrocyte marker chondrocytes in single cells versus single nuclei. (f) UMAP of sequencing material
genes. (c) Variance of gene expression explained by metadata variables in the (cells or nuclei) and location (trachea, bronchi, parenchyma).
Nature Genetics

Article https://doi.org/10.1038/s41588-022-01243-4
Extended Data Fig. 2 | See next page for caption.
Nature Genetics

Article https://doi.org/10.1038/s41588-022-01243-4
Extended Data Fig. 2 | Novel fibroblast subsets. (a) Dot plot of marker gene Small dots represent cells, circles represent mean values and bars show standard
expression for indicated cell types. (b) UMAP of location and sequencing deviation. (e) Dot plot showing the cell type cross-validation by transferring cell
material from fibroblasts. (c) Heatmap showing annotated cell types to the type labels from our single cell dataset (row) to cell types from Travaglini et al.
predicted labels for fibroblasts from Travaglini et al. (Travaglini et al. 2020) by 2020 (column). For each column (each cell type from the Travaglini et al. 2020),
the Azimuth tool, coloured by proportion. Labels by the proportion of annotated size of a dot denotes the proportion of cells assigned to a given cell type in our
cells and the total number of cells mapping to the reference. (d) Violin plots with dataset and colour denotes the average probability. Highlighting marks the
predicted annotation score for each of the annotated cell types to the reference. airway-enriched cell types.
Nature Genetics

Article https://doi.org/10.1038/s41588-022-01243-4
Extended Data Fig. 3 | Validation of immune recruiting fibroblasts and their mapping density scores with zoom into the region of interest, showing density
tissue localisation. (a) smFISH staining in human bronchi tissue for IR-Fibro values for IR-Fibro and relevant immune cells from the current lung study as well
markers (CCL21, CCL19) showing independent localisation from immune cells as for germinal centre cell types from a gut18. Dashed lines are added for better
(PTPRC) and smooth muscle cells (ACTA2) marked by arrows. (b) H&E staining visual comparison between the cell types and regions.
on Visium ST with manually annotated immune infiltrate in blue. cell2location
Nature Genetics

| Article                            |     |     |                                                                    |     |     |                             |     |     | https://doi.org/10.1038/s41588-022-01243-4 |                       |     |     |
| ---------------------------------- | --- | --- | ------------------------------------------------------------------ | --- | --- | --------------------------- | --- | --- | ------------------------------------------ | --------------------- | --- | --- |
| a Human protein atlas: COL15A1     |     |     | Human protein atlas: COL15A1                                       |     |     | Human protein atlas: ENTPD1 |     |     |                                            |                       |     |     |
| HPA017913, Bronchus Female, age 53 |     |     | HPA017915, Bronchus Female, age 53HPA014067, Bronchus Male, age 77 |     |     |                             |     |     |                                            |                       |     |     |
| 50 µm                              |     |     |                                                                    |     |     |                             |     |     | c                                          | PB-fibro DEGs in COPD |     |     |
50 µm
Peribronchial
fibroblasts
|     |     | Peribronchial  |     | Peribronchial  |     |     |     |     | 50 µm |     |     |     |
| --- | --- | -------------- | --- | -------------- | --- | --- | --- | --- | ----- | --- | --- | --- |
|     |     | fibroblasts    |     | fibroblasts    |     |     |     |     |       |     |     |     |
b
|     |           |                          |                                       | TMEM132C       |                |              |                 |     | Adams et al. 2020 |     |             |      |
| --- | --------- | ------------------------ | ------------------------------------- | -------------- | -------------- | ------------ | --------------- | --- | ----------------- | --- | ----------- | ---- |
|     | PCDH11X   |                          | SCARA3 COL12A1                        | ENTPD1 COL13A1 | COL15A1 CCDC68 |              |                 | d   |                   |     |             |      |
|     | GRID2     | ZFHX4 CHI3L1 MFGE8 RUNX2 | TMTC1 FGFR2 F13A1 CORIN LHFPL3 PLPPR4 | COL7A1         | TAGLN MYH11    | ACTA2 COL1A1 | Mean expression |     |                   |     |             |      |
|     | LGR4 LGR6 |                          | KDR WIF1                              |                | LGR5 CNN1      | ASPN         | in group        |     |                   |     | Fold change | LTSR |
0.0 Max
|               |     |     |     |     |     |     |                    |     |     |     | >3   | >0.9999 |
| ------------- | --- | --- | --- | --- | --- | --- | ------------------ | --- | --- | --- | ---- | ------- |
| Myofibroblast |     |     |     |     |     |     |                    |     |     |     |      | 0.999   |
| Fibro-adv     |     |     |     |     |     |     |                    |     |     |     | 0    |         |
| Fibro-alv     |     |     |     |     |     |     | Cells detected (%) |     |     |     |      | 0.99    |
|               |     |     |     |     |     |     |                    |     |     |     | <1/3 | 0.9     |
PB-fibro
| PC-fibro |                   |     |     |                                |     |     | 10 20 30 | 40 50 60 |     |     |     | 0.5 |
| -------- | ----------------- | --- | --- | ------------------------------ | --- | --- | -------- | -------- | --- | --- | --- | --- |
| e        | HLCA fibroblasts  |     | f   | Human protein atlas: COL12A1,  |     |     |          |          |     |     |     |     |
HPA009143, bronchus
(all datasets)
HLCA
(without Adams et al. 2020)
50 µm
Adventitial fibroblasts
Alveolar fibroblasts
Peribronchial fibroblasts
Pericytes
| 2PAMU |     |     | Subpleural fibroblasts |     |     |     |     |     |     |     |     |     |
| ----- | --- | --- | ---------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
UMAP1
Neighbourhood
|     | enrichment  | IPF enriched |     |     |     |     |     |     |     |     |     |     |
| --- | ----------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
3
Perichondrium
2
1
0
Cartilage
(detached)
|       |     |     | -1  |     |     |     |     |     | emitoduesP      |                |            |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --------------- | -------------- | ---------- | --- |
|       |     |     |     |     |     |     |     | h   | Genes with      | Markers for    |            |     |
|       |     |     |     |     |     |     |     |     | epyt lleC       | perichondrial  | Cartilage  |     |
| 2PAMU |     |     | -2  |     |     |     |     |     | bone/cartilage  |                | genes      |     |
|       |     |     |     |     |     |     |     |     | phenotype       | fibroblasts    |            |     |
g
| UMAP1 |     | Healthy e-3nriched |     |     |     |     |     |     |     |     |     |     |
| ----- | --- | ------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Enrichment per cell type
etycordnohC emitoduesP
logFC
|     |     | -4 -3 -2 -1 |     |     | tsalborbiF |     |     |     |     |     |     |     |
| --- | --- | ----------- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
0 1 2 3 4
| Adventitial fibroblasts |     |     |     |     | Chondrocyte  |     |     |     |     |     |     |     |
| ----------------------- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- |
differentiation
Alveolar fibroblasts
Mixed
Peribronchial
fibroblasts
|                        | Pericytes |     |     |       |               |             |     |     |                                               |                                                               |                                                                     | srpxE |
| ---------------------- | --------- | --- | --- | ----- | ------------- | ----------- | --- | --- | --------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------------- | ----- |
|                        |           |     |     |       | Adventitial   | Chondrocyte |     |     |                                               |                                                               |                                                                     |       |
| Subpleural fibroblasts |           |     |     | 1PAMU | fibroblast    |             |     |     |                                               |                                                               |                                                                     |       |
|                        |           |     |     |       | Perichondrial |             |     |     | 2CTAFN 1A04CLS 1A21LOC 1AYE 1FPIW 1BRADA BNLF | 4TAF 6A6LOC ULC 2RFGF 8EGFM 1L3IHC 3ARACS 4XHFZ 2DIRG X11HDCP | 2XNUR CYPE 1NTAM 3NTAM 9XOS 1NLPAH 1LTYC 3A9LOC 1A2LOC 1A9LOC  NACA |       |
fibroblast
UMAP2
i Enrichment of perichondrial fibroblast marker genes in skeletal abnormalities in humans
|     |     |     |     | 82FEGHRA | 1A061MAF |     |     |     |     | APB24CDC |     |     |
| --- | --- | --- | --- | -------- | -------- | --- | --- | --- | --- | -------- | --- | --- |
MOCEM 1A11LOC B4DMRF 8DMAPC 5DNAFZ 3ARGDA BC1PPP 1I1CNYD 1A8LOC 82DRKNA 3D22CST 1AMNCK 11A93CLS 1A72LOC PID4EDP 2DILERP 1BRADA 2DSHCF Y11HDCP X11HDCP 3BRGDA 7121AAIK BHDKCB 3ARACS 24OXBF 1DLPSIRC 1BANCK 1A21LOC 86CDCC 1A04CLS 3BTBOHT 2ENURP
Human Phenotype ontology 01AGTI B4PPNI D1OYM 2RFGF 1PPNE 2BBPA 5PBKF 8EGFM 11HDC 3MNET 2MAIT 5PMB SDMG 1L3IHC 1CNAT DRPTP 4TDUN 61RRP 3NSES 6CPG 3XHFZ 4DSHT 3SAPN REPMB C1EDP 2PWW 6PPM 41KDC 1HCMIL NACA 3LIDE 1CTMT HKNA 2YCDA 2XNUR 2DIRG 71XDD 4TIDD 1STUM 9CADH 3OXOF 1FPIW ACAU 1OBOR MLACIP 2KPAD PRAPIT 3LNMF PINXT R1HTP
Term name Term ID 6XOS ULC CNT XOT 2LLE 1PIH NZAK BNLF 4TAF GRE MIV 1AYE 1NF
M i x e d   h e a r in g  i m p airment
| S k e l e t a l   d y                      | s p l a s ia   | H P : 0 0 0 0 4 | 1 0 |     |     |     |     |     |     |     |     |     |
| ------------------------------------------ | -------------- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| M i c r o m e l i a                        |                | H P : 0 0 0 2 6 | 5 2 |     |     |     |     |     |     |     |     |     |
| M a l a r   f a t t e                      | n i n g        | H P : 0 0 0 2 9 | 8 3 |     |     |     |     |     |     |     |     |     |
| Abnormality of malar bones                 |                | H P : 0 0 0 0 2 | 7 2 |     |     |     |     |     |     |     |     |     |
| Abnormal joint morphology                  |                | HP:0012369      |     |     |     |     |     |     |     |     |     |     |
| Abnormal sacrum morphology                 |                | HP:0001367      |     |     |     |     |     |     |     |     |     |     |
| Abnormality of pelv. bone morph.HP:0002644 |                | HP:0005107      |     |     |     |     |     |     |     |     |     |     |
| Narrow pelvis bone                         |                | HP:0003275      |     |     |     |     |     |     |     |     |     |     |
Abnormality of fibula morphology HP:0002991
| Edema  |     | HP:0000969 |     |     |     |     |     |     |     |     |     |     |
| ------ | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Abnormality of the zygomatic bonHeP :0010668
| Abnormality of cranial sutures  |     | HP:0011329 |     |     |     |     |     |     |     |     |     |     |
| ------------------------------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Aplasia/hypoplasia of the fibula HP:0006492
| Flat face |     | HP:0012368 |     |     |     |     |     |     |     |     |     |     |
| --------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Extended Data Fig. 4 | See next page for caption.
Nature Genetics

Article https://doi.org/10.1038/s41588-022-01243-4
Extended Data Fig. 4 | Peribronchial and perichondrial fibroblasts. (a) Protein in the extended HLCA (minus Adams et al. 2020). (e) Milo cell type abundance
staining of PB-Fibro markers (COL15A and ENTPD1) in human bronchus sections analysis of fibroblasts from the HLCA comparing IPF patients and healthy
from the HPA. (b) Marker genes for PB-fibro and PC-fibro. (c) Upregulated genes controls. UMAP of fibroblast clusters, neighbourhood enrichment UMAP
in COPD patient’s PB-fibro cells (74 cells, 12 donors) compared to controls (20 showing log fold change in IPF compared to healthy, and violin plot of log fold
cells, 9 donors) from scRNAseq data98. Selected upregulated genes associated change of the neighbourhood for each cell, grouped by cell type. Dashed line
with COPD or emphysema by GWAS (RGCC, DGKH, NTM, SULF1, NPC2, RPL5, highlights the region of PB fibros on the UMAPs. (f) Protein staining of PC-Fibro
LMCD1, MRTFA, DENND5A, KLF4) or in other studies (NFATC2, MT2A and marker (COL12A1) in human bronchus from the HPA mapping to cartilage. (g)
SIK2). Wilcoxon rank sum test p < 0.05 (two sided), exact P values and full list UMAP of adventitial fibroblasts, PC-fibro and chondrocytes from single nuclei
is in Supplementary Table 10. (d) Cell type proportion analysis using PLMM to data coloured by monocle 3 pseudotime and cell type. (h) Expression of genes
compare fibroblasts in the extended HLCA across disease conditions with fold associated with bone/cartilage function, markers of PC-fibro and cartilage genes
changes and Local True Sign Rate (LTSR). Covariates are listed in the methods. in the nuclei as shown on (g), ordered by pseudotime. (i) PC-fibro marker gene
Cell abundances were analysed in Adams et al. 2020 dataset only, and validated enrichment in Human Phenotype Ontology by g:Profiler.
Nature Genetics

Article https://doi.org/10.1038/s41588-022-01243-4
Extended Data Fig. 5 | See next page for caption.
Nature Genetics

Article https://doi.org/10.1038/s41588-022-01243-4
Extended Data Fig. 5 | Schwann cells and nerve-associated fibroblasts (NAF). nmSchwann cells. (e) Expression in Transcript per million (TPM) of NAF markers
(a) Marker dot plot for myelinating, non-myelinating Schwann cells and for epi- in GTEx bulk RNA-seq data. (f) Visium ST H&E staining of human bronchi, with
and endoneurial NAF-s. (b, c) g:Profiler gene set enrichment results using g:GOSt zoom in on nerve bundle and cell2location cell type mapping density scores for
method and g:SCS threshold and multiple testig correction with flat list as input Schwann and NAF cell types. (g-i) HPA antibody staining of (g) non-myelinating
for myelinating Schwann cell markers with detailed results for myelination and Schwann cell markers (CADM, GRIK2, NCAM1, ITGB4 and L1CAM) (h) endoneurial
transcription factor EVX1 (b) and for non-myelinating Schwann cell markers NAF marker (USP54) and (i) perineurial NAF markers (SLC22A3 and SORBS1)
(c). (d) Expression of neuropathy associated genes in Schwann and NAF cell within the nerve bundles in human bronchus. Arrows indicate nerve bundles. (j)
types. Previously unknown cell type specific expression shown in colour: light RNAscope staining for myelinating (MLIP) and non-myelinating (SCN7A, SOX10)
green for novel expression pattern, light blue for distinguishing expression for Schwann cell and perineurial (SLC2A1) NAF specific genes in bronchial nerves.
Nature Genetics

Article https://doi.org/10.1038/s41588-022-01243-4
Extended Data Fig. 6 | See next page for caption.
Nature Genetics

Article https://doi.org/10.1038/s41588-022-01243-4
Extended Data Fig. 6 | Vascular and smooth muscle cell types. (a) Markers by a thick smooth muscle layer. The orange rectangle shows muscular tissues
dot plot for vascular endothelia. (b) cell2location density scores of pulmonary from oesophagus, and the blue rectangle shows the non-muscular mucous layer
and vascular endothelium for parenchyma and bronchi Visium ST sections. (c) of oesophagus tissue. (f) IR-Ven-peri markers localise at the venous vessels in
Bronchi section with H&E and cell2location analysis density score for airway the airway. smFISH staining for IR-Ven-peri (CCL21, CCL19), venous endothelia
smooth muscle population on a Visium ST slide. (d) NPR2 staining in oesophagus (ACKR1) and smooth muscle (ACTA2) markers. (g) Leukocyte rolling and homing
and bronchus from the HPA. Black arrows indicate the airway and oesophagus genes, and chemokines expressed in Endothelia and SM/Perivascular cells
surrounding non-vascular smooth muscle. (e) ASM marker expression in together with their interaction partners expression in immune cell groups.
all GTEx tissues. Tissues are ordered by unsupervised clustering based on Interaction partners are indicated with blue shades.
expression similarity. The dotted line highlights tissues which are surrounded
Nature Genetics

Article https://doi.org/10.1038/s41588-022-01243-4
Extended Data Fig. 7 | See next page for caption.
Nature Genetics

Article https://doi.org/10.1038/s41588-022-01243-4
Extended Data Fig. 7 | Epithelial cell annotations and location specific expression dot plot. (i) smFISH staining for muscle (TAGLN), basal epithelia
ciliated cell gene expression. (a) Marker gene expression dot plot for airway (KRT14), duct (ALDH1A3) and myoepithelium (FHOD3) in human bronchi
epithelial cells. (b) UMAP of airway epithelial cells from scRNA-seq data. (c) sections. (j) HPA staining for muscle and epithelial marker proteins in human
Cell type proportion analysis with fold changes and Local True Sign Rate (LTSR) bronchial glands. (k) Unsupervised non-negative matrix factorisation (NMF)
score for all cell type groups with regards to variables shown. Cell numbers are in analysis of Visium ST cell2location results for 11 factors showing NMF factor
Supplementary Table 7. (d) smFISH staining for mucous (MUC5B), serous (LPO) loadings normalised per cell type (dot size and colour). Other factors/cell
and duct (MIA) cell markers in human bronchi sections. (e) smFISH staining of types are shown in Supplementary Fig. 4. (l) Violin plots of normalised log-
secretory goblet/club (SCGB1A1), ciliated (FOXJ1) and duct (ALDH1A3/RARRES1) transformed expression separated by location in the single nuclei RNA-seq data
in human bronchus section. (f) Visium ST H&E from bronchial section and for 3 genes upregulated (methods) in nasopharyngeal carcinoma gene set from
cell2location density values for mapping duct, mucous, serous, ciliated and GSEA database with LTSR>0.9 consistently higher expressed in the trachea. (m)
myoepithelial cells. (g) RNA velocity results on UMAP from scRNAseq of airway SARS-CoV-2 receptor and viral entry gene (ACE2) expression in ciliated cells from
epithelia. Colours indicate cell types as in (b). (h) Myoepithelial marker gene snRNA-seq data shown by location in a violin plot.
Nature Genetics

Article https://doi.org/10.1038/s41588-022-01243-4
Extended Data Fig. 8 | See next page for caption.
Nature Genetics

Article https://doi.org/10.1038/s41588-022-01243-4
Extended Data Fig. 8 | Immune cell type groups. (a) Marker gene expression of location, donor, material and protocol on immune cell type proportions
plot along with UMAP for Megakaryocytes and Mast cells. (b) Marker genes dot (assessed by PLMM) are shown by forest plots. Each square dot with an error
plot for Myeloid cells. (c) Marker genes dot plot for T & NK cells. (d) cell2location bar shows the square root of variance explained by each factor and its 95%
density scores for CD8-TRM, Ciliated and CD8-EM cell types in human bronchi confidence interval, respectively. Dotplots show point estimates of fold changes
sections and corresponding H&E. (e) Fraction of clonally expanded cells in T & and Local True Sign Rate (LTSR) for myeloid cell types (g), T & NK cell types (h)
NKT cell types from VDJ data. (f) Proportion of shared TCR clonotypes between and B lineage cell types (i). The number of cells in each cell type group are in
samples from VDJ data. Colour bars indicate location and donor. (g-i) Effects Supplementary Table 7.
Nature Genetics

Article https://doi.org/10.1038/s41588-022-01243-4
Extended Data Fig. 9 | See next page for caption.
Nature Genetics

Article https://doi.org/10.1038/s41588-022-01243-4
Extended Data Fig. 9 | Additional data on B lineage and IgA plasma cell example of FFPE Visium slide region with mucous and non-mucous glands
localisation. (a) Marker gene expression dot plot for B-lineage cells. (b) Gene annotated per voxel, and enrichment of cell types by cell2location in the micro-
expression dot plot for top differentially expressed genes between IgA and anatomical tissue environments across 2 FFPE sections (trachea and bronchi
IgG plasma cells. (c) Number of B lineage cells with different Ig isotypes in 2-3) from 1 donor. (h) Multiplex IHC of human trachea for Ig isotypes (IgA, IgG,
parenchyma from the analysis of VDJ amplified libraries. (d, e) HPA staining for IgD) showing distinction between glands (dashed lines) and non-gland regions
B plasma marker MZB1 in the bronchus.(d) and nasopharyngeal glands.(e). (f) of tissue. (i) IgA staining in mouse colon and trachea from wild type C57/BL6
Spatial localisation of selected NMF factors (total N=11, Figure 4f, Supplementary mice from Charles River, USA or Kindai University, Japan (where specified).
Fig. 4) from unsupervised NMF analysis of Visium ST cell2location results. The Representative staining from 2 experiments, 3 sections per experiment. AF =
total cell abundance of constituent cell types for factors 3 and 6 are shown on a autofluorescence (shown in red). Arrows showing clusters of IgA plasma cells at
bronchi section, with H&E and manual gland annotations shown for reference. the epithelial surface in tracheal sections.
White dashed lines highlight mucous/duct (factor 6) specific areas. (g) An
Nature Genetics

Article https://doi.org/10.1038/s41588-022-01243-4
Extended Data Fig. 10 | See next page for caption.
Nature Genetics

Article https://doi.org/10.1038/s41588-022-01243-4
Extended Data Fig. 10 | Additional gland associated immune niche data - of AICDA in B cell subsets. (g) IHC from the HPA showing HLA-DR, MUC5B and
interactions of gland epithelial cells with immune cells. (a) Expression dot PRR4 staining with HLA-DR+ regions corresponding with non-mucous areas
plot of genes relevant for Figure 5h. (b) Co-staining of CCL28 RNA/protein and of gland. Red/purple dashed lines indicate mucous/serous cells respectively
IgA2 protein in airway submucosal glands, left: smFISH; right: IHC for CCL28. based on morphology and/or marker gene expression. (h) smFISH (MUC5B) plus
(c) Expression of TNFSF13, IL-6 and CCL28 in SMG-Serous and Duct cell sc/ IHC (HLA-DR) staining in human airway SMG. (i) IHC staining of CD4, CD45RO
snRNAseq data along the tracheobronchial tree. Change in CCL28 in serous (memory marker), CD45RA (naive marker), IgA2 and EpCAM in the SMG. Blue
cells was statistically significant with two-sided Spearman’s rank correlation arrows indicate CD4+CD45RA+ cells. (j) IHC staining of HLA-DR, EpCAM, CD3,
(methods) (p-values 1.6 × 10-8, 0.0034 and 1.3 × 10-5 for donors A37, A41 and A42 CD31 and CD4 in the airway SMG. Arrows point to CD3+CD4+ cells. (k) IHC
correspondingly). (d) smFISH on the human trachea with DAPI, TNFSF13/APRIL, staining of CD4, CD45RO, HLA-DR and EpCAM in the airway SMG showing close
RARRES1 and LPO. Dashed lines show regions of duct, mucous and serous glands. interactions between CD4+CD45RO+ T cells with HLA-DR+ glands. Arrows point
(e) smFISH (TNFSF13/APRIL, and CD79A) and IHC (IgA2) of human tracheal SMG to CD4+CD45RO+ cells.
showing APRIL+ and APRIL- glands annotated. (f) Violin plot for expression
Nature Genetics