Journal of Cystic Fibrosis 24 (2025) 849–860

Contents lists available at ScienceDirect

Journal of Cystic Fibrosis

journal homepage: www.elsevier.com/locate/jcf

Original Article

Evidence for altered immune-structural cell crosstalk in cystic fibrosis
revealed by single cell transcriptomics

☆

, Martin Banchero a,d, Orestes A. Carpaij a,d,

, Pascal Barbry e, Lieke S. Kamphuis b

Marijn Berg a,d,1,# , Lisette Krabbendam b,1,$ , Esmee K. van der Ploeg b
Menno van Nimwegen b, Tjeerd van der Veer a,b,^
Remco Hoogenboezem c, Maarten van den Berge a,d, Eric Bindels c
Antoine Collin e
Martijn C. Nawijn a,d,2, Ralph Stadhouders b,2,*
a Department of Pathology and Medical Biology, University of Groningen, University Medical Center Groningen, Groningen, Netherlands
b Department of Pulmonary Medicine, Erasmus MC, University Medical Center, Rotterdam, Netherlands
c Department of Hematology, Erasmus MC, University Medical Center, Rotterdam, Netherlands
d GRIAC research institute, University Medical Center Groningen, Groningen, Netherlands
e Universit´e Cˆote d’Azur, Centre National de la Recherche Scientifique and INSERM, Institut de Pharmacologie Mol´eculaire et Cellulaire, 3IA Cˆote d’Azur, IHU Respirera,
Sophia Antipolis, France

, Rudi W. Hendriks b,2 ,

, Joachim G.J.V. Aerts b,

,

A R T I C L E  I N F O

A B S T R A C T

Keywords:
Cystic fibrosis
Single-cell RNA-sequencing
Bronchial biopsies
structural-immune cell crosstalk

Background:  Chronic  pulmonary  inflammation  strongly  contributes  to  respiratory  failure  and  mortality  in  pa-
tients with cystic fibrosis (pwCF). Effective anti-microbial immunity and maintaining lung homeostasis require
continuous  structural-immune  cell  communication.  Whether  and  how  this  crosstalk  is  altered  in  CF  remains
poorly understood, obscuring potential new angles for therapy development to restore airway homeostasis in
pwCF.
Methods: We performed droplet-based single cell RNA-sequencing on bronchial biopsies from pwCF to investigate
structural-immune cell crosstalk. Computational analyses were used to compare these data to samples obtained
from healthy controls.
Results: CF airway wall biopsies showed lower proportions and altered transcriptomes of basal cells, submucosal
gland cells and endothelial cells, and a higher abundance of ciliated cells, monocytes, macrophages and T cells.
Both  B  and  T  lymphocytes  displayed  aberrantly  activated  phenotypes  with  transcriptional  changes  linked  to
hypoxia and vascular endothelial growth factor signaling, indicative of crosstalk with endothelial cells. The CF
lung  displayed  unique  changes  in  intercellular  communication  potential  involving  ionocytes,  macrophages,
endothelial cells and lymphocytes. This included interactions between HLA-E on structural cells and the drug-
gable CD94/NKG2A immune checkpoint on CD8
Conclusions:  We  report  the  first  single  cell  transcriptome  atlas  of  the  CF  lung  containing  the  full  spectrum  of
structural  and immune  cells,  providing  a  valuable  resource  for  investigating  changes to  cellular  composition,
phenotypes  and  crosstalk  linked  to  CF.  Our  analyses  highlight  dysregulated  basal  cell  function  and  adaptive
immunity in pwCF –  despite favorable responses to CFTR modulator therapy. We identify novel aspects of CF
pathophysiology and potential entry points for therapeutic strategies.

T cells.

+

☆

Bibliography: Parts of the data described in this manuscript have been presented at the European Cystic Fibrosis Conference, on the 10th of June 2023, in Vienna,

Austria.

* Corresponding author.

E-mail address: r.stadhouders@erasmusmc.nl (R. Stadhouders).

# Current address: Department of Genetics, University of Groningen, University Medical Center Groningen, Groningen, Netherlands.
$ Current address: Chiesi Pharmaceuticals B.V., Amsterdam, Netherlands.
^ Current address: Department of Pulmonary Medicine, Leiden University Medical Centre, Leiden, Netherlands.
1 equal contribution.
2 shared senior authors.

https://doi.org/10.1016/j.jcf.2025.01.016
Received 29 July 2024; Received in revised form 29 November 2024; Accepted 31 January 2025
Available online 13 February 2025
1569-1993/© 2025 The Author(s).  Published by Elsevier B.V. on behalf of European Cystic Fibrosis Society.  This is an open access article under the CC BY license
( http://creativecommons.org/licenses/by/4.0/ ).

M. Berg et al.

Journal of Cystic Fibrosis 24 (2025) 849–860

1. Introduction

Cystic Fibrosis (CF) is a life-limiting, multisystem, autosomal reces-
sive disorder caused by a mutation in the cystic fibrosis transmembrane
conductance  regulator  (CFTR)  gene  [1].  CFTR  regulates  the  pH  and
hydration of the epithelial lining fluid through chloride and bicarbonate
transport in epithelial cells [1]. In the lungs, CFTR dysfunction leads to
dehydration  and  thickening  of  the  epithelial  lining  fluid,  as  well  as
acidification and hypoxia, resulting in mucus tethering, loss of ciliary
function and reduced antimicrobial function [2]. Changes in mucocili-
ary function lead to a hyper-inflammatory state and persistent bacterial
infections (e.g. with Pseudomonas aeruginosa) in the airways of patients
with CF (pwCF). Restoring CFTR function with modulators –such as the
triple  drug  combination  Elexacaftor/Tezacaftor/Ivacaftor  (Kaftrio)–
results in significant improvement of clinical symptoms in most patients,
including lung function and frequency of exacerbations [3]. However,
side  effects  or  drug-drug  interactions  of  CFTR  modulators  precludes
their use in  some patients [4].  Moreover, while modulator therapy is
reported  to  reduce  systemic  and  local  inflammatory  markers  [5,6],
bacterial infections and inflammation in the airways continue to pose a
substantial  problem  [7–10].  Hence,  there  is  a  need  for  alternative
treatment strategies for pwCF.

Upon viral or bacterial infections, different types of airway epithelial
cells  contribute  to  pathogen  clearance  via  initiation  of  innate  and
adaptive immune responses [11]. These are often accompanied by tissue
damage that requires repair, which involves crosstalk between epithelial
and immune cells. A disrupted epithelial-immune cell crosstalk has been
shown  to  contribute  to  airway  inflammation  and  irreversible  tissue
remodeling in chronic respiratory diseases, such as COPD and asthma
[11].  Extensive  remodeling  also  occurs  in  the  airways  of  pwCF,  in
addition  to  an  impaired  capacity  of  the  immune  system  to  clear  in-
fections [1].

In  previous  studies,  single-cell  RNA  sequencing  (scRNA-seq)  has
provided  detailed  knowledge  of  the  composition  and  transcriptional
profile  of  airway  epithelial  cells  [12],  sputum  cells  [13]  and  bron-
choalveolar lavage (BAL) samples [14,15] from pwCF. The CF epithelial
compartment showed increased secretory activity, reduced basal (stem)
cell proliferation and skewed differentiation towards ciliated cells – in
line with dysfunctional tissue repair in pwCF [12]. Sputum samples from
pwCF were characterized by influx of recruited monocytes and imma-
ture pro-inflammatory neutrophils, as opposed to the dominant presence
of alveolar macrophages in healthy control samples [13]. In lung tissue
from  pwCF,  CFTR  dysfunction  resulted  in  increased  numbers  of
lymphoid follicles and activated B cells [2,16]. While B cells were also
increased in sputum of pwCF, a detailed analysis of T cells was precluded
by limited T cell numbers obtained in this study. In BAL samples from
children with CF, several distinct macrophage populations and CD4
T
cells  expressing inflammatory IFNα/β  and  NFκB signaling  genes  were
described,  although  no  statistical  comparisons  with  healthy  control
samples could be made [14]. An early discovery in CF research is the
failure of adaptive immunity and T cell responses against Pseudomonas
aeruginosa [17,18]. For example, several studies reported the launch of
ineffective Th2 and Th17 responses in Pseudomonas aeruginosa inflamed
lungs of pwCF [18–21]. CFTR mutant T cells displayed altered cytokine
production profiles in vitro [22], and regulatory T cell (Treg) numbers
were decreased in pwCF with a chronic Pseudomonas aeruginosa infec-
tion, correlating with lung function [23]. Thus, CFTR dysfunction and
recurrent  infections are linked to transcriptional changes and cellular
dysfunction in the lungs of pwCF.

+

The  abovementioned  studies  provide  valuable  insights  into  the
composition and transcriptional phenotypes of epithelial cells, macro-
phages and neutrophils in the airways of pwCF [24]. However, no study
has transcriptionally characterized the full spectrum of both innate and
adaptive  immune  cells  in  combination  with  structural  cells  (e.g.
epithelial  cells)  from  the  same  CF  lung  tissue  microenvironment,
obscuring  our  understanding  of  airway  lymphocyte  phenotypes  and

850

(dysregulated)  structural-immune  cell  crosstalk  in  pwCF.  Here,  we
conducted  a  detailed  single-cell  transcriptomic  analysis  of  airway  bi-
opsies of adult pwCF and healthy controls to obtain a comprehensive
overview of the cellular landscape in CF lungs, encompassing both the
structural and immune cell compartments – as well as potential crosstalk
between these.

2. Results

2.1. Single cell RNA-sequencing of airway biopsies from pwCF and
healthy controls

To acquire a comprehensive overview of the full spectrum of immune
and  structural  cells  in  the  lung,  droplet-based  scRNA-seq  (10X  Chro-
mium) was performed on bronchial biopsies from pwCF (n = 3 donors,
19,855 cells in total) (Fig. 1A). All pwCF harbored at least one ΔF508
mutation and used CFTR modulators at the time of inclusion (Table 1),
presenting  with  mild-to-moderate  disease  (%FEV1  > 40)  in  line  with
favorable therapy response. The obtained CF dataset was generated at
Erasmus MC (EMC). Because of the unavailability of bronchial biopsies
from healthy controls  (HC) at  EMC,  we leveraged  existing scRNA-seq
data  from  bronchial  biopsies  of  HCs  generated  at  the  Universit´e  cˆote
d’Azur (UCdA) (n = 9) [25] and the UMC Groningen (UMCG) (n = 10)
[26].  To  correct  for  sample  variation  due  to  anatomical  location  and
processing between the HC samples and CF samples (see Table 1 and
Methods),  we  integrated  the  three  datasets  with  the  Mutual  Nearest
Neighbors  method  (fastMNN  [27])  making  use  of  the  healthy  donor
samples  from  the  recently  published  Human  Lung  Cell  Atlas  (HLCA)
dataset  [28].  This  atlas  describes  cell-type  specific  transcriptional
changes associated with location along the proximal-to-distal axis of the
bronchial tree. Mapping the individual samples lacking annotation on a
trained model of the HLCA, followed by label transfer using scArches
[29] to facilitate cluster annotation, resulted in the identification of 17
cell types (using HLCA consensus labels; Fig. 1B) – including epithelial,
immune and stromal cells. The accuracy of the transferred labels was
validated  by  the  expression  of  known  cell-type  specific  markers
(Fig. 1C). To make this dataset available as a resource for the commu-
nity,  we  generated  a  cellXgene  object  [30]  that  can  be  interactively
explored  in  a  web  browser  (https://cellxgene.cziscience.com/collecti
ons/54004c5c-af08–4693-a606–73871b6ef989).  Thus,  combined  data
generation and integration yielded a new single cell transcriptome atlas
of  the human  lung, allowing  for  in-depth  exploration of  immune and
structural cell phenotypes in pwCF.

2.2. Altered cell composition in airway biopsies of pwCF

All 17 cell types were detected in both CF and HC biopsies (Fig. 2A-B)
and in all three datasets (Fig. S1A). CFTR expression was observed in
several epithelial cell clusters, but was highest in pulmonary ionocytes
(cluster  5,  Fig.  2C)  –  in  line  with  previous  reports  [12,31,32].  CFTR
expression was comparable between CF and HCs in all CFTR expressing
cells,  including  ionocytes,  which  is  in  line  with  post-transcriptional
mechanisms  disrupting  CFTR  function  for  the  involved  mutations
(Fig. S1B, Fig. 2D). To add robustness to the observed changes in cell
type composition in the airway wall of pwCF, we focused on those dif-
ferences  that  were  reproducible  in  the  comparison  between  the  CF
cohort and both HC cohorts. Generalized mixed model analysis revealed
a  significant  reduction  in  the  proportions  of  basal  cells  (cluster  1),
submucosal  gland  epithelial  cells  (cluster  4)  and  endothelial  cells
(cluster  16)  in  the  airway  biopsies  from  pwCF  compared  to  HCs.  In
contrast, the numbers of monocytes and macrophages (clusters 13–14),
T cells (clusters 7–8) were
ciliated cells (cluster 2) as well as CD4
significantly  increased  in  pwCF  (Fig.  2E,  Fig.  S1C).  Cell-cycle  phase
analysis demonstrated that compositional differences were likely inde-
pendent of cell cycle activity (Fig. S1D-E). While neutrophils were not
annotated  as  a  distinct  cluster  likely  due  to  low  RNA  content  and

/CD8

+

+

M. Berg et al.

Journal of Cystic Fibrosis 24 (2025) 849–860

limitations  of  the  10X  Genomics  platform  versions  used  for  HLCA
annotation, we did detect a small subset of neutrophil-like cells (defined
by  high  levels  of  FCGR3B  and  CSF3R  expression)  residing  within  the
monocyte cluster, which was largely derived from pwCF (Fig. S1F-G).
Hence, we observed substantial changes in cell type composition of the
lower airway wall between pwCF and HCs, involving an overall decrease
in abundance of most epithelial cell subsets and an increased immune

cell presence.

2.3. Transcriptional changes in epithelial cell subsets in CF airway
biopsies

To further explore disease-associated differences between pwCF and
HC,  differential  gene  expression  analysis  was  performed  on  the

Fig. 1. scRNA-seq of lung biopsies from pwCF and healthy controls. (A) Schematic overview of sampling locations, sample characteristics and workflow for 10X
Chromium single-cell RNA-sequencing data generation. Figure created using BioRender. (B) Uniform Manifold Approximation and Projection (UMAP) clustering of
the annotated cell types across all samples combined. (C) Expression levels of selected cell type-specific markers in the 17 annotated cell types.

851

M. Berg et al.

Journal of Cystic Fibrosis 24 (2025) 849–860

Table 1
Airway biopsy donor characteristics grouped per dataset.

Status
Age (years)
Sex (M/F)
BMI (kg/m2)
CF mutation

FEV1 (L)
FEV1 (%)
P. Aeruginosa
Colonization

CFTR

modulator

Biopsy position

Digestion
protocol

EMC

n = 3
Cystic fibrosis
23 ± 4.4
1/2
21.7 ± 4.0
donor #1:
ΔF508/R553X,
donor #2:
ΔF508/ΔF508,
donor #3:
ΔF508/A455E
3.55 ± 0.4
91.3 ± 14.5
donor #1: no
donor #2: yes
donor #3: no
donor #1: ETI*,
donor #2: ETI*
donor #3: TI**
subcarinal

enzymatic
digestion:
Liberase + DNase

UMCG

n = 10
Healthy
55.8 ± 6.1
8/2
24.8 ± 4.1
NA

UCDA

n = 9
Healthy
29 ± 3.4
4/5
Unknown
NA

3.9 ± 3.9
115.7 ± 13.8
Unknown

Unknown
Unknown
Unknown

NA

NA

airway 3–6th
generation
enzymatic
digestion:
Collagenase D +
DNase

subcarinal

protease from
Bacillus
Licheniformis

* ETI = Elexacaftor/Tezacaftor/Ivacaftor.
** TI = Tezacaftor/Ivacaftor.

+

+

+

including

inflammatory  cytokines

investigated  in  previous  scRNA-seq  analyses  [12–15].  In  our  study,
T cell exhibited the most DEGs, with 106 upregulated
cytotoxic CD8
and  23  downregulated  genes  in  pwCF  compared  to  HC  (Fig.  3B-C).
Upregulated  genes  were  involved  in  pro-inflammatory  and  defense
response  pathways,
(IFNG),
trafficking-associated  genes  (GNAI2),  activation-associated  transcrip-
tion  factors  (FOS,  JUND)  and  canonical  immune  activation  marker
(CD69) (Fig. 3C). Increased expression of CD81 indicates activation and
proliferation of T cells through co-engagement with CD3 [34], which
was also upregulated in CD8
T cells from pwCF (Fig. 3C). 16 DEGs were
T helper cells, all of which were upregulated in pwCF
detected in CD4
(Fig. 3D). These genes also act in pathways relevant to T cell activation,
including KLF2, IL7R and CD48. Interestingly, both CD4
T
cells  showed  enhanced  expression  of  genes  potentially  related  to
vascular  endothelial  growth  factor  receptor  (VEGFR)  signaling,
including  TXNIP,  MAP2K2  and  ETS1.  TXNIP  and  MAP2K2  showed
broader trends of upregulating across many epithelial and immune cell
subsets (Fig. S3A), suggesting that altered VEGFR signaling may be a
feature  of  CF  pathophysiology.  Of  note,  endothelial  cells  –  known  to
respond to VEGF signaling [35]– showed marked changes in expression
of  cell  differentiation  genes  in  pwCF  (Fig.  S3B),  indicating  altered
endothelial cell phenotypes in pwCF. In B cells, we detected 86 upre-
gulated genes and 16 downregulated genes in pwCF (Fig. 3E). Similar to
both T cell subsets, these transcriptional changes are mostly linked to
regulating cell activation (e.g. SYK, CD81) and interferon responses (e.g.
HLA-DP, LTB). In addition, platelet-derived growth factor receptor beta
(PDGFRB) signaling was increased in B cells from pwCF.

and CD8

+

+

transcriptional profile per cell type. We strictly focused on differentially
expressed genes (DEGs) found in comparison with both HC cohorts. In
the epithelial compartment, most DEGs were detected in basal cells (n =
509) and ciliated cells (n = 382), whereas fewer DEGs were observed in
secretory cells (n = 270) and submucosal gland epithelial cells (n = 83)
(Fig. 3A). In epithelial cells, substantial numbers of DEGs were cell type-
specific,  especially  for  basal  and  ciliated  cells  (>60  %  of  all  DEGs;
Fig. 3A). Gene ontology (GO) enrichment analysis revealed a striking
similarity of altered biological pathways among epithelial cell subsets of
pwCF  (Fig.  S2A-B).  Pathways  were  most  prominently  involved  in  in-
flammatory  responses,  chromatin  organization  and  DNA  damage
response (Fig. SA-B). Submucosal gland epithelial cells showed a more
functionally distinct DEG signature related to gland development and
responses to lipoproteins or hormones (Fig. S2A-B). Interestingly, most
epithelial cell DEGs (72–86 %) were upregulated in pwCF compared to
HC, including a large number of interferon responsive genes (e.g. IFIT1,
MX1,  OAS2;  consistent  with  previously  published  results  [33]),  chro-
matin modifying enzymes (e.g. KDM1A, KMT5A) and DNA repair factors
(e.g. RAD50, ERCC6, ERCC8) (Table S1).

Similar  to  previous  findings  by  Carraro  et  al.  [12].,  basal  cells  in
pwCF showed lower expression of keratinization-associated genes CSTA
(cystatin A) and HSPB1 (heat shock protein B1) (Fig. S2C). In contrast to
the  Carraro  study, expression  levels  of  AP-1 family  genes  FOS,  FOSB,
JUN and JUNB were not increased in our basal cells. In line with Carraro
et al., ciliated cells in pwCF showed a trend towards higher expression of
genes  linked  to  ciliogenesis  such  as  DNAH5,  SYNE1  and  SYNE2,
although expression of AGR3 – encoding a protein responsible for ciliary
beat frequency and motility – was not increased (Fig. S2D). Like Carraro
et  al.,  we  also  observed  somewhat  higher  levels  of  immune-linked
HLA-DPA1 and HLA-DRB1 gene expression on ciliated cells (Fig. S2D).
Together, these analyses indicate impaired inflammatory responses
and  increased  expression  of  chromatin  remodeling  as  well  as  DNA
damage repair genes in epithelial cells from the airways of pwCF.

2.4. Lymphocytes in airway biopsies of pwCF exhibit altered
transcriptional programs

The lymphocyte compartment of pwCF has only been superficially

Interestingly, expression of IGHG3 and IGLC2 –encoding subunits of
the antigen-specific B cell receptor (BCR)– was significantly lower in B
cells from pwCF than from HCs (Fig. 3E). Expression levels of other BCR
genes  (IGHD,  IGHA1,  IGHG1,  IGLC3,  and  IGLC1)  were  also  lower  in
pwCF (although not statistically significant in both comparisons), sug-
gesting  a  concerted  downregulation  of  BCR  expression  rather  than  a
change  in  repertoire.  In  the  Human  Lung  Cell  Atlas  [28],  these  BCR
genes are particularly highly expressed in plasma cells (not annotated as
a separate cell-type in our dataset), indicating a possible lower abun-
dance  or  activity  of  plasma  cells  in  pwCF.  This  was  supported  by
decreased  expression  of  the  gene  encoding  the  CD138  plasma  cell
marker in pwCF (SCD1, P = 0.06). Other lymphoid or myeloid cell types
identified  in  our  dataset  generally  showed  relatively  few  DEGs.  A
complete list of all DEGs detected in this study can be found in Table S1.
Together,  these  data  reveal  deregulated  transcriptional  programs
across the major lymphocyte subsets in the lungs of pwCF and identify
novel biological pathways altered in CF T and B cells.

2.5. Evidence for altered intercellular crosstalk in the airways of pwCF

To investigate whether the observed changes in cell proportions and
transcriptional profiles were predicted to affect intercellular communi-
cation  in  pwCF,  we  performed  cell-cell  interaction  analysis  using
LIgand-receptor ANalysis frAmework (LIANA [36]) on the CF and two
control datasets. First, we identified the total numbers of potential in-
teractions between all cells in each individual dataset (Fig. S4A). Sub-
sequently, unique interactions between cells in pwCF were determined
by removing any interactions detected in either of the two HC datasets
(Fig.  S4B).  This  analysis  revealed  a  substantial  number  of  unique
cell-cell  interactions  among  basal  cells  and  between  endothelial  and
basal cells (Fig. S4B). In addition, macrophages, ionocytes and stromal
cells showed increased incoming signals from various other cell types in
pwCF. Macrophages for example received increased numbers of signals
from most  other cell types,  including endothelial  cells, B  cells, and  T
cells.

Cellular  crosstalk  between  the  adaptive  immune  system  and  lung
structural  or  resident  immune  cells  is  largely  unexplored  in  CF.  Our
analyses  reveal  altered  interaction  potential  towards  (Fig.  4A,C)  and
from  (Fig.  4B,D)  B  and  T  cells  in  pwCF.  Ionocytes  and  macrophages

852

​
M. Berg et al.

Journal of Cystic Fibrosis 24 (2025) 849–860

+

+

and CD8

engaged in CF-specific putative interactions with adaptive lymphocytes,
whereas particularly CD4
T cells showed potential for CF-
specific  interactions  with  macrophages,  monocytes  and  endothelial
+
cells (Fig. 4A-D). For instance, CD8
T cells showed higher expression of
IFNG,  which  was  predicted  to  interact  with  its  receptor  (IFNGR1/2)
expressed on basal epithelial cells, DCs, endothelial cells, macrophages
and  stromal  cells  (Fig.  4E).  Furthermore,  all  lymphocyte  subsets
exhibited higher expression of GNAI2 (encoding an immunomodulatory
protein [37], which can engage in interactions with multiple receptors
on  basal  cells,  stromal  cells  and  ILC/NK  cells  (Fig.  4E).  Finally,  both
CD4
T cells express CALR (encoding Calreticulin) at higher
levels in pwCF, which can bind to LRP1 (encoding CD91) expressed by
macrophages to promote pro-inflammatory responses [38].

and CD8

+

+

Analysis of signals received by lymphocytes revealed a remarkable
increase in interactions with HLA-E in pwCF, which is expressed on a

+

range of cell types (Fig. 4F). HLA-E was predicted to interact with CD8A/
B and several killer-like lectin receptors (KLRC1/2/3, KLRD1, KLRK1)
T  cells.  Together,  HLA-E  and  CD94/NKG2A  (encoded  by
on  CD8
KLRD1 and KLRC1, respectively) form an important immune checkpoint
signaling route associated with controlling CD8
T cell activity (Fig. 4F)
+
+
[39–41]. Interestingly, B cells, CD4
T cells may also receive
signals from GNAI2 (expressed by macrophages, DCs, ILC/NK cells, and
proliferating  T  cells)  via  their  expression  of  CXCR3, F2R,  and  S1PR4,
indicating that signaling through GNAI2 is of particular importance in
CF.

and CD8

+

Taken  together,  these  data  indicate  altered  cellular  crosstalk  be-
tween  immune  cells  –  including  adaptive  lymphocytes  –  and  lung
structural  cells  in  pwCF  compared  to  HCs,  implicating  novel  cell-cell
interaction pathways in CF pathophysiology.

Fig. 2. Cell type composition of lung biopsies from patients with CF (pwCF) and healthy controls (HCs). (A-B) UMAP clustering of the 17 detected cell types (see
Fig. 1B) split between pwCF (A) and HCs (B) (C) CFTR expression levels across all samples combined. (D) CFTR expression in pulmonary ionocytes from pwCF and
HCs. (E) Composition analysis of the 17 cell types present in the airway wall biopsies. Odds ratios depict depletion (odds ratio <1) or enrichment (odds ratio >1) in
HC versus CF samples. Purple dots indicate a statistically significant decrease in pwCF, orange dots indicate increased proportions in pwCF (P < 0.05 in generalized
mixed model analysis). Gray dots indicate a lack of statistical significance.

853

M. Berg et al.

Journal of Cystic Fibrosis 24 (2025) 849–860

Fig. 3. Differential gene expression analysis in lymphocytes of pwCF. (A, B) Upset plot showing the number of total (between brackets), unique (single circle) and
shared (connected circles) differentially expressed genes (DEGs, FDR<0.05) detected in CF versus HC bronchial epithelial subsets (A) and lymphocytes (B). (C-E) Left-
hand panels: volcano plots indicating DEGs in CD8
T cells (D) and B cells (E) between CF and HCs. Highlighted genes are statistically significant
(FDR<0.05) in both the EMC/UMCG and EMC/UCdA comparisons. Center panels: Selected enriched pathways in CD8
T cells (D) and B cells (E).
Right-hand panels: Scaled expression of key genes associated with the selected pathways (indicated by matching colors). Expression values of individual tissue donors
are shown: blue indicates healthy control donors; orange indicates CF donors.

T cells (C), CD4

T cells (C), CD4

+

+

+

+

854

M. Berg et al.

Journal of Cystic Fibrosis 24 (2025) 849–860

(caption on next page)

855

M. Berg et al.

Journal of Cystic Fibrosis 24 (2025) 849–860

Fig. 4. Transcriptome-informed changes in putative intercellular communication in the lungs of pwCF. (A, B) Interaction heatmaps showing receptor-ligand pairs
(‘interactions’) unique to CF (i.e. no identical source-target and associated receptor-ligand combinations detected in either control datasets) centered on interactions
towards (panel A) or from (panel B) B and T cells. (C, D) Circos plots of CF unique interactions between lymphocytes (B cells and CD4+ or CD8+ T cells) and other
cell types. In panel C, the receivers of the signals are lymphocytes; in panel D the lymphocytes are the senders of the signal. (E, F) LIANA dotplot indicating CF unique
interactions between ligands expressed on ‘senders’ (orange) and receptors expressed on receivers (green) unique to indicated cells and only involving differentially
+
expressed genes. In panel E, the senders (orange) of the signals are B, CD4
T cells are the receivers (green). Selected
, or CD8
predicted interactions shown in panels C-F involved at least one differentially expressed gene (FDR < 0.05) in the CF vs. control analysis shown in Fig. 3.

T cells; in panel F the B, CD4

, or CD8

+

+

+

3. Discussion

Aberrant  epithelial-immune  cell  crosstalk  is  at  the  heart  of  many
chronic  inflammatory  diseases  [11].  Whereas  previous  studies  have
focused  separately  on  purified  epithelial  cells  or  immune  cells  from
sputum or BAL, our analysis of the lower airway wall provides the first
single cell CF transcriptome atlas that contains both structural and im-
mune  cells,  allowing
for  hypothesis  generation  on  altered
epithelial-immune cell crosstalk in pwCF. We observed unique changes
in  the composition and transcriptomic  phenotypes of  the airway wall
structural and inflammatory cells in CF compared to healthy subjects,
including marked alterations in the basal cell, endothelial cell, macro-
phage and lymphocyte compartments. Notably, we detected extensive
changes  in  predicted  intercellular  communication  in  pwCF,  including
altered  structural-immune  cell  crosstalk  involving  B  cells,  T  cells  and
druggable  immune  checkpoints  such  as  the  CD94/NKG2A  axis  [42].
Importantly,  pwCF  included  in  this  study  showed  a  mild-to-moderate
disease state in line with beneficial responses to CFTR modulator ther-
apy, suggesting that the observed alterations persist even after rescuing
CFTR  function.  Thus,  the  CF-linked  changes  we  report  here  are  not
linked  to  severe  pulmonary  inflammation  or  disease  exacerbations.
Instead, they appear to associate with chronic low-grade immune acti-
vation and persistent tissue remodeling in adult pwCF, although com-
parisons  of  pre-  and  post-modulator  therapy  samples  are  required  to
draw definite conclusions regarding the precise impact of CFTR modu-
lators. Together, our analyses highlight novel aspects of CF pathophys-
iology and potential entry points for therapy development, while at the
same time providing the field with a unique resource for investigating
changes to cellular composition, phenotypes and potential for crosstalk
in CF lungs.

Our  study  reveals  several  changes  in  the  cell  composition  of  the
airway wall in pwCF. Most notably, we observed a reduced frequency of
basal cells –the primary stem cell of the proximal airways [43] and main
target of genome editing approaches to treat pwCF [44]. Combined with
the highest number of transcriptionally affected genes active in immune
and damage response pathways as well increased potential for altered
cell-cell communication, our findings point towards major dysfunction
of the lung basal cell compartment in pwCF. This is in line with in vitro
studies describing impaired basal cell differentiation in CF [45] and the
emergence of potentially pathogenic basal cell variants in vitro cultures
of end-stage CF lungs [46]. Moreover, scRNA-seq analyses by Carraro
et al. indicated reduced basal cell proliferation and skewed differentia-
tion towards ciliated cells in pwCF [12], supporting our finding of lower
basal cell and higher ciliated cell abundance in the CF airway wall.

We  also  found  an  increase  in  monocytes  and  macrophage  pro-
portions in pwCF. Previous studies of BAL and sputum samples support
an  elevated  presence  of  macrophages  in  moderate-to-severe  CF  [47].
Others reported altered functionality and transcriptomic changes in CF
BAL/sputum monocytes and macrophages [13,47,48]. In contrast, we
detected  very  few  gene  expression  alterations  in  these  myeloid  cell
populations within the airway wall of patients with milder CF, which is
similar to findings reported by Li et al. in their scRNA-seq study of BAL
samples of moderate CF [15]. One possible explanation for these dis-
crepancies  is  the  difference  in  disease  status  at  the  time  of  sampling,
which may impact the phenotypes of innate immune cells.

In  our  dataset,  all  lymphocyte  subsets  displayed  transcriptionally
deregulated  pathways  associated  with  activation.  Furthermore,  T  cell
abundance was increased in pwCF, supporting the notion of a chronic

and aberrant adaptive immune cell activation in CF [49], even in pa-
tients treated with CFTR modulator therapy and with a relatively mild
disease status. Interestingly, our dataset revealed higher expression of
TXNIP and ETS1 in several lymphocyte but also epithelial cell subsets.
TXNIP and ETS1 encode proteins that promote NLRP3 inflammasome
assembly and activation [50], which was recently proposed as a target
for suppressing inflammation in CF [51]. Local hypoxia –present in CF
airways  due  to  mucus  plugs  [52]–  induces  TXNIP  expression  [53],
implying  a  direct  link  between  oxygen  deprivation  and  induction  of
pulmonary inflammation in pwCF. Hypoxia can also cause upregulation
of  VEGF  levels,  thereby  inducing  endothelial  cell  remodeling  [54],
which  is  in  line  with  our  observation  of  altered  proportions  of  endo-
thelial  cells  and  substantial  changes  to  their  transcriptome  in  pwCF.
Genes involved in VEGF signaling were notably upregulated across both
epithelial and immune cells in our dataset, suggesting a significant role
for this pathway in CF pathophysiology. VEGFA, a central mediator of
angiogenesis, has been reported to be elevated in both serum [55–57]
and lung homogenates [58] from pwCF. Moreover, Martin et al. [10]
reported  increased  VEGFA  expression  in  the  CF  airway  epithelium,
implying VEGF signaling in vascular remodeling observed in CF lungs.
Together, these findings warrant further investigation into the role of
hypoxia, VEGF signaling and endothelial cell biology in CF pathophys-
iology [59].

We also observed elevated GNAI2 expression in CD8

T- and B-cells.
GNAI2 is involved in the regulation of adenylate cyclase, which has been
implicated  in  regulating  CFTR  function  and  HCO3-  influx  [60,61].
Moreover, loss of GNAI2 in lymphocytes leads to impaired chemokine
receptor  signaling  and  lymphocyte  trafficking  [62,63].  Future  studies
should explore the role of GNAI2 in lymphocyte biology in pwCF, which
is potentially relevant for both CFTR function and inflammation.

+

+

Analysis of  interaction  potential  revealed  elevated  and  CF-specific
potential  interactions  in  ionocytes  and  macrophages,  often  involving
adaptive  lymphocytes.  T  cells  in  pwCF  also  showed  altered  putative
interactions  with  myeloid  and  endothelial  cells.  For  example,  we
detected an increased interaction between HLA-E expressed on a range
of  cell  types  and  its  receptor  CD94/NKG2A  (encoded  by  KLRD1  and
KLRC1,  respectively)  expressed  on  CD8
T  cells  in  pwCF.  Binding  of
+
HLA-E to CD94/NKG2A on NK or CD8
T cells can inhibit their activity
+
[64].  Additionally,  NKG2A  activation  impairs  CD8
T  and  NK
cell-mediated  immunity  against  cancer  [42,65]  and  respiratory  viral
infections  [66,67].  Hence,  in  pwCF,  chronic  infections  may  lead  to
dysfunctional  CD8
the
HLA-E/CD94/NKG2A immune checkpoint, which could contribute to a
reduced  capacity  for  clearing  infections.  Targeting  this  pathway  with
blocking  antibodies  (e.g.  developed  for  cancer  therapy  [42,65])  may
therefore be considered in CF. However, increased interactions between
HLA-E and CD94 combined with NKG2C (KLRC2) or NKG2E (KLRC3)
were also predicted, which have in contrast been linked to CD8
T cell
activation [68]. Notably, HLA-E expression was shown to be induced in
several cell types by pro-inflammatory cytokines, including IL-6 [69],
which in turn is elevated in sputum and BAL of pwCF [70]. Targeting
IL-6 may thus represent another opportunity to modulate HLA-E activity
in CF.

activation

through

cells

of

T

+

+

Our  study  has  several  limitations.  First,  our  cohort  consists  of  a
relatively low number of CF patients due to the invasiveness of the bi-
opsy  procedure  and  the  significant  clinical  improvement  recently
observed upon triple CFTR modulator treatment. This small sample size
may influence how well our findings can be translated to the broader

856

M. Berg et al.

Journal of Cystic Fibrosis 24 (2025) 849–860

group  of  pwCF,  although  all  individuals  studied  here  did  carry  the
dominant ΔF508 mutation. Second, we used a HC dataset obtained from
two other centers, which may lead to biases due to differences in tissue
processing and exact sampling location. To mitigate these effects, the CF
dataset  was  compared  to  both  HC  datasets  independently  and  only
overlapping  differences  were  considered  robust.  Third,  apart  from  a
minor subset of neutrophil-like cells our dataset largely lacked neutro-
phils, which have previously been shown to be highly relevant for CF
pathophysiology [71]. Neutrophils are notoriously difficult to capture
using  droplet-based  10X  single  cell  RNA-Seq  due  to  their  low  mRNA
content and fragile nature [72,73]. The use of optimized protocols and
alternative  single  cell  sequencing  technologies  could  alleviate  this  in
future studies [72,73]. Finally, further research is required to validate
the predicted interactions, for example using imaging mass cytometry or
spatial transcriptomics applications.

In summary, our study reports the first single-cell RNA-sequencing
dataset derived from complete lung biopsies of pwCF. Our study delivers
novel perspectives on changes in cellular composition, transcriptional
phenotypes and  altered cellular crosstalk unique to  CF, which do not
appear to be resolved by CFTR modulator therapy. These findings will
serve  as  a  valuable  resource  to  the  field  and  open  new  avenues  for
follow-up studies into the pathophysiology of CF.

4. Materials and methods

4.1. Patient recruitment and ethical approval

The  medical  ethics  committees  (METC)  of  the  Erasmus  Medical
Center  and  Groningen  University  Medical  Center  approved  these
studies. Moreover, the Comit´e de Protection des Personnnes Sud Est IV
also  approved  the  study  performed  in  the  UCdA  in  Nice,  France.  All
patients and healthy controls gave their written informed consent. CF
patients were eligible if between 18 and 70 years of age and homozygous
for  the  ΔF508  mutation  or  heterozygous  for  the  ΔF508  mutation  in
combination with a different CFTR mutation. Patient exclusion criteria
were: smoking within the last 3 months, active or treated malignancy,
past  lung  transplantation,  severe  cardiac  decompensation,  unstable
angina,  cardiac  arrhythmias,  recent  myocardial  infarction,  unstable
bronchial asthma, severe impairment of lung function, and severe un-
treated  hypertension.  All  included  patients  volunteered  for  research
bronchoscopies and presented with a mild-to-moderate disease status (%
FEV1 > 40) while receiving CFTR modulator therapy. Healthy controls
were excluded when presenting with a history of smoking >10 pack-
years.

finely  followed  by  tissue  dissociated  for  1  hour  with  a  mixture  of
collagenase D and DNase I (Roche) in HBSS (Lonza). The cell suspension
was filtered, washed and counted and immediately processed for single
cell transcriptomics.

4.3. Single cell transcriptome generation of bronchial cell suspensions

Single cell suspensions were run on a Chromium Single Cell G Chip
and libraries were generated using 10x Chromium Next GEM Single Cell
3′  Reagent  Kit  v3.1  (10x  Genomics)  according  to  the  manufacturer’s
protocol. Single cell sequencing was performed on a Novaseq6000 sys-
tem (Illumina, San Diego, USA), using an S2 v1.5 100 cycles flow cell
(Illumina) with run settings 28–10–10–90 cycles. Very similar protocols
were  used  to  generate  the  UCdA  [25]  and  UMCG  datasets  [26],  see
references for detailed information.

4.4. Data processing and cell annotation

Sequencing data were re-mapped and counted with 10x Genomics
Cell  Ranger  6.0.2  software  using  the  10x  Genomics  GRCh38–2020-A
reference transcriptome with the “include introns” option enabled. Cell
Ranger Single-Cell Software Suite v2.3.0 was used to perform sample
demultiplexing,  barcode  processing  and  single-cell  3′  gene  counting
using default parameters. Subsequent transcriptome analysis was per-
formed using Seurat version 4.3.0 [74]. Samples were filtered to only
contain cells with 200 or more expressed genes, <25 % mitochondrial
RNA, and fewer than 10 counts of HBB. All samples were then merged
and integrated using FastMNN28 version 1.4 with the Seurat wrapper.
We calculated the UMAP based on the first 30 principal components.
Cell selection and labels for the samples from the UMCG were taken from
the  Human  Lung  Cell  Atlas  (HLCA).  The  HLCA  reference  model  for
SCArches  [29]  version  0.5.3  was  used  to  obtain  cell  labels  using  the
default  settings  for  label  transfer  for  the  other  samples.  The  level  of
precision of the transfer labels was chosen based on the number of cells
per subset, expected biological relevance, and statistical considerations.
Upon inspection, one population labeled “unknown” was manually an-
notated as CD8
T cells based on marker gene expression and proximity
on the UMAP. Other cells lacking annotation labels and cells annotated
as alveolar epithelium were removed. Cell cycle scoring was performed
using the CellCycleScoring function of the Seurat R package. A cellXgene
object  containing  the  single  cell  transcriptome  dataset  generated  and
analysed  in  this  study  can be  interactively  explored  at:  https://cellxg
ene.cziscience.com/collections/54004c5c-af08–4693-a606–73871b6
ef989.

+

4.2. Bronchial biopsy collection and processing

4.5. Differential abundance testing

◦

EMC:  3–5  biopsies  were  taken  per  patient  from  the  carina  during
bronchoscopies under local anesthesia. Biopsies were collected in 5 mL
RPMI  + 10  %  FCS  + 10  µL  Rho  K  inhibitor  (10  µM).  Single-cell  sus-
pensions  were  obtained  by  mincing  the  biopsies  finely  followed  by
enzymatic digestion with RPMI + Liberase TM (125 µg/mL) + DNase
(0.1 mg/mL) + Rho kinase inhibitor (10 µM) for 30 min at 37
C. Cells
were washed with 20 mL RPMI + 10 % FCS + Rho K inhibitor (10 µM),
filtered through 70 µm filter and immediately processed for single cell
transcriptomics. UCdA: For detailed information see [25].  Briefly, bi-
opsies  were  taken from the  carina during  bronchoscopies under local
anesthesia.  Tissue  samples  were  dissociated  for  1  hour  using  Bacillus
Licheniformis protease (Sigma-Aldrich, P5380). After 1 hour, the biopsy
was  finely minced and  returned to dissociation  buffer. Next, protease
activity  was  inactivated,  cells  were  washed,  filtered  and  immediately
processed for single cell transcriptomics. UMCG: For detailed informa-
tion see [26]. Briefly: bronchoscopies were performed during conscious
sedation. Six macroscopically adequate biopsies were collected located
between the third and sixth generation of the right lower and middle
lobe.  Single  cell  suspensions  were  obtained  by  mincing  the  biopsies

To  perform  differential  abundance  testing  we  used  a  binomial
generalized  linear  mixed  effects  model  using  the  R  package  lme4
(version 1.1–34). For each cell type we created a 0/1 identity vector (i.e.
indicating per cell if it belonged to that cell type) and tested if the odds of
being that cell type is higher in pwCF as compared to healthy controls,
using donor and source laboratory as co-variates. Formula used: Celltype
~ disease + 1|donor + 1|source lab. To test for statistical significance,
we use the emmeans R package (version 1.8.8) to create a confidence
interval.

4.6. Differential gene expression analysis and cell-cell interaction
prediction

Differential gene expression analyses were performed separately for
EMC vs. UMCG and EMC vs. UCdA using aggregate counts per donor per
cell type. These were normalized and tested for differential expression
using  edgeR  version  3.40.2  [75].  Differential  expression  analysis  was
performed using the qlf-fit model, with the nominally significant (P <
0.05) results concatenated and FDR adjusted. For pathway analysis we

857

M. Berg et al.

Journal of Cystic Fibrosis 24 (2025) 849–860

used  Metascape  (http://metascape.org [76])  with  default  settings.
Interaction analyses were performed separately on all samples from each
institution  using  LIANA  [36]  with  100  permutations.  LIANA  includes
interactions between secreted ligands and plasma membrane receptors,
secreted  enzymes,  extracellular  matrix  proteins,  transporters,  and  in-
teractions  that  require  the  physical  contact  between  cells,  such  as
cell-cell  adhesion  proteins  and  gap  junctions.  First,  each  dataset  was
individually filtered for statistically significant interactions (aggregate
rank P < 0.05). Next, any interactions in the pwCF dataset that matched
the  source-target  pairs  and  receptor-ligand  combinations  present  in
either control dataset were removed to identify interactions unique to
pwCF  (‘CF  unique’  interactions).  Interactions  detected  in  both  HC
identical  source-target  and  associated
datasets  and  with  no
receptor-ligand combinations in the pwCF dataset were considered ‘HC
unique’  interactions.  Interaction  figures  were  made  using  LIANA  and
CCPlot.

Data statement

The  authors  confirm  that  the  data  supporting  the  findings  of  this
study are available within the article and its Supplementary material. A
cellXgene  object  containing  the  single  cell  transcriptome  dataset
generated and analysed in this study can be interactively explored at: htt
ps://cellxgene.cziscience.com/collections/54004c5c-af08-469
3-a606-73871b6ef989. Code used to perform the analyses and produce
the  figures  in  this  study  can  be  found  on  GitHub:  https://github.
com/R-stadhouders/Berg-Krabbendam-et-al.analysis-scripts.

potential competing interests.

Acknowledgements

We thank all members from the Stadhouders, Hendriks and Nawijn
laboratories for helpful discussions. We are grateful to all patients that
donated samples for our study.

Funding

This  work  was  made  possible  by  generous  support  from  TAAI
Foundation  (Grant  number:  NL76489.078.21).  R.W.H.  is  further  sup-
ported  by  Dutch  Lung  Foundation  grant  4.1.18.226.  R.S.  is  further
supported by a Dutch Research Council Vidi grant (09150172010068),
an  Erasmus  MC  Fellowship,  and  a  Dutch  Lung  Foundation  Junior
Investigator grant (4.2.19.041JO). This work was supported by grants
from the French government managed by the Agence Nationale de la
Recherche  under  the  France  2030  programme  (Respirera:  ANR-23-
IAHU-0007,  4D-OMICs:  ANR-21-ESRE-0052,  3IA:  ANR-19-P3IA-0002)
and Conseil d´epartemental 06 (2016–294DGADSH–CV). Support from
the National Infrastructure France  G´enomique to PB is acknowledged
(ANR-10-INBS-09–02, ANR-10-INBS-09–03).

Supplementary materials

Supplementary material associated with this article can be found, in

the online version, at doi:10.1016/j.jcf.2025.01.016.

Data availability

References

Code used to perform the analyses and produce the figures in this
study can be found on GitHub: https://github.com/R-stadhouders/Berg-
Krabbendam-et-al.analysis-scripts.

CRediT authorship contribution statement

Marijn  Berg:  Data curation,  Formal  analysis, Investigation,  Meth-
odology, Visualization, Writing – original draft. Lisette Krabbendam:
Conceptualization,  Data  curation,  Formal  analysis,  Investigation,
Methodology, Visualization, Writing – original draft. Esmee K. van der
Ploeg: Formal analysis, Investigation, Visualization, Writing – original
draft. Menno van Nimwegen: Data curation, Investigation, Methodol-
ogy,  Writing  –  review  &  editing.  Tjeerd  van  der  Veer:  Resources,
Writing – review & editing. Martin Banchero: Investigation, Method-
ology, Writing –  review &  editing. Orestes A. Carpaij: Investigation,
Methodology,  Writing  –  review  &  editing.  Remco  Hoogenboezem:
Data curation, Methodology, Writing – review & editing. Maarten van
den  Berge:  Resources,  Writing  –  review  &  editing.  Eric  Bindels:
Investigation, Methodology, Writing – review & editing. Joachim G.J.
V.  Aerts:  Funding  acquisition,  Writing  –  review  &  editing.  Antoine
Collin:  Resources,  Writing  –  review  &  editing.  Pascal  Barbry:  Re-
sources, Writing – review & editing. Lieke S. Kamphuis: Investigation,
Methodology,  Funding  acquisition,  Resources,  Writing  –  review  &
editing. Rudi W. Hendriks: Conceptualization, Supervision, Writing –
original  draft.  Martijn  C.  Nawijn:  Conceptualization,  Data  curation,
Supervision,  Writing  –  original  draft.  Ralph  Stadhouders:  Conceptu-
alization,  Data  curation,  Funding  acquisition,  Methodology,  Supervi-
sion, Validation, Visualization, Writing – original draft.

Declaration of competing interest

The  authors  declare  the  following  financial  interests/personal  re-
lationships which may be considered as potential competing interests:

JGJVA reports grants or consulting fees from Boehringer-Ingelheim,
MSD,  BMS,  Astra-Zeneca,  Eli-Lilly,  Verastem,  Nutricia,  Amphera  and
CureVac, which are not related to this work. All other authors declare no

[1] Shteinberg M, Haq IJ, Polineni D, Davies JC. Cystic fibrosis. Lancet 2021;397

(10290):2195–211.

[2] Bojanowski CM, Lu S, Kolls JK. Mucosal immunity in cystic Fibrosis. J Immunol

2021;207(12):2901–12.

[3] Shteinberg M, Taylor-Cousar JL. Impact of CFTR modulator use on outcomes in
people with severe cystic fibrosis lung disease. Eur Respir Rev 2020;29(155).
[4] Purkayastha D, Agtarap K, Wong K, Pereira O, Co J, Pakhale S, Kanji S. Drug-drug
interactions with CFTR modulator therapy in cystic fibrosis: focus on Trikafta(R)/
Kaftrio(R). J Cyst Fibros 2023;22(3):478–83.

[5] Schnell A, Hober H, Kaiser N, Ruppel R, Geppert A, Tremel C, et al. Elexacaftor -
Tezacaftor - Ivacaftor treatment improves systemic infection parameters and
Pseudomonas aeruginosa colonization rate in patients with cystic fibrosis a
monocentric observational study. Heliyon 2023;9(5):e15756.

[6] Lepissier A, Bonnel AS, Wizla N, Weiss L, Mittaine M, Bessaci K, et al. Moving the
dial on airway inflammation in response to Trikafta in adolescents with cystic
fibrosis. Am J Respir Crit Care Med 2023;207(6):792–5.

[7] Allen L, Allen L, Carr SB, Davies G, Downey D, Egan M, et al. Future therapies for

cystic fibrosis. Nat Commun 2023;14(1):693.

[8] Schaupp L, Addante A, Voller M, Fentker K, Kuppe A, Bardua M, et al. Longitudinal
effects of elexacaftor/tezacaftor/ivacaftor on sputum viscoelastic properties,
airway infection and inflammation in patients with cystic fibrosis. Eur Respir J
2023;62(2).

[9] Tunney MM, Wark P. Long-term therapy with elexacaftor/tezacaftor/ivacaftor

(ETI) in cystic fibrosis: improved clinical outcomes but infection and inflammation
persist. Eur Respir J 2023;62(2).

[10] Martin C, Coolen N, Wu Y, Thevenot G, Touqui L, Pruliere-Escabasse V, et al. CFTR
dysfunction induces vascular endothelial growth factor synthesis in airway
epithelium. Eur Respir J 2013;42(6):1553–62.

[11] Hewitt RJ, Lloyd CM. Regulation of immune responses by the airway epithelial cell

landscape. Nat Rev Immunol 2021;21(6):347–62.

[12] Carraro G, Langerman J, Sabri S, Lorenzana Z, Purkayastha A, Zhang G, et al.

Transcriptional analysis of cystic fibrosis airways at single-cell resolution reveals
altered epithelial cell states and composition. Nat Med 2021;27(5):806–14.
[13] Schupp JC, Khanal S, Gomez JL, Sauler M, Adams TS, Chupp GL, et al. Single-cell
transcriptional archetypes of airway inflammation in cystic fibrosis. Am J Respir
Crit Care Med 2020;202(10):1419–29.

[14] Maksimovic J., Shanthikumar S., Howitt G., Hickey P.F., Ho W., Anttila C., et al.
Single-cell atlas of bronchoalveolar lavage from preschool cystic fibrosis reveals
new cell phenotypes. BioRxiv. 2022:2022.06.17.496207.

[15] Li X, Kolling FW, Aridgides D, Mellinger D, Ashare A, Jakubzick CV. ScRNA-seq
expression of IFI27 and APOC2 identifies four alveolar macrophage superclusters
in healthy BALF. Life Sci Alliance 2022;5(11).

[16] Polverino F, Lu B, Quintero JR, Vargas SO, Patel AS, Owen CA, et al. CFTR

regulates B cell activation and lymphoid follicle development. Respir Res 2019;20
(1):133.

[17] Ratner D, Mueller C. Immune responses in cystic fibrosis: are they intrinsically

defective? Am J Respir Cell Mol Biol 2012;46(6):715–22.

858

M. Berg et al.

Journal of Cystic Fibrosis 24 (2025) 849–860

[18] Bruscia EM, Bonfield TL. Update on Innate and adaptive immunity in Cystic

Fibrosis. Clin Chest Med 2022;43(4):603–15.

[19] Tiringer K, Treis A, Fucik P, Gona M, Gruber S, Renner S, et al. A Th17- and Th2-
skewed cytokine profile in cystic fibrosis lungs represents a potential risk factor for
Pseudomonas aeruginosa infection. Am J Respir Crit Care Med 2013;187(6):621–9.
[20] Kushwah R, Gagnon S, Sweezey NB. Intrinsic predisposition of naive cystic fibrosis
T cells to differentiate towards a Th17 phenotype. Respir Res 2013;14(1):138.
[21] Hartl D, Griese M, Kappler M, Zissel G, Reinhardt D, Rebhan C, et al. Pulmonary T

[47] Leveque M, Le Trionnaire S, Del Porto P, Martin-Chouly C. The impact of impaired
macrophage functions in cystic fibrosis disease progression. J Cyst Fibros 2017;16
(4):443–53.

[48] Slimmen LJM, Giacalone VD, Schofield C, Horati H, Manai B, Estevao SC, et al.

Airway macrophages display decreased expression of receptors mediating and
regulating scavenging in early cystic fibrosis lung disease. Front Immunol 2023;14:
1202009.

[49] Giacalone VD, Dobosh BS, Gaggar A, Tirouvanziam R, Margaroli C.

(H)2 response in Pseudomonas aeruginosa-infected patients with cystic fibrosis.
J Allergy Clin Immunol 2006;117(1):204–11.

Immunomodulation in Cystic Fibrosis: why and how? Int J Mol Sci 2020;21(9).

[50] Mohamed IN, Ishrat T, Fagan SC. El-Remessy AB. Role of inflammasome activation

[22] Moss RB, Bocian RC, Hsu YP, Dong YJ, Kemna M, Wei T, Gardner P. Reduced IL-10
secretion by CD4+ T lymphocytes expressing mutant cystic fibrosis transmembrane
conductance regulator (CFTR). Clin Exp Immunol 1996;106(2):374–88.

[23] Hector A, Schafer H, Poschel S, Fischer A, Fritzsching B, Ralhan A, et al. Regulatory
T-cell impairment in cystic fibrosis patients with chronic pseudomonas infection.
Am J Respir Crit Care Med 2015;191(8):914–23.

[24] Januska MN, Walsh MJ. Single-cell RNA sequencing reveals new basic and

translational insights in the Cystic fibrosis lung. Am J Respir Cell Mol Biol 2023;68
(2):131–9.

[25] Deprez M, Zaragosi LE, Truchi M, Becavin C, Ruiz García S, Arguel MJ, et al.

A single-cell atlas of the Human healthy airways. Am J Respir Crit Care Med 2020;
202(12):1636–45.

[26] Vieira Braga FA, Kar G, Berg M, Carpaij OA, Polanski K, Simon LM, et al. A cellular
census of human lungs identifies novel cell states in health and in asthma. Nat Med
2019;25(7):1153–63.

[27] Haghverdi L, Lun ATL, Morgan MD, Marioni JC. Batch effects in single-cell RNA-
sequencing data are corrected by matching mutual nearest neighbors. Nat.
Biotechnol. 2018;36(5):421–7.

[28] Sikkema L, Ramírez-Su´astegui C, Strobl DC, Gillett TE, Zappia L, Madissoon E,

et al. An integrated cell atlas of the lung in health and disease. Nat. Med. 2023;29
(6):1563–77.

[29] Lotfollahi M, Naghipourfar M, Luecken MD, Khajavi M, Büttner M,

Wagenstetter M, et al. Mapping single-cell data to reference atlases by transfer
learning. Nat. Biotechnol. 2022;40(1):121–30.

[30] Megill C., Martin B., Weaver C., Bell S., Prins L., Badajoz S., et al. cellxgene: a

performant, scalable exploration platform for high dimensional sparse matrices.
2021:2021.04.05.438318.

[31] Plasschaert LW, Zilionis R, Choo-Wing R, Savova V, Knehr J, Roma G, et al.
A single-cell atlas of the airway epithelium reveals the CFTR-rich pulmonary
ionocyte. Nature 2018;560(7718):377–81.

[32] Montoro DT, Haber AL, Biton M, Vinarsky V, Lin B, Birket SE, et al. A revised

airway epithelial hierarchy includes CFTR-expressing ionocytes. Nature 2018;560
(7718):319–24.

[33] Kormann MSD, Dewerth A, Eichner F, Baskaran P, Hector A, Regamey N, et al.
Transcriptomic profile of cystic fibrosis patients identifies type I interferon
response and ribosomal stalk proteins as potential modifiers of disease severity.
PLoS One 2017;12(8):e0183526.

[34] Sagi Y, Landrigan A, Levy R, Levy S. Complementary costimulation of human T-cell
subpopulations by cluster of differentiation 28 (CD28) and CD81. Proc Natl Acad
Sci U S A. 2012;109(5):1613–8.

[35] Simons M, Gordon E, Claesson-Welsh L. Mechanisms and regulation of endothelial

VEGF receptor signalling. Nat Rev Mol Cell Biol 2016;17(10):611–25.

in the pathophysiology of vascular diseases of the neurovascular unit. Antioxid
Redox Signal 2015;22(13):1188–206.

[51] McElvaney OJ, Zaslona Z, Becker-Flegler K, Palsson-McDermott EM, Boland F,

Gunaratnam C, et al. Specific inhibition of the NLRP3 inflammasome as an
antiinflammatory strategy in Cystic fibrosis. Am J Respir Crit Care Med 2019;200
(11):1381–91.

[52] Boucher RC. Muco-obstructive lung diseases. N Engl J Med 2019;380(20):1941–53.
[53] Li Y, Miao LY, Xiao YL, Huang M, Yu M, Meng K, Cai HR. Hypoxia induced high
expression of thioredoxin interacting protein (TXNIP) in non-small cell lung cancer
and its prognostic effect. Asian Pac J Cancer Prev 2015;16(7):2953–8.
[54] Montgomery ST, Mall MA, Kicic A, Stick SM, Arest CF. Hypoxia and sterile

inflammation in cystic fibrosis airways: mechanisms and potential therapies. Eur
Respir J 2017;49(1).

[55] McColley SA, Stellmach V, Boas SR, Jain M, Crawford SE. Serum vascular

endothelial growth factor is elevated in cystic fibrosis and decreases with treatment
of acute pulmonary exacerbation. Am J Respir Crit Care Med 2000;161(6):
1877–80.

[56] Meyer KC, Cardoni A, Xiang ZZ. Vascular endothelial growth factor in
bronchoalveolar lavage from normal subjects and patients with diffuse
parenchymal lung disease. J Lab Clin Med 2000;135(4):332–8.

[57] Watts KD, McColley SA. Elevated vascular endothelial growth factor is correlated
with elevated erythropoietin in stable, young cystic fibrosis patients. Pediatr
Pulmonol 2011;46(7):683–7.

[58] Krenn K, Klepetko W, Taghavi S, Paulus P, Aharinejad S. Vascular endothelial

growth factor increases pulmonary vascular permeability in cystic fibrosis patients
undergoing lung transplantation. Eur J Cardiothorac Surg 2007;32(1):35–41.
[59] Declercq M, Treps L, Carmeliet P, Witters P. The role of endothelial cells in cystic

fibrosis. J Cyst Fibros 2019;18(6):752–61.

[60] Baudouin-Legros M, Hamdaoui N, Borot F, Fritsch J, Ollero M, Planelles G,
Edelman A. Control of basal CFTR gene expression by bicarbonate-sensitive
adenylyl cyclase in human pulmonary cells. Cell Physiol Biochem 2008;21(1–3):
75–86.

[61] Sun XC, Zhai CB, Cui M, Chen Y, Levin LR, Buck J, Bonanno JA. HCO(3)

(-)-dependent soluble adenylyl cyclase activates cystic fibrosis transmembrane
conductance regulator in corneal endothelium. Am J Physiol Cell Physiol 2003;284
(5):C1114–22.

[62] Han SB, Moratz C, Huang NN, Kelsall B, Cho H, Shi CS, et al. Rgs1 and Gnai2

regulate the entrance of B lymphocytes into lymph nodes and B cell motility within
lymph node follicles. Immunity 2005;22(3):343–54.

[63] Hwang IY, Park C, Kehrl JH. Impaired trafficking of Gnai2± and Gnai2-/- T

lymphocytes: implications for T cell movement within lymph nodes. J Immunol
2007;179(1):439–48.

[36] Dimitrov D, Turei D, Garrido-Rodriguez M, Burmedi PL, Nagai JS, Boys C, et al.

[64] Wang X, Xiong H, Ning Z. Implications of NKG2A in immunity and immune-

Comparison of methods and resources for cell-cell communication inference from
single-cell RNA-seq data. Nat Commun 2022;13(1):3224.

[37] Boularan C, Kehrl JH. Implications of non-canonical G-protein signaling for the

immune system. Cell Signal 2014;26(6):1269–82.

[38] Ogden CA, deCathelineau A, Hoffmann PR, Bratton D, Ghebrehiwet B, Fadok VA,

Henson PM. C1q and mannose binding lectin engagement of cell surface
calreticulin and CD91 initiates macropinocytosis and uptake of apoptotic cells.
J Exp Med 2001;194(6):781–95.

[39] Eugene J, Jouand N, Ducoin K, Dansette D, Oger R, Deleine C, et al. The inhibitory

receptor CD94/NKG2A on CD8(+) tumor-infiltrating lymphocytes in colorectal
cancer: a promising new druggable immune checkpoint in the context of HLAE/
beta2m overexpression. Mod Pathol 2020;33(3):468–82.

[40] Abd Hamid M, Wang RZ, Yao X, Fan P, Li X, Chang XM, et al. Enriched HLA-E and

CD94/NKG2A interaction limits antitumor CD8(+) tumor-infiltrating T
lymphocyte responses. Cancer Immunol Res 2019;7(8):1293–306.

[41] Masilamani M, Nguyen C, Kabat J, Borrego F, Coligan JE. CD94/NKG2A inhibits
NK cell activation by disrupting the actin network at the immunological synapse.
J Immunol 2006;177(6):3590–6.

[42] Andre P, Denis C, Soulas C, Bourbon-Caillet C, Lopez J, Arnoux T, et al. Anti-
NKG2A mAb is a checkpoint inhibitor that promotes Anti-tumor immunity by
unleashing both T and NK cells. Cell 2018;175(7):1731–43. e13.

mediated diseases. Front Immunol 2022;13:960852.

[65] van Montfoort N, Borst L, Korrer MJ, Sluijter M, Marijt KA, Santegoets SJ, et al.

NKG2A Blockade potentiates CD8 T cell immunity induced by cancer vaccines.
Cell. 2018;175(7):1744–55. e15.

[66] Zhou J, Matsuoka M, Cantor H, Homer R, Enelow RI. Cutting edge: engagement of
NKG2A on CD8+ effector T cells limits immunopathology in influenza pneumonia.
J Immunol 2008;180(1):25–9.

[67] Gangaev A, Ketelaars SLC, Isaeva OI, Patiwael S, Dopler A, Hoefakker K, et al.
Identification and characterization of a SARS-CoV-2 specific CD8(+) T cell
response with immunodominant features. Nat Commun 2021;12(1):2593.
[68] Guma M, Busch LK, Salazar-Fontana LI, Bellosillo B, Morte C, Garcia P, Lopez-
Botet M. The CD94/NKG2C killer lectin-like receptor constitutes an alternative
activation pathway for a subset of CD8+ T cells. Eur J Immunol 2005;35(7):
2071–80.

[69] Pereira BI, Devine OP, Vukmanovic-Stejic M, Chambers ES, Subramanian P,

Patel N, et al. Senescent cells evade immune clearance via HLA-E-mediated NK and
CD8(+) T cell inhibition. Nat Commun 2019;10(1):2387.

[70] Nixon LS, Yung B, Bell SC, Elborn JS, Shale DJ. Circulating immunoreactive

interleukin-6 in cystic fibrosis. Am J Respir Crit Care Med 1998;157(6):1764–9. Pt
1.

[71] Wang G, Nauseef WM. Neutrophil dysfunction in the pathogenesis of cystic

[43] Wells JM, Watt FM. Diverse mechanisms for endogenous regeneration and repair in

fibrosis. Blood 2022;139(17):2622–31.

mammalian organs. Nature 2018;557(7705):322–8.

[44] King NE, Suzuki S, Barilla C, Hawkins FJ, Randell SH, Reynolds SD, et al.

Correction of airway stem cells: genome editing approaches for the treatment of
cystic fibrosis. Hum Gene Ther 2020;31(17–18):956–72.

[45] Adam D, Roux-Delrieu J, Luczka E, Bonnomet A, Lesage J, Merol JC, et al. Cystic

fibrosis airway epithelium remodelling: involvement of inflammation. J Pathol
2015;235(3):408–19.

[46] Wang S, Niroula S, Hoffman A, Khorrami M, Khorrami M, Yuan F, et al.

Inflammatory activity of epithelial stem cell variants from cystic fibrosis lungs is
not resolved by CFTR modulators. Am J Respir Crit Care Med 2023;208(9):930–43.

[72] Salcher S, Sturm G, Horvath L, Untergasser G, Kuempers C, Fotakis G, et al. High-
resolution single-cell atlas reveals diversity and plasticity of tissue-resident
neutrophils in non-small cell lung cancer. Cancer Cell 2022;40(12):1503–20. e8.
[73] Wang L, Liu Y, Dai Y, Tang X, Yin T, Wang C, et al. Single-cell RNA-seq analysis
reveals BHLHE40-driven pro-tumour neutrophils with hyperactivated glycolysis in
pancreatic tumour microenvironment. Gut 2023;72(5):958–71.

859

M. Berg et al.

Journal of Cystic Fibrosis 24 (2025) 849–860

[74] Hao Y, Hao S, Andersen-Nissen E, Mauck 3rd WM, Zheng S, Butler A, et al.

[76] Zhou Y, Zhou B, Pache L, Chang M, Khodabakhshi AH, Tanaseichuk O, et al.

Integrated analysis of multimodal single-cell data. Cell 2021;184(13):3573–87.
e29.

[75] Robinson MD, McCarthy DJ, Smyth GK. edgeR: a bioconductor package for

differential expression analysis of digital gene expression data. Bioinformatics
2010;26(1):139–40.

Metascape provides a biologist-oriented resource for the analysis of systems-level
datasets. Nat Commun 2019;10(1):1523.

860

