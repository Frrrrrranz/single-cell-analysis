Article
A molecular cell atlas of the human lung
from single-cell RNA sequencing
https://doi.org/10.1038/s41586-020-2922-4 Kyle J. Travaglini1,2,16, Ahmad N. Nabhan1,2,12,16, Lolita Penland3,13, Rahul Sinha4,5, Astrid Gillich1,2,
Rene V. Sit3, Stephen Chang1,2, Stephanie D. Conley4,5, Yasuo Mori4,5,14, Jun Seita4,5,15,
Received: 24 August 2019
Gerald J. Berry5, Joseph B. Shrager6, Ross J. Metzger2,7, Christin S. Kuo8, Norma Neff3,
Accepted: 26 August 2020 Irving L. Weissman4,5,9,10, Stephen R. Quake3,11 ✉ & Mark A. Krasnow1,2 ✉
Published online: 18 November 2020
Check for updates Although single-cell RNA sequencing studies have begun to provide compendia of cell
expression profiles1–9, it has been difficult to systematically identify and localize all
molecular cell types in individual organs to create a full molecular cell atlas. Here,
using droplet- and plate-based single-cell RNA sequencing of approximately 75,000
human cells across all lung tissue compartments and circulating blood, combined
with a multi-pronged cell annotation approach, we create an extensive cell atlas of the
human lung. We define the gene expression profiles and anatomical locations of 58
cell populations in the human lung, including 41 out of 45 previously known cell types
and 14 previously unknown ones. This comprehensive molecular atlas identifies the
biochemical functions of lung cells and the transcription factors and markers for
making and monitoring them; defines the cell targets of circulating hormones and
predicts local signalling interactions and immune cell homing; and identifies cell
types that are directly affected by lung disease genes and respiratory viruses. By
comparing human and mouse data, we identified 17 molecular cell types that have
been gained or lost during lung evolution and others with substantially altered
expression profiles, revealing extensive plasticity of cell types and cell-type-specific
gene expression during organ evolution including expression switches between cell
types. This atlas provides the molecular foundation for investigating how lung cell
identities, functions and interactions are achieved in development and tissue
engineering and altered in disease and evolution.
Since Malpighi10, dozens of lung cell types have been discovered by along with peripheral blood (Extended Data Fig. 1a, d). Lung samples
microscopy11, creating histological atlases that are the cellular foun- were dissociated into cell suspensions, and each suspension was sorted
dation for pulmonary medicine. More recently, cell-type-specific into epithelial (EPCAM+), endothelial/immune (CD31+CD45+) and stro-
markers12,13 have been identified that provide molecular definitions mal (EPCAM−CD31−CD45−) populations (Supplementary Fig. 1a). This
and functions of the cell types14, reaching its apex in genome-wide allowed us to balance tissue compartment representation for sequenc-
expression profiling by single-cell RNA sequencing (scRNA-seq)15–19. We ing. We also sorted blood cells to balance immune lineages (Supplemen-
sought to create a comprehensive molecular cell atlas of adult human tary Fig. 1b). Sequencing libraries were prepared using 10x Chromium
lung using scRNA-seq analysis, a substantial challenge because the 45 (10x) or SmartSeq2 (SS2)20. Higher throughput of 10x enabled discovery
histological cell types have diverse structures, locations, and abun- of rare cell types, whereas SS2 gave deeper transcriptomic information;
dances that vary over five orders of magnitude (Supplementary Table 1). there were also platform-specific idiosyncrasies in cell capture. We
sequenced thousands of cells from each compartment for each subject
(Supplementary Table 2) to directly compare cell types without batch
Fifty-eight molecular cell types of the human lung
correction, and did so for three subjects to address individual differ-
We acquired histologically normal lung tissue intraoperatively from ences. High-quality transcriptomes were obtained from approximately
bronchi (proximal), bronchiole (medial), and alveolar (distal) regions 75,000 cells (65,662 10x; 9,404 SS2).
1Department of Biochemistry, Howard Hughes Medical Institute, Stanford University School of Medicine, Stanford, CA, USA. 2Vera Moulton Wall Center for Pulmonary Vascular Disease,
Stanford University School of Medicine, Stanford, CA, USA. 3Chan Zuckerberg Biohub, San Francisco, CA, USA. 4Institute for Stem Cell Biology and Regenerative Medicine, Stanford University
School of Medicine, Stanford, CA, USA. 5Department of Pathology, Stanford University School of Medicine, Stanford, CA, USA. 6Department of Cardiothoracic Surgery, Stanford University
School of Medicine, Stanford, CA, USA. 7Department of Pediatrics, Division of Cardiology, Stanford University School of Medicine, Stanford, CA, USA. 8Department of Pediatrics, Pulmonary
Medicine, Stanford University School of Medicine, Stanford, CA, USA. 9Ludwig Center for Cancer Stem Cell Research and Medicine, Stanford University School of Medicine, Stanford, CA, USA.
10Stanford Cancer Institute, Stanford University School of Medicine, Stanford, CA, USA. 11Department of Bioengineering, Stanford University, Stanford, CA, USA. 12Present address: Genentech,
South San Francisco, CA, USA. 13Present address: Calico Life Sciences, South San Francisco, CA, USA. 14Present address: Department of Medicine and Biosystemic Science, Kyushu University
Graduate School of Medical Science, Fukuoka, Japan. 15Present address: Medical Sciences Innovation Hub Program, RIKEN, Tokyo, Japan. 16These authors contributed equally: Kyle J. Travaglini,
Ahmad N. Nabhan. ✉e-mail: steve@czbiohub.org; krasnow@stanford.edu
Nature | Vol 587 | 26 November 2020 | 619

Article
a Epithelial Endothelial
Airway Alveoli 16 17 18 19 20 21 22 23 24 33
Art VeinCap-aCapCap-i1Cap-i2Bro1Bro2Lym Meso
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 1,5761,1974,9748,263 716 464 561 235 511 29
Club CilCil-pxBasBas-pxBas-dBas-pGobMuc Ser Ion NE AT1 AT2AT2-s
1,8291,872 88 676 157 308 47 392 491 24 24 66 1,3934,574 870
b Proximal airway Distal airway Alveoli Airway cross-section
2 8 3 1 12 1 12 2 11 8 8 2 1 4,5 8 6 2 1
18
4,5,6,7 4 32 25,28
25,28 25,28 32 27 19 32 22,23
32 22,23 22,23 50,51 14,15 31 16
29 9 11 29 47 29
26 26 13 24 26
10 16 16 30
17
4445
c AT2 and AT2-s AT2-s
AT2 markers AT2 AT2-s Gen AT2 AT2-s S F T P B S F T P D S F T P C P G C H HI P WI F 1 C A 2 N N M T C P T C F 7 L 2 W N T 5 A L R P 5
SFTPC AT2
AT2-s
0 8 16 ln(CPM + 1)
We grouped cells based on the expression of compartment-specific Immune cells were the most heterogeneous and included circulat-
markers (Extended Data Fig. 1b), then iteratively clustered21 them for ing, egressed and lung-resident cells. To aid identity assignment, we
each subject to identify transcriptionally distinct cell populations. defined transcriptional profiles of circulating immune cells by bulk
Populations between subjects were merged using cluster-specific RNA sequencing of 21 sorted, functionally characterized classes of
marker genes for downstream analyses. Our approach identified human blood cells (Extended Data Fig. 2a, Supplementary Table 3).
58 transcriptionally distinct cell populations (mean 51 per subject) We also obtained scRNA-seq profiles of around 5,000 blood cells from
(Extended Data Fig. 1c, Supplementary Table 2), 37 more than a recent two patients whose lung cells we analysed. Canonical immune mark-
state-of-the-art study19. ers and the ascertained panels of differentially expressed genes were
used to assign the identities to 25 immune clusters from our lung and
blood scRNA-seq analysis, including all but one previously known lung
Transcriptomes of canonical cell types
immune cell type (Fig. 2a, Extended Data Fig. 2b).
The 58 molecular types included 15 epithelial, 9 endothelial, 9 stro- Our approach defined genome-wide expression profiles for nearly
mal and 25 immune populations, greater than the number of classi- all classical lung cell types (41 out of 45, 91%), from the most abun-
cal cell types in each compartment (Supplementary Table 2). Using dant (capillaries, approximately 23% of lung cells) to exceedingly rare
extant and newly identified (bronchial vessel) markers (Supplemen- (ionocytes, 0.01%) (Supplementary Table 1). One-quarter (11 out of
tary Table 1) and single-molecule fluorescence in situ hybridiza- 45) previously lacked high-quality single-cell transcriptomes. The
tion (smFISH), we found clusters that represent all but one classical only classical types not captured are extremely rare (neurons, glia),
lung cell type in epithelial, endothelial and stromal compartments primarily found in disease (tuft cells)22, or require special isolation
(Fig. 1a, b). methods (eosinophils).
620 | Nature | Vol 587 | 26 November 2020
)%(
sllec
+CTPFS
e Gen AlvF AdvF LipF MyoF/FibM/ASM AlvF AdvF AlvF Peri
d 203 100 508 387 100 FB markers 75 75 50
50 25
AT2-s WIF1 0
DAPI
2
0
5
ln(UP10K + 1) 0 3 6 Alv
e
ol
x
i
.
v as c
ul
ar
o
Pr
)%( sllec+2A1LOC
Stromal
Muscle 27 28 29 30 31 32
MyoFFibMAdvFAlvF LipF Peri
25 26 300 113 715 1,656 55 2,126
ASMVSM
1,039 645
LipF AdvF
Alveoli C O L 1 A 2 B S G T A G L N A C T A 2 G P C 3 S PI N T 2 F G F R 4 S E R PI N S F F 1 R P 2 PI 1 6 A P O E F S T P LI N 2 A S P N WI F 1 F G F 1 8 S C X L G R 6 M Y H 1 1 C N N 1 A C T G 2 C O X 4I 2 R E R G L K C N A 5 f Alveoli Artery AlvF
AdvF
LipF
MyoF
FibM
ASM
COL1A2 COL1A2 GPC3 SERPINF1 ECM ECM
Fig. 1 | Identities and locations of lung epithelial, endothelial, and stromal reads. d, smFISH and quantification (n = 203 cells scored, staining repeated in
cell types. a, Human lung molecular cell types identified after iterative two different participants from those profiled) for shared AT2 and
clustering (each level of hierarchy is an iteration) of scRNA-seq profiles of cells AT2-signalling marker SFTPC (white) and specific AT2 marker WIF1 (red puncta).
in indicated tissue compartments. Black, canonical types; blue, proliferating or Scale bar, 10 μm. AT2-signalling cells (SFTPC+ WIF1−; box, enlarged at right,
differentiating subpopulations; red, novel populations. Number of cells shown yellow arrowhead) are intermingled among AT2 cells (SFTPC+ WIF1+, white
below cluster name. AdvF, adventitial fibroblast; AlvF, alveolar fibroblast; Art, arrowheads). e, Dot plot of stromal markers (10x dataset). FB, fibroblast.
artery; ASM, airway smooth muscle; AT2-s, AT2-signalling; Bas, basal; Bas-d, f, smFISH and quantification for general fibroblast marker COL1A2 (white),
differentiating basal; Bas-p, proliferating basal; Bas-px, proximal basal; Bro1, alveolar fibroblast marker GPC3 (red, left) and adventitial fibroblast marker
bronchial vessel 1 cell; Bro2, bronchial vessel 2 cell; Cap, general capillary cell; SERPINF1 (red, right). Blue, DAPI; green, extracellular matrix (ECM;
Cap-a, capillary aerocyte; Cap-i1, capillary intermediate 1 cell; Cap-i2, capillary autofluorescence); prox., proximal. Adventitial fibroblasts (arrowheads, right)
intermediate 2 cell; Cil, ciliated; Cil-px, proximal ciliated; FibM, fibromyocyte; localize around vessels (ECM). Graph shows quantification of stromal cell type
Gob, goblet; Ion, ionocytes; LipF, lipofibroblast; Lym, lymphatic; Meso, in alveolar and proximal vascular regions (n denotes number of cells scored in
mesothelial; MyoF, myofibroblast; Muc, mucous; NE, neuroendocrine; Peri, each region; staining repeated in two different participants from those
pericyte; Ser, serous; VSM, vascular smooth muscle. b, Diagrams showing profiled). Pericyte and lipofibroblast marker staining in Extended Data Fig. 4h,
localization and morphology of each type (cell type numbering or names in a i. Scale bars, 10 μm. For more details on statistics and reproducibility,
and Fig. 2a). c, Dot plot of AT2 marker expression (10x dataset). UP10K, unique see Methods.
molecular identifiers (UMIs) per 10,000. CPM, counts per million mapped

| a   |          |     | Lymphocytes |        |     | Granulocytes | Platelets |         |       |     | Myeloid       |     |     |
| --- | -------- | --- | ----------- | ------ | --- | ------------ | --------- | ------- | ----- | --- | ------------- | --- | --- |
|     | 34       | 35  |             | (NK/T) |     | 43           | 44 45 46  | 47      | 48 49 |     | (DC/Monocyte) |     |     |
|     | B Plasma |     |             |        |     | Neu Mast     | Mast Mega | MP MP-p | pDC   |     |               |     |     |
|     |          |     |             |        |     | Ba 1         | Ba 2      |         |       |     |               |     |     |
854 189 (CD8) 38 39 40 41 42 113 1,396 552 40 14,766 226 150 (DC) (Monocyte)
|     |     |     |     | CD4 CD4 NKT | NK NK/T-p |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ----------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
M/E Na
|     |     | 36    | 37    | 3,139 1,063 387 6,001 | 122 |     |     |     | 50       | 51              | 52 53   | 54 55 56      | 57 58     |
| --- | --- | ----- | ----- | --------------------- | --- | --- | --- | --- | -------- | --------------- | ------- | ------------- | --------- |
|     |     | CD8   | CD8   |                       |     |     |     |     | mDC1mDC2 |                 | DC DC   | DC Mono Mono  | Mono Mono |
|     |     | M/E   | Na    |                       |     |     |     |     |          | IGSF21EREGTREM2 |         | Cl. OLR1      | NC Int.   |
|     |     | 1,249 | 2,420 |                       |     |     |     |     | 141      | 273             | 288 142 | 159 2,183 207 | 831 194   |
)%( ecnadnubA 100
80
60
40
20
0
IV Egr Egr Egr Egr Egr Hom Egr Egr Egr Hom Hom IV Res Res Egr Hom Egr Hom Hom Hom Egr Hom Egr Hom
Blood
Lung (cid:54) (cid:54) (cid:54) (cid:54) (cid:54) (cid:54) (cid:54) (cid:54)
| b   |     |     | c   | General |     |     |     | Lymphocyte |     |     |     | Myeloid |     |
| --- | --- | --- | --- | ------- | --- | --- | --- | ---------- | --- | --- | --- | ------- | --- |
DC subtypes (AREG ,  T H B D ,   M P H O S P H 6 ,   P L A U R , H BEGF
F21 + + M2 + (CREM, RGS2, SLA, NFE2L2) (CD69, RGS1, LMNA, RGCC, DUSP6, SOCS1) M E R T N L ,   G N A I3 ,  IL 1 B ,   B R E - AS 1)
|     | C1 C2 | G   |     |     |     |     |     |     |     |     |     |     |     |
| --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
D D S R E R E Lymphocytes Myeloid cells Lymphocytes Myeloid cells Lymphocytes Myeloid cells
|     | m m I G | E T | 20  |     |     |     | 15  |     |     | 20  |     |     |     |
| --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
HLA-DPB1
| GPR183 |        |     | erocs erutangiS |     |     |     | 10  |     |     | 15  |     |     |     |
| ------ | ------ | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|        | LAMP3  |     | 10              |     |     |     |     |     |     |     |     |     |     |
| CLEC9A |        |     |                 |     |     |     |     |     |     | 10  |     |     |     |
|        | CD1C   |     |                 |     |     |     | 5   |     |     |     |     |     |     |
|        | PLD4   |     |                 |     |     |     |     |     |     | 5   |     |     |     |
|        | GPR34  |     | 0               |     |     |     | 0   |     |     |     |     |     |     |
|        | IGSF21 |     |                 |     |     |     |     |     |     | 0   |     |     |     |
|        | EREG   |     |                 |     |     |     |     |     |     | −5  |     |     |     |
CLEC5A
TREM2 IV L IV L IV L IV L IV L IV L IV L IV L IV L IV L IV L IV L IV L IV L IV L IV L IV L IV L IV L IV L IV L IV L IV L IV L IV L IV L IV L
CHI3L1
m a  T a  T  T Na T NK pD C Mon o Mono m a  T a  T  T Na T NK pD C Mon o Mono m a  T a  T  T Na T NK pD C Mon o Mono
|     |     |     | B/Plas M/E | N M/E |     |     | B/Plas M/E N | M/E |     | B/Plas | M/E N | M/E |     |
| --- | --- | --- | ---------- | ----- | --- | --- | ------------ | --- | --- | ------ | ----- | --- | --- |
0 3 6 8  D8  4  D4  Cl.  C  8  D8  4  D4  Cl.  C  8  D8  4  D4  Cl.  C
|     |     |     | C D | C C D C |     | N   | C D C | C D C | N   |     | C D C C | D C | N   |
| --- | --- | --- | --- | ------- | --- | --- | ----- | ----- | --- | --- | ------- | --- | --- |
25–100% ln(UP10K + 1)
Fig. 2 | Identity and residency of lung immune cells. a, Human lung immune  killer cell; NKT, natural killer T cell; NK/T-p, proliferating natural killer/T cells.
molecular types clustered and annotated as in Fig. 1a. Clusters 45 (grey) and 56  b, Dot plot showing expression (10x dataset) in dendritic cell clusters 50–54 of,
(light red) were found only in one subject. Bar graphs show relative abundance  from top row to bottom: two canonical dendritic markers, four myeloid
of each immune type in lung (blue) and blood (red) samples. Lung ‘resident’  dendritic (mDC1, mDC2) markers, and six markers for three novel dendritic
populations (IGSF21+, EREG+ and TREM2+). c, Box-and-whisker plots of general,
(Res) or ‘homing’ (Hom) immune types, more than 90% enrichment in lung
samples; ‘intravascular’ (IV), more than 90% enrichment in blood; ‘egressed’  lymphocyte-specific, and myeloid-specific lung residency (egression)
(Egr), all other types (assignments are provisional because cell harvesting  signature scores (of cells in a) based on expression of indicated genes in 10x
influences enrichment values). Red lettering denotes cells not previously  profiles of indicated immune types isolated from blood (intravascular, IV) or
known to home to (be enriched in) lung or change expression (Δ) after  lung (L). Many previously known lymphocyte residency genes (for example,
egression from blood. Mono Cl., classical monocyte; CD4 M/E, CD8+ memory/
S1PR1, RUNX3, RBPJ and HOBIT) were lowly expressed and only uncovered in
effector T cell; CD4 Na, CD4+ naive T; CD8 M/E, CD8+ memory/effector T; CD8
SS2 profiles. Grey shading denotes myeloid cells. n cells in each
Na, CD8+ naive T; DC, dendritic cell; Mono Int., intermediate monocyte; mDC,
box-and-whisker (from left to right): 725; 187; 419; 771; 631; 1,411; 594; 2,419;
myeloid dendritic; pDC, plasmacytoid dendritic cell; MP, macrophage; MP-p,  644; 288; 519; 4,250; 21; 116; 1,064; 1,013; 200; and 604. For more details on
proliferating macrophage; Mono NC, non-classical monocyte; NK, natural  statistics and reproducibility, see Methods.
(small, simple) airways (Extended Data Fig. 3e, f). The basal cell clus-
New lung cell types, subtypes and states ters are distinguished by hundreds of genes, which suggests that they
Many canonical types were represented by more than one cluster, so  are molecularly distinct cell types that differ in hormone production
the specific identities of 25 clusters remained uncertain. All but one  (ALOX15, ADH7, SNCA) and adhesion (POSTN, ISLR, PCDH7) (Extended
were found in samples from several participants so were unlikely to  Data Fig. 3b). There were also distinct clusters of ciliated cells along
be subject-specific (Supplementary Table 2). This suggested that the  the proximal–distal axis (Extended Data Fig. 3g, h).
distinct expression profiles uncovered represented discrete molecular  We uncovered two clusters of alveolar type 2 (AT2) cells (Fig. 1c),
states or novel cell types or subtypes. To distinguish these possibili- which produce surfactant that prevents alveolar collapse. These
ties, we analysed the differentially expressed genes and examined cell  are intermingled throughout the alveolar epithelium (Fig. 1d). One
structure and location. cluster (WIF1+HHIP+CA2+) expressed higher levels of some canonical
We first identified clusters representing common cell states. Three  AT2 markers (SFTPA1, SFTPC and ETV5) and selectively expressed
clusters (proliferating basal cells, proliferating natural killer/T cells, and  inhibitors of Wnt (WIF1) and Hedgehog (HHIP) signalling and the cell
proliferating macrophages) were enriched in the expression of cell cycle  cycle (CDKN1A), indicating that they are quiescent (Extended Data
genes, which indicates that they represent the proliferative states of basal  Fig. 3i, left). The other, tenfold less-abundant cluster (AT2-signalling
cells, natural killer cells, T cells and macrophages, respectively, and are  cells) selectively expressed genes involved in Wnt signalling (WNT5A,
the most proliferative lung cell types (Extended Data Fig. 3a). Another  LRP5, CTNNBIP and TCF7L2 (also known as TCF4)) and detoxification
cluster (differentiating basal cells) had reduced expression of KRT5 and  (CP, GSTA1 and CYP4B1) (Extended Data Fig. 3i, right). AT2-signalling
increased expression of HES1, KRT7 and SCGB3A2, indicating active dif- cells could be alveolar stem cells, homologous to the rare, Wnt-active
ferentiation to other epithelial fates23,24, consistent with their transitional  subpopulation of mouse AT2 cells (AT2stem)25,26. However, homol-
morphology (Extended Data Fig. b, c). Proliferating and differentiating  ogy between human AT2-signalling and mouse AT2stem cells is pro-
basal cells derived mostly from proximal lung samples (Extended Data  visional, because although both show increased Wnt signalling or
Fig. 3d, e), suggesting one-third of proximal basal cells are active. components, the many other expression differences between human
The other basal cell clusters were quiescent and localized to prox- AT2-signalling and ‘bulk’ AT2 cells are not shared by mouse AT2stem
| imal (large, pseudostratified) airways, or both proximal and distal  |     |     |     |     |     |     | cells. |     |     |     |     |     |     |
| -------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- |
Nature | Vol 587 | 26 November 2020 | 621

Article
We found unexpected molecular diversity in the endothelial com- immune cells plus specific subprograms for myeloid cells and lym-
partment (Extended Data Fig. 3j). Two populations were identified as phocytes.
bronchial by their localization around bronchi (Extended Data Fig. 3k).
Thus, bronchial endothelial cells are distinct from their counterparts in
Cell markers, regulators and interactions
the pulmonary circulation, distinguished by matrix (VWA1 and HSPG2),
fenestrated morphology27 (PLVAP) and cell cycle-associated (MYC and We identified optimal markers for each previously known and newly
HBEGF) genes. Four clusters of endothelial cells in the pulmonary cir- identified lung cell type (Extended Data Fig. 5a, Supplementary Table
culation expressed capillary markers. Two (capillary aerocytes and 4). Approximately 200 markers can distinguish virtually all types
general capillary cells) are intermingled alveolar capillary cell types28; (Extended Data Fig. 5b), so could be used with multiplexed smFISH34–36
the others are rare capillary types showing features of both (capillary to simultaneously detect in clinical specimens alterations in their num-
‘intermediates’ 1 and 2). bers and relationships. A similar compendium of membrane protein
We identified new types in the stroma, the least characterized com- markers (Supplementary Table 4) could be used to purify or thera-
partment. Two clusters expressed classical fibroblast markers (BSG and peutically target specific lung cell types. We also identified around
COL1A2) (Fig. 1e) but one (SPINT2+FGFR4+GPC3+) localized to alveoli 400 cell type-selective transcription factors (Extended Data Fig. 5e,
(‘alveolar fibroblasts’) and the other (SFRP2+PI16+SERPINF1+) to vas- Supplementary Table 4), putative ‘master regulators’ that could help
cular adventitia and nearby airways (‘adventitial fibroblasts’) (Fig. 1f, create all lung cell types by cellular reprogramming. These include
Extended Data Fig. 4a–d). Both expressed genes involved in canonical what may be long-sought master regulators of AT1 cells (for example,
fibroblast functions (matrix biosynthesis, adhesion and signalling MYRF), which comprise the gas-exchange surface, and of pericytes
regulators) but the specific genes often differed (Extended Data Fig. 4e). (TBX5) (Extended Data Fig. 5c, d).
Each cluster also has distinct functions: expression of voltage-gated The atlas allowed us to map the cell targets of circulating hormones,
sodium channel SCN7A and glutamate receptor GRIA1 suggest alveolar based on expression of their cognate receptors. Receptors for some
fibroblasts are excitable cells with glutamatergic input (Supplementary hormones are broadly expressed, indicating direct action throughout
Table 4). Their profiles also suggest novel, shared functions including the lung (Extended Data Fig. 6a). Other hormones have specific and
the recruitment of immune cells (IL1RL1, IL32, CXCL2 and genes in the unexpected targets, such as somatostatin (SSTR1, arteries), melano-
class II major histocompatibility complex locus) and the complement cortin (MC1R, ionocytes), and oxytocin (OXTR, ciliated cells). Pericytes
system (C2, C3, C7, CFI, CFD, CFH and CFB). are predicted targets of several hormones, which could affect their
Two stromal clusters were enriched for ACTA2, a canonical marker contractile machinery to regulate alveolar perfusion (Extended Data
of myofibroblasts (Fig. 1e), which help form and stabilize alveoli. One Fig. 6b). Receptors for half the hormones were not detectably expressed
cluster (WIF1+FGF18+ASPN+) is classical myofibroblasts and localized so these hormones may not directly influence lung physiology. We also
to alveolar ducts (Extended Data Fig. 4f). The other (‘fibromyocytes’) mapped local signalling interactions by examining expression of ligands
showed higher expression of contractile genes (MYH11, CNN1 and and receptors, which predicts up to hundreds of interactions among
TAGLN), was preferentially isolated from samples of proximal lungs, neighbouring cell types (Extended Data Fig. 6c, Supplementary Table 5).
and was found both intermingled with airway smooth muscle and in The expression of chemokine receptors illuminated immune cell
alveoli (Extended Data Figs. 3e, 4g). Both populations shared expres- homing (Fig. 3). Our data confirmed canonical homing interactions such
sion of genes for canonical fibroblast functions, although the specific as CD4+ T cells to lymphatic vessels, and provides specificity for others
genes differed from alveolar and adventitial fibroblasts (Supplemen- such as plasma cell homing to epithelial mucosa through CCL28 from
tary Table 4). serous cells. It also predicts new interactions such as CX3CR1-mediated
homing of nonclassical monocytes to CX3CL1-expressing endothelial
and airway epithelial cells. All three new dendritic populations express
Lung immune cell residency signatures
CCR1, which could mediate their attraction to veins (CCL23), bronchial
To distinguish between lung-resident, egressed and circulating immune vessels (CCL14), ciliated cells (CCL15), and lymphocytes (CCL5). Iono-
cells, we compared the relative abundance of each immune population cytes are the only non-immune cell to express appreciable levels of any
in lung and peripheral blood samples from the same subject (Fig. 2a). chemokine receptor (CXCR4).
Eleven clusters (including alveolar macrophages, as expected29)
consisted of cells only from lung samples, with no or rare exception,
Mapping cellular focus of lung diseases
which indicates that they are lung-resident or greatly enriched. This
included three novel lung dendritic populations: IGSF21+ and rare EREG+ We determined the expression of 233 extant lung disease genes
dendritic cells express asthma genes (CCL2, CCL13 and IGSF21) and (Extended Data Fig. 7). Disease genes with cell-type-specific expres-
developmental signals (EREG, VEGFA, AREG), respectively, and both sion (Extended Data Fig. 8a) and cell types expressing many genes
localize to proximal vessels; TREM2+ dendritic cells localize to vessels associated with a specific disease (Extended Data Fig. 8b) are of special
and alveoli and express lipid machinery (APOC1, APOE and CYP27A1) interest because they can pinpoint the cellular origin of disease. This
(Fig. 2b, Extended Data Fig. 4k–n). supported known or suspected ‘culprit’ cells for 27 genes involved in
The other immune cell types were found in both lung and blood 12 diseases, and identified potential culprits for 21 genes implicated in
samples. For some types, every cell—whether from lung or blood— 15 diseases including pericytes in pulmonary hypertension, capillar-
clustered together. However, for other types, cells from lung formed ies in atrioventricular dysplasia, and AT2 cells in chronic obstructive
a separate cluster (Extended Data Fig. 4o). Some of the differentially pulmonary disease (COPD). We confirmed pericyte, capillary and AT2
expressed genes may be due to technical differences (for example, expression of disease genes by smFISH (Extended Data Fig. 8c–e).
collagenase treatment of lung30, circulating RNA in blood31), but others We mapped expression of 80 genes encoding virus receptors, includ-
such as upregulation in lung cells of lymphocyte-residence gene CD69 ing 26 used by respiratory viruses (Extended Data Figs. 9a, 10). NECTIN4
probably represent genes induced after egression32. We identified a (measles virus receptor) was enriched in club, ciliated, differentiating
core transcriptional signature for all human lung-resident lympho- basal, and goblet cells, and CDHR3 (‘common cold’ rhinovirus C) was
cytes (Fig. 2c), which overlaps a residence signature found by bulk enriched in ciliated and neuroendocrine cells, indicating that infections
RNA sequencing of CD8+ T cells in mouse spleen, gut and liver33. We initiate in those bronchial types. By contrast, ACE2 (SARS, COVID-19
also found a residency signature for lung myeloid cells that overlaps coronaviruses) and DPP4 (MERS coronavirus) were both detected in AT2
the lymphocyte signature, supporting a core residency program for cells (Extended Data Fig. 9b), consistent with severe alveolar pathology37.
622 | Nature | Vol 587 | 26 November 2020

Myeloid Lymphocytes Myeloid Lymphocytes Stromal Endothelium Epithelium
o
o n o M o n C C
I nt M o n N o C M o n O o L R 1 C C l. l M . M o n T o R E M 2 E D R C E G D I C G S F 2 1 m D D C C 2 m D C 1 p D C M P- p M P M K B as/ M a B 2 as/ M a N 1 K/ T- p N K N K T C D 4 N a C D 4 M/ C E D 8 N a C D 8 M/ P E l as m a BI o nRecep C to h r e s mokin L C e ig X a C n L d 1 s I nt. M o n N o C M o n O o L R 1 Cl C . l. M o n T o R E M 2 E D R E G D I C G S F 2 1 m D D C 2 m D C 1 p D C M P- p M P M K B as/ M a B 2 as/ M a N 1 K/ T- p N K N K T C D 4 N a C D 4 M/ E C D 8 N a C D 8 M/ E Pl as m a BM es o Peri Li p F Alv F A dv F My o F Fi b M V S M A S M Ly m Br o 2 Br o 1 C a p-i 2 C a p-i 1 C a p- a C a p Vei n Art A T 2-s A T 2 A T 1 N E I o n S er M u c G o b B as- p B as- d B as- p x B as Cil- p x CilCl u b
CXCR1 CXCL2
CXCL3
CXCR2 CXCL5
CXCL6
CXCR3 PPBP
CXCR4 CXCL8
CXCL9
CXCR6 CXCL10
CXCL12
GPR35 CXCL16
CCR2 CX C C C L1 L 7 8
CCR1 CCL2
CCL3
CCR5 CCL5
CCL13
CCR6 CCL14
CCR7 CCL15
CCL20
CCR10 CCL21
CCL23
CX3CR1 CCL28
CX3CL1
Migrating cells ln(UP10K + 1) 0 1 2 3 4 Target cells ln(UP10K + 1) 0 2 4 6 8 25–100%
Fig. 3 | Chemokine signalling predicts immune cell homing in lung. Dot migrating immune cell types and ionocytes (ion, red) expressing cognate
plots showing expression of chemokine receptors (left) and ligands (right) in receptor; thicker lines indicate previously unknown interactions. For more
human lung cells (10x dataset); only cell types and chemokines with detected details on statistics and reproducibility, see Methods. Bas/Ma, basophil/mast
expression are shown. Colored lines connect ligand sources (target cells) with cell; MK, megakaryocyte.
the canonical AT1 transcription factor in mouse, is expressed in both
Evolution of cell types and expression
AT1 and AT2 cells in human (Fig. 4c, e), which indicates the existence of
Construction of a mouse lung atlas2 plus additional cells annotated other AT1 transcription factors such as MYRF, which is AT1-selective in
as above for human (Supplementary Table 6) allowed analysis of evo- both species (Extended Data Fig. 12c). Expanded expression of RAMP3,
lutionary conservation of lung cell types and their transcriptomes. co-receptor for vasodilators CGRP and adrenomedullin, presumably
Homologous cell types were assigned by conserved expression of alters pulmonary vascular response to these hormones (Extended
cell-type markers (Fig. 4a). Notably, mice seem to lack 17 (29%) of the Data Fig. 12d).
58 human lung cell types including 12 of the 14 (86%) newly identified Type 3 (‘expression switch’) changes involve a switch in expression
types. Some missing mouse populations might be rare, transient, unsta- from one cell type to another. Two medically important examples
ble, or too diverged to relate transcriptionally so may be uncovered are COPD/emphysema genes SERPINA1 and HHIP, both selectively
by further studies. By contrast, just five mouse cell populations, all expressed in AT2 cells in human but alveolar stromal cells in mice
immune, were not found in human. This suggests substantial diversi- (Fig. 4d, e, Extended Data Fig. 12e); other hedgehog pathway com-
fication of lung cell types during mammalian evolution. ponents were mostly conserved (Extended Data Fig. 12f). Extreme
We compared expression levels of all active genes in each human examples occurred during evolution of species-specific cell types, such
cell type with those of the orthologous genes in the corresponding as consolidation in the expression of anti-bacterial enzymes (LTF, LYZ
mouse type (Extended Data Fig. 11a, Supplementary Table 7). Most and BPIFB1) from several mouse airway cells into human-specific serous
cell types correlated best with their counterparts across species, but cells, and consolidation of broadly expressed lipid-handling genes
surprisingly one human type (goblet) showed greater correlation (PLIN2 and APOE) from mouse alveolar fibroblasts (which can contain
with another mouse type (club, R = 0.68 versus 0.63) (Extended Data lipid droplets) and myofibroblasts to human-specific lipofibroblasts
Fig. 11b)—despite conserved expression of canonical markers and mas- (Extended Data Fig. 12g).
ter regulator SPDEF (Extended Data Fig. 11c). Corresponding cell types Despite general conservation of cell type expression patterns noted
in human and mouse diverged in expression (a greater than 20-fold above, only 6% of expressed genes showed fully conserved patterns
change, P < 0.05) of hundreds of genes, such as SERPINA1, PGC, WIF1 (type 0), most extremely specific or broadly expressed (Extended Data
and LYZ in AT2 cells (Fig. 4b). Lung as a whole had fewer diverged genes Fig. 12h, Supplementary Table 8). Thus, expression patterns of nearly
than any cell type, which suggests that expression lost in one type is all genes are evolutionarily labile, most undergoing broadening (55%,
gained in another (Extended Data Fig. 11d). Diverged genes varied above type 2) or simple gain or loss (29%, type 1) and rarely cell type switching
age-related expression changes in mice (Extended Data Fig. 11e) and (10%, type 3) (Supplementary Table 9).
included canonical cell-type markers, transcription factors, signalling
molecules and disease genes.
Discussion
Evolutionary changes in expression grouped into four types (Sup-
plementary Table 7). Type 0 (‘conserved’) genes are expressed in the We constructed a comprehensive expression atlas of human lung
same cell types in mouse and human (Fig. 4e, Extended Data Fig. 12a). comprising 58 molecular types and their locations (Fig. 1b) including
Type 1 (‘expression gain/loss’) genes show simple gain (or loss) of 41 out of 45 previously known cell types, all but the exceedingly rare.
expression between species, which involved a single cell type (type We identified 14 novel populations across all four compartments that
1a, PGC) (Fig. 4e), several types (type 1b, RNASE1) (Extended Data are as distinct molecularly as the canonical cell types; each must be
Fig. 12b), or entire lung (type 1c, TRIM38) (Extended Data Fig. 12b). thoroughly characterized, as done for new capillary types28. If there
Type 2 (‘expression expansion/contraction’) changes involved gain are other lung cell types, they must be exceedingly rare, fragile, region-
(or loss) of expression in additional lung cell types, expanding (or con- or stage-specific, or so similar to the 58 that they are not resolved by
tracting) expression of the gene during evolution. For example, HOPX, current methods.
Nature | Vol 587 | 26 November 2020 | 623

Article
| a   |     |     | Epithelial |     |     |     | Endothelial |     |     |     | Stromal |     |
| --- | --- | --- | ---------- | --- | --- | --- | ----------- | --- | --- | --- | ------- | --- |
Mouse Club Cil Bas Gob * * Ion NE AT1 AT2 Art Vein Cap-a Cap * * Lym ASMVSM MyoF AdvF AlvF * Peri Meso
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 20 19 21 22 23 24 25 26 27 28 29 30 31 32 33
Human Club Cil Cil-pxBasBas-pxBas-dBas-pGobMuc Ser Ion NE AT1 AT2AT2-s Art Vein Cap-aCap-i1CapCap-i2Bro1 Bro2 Lym ASMVSM MyoF FibM AdvF AlvF LipF Peri Meso
|     |     |     | Lymphocytes |         |     | Granulocytes | Platelets |     |     | Myeloid |      |           |
| --- | --- | --- | ----------- | ------- | --- | ------------ | --------- | --- | --- | ------- | ---- | --------- |
|     |     | B   | CD8 CD8     | CD4 CD4 | T T |              |           |     |     | DC      | Mono | Mono Mono |
Mouse B ZBTB32Plasma M/E Na M/E Na LY6G5BALOX5 NKT NK NK/T-p Neut Mast Baso Mega AlvMPAlvMP(cid:60)ppDC mDC1 mDC2 CCR7 IntM(cid:92) Class NC Int
* *
Human 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58
B Plasma CD8 CD8 CD4 CD4 NKT NK NK/T-p Neut Mast Mast Mega MP MP(cid:60)p pDC mDC1 mDC2 DC DC DC Mono Mono Mono Mono
|     |     |     | M/E Na | M/E Na |     | Ba 1 | Ba 2 |     |     | IGSF21EREG | TREM2 Class OLR1 | NC Int |
| --- | --- | --- | ------ | ------ | --- | ---- | ---- | --- | --- | ---------- | ---------------- | ------ |
b HOPX immunostaining (type 2 expansion) HHIP smFISH (type 3 switch)
AT2
|     |      | R = 0.69, 189 divergent genes |     |     | c             |     |     | Alveoli | d   |     |     | Alveoli |
| --- | ---- | ----------------------------- | --- | --- | ------------- | --- | --- | ------- | --- | --- | --- | ------- |
|     | 12.5 |                               |     |     | )ylno 1TA( mM |     |     |         |     |     |     |         |
)FoyM( mM
eneg fo noisserpxE )1 + MPC(nl ,namuh ni
10.0
PGC
SLPI
|     | 7.5 | Mm(SERPINA1) |     |     |     |     |     |     |     |     |     |     |
| --- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
SDR16C5
|     | 5.0 | CRTAC1 |     |     |     |     |     |     | Elastin | HHIP | Merge |     |
| --- | --- | ------ | --- | --- | --- | --- | --- | --- | ------- | ---- | ----- | --- |
WIF1
|     |     |        | SCD     |           | 2)  |     |     | Alveoli |      |     |     | Alveoli |
| --- | --- | ------ | ------- | --------- | --- | --- | --- | ------- | ---- | --- | --- | ------- |
|     | 2.5 | CSF3R  | LPCAT1  |           | AT  |     |     |         |      |     |     |         |
|     |     | S100G  | TSPAN11 |           | d   |     |     |         | 2)   |     |     |         |
|     |     | EGFL6  |         |           | n   |     |     |         | AT   |     |     |         |
|     | 0   |        | RNASE4  | Mm(LYZ)   | a   |     |     |         |      |     |     |         |
|     |     |        |         |           | 1   |     |     |         | Hs ( |     |     |         |
|     |     | 0  2.5 | 5.0 7.5 | 10.0 12.5 | AT  |     |     |         |      |     |     |         |
Hs (
|     |     | Expression of gene    |     |     |      |      |       |     |     |      | Merge |     |
| --- | --- | --------------------- | --- | --- | ---- | ---- | ----- | --- | --- | ---- | ----- | --- |
|     |     | in mouse, ln(CPM + 1) |     |     | MUC1 | HOPX | Merge |     | SPC | HHIP |       |     |
e Type 0 conserved expression pattern Type 1 gain/loss Type 2 expansion/contraction Type 3 switch
ln(CPM + 1)
ASCL1 expression 0 4 8 PGC expression 0 5 10 HOPX expression 0 5 10 HHIP expression 0 6 12
Mouse
25–100%
Epi Endo Stromal Immune Epi Endo Stromal Immune Epi Endo Stromal Immune Epi Endo Stromal Immune
Human
Fig. 4 | Evolutionary divergence of lung cell types and expression patterns.  and AT2 marker MUC1 (green), and DAPI (blue). HOPX is expressed selectively
a, Mouse (top) lung molecular cell types (profiled and identified as for human,  in AT1 cells (arrowheads) in mouse but in human expression has expanded to
see Methods) aligned with homologous human types (bottom, Figs. 1a, 2a)   AT2 and AT2-signalling cells (dashed circles). Scale bars, 10 μm. Staining
by expression of classical markers in Supplementary Table 6. Thin lines,  repeated on three participants and mice. d, Alveolar sections from mouse (top)
evolutionary expansions; dashed lines, potential expansions of  and human (bottom) probed by smFISH for Hhip and HHIP (red) and hydrazide
functionally-related types. Red text, newly identified populations (light red,  staining for myofibroblast marker elastin (green) in mouse and smFISH for
identified in only one subject); blue, cell states more abundant in human; grey,  AT2 marker SFTPC (green) in human. Note HHIP expression switch from
extant mouse cell types not captured in our data or found in only one patient in  myofibroblast (mouse, arrowhead) to AT2 cells (human, dashed circles). Scale
human. Asterisk denotes missing cell types. AlvMP, alveolar macrophages;  bars, 10 μm. Staining repeated on three human partipicants and mice. e, Dot
AlvMP-p, proliferating alveolar macrophages. b, Scatter plot comparing  plots of expression (SS2 data sets) of homologous genes indicated in mouse
average expression levels (dots) in AT2 cells of each expressed human gene and  and human lung cell types (ordered as in a) exemplifying the four observed
mouse orthologue (SS2 datasets; n = 3,404 human and 318 mouse AT2 cells).   scenarios (type 0, 1, 2, 3) for evolution of cellular expression pattern. Colours
R denotes Pearson correlation coefficient. Red dots denote divergent genes  highlight cell types with conserved (blue) and diverged (red) expression. Endo,
(selected ones indicated) expressed 20-fold higher in either species. P < 0.05,  endothelial; Epi, epithelial. For more details on statistics and reproducibility,
| ‘MAST’ differential gene expression test. Scale, ln(CPM + 1). c, Alveolar sections  |     |     |     |     |     | see Methods. |     |     |     |     |     |     |
| ----------------------------------------------------------------------------------- | --- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- |
from mouse (top, Mm) and human (bottom, Hs) immunostained for HOPX (red)
The atlas has broad implications for physiology and medicine,  functional consequences of these changes, and to determine the selec-
providing insight into the functions, regulation and interactions of  tive forces operative for genes with fully conserved expression. The
the known and new cell types. It identifies those directly affected by  evolutionary cell type and expression changes predict where mouse
hormones, viruses and extant lung disease genes, and distinguishes  will fail to model human lung physiology and disease.
lung-resident and homing immune cell types and infers their expres- The success of our atlas relied on: procuring fresh tissue across the
sion changes after egression from circulation and the cellular sources  organ plus matched blood; balancing tissue compartments to ensure
of homing signals. The atlas defines type-selective transcription factors  broad cell representation; extensive profiling of each subject using
for creating cells to engineer a lung, and provides optimal markers and  broad cell capture and deep gene coverage scRNA-seq strategies;
a benchmark for monitoring all types and how they change during  clustering subject and compartment data separately and iteratively;
development, ageing, disease and evolution. assigning cell identies using extant markers, functions of selectively
Mice appear to lack 17 out of the 58 human molecular lung cell types,  expressed genes, and tissue localization. Applying the approach to
including most (12 out of 14) of the newly discovered ones. This sug- other organs could create a comprehensive human molecular cell atlas.
gests a considerable expansion of cell types in the human lineage,
perhaps for new functions, durability, or regenerative capacity of
Online content
our 6,000-fold larger lungs and 30-times longer lifespan38,39. Even
homologous cell types diverged in expression of hundreds of genes.  Any methods, additional references, Nature Research reporting sum-
Indeed, just 6% of expressed genes had fully conserved expression pat- maries, source data, extended data, supplementary information,
terns across the lung, indicating widespread gain, loss or conversion  acknowledgements, peer review information; details of author con-
of cell-type-specific transcriptional enhancers during mammalian  tributions and competing interests; and statements of data and code
evolution. It will be important to unravel the genetic mechanisms and  availability are available at https://doi.org/10.1038/s41586-020-2922-4.
624 | Nature | Vol 587 | 26 November 2020

1. Enge, M. et al. Single-cell analysis of human pancreas reveals transcriptional signatures 22. Howitt, M. R. et al. Tuft cells, taste-chemosensory cells, orchestrate parasite type 2
of aging and somatic mutation patterns. Cell 171, 321–330.e14 (2017). immunity in the gut. Science 351, 1329–1333 (2016).
2. Tabula Muris Consortium. Single-cell transcriptomics of 20 mouse organs creates a 23. Rock, J. R. et al. Notch-dependent differentiation of adult airway basal stem cells. Cell
Tabula Muris. Nature 562, 367–372 (2018). Stem Cell 8, 639–648 (2011).
3. Han, X. et al. Mapping the mouse cell atlas by microwell-seq. Cell 173, 1307 (2018). 24. Garcia, S. R. et al. Single-cell RNA sequencing reveals novel cell differentiation dynamics
4. Zeisel, A. et al. Molecular architecture of the mouse nervous system. Cell 174, 999–1014. during human airway epithelium regeneration. Preprint at https://doi.org/10.1101/451807
e22 (2018). (2018).
5. Saunders, A. et al. Molecular diversity and specializations among the cells of the adult 25. Nabhan, A. N., Brownfield, D. G., Harbury, P. B., Krasnow, M. A. & Desai, T. J. Single-cell Wnt
mouse brain. Cell 174, 1015–1030.e16 (2018). signaling niches maintain stemness of alveolar type 2 cells. Science 359, 1118–1123
6. Vento-Tormo, R. et al. Single-cell reconstruction of the early maternal-fetal interface in (2018).
humans. Nature 563, 347–353 (2018). 26. Zacharias, W. J. et al. Regeneration of the lung alveolus by an evolutionarily conserved
7. Young, M. D. et al. Single-cell transcriptomes from human kidneys reveal the cellular epithelial progenitor. Nature 555, 251–255 (2018).
identity of renal tumors. Science 361, 594–599 (2018). 27. Stan, R. V. et al. The diaphragms of fenestrated endothelia: gatekeepers of vascular
8. Aizarani, N. et al. A human liver cell atlas reveals heterogeneity and epithelial progenitors. permeability and blood composition. Dev. Cell 23, 1203–1218 (2012).
Nature 572, 199–204 (2019). 28. Gillich, A. et al. Capillary cell-type specialization in the alveolus. Nature 586, 785–789
9. Han, X. et al. Construction of a human cell landscape at single-cell level. Nature 581, (2020).
303–309 (2020). 29. Tan, S. Y. S. & Krasnow, M. A. Developmental origin of lung macrophage diversity.
10. Young, J. Malpighi’s “De pulmonibus.”. Proc. R. Soc. Med. 23, 1–11 (1929). Development 143, 1318–1327 (2016).
11. Gehr, P., Bachofen, M. & Weibel, E. R. The normal human lung: ultrastructure and 30. van den Brink, S. C. et al. Single-cell sequencing reveals dissociation-induced gene
morphometric estimation of diffusion capacity. Respir. Physiol. 32, 121–140 (1978). expression in tissue subpopulations. Nat. Methods 14, 935–936 (2017).
12. Balis, J. U., Paterson, J. F., Paciga, J. E., Haller, E. M. & Shelley, S. A. Distribution and 31. Zheng, G. X. Y. et al. Massively parallel digital transcriptional profiling of single cells. Nat.
subcellular localization of surfactant-associated glycoproteins in human lung. Lab. Commun. 8, 14049 (2017).
Invest. 52, 657–669 (1985). 32. Shiow, L. R. et al. CD69 acts downstream of interferon-α/β to inhibit S1P1 and lymphocyte
13. Hermans, C. & Bernard, A. Lung epithelium-specific proteins: characteristics and egress from lymphoid organs. Nature 440, 540–544 (2006).
potential applications as markers. Am. J. Respir. Crit. Care Med. 159, 646–678 (1999). 33. Mackay, L. K. et al. Hobit and Blimp1 instruct a universal transcriptional program of tissue
14. Franks, T. J. et al. Resident cellular components of the human lung: current knowledge residency in lymphocytes. Science 352, 459–463 (2016).
and goals for research on cell phenotyping and function. Proc. Am. Thorac. Soc. 5, 34. Moffitt, J. R. & Zhuang, X. RNA imaging with multiplexed error-robust fluorescence in situ
763–766 (2008). hybridization (MERFISH). Methods Enzymol. 572, 1–49 (2016).
15. Tang, F. et al. mRNA-Seq whole-transcriptome analysis of a single cell. Nat. Methods 6, 35. Wang, X. et al. Three-dimensional intact-tissue sequencing of single-cell transcriptional
377–382 (2009). states. Science 361, eaat5691 (2018).
16. Gawad, C., Koh, W. & Quake, S. R. Single-cell genome sequencing: current state of the 36. Eng, C. L. et al. Transcriptome-scale super-resolved imaging in tissues by RNA seqFISH.
science. Nat. Rev. Genet. 17, 175–188 (2016). Nature 568, 235–239 (2019).
17. Treutlein, B. et al. Reconstructing lineage hierarchies of the distal lung epithelium using 37. Huang, C. et al. Clinical features of patients infected with 2019 novel coronavirus in
single-cell RNA-seq. Nature 509, 371–375 (2014). Wuhan, China. Lancet 395, 497–506 (2020).
18. Reyfman, P. A. et al. Single-cell transcriptomic analysis of human lung provides insights 38. Limjunyawong, N., Fallica, J., Horton, M. R. & Mitzner, W. Measurement of the
into the pathobiology of pulmonary fibrosis. Am. J. Respir. Crit. Care Med. 199, 1517–1536 pressure-volume curve in mouse lungs. J. Vis. Exp. 52376, 52376 (2015).
(2019). 39. Seeley, R. R., Stephens, T. D. & Tate, P. Essentials of Anatomy and Physiology 7th edn
19. Braga, F. A. V. et al. A cellular census of human lungs identifies novel cell states in health (2005).
and in asthma. Nat. Med. 25, 1153–1163 (2019).
20. Picelli, S. et al. Full-length RNA-seq from single cells using Smart-seq2. Nat. Protoc. 9, Publisher’s note Springer Nature remains neutral with regard to jurisdictional claims in
171–181 (2014). published maps and institutional affiliations.
21. Blondel, V. D. et al. Fast unfolding of communities in large networks. J. Stat. Mech. 2008,
P10008 (2008). © The Author(s), under exclusive licence to Springer Nature Limited 2020
Nature | Vol 587 | 26 November 2020 | 625

Article
Methods strainer (Fisherbrand 22363548), pelleted again (300g, 5 min, 4 °C),
and resuspended in magnetic activated cell sorting (MACS) buffer (0.5%
Human lung tissue and peripheral blood BSA, 2 mM EDTA in PBS) with Human FcR Blocking Reagent (Miltenyi
Freshly resected lung tissue was procured intraoperatively from 130-059-901) to block non-specific binding of antibodies (see below).
patients undergoing lobectomy for focal lung tumours. Normal lung Immune cells, including granulocytes, were isolated from peripheral
tissues (approximately 5 cm3) were obtained from uninvolved regions blood using a high density ficoll gradient45. In brief, peripheral blood
and annotated for the specific lung lobe and location along the airway was diluted tenfold with FACS buffer (2% FBS in PBS), carefully layered
or periphery. Pathological evaluation (by G.B.) confirmed normal histol- on an RT Ficoll gradient (Sigma HISTOPAQUE-1119), and centrifuged
ogy of the profiled regions, except for areas of very mild emphysema in at 400g for 30 min at room temperature. The buffy coat was carefully
patient 1. Patient 1 was a 75-year-old male with a remote history of smok- removed, diluted fivefold with FACS buffer, pelleted (300g, 5 min, 4 °C),
ing, diagnosed with early stage adenocarcinoma who underwent left and incubated in ice cold FACS buffer containing DNase I (Worthington
upper lobe (LUL) lobectomy; two blocks of normal tissue were obtained LS006344) for 10 min at 4 °C. Clumps were separated by gentle pipet-
from lung periphery (distal 1a and 1b). Patient 2 was a 46-year-old male, ting to create a single-cell suspension.
non-smoker with a right middle lobe (RML) endobronchial carcinoid, Mouse lung samples were processed into single cell suspensions as
who underwent surgical resection of the right upper and middle lobes; previously described2. In brief, each lung was dissected, minced, and
two blocks of tissue were selected from mid-bronchial region (medial placed in gentleMACS c-tubes (Miltenyi 130-096-334) with digestion
2) and periphery (distal 2) of right upper lobe (RUL). Patient 3 was a buffer (400 μg ml−1 liberase DL (Sigma 5466202001) in RPMI (Gibco
51-year-old female, non-smoker with mild adult-onset asthma and a 72400120)). The minced tissue was partially dissociated by running
left lower lobe (LLL) endobronchial typical carcinoid, who underwent ‘m_lung_01’ on a gentleMACS Dissociator (Miltenyi 130-093-235),
LLL lobectomy; three tissue blocks were resected from the bronchus incubated at 37 °C on a nutator for 30 min, completely dissociated
(proximal 3), mid-bronchial (medial 2), and periphery (distal 3) of the on a gentleMACS by running ‘m_lung_02’, and kept at 4 °C or on ice for
LLL. All tissues were received and immediately placed in cold PBS and the remainder of the protocol. Cells were washed with 5% FBS in PBS,
transported on ice directly to the research lab for single cell dissocia- centrifuged at 300g for 5 min, resuspended in 5% FBS in PBS, filtered
tion procedures. Peripheral blood was collected from patients 1 and through a 70-μm strainer (Fisherbrand 22363548), and centrifuged
3 in EDTA tubes. For bulk RNA-seq of canonical immune populations, again and resuspended in FACS buffer (2% FBS in PBS).
whole blood from healthy human donors was obtained commericially
(AllCells) in EDTA tubes. Patient tissues were obtained under a protocol Magnetic separation of lung tissue compartments
approved by Stanford University’s Human Subjects Research Compli- Immune and endothelial cells were overrepresented in our previous
ance Office (IRB 15166) and informed consent was obtained from each mouse single-cell suspensions. To partially deplete these populations
patient before surgery. All experiments followed applicable regulations in our human samples, we stained cells isolated from lung with MACS
and guidelines. microbeads conjugated to CD31 and CD45 (Miltenyi 130-045-801, 130-
091-935) then passed them through an LS MACS column (Miltenyi,
Mouse lung tissue 130-042-401) on a MidiMACS Separator magnet (Miltenyi, 130-042-
Lung tissue for Tabula Muris Senis40 was obtained as previously 302). Cells retained on the column were designated ‘immune and
described. We obtained additional tissue from two mice express- endothelial enriched’. The flowthrough cells were then split, with 80%
ing Cre recombinase and two expressing oestrogen-inducible Cre immunostained for FACS (see below) and the remaining 20% stained
recombinase (Cre-ERT2) for conditional cell-specific labelling in vivo with EPCAM microbeads (Miltenyi 130-061-101). EPCAM stained cells
with the gene-targeted alleles FVB-Tbx4-LME-cre41,42 (lung stroma) were passed through another LS column. Cells retained on the column
and B6.129-Axin2-cre-ERT241, respectively. Cre-dependent reporter were labelled ‘epithelial enriched’, and cells that flowed through were
alleles Rosa26ZsGreen1, which expresses cytosolic ZsGreen1 follow- designated ‘stromal’.
ing Cre-mediated recombination, and Rosa26mTmG, which expresses
membrane-targeted green fluorescent protein (mGFP) after recombina- Flow cytometry and cell sorting
tion and membrane-targeted tdTomato (mTomato) in all other tissues, Lysis plates for single-cell mRNA sequencing were prepared as previ-
were used to label cells expressing Tbx4 and Axin2, respectively43,44. ous described2. 96-well lysis plates were used for cells from the blood
Induction of the Axin2-cre-ERT2 allele was done by intraperitoneal and mouse samples and contained 4 μl of lysis buffer instead of 0.4 μl.
injection of tamoxifen (3 mg) once a day for three days as described25. After negative selection against immune and endothelial cells by
All mouse experiments followed applicable regulations and guidelines MACS, the remaining human lung cells were incubated with FcR Block
and were approved by the Institutional Animal Care and Use Committee (Becton Dickinson 564219) for 5 min and stained with directly conju-
at Stanford University (Protocol 9780). gated anti-human CD45 (Biolegend 304006) and EPCAM (eBioscience
25-9326-42) antibodies on a Nutator for 30 min at the manufacturer’s
Isolation of lung and blood cells recommended concentration. Cells were then pelleted (300g, 5 min,
Individual human lung samples were dissected, minced, and placed in 4 °C), washed with FACS buffer three times, then incubated with cell
digestion media (400 μg ml−1 liberase DL (Sigma 5466202001) and 100 viability marker Sytox blue (1:3,000, ThermoFisher S34857) and loaded
μg ml−1 elastase (Worthington LS006365) in RPMI (Gibco 72400120) onto a Sony SH800S cell sorter. Living single cells (Sytox blue-negative)
in a gentleMACS c-tube (Miltenyi 130-096-334). Samples were par- were sorted into lysis plates based on three gates: EPCAM+CD45−
tially dissociated by running ‘m_lung_01’ on a gentleMACS Dissociator (designated epithelial), EPCAM−CD45+ (designated immune), and
(Miltenyi 130-093-235), incubated on a Nutator at 37 °C for 30 min, and EPCAM−CD45- (designated endothelial or stromal).
then dispersed to a single cell suspension by running ‘m_lung_02’. Pro- Immune cells from subject matched blood were incubated with
cessing buffer (5% fetal bovine serum in PBS) and DNase I (100 μg ml−1, FcR Block and Brilliant Violet buffer (BD 563794) for 20 min and then
Worthington LS006344) were then added and the samples rocked at stained with directly conjugated anti-human CD3 (BD 563548), CD4 (BD
37 °C for 5 min. Samples were then placed at 4 °C for the remainder of 340443), CD8 (BD 340692), CD14 (BD 557831), CD19 (Biolegend 302234),
the protocol. Cells were filtered through a 100-μm filter, pelleted (300g, CD47 (BD 563761), CD56 (BD 555516), and CD235a (BD 559944) antibod-
5 min, 4 °C), and resuspended in ACK red blood cell lysis buffer (Gibco ies for 30 min at the manufacturer’s recommended concentration. Cells
A1049201) for 3 min, after which the buffer was inactivated by adding were pelleted (300g, 5 min, 4 °C), washed with FACS buffer twice, and
excess processing buffer. Cells were then filtered through a 70-μm then incubated with the viability marker propidium iodide and loaded

onto a BD FACSAria II cell sorter. Living (propidium iodide-negative) control library was spiked in at 1% before sequencing. Human libraries
single, non-red blood (CD235a−) cells were sorted into lysis plates along were sequenced on a NovaSeq 6000 (Illumina) and mouse libraries on
with specific immune populations: B cells (CD19+CD3−), CD8+ T cells a NextSeq 500 (Illumina).
(CD8+), CD4+ T cells (CD4+), natural killer cells (CD19−CD3−CD56+CD14−), Cells isolated from each compartment (immune and endothelial
classical monocytes (CD19−CD3−CD56−CD14+). After sorting, plates enriched, epithelial enriched, stromal) and subject blood were cap-
were quickly sealed, vortexed, spun down for 1 min at 1,000g, snap tured in droplet emulsions using a Chromium Single-Cell instrument
frozen on dry ice, and stored at −80 until cDNA synthesis. (10x Genomics) and libraries were prepared using the 10x Genomics 3′
Mouse cells were incubated with the viability marker DAPI and loaded Single Cell V2 protocol as previously described2. All 10x libraries were
onto a BD Influx cell sorter. Living (DAPI-negative) single cells were pooled and sequenced on a NovaSeq 6000 (Illumina).
sorted into lysis plates based on presence or absence of the fluorescent
lineage label (mEGFP for Axin2-cre-ERT2, ZsGreen1 for Tbx4-LME-cre). Immune cell bulk mRNA sequencing
Immune cells for bulk mRNA sequencing were incubated with FcR Total RNA from bulk-sorted canonical immune populations was reverse
Block for 20 min and then stained with one of six panels of directly transcribed to cDNA, amplified, and prepared as sequencing libraries
conjugated antibodies for 30 min at the manufacturers recommended as previously described45. Libraries were sequenced on a NextSeq 500
concentration: anti-human CD16 (BD 558122), CD123 (BD 560826), (Illumina).
CCR3 (R&D FAB155F), ITGB7 (BD 551082), CD3 (BD 555341), CD14 (Invit-
rogen MHCD1406), CD19 (BD 555414), and CD56 (BD 555517) (basophils, Immunohistochemistry
neutrophils and eosinophils); anti-human CD16 (BD 558122), CD14 (BD Mouse and human lungs were collected as previously described25,46.
347497), CD4 (BD 340443), CD3 (BD 555341), CD8 (BD 555368), CD19 After inflation, lungs were removed en bloc, fixed in 4% paraformalde-
(BD 555414), and CD56 (BD 555517) (classical and nonclassical mono- hyde (PFA) overnight at 4 °C with gentle rocking, then cryo-embedded
cytes); anti-human CD16 (BD 558122), CD1c (Miltenyi Biotec 130-098- in Optimal Cutting Temperature compound (OCT, Sakura) and sec-
007), CD11c (BD 340544), CCR3 (R&D FAB155F), CD123 (BD 560826), tioned using a cryostat (Leica) onto Superfrost Plus Microscope Slides
HLA-DR (BD 335796), CD3 (BD 555341), CD4 (BD 555348), CD8 (BD (Fisherbrand). Immunohistochemistry was performed using primary
555368), CD14 (Invitrogen MHCD1406), CD19 (BD 555414), and CD56 antibodies raised against the following antigens and used at the indi-
(BD 555517) (pDCs, mDCs, CD16+ dendritic cells); anti-human IgM/IgD cated dilutions to stain slides overnight at 4 °C: anti-proSP-C (rabbit,
(BD 555778), CD19 (BD 557835), CD27 (BD 558664), CD20 (BD 335794), Chemicon AB3786, 1:250 dilution), HES1 (rabbit, Cell Signaling 11988S
CD3 (BD 555341), CD4 (BD 555348), CD14 (Invitrogen MHCD1406), and clone D6P2U, 1:100), MUC-1 (hamster, Thermo Scientific HM1630, clone
CD56 (BD 555517) (B cells); anti-human CD16 (BD 558122), CD57 (BD MH1, 1:250), Ki67 (rat, DAKO M7249 clone MIB-1, 1:100), and keratin-5
347393), CD56 (BD 557747), CD3 (BD 555341), CD4 (BD 555348), CD14 (chicken, Biolegend 905901, 1:100). Primary antibodies were detected
(Invitrogen MHCD1406), and CD19 (BD 555414) (natural killer cells); and with Alexa Fluor-conjugated secondary antibodies (Jackson Immu-
anti-human CD45RA (Biolegend 304118), CCR7 (R&D FAB197F), CD62L noResearch) unless otherwise noted, then mounted in Vectashield
(BD 555544), CD45RO (BD Pharmingen 560608), CD4 (BD 340443), CD8 containing DAPI (5 μg ml−1, Vector labs). Images were acquired with a
(BD 340584), CD11b (BD 555389), CD14 (Invitrogen MHCD1406), CD19 laser scanning confocal fluorescence microscope (Zeiss LSM780) and
(BD 555414), CD56 (BD 555517) (T cells). Cells were washed with FACS processed with Fiji (v.2.0) and Imaris (v.9.2.0, Oxford Instruments).
buffer twice, incubated with the viability marker propidium iodide and Immunostaining experiments were performed on at least two human
loaded onto a BD FACSAria II cell sorter. Approximately 40,000 cells or mouse participants distinct from the donors used for sequencing,
from 21 canonical immune populations (Supplementary Table 3) were and quantifications were based on at least 10 fields of view in each.
sorted in duplicate into Trizol LS (Invitrogen 10296010).
After sorting, all plates and samples were quickly sealed, vortexed, Single molecule in situ hybridization
spun down for 1 min at 1,000g and then snap frozen on dry ice and Samples were fixed in either 10% neutral buffered formalin, dehy-
stored at −80 °C until cDNA synthesis. drated with ethanol and embedded in paraffin wax or fixed in 4%
paraformaldehyde and embedded in OCT compound. Sections from
Single-cell mRNA sequencing paraffin (5 μm) and OCT (20 μm) blocks were processed using stand-
mRNA from single cells sorted from human and mouse lungs and human ard pre-treatment conditions for each per the RNAscope multiplex
blood into lysis plates was reverse transcribed to cDNA and amplified fluorescent reagent kit version 2 (Advanced Cell Diagnostics) assay
as previously described2. Illumina sequencing libraries for cDNA from protocol. TSA-plus fluorescein, Cy3 and Cy5 fluorophores were used
single cells were prepared as previously described2. In brief, cDNA librar- at 1:500 dilution. Micrographs were acquired with a laser scanning
ies were prepared using the Nextera XT Library Sample Preparation kit confocal fluorescence microscope (Zeiss LSM780) and processed
(Illumina, FC-131-1096). Nextera tagmentation DNA buffer (Illumina) with ImageJ and Imaris (version 9.2.0, Oxford Instruments). smFISH
and Tn5 enzyme (Illumina) were added, and the sample was incubated experiments were performed on at least two human or mouse par-
at 55 °C for 10 min. The reaction was neutralized by adding Neutralize ticipants distinct from the donors used for sequencing, and quanti-
Tagment Buffer (Illumina) and centrifuging at room temperature at fications were based on at least 10 fields of view in each. For smFISH,
3,220g for 5 min. Mouse samples were then indexed via PCR by adding fields of view were scored manually, calling a cell positive for each
i5 indexing primer, i7 indexing primer, and Nextera NPM mix (Illu- gene probed if its nucleus had at least three associated expression
mina). Human samples were similarly indexed via PCR using custom, puncta. Proprietary (Advanced Cell Diagnostics) probes used were:
dual-unique indexing primers (IDT)2. KRT5 (547901-C2), SERPINB3 (828601-C3), SFTPC (452561-C2), WIF1
Following library preparation, wells of each library plate were pooled (429391), CLDN5 (517141-C2, 517141-C3), MYC (311761-C3), ACKR1
using a Mosquito liquid handler (TTP Labtech), then purified twice (525131, 525131-C2), COL1A2 (432721), GPC3 (418091-C2), SERPINF1
using 0.7x AMPure beads (Fisher A63881). Library pool quality was (564391-C3), C20rf85 (560841-C3), DHRS9 (467261), GJA5 (471431),
assessed by capillary electrophoresis on a Tapestation system (Agilent) CCL21 (474371-C2), COX4I2 (570351-C3), APOE (433091-C2), ACGT2
with either a high sensitivity or normal D5000 ScreenTape assay kit (828611-C2), ASPN (404481), IGSF21 (572181-C3), GPR34 (521021),
(Agilent) or Fragment analyser (AATI), and library cDNA concentrations EREG (313081), GPR183 (458801-C2), TREM2 (420491-C3), CHI3L1
were quantified by qPCR (Kapa Biosystems KK4923) on a CFX96 Touch (408121), MYRF (499261), AGER (470121-C3), TBX5 (564041), KCNK3
Real-Time PCR Detection System (Biorad). Plate pools were normalized (536851), ACVRL1 (559221), SERPINA1 (435441), HHIP (464811), SLC7A10
and combined equally to make each sequencing sample pool. A PhiX (497081-C2), FGFR4 (443511), PI16 (451311-C2), SERPINF1 (310731),

Article
HHIP (448441-C3), SFTPC (314101-C2), NKX2-1 (434721-C3), and MYRF expression of these marker genes. Pearson correlations were calculated
(524061). between the average expression profiles from each immune cluster for
all cells in the SS2 with the average bulk profiles using the ‘cor’ function
Sequencing read alignments and quality control in R. There were no clusters that lacked expression of canonical marker
Reads from single cells isolated using 10x chromium were demulti- genes. When two or more clusters were assigned the same identity, we
plexed and then aligned to the GRCh38.p12 human reference (from first determined whether their tissue locations differed substantially
10x Genomics) using Cell Ranger (version 2.0, 10x Genomics). Cells (for example, proximal versus distal, alveolar versus adventitial) and
with fewer than 500 genes detected or 1,000 UMIs were excluded from prepended these locations when applicable. When both clusters local-
further analyses. ized to the same tissue region (for example, capillary endothelial cells
Reads from single cells isolated by flow cytometry were demulti- or AT2 cells), we next compared their differentially expressed genes
plexed using bcl2fastq (v.2.19.0.316, Illumina), pruned for low nucleo- head-to-head to identify differences in molecular functions. These
tide quality scores and adaptor sequences using skewer (v.0.2.2), and functional differences were also prepended, when applicable (for exam-
aligned to either (depending on organism) the GRCh38.p12 human ple, signalling AT2 versus AT2, proliferating basal versus basal). If the
reference genome with both the gencode-vH29 and NCBI-108 annota- clusters could not be resolved by location or function, we prepended
tions or the GRCm38.p6 mouse reference genome with the NCBI-106 a representative marker gene to their ‘canonical’ identity (for example,
annotation (with fluorescent genes mEGFP, tdTomato, and ZsGreen1 IGSF21+ dendritic, EREG+ dendritic, and TREM2+ dendritic). Cells from
supplemented) using STAR (v.2.6.1d) in two-pass mapping mode, in different subjects with the same annotation were merged into a single
which the first pass identifies novel splice junctions and the second group for all downstream analyses.
pass aligns reads after rebuilding the genome index with the novel Approximately 35,000 mouse lung and blood cell expression profiles
junctions. The number of reads mapping to each annotated gene were by SS2 and 10x from Tabula Muris Senis2 were combined with 522 cells
calculated by STAR during the second pass alignment, and cells with isolated from Axin2-Cre-ERT2> Rosa26mTmG (A.N.N.) and Tbx4-LME-Cre
fewer than 500 genes detected or 50,000 mapped reads were excluded > Rosa26ZsGreen1 (K.J.T.) mice and amplified by SS2. Cells were strati-
from later analyses. Reads from mRNA sequencing of canonical immune fied by technology (10x versus SS2), re-clustered and re-annotated
populations were demultiplexed, aligned and quantified using the using the strategy described above for human lung cells.
same pipeline.
Re-annotation of existing human lung single cell RNA
Cell clustering, doublet calling, and annotation sequencing datasets
Expression profiles of cells from different subjects and different cap- UMI tables were obtained from the Gene Expression Omnibus
ture approaches (10x and SS2) were clustered separately using the R (GSE122960 for ref. 18, GSE130148 for ref. 19), clustered, and annotated
software package Seurat (v.2.3)47. In brief, counts (SS2) and UMIs (10x) using the strategy described above. New annotations for each cell are
were normalized across cells, scaled per million (SS2) or per 10,000 available on GitHub (see below).
(10x), and converted to log scale using the ‘NormalizeData’ function.
These values were converted to z-scores using the ‘ScaleData’ command Cell type pairwise correlations
and highly variable genes were selected with the ‘FindVariableGenes’ We obtained average expression profiles for each cell type from all cells
function with a dispersion cutoff of 0.5. Principle components were in the 10x dataset, supplemented with the average expression profile
calculated for these selected genes and then projected onto all other from neutrophils in the SS2 dataset, and calculated pairwise Pearson
genes with the ‘RunPCA’ and ‘ProjectPCA’ commands. Clusters of similar correlation coefficients using the ‘cor’ function in R.
cells were detected using the Louvain method for community detec-
tion including only biologically meaningful principle components (see Identification of proliferation signature
below) to construct the shared nearest neighbour map and an empiri- Expression profiles from matched proliferating and quiescent cell
cally set resolution, as implemented in the ‘FindClusters’ function. types were compared head-to-head using the ‘MAST’ statistical
When clustering all cells from a single subject at once, we found that framework implemented in the ‘FindMarkers’ command in Seurat.
the first principal components defining heterogeneity represented dif- Differentially-expressed genes common in each proliferating cell type
ferences in tissue compartment, but some cell types within a compart- were converted to z-scores using the ‘ScaleData’ command in Seurat,
ment (for example, basal, goblet club, neuroendocrine and ionocyte) and summed to create a proliferation score for each cell in the 10x
had a tendency to co-cluster. Clusters were therefore grouped based dataset.
on expression of tissue compartment markers (for example, EPCAM,
CLDN5, COL1A2 and PTPRC) using the ‘SubsetData’ command and the Identification of immune egression signatures
same procedure (from ‘ScaleData’ onwards) was applied iteratively to Blood and tissue expression profiles for each immune cell type
each tissue compartment until the markers enriched in identified clus- were compared head-to-head using the ‘MAST’ statistical frame-
ters, identified using the ‘MAST’ statistical framework48 implemented work implemented in the ‘FindMarkers’ command in Seurat.
in the ‘FindMarkers’ command, were no longer biologically meaningful Differentially-expressed genes common in each subject were screened
(for example, clusters distinguished by dissociation-induced genes30, for dissociation artefact and contamination by red blood cells. Genes
ribosomal genes, mitochondrial genes, or ambient RNA released by specific to tissue immune cells were binned based on their breadth
abundant cells such as RBCs31). Doublets were identified by searching of expression (lymphocyte, myeloid or both), converted to z-scores
for cells with substantial and coherent expression profiles from two using the ‘ScaleData’ command in Seurat, and summed to create an
or more tissue compartments and/or cell types. egression score for each cell in the 10x dataset.
To assign clusters identities, we first compiled a list of all established
lung cell types, their abundances, their classical markers, and any RNA Identification of enriched marker genes, transcription factors,
markers (when available) (Supplementary Table 1). RNA markers for and disease genes
canonical immune populations (Supplementary Table 3) were obtained Differentially expressed genes for each annotated cell type relative to
from bulk mRNA sequencing by correlating the average expression the other cells within its tissue compartment were identified using the
(each captured in duplicate) with a test vector where the target popu- ‘FindMarkers’ command in Seurat with the ‘MAST’ statistical framework
lation position equaled 10 and all others equaled 0 (see GitHub for after downsampling each cell type to 100 (SS2) or 500 (10x) cells. To
details). Clusters were assigned a canonical identity based on enriched obtain the most sensitive and specific markers for each cell type, we

ranked enriched genes, with a P value less than 10−5 and a sensitivity both positive and negative; and type 1 if elements were either positive
greater than 0.4, by their Matthews correlation coefficients (MCCs) or negative and 0.
calculated for each cell type from all cells in the 10x data set (numbers
available in Supplementary Table 2). To measure the utility of using Statistics and reproducibility
multiple markers in assigning cell identities, we calculated MCC scores All heat maps and plots with single cell expression data include every
for all possible combinations of each cell type’s top five marker genes. cell from indicated types (numbers available in Supplementary Table
Enriched genes were annotated as transcription factors or genes 2 for human and Supplementary Table 6 for mouse) for sequencing
associated with pulmonary pathology based on lists compiled from technology specified (SS2 or 10x), unless otherwise stated. Scatter
The Animal Transcription Factor Database (http://bioinfo.life.hust.edu. plots were generated with ggplot2’s ‘geom_point’ function. Dot plots
cn/AnimalTFDB), The Online Mendelian Inheritance in Man Catalog were generated using a modified version of Seurat’s ‘DotPlot’ function
(OMIM)49, and Genome Wide Association Studies (GWAS) obtained (available on GitHub). Violin plots were created with Seurat’s ‘VlnPlot’
from the EMBL-EBI Catalog50 (EFO IDs 0000270, 0000341, 0000464, function and show proportion of single cells at indicated expression
0000571, 0000702, 0000707, 0000708, 0000768, 0001071, levels. Box-and-whisker plots were generated with ggplot2’s ‘geom_box-
0003060, 0003106, 0004244, 0004312, 0004313, 0004314, 0004647, plot’ function; lower and upper hinges correspond to first and third
0004713, 0004806, 0004829, 0005220, 0005297, 0006505, 0006953, quartiles, whiskers extend from hinge to the largest or smallest value
0007627, 0007744, 0007944, 0008431, 0009369, 0009370; GO IDs no further than 1.5 times the interquartile range. Data beyond whiskers
0031427, 0097366; Orphanet IDs 586 182098; log(p-value) < -20, sta- are shown as outlying points. Correlations use Pearson’s coefficient.
tistical tests vary in indicated studies). Viral entry genes were obtained Differentially expressed genes were identified using the ‘MAST’ sta-
from Gene Ontology (GO:0046718) and then curated and associated tistical framework48 implemented in Seurat’s ‘FindMarkers’ function.
with their cognate virus(es) based on literature citations available in Immunostaining and smFISH experiments were performed on at least
our GitHub repository. 2 human or mouse subjects distinct from the donors used for sequenc-
ing, and quantifications were based on at least 10 fields of view in each.
Cellular interaction and hormone target mapping For smFISH, fields of view were scored manually, calling a cell positive
Interactions between cell types were predicted using CellPhoneDB for each gene probed if its nucleus had at least three associated expres-
(‘statistical_analysis’ method) with all cells in the SS2 dataset, as previ- sion puncta. No statistical methods were used to predetermine sample
ously described6. For our targeted analyses, we curated the chemokine size. The experiments were not randomized and investigators were not
receptor-ligand interaction map and list of hormone receptors from an blinded to allocation during experiments and outcome assessment.
extensive literature search (available on GitHub, see below).
Reporting summary
Human and mouse gene alignment, cell type correlation, and Further information on research design is available in the Nature
gene expression comparisons Research Reporting Summary linked to this paper.
The gene expression matrices from our human SS2 cells and the Tabula
Muris Senis SS2 cells, supplemented with the 522 mouse cells from
Data availability
Axin2-creER > mTmG and Tbx4-Cre > ZsGreen1 described above, were col-
lapsed to HomologyIDs obtained from the Mouse Genome Informatics Counts/UMI tables, cellular metadata, Seurat objects, and
database to enable direct comparison. We obtained mean expression scanpy objects are available on Synapse (https://www.synapse.
profiles for each cell type from all cells in the SS2 dataset and calcu- org/#!Synapse:syn21041850). The data can be explored in a browser
lated pairwise Pearson correlation coefficients using the ‘cor’ function using cellxgene at https://hlca.ds.czbiohub.org/. Human sequenc-
in R. We defined species-specific gene expression as those enriched ing data are available by data access agreement on the European
20-fold in either direction (mouse > human or human > mouse) with a Genome-phenome Archive (EGA) under accession EGAS00001004344.
P value less than 10−5 (calculated by ‘MAST’ as above) from all cells for Use of human sequencing data are restricted to not for profit research
the indicated types in the SS2 dataset. Correlations and age-specific only and requires approval or a waiver from requesting investigator’s
genes were obtained the same manner using all cells from 3-month and institutional review board. Mouse sequencing data are available on
24-month in the combined SS2 mouse dat set. the National Institute of Health’s Sequence Read Archive (SRA) under
To compare the expression pattern of each gene across species we BioProject accession PRJNA632939. Source data are provided with
binarized genes as expressed (1) or not expressed (0) in each cell type’s this paper.
average expression profile calculated from all mouse and human SS2
cells of the types compared above. A cell type ‘expressed’ a gene if the
Code availability
median of that gene’s non-zero expression values across the constitu-
ent cells was greater than the median of every non-zero expression The code for demultiplexing counts/UMI tables, clustering, annotation,
value for all other genes plus or minus two standard deviations (varied downstream analyses, and obtaining source data/generating figures
in 0.25 increments) and if the percentage of cells within the cell type that include single-cell expression data are available on GitHub (https://
with non-zero expression values was greater than the median percent github.com/krasnowlab/HLCA).
of non-zero expression values for all other genes plus or minus two
standard decisions (varied in 0.25 increments). These cutoffs were var-
40. Tabula Muris Consortium. A single cell transcriptomic atlas characterizes aging tissues in
ied independently to ensure genes were robustly categorized. We then the mouse. Nature 583, 590–595 (2019).
ordered these gene vectors to match homologous cell types between 41. van Amerongen, R., Bowman, A. N. & Nusse, R. Developmental stage and time dictate the
fate of Wnt/β-catenin-responsive stem cells in the mammary gland. Cell Stem Cell 11,
species with at least five cells and combined them to a single vector
387–400 (2012).
for each gene (V = (a − b) + 2ab, in which a is the ordered human vector 42. Greif, D. M. et al. Radial construction of an arterial wall. Dev. Cell 23, 482–493 (2012).
and b is the ordered mouse vector) that indicated for each cell type 43. Muzumdar, M. D., Tasic, B., Miyamichi, K., Li, L. & Luo, L. A global double-fluorescent Cre
reporter mouse. Genesis 45, 593–605 (2007).
whether: Both mouse and human expressed the gene (2), only human
44. Madisen, L. et al. A robust and high-throughput Cre reporting and characterization
(1), only mouse (−1), or neither (0). We then classified genes by the fol- system for the whole mouse brain. Nat. Neurosci. 13, 133–140 (2010).
lowing: conserved if any element of V equaled 2 and all other elements 45. Moraga, I. et al. Tuning cytokine receptor signaling by re-orienting dimer geometry with
surrogate ligands. Cell 160, 1196–1208 (2015).
equaled 0; type 2 if any element equaled 2 and any other equaled 1 or
46. Desai, T. J., Brownfield, D. G. & Krasnow, M. A. Alveolar progenitor and stem cells in lung
−1; not expressed if all elements equaled 0; type 3 if elements were development, renewal and cancer. Nature 507, 190–194 (2014).

Article
47. Butler, A. et al. Integrating single-cell transcriptomic data across different conditions, Mildred Berg Stanford Graduate Fellowship. M.A.K. is an investigator of the Howard Hughes
technologies, and species. Nat. Biotechnol. 36, 411–420 (2018). Medical Institute.
48. Finak, G. et al. MAST: a flexible statistical framework for assessing transcriptional changes
and characterizing heterogeneity in single-cell RNA sequencing data. Genome Biol. 16,
Author contributions K.J.T., A.N.N., L.P., R.S., A.G., C.S.K., R.J.M. and M.A.K. conceived the
278 (2015).
project and designed the lung and blood cell isolation strategy, J.B.S. and C.S.K. designed
49. Amberger, J. S. et al. OMIM.org: Online Mendelian Inheritance in Man (OMIM), an online
clinical protocols, reviewed clinical histories and coordinated patient care teams to obtain
catalog of human genes and genetic disorders. Nucleic Acids Res. 43, D789–D798 (2014).
profiled tissues, G.B. provided expert clinical evaluation and micrographs of donor tissue
50. Buniello, A. et al. The NHGRI-EBI GWAS Catalog of published genome-wide association
histology, K.J.T., A.N.N., R.S. and A.G. processed tissue to single-cell suspensions, K.J.T., A.N.N.,
studies, targeted arrays and summary statistics 2019. Nucleic Acids Res. 47 (D1), D1005–
L.P. A.G., R.S. and S.D.C. sorted cells for SS2, A.N.N., L.P., S.C. and R.V.S. prepared sequencing
D1012 (2019).
libraries, and K.J.T., R.V.S. and L.P. processed and aligned sequencing data. R.S., J.S. and Y.M.
performed and supervised bulk mRNA sequencing on defined immune populations. K.J.T.,
Acknowledgements We are grateful to the tissue donors and the clinical staff at Stanford A.N.N., R.S. A.G. and R.J.M. provided tissue expertise and annotated cell types. K.J.T., A.N.N.
Medical Center who made tissue collection possible, especially J. Benson and E. Chen. We are and M.A.K. designed and implemented bioinformatic methods and interpreted results. K.J.T.,
especially grateful to Jim Spudich who spurred this study. We also thank the Stanford Shared A.N.N. and A.G. performed follow up stains. M.A.K., S.R.Q., N.F.N., I.L.W., C.S.K. and R.J.M.
FACS Facility for their expertise and sorting services, especially L. Nichols and M. Weglarz; supervised and supported the work. K.J.T., A.N.N. and M.A.K. wrote the manuscript, and all
members of Chan Zuckerberg Biohub and Quake laboratory who supported this work, authors reviewed and edited the manuscript.
particularly A. McGeever, B.Yu, B. Jones and S. Kolluru; M. Kumar for discussions on annotation
of stromal cells; and M. Petersen for illustrating the lung schematic (Fig. 1b) and C. Kao for help Competing interests The authors declare no competing interests.
with figure formatting. Some computing for this project was performed on the Sherlock
cluster; we thank Stanford University and the Stanford Research Computing Center for Additional information
providing computational resources and support that contributed to the results. We thank Supplementary information is available for this paper at https://doi.org/10.1038/s41586-020-
J. Spudich and members of the Krasnow laboratory for discussions and comments on the 2922-4.
manuscript, and A. Lozano for discussions on bioinformatic analyses. This work was supported Correspondence and requests for materials should be addressed to S.R.Q. or M.A.K.
by funding from the Chan Zuckerberg Biohub (S.R.Q.), the Howard Hughes Medical Institute, Peer review information Nature thanks Shalev Itzkovitz and the other, anonymous, reviewer(s)
National Institutes of Health, and the Vera Moulton Wall Center for Pulmonary Vascular Disease for their contribution to the peer review of this work.
(M.A.K.), and the Ludwig Cancer Center at Stanford (I.L.W.). K.J.T was supported by a Paul and Reprints and permissions information is available at http://www.nature.com/reprints.

Extended Data Fig. 1 | See next page for caption.

Article
Extended Data Fig. 1 | Strategy for scRNA-seq and annotation of human COL1A2 (green), and PTPRC (purple)), as shown for t-distributed stochastic
lung and blood cells. a, Workflow for capture and mRNA sequencing of single neighbour embedding (t-SNE) plot of lung and blood cell expression profiles
cells from the healthy unaffected regions indicated (D, distal; M, medial; P, obtained by 10x from participant 3. Cells from each tissue compartment were
proximal lung tissue; see d) of fresh, surgically resected lungs with focal then iteratively re-clustered until differentially-expressed genes driving
tumours from three participants (1, 2 and 3) and their matched peripheral clustering were no longer biologically meaningful. Cell cluster annotation was
blood. Cell representation was balanced among the major tissue based on expression of canonical marker genes from the literature, markers
compartments (endothelial, immune, epithelial and stroma) by magnetic and found through RNA sequencing of purified cell populations (bulk RNA
fluorescence activated cell sorting (MACS and FACS) using antibodies for the markers), ascertained tissue location, and inferred molecular function from
indicated surface markers (CD31, CD45, EPCAM). Cell capture and scRNA-seq differentially-expressed genes. c, Heat map of pairwise Pearson correlations of
was done using 10x droplet technology or SS2 analysis of plate-sorted cells. the average expression profile of each cluster in the combined 10x dataset
Number of profiled cells from each compartment are shown in parentheses. plus SS2 analysis of neutrophils. n values are in Supplementary Table 2. Tissue
For blood, immune cells were isolated on a high density Ficoll gradient, and compartment and identification number of each of the 58 clusters are
unsorted cells profiled by 10x and sorted cells (using canonical markers for the indicated. For more details on statistics and reproducibility, see Methods.
indicated immune populations) by SS2. Total cell number (all three d, Representative micrographs of donor lungs from formalin-fixed, paraffin-
participants) and median number of expressed genes per cell are indicated for embedded sections stained with haematoxylin and eosin showing bronchi,
each method. b, Cell clustering and annotation pipeline. Cell expression bronchioles, submucosal glands, arteries, veins and alveoli near regions used
profiles were computationally clustered by nearest-neighbour relationships for scRNA-seq. Staining repeated on at least five sections (encompassing
and clusters were then separated into tissue compartments based on different anatomical regions) from each participant used for scRNA-seq. Scale
expression of compartment-specific markers (EPCAM (blue), CLDN5 (red), bar, 100 μm.

Extended Data Fig. 2 | See next page for caption.

Article
Extended Data Fig. 2 | Selectively expressed RNA markers of human profiles of human blood immune cells in the SS2 dataset annotated by
immune cell types from bulk mRNA sequencing of FACS-purified immune canonical markers and enriched RNA markers from the bulk RNA-seq analysis.
cells. a, Heat map of RNA expression of the most selectively-expressed The highest correlation in overall gene expression (white dot) of each
genes from bulk mRNA sequencing of the indicated FACS-sorted immune annotated immune cell cluster in the SS2 dataset (columns) was to the bulk
populations (Supplementary Table 3). This dataset provided RNA markers for RNA-seq of the same FACS-purified immune population (rows), supporting the
human immune cell populations that have been classically defined by their cell scRNA-seq immune cluster annotations (red squares). Cell numbers are
surface markers. b, Heat map of pairwise Pearson correlation scores between in Supplementary Table 2. For more details on statistics and reproducibility,
the average expression profiles of the immune cell types indicated that were see Methods.
obtained from bulk mRNA sequencing (BulkSeq, a) to the average scRNA-seq

Extended Data Fig. 3 | See next page for caption.

Article
Extended Data Fig. 3 | Expression differences and localization of lung cell 467, 2,095, 434, 198 and 28. f, RNAscope smFISH and quantification for general
states and canonical epithelial and endothelial subtypes. a, Proliferative basal marker KRT5 (red) and proximal basal cell marker SERPINB3 (white) with
signature score (based on expression of indicated genes in cells from 10x DAPI counter stain (blue) and ECM autofluorescence (green) on proximal,
dataset; cell numbers are in Supplementary Table 2) of each cluster of basal pseudostratified bronchi and distal, simple bronchioles. Scale bars, 20 μm
cells, T and natural killer cells, and macrophages. Three clusters had high (inset, 10 μm). Note enrichment of proximal basal cells (KRT5 SERPINB3 double
scores: proliferating basal cells (Bas-p), proliferating natural killer/T cells (NK/ positive, yellow arrowhead and box) enrichment at base of pseudostratified
T-p), and proliferating macrophages. b, Dot plot of mean level of expression airways. SERPINB3 was not detected in simple airways, indicating that basal
(dot intensity, grey scale) of indicated basal cell markers and percent of cells in cells (but not proximal basal cells) are present there. Staining repeated on two
population with detected expression (dot size) for 10x dataset. Note partial participants. g, Dot plot of expression in ciliated and proximal ciliated cells of
overlap of markers among different basal populations. c, Immunostaining of canonical (general) ciliated cell markers and specific proximal ciliated markers
adult human pseudostratified airway for differentiation marker HES1 (green) in (in 10x dataset). h, smFISH and quantification of human pseudostratified
basal cells (marked by KRT5, red) with DAPI (nuclear) counter stain (blue). epithelial (left) and simple epithelial (right) airways for general ciliated marker
Scale bars, 10 μm. Note apical processes extending from HES1+ basal cells C20orf85 (white) and proximal ciliated marker DHRS9 (red) with DAPI
(arrowheads) indicating migration away from basal lamina as they counterstain (blue) and ECM autofluorescence (green). Note restriction of
differentiate. Other HES1+ cells have turned off basal marker KRT5. Dashed proximal ciliated cells to pseudostratified airways. Scale bars, 10 μm. Staining
outlines, basal cell nuclei. Quantification shows fraction of basal cells (cuboidal repeated on two particpants. i, Heat map of expression of representative
KRT5+ cells on basement membrane) and differentiating basal (Bas-d) cells general AT2, AT2 selective, and AT2-signalling selective marker genes in AT2
(KRT5+ cells with apical processes) that were HES1+. n denotes KRT5+ cells and AT2-signalling human lung cells (SS2 data). AT2 selective markers include
scored in sections of two human lungs with staining repeated on four negative regulators of Hedgehog and Wnt signalling pathways (for example,
participants. d, Immunostaining of adult human pseudostratified airway for HHIP and WIF1, highlighted red) and AT2-signalling selective markers include
proliferation marker MKI67 (green) in basal cells (marked by KRT5, red) with Wnt ligands, receptors and transcription factors (for example, WNT5A, LRP5
DAPI counter stain (blue). Scale bars, 5 μm. Quantification shows abundance of and TFC7L2 highlighted green). Values shown are ln(CPM + 1) for 50 randomly
proliferating (MKI67-expressing) basal cells in pseudostratified (pseudo) and selected cells in each cluster (SS2 data). j, Dot plot of expression of endothelial
simple epithelial airways; n denotes KRT5+ cells scored in sections of two markers (10x dataset). k, Micrograph (low magnification, left) of bronchial
human lungs with staining repeated on four participants. e, Relative vessel (boxed region) showing vessel location near airway (dotted outline).
abundance of epithelial and stromal cell types in scRNA-seq analysis of human smFISH for general endothelial marker CLDN5 (red, centre), bronchial vessel-
lung samples obtained from proximal (blue; 10x cells from P3) and distal (red; specific markers MYC (green) and Bro1-specific marker ACKR1 (red, right) on
10x cells from D1a, D1b, D2, D3) lung sites. In addition to the expected proximal serial sections of bronchial vessel cells (arrowheads), co-stained for DAPI
enrichment of some airway cell types (goblet cells, ionocytes, neuroendocrine (blue). Scale bar, 10 μm. Quantification shows relative abundance of Bro1 and
cells) and distal enrichment of alveolar cell types (AT1, AT2, AT2-signalling, Bro2 cells. Staining repeated on two participants. l–n, smFISH and
myofibroblasts), note three bracketed pairs of related cell types (ciliated and quantification of vessel types indicated (dotted outlines) showing vein marker
proximal ciliated; basal and proximal basal (Bas-px) cells; myofibroblasts and ACKR1 (red; l), artery marker GJA5 (red; m), lymphatic marker CCL21 (red; n), and
fibromyocytes) with one of them proximally enriched. Relative enrichment general endothelial marker CLDN5 with DAPI counter stain (blue) and ECM
values are provisional because they can be influenced by efficiency of autofluorescence (green). Scale bars, 50 μm (l), 30 μm (m) and 40 μm (n).
collection during cell dissociation and isolation. Cell number for proximal cells Staining repeated on two participants. For more details on statistics and
are (from left to right): 357, 275, 73, 175, 153, 191, 39, 145, 57, 24, 20, 10, 328, 1,505, reproducibility, see Methods.
235, 25 and 70; and for distal cells are: 537, 806, 15, 197, 4, 58, 6, 14, 336, 0, 2, 1,

Extended Data Fig. 4 | See next page for caption.

Article
Extended Data Fig. 4 | Markers and lung localization of stromal and airway smooth muscle (yellow box) cells. Fibromyocytes (white arrowheads)
dendritic subtypes. a–d, smFISH for RNA of indicated marker genes of and airway smooth muscle (yellow arrowheads) are intermingled in wall of
alveolar fibroblasts (a, b) and adventitial fibroblasts (c, d) in adult human (a, c) pseudostratified airway (dotted outline). Staining repeated on two
and mouse (b, e) alveolar (a, b) and pulmonary artery (c, d) sections. ECM participants. h, i, smFISH of human alveolar sections probed for general
autofluorescence (green; a, c) to show blood vessels; Elastin (green, b, d); DAPI stromal marker COL1A2 (white), pericyte marker COX4I2 (red; h), lipofibroblast
counterstain (blue, all panels). Staining repeated on two human participants or marker APOE (red; i). ECM autofluorescence, green; DAPI counterstain, blue.
three mice. a, smFISH probes: general fibroblast marker COL1A2 (white) and Inset (h), boxed region showing close-up of pericyte. Inset (i), boxed region
alveolar fibroblast-selective marker GPC3 (red). Arrowheads denote alveolar showing close-up of COL1A2 APOE double-positive LipF. LipF cells are
fibroblasts. Inset, close-up of boxed region showing merged (top) and split intermingled among other stromal cells (single-positive COL1A2) and
channels of an alveolar fibroblast. Scale bars, 20 μm (inset 60 μm). b, smFISH macrophages (single-positive APOE). Quantification in Fig. 1f. Scale bars,
probes: alveolar fibroblast-selective markers Slc7a10 (white) and Frfr4 (red). 20 μm. Staining repeated on two participants . j, Dot plot of COX4I2 expression
Elastin (green) shows alveolar entrance ring. Arrowheads denote alveolar in alveolar stromal cell types (10x dataset). k, Heat map of expression of
fibroblasts. Scale bar, 5 μm. c, smFISH probes: general fibroblast marker dendritic cell marker genes in 50 randomly selected cells from indicated
COL1A2 (white) and adventitial fibroblast -selective marker SERPINF1 (red). dendritic cell clusters (human blood and lung 10x datasets). Cells in all clusters
Adventitial fibroblasts (some indicated by arrowheads) localize around blood express general dendritic markers including antigen presenting genes but
vessels (ECM, green). Inset, close-up of boxed region showing merged (top) and each cluster also has its own selective markers. Red highlighted markers
split channels of an adventitial fibroblast. Dashed line denotes the artery distinguishing the newly identified dendritic cell clusters (IGSF21+, EREG+,
boundary. Scale bars, 30 μm (inset 90 μm). d, smFISH probes: adventitial TREM2+) suggest different roles in asthma (IGSF21+), growth factor regulation
fibroblast-selective markers Pi16 (white) and Serpinf1 (red). Adventitial (EREG+), and lipid handling (TREM2+). l–n, smFISH of adult human lung
fibroblasts (arrowheads) surround artery (marked by elastin, green). Scale bar, proximal and alveolar (Alv) sections as indicated probed for IGSF21+ dendritic
10 μm. e, Heat map of expression of representative general, adventitial- cell markers IGSF21 (red) and GPR34 (white) (l), EREG+ dendritic cell marker
selective, and alveolar-selective fibroblast markers in 50 randomly selected EREG (red) and general dendritic cell marker GPR183 (white) (m), and TREM2+
cells from adventitial (left) and alveolar (right) fibroblast clusters (SS2 dataset). dendritic cell markers TREM2 (red) and CHI3L1 (white) (n). DAPI counterstain,
Note specialization (highlighted red) in growth factors (AdvF: PDGFRL, IGFBP4; blue. Non-punctate signal in red channel (l, n) is erythrocyte autofluorescence.
AlvF: FGFR4, VEGFD) and morphogen (AdvF: SFRP2; AlvF: NKD1, DKK3) Insets, boxed regions showing merged and split channels of close-up of single
signalling or regulation. f, g, smFISH and quantification of cell abundance in dendritic cell of indicated type. Scale bars, 20 μm. Arrowheads denote double-
human alveolar (f) and pseudostratified epithelial airway (g) sections probed positive cells. Quantification shows distribution of each dendritic type; note
for myofibroblast and fibromyocyte marker ASPN (red), and for fibromyocyte IGSF21+ and EREG+ dendritic cells show strong proximal enrichment. Staining
and airway smooth muscle markers COX4I2 (white; f) and ACTG2 (white; g). repeated on two participants. o, t-SNE of expression profile clusters of
ECM autofluorescence, green; DAPI counterstain, blue. Inset (f), boxed region monocytes and B, T and natural killer cells (10x dataset, participant 1, 2,622
showing close-up of merged (top) and split channels of ASPN+ COX4I2− cells). Note separate cell clusters of each immune cell type isolated from lung
myofibroblast. Myofibroblasts and fibromyocytes (see below) probably make (no outline) and blood (dashed outline). Asterisk denotes small number of B
up remaining cells in Fig. 1f quantification. Inset (g), boxed regions showing cells isolated from the lung that cluster next to blood B cells. For more details
close-up of merged (top) and split channels of fibromyocyte (white box) and on statistics and reproducibility, see Methods.

Extended Data Fig. 5 | Markers and transcription factors that distinguish selectively expressed in AT1 cells (arrowheads; 97% of MYRF+ cells were AGER+,
human lung cell types. a, Violin plots of expression levels (ln(UP10K + 1)) of the n = 250 scored cells). Inset, boxed region showing merged and split channels of
most sensitive and specific markers (gene symbols) for each human lung cell AT1 cell. Scale bar, 10 μm. Staining repeated on two participants. d, Alveolar
type in its tissue compartment (10x dataset). Cell numbers given section of human lung probed by smFISH for pericyte marker COX4I2 and
in Supplementary Table 2. b, Scheme for selecting the most sensitive and transcription factor TBX5. TBX5 is enriched in pericytes (arrowheads, 92% of
specific marker genes for each cell type using Matthews correlation coefficient TBX5+ cells were COX4I2+, n = 250). Inset, boxed region showing merged and
(MCC). Box-and-whisker plots below show MCCs, true positive rates (TPR), and split channels of pericyte. Scale bar, 5 μm. Staining repeated on two
false discovery rates (FDR) for each cell type (n = 58) using indicated number participants. e, Dot plot of expression of enriched transcription factors in each
(nGene) of the most sensitive and specific markers (10x dataset). Note all lung cell type (SS2 dataset). Red text, genes not previously associated with the
measures saturate at approximately 2–4 genes, hence simultaneous in situ cell type. Red shading, transcription factors including MYRF that are highly
probing of a human lung for the approximately 100–200 optimal markers enriched in AT1 cells, and TBX5 and others highly enriched in pericytes. For
would assign identity to nearly every cell. c, Alveolar section of human lung more details on statistics and reproducibility, see Methods.
probed by smFISH for AT1 marker AGER and transcription factor MYRF. MYRF is

Article
Extended Data Fig. 6 | See next page for caption.

Extended Data Fig. 6 | Lung cell targets of circulating hormones and local preferentially expressed in Cap relative to Cap-a cells. c, Heat maps showing
signals. a, Dot plot of hormone receptor gene expression in lung cells (SS2 number of interactions predicted by CellPhoneDB software between human
dataset). Type and name of cognate hormones for each receptor are shown at lung cell types located in proximal lung regions (left panel in each pair) and
top. Teal, broadly-expressed receptors in lung; other colours, selectively- distal regions (right) based on expression patterns of ligand genes (‘sending
expressed receptors (<3 lung cell types). Small coloured dots next to cell cell’) and their cognate receptor genes (‘receiving cell’) (SS2 dataset). The pair
type names show selectively targeted cell types. AA, amino acid; AM, of heat maps at the top left show values for all predicted signalling interactions
adrenomedullin; CGRP, calcitonin gene-related peptide; EPO, erythropoietin; (‘all interactions’), and other pairs show values for the indicated types of signals
GCCT, glucocorticoid; GH, growth hormone; GIP, gastric inhibitory peptide; (growth factors, cytokines, integrins, WNT, Notch, BMP, FGF and TFGβ).
IGF, insulin-like growth factor; MCCT, mineralocorticoid; RA, retinoic acid; SST, Predicted interactions between cell types range from 0 (lymphocyte signalling
somatostatin. b, Schematic of inferred pericyte cell contractility pathway and to neutrophils) to 136 (AdvF signalling to Cap-i1). Note expected relationships,
its regulation by circulating hormones (AGT, PTH) and capillary expressed such as immune cells expressing integrins to interact with endothelial cells and
signals (EDN, NO). Dots show expression of indicated pathway genes: values at having higher levels of cytokine signalling relative to their global signalling,
left (outlined red) in each pair of dots in capillary diagram (top) show and unexpected relationships, such as fibroblasts expressing most growth
expression in Cap-a cells (aerocytes) and at right (outlined blue) show factors and lack of Notch signalling originating from immune cells. For more
expression in general Cap cells (SS2 dataset). Note most signal genes are details on statistics and reproducibility, see Methods.

Article
Extended Data Fig. 7 | Lung cell expression patterns of genes implicated in association genes ≥ 10−20 significance) and Online Mendelian Inheritance in
lung disease. Dot plots of expression (in SS2 dataset) of 233 lung disease genes Man (OMIM). For more details on statistics and reproducibility, see Methods.
curated from genome-wide association studies (GWAS; genome-wide

Extended Data Fig. 8 | See next page for caption.

Article
Extended Data Fig. 8 | Mapping cellular origins of lung disease by cell- probed for in pulmonary hypertension disease gene KCNK3 (red) and
selective expression of disease genes. a, Dot plots of expression of lung pericyte marker COX4I2 (white) with DAPI counterstain (blue) and ECM
disease genes (numbered, associated disease shown above) enriched in autoflourescence (green). Note pericyte-specific expression (arrowheads, 91%
specific lung cell types (SS2 datasets). Red, novel cell type association of gene of COX4I2+ pericytes were KCNK3+, n = 77). Scale bar, 5 μm. Cell numbers for
or disease; grey, diseases with developmental phenotype. AWS, Alagille– each type given in Supplementary Table 2. d, smFISH of alveolar section of
Watson syndrome; BBS, Bardet–Biedl syndrome; CF, cystic fibrosis; Dys, adult human lung probed for atrioventricular (AV) dysplasia gene ACVRL1 (red),
dysplasia; EDS, Ehlers-Danlos syndrome; Fam Med, familial Mediterranean; IPF, endothelial marker CLDN5 (white) with DAPI counterstain. Note ACVRL1 CLDN5
idiopathic pulmonary fibrosis; PH, pulmonary hypertension; SGB, Simpson- double-positive capillaries (white arrowheads, 70% of CLDN5+ capillaries were
Golabi-Behmel; SM, smooth muscle; SMD, surfactant metabolism dysfunction; ACVRL1+, n = 102) and some CLDN5 single-positive capillaries (yellow
TB, tuberculosis; VDES, Van den Ende-Gupta syndrome. b, Dot plot of arrowheads). Scale bar, 5 μm. e, smFISH of alveolar section of adult human lung
expression (SS2 dataset) of all genes implicated in pulmonary hypertension, probed for COPD or emphysema gene SERPINA1 and AT2 marker SFTPC, and
tuberculosis and COPD or emphysema (OMIM, Mendelian disease genes from DAPI. Note AT2-specific expression (arrowheads; 93% of AT2 cells were
OMIM database; GWAS, genome-wide association genes ≥ 10−20 significance). SERPINA1+, n = 176). Scale bar, 5 μm. For more details on statistics and
Note canonical AT2 cells (red shading) express all and AT2-signalling cells (blue reproducibility, see Methods.
shading) express most. c, smFISH of alveolar section of adult human lung

Extended Data Fig. 9 | Lung cell expression patterns of respiratory virus shading, cell types inhaled viruses can directly access. Doughnut plots (right)
receptors. a, Dot plot showing expression in human lung cell types of entry showing relative number of receptor-expressing cells of cell types viruses can
receptors (indicated at left) for respiratory viruses (indicated at right, numbers directly access (shaded grey in a), normalized by their abundance values
indicate viral families) (SS2 dataset). Red shading, cell types inhaled viruses from Supplementary Table 1 (and refined by the relative abundance values in
could directly access (epithelial cells and macrophages); darker red shading Fig. 1 and Extended Data Figs. 3 and 4). Note prevalence of AT2 alveolar cells for
shows expression values for measles receptor NECTIN4 and rhinovirus C ACE2, receptor for SARS-CoV and SARS-CoV-2, and for DPP4, receptor for
receptor CDHR3. b, Violin plots (left) and dot plots (immediately above violin MERS-CoV, in contrast to prevalence of macrophages for ANPEP, receptor for
plots) showing expression of coronavirus receptors ACE2, DPP4, and ANPEP in common cold causing coronavirus 229E. For more details on statistics and
lung cell types (10x dataset, cell numbers given in Supplementary Table 2). Grey reproducibility, see Methods.

Article
Extended Data Fig. 10 | Lung cell expression patterns of non-respiratory expression of receptors for respiratory viruses). For more details on statistics
virus receptors. Dot plot of expression of entry receptors for non-respiratory and reproducibility, see Methods.
viruses in human lung cell types (compare with Extended Data Fig. 9a showing

Extended Data Fig. 11 | See next page for caption.

Article
Extended Data Fig. 11 | Comparison of mouse and human gene expression White dot denotes human-to-mouse correlation. c, Dot plot of expression of
profiles in homologous lung cell types and across age. a, Scatter plots canonical goblet cell markers MUC5B and MUC5AC and transcription factor
showing median expression levels (ln(CPM + 1)) in indicated cell types of each SPDEF in mouse (left) and human (right) goblet cells. d, Scatter plot showing
expressed human gene and mouse orthologue (mouse and human SS2 average expression levels (dots) across all cells (‘pseudo-bulk’ lung expression)
datasets, human and mouse cell numbers given in Supplementary Tables 2 and of each expressed human gene and mouse orthologue (mouse and human SS2
6, respectively). Note tens to hundreds of genes that show a 20-fold or greater datasets). Scale, ln(CPM + 1). Pearson correlation (R values) between the
expression difference (and P < 0.05, MAST) between species (red dots, gene average mouse and human gene expression profiles are indicated. e, Scatter
names indicated for some and total number given above). Basophil/mast cell 1 plots comparing median expression levels (ln(CPM + 1)) in indicated mouse
(Bas/Ma 1) cells have the most differentially expressed genes (343), and CD4+ lung cell types of each expressed gene at age 3 months (x axis) and 24 months
M/E T cells have the least (79). Pearson correlation scores (R values) between (y axis) in SS2 datasets from Tabula Muris Senis40 (cell numbers given
the average mouse and human gene expression profiles for each cell type are in Supplementary Table 6). Pearson correlation scores between average gene
indicated. ‘Mm()’ and ‘Hs()’ denotes genes in which duplications between expression profile for each cell type at each age are indicated (R values), along
mouse and human were collapsed to HomologyID. b, Heat map showing global with number of genes (red dots) showing 20-fold or greater expression
transcriptome Pearson correlation between indicated human and mouse difference (and P < 0.05, MAST) between ages. Names of some genes are given
epithelial cells (SS2 dataset, human and mouse cell numbers given in next to the corresponding red dot. For more details on statistics and
Supplementary Tables 2 and 6, respectively). Red outline denotes homologous reproducibility, please see Methods.
cell types based on classical markers described in Supplementary Table 6.

Extended Data Fig. 12 | Patterns of conserved and divergent gene those of other Hedgehog pathway genes including ligands (SHH, DHH, IHH),
expression across human and mouse lung cell types. a, Dot plots of PTPRC receptors (PTCH1, PTCH2, SMO), and transducers (GLI1, GLI2, GLI3) (SS2
and MYL6 expression in mouse and human lung cell types (SS2 datasets) datasets). g, Dot plots of expression of serous cell markers LTF, LYZ, BPIFBP1
showing two examples of conserved (type 0) expression pattern. Blue shading, and HP showing switched expression (type 3 change) from mouse airway
homologous cell types with conserved expression. b, Dot plots showing gain of epithelial cells to human serous cells, which mice lack (asterisk). Dot plots of
expression (type 1 change) in several human cell types of RNASE1 (left) and all expression of lipid handling genes APOE, PLIN2 and FST show switched
human cell types of TRIM38 (right). Red shading, cell types with divergent expression (type 3 change) from mouse alveolar stromal cells to human
(gained) expression. c, Alveolar section of adult mouse lung probed by smFISH lipofibroblasts, which mice lack (asterisks). ‘Mm()’ or ‘Hs()’, genes in which
for general alveolar epithelial marker Nkx2-1, AT2 marker Sftpc, and duplications between mouse and human were collapsed to HomologyIDs (10x
transcription factor Myrf. Note Myrf is selectively expressed in mouse AT1 cells and SS2 datasets). h, Pie chart of fraction of expressed genes in lung showing
(Nkx2-1+ Sftpc− cells), as it is in humans (Extended Data Fig. 6c). Scale bar, 5 μm. each of the four types of evolutionary changes in cellular expression patterns
Staining repeated on three mice. d, Dot plots of expression of CGRP and ADM from mouse to human. Histogram below shows number of lung cell types that
hormone receptor genes showing expansion of expression (type 2 change) in the 602 genes with perfectly conserved cellular expression patterns (type 0)
human endothelial cells (10x data sets). e, Dot plots of expression of are expressed in; note that almost all are expressed in either a single cell type
emphysema-associated gene SERPINA1 showing switched expression (type 3 (67%) or nearly all cell types (33%). For more details on statistics and
change) from mouse pericytes (top) to human AT2 cells (bottom) (SS2 reproducibility, see Methods.
datasets). f, Dot plots comparing expression and conservation of HHIP with

1
nature
research
|
reporting
summary
October
2018
Corresponding author(s): Mark Krasnow and Stephen Quake
Last updated by author(s): Nov 5, 2020
Reporting Summary
Nature Research wishes to improve the reproducibility of the work that we publish. This form provides structure for consistency and transparency
in reporting. For further information on Nature Research policies, see Authors & Referees and the Editorial Policy Checklist.
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
Data collection Smart-Seq2 cell capture: Sony SH800S Cell Sorter software v1.8, BD Diva software v8. Smart-Seq2 cDNA synthesis and Library
preparation: Mosquito Liquid Handler software, MANTIS Liquid Handler Control software. Library quality control: Tapestation or
Fragment analyzer software. Microscopy: Zen Black
Data analysis Smart-Seq2 sequence de-multiplexing: bcl2fastq v2.19.0.316. Smart-Seq2 alignment and gene counting: skewer v0.2.2, STAR v2.6.1d.
10x sequence de-multiplexing, alignment, and UMI counting: CellRanger v2.0.1
Filtering, clustering, and annotating cells: Seurat v2.3, R v3.6.3
Microscopy: Imaris v9.2.0, Fiji v2
Flow cytometry: Flowjo v10.5.3
Cell interactions: CellPhoneDB v2.1.2, python v3.7.2
The code for demultiplexing counts/UMI tables, clustering, annotation, downstream analyses, and obtaining source data/generating
figures that include single cell expression data is available on GitHub (https://github.com/krasnowlab/HLCA).
For manuscripts utilizing custom algorithms or software that are central to the research but not yet described in published literature, software must be made available to editors/reviewers.
We strongly encourage code deposition in a community repository (e.g. GitHub). See the Nature Research guidelines for submitting code & software for further information.
Data
Policy information about availability of data
All manuscripts must include a data availability statement. This statement should provide the following information, where applicable:
- Accession codes, unique identifiers, or web links for publicly available datasets
- A list of figures that have associated raw data
- A description of any restrictions on data availability
Counts/UMI tables, cellular metadata, Seurat objects, and scanpy objects are available on Synapse (https://www.synapse.org/#!Synapse:syn21041850). The data
can be explored in a browser using cellxgene at https://hlca.ds.czbiohub.org/. Human sequencing data is available by data access agreement on the European

2
nature
research
|
reporting
summary
October
2018
Genome-phenome Archive (EGA) under accession EGAS00001004344. Use of human sequencing data is restricted to not for profit research only and requires
approval or a waiver from requesting investigator’s institutional review board. Mouse sequencing data is available on the National Institute of Health’s Sequence
Read Archive (SRA) under BioProject accession PRJNA632939. Source data behind immunostaining or smFISH quantification (Figure 1; Extended Data Figures 3 and
4) are available within the manuscript files.
Field-specific reporting
Please select the one below that is the best fit for your research. If you are not sure, read the appropriate sections before making your selection.
Life sciences Behavioural & social sciences Ecological, evolutionary & environmental sciences
For a reference copy of the document with all sections, see nature.com/documents/nr-reporting-summary-flat.pdf
Life sciences study design
All studies must disclose on these points even when the disclosure is negative.
Sample size Single cells were isolated from peripheral blood or surgically resected, unaffected lung tissue from patients undergoing pulmonary
lobectomies for focal tumors. We sampled two distal regions from Patient 1, one distal and one medial region from Patient 2, and a distal,
medial, and proximal region from Patient 3. Sample size was not predetermined. Cell atlas completeness was assessed by the percentage of
canonical lung cell types captured, which was greater than 90% after 3 patients.
Data exclusions Poor quality cells were excluded from clustering using pre-established thresholds for the number of reads (Smart-Seq2 <50000) or UMIs (10x
<1000) and genes (<500) detected.
Doublets were excluded by manual inspection following clustering, looking for evidence of coherent expression profiles from two cell types.
Replication Flow cytometer, single molecule in situ hybridization, and immunohistochemistry experiments were consistent across patient samples or
mice. >80% molecular types were observed in more than one patient either by sequencing or follow up experiments.
Randomization Samples from human and mouse were all considered controls and were not randomized.
Blinding Patients were de-identified and assigned an identifier. Researchers were aware of basic demographic information and relevant medical
history, clinicians were aware of each patient's full history.
Reporting for specific materials, systems and methods
We require information from authors about some types of materials, experimental systems and methods used in many studies. Here, indicate whether each material,
system or method listed is relevant to your study. If you are not sure if a list item applies to your research, read the appropriate section before selecting a response.
Materials & experimental systems Methods
n/a Involved in the study n/a Involved in the study
Antibodies ChIP-seq
Eukaryotic cell lines Flow cytometry
Palaeontology MRI-based neuroimaging
Animals and other organisms
Human research participants
Clinical data
Antibodies
Antibodies used Magnetically conjucated antibodies: anti-human CD45 (Miltenyi 130-045-
801, 1:50 dilution), human EPCAM (Miltenyi 130-061-101, 1:50) and human CD31 (Miltenyi 130-091-935, 1:100).
Fluorescently conjugated antibodies for lung single cell sorting, used at the manufacturers recommended concentration: anti-
human CD45 (Biolegend 304006, clone HI30, https://www.biolegend.com/en-us/products/fitc-anti-human-cd45-antibody-707)
and EPCAM (eBioscience 25-9326-42, clone 1B7, https://www.thermofisher.com/antibody/product/CD326-EpCAM-Antibody-
clone-1B7-Monoclonal/25-9326-42).
Fluorescently conjugated antibodies for immune single cell sorting, used at 1:20 dilution: anti-human CD3
(BD 563548, clone UCHT1, https://www.bdbiosciences.com/us/applications/research/t-cell-immunology/th-1-cells/surface-
markers/human/buv395-mouse-anti-human-cd3-ucht1-also-known-as-ucht-1-ucht-1/p/563548), CD4 (BD 340443, clone SK3,
https://www.bdbiosciences.com/us/applications/research/t-cell-immunology/th-1-cells/surface-markers/human/apc-mouse-
anti-human-cd4-sk3-also-known-as-leu3a/p/340443), CD8 (BD 340692, clone SK1, https://www.bdbiosciences.com/us/
applications/clinical/blood-cell-disorders/asr-reagents/cd8-fitc-sk1/p/340692), CD14 (BD 557831, clone MPP9, https://
www.bdbiosciences.com/eu/applications/research/stem-cell-research/hematopoietic-stem-cell-markers/human/negative-

3
nature
research
|
reporting
summary
October
2018
markers/apc-cy7-mouse-anti-human-cd14-mp9-also-known-as-mp-9/p/557831), CD19 (Biolegend 302234, clone HIB19, https://
www.biolegend.com/en-us/products/brilliant-violet-421-anti-human-cd19-antibody-7144), CD47 (BD 563761, clone B6H12,
https://www.bdbiosciences.com/eu/applications/research/stem-cell-research/cancer-research/human/bv711-mouse-anti-
human-cd47-b6h12/p/563761), CD56 (BD 555516, clone B159, https://www.bdbiosciences.com/us/applications/research/stem-
cell-research/hematopoietic-stem-cell-markers/human/negative-markers/pe-mouse-anti-human-cd56-b159/p/555516), and
CD235a (BD 559944, clone GA-R2, https://www.bdbiosciences.com/us/reagents/research/antibodies-buffers/immunology-
reagents/anti-human-antibodies/cell-surface-antigens/pe-cy5-mouse-anti-human-cd235a-ga-r2-hir2/p/559944)
Fluorescent antibodies for immune bulk cell sorting, used at 1:20 dilution: anti-human
CD16 (BD 558122, clone 3G8, https://www.bdbiosciences.com/us/applications/research/stem-cell-research/cancer-research/
human/pacific-blue-mouse-anti-human-cd16-3g8/p/558122), CD123 (BD 560826, clone 7G3, https://www.bdbiosciences.com/
us/applications/research/b-cell-research/surface-markers/human/pe-cy7-mouse-anti-human-cd123-7g3/p/560826), CCR3 (R&D
FAB155F, clone 61828, https://www.rndsystems.com/products/human-ccr3-fluorescein-conjugated-antibody-61828_fab155f),
ITGB7 (BD 551082, clone FIB504, https://www.bdbiosciences.com/us/reagents/research/antibodies-buffers/immunology-
reagents/anti-human-antibodies/cell-surface-antigens/apc-rat-anti-integrin-7-fib504/p/551082), CD3 (BD 555341, clone HIT3a,
https://www.bdbiosciences.com/us/applications/research/t-cell-immunology/th-1-cells/surface-markers/human/pe-cy5-mouse-
anti-human-cd3-hit3a/p/555341), CD14 (Invitrogen MHCD1406, clone TuK4, https://www.thermofisher.com/antibody/product/
CD14-Antibody-clone-TuK4-Monoclonal/MHCD1406), CD19 (BD 555414, clone HIB19, https://www.bdbiosciences.com/eu/
applications/research/clinical-research/oncology-research/blood-cell-disorders/surface-markers/human/pe-cy5-mouse-anti-
human-cd19-hib19/p/555414), and CD56 (BD 555517, clone B159, https://www.bdbiosciences.com/us/applications/research/
stem-cell-research/hematopoietic-stem-cell-markers/human/negative-markers/pe-cy5-mouse-anti-human-cd56-b159/
p/555517) (“basophils, neutrophils and eosinophils”); anti-human CD16 (BD 558122, see above), CD14 (BD 347497, MPP9,
https://www.bdbiosciences.com/us/applications/research/stem-cell-research/hematopoietic-stem-cell-markers/human/
negative-markers/pe-mouse-anti-human-cd14-mp9-also-known-as-mp-9/p/347497), CD4 (BD 340443, see above), CD3 (BD
555341, see above), CD8 (BD 555368, clone RPA-T8, https://www.bdbiosciences.com/us/reagents/research/antibodies-buffers/
immunology-reagents/anti-human-antibodies/cell-surface-antigens/pe-cy5-mouse-anti-human-cd8-rpa-t8/p/555368), CD19 (BD
555414, see above), and CD56 (BD 555517, see above) (“classical and nonclassical monocytes”); anti-human CD16 (BD 558122,
see above), CD1c (Miltenyi Biotec 130-098-007, clone AD5-8E7, discontinued, new product https://www.miltenyibiotec.com/US-
en/products/cd1c-bdca-1-antibody-anti-human-ad5-8e7.html), CD11c (BD 340544, clone S-HCL-3, https://
www.bdbiosciences.com/us/reagents/research/clinical-research---ruo-gmp/single-color-antibodies/apc-mouse-anti-human-
cd11c-s-hcl-3/p/340544), CCR3 (R&D FAB155F, see above), CD123 (BD 560826, see above), HLA-DR (BD 335796, clone L243,
https://www.bdbiosciences.com/us/applications/research/stem-cell-research/mesenchymal-stem-cell-markers-bone-marrow/
human/negative-markers/apc-cytrade7-mouse-anti-human-hla-dr-l243/p/335796), CD3 (BD 555341, see above), CD4 (BD
555348, clone RPA-T4, https://www.bdbiosciences.com/eu/applications/research/t-cell-immunology/th-1-cells/surface-markers/
human/pe-cy5-mouse-anti-human-cd4-rpa-t4/p/555348), CD8 (BD 555368, see above), CD14 (Invitrogen MHCD1406, see
above), CD19 (BD 555414, see above), and CD56 (BD 555517) (“pDCs, mDCs, CD16+ DCs”); anti-human IgM/IgD (BD 555778,
clone IA6-2, https://www.bdbiosciences.com/us/applications/research/b-cell-research/immunoglobulins/human/fitc-mouse-
anti-human-igd-ia6-2-also-known-as--ia6-2/p/555778), CD19 (BD 557835, clone SJ25C1, https://www.bdbiosciences.com/eu/
applications/research/clinical-research/oncology-research/blood-cell-disorders/surface-markers/human/pe-cy7-mouse-anti-
human-cd19-sj25c1-also-known-as-sj25-c1/p/557835), CD27 (BD 558664, clone M-T271, https://www.bdbiosciences.com/us/
applications/research/clinical-research/oncology-research/blood-cell-disorders/surface-markers/human/apc-mouse-anti-
human-cd27-m-t271/p/558664), CD20 (BD 335794, clone L27, https://www.bdbiosciences.com/us/applications/research/stem-
cell-research/hematopoietic-stem-cell-markers/human/negative-markers/apc-cytrade7-mouse-anti-human-cd20-l27/p/335794),
CD3 (BD 555341, see above), CD4 (BD 555348, see above), CD14 (Invitrogen MHCD1406, see above), and CD56 (BD 555517, see
above) (“B cells”); anti-human CD16 (BD 558122, see above), CD57 (BD 347393, clone HNK-1, https://www.bdbiosciences.com/
us/applications/research/t-cell-immunology/t-follicular-helper-tfh-cells/surface-markers/human/fitc-mouse-anti-human-cd57-
hnk-1/p/347393), CD56 (BD 557747, clone B159, https://www.bdbiosciences.com/eu/applications/research/stem-cell-research/
hematopoietic-stem-cell-markers/human/negative-markers/pe-cy7-mouse-anti-human-cd56-b159/p/557747), CD3 (BD 555341,
see above), CD4 (BD 555348, see above), CD14 (Invitrogen MHCD1406, see above), and CD19 (BD 555414, see above) (“NK
cells”); and anti-human CD45RA (Biolegend 304118, clone IV N906, https://www.biolegend.com/en-us/products/pacific-blue-
anti-human-cd45ra-antibody-3339), CCR7 (R&D FAB197F, clone 150503, https://www.rndsystems.com/products/human-ccr7-
fluorescein-conjugated-antibody-150503_fab197f), CD62L (BD 555544, clone DREG-56, https://www.bdbiosciences.com/eu/
applications/research/t-cell-immunology/regulatory-t-cells/surface-markers/human/pe-mouse-anti-human-cd62l-dreg-56/
p/555544), CD45RO (BD Pharmingen 560608, clone UCHL1, https://www.bdbiosciences.com/us/applications/research/b-cell-
research/surface-markers/human/pe-cy7-mouse-anti-human-cd45ro-uchl1/p/560608), CD4 (BD 340443, see above), CD8
(BD 340584, clone SK1, https://www.bdbiosciences.com/us/reagents/research/clinical-research---ruo-gmp/single-color-
antibodies/apc-mouse-anti-human-cd8-sk1/p/340584), CD11b (BD 555389, clone ICFR44, https://www.bdbiosciences.com/us/
applications/research/stem-cell-research/mesenchymal-stem-cell-markers-bone-marrow/human/negative-markers/pe-cy5-
mouse-anti-human-cd11b-icrf44-also-known-as-44/p/555389), CD14 (Invitrogen MHCD1406, see above), CD19 (BD 555414, see
above), CD56 (BD 555517, see above) (“T cells”).
Primary antibodies used for immunohistochemistry: anti-proSP-C (rabbit, Chemicon AB3786, 1:250 dilution), HES1 (rabbit, Cell
Signaling 11988S clone D6P2U, 1:100), MUC-1 (hamster, Thermo Scientific HM1630, clone MH1, 1:250), Ki67 (rat, DAKO M7249
clone MIB-1, 1:100), and Keratin-5 (chicken, Biolegend 905901, 1:100)
Validation Antibodies used for magnetic cell separation were validated by Miltenyi Biotec from human tissue containing known target
populations: CD45 (blood and bone marrow;https://www.miltenyibiotec.com/US-en/products/cd45-microbeads-human.html),
EPCAM (lung adencarcinoma;https://www.miltenyibiotec.com/US-en/products/cd326-epcam-microbeads-human.html), and
CD31 (foreskin;https://www.miltenyibiotec.com/US-en/products/cd31-microbead-kit-human.html). See indicated websites for
specific details.
All antibodies for flow cytometry were validated against isotype controls in human cells by manufacturer for that application, see
manufacturers' websites (noted above) for details.

4
nature
research
|
reporting
summary
October
2018
Antibodies for immunohistochemistry were validated by their manufacturer in human tissue with a canonical staining pattern:
pro-SP-C (lung;https://www.emdmillipore.com/US/en/product/Anti-Prosurfactant-Protein-C-proSP-C-Antibody,MM_NF-
AB3786), HES1 (breast carcinoma;https://www.cellsignal.com/products/primary-antibodies/hes1-d6p2u-rabbit-mab/11988),
MUC-1 (breast carcinoma;https://www.thermofisher.com/order/catalog/product/HM-1630-P1#/HM-1630-P1), Ki67
(tonsillar;https://www.agilent.com/en/product/immunohistochemistry/antibodies-controls/primary-antibodies/ki-67-antigen-
(dako-omnis)-76239), Keratin 5 (skin;https://www.biolegend.com/en-us/products/keratin-5-polyclonal-chicken-antibody-
purified-10957). See indicates websites for specific details.
Animals and other organisms
Policy information about studies involving animals; ARRIVE guidelines recommended for reporting animal research
Laboratory animals 1) 2m old female B6,Axin2-CreER (https://www.jax.org/strain/018867, heterozygous) bred into B6,mTmG (https://www.jax.org/
strain/007676, heterozygous)
2) 2m old female FVB,Tbx4-Cre (http://www.informatics.jax.org/allele/MGI:5635865, heterozygous) bred into B6,Ai6 (https://
www.jax.org/strain/007906, heterozygous)
3) Tabula Muris Senis: C57J/B6 mice, male and female, ages 1m, 3m, 12m, 18m, 21m, 24m, and 30m.
All animals were species Mus musculus.
Wild animals Study did not involve wild animals.
Field-collected samples Study did not involve samples collected from the field.
Ethics oversight All mouse experiments followed applicable regulations and guidelines and were approved by the Institutional Animal Care and
Use Committee at Stanford University (Protocol 9780).
Note that full information on the approval of the study protocol must also be provided in the manuscript.
Human research participants
Policy information about studies involving human research participants
Population characteristics Patient ages (in order) were 75, 46, and 51; sexes male, female, and male; all patients had normal pulmonary function tests and
were otherwise healthy except for early stage focal tumors.
Recruitment Patients were recruited and consented by C.S.K. and J.B.S after selecting surgical resection with curative intent as their treatment
option for early-stage, focal tumors. Stanford Hospital’s patient pool is not necessarily representative of the broader human
population and there may be additional cell types and states found from future studies from other centers. While we selected
subjects with no history of serious pulmonary disease (other than their focal lung tumors) and included both genders in our
study, expression profiles from captured cell types will vary to some extent with age, ethnicity, gender, socioeconomic status,
and health status.
Ethics oversight Patient tissues were obtained under a protocol approved by Stanford University’s Human Subjects Research Compliance Office
(IRB 15166) and informed consent was obtained from each patient prior to surgery. All experiments followed applicable
regulations and guidelines.
Note that full information on the approval of the study protocol must also be provided in the manuscript.
Flow Cytometry
Plots
Confirm that:
The axis labels state the marker and fluorochrome used (e.g. CD4-FITC).
The axis scales are clearly visible. Include numbers along axes only for bottom left plot of group (a 'group' is an analysis of identical markers).
All plots are contour plots with outliers or pseudocolor plots.
A numerical value for number of cells or percentage (with statistics) is provided.
Methodology
Sample preparation Tissue source
Freshly resected lung tissue was procured intraoperatively from patients undergoing lobectomy
for focal lung tumors. Normal lung tissues (~5 cm3) were obtained from uninvolved regions and
annotated for the specific lung lobe and location along the airway or periphery. Pathological
evaluation (by G.B.) confirmed normal histology of the profiled regions, except for areas of very
mild emphysema in Patient 1. Patient 1 was a 75 year-old male with a remote history of
smoking, diagnosed with early stage adenocarcinoma who underwent left upper lobe (LUL)
lobectomy; two blocks of normal tissue were obtained from lung periphery (“Distal 1a and 1b”).

5
nature
research
|
reporting
summary
October
2018
Patient 2 was a 46 year-old male, non-smoker with a right middle lobe (RML) endobronchial
carcinoid, who underwent surgical resection of the right upper and middle lobes; two blocks of
tissue were selected from mid-bronchial region (“Medial 2”) and periphery (“Distal 2”) of right
upper lobe (RUL). Patient 3 was a 51 year-old female, non-smoker with a LLL endobronchial
typical carcinoid, who underwent LLL lobectomy; three tissue blocks were resected from the
bronchus (“Proximal 3”), mid-bronchial (“Medial 2”), and periphery (“Distal 3”) of the LLL. All
tissues were received and immediately placed in cold phosphate buffered saline (PBS) and
transported on ice directly to the research lab for single cell dissociation procedures. Peripheral
blood was collected from patients 1 and 3 in EDTA tubes.
------------------------
Lung cell processing and staining
Individual human lung samples were dissected, minced, and placed in digestion media (400
μg/ml Liberase DL (Sigma 5401127001) and 100 μg/ml elastase (Worthington LS006365) in
RPMI (Gibco 72400120) in a gentleMACS c-tube (Miltenyi 130-096-334). Samples were
partially dissociated by running ‘m_lung_01’ on a gentleMACS Dissociator (Miltenyi 130-093-
235), incubated on a Nutator at 37°C for 30 minutes, and then dispersed to a single cell
suspension by running ‘m_lung_02’. Processing buffer (5% fetal bovine serum in PBS) and
DNAse I (100 μg/ml, Worthington LS006344) were then added and the samples rocked at 37°C
for 5 minutes. Samples were then placed at 4oC for the remainder of the protocol. Cells were
filtered through a 100 μm filter, pelleted (300 x g, 5 minutes, 4°C), and resuspended in ACK red
blood cell lysis buffer (Gibco A1049201) for 3 minutes, after which the buffer was inactivated
by adding excess processing buffer. Cells were then filtered through a 70 μm strainer
(Fisherbrand 22363548), pelleted again (300 x g, 5 minutes, 4°C), and resuspended in magnetic
activated cell sorting (MACS) buffer (0.5% BSA, 2 mM EDTA in PBS) with Human FcR
Blocking Reagent (Miltenyi 130-059-901) to block non-specific binding of antibodies (see
below).
Immune and endothelial cells were overrepresented in our previous mouse single cell
suspensions. To partially deplete these populations in our human samples, we stained cells
isolated from lung with MACS microbeads conjugated to CD31 and CD45 (Miltenyi 130-045-
801, 130-091-935) then passed them through an LS MACS column (Miltenyi, 130-042-401) on a
MidiMACS Separator magnet (Miltenyi, 130-042-302). Cells retained on the column were
designated “immune and endothelial enriched.” The flow through cells were then split, with 80%
immunostained for FACS (see below) and the remaining 20% stained with EPCAM microbeads
(Miltenyi 130-061-101). EPCAM stained cells were passed through another LS column. Cells
retained on the column were labeled “epithelial enriched”, and cells that flowed through were
designated “stromal”.
Following negative selection against immune and endothelial cells by MACS, the remaining
human lung cells were incubated with FcR Block (Becton Dickinson (BD) 564219) for 5 minutes
and stained with directly conjugated anti-human CD45 (Biolegend 304006) and EPCAM
(eBioscience 25-9326-42) antibodies on a Nutator for 30 minutes. Cells were then pelleted (300
x g, 5 minutes, 4°C), washed with FACS buffer three times, then incubated with cell viability
marker Sytox blue (1:3000, ThermoFisher S34857).
------------------------
Immune cell processing and staining
Immune cells, including granulocytes, were isolated from peripheral blood using a high density
ficoll gradient56. Briefly, peripheral blood was diluted 10-fold with FACS buffer (2% FBS in
PBS), carefully layered on an RT Ficoll gradient (Sigma HISTOPAQUE®-1119), and
centrifuged at 400 x g for 30 minutes at room temperature. The buffy coat was carefully
removed, diluted 5-fold with FACS buffer, pelleted (300 x g, 5 minutes, 4°C), and incubated in
ice cold FACS buffer containing DNAse I (Worthington LS006344) for 10 minutes at 4°C.
Clumps were separated by gentle pipetting to create a single cell suspension.
Immune cells from subject matched blood were incubated with FcR Block and Brilliant Violet
buffer (BD 563794) for 20 minutes and then stained with directly conjugated anti-human CD3
(BD 563548), CD4 (BD 340443), CD8 (BD 340692), CD14 (BD 557831), CD19 (Biolegend
302234), CD47 (BD 563761), CD56 (BD 555516), and CD235a (BD 559944) antibodies for 30
minutes. Cells were pelleted (300 x g, 5 minutes, 4°C), washed with FACS buffer twice, and
then incubated with the viability marker propidium iodide.
------------------------
Immune bulk sort processing and staining
Immune cells for bulk mRNA sequencing were incubated with Fc Block for 20 minutes and then
stained with one of six panels of directly conjugated antibodies for 30 minutes: anti-human
CD16 (BD 558122), CD123 (BD 560826), CCR3 (R&D FAB155F), ITGB7 (BD 551082), CD3
(BD 555341), CD14 (Invitrogen MHCD1406), CD19 (BD 555414), and CD56 (BD 555517)

6
nature
research
|
reporting
summary
October
2018
(“basophils, neutrophils and eosinophils”); anti-human CD16 (BD 558122), CD14 (BD 347497),
CD4 (BD 340443), CD3 (BD 555341), CD8 (BD 555368), CD19 (BD 555414), and CD56 (BD
555517) (“classical and nonclassical monocytes”); anti-human CD16 (BD 558122), CD1c
(Miltenyi Biotec 130-098-007), CD11c (BD 340544), CCR3 (R&D FAB155F), CD123 (BD
560826), HLA-DR (BD 335796), CD3 (BD 555341), CD4 (BD 555348), CD8 (BD 555368),
CD14 (Invitrogen MHCD1406), CD19 (BD 555414), and CD56 (BD 555517) (“pDCs, mDCs,
CD16+ DCs”); anti-human IgM/IgD (BD 555778), CD19 (BD 557835), CD27 (BD 558664),
CD20 (BD 335794), CD3 (BD 555341), CD4 (BD 555348), CD14 (Invitrogen MHCD1406), and
CD56 (BD 555517) (“B cells”); anti-human CD16 (BD 558122), CD57 (BD 347393), CD56
(BD 557747), CD3 (BD 555341), CD4 (BD 555348), CD14 (Invitrogen MHCD1406), and CD19
(BD 555414) (“NK cells”); and anti-human CD45RA (Biolegend 304118), CCR7 (R&D
FAB197F), CD62L (BD 555544), CD45RO (BD Pharmingen 560608), CD4 (BD 340443), CD8
(BD 340584), CD11b (BD 555389), CD14 (Invitrogen MHCD1406), CD19 (BD 555414), CD56
(BD 555517) (“T cells”). Cells were washed with FACS buffer twice, incubated with the
viability marker propidium iodide.
Instrument Lung samples: Sony SH800S, Blood samples: FACS Aria II
Software Lung samples: Sony SH800S Cell Sorter software v1.8, Blood samples: BD Diva software v8
Cell population abundance We sorted equal numbers of epithelial, immune, and endothelial/stromal cells with the gating strategy described below. The
percentage of expression profiles from each tissue compartment is consistent with the sorting (30% endothelial/immune, 34%
epithelial, 36% immune).
Gating strategy Lung samples: Living single cells (Sytox blue-negative) were sorted into lysis plates based on three gates:
EPCAM+CD45- (designated “epithelial”), EPCAM-CD45+ (designated “immune”), and EPCAM-CD45-
(designated “endothelial or stromal”). Blood samples: Living (propidium iodide-negative) single, non-red blood (CD235a-) cells
were sorted into lysis plates along with specific immune populations: B cells (CD19+CD3-), CD8+ T cells
(CD8+), CD4+ T cells (CD4+), NK cells (CD19-CD3-CD56+CD14-), classical monocytes (CD19-
CD3-CD56-CD14+). (See Extended Data Figure S1).
Please see Extended Data Table S3 for sorting strategy from bulk sorted immune populations.
Tick this box to confirm that a figure exemplifying the gating strategy is provided in the Supplementary Information.