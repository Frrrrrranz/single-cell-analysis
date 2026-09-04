nature metabolism
Article https://doi.org/10.1038/s42255-023-00876-x
Delineating mouse β-cell identity during
lifetime and in diabetes with a single cell atlas
Received: 21 December 2022 Karin Hrovatin 1,2, Aimée Bastidas-Ponce 3,4,5, Mostafa Bakhti 3,4,
Luke Zappia 1,6, Maren Büttner 1,7,8, Ciro Salinno3,4,5, Michael Sterr3,4,
Accepted: 26 July 2023
Anika Böttcher 3,4, Adriana Migliorini3,4,9, Heiko Lickert 3,4,5
Published online: 11 September 2023 & Fabian J. Theis 1,2,6
Check for updates
Although multiple pancreatic islet single-cell RNA-sequencing (scRNA-seq)
datasets have been generated, a consensus on pancreatic cell states in
development, homeostasis and diabetes as well as the value of preclinical
animal models is missing. Here, we present an scRNA-seq cross-condition
mouse islet atlas (MIA), a curated resource for interactive exploration
and computational querying. We integrate over 300,000 cells from nine
scRNA-seq datasets consisting of 56 samples, varying in age, sex and
diabetes models, including an autoimmune type 1 diabetes model (NOD),
a glucotoxicity/lipotoxicity type 2 diabetes model (db/db) and a chemical
streptozotocin β-cell ablation model. The β-cell landscape of MIA reveals
new cell states during disease progression and cross-publication differences
between previously suggested marker genes. We show that β-cells in the
streptozotocin model transcriptionally correlate with those in human type
2 diabetes and mouse db/db models, but are less similar to human type 1
diabetes and mouse NOD β-cells. We also report pathways that are shared
between β-cells in immature, aged and diabetes models. MIA enables a
comprehensive analysis of β-cell responses to different stressors, providing a
roadmap for the understanding of β-cell plasticity, compensation and demise.
The major hallmark of diabetes mellitus is impaired glucose homeo- surgery and islet transplantation, are highly invasive or can be only
stasis. Blood glucose is regulated by multiple hormones secreted from offered to a small number of patients2–4. The central role of β-cells in
pancreatic islets of Langerhans that consist of insulin-producing β-cells, diabetes development urges the establishment of new therapies that
which are main acters in diabetes, as well as glucagon-producing α-cells, focus on restoring β-cell mass and function4,5. Achieving such strategies
somatostatin-producing δ-cells, pancreatic polypeptide-producing requires a deeper understanding of β-cell heterogeneity, maturation,
γ-cells and ghrelin-producing ε-cells1. Type 1 diabetes (T1D) and type function and failure6–8.
2 diabetes (T2D) arise due to the loss or progressive dysfunction of Shortly after birth, β-cells are immature, defined by poor glucose-
β-cells, respectively. Current anti-diabetic medications do not lead stimulated insulin secretion (GSIS)9. Immature β-cells gain functional
to remission, whereas more-effective treatments, such as bariatric maturation, as defined by the expression of several protein markers,
1Institute of Computational Biology, Helmholtz Zentrum München, Neuherberg, Germany. 2TUM School of Life Sciences Weihenstephan, Technical
University of Munich, Freising, Germany. 3Institute of Diabetes and Regeneration Research, Helmholtz Zentrum München, Neuherberg, Germany.
4German Center for Diabetes Research (DZD), Neuherberg, Germany. 5Medical Faculty, Technical University of Munich, Munich, Germany.
6Department of Mathematics, Technical University of Munich, Garching, Germany. 7Genomics and Immunoregulation, Life & Medical Sciences
(LIMES) Institute, University of Bonn, Bonn, Germany. 8Systems Medicine, Deutsches Zentrum für Neurodegenerative Erkrankungen (DZNE), Bonn,
Germany. 9McEwen Stem Cell Institute, University Health Network (UHN), Toronto, Ontario, Canada. e-mail: heiko.lickert@helmholtz-muenchen.de;
fabian.theis@helmholtz-muenchen.de
Nature Metabolism | Volume 5 | September 2023 | 1615–1637 1615

Article https://doi.org/10.1038/s42255-023-00876-x
a b
Mouse pancreatic islet scRNA seq atlas Exploring islet and β cell biology
9 heterogeneous datasets Endocrine cell Diabetes models and
>300,000 cells comparison dysfunction states
β
α δ
Immature
Sex Pathway 1
Age
Diabetes β cell heterogeneity Validation and
Chemical >100,000 cells human comparison
stress
Aged Immature
male T1D
Aged
female T2D
Adult
Chem
c
Insights beyond individual datasets
Capture Comparison of Gene Conserved
heterogeneity multiple phenotypes contextualization patterns
Compared specific cell states
Datasets
Dataset Genes Conserved
All cell states
Cell
manifold Gene
groups
d
Atlas as a resource
Interactive Curated Cell state Atlas
exploration data collection contextualization extension
Atlas
New
dataset
including Urocortin-3, Flattop, transcription factor MafA and glucose senescence-associated secretory phenotype in T1D20,27. β-cell identity
transporter encoded by Slc2a2 (also known as Glut2) and accurate can also be disrupted due to chemical stress28 and the streptozotocin
GSIS in the first weeks after birth and again after weaning9–12. Adult (STZ)-induced ablation of β-cells was previously used to study both
β-cells also differ within and across phenotypes and conditions7,11. T1D and T2D29–31. Yet, due to failed clinical translation of treatments
For instance, insulin production and secretion of β-cells are changed showing promise in animal models, it is important to decipher to which
due to healthy aging or stress-induced senescence13–17. The function extent models resemble human diabetes25.
also differs between sexes, with male β-cells having transcriptomic The implication of single-cell RNA sequencing (scRNA-seq) has
signatures more akin to T2D18. greatly enhanced our understanding of β-cell maturation, heterogene-
Different stressors can lead to β-cell failure, which is often studied ity and function in health and disease1,30,32–35. Nevertheless, there is no
with mouse models19,20. T2D is marked by gluco-/lipotoxicity leading consensus on which β-cell populations exist6,8,36 and which pathways
to β-cell dedifferentiation, compensatory insulin production and lead to β-cell dysfunction in different conditions. For example, for T2D
resulting endoplasmic reticulum (ER) stress21,22, all of which are also progression alone, previous studies used different systems and indi-
present in the hyperphagic mouse db/db model23,24. In contrast, T1D vidually identified various molecular changes, associated with energy
is caused by autoimmune attack against β-cells25,26 that is mirrored metabolism, compensatory insulin secretion, apoptosis, inflammation,
by the mouse non-obese diabetic (NOD) model, which was also used dedifferentiation and disrupted islet communication32,37,38. This ambi-
to show the importance of β-cell stress-induced senescence and guity can be attributed to heterogeneous cellular states, joint action of
Nature Metabolism | Volume 5 | September 2023 | 1615–1637 1616
2
yawhtaP
STZ db/db NOD
Aged
Adult
Fig. 1 | The MIA of scRNA-seq datasets across conditions offers new insights b, Putative new biological insights. c, Analyses enabled by MIA that would not have
into islet and β-cell biology. a, MIA content, including different conditions: been possible on individual datasets. d, Potential use cases of MIA as a resource
sex, age, diabetes models (STZ, db/db and NOD) and anti-diabetic treatments for future studies.
and chemical stress (application of different chemicals such as FoxO inhibitor).

Article https://doi.org/10.1038/s42255-023-00876-x
multiple molecular mechanisms, different stressors and confounding hyperparameter selection (Fig. 2b), as discussed in Supplementary
of unknown environmental factors26,32,35,38,39. Such complexity cannot Note 1. The integrated atlas shows clear separation into clusters that
be fully captured in datasets of individual studies. Hence, a combined correspond to distinct cell types (Fig. 2e and Extended Data Fig. 1a–c)
analysis of multiple datasets is needed to comprehensively describe that colocalize across datasets (Fig. 2d).
β-cell heterogeneity in health and disease and to disentangle molecular As the available cell type annotation was incomplete and inconsist-
pathways contributing to the deterioration of glucose homeostasis in ent across datasets (Extended Data Fig. 1c,d) we manually re-annotated
various dysfunction conditions. the integrated embedding (Fig. 2e,f and Extended Data Fig. 1a). This
Direct comparison of multiple scRNA-seq datasets generated by enabled us to resolve cell populations that were not annotated in some
different scientific groups is often not possible due to batch effects. of the original studies, potentially because low cell numbers hamper
To circumvent this, multiple scRNA-seq data analysis and integra- annotation48. For example, we found that Schwann cells (617 out of
tion40–43 approaches have been proposed. This also enabled the crea- 301,796 atlas cells) were present across the studies (Extended Data
tion of so-called ‘integrated atlases’ that provide an expertly curated Fig. 2), although they were not annotated in any individual dataset
resource with a high-quality embedding optimized to retain biologi- (Extended Data Fig. 1d). Similarly, none of the original annotations
cal variation, while removing batch effects. Atlases have become an distinguished between activated and quiescent stellate cells and
invaluable tool as they provide new insights beyond individual data- some of the studies did not annotate stellate cells at all (Extended Data
sets, such as the description of the cellular landscape in health and Fig. 1d and Extended Data Fig. 2).
disease, and comparison across animal or in vitro models and cor- Additionally, we also observed populations influenced by tech-
responding human datasets44–46. While previous efforts have been nical artifacts that colocalized across datasets, namely a low-quality
made to compare the results of multiple islet scRNA-seq studies18,35,47, cluster (lowQ, 853 cells, as well as low-quality cells identified based on a
a comprehensive integrated atlas of mouse pancreatic islet cells across more detailed analysis of individual cell type clusters, 2,782 cells within
biological conditions and datasets with sufficient power to identify β-cell cluster and 377 cells within α-cell cluster) and mixed (doublet)
cell states is still missing. Therefore, we present the integrated MIA clusters (altogether 9,966 cells) (Extended Data Fig. 1a and Supplemen-
of scRNA-seq datasets across conditions (Fig. 1a). The analysis of MIA tary Table 2). They may be useful in the future in automatic annotation
provided insights that could not be obtained from individual data- transfer to identify residual low-quality populations in new datasets,
sets (Fig. 1c), including a holistic description of the β-cell landscape such as doublets that are often hard to identify.
across datasets and conditions, identification of similarities and dif-
ferences between diabetes models and disentanglement of molecular Embryonic and postnatal endocrine cell type markers
pathways involved in different types of β-cell dysfunction (Fig. 1b). To partially overlap
empower future studies we also made MIA available for both interac- Pancreatic islet profiling and stem cell differentiation highly depend
tive and computational analyses (Fig. 1d; https://github.com/theislab/ on reliable endocrine cell type markers49; however, markers of indi-
mouse_cross-condition_pancreatic_islet_atlas). vidual cell types may differ across developmental stages. For example,
in embryonic and postnatal stages different cell types are present,
Results meaning that different markers will be specific for an individual cell
An integrated atlas of mouse pancreatic islet cells across type against all other present cell types. Furthermore, our integrated
conditions embedding revealed molecularly distinct cell states within cell types
To better understand what the transcriptome of individual healthy across development (Fig. 2d and Extended Data Fig. 1). Thus, we provide
pancreatic islet cells looks like and how it changes across a lifetime and cell-type-specific markers separately for embryonic and postnatal
upon various forms of diabetogenic stress, we integrated nine mouse mice (Supplementary Table 3). We did not compute postnatal ε-cell
datasets. We comprehensively collected seven previously published and embryonic γ-cell markers due to the lack of these cell types at the
datasets (Methods describe data inclusion criteria) and generated respective stages.
two new datasets (Table 1). MIA contains 301,796 pancreatic islet cells The identified embryonic and postnatal markers only partially
from 56 samples (Fig. 2a,c, Table 1 and Supplementary Table 1). We use overlapped (Extended Data Fig. 3a), confirming that distinct marker
the term dataset for the collection of samples that were generated for sets are needed at different developmental stages. For example, while
the same purpose (for example, published together) and the term the expression of Cer1 is higher in embryonic compared to postnatal
sample for jointly processed cells with shared biology, which may δ-cells, it is a potential δ-cell marker only in postnatal and not in embry-
originate from a single animal, sequenced individually or demulti- onic samples. This is due to the high expression of Cer1 also in ε-cells
plexed, or are pooled across multiple animals sequenced on the same and high-level Ngn3-expressing endocrine precursor cells that are
lane without demultiplexing. The samples within MIA vary in sex, age present only in the embryo (Extended Data Fig. 3b).
(ranging from embryonic to postnatal, to adult, to aged), applica- Some of the markers were shared with human endocrine markers
tion of chemical stressors implicated in the loss of cellular identity reported in a recent scRNA-seq meta-analysis49 (mouse homologs
(FoxO inhibitor and artemether) and disease status (diabetes models, Ttr, Gcg, Irx2 and Slc7a2 for α-cells; Ins1, Ins2, G6pc2 and Iapp for
NOD, db/db and multiple low-dose STZ (mSTZ) together with different β-cells; Sst and Rbp4 for δ-cell; Ppy for γ-cells; Fig. 3a) and in other
anti-diabetic treatments (vertical sleeve gastrectomy (VSG), insulin, publications (Ghrl and Irs4 for ε-cells)50,51. Furthermore, we detected
glucagon-like peptide 1 (GLP-1) and estrogen) (Fig. 2a). To cover a wide several new cell-type-specific genes at different developmental
range of developmental stages we extended the available scRNA-seq stages (for example, Wnk3 and Nxph1 for α-cells; Cytip and Spock2
data (embryo to adult) with a newly generated scRNA-seq of aged for β-cells; Slc2a3, Nrsn1 and Spock3 for δ-cells; Vsig1 for γ-cells;
mice (>2 years) across sexes (17,361 cells). To identify characteristics Fig. 3a). Among these, Spock3 has been reported multiple times as
of mature cells conserved across datasets we sampled islet cells from a human α-cell, rather than δ-cell marker49,52,53; however, in mice, we
adult (4-month-old) male mice (17,353 cells), thus complementing two observed consistent upregulation in δ-cells across datasets, which is
other publicly available datasets. further supported by a previous study reporting this gene as a δ-cell
To enable joint analysis of all datasets we performed data integra- marker in zebrafish54.
tion, creating a joint embedding space. We ensured optimal trade-off We analyzed the protein expression of two transcriptome-based
between batch correction and biological preservation on the level of markers (Ttr in α-cells and Rbp4 in δ-cells) with immunohistochemistry
cell types and cell states by evaluating different integration approaches, in mouse islets (Extended Data Fig. 3c). As anticipated, the expression
including preprocessing and data selection, integration tools and of Ttr protein, which is involved in the regulation of Gcg expression
Nature Metabolism | Volume 5 | September 2023 | 1615–1637 1617

Article https://doi.org/10.1038/s42255-023-00876-x
Table 1 | Summary of datasets used for the atlas and their availability. For detailed sample information, including sex, please
refer to Supplementary Table 1
Name Description N samples GEO accession Reference Source Ensembl
release
Embryonic Embryo progression from E12.5 to E15.5 4 GSE132188 60 In-house 100
P16 Healthy young (P16) islets sorted according to 3 GSE161966 79 In-house 94
the Fltp lineage-tracing model
4m Healthy adult (4-month-old) islets from pancreas 4 GSE211796 Previously unpublished In-house 94
head and tail sorted according to the Fltp Venus
reporter to isolate FVR+ and FVR− cells
Aged Healthy aged (2-year-old) islets sorted 3 GSE211795 Previously unpublished In-house 94
according to the Fltp lineage-tracing model
mSTZ Healthy adult control, mSTZ-induced T2D 7 GSE128565 30 In-house 100
model and mSTZ model with different anti-T2D
treatments
db/db Healthy adult control, db/db-induced T2D 8 GSE174194 23 In-house 94
model and db/db model with different anti-T2D
treatments
5wNOD NOD model of T1D before T1D onset (5 weeks) 3 GSE144471 176 External 100
8–16wNOD NOD model of T1D during T1D development 9 GSE117770 27 External 100
(8–16 weeks)
Chem Healthy young adult control or with applied 15 GSE142465 (GSM4228185 to 28 External 100
chemical stress; sequencing with spike-in cells GSM4228199)
GEO, Gene Expression Omnibus.
and glucose homeostasis55, was specific to α-cells. In contrast, Rbp4 embryonic stage and that they quickly downregulate the expression
protein, which was previously reported to be a marker of δ-cells49,56, is of developmental genes, explaining the mapping of embryonic δ-cells
expressed across the whole islet and could thus not be used to reliably to the postnatal cluster. However, we must note that genes potentially
distinguish δ-cells in immunohistochemistry (Fig. 3a and Extended involved in somatostatin regulation could also be related to other cel-
Data Fig. 3c). Its relatively high protein levels in β-cells may be further lular functions at this developmental stage. Thus, further validation of
explained by the young developmental stage (P9) of the used islets δ-cell physiology during development would be required.
and hence β-cell immaturity, which is known to be associated with
high Rbp4 expression57,58. β-cells show heterogeneity across and within conditions
Extensive research has shown that β-cells are heterogeneous7,9,11; how-
Embryonic δ-cells cluster with postnatal δ-cells ever, there is a lack of knowledge on how these states relate6,8. Hence,
One of the key questions in islet biology is when and how endocrine cells we aimed to use MIA to comprehensively describe β-cell states along-
become functionally mature, which is of relevance for developing func- side their molecular characteristics in different sexes, ages and stress
tional cell types from pluripotent stem cells1. As MIA provides a shared conditions (Table 1).
embedding of different biological conditions from multiple datasets To test whether the integration is adequate for downstream anal-
that would otherwise not have been comparable due to confound- yses of β-cell states we assessed a MIA subset consisting of 102,143
ing batch effects, we leveraged it to analyze cell populations during β-cells. Cells separated on the embedding based on biological covari-
endocrine maturation. As expected, most embryonic cells (termed E ates, such as age and disease status and overlapped between sam-
group) generally did not overlap with postnatal cells (termed P group), ples with similar biological covariates from different datasets (Fig. 4a
but notably we observed that a large proportion of embryonic δ-cells and Extended Data Fig. 4). For example, healthy control β-cells
mapped to the postnatal δ-cell cluster (termed E P-like group; Fig. 3b mapped together regardless of their dataset of origin (mSTZ, db/db
and Extended Data Figs. 1d and 3d). and 8–16wNOD), whereas the cells from diabetic samples from these
To understand this overlap, we evaluated the expression of endo- datasets mapped away from the healthy clusters. This is in accord-
crine development and δ-cell function-related genes. The E P-like δ-cells ance with previously reported β-cell changes in aging and diabetic
had, in comparison to the E group, lower expression of δ-cell lineage dysfunction6,70,71. Furthermore, we assessed the expression patterns of
determinant Hhex59 and lower expression of gene markers enriched in known immaturity (Rbp4), maturity (Mafa), stress (Gast), aging/senes-
the Fev-positive population60, from which δ-cells arise60–63 (Fig. 3c and cence (Cdkn2a) and inflammatory (B2m) β-cell transcriptomic markers
Extended Data Fig. 3e). Among known δ-cell functional genes, somato- (Fig. 4b), showing complementary patterns when considering opposite
statin was highly expressed already in the E group, likely because Sst has activity of β-cell functional maturation (Mafa) and dedifferentiation
been used for δ-cell annotation, therefore not capturing earlier δ-cell (Gast) markers. Altogether, this indicates successful integration of the
developmental stages50. Other functional genes encode transcription datasets both on the cell-type and cell-state level.
factors involved in Sst gene expression64 and genes encoding sensors
required for appropriate paracrine regulation, namely neurotransmit- Transcriptomic similarity of db/db and STZ diabetes
ters, hormone receptors, including the somatostatin receptor (Sstr3 model β-cells
gene) (autocrine feedback) and genes encoding nutrient sensors, The usage of the appropriate mouse model is of utmost importance to
including sensors for milk-based high-fat weaning diet (fatty acids, studying β-cell function both in healthy and disease conditions19. Differ-
Ffar4 gene; amino acids, SLC7 family)56,65–69 (Fig. 3c). They were relatively ent models with unique phenotypes and disease mechanisms have been
highly expressed in all cell groups. This indicates that δ-cells already developed20, each of them with advantages and limitations to be con-
possess the machinery for regulating somatostatin expression at the sidered19. To better understand the transcriptomic differences among
Nature Metabolism | Volume 5 | September 2023 | 1615–1637 1618

| Article |     |     |     |     |     |     | https://doi.org/10.1038/s42255-023-00876-x |     |     |     |     |
| ------- | --- | --- | --- | --- | --- | --- | ------------------------------------------ | --- | --- | --- | --- |
a
| Dataset | Embryonic | P16 4m | Aged |     | Chem | 5wNOD | 8−16wNOD |     | mSTZ |     | db/db |
| ------- | --------- | ------ | ---- | --- | ---- | ----- | -------- | --- | ---- | --- | ----- |
E5.21 E5.31 E5.41 E5.51 m3−2 m3−2 m3−2 m3−2 m3−2 m3−2 m3−2 m3−2 m3−2 m3−2 m3−2 m3−2 m3−2 m3−2 m3−2 w81−61 w81−61 w81−61 w81−61 w81−61 w81−61 w81−61 w81−61
Age d61 d61 d61 m4 m4 m4 m4 y2 y2 y2 w5 w5 w5 w8 w8 w8 w41 w41 w41 w61 w61 w61 d281 d281 d281 d281 d281 d281 d281
Sex
ABAG ABAG ABAG 01A 01A 01A OXOF OXOF OXOF DON DON DON DON DON DON DON DON DON DON DON DON ZTSm ZTSm ZTSm ZTSm ZTSm ZTSm bd/bd bd/bd bd/bd bd/bd bd/bd bd/bd
| Stress |     |     |     |     | 1A 1A 1A |     |     |     |     |     |     |
| ------ | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- |
i+e+G
| Treatment |     |     |     |     |     |     |     |     | G   | e e+G i | FP FP GSV GSV |
| --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------------- |
New datasets Age: E 0−1m 1−1.5m 1.5−2m 2−3m 3−7m 2y     Sex: Male Female Mixed     Stress: T1D T2D Other chemical None Treatment: None Anti-diabetic
| b   |     |     |     | Atlas optimization |     |     |     | c   |     |     |     |
| --- | --- | --- | --- | ------------------ | --- | --- | --- | --- | --- | --- | --- |
Embryonic
db/db
mSTZ
tesataD P16
|     | Data collection | Preprocessing |     | Cell selection | Integration | Atlas evaluation |     |     |     |     |     |
| --- | --------------- | ------------- | --- | -------------- | ----------- | ---------------- | --- | --- | --- | --- | --- |
Aged
Public data Ambient removal* Cell types* Method* Metrics 8-16wNOD
4m
|     | New data | Remove most     |     | All cells | cVAE | Bio   |     |     |       |     |     |
| --- | -------- | --------------- | --- | --------- | ---- | ----- | --- | --- | ----- | --- | --- |
|     |          | ambient genes   |     | β-cells   | scVI | Batch |     |     | Chem  |     |     |
|     |          | SoupX           |     |           |      |       |     |     | 5wNOD |     |     |
DecontX Hyperparameters* Known markers 0 5,000 10,000 15,00020,000
* Optimized
|     | Selected | CellBender |     |     |     |     |     |     |     | N cells |     |
| --- | -------- | ---------- | --- | --- | --- | --- | --- | --- | --- | ------- | --- |
Metadata
| d   | Dataset |     |           | e   | Cell type |     |             | f         |             |         |         |
| --- | ------- | --- | --------- | --- | --------- | --- | ----------- | --------- | ----------- | ------- | ------- |
|     |         |     |           |     |           |     |             |           | E endo.     | 7,748   |         |
|     |         |     |           |     |           |     |             |           | E non-endo. | 29,177  |         |
|     |         |     |           |     |           |     |             |           | α           | 40,935  |         |
|     |         |     |           |     |           |     | E endo.     |           | β           |         | 102,143 |
|     |         |     |           |     |           |     | E non-endo. |           | δ           | 24,775  |         |
|     |         |     | Embryonic |     |           |     | α           | epyt lleC |             | γ 6,999 |         |
β
|     |     |     | P16      |     |     |     | δ             |     | Endo. prolif. | 887    |     |
| --- | --- | --- | -------- | --- | --- | --- | ------------- | --- | ------------- | ------ | --- |
|     |     |     | 4m       |     |     |     |               |     | Acinar        | 480    |     |
|     |     |     | Aged     |     |     |     | γ             |     |               |        |     |
|     |     |     |          |     |     |     | Endo. prolif. |     | Ductal        | 8,742  |     |
|     |     |     | Chem     |     |     |     | Acinar        |     |               |        |     |
|     |     |     | 5wNOD    |     |     |     | Ductal        |     | Endothelial   | 13,469 |     |
|     |     |     | 8–16wNOD |     |     |     |               |     | Immune        | 31,703 |     |
Endothelial
|     |     |     | mSTZ  |     |     |     | Immune      |     | Schwann     | 617    |     |
| --- | --- | --- | ----- | --- | --- | --- | ----------- | --- | ----------- | ------ | --- |
|     |     |     | db/db |     |     |     | Schwann     |     |             |        |     |
|     |     |     |       |     |     |     |             |     | Stellate a. | 18,332 |     |
|     |     |     |       |     |     |     | Stellate a. |     | Stellate q. | 4,970  |     |
Stellate q.
|     |     |     |     |     |     |     |     |     |     | 0 25 50 | 75 100 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------ |
N cells (thousands)
Fig. 2 | The integrated MIA captures cell types and states across lifetime,  re-annotation (excluding low-quality cells) shown on a UMAP. f, Number of
sexes and multiple stressed or diabetic conditions from different scRNA-seq  cells per cell type from atlas-level re-annotation, excluding low-quality cells.
datasets. a, Metadata of datasets and samples used in MIA. b, Overview of atlas  E, embryonic; P, postnatal; d, days; w, weeks; m, months; y, years; A1/A10,
integration evaluation. We tested multiple integration approaches and used the  artemether (1 or 10 μM); FOXO, FoxO inhibitor; G, GLP-1; e, estrogen; i, insulin; PF,
circled ones for the final atlas. c, Number of cells per sample (dots) within each  pair-fed; VSG, vertical sleeve gastrectomy; endo., endocrine; prolif., proliferative;
dataset. d, Dataset distribution within the integrated atlas (excluding low-quality  stellate a., stellate-activated; stellate q., stellate-quiescent.
cells) shown on a UMAP. Datasets are described in Table 1. e, Atlas-level cell-type
the diabetes mouse models, we compared the commonly used genetic  healthy β-cell region of MIA and STZ-treated cells mapped onto the
models of T1D (NOD, for which we used samples from early disease  region with mSTZ and db/db model samples (Fig. 4c). Similarly, in the
stages20,27) and T2D (db/db24) together with the β-cell ablation model  future mapping onto MIA may reveal relationships between other
(STZ) that was previously used to study both T1D and T2D29,30. The NOD  dysfunctional conditions.
model is characterized by autoimmune and cytokine-mediated destruc- To better understand molecular mechanisms underlying β-cell
tion of β-cells as well as ER stress72,73. The leptin-receptor-deficient   dysfunction within each of the models, we analyzed the expression
db/db mice are obese, hyperglycemic and dyslipidemic74,75, leading to  of known β-cell function and stress genes (Fig. 4d). In the mSTZ and
β-cell failure and compensation, which are associated with metabolic  db/db models multiple maturity and insulin-related genes were down-
stress, including ER stress23,24. The STZ treatment is used for specific
regulated, while in the NOD model immune modulation genes were
destruction of β-cells due to its affinity for the Slc2a2 (ref. 76) protein  upregulated. In all three models we observed expression changes in
expressed in β-cells. The stressor is applied either in a single high dose  several unfolded protein response, reactive oxygen species defense and
to resemble T1D or in multiple low doses to elicit partial β-cell loss  senescence-related genes. This indicates the involvement of metabolic
reminiscent of T2D, but in the absence of insulin resistance19, with both  stress in db/db and mSTZ models and immune stress in the NOD model,
strategies analyzed below. in accordance with current views on T1D and T2D pathomechanisms77.
Based on MIA embedding, we found that β-cells from mSTZ-  To elucidate which mouse models capture transcriptional signa-
induced (multiple low doses) and db/db models mapped together,  tures of human T1D or T2D, we assessed whether changes observed in
separately from NOD diabetic β-cells (Fig. 4a). To further validate  human diabetes are also present in mice. We performed differential
the similarity between the mSTZ and db/db models, we mapped onto   gene expression (DGE) analysis on β-cells from multiple human T1D
MIA another mouse dataset (referred to as the Feng dataset31, not  and T2D datasets (Table 2), selected genes upregulated across multiple
part of MIA), containing samples treated with STZ (single high dose).  datasets per diabetes type (T1D 32 genes, T2D 59 genes) and identified
Again, the healthy control cells from the Feng study mapped onto the  enriched gene sets (Supplementary Table 4). We further complemented
Nature Metabolism | Volume 5 | September 2023 | 1615–1637 1619

Article https://doi.org/10.1038/s42255-023-00876-x
α E
our gene set list with known human diabetes-associated gene sets from the basis of the metadata (altogether referred to as ‘coarse states’;
the literature. Human T1D is marked by the upregulation of immune Fig. 5a and Extended Data Fig. 5a). We resolved populations of healthy
gene sets21, which were much more strongly upregulated in NOD than adult, immature, aged (separated by sex), NOD diabetes model, mixed
db/db and mSTZ models (Fig. 4e; details of gene set activity analysis db/db and mSTZ diabetes models and cells from the dataset with chemi-
across mouse models are provided in Supplementary Note 2). Con- cal perturbations in cultured islets (referred to as chem) that likely
versely, human T2D is associated with changes in hormone metabolism separate due to strong differences in sample handling. For a detailed
and stress related to metabolic compensation21,22,78, which were upregu- description of states see Supplementary Note 4.
lated in db/db and mSTZ but not in the NOD model. Thus, the mSTZ We support the annotation of coarse states with known β-cell
model reflects key molecular changes of human T2D, but not T1D. The state markers depicted in Fig. 5b. Some known markers were not
presence of metabolic stress in the mSTZ model β-cells after clearance state-specific, such as certain immature marker genes that were
of the chemical stressor can be explained by the surviving population also highly expressed in the db/db + mSTZ state (for example, Cd81;
of β-cells being too small to prevent hyperglycemia and hence leading Fig. 5b), in accordance with β-cell dedifferentiation in mouse diabetes
to compensatory insulin-production behavior and subsequent stress. models23,30,79. Thus, the identification of new state-specific markers
could improve the monitoring of β-cells in specific states to study
Markers of β-cell states conserved across datasets their function. We identified markers specific for an individual β-cell
As it is unclear how newly reported β-cell states correspond across state and conserved across all datasets mapping to that state, with
publications6,7, we next aimed to utilize the cross-dataset integrated top markers highlighted in Fig. 5c (Supplementary Table 5; a more
conditions within MIA to describe β-cell heterogeneity in health detailed description is in Supplementary Note 4). For example, we
and disease in a unified manner. We annotated states on postnatal identified a new marker of healthy adult state Prss53, associated with
non-proliferative β-cells (‘β’ cluster in Fig. 2e) and labeled them on mitochondrial function80.
Nature Metabolism | Volume 5 | September 2023 | 1615–1637 1620
α
)namuh(
β
)namuh(
δ
)namuh(
γ
)namuh(
ε
)namuh(
α )wen( β )wen( δ )wen( γ
)wen(
a
α P
β E
β P
δ E
δ P
ε E
γ P
b α β δ
E
E P-like
c Hormone Nutrient Fraction of cells
Fev + δ Sst TFs receptors sensors
δ E 20 40 60 80100
δ E P-like Relative
δ P mean expression
0 0.5 1.0 4xaP veF kcC xehH tsS 1xdP 1xonkP 1xbP 3rtsS rgcG rsnI 2rhrC r1plG 4rafF 1a2clS 3a2clS 1a7clS 2a7clS 5a7clS
Marker
Embryonic
Postnatal
Both
Age
12.5 E
13.5 E
0 0.025 0.050 0 0.025 0.050 0 0.0025 0.0050 14.5 E
Ratio of sample Ratio of sample Ratio of sample 15.5 E
epytbuS
2xrI rtT gcG 2a7clS 1snI 2snI 2cp6G ppaI 4pbR tsS ypP lrhG 4srI 3knW 1hpxN pityC 2kcopS 3a2clS 1nsrN 3kcopS 1gisV
Fig. 3 | The integrated atlas embedding shows differences between within a sample. Cell groups are E, embryonic cells mapping to the embryonic
embryonic and postnatal endocrine cells. a, Expression of endocrine markers cluster; and E P-like, embryonic cells mapping to the postnatal cluster.
shown across postnatal (P) and embryonic (E) endocrine cell types, including c, Expression of known maturity and δ-cell function markers across embryonic
known markers shared with human (labeled human) and newly identified δ-cells groups. Groups are as in b: P, postnatal cells mapping to the postnatal
markers (labeled new). b, Number of cells in each embryonic endocrine cell cluster. In a and c, relative expression is computed as the average of cell groups
group within individual embryonic samples, expressed as a fraction of cells normalized to [0,1] for each gene feature.

| Article |         |     |     |     |                   |     |     |     |     | https://doi.org/10.1038/s42255-023-00876-x |                |     |     |     |
| ------- | ------- | --- | --- | --- | ----------------- | --- | --- | --- | --- | ------------------------------------------ | -------------- | --- | --- | --- |
| a       | Dataset |     |     |     | Healthy age group |     |     |     |     |                                            | Diabetes model |     |     |     |
Embryonic
P16
4m
|     |     |     | Aged |     |     |     |     | Pup        |     |     |     |     | Healthy control |     |
| --- | --- | --- | ---- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --------------- | --- |
|     |     |     |      |     |     |     |     | Adolescent |     |     |     |     | NOD             |     |
Chem
|     |     |     | 5wNOD    |     |     |     |     | Young adult               |     |     |     |     | mSTZ                    |     |
| --- | --- | --- | -------- | --- | --- | --- | --- | ------------------------- | --- | --- | --- | --- | ----------------------- | --- |
|     |     |     | 8–16wNOD |     |     |     |     | Adult                     |     |     |     |     | db/db                   |     |
|     |     |     | mSTZ     |     |     |     |     | Aged                      |     |     |     |     | Excluded (dataset       |     |
|     |     |     | db/db    |     |     |     |     | Excluded (stressed cells) |     |     |     |     | without diabetes model) |     |
b
|     | Ins1 |     | Mafa |     | Rbp4 |     |     | Cdkn2a |     |     | Gast |     | B2m |     |
| --- | ---- | --- | ---- | --- | ---- | --- | --- | ------ | --- | --- | ---- | --- | --- | --- |
6
|     |     |      |     | 4   |     |     |     |     |     |     |     |     |     | 6   |
| --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     | 10.0 |     |     |     |     |     |     |     | 1.5 |     |     |     |     |
3
|     |     | 7.5 |     |     |     |     | 4   |     |     |     |     | 4   |     | 4   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1.0
2
5.0
|     |     |     |     |                       |     |     | 2      |           |           |            |     | 2         |            |                   |
| --- | --- | --- | --- | --------------------- | --- | --- | ------ | --------- | --------- | ---------- | --- | --------- | ---------- | ----------------- |
|     |     |     |     |                       |     |     |        |           |           | 0.5        |     |           |            | 2                 |
|     |     | 2.5 |     | 1                     |     |     |        |           |           |            |     |           |            |                   |
|     |     | 0   |     | 0                     |     |     | 0      |           |           | 0          |     | 0         |            | 0                 |
| c   |     |     |     | d                     |     |     |        |           |           | gnissecorp |     | tnecseneS | noitaludom |                   |
|     |     |     |     |                       |     |     |        | noiterces | sisehtnys |            |     |           |            |                   |
|     |     |     |     |                       |     |     | erutaM |           |           |            |     | esnefed   | enummI     |                   |
|     |     |     |     |                       |     |     |        | nilusnI   | nilusnI   |            |     |           |            |                   |
|     |     |     |     |                       |     |     |        |           | dna       | RPU        | SOR |           |            |                   |
|     |     |     |     | Healthy control (NOD) |     |     |        |           |           |            |     |           |            | Fraction of cells |
NOD
Healthy control (mSTZ)
|     |     |     |             |                         |     | mSTZ  |     |     |     |     |     |     |     | 20406080 100    |
| --- | --- | --- | ----------- | ----------------------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --------------- |
|     |     |     | Query group | Healthy control (db/db) |     |       |     |     |     |     |     |     |     | Relative        |
|     |     |     |             |                         |     | db/db |     |     |     |     |     |     |     | mean expression |
Healthy control
|     |     |     | STZ |     |     |     |                |                                       |                   |                  |                     |                              |                                      | 0 0.5 1.0 |
| --- | --- | --- | --- | --- | --- | --- | -------------- | ------------------------------------- | ----------------- | ---------------- | ------------------- | ---------------------------- | ------------------------------------ | --------- |
|     |     |     |     |     |     |     | 1snI afaM 6xaP | 3ncU 2a2clS 2cp6G 8a03clS 52panS 4tyS | b1orE 1rafF 1kscP | n1kscP 3ftA 4ftA | 5apsH 1pbX 1tM 1doS | 1xpG 2xpG 2lcB a1nkdC 3pbfgI | 6lI 1enipreS 01lcxC 1K-2H 1paT 1tatS |           |
Excluded
(reference)
| e   | T1D | T1D | T2D | T1D and T2D |     | T2D |     | T2D | T2D |     | T2D | T2D | T2D | Human  |
| --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |
upregulated
MHC class I Antimicrobial Regulation of Transport Endocrine Hormone Oxidative Ribosome Regulation of Proteasomal
protein complex humoral response response to vesicle membrane pancreas metabolic process phosphorylation biogenesis cellular response protein catabolic
|     |     |     | extracellular stimulus |     |     | development |     |     |     |     |     | to hypoxia | process |     |
| --- | --- | --- | ---------------------- | --- | --- | ----------- | --- | --- | --- | --- | --- | ---------- | ------- | --- |
NOD
Status
| ledoM |     |     |     |     |     |     |     |     |     |     |     |     |     | Diabetic |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- |
db/db
Healthy
mSTZ
00.5 1.0 1.5 00.10.20.3 –0.2 00.20.4 00.10.20.30.4 0 0.2 0.4 0 0.1 0.2 00.5 1.0 1.5 0 0.20.40.6 –0.250 0.25 0.50 0.75 0 0.10.20.3
|     | Score | Score | Score | Score |     | Score |     | Score | Score |     | Score | Score | Score |     |
| --- | ----- | ----- | ----- | ----- | --- | ----- | --- | ----- | ----- | --- | ----- | ----- | ----- | --- |
Fig. 4 | The integrated atlas embedding reveals similarities between mSTZ  is from the 8–16wNOD dataset, other model names correspond to the dataset
and db/db diabetes models. a, Distribution of technical (dataset) and biological  names). Relative expression is computed as the average of cell groups normalized
(age, disease status) covariates on a UMAP of the β-cell MIA subset. The age  to [0,1] for each gene feature. e, Activity of gene sets upregulated in T1D or
subplot shows only cells from healthy, non-stressed samples. The disease subplot  T2D human samples shown for mouse diabetes models and corresponding
shows only cells from samples belonging to datasets that contain both healthy  healthy controls from individual datasets (as in d). On the overlay boxplots
and diabetes model data. b, Expression of selected β-cell heterogeneity markers  the white dot represents the median, the box the quartiles and the whiskers
on a UMAP of the β-cell MIA subset. c, Joint UMAP embedding of the reference  the minimum and maximum (no cells qualified as outliers). The data sizes are
atlas (background) and the external (Feng) mouse dataset (query, foreground)  (reported as ‘N samples (N cells)’), NOD_elimination diabetic 6 (3,191) and healthy
indicating positioning of healthy control and STZ-treated query cells.   3 (548); STZ diabetic 1 (1,496) and healthy 1 (5,795); VSG diabetic 2 (5,264) and
d, Expression of known β-cell function genes across different diabetes models  healthy 2 (7,706). Each sample contains islets from multiple mice. MHC, major
and corresponding healthy controls from individual datasets (the NOD model  histocompatibility complex.
To test the robustness of our markers we analyzed their expression  (postnatal days 12 (P12) and 21 (P21)) mapped between the immature,
on the Feng mouse dataset that is not part of the atlas31. This data-
adult and chem MIA states.
set consists of healthy young and adult mice, with multiple samples  Additionally, we assessed whether previously known and
spanning the ages of 0.1–4 months, as well as STZ-treated diabetic  MIA-based markers could be directly translated to ten human datasets
samples (Extended Data Fig. 6c,d). The proposed T2D model state  with differences in donor metadata (Extended Data Fig. 6e,f). Only
(db/db + mSTZ) and adult state markers were expressed as expected  B2m (T1D marker)27 and Rbp4 (immature marker)79 were significantly
in the Feng dataset; however, we did not observe specific expression of  upregulated in all human samples associated with those phenotypes.
immature markers in the young samples. We next evaluated whether  This is in accordance with previous reports81 showing that not all mouse
this difference arises due to a different immature cell state present  markers directly translate to human data.
in the Feng dataset or due to technical issues in marker identifica-
tion. Thus, we mapped Feng dataset cells to MIA. Indeed, we observed  β-cell heterogeneity within biological conditions
differences in the two immature cell states, as young samples from  β-cells are known to be heterogeneous within individuals11,12,82; how-
the Feng dataset did not map to MIA immature state (Extended Data   ever, our metadata-driven coarse states mainly did not reveal multiple
Fig. 7a,b). The Feng postnatal day 3 (P3) β-cells mapped between  populations per sample (Extended Data Fig. 5c). Some marker genes
embryonic and postnatal β-cells of MIA and the young postnatal cells  were heterogeneously expressed within coarse states, such as Rbp4 in
Nature Metabolism | Volume 5 | September 2023 | 1615–1637 1621

Article https://doi.org/10.1038/s42255-023-00876-x
Table 2 | Datasets used for validation, not part of the atlas. For detailed sample information, including sex, please refer to
Supplementary Table 12
Species Description N samples Technology N cells (N β-cells) GEO accession Reference
Mouse Healthy adult and aged islets 2 SMARTer 207 (207) GSE83146 177
Mouse Endocrine cells from healthy young and adult 17 STRT-seq 2,999 (1,005) GSE137909 31
mice and adult mice treated with STZ or STZ and
insulin, with samples collected at different times
after STZ treatment
Human Islets from non-diabetic, T1D and non-diabetic 24 Chromium v2/v3 66,052 (11,298) GSE148073 26
islet autoantibody positive donors, including
child donors
Human Islets from non-diabetic and T2D adult donors 18 SMARTer Ultra 1,600 (503) GSE81608 52
Low RNA
Human Islets from non-diabetic adult and aged donors 5 Chromium v2 26,474 (11,923) GSE198623 81
Human Islets from non-diabetic child and adult donors 8 Smart-seq2 2,282 (348) GSE81547 15
Human Islets from adult non-diabetic and T2D donors 8 SMARTer 617 (264) GSE86469 178
Human FACS-sorted islet cells from adult and aged 14 Smart-seq2 2,245 (674) GSE124742 (FACS) 21
donors with or without T2D
Human Patch-seq of islet cells from adult and aged 53 Smart-seq2 2,319 (496) GSE124742, GSE164875 21,97
donors without diabetes, with T1D (adult only) or (patch-seq)
with T2D
Human Islets from non-diabetic and T2D adult donors 9 Drop-seq 27,996 (9,958) GSE101207 78
Human Islets from non-diabetic child and non-diabetic 22 Smart-seq 619 (182) GSE154126 179
and T2D adult donors
Human Islets from non-diabetic child and non-diabetic, 9 Smart-seq 457 (111) GSE83139 22
T1D and T2D adult donors
young and db/db + mSTZ states and Mafa and Gast in the db/db + mSTZ state) also contained db/db model cells. This may be explained by
state (Fig. 4b), indicating that we could identify higher resolution either mSTZ diabetes model having a milder hyperglycemia than the
states in MIA. db/db model23,30, leading to a lower β-cell compensatory response
Annotation of cell states is challenging due to uncertainty about and thus reduced stress, or by a different mechanism of β-cell dam-
the number of distinct states83. To ensure that states can always be age due to the use of STZ. As these two populations clearly differ in
biologically interpreted, we based clustering on interpretable fea- their metabolism, they may be of relevance for studying diabetes
tures (termed gene programs (GPs); Fig. 5d and Methods). GPs are with the mSTZ model.
data-driven groups of genes coexpressed across β-cells (27 GPs, 14–228 Publications based on individual datasets often do not agree on
genes; Extended Data Fig. 8a and Supplementary Table 6). Most of the β-cell heterogeneity markers35. Thus, we used the wide range of β-cell
GPs were enriched for distinct molecular functions (Supplementary phenotypes across datasets within MIA, encompassed by the fine β-cell
Table 6) and we show that they generalize to other datasets by explain- states, to assess population markers manually extracted from the lit-
ing variance in two external mouse and ten human datasets (Extended erature (Fig. 5f and Supplementary Table 7). Some markers previously
Data Fig. 8f). reported as marking the same β-cell population, such as markers of
We defined 19 fine β-cell states (Fig. 5e), which mainly corre- maturity or dedifferentiation (often related to T2D models), separated
sponded to subclusters of the coarse states (Extended Data Fig. 5e) and into multiple groups with distinct expression patterns across fine
described more subpopulations within samples, while still containing states (Fig. 5f). This shows how MIA could be used to find specific and
cells from multiple samples and datasets (Extended Data Fig. 5d and sensitive markers. Furthermore, we observed that different groups
Supplementary Table 2). Additionally, two clusters were characterized of markers reported across studies with different biological focuses
by low-quality control metrics and were thus not regarded as true cell share similar expression profiles, such as mature10,23,84,85, extreme
states (Fig. 5e and Extended Data Fig. 5b). We further discuss β-cell insulin-producing23,85 and immune-attack-susceptible markers86. The
heterogeneity captured within MIA in relation to previous literature immune-attack-susceptible markers were extracted by Rui et al.86 who
in Supplementary Note 5. reported NOD subpopulations differing in immune-attack susceptibil-
We observed two populations of β-cells in the mSTZ model ity. They reported that the immune-attack-susceptible population
(states mSTZ and db/db + mSTZ; Fig. 5e and Extended Data Fig. 5d). expressed β-cell maturity genes and indeed we observed that the popu-
We used biologically interpretable GP differences to ease the com- lation markers reported by Rui et al. colocalized with known maturity
parison of these two states (Extended Data Fig. 8b,d; for validation genes in MIA (Fig. 5f). This demonstrates how the heterogeneous cell
of this approach see Supplementary Note 6). The db/db + mSTZ state states within MIA can be used for gene contextualization by providing
had higher activity of multiple GPs that contained known diabetes information on which β-cell states express a gene of interest and which
markers or were associated with ER stress (GP2, GP3 and GP4) and known markers have similar expression patterns.
cell state mSTZ had higher activity of GPs associated with imma-
turity (GP8 and GP23). Both increased ER stress and immaturity β-cell dysfunction patterns within healthy samples
were reported in the paper publishing the mSTZ dataset30; however, In our GP analysis we observed that GPs that changed between healthy
they did not describe dysfunctional populations differing in the and T2D model cells (GPs 3, 4, 19 and 20; Extended Data Fig. 8a,b) were
two processes. While the more immature state (mSTZ state) was also among GPs explaining the largest proportion of cell-to-cell vari-
specific to the mSTZ model, the more stressed state (db/db + mSTZ ability within healthy datasets and samples in both mouse and human
Nature Metabolism | Volume 5 | September 2023 | 1615–1637 1622

| Article |     |     |     |     |     |     |     |     |     | https://doi.org/10.1038/s42255-023-00876-x |     |     |     |     |
| ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------ | --- | --- | --- | --- |
| a       |     |     | b   |     |     |     |     |     | c   |                                            |     |     |     |     |
β Imm. MatureAgedT1D T2D Imm.Adult AgedF AgedM NOD-D db/db + mSTZChem
Coarse subtypes
Imm.
Adult
AgedF
AgedM
NOD-D
Imm. db/db + mSTZ
Adult
AgedF Chem
AgedM LowQ
NOD-D LowQ-hMT
db/db + mSTZ
Chem
1snI 2snI 1-6xkN 1xdP 4pbR 18dC bfaM afaM 3ncU 2a2clS a2nkdC 1pb35prT m2B tsaG cG 3a1hdlA kcC bodlA bghC stnuoc N seneg N .carf TM F a3roT ackrP 1a73clS 35ssrP beN 81wxbF 1tlag3B 1hpT 1omF 1paglD 1daG 2srI 2tmB kiR30J1200399 kiR80B610038F 1484mG ptgI kndI 1apP 2scroS 01a5clS tsaG 7anipreS 3nlgaT 2nkP ziK
|     |     |     | Fraction of |                       | Relative  | Relative mean  | Female |     |     |     |     |     |     |     |
| --- | --- | --- | ----------- | --------------------- | --------- | -------------- | ------ | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |             | cells mean expression |           | quality metric | ratio  |     |     |     |     |     |     |     |
|     |     |     | 20406080    | 100 0                 | 0.5 1.0 0 | 0.5 1.0        | 0 0.5  | 1.0 |     |     |     |     |     |     |
d f 2−2xkN 1−6xkN a2nkdC b11fsrfnT 1enipreS 3gorueN a1nkdC b2nkdC 01lcxC
|     |     |     |     |     |     |     |     |     |     | 1xdP | aghC 3ncU 4ltyS | 2a2clS afaM 3ftA bghC | 8ccbA ppaI 3xpG 18dC | 1lcxC 4lcC 4pbR bfaM r1plG |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --------------- | --------------------- | -------------------- | -------------------------- |
|     |     |     |     |     |     |     |     |     |     |      | 1snI 2snI       |                       |                      | cG kcC ypN taC             |
Functional β-cell subtypes
|     |     |     |     | Variability within |                              | Cell clusters with unique  |     |     |     | T1D  |     |     |     |     |
| --- | --- | --- | --- | ------------------ | ---------------------------- | -------------------------- | --- | --- | --- | ---- | --- | --- | --- | --- |
|     |     |     |     | the whole atlas    | combination of gene programs |                            |     |     |     | Aged |     |     |     |     |
Dedifferentiated
Gene programs variable across the atlas Gene programs Gene programs Extreme
Immature
Select variable genes Cluster variable genes slleC Immune-attack resistant
| with Moran’s I |          |       | Applications |         |     |     |     | Immune-attack susceptible |                     |           |     |     |     |     |
| -------------- | -------- | ----- | ------------ | ------- | --- | --- | --- | ------------------------- | ------------------- | --------- | --- | --- | --- | --- |
|                | Programs | Genes |              |         |     |     |     |                           | Immune-infiltration |           |     |     |     |     |
|                |          |       |              | Samples |     |     |     | Marker                    |                     | Mature    |     |     |     |     |
|                | slleC    |       |              |         |     |     |     | False                     | Proliferative       |           |     |     |     |     |
|                |          |       |              |         |     |     |     | True                      |                     | Senescent |     |     |     |     |
Variability conserved across samples
|     |               |     |     |     |     |               |                 | Relative   | db/db-VSG    |       |     |     |     |     |
| --- | ------------- | --- | --- | --- | --- | ------------- | --------------- | ---------- | ------------ | ----- | --- | --- | --- | --- |
|     |               |     |     |     |     | Gene programs |                 | mean       | db/db + mSTZ |       |     |     |     |     |
|     |               |     |     |     |     |               |                 | expression |              | mSTZ  |     |     |     |     |
|     |               |     |     |     |     |               | Conserved       | 1.0        |              |       |     |     |     |     |
| e   | Fine subtypes |     |     |     |     |               | Sample specific |            |              | Imm.3 |     |     |     |     |
Chem1
|     |     |     |       |     |        |     |     | 0.5 | NOD-imm. |       |     |     |     |     |
| --- | --- | --- | ----- | --- | ------ | --- | --- | --- | -------- | ----- | --- | --- | --- | --- |
|     |     |     | Imm.1 |     | AgedF2 |     |     | 0   |          | NOD-D |     |     |     |     |
sretsulc lleC D-inter.
|     |     |     | Imm.2 |     | D-inter. |     |     |     |             | Adult2 |     |     |     |     |
| --- | --- | --- | ----- | --- | -------- | --- | --- | --- | ----------- | ------ | --- | --- | --- | --- |
|     |     |     | Imm.3 |     | NOD-D    |     |     |     | Adult-imm.2 |        |     |     |     |     |
Chem3
|     |     |     | NOD-imm. |     | db/db + mSTZ |     |     |     |     | Chem2 |     |     |     |     |
| --- | --- | --- | -------- | --- | ------------ | --- | --- | --- | --- | ----- | --- | --- | --- | --- |
Annotation
|     |     |     | Adult-imm.1 |     | mSTZ      |     |     | Multi-marker  |     | Imm.1 |     |     |     |     |
| --- | --- | --- | ----------- | --- | --------- | --- | --- | ------------- | --- | ----- | --- | --- | --- | --- |
|     |     |     | Adult-imm.2 |     | db/db–VSG |     |     | similarity    |     | Imm.2 |     |     |     |     |
Adult-imm.1
|     |     |     | Adult1        |     | Chem1 |     |     | Heterogeneity of   |               |        |     |     |     |     |
| --- | --- | --- | ------------- | --- | ----- | --- | --- | ------------------ | ------------- | ------ | --- | --- | --- | --- |
|     |     |     |               |     |       |     |     | mature markers     |               | Adult1 |     |     |     |     |
|     |     |     | Adult2        |     | Chem2 |     |     |                    | Adult + agedM |        |     |     |     |     |
|     |     |     |               |     |       |     |     | Heterogeneity of   |               | AgedF1 |     |     |     |     |
|     |     |     | Adult + agedM |     | Chem3 |     |     | dedifferentiation  |               |        |     |     |     |     |
|     |     |     | AgedF1        |     |       |     |     | markers            | AgedF2        |        |     |     |     |     |
g
|             |     |     |     |     |     |     | Dedifferentiation |     |     |     |     |     |              | (Anti)apoptotic |
| ----------- | --- | --- | --- | --- | --- | --- | ----------------- | --- | --- | --- | --- | --- | ------------ | --------------- |
| Correlation |     |     |     |     |     |     |                   |     |     |     |     |     | n e e ration |                 |
Mature u l i n ted Immature S efense m o tors Imm u n Protective
|                    |        |      | Ins a |     |       |     |     |      | UPR |      | RO  |     | Ho r c e p il t |     |
| ------------------ | ------ | ---- | ----- | --- | ----- | --- | --- | ---- | --- | ---- | --- | --- | --------------- | --- |
| spuorg eneG –1 0 1 |        |      | r e l |     |       |     |     |      |     |      | d   |     | r e inf         |     |
| InsL (1) XXX       |        |      |       |     |       |     |     |      |     | XXX  |     |     | XX              | XXX |
| Imm. (2)           |        |      |       | X   | X X X | X X |     |      |     |      |     | X   |                 |     |
| InsH-str. (3)      |        | XXXX | X X   | XXX |       |     | X   | XXXX |     |      |     | X   | X               |     |
| Aged (4)           |        |      |       |     |       |     |     | X    | XX  | XX X |     |     | XX              |     |
| InsH (5)           | XX XXX | X    |       | XX  |       |     | X   | X    |     | X    |     |     |                 |     |
a1r1ppP 3ncU 42cjanD 2biC 2sspaP afaM 5mprT l2mtsV l1gidnyS 35ssrP 21gnG 8ccbA 7tyS b1ncS 1rafF 8a03clS 4ltyS 2cp6G 1kscP epC bghC 2kscP 1rsS bh4P 2snI a3baR 1snI b1orE 4tyS 1xdD 24cdC 5gcS ppaI n1kscP aghC a3ncS ypN 3ndlC 1plpA 7pbfgI 4pbR 4ndlC maclA lnlsM 4pqA bfaM lpixlM 4mneT 18dC 1l4pcP 32ssrP 3nlgaT 3gorueN nrtlC 3gcS maP 1crhtC 4afudN pyS 2dpG 3tM 5bfudN bnuJ rlaC 5apsH 1b09psH 3lreD pcV 9sO 1pbX 1dupreH a51r1ppP 4ftA 3tidD 3ftA 1hpsH nuJ 1ltF 2tM 1tM 1htF 1sp-1ltF 1oqN 2a3clS 1pbcP 2xdrP 1lnxT 6xdrP 1nxT 1xdrP 3xpG r2fgI rsnI 3rtsS r1fgI rgcG nrptP 1daG m2B pinxT 3piafnT leR 1lcM paiX 9psaC 1l2lcB 8psaC 2l2lcB daB 2lcB 1rpuN 2a2ptA 5ftA 1tkA 2l2efN
X, gene contained in gene group
Fig. 5 | MIA encompasses β-cells heterogeneity across and within biological  f, Expression of known β-cell heterogeneity markers across fine β-cell states.
conditions. a, Coarse β-cell states labeled based on sample metadata (excluding  Phenotypes associated with individual genes (top). The dotted boxes represent
low-quality clusters) shown as a UMAP. b, Expression of known markers (marker  two distinct sets of maturity (orange) and dedifferentiation or diabetes markers
groups are specified on the top of the plot), quality control metrics and sex ratios  (red); the solid cyan box shows overlap and expression similarity between
across coarse β-cell states displayed in separate dot-plot panels. In the marker  maturity, immune-attack susceptibility and extreme insulin producer markers.
expression panel, the dot size indicates the fraction of cells expressing a gene,  g, Correlation between gene groups variable in all healthy samples and known
whereas in other panels it is set to a fixed size. c, Expression of MIA-based markers  β-cell heterogeneity markers on the healthy β-cell subset. Markers present
of coarse β-cell states. d, Overview of the method used for extraction of GPs and  within a specific gene group are annotated with an X. imm., immature; M, male, F,
subsequent cell clustering resolution selection or definition of consistently  female; NOD-D, NOD diabetic; D.-inter, diabetic intermediate; insL/H, insulin low/
variable GPs across samples. e, Fine β-cell states defined based on the presence of  high; str., stressed. In b, c and f, relative expression is computed as the average of
a unique combination of GPs (excluding low-quality clusters) shown as a UMAP.  cell groups normalized to [0,1] for each gene feature.
(Extended Data Fig. 8g and Supplementary Table 6). This motivated  genes implicated in β-cell metabolic stress recovery, such as ATP
us to describe heterogeneity conserved across healthy adult samples. production-related genes82 (Fig. 5g and Supplementary Table 8).
We collected genes that are consistently variable within individual  The negative correlation between the expression of group 1 and
healthy samples and grouped them based on coexpression patterns  groups 3 and 5 (Extended Data Fig. 9) is in accordance with previously
conserved across samples, resulting in five gene groups (a detailed  reported cycling of β-cells between insulin production and recov-
description of groups is in Supplementary Note 7 and Supplementary  ery in mice and humans82,87,88. As group 1 genes, including multiple
Table 8). Groups 3 and 5 were associated with β-cell maturity and insulin  mitochondria-associated genes, β-cell maturation and function genes
production, with group 3 having a stronger insulin-production-related  (Ucn3, Ftl1, Cd63 and Scg2)47,89 and protective genes (Nupr1, Atp2a2
and Atf5)90–92, are involved in healthy metabolic stress recovery they
stress signature (Fig. 5g and Supplementary Table 8). Group 1 contained
Nature Metabolism | Volume 5 | September 2023 | 1615–1637 1623

Article https://doi.org/10.1038/s42255-023-00876-x
may be of interest for T2D therapy. Indeed, group 1 showed the lowest First, we used the DEG groups to disentangle dysfunction patterns
activity in the diabetes model β-cells (Extended Data Fig. 9b), indicating of interest from confounding effects. In the original NOD dataset paper
impaired stress recovery. by Thompson et al.27 the authors observed confounding of dysfunc-
We also observed two gene groups indicating that cells within tion progression and age differences between samples containing
healthy adults differ in the degree of maturity and senescence. Group 4 healthy (8 weeks) and dysfunctional cells (14 and 16 weeks), impairing
contained senescence genes and healthy adult cells most highly the interpretation of diabetes-associated changes. Indeed, we also
expressing these genes colocalized with aged cells. Notably, while observed, among NOD downregulated genes, one group (T1-down1),
group 2 contained immaturity genes, the healthy adult cells with high which was highly expressed across multiple immature states (Fig. 6a)
expression of this group partially colocalized with the immature subset and contained genes associated with immaturity (Pyy and Npy)99,100 thus
of mSTZ model cells (fine β-cell states imm.3 and mSTZ) (Supplemen- likely representing a confounding effect of age. Other gene groups did
tary Note 7, Fig. 5g, Extended Data Fig. 9 and Supplementary Table 8). not seem to be associated with known batch effects.
Comparison to a meta-analysis of human healthy heterogeneity With our DEG clustering approach, we disentangled two
markers35, revealed shared genes Tm4sf4 and Clu from group 3 (insulin NOD-upregulated immune processes (groups T1-up2 and T1-up3) that
production and metabolic stress) and genes Fos, Herpud1 and Rgs4 from showed differences in expression across β-cell states. Group T1-up3
group 4 (aging). While these orthologs likely share function across spe- was NOD diabetic cells (state 14–16wNOD) specific and more strongly
cies, Mawla and Huising35 did not specifically state which β-cell states enriched for antigen-processing genes (containing genes B2m, Tap2 and
they are associated with. major histocompatibility complex (MHC) II group members), whereas
T1-up2 was, in addition to NOD diabetic cells, also highly expressed in
Diabetes response of β-cells is highly complex immature cells (Fig. 6a) and more strongly enriched for innate immune
While β-cells are the primary cell type affected in diabetes, the disease response genes (containing genes Stat1, Stat2, Gbp7 and immunopro-
also has broader effects on the whole islet93,94. To investigate these teasome group members), potentially representing the regulation
effects, we performed DGE analysis between healthy and T1D model of β-cells by the immune system that is not restricted to diabetes101.
or T2D model samples in α-, β−, γ- and δ-cells. All cell types had a large Upregulation of both T1-up3 and T1-up2 in NOD is in accordance with
number of differentially expressed genes (DEGs) in both diabetes types the active involvement of β-cells in T1D-related immune response by
(Supplementary Fig. 2 and Supplementary Table 9). DEGs in the β-cell means of antigen presentation and immune infiltration in the islets27,102,
T1D model and T2D model had a relatively low overlap and were also respectively. Furthermore, in the NOD diabetes model, we also observed
distinct from DEGs in other cell types (Fig. 6b). This is in accordance upregulation of senescence-related genes (group T1-up4) that were
with different mechanisms that lead to the loss or dysfunction of β-cells shared with aged females (Fig. 6a). Indeed, senescence genes have
in T1D and T2D77. In contrast, DEGs overlapped more strongly between been previously reported in association with NOD model dysfunction
T1D model and T2D model within α-, γ- and δ-cells and also showed a and aging individually27,103 and we here show their relationship.
relatively high overlap across these cell types. This is likely due to β-cells As expected, in db/db + mSTZ cellular metabolism that is nec-
being the primary cell type affected in diabetes, further leading to islet essary for normal β-cell function77 was disrupted. A group of genes
disruption and causing residual stress in other endocrine cells95,96. (T2-down3) was downregulated across all T2D model cell states and was
To characterize the residual stress within endocrine cell types higher across healthy cell states (Fig. 6a), with enrichment for insulin
other than β-cells we examined shared DEGs in both diabetes types. secretion and steroid metabolism. Additionally, we observed DEG
Upregulated genes were enriched for ER stress, whereas downregulated groups supporting mSTZ subpopulations associated with immaturity
genes were enriched for gene sets related to membrane depolarization or metabolic stress, which we observed above based on GP differences
and ion transport (Supplementary Table 9) and contained hormone (Supplementary Note 9).
genes (Gcg in α-cells, Ppy in γ-cells and Sst in δ-cells) (Supplementary Multiple parallels can be drawn between NOD and db/db + mSTZ
Table 9). This indicates that diabetes also affects endocrine hormone dysregulation. For example, NOD group T1-up1 also showed high
production and secretion in endocrine cell types beyond β-cells. In expression in cell states from db/db and mSTZ datasets (Fig. 6a) and
support of this, a recent human α-cell patch-seq study reported a loss of partially overlapped with db/db + mSTZ upregulated genes (Extended
electrophysiological identity in T2D97 and electrophysiology of δ-cells Data Fig. 10d), with the overlap containing multiple genes previously
was likewise reported to be disrupted in prediabetic mice98. However, in associated with diabetes (Gc, Fabp5, Spp1 and Vgf)104–107. NOD and
further analyses we decided to focus on β-cells due to their importance db/db + mSTZ also shared similarities in downregulated genes
in diabetes development94. (T1-down4 and T2-down2; Extended Data Fig. 10d) that were, in turn,
highly expressed in healthy mature cells (Fig. 6b). These groups
Diabetes-unique and cross-condition dysfunction in β-cells contained multiple cross-species conserved β-cell genes (Atf3, Btg2,
To find genes dysregulated in the T1D NOD model and T2D db/db and Ddit3, Egr4, Fosb and Jun)108, targets of β-cell expression program
mSTZ model β-cells, a DGE analysis was performed for each model regulator CREB (Per1, C2cd4b, Nr4a2, Fos and Dusp1)108,109 and genes
group. As cells within individual subjects can be heterogeneously dys- involved in management of metabolic stress involved in insulin pro-
functional, leading to reduced power in DGE analysis78, we leveraged duction and secretion in non-diabetic β-cells (Egr1, Hspa1b, Ddit3 and
MIA embedding to assign cells from healthy controls and disease mod- Dnajb1)82,110. This indicates that the β-cell phenotype is compromised
els along a healthy–dysfunctional trajectory (Extended Data Fig. 10a across diabetes models. In contrast, some gene groups were conversely
and Supplementary Note 8). This is of special importance for NOD mice, expressed in NOD and db/db + mSTZ analyses. For example, NOD group
as in the original study the authors observed incomplete penetrance27 T1-down3, containing some genes involved in adaptive stress response
dysfunctional β-cell phenotype27. (Txnip and Herpud1)33,111, was, in addition to healthy cells, also highly
As the DGE analysis resulted in hundreds of DEGs that are expected expressed in db/db and mSTZ model cells.
to be heterogeneous in terms of their molecular function, we clus- As it has been previously reported that diabetes results in the
tered them using their expression across all β-cells within MIA (sizes dedifferentiation of β-cells toward less-mature states in both mice
12–349 genes; Fig. 6a and Supplementary Table 10). The groups are and humans22,23,30,112 we compared the expression of upregulated
described in more detail in Supplementary Table 10 in terms of gene genes across postnatal β-cell states and embryonic cell types, includ-
set enrichment, gene membership and cell states with high expression. ing endocrine cells and their progenitors. Among both the NOD and
In the text they are referred to as T1 groups for NOD and T2 groups for db/db + mSTZ upregulated genes we found genes that were strongly
db/db + mSTZ. expressed in embryonic data or were specific to diabetes model
Nature Metabolism | Volume 5 | September 2023 | 1615–1637 1624

Article https://doi.org/10.1038/s42255-023-00876-x
DE gene groups
cells (Extended Data Fig. 10c). This shows that changes in diabetes Feng dataset (Extended Data Fig. 7). In contrast, group T2-down1 had
models involve both dedifferentiation as well as diabetes-model- a relatively low expression difference between diabetic and healthy
specific responses. MIA cell states (Fig. 6a). For both gene groups, the observed expres-
To validate our findings, we further examined whether DEGs are sion patterns in MIA already indicate that they may not generalize to
translatable to other datasets. In the Feng dataset, which is not part of other datasets that have a somewhat different healthy and diseased cell
the atlas and contains STZ-treated samples31, most T2-groups had the state composition. The dissection of DEGs based on MIA β-cell states
expected expression direction in the STZ model cells (Extended Data enabled us to explain why a subset of DEGs may not be translatable to
Fig. 10b). However, two gene groups (T2-down1 and T2-down5) did not other datasets, which is a common, usually unexplained, problem in
show different expression activity between diabetic-model and healthy scRNA-seq studies.
Feng cells. For group T2-down5 the discrepancy could be explained by To support RNA-level DGE results (Supplementary Table 10) at the
the gene group being most highly expressed in immature healthy cell protein level, we selected relatively highly expressed DEGs and stained
states from MIA (Fig. 6a), which, as discussed above, are absent in the them with specific antibodies in islets from healthy and diabetes model
Nature Metabolism | Volume 5 | September 2023 | 1615–1637 1625
sretsulc
llec eniF
Imm.1
Imm.2
Imm.3
NOD-imm.
Adult-imm.1
Adult-imm.2 Adult1
Adult2
Adult + agedM
AgedF1 AgedF2 D-inter.
NOD-D
db/db + mSTZ
mSTZ
db/db-VSG
Chem1
Chem2
Chem3
1nwod-1T 2nwod-1T 3nwod-1T 4nwod-1T 5nwod-1T 1pu-1T 2pu-1T 3pu-1T 4pu-1T 1nwod-2T 2nwod-2T 3nwod-2T 4nwod-2T 5nwod-2T 6nwod-2T 7nwod-2T 1pu-2T 2pu-2T 3pu-2T
NOD NOD db/db + mSTZ db/db + mSTZ Marked cell states down up down up
Representative of DGE analysis groups
Highlighted in the manuscript
DE gene groups
Relative
activity 1.0 0.5
0
Marked cell states
Representative of DGE analysis
healthy control group
Representative of DGE analysis
diabetes model group
Examples of cell state specific
and shared gene groups
sretsulc
llec
esraoC
)xes
yb detarapes(
T2D δ 0.4
0.3
0.2
NOD-D − F
Jaccard
index
T1D α
T2D α
T1D γ
0.1
sGED
T2D γ
T1D β
T2D β
DEGs
δ D1T δ D2T α D1T α D2T γ D1T γ D2T β D1T
Adult − M
AgedF − F AgedM − M Chem − M
db/db + mSTZ − M
Imm. − F
Imm. − M
1 elaM 2 elaM 3 elaM 4 elaM 1 elameF 2 elameF 3 elameF 4 elameF
Male up Female up
xeS
a b c
Sex
Male
Female Relative activity 1.0
0.5
0
d e
Marker
Ucn3/Insulin Aldh1a3/Insulin Nucb2/Insulin Fkbp11/Insulin Mt3/Insulin
Maturity (known)
Dysfunction (known)
WT
Dysfunction (new)
NOD
db/db
f g
Imm.1 AgedF2
Imm.2 D-inter. Imm.3 NOD-D
NOD-imm. db/db + mSTZ
NOD Adult-imm.1 mSTZ
Adult-imm.2 db/db-VSG
Adult1 Chem1
Adult2 Chem2 Adult + agedM Chem3
AgedF1
Healthy db/db + mSTZ
Intermediate
sretsulc
lleC
Adult2 D-inter.
NOD-D
Adult2
D-inter.
db/db + mSTZ
Adult2
D-inter.
db/db + mSTZ
ypN a1apsH rpiG 1bjanD 1psuD nuJ tanN 2gtB b1apsH 3piafnT
b54ddaG
3ftA 2psU 81psuD x72psU bnuJ soF 01psuD 3scoS 3tidD 4xbC 2pb2frI 2bakrP 2haiS 4creH fgV cG 5pbaF 3taalP 3adlhP 1ppS 1lpaD
Down Up
DON
ZTSm
bd/bd
Healthy control (NOD)
Fraction of cells
Healthy control (mSTZ)
20406080100
Healthy control (db/db) Relative
db/db mean expression
0 0.5 1.0
Relative mean
expression
per dataset
1.0
0.5
0
3ncU 3a1hdlA 2bcuN 11pbkF 3tM
NOD
mSTZ
Fig. 6 | β-cell diabetes dysfunction involves different molecular patterns that controls. e, Validation of selected diabetes model β-cell DEGs on protein level
are unique or shared with other conditions, including different diabetes with immunohistochemistry. The images are representative examples of three
models and aging. a, The activity of β-cell diabetes-trajectories (NOD and independent animals. Scale bars, 50 μM. For every antibody pair, the left plot
db/db + mSTZ) DEG groups across fine β-cell states (red rectangles mark shows an overlay of channels and the right shows individual channels. f, PAGA
examples highlighted in text). Cell groups representative of healthy and diabetic graph showing connectivity (lines) between fine β-cell states (dots) imposed on
states in DGE analysis are marked with blue and orange rectangles, respectively. β-cell UMAP. The connections between healthy, intermediate and diabetes model
b, Overlap of DEGs across diabetes models (T1D NOD, T2D db/db + mSTZ) states are marked in solid lines. g, Expression of DEGs with the same direction in
and endocrine cell types. c, Expression of DEG groups between aged males NOD and db/db + mSTZ trajectories in healthy, intermediate and diseased states
and females across coarse β-cell states, split by sex. Marked are cell groups per dataset (dataset 8–16wNOD is abbreviated as NOD). Expression is normalized
highlighted in the text and groups representative of healthy and diabetes per gene and dataset. imm., immature; M, male; F, female; NOD-D, NOD diabetic;
model cells from DGE analysis. d, Gene expression of diabetes markers that D.-inter, diabetic intermediate. In a, c, d and g relative expression is computed as
were validated on protein level; shown for diabetes models and associated the average of cell groups normalized to [0,1] for each gene feature.

Article https://doi.org/10.1038/s42255-023-00876-x
(NOD and db/db) mice (Fig. 6d,e). First, we validated that islets con- disease progression or a result of treatment and further investigations
tain expected healthy and dysfunctional β-cell states by profiling the are required to clarify this state.
protein expression of insulin, an established maturation marker Ucn3
(ref. 9) and a dedifferentiation marker Aldh1a3 (refs. 113,114) (Fig. 6d,e Sex differences in β-cells involve diabetes-associated genes
and Supplementary Note 10). We next profiled three new markers of Sex differences affect normal β-cell function and subsequent develop-
the T2D model: Nucb2, which is involved in insulin secretion115,116 and ment of diabetes126–129. Therefore, we assessed sex differences across
whose mutations were reported to be associated with diabetes risk117, ages and their relationships to diabetes models. Two datasets from
Fkbp11, an ER-located chaperone previously reported to be upregu- early postnatal (P16) and aged (2 years) mice with a mixture of male
lated in certain mouse T2D models118,119 and Mt3, which was reported and female cells were used. In P16 mice we did not observe any DEGs,
to be associated with β-cell death120. Protein and RNA levels of Nucb2 except for sex-linked Y-chromosome genes (Ddx3y, Eif2s3y and Uty),
were upregulated in both NOD and db/db islets and Fkbp11 and Mt3 in which were also used during data preprocessing for sex-annotation of
the db/db islets. This validation supports the observations from our cells. More DEGs were observed in aged mice (26 male and 116 female
DGE analysis and proposes new dysfunction markers on both the RNA upregulated genes; Supplementary Table 11), which is also reflected
and protein level. in the clear separation of these cells into two distinct states (Fig. 5a).
When comparing NOD and db/db + mSTZ genes to multiple To further dissect the aged DEGs we clustered them based on expres-
human datasets we did not observe the expected DEG group activ- sion across all β-cells of MIA, resulting in four female and four male
ity differences between healthy and diabetic samples in a consistent groups (female1–4 and male1–4; Fig. 6c, Supplementary Fig. 3 and
manner (Extended Data Fig. 10b); however, certain diabetes hallmark Supplementary Table 11).
genes translate across the species. For example, the Dgkb gene, whose Females are known to have higher insulin production and are less
ortholog is associated with human T2D121, was upregulated in our prone to develop T2D18,130. Indeed, we observed some DEG groups
db/db + mSTZ analysis. Thus, future studies could use our diabetes explaining these phenotypes. Group male4, which was highly expressed
DGE results to query for molecular changes shared with humans and in T2D model state (Fig. 6c), contained multiple genes related to ded-
thus assess whether pathways of interest could be further profiled with ifferentiation, immaturity and other endocrine cell types49,113,131–133
NOD, db/db or mSTZ models. (Supplementary Table 11). In contrast, the female1 group, which was
likewise expressed in T2D model state (Fig. 6c), contained multiple
A shared progression state in type 1 and 2 diabetes model β-cells genes previously reported to be upregulated in pregnancy23,134 (Supple-
One of the key goals of diabetes research is to understand the tran- mentary Table 11) as well as genes related to insulin secretion (Chgb)135
sition from pre-diabetes to diabetes and back upon treatment to and stress response (Mapk4 and Gpx3)136,137. Furthermore, a group
identify disease states where remission is still possible. To decipher expressed specifically in aged female cells (female4, 78 genes; Fig. 6c),
the relationships between healthy and diseased states we calculated contained some genes involved in insulin regulation138–140 and glucose
a partition-based graph abstraction (PAGA) on the fine β-cell states metabolism141,142 (Supplementary Table 11). Altogether, this indicates
(Fig. 6f). The connection from the main healthy state (adult2, con- that female β-cells are more inclined to diabetes-associated compensa-
taining healthy adult cells across datasets) to the T1D model state tion and male β-cells to loss of identity.
(14–16wNOD) or the T2D model state (db/db + mSTZ) led in both cases
via an intermediate state (D-inter.). Indeed, it has been suggested previ- Discussion
ously that both T1D and T2D may share some molecular stress patterns Here we present the MIA, a high-quality integrated atlas, that compiles
in β-cells, but diverge in the final outcome due to a persistent immune multiple developmental stages and disease conditions from 56 samples
or metabolic challenge, respectively27,122–124; however, we did not find a with transcriptomics readouts of over 300,000 cells. The exploration of
report of a shared intermediate state in T1D and T2D models. MIA provides new insights into islet biology and diabetes research that
The intermediate state contained both stressed healthy and dia- could not have been obtained from individual datasets. Our key discov-
betic cells (Extended Data Fig. 5d and Supplementary Note 7), includ- eries are the description of the β-cell landscape from diverse datasets,
ing cells from the Feng dataset mapped onto MIA (Fig. 4c); however, the proposition that mSTZ diabetes model molecularly resembles T2D
the sample with the largest cell proportion localizing in this state rather than T1D and the identification of molecular pathways involved
was the mSTZ diabetes model sample with regenerative anti-diabetic in different types of β-cell dysfunction. While this paper is focused on
treatment30 (GLP-1 + estrogen + insulin; Extended Data Fig. 5d). This β-cells, we also showcased that MIA can be used for studying other cell
indicates that the intermediate state may be related to either treatment types, presenting an opportunity for future studies.
effects or diabetes progression and β-cell stress. We used MIA to comprehensively describe the β-cell landscape
Molecular differences between the healthy and the intermediate across datasets and conditions. We identified molecular variation
state resembled those observed in the diabetic states (14–16wNOD, conserved across healthy adult β-cells. This included pathways of
db/db + mSTZ; Extended Data Fig. 8c,e), as described in Supplemen- immaturity and aging as well as pathways potentially involved in
tary Note 11. As the intermediate state may be related to both T1D cycling between insulin production and metabolic stress, followed
and T2D models we profiled the expression of diabetes DEGs shared by regeneration. We further proposed the use of GPs to identify and
between T1D model and T2D model DGE analyses (described above). characterize molecularly distinct cell states in the β-cell landscape.
Most of these genes already exhibited expression differences between This led to the identification of an intermediate β-cell state between
the healthy and the intermediate state and further changed from the healthy controls and different diabetes models that may be involved
intermediate to the diabetes model states (Fig. 6g and Supplementary in diabetes progression or treatment-induced remission. We also
Note 11). Notably, shared downregulated genes (89 genes) were strongly observed two distinct populations within the mSTZ model differing in
enriched for response to extracellular stimuli and transcription factor immaturity and compensatory phenotype, which may be of relevance
regulation of gene expression due to genes of activator protein-1 (AP-1) when using the STZ model in future diabetes studies. Notably, when
complex, which are involved in cell survival and death125. This indicates comparing different diabetes models, we observed that β-cells in the
that regulatory mechanisms are disrupted between the healthy and STZ model exhibited a gene expression profile akin to the db/db model
intermediate states. and not the NOD model. This was again reflected in comparison to
Our analysis suggests that the intermediate state presents a snap- human data, where mSTZ β-cells showed upregulation of T2D-related
shot of the transition between healthy and dysfunctional cells in dif- metabolic stress pathways while lacking upregulation of T1D-related
ferent diabetes models; however, it is unclear whether this is part of immune pathways.
Nature Metabolism | Volume 5 | September 2023 | 1615–1637 1626

Article https://doi.org/10.1038/s42255-023-00876-x
For future studies, MIA enables automatic cell type and state trans- libitum access to diet (irradiated standard diet for rodents, Altromin
fer as well as cross-study and cross-condition comparison by embedding 1314, Altromin Spezialfutter) and water.
cells into a shared reference space. We have demonstrated this with the Islets of Langerhans have been isolated using a standard pro-
Feng dataset, which is not part of MIA, resulting in the expected mapping tocol148,149. The aged dataset was generated from islets of Langer-
of healthy control and STZ diabetes model β-cells to the corresponding hans isolated from the Fltp lineage-tracing mouse model (Fltp iCre
MIA regions. This also showed that the immature populations present in mTmG)150 in mice older than 2 years. Two male and two female mice
MIA and the Feng dataset differ, indicating that the reason for them not were pooled together after islet isolation and before FACS. The sort-
sharing markers is likely of biological nature, attributed to different cell ing was used to separate cells into Fltp-negative (tomato-positive),
states. Our vision is that future studies can similarly map their datasets Fltp-lineage-positive (GFP positive) and Fltp-transient (double-positive)
on top of MIA and publicly provide the generated embeddings to further populations (Supplementary Fig. 4), using FACSDiva (v.6.1.3) and
extend the conditions compiled in MIA. As an example, we showed this FlowJo (v.10.8.1) software. Separate libraries were generated for each
for a young (P3) sample from the Feng dataset, for which we do not sorted population after pooling across sexes. For the 4m dataset,
have a matched developmental stage in MIA, with its embedding filling we used the Fltp reporter mouse line FltpZV (ref. 151). The pancreas
the gap between our embryonic and older postnatal samples. head and tail were anatomically separated before islet isolation. Islets
The heterogeneity compiled within MIA also enables contextu- from six FltpZV/+ male mice were pooled. Subsequently, Fltp Venus
alization at the gene level. For example, known β-cell maturity and reporter-positive and negative cells were sorted (Supplementary Fig. 4),
dysfunction markers are more heterogeneous than expected, showing thus generating four libraries. The metadata of all samples are shown
distinct expression subgroups across β-cells states of MIA. Similarly, in Supplementary Table 1.
researchers could use the interactive cellxgene143 instance of MIA to Libraries of single cells were produced using the Chromium
analyze the expression of their genes of interest across cell types and Single-Cell 3′ library and 10x Genomics gel bead kit v.3.1 (PN 1000121)
diverse biological conditions within MIA. in the aged dataset and with v.2 (PN 120237) in the 4m dataset. Briefly,
Our next aim was to describe which pathways are involved in dif- 10,000 cells were loaded per channel of a 10x chip to produce gel
ferent β-cell dysfunction phenotypes. Therefore, we used MIA to group bead-in-emulsions (GEMs). Then the samples underwent reverse tran-
DEGs and contextualize them based on expression across other con- scription to barcoded RNA, followed by cleanup, complementary DNA
ditions. For diabetes-model DEGs this approach revealed phenotype amplification, enzymatic fragmentation, 5′ adaptor and sample index
specific as well as shared molecular changes across diabetes mod- attachment. The samples of the aged dataset were sequenced using a
els, aging and immaturity. Grouping of DEGs also identified distinct NovaSeq6000 (Illumina) with 100-bp paired-end sequencing and the
dysfunction-associated changes across sexes, explaining lower suscep- samples of 4m dataset were sequenced using a HiSeq4000 (Illumina)
tibility of females for diabetes due to upregulation of compensatory with 150-bp paired-end sequencing of read 2.
rather than loss of identity pathways that were observed in males. In the
future, the dissection of dysfunction patterns based on multiple pheno- Datasets included in the atlas
types may provide valuable insights for personalized medicine, which is We used nine mouse pancreatic islet scRNA-seq datasets previously
based on knowledge about different disease-associated molecular pat- generated with 10x Genomics Chromium technology. Data availabil-
terns. It may also be useful for drug repurposing, which relies on path- ity is described in Table 1. Public data were obtained from the GEO in
ways shared across diseases144–146. For example, it was previously shown July 2020 by comprehensively searching for mouse pancreatic islet
that removing senescent cell populations in NOD mice and models of scRNA-seq datasets. From the collected datasets we excluded datasets
aging improves the overall regulation of glucose levels27,103. Indeed, that would not be applicable for analysis of β-cell heterogeneity, such
in our analysis, we observed upregulation of senescence-associated as cancer and reprogramming datasets as well as datasets with low
genes in both aged and T1D model cells. endocrine cell counts, including embryonic datasets, with the excep-
We show that our results are reproducible in independent mouse tion of an in-house embryonic dataset. We also excluded datasets that
transcriptomic data and in immunohistochemistry, proposing new were not generated with Chromium (namely Smart-seq2) as most of
markers of T2D model-associated dysfunction (Nucb2, Fkbp11 and them had low cell counts and could lead to strong cross-technology
Mt3). Comparison to human datasets revealed some similarities to batch effects due to differences in sensitivity and bias in the type of
mice; however, new methods will be required to improve cross-species captured genes152. Furthermore, some of the integration methods
comparison and translation. are not designed for full-length reads, such as Smart-seq2 (ref. 41).
In conclusion, MIA provides a useful tool for islet biology and Altogether, using additional sequencing technologies would make
diabetes research. It is available as a curated resource in formats that the integration more challenging.
enable interactive exploration via cellxgene and computational analy- All computational analyses of scRNA-seq data were performed
ses (https://github.com/theislab/mouse_cross-condition_pancre- with Scanpy (v.1.6–1.8.1)153, except where noted elsewhere.
atic_islet_atlas), including access to the cellxgene curated dataset via
Sfaira147. Our discoveries in β-cell biology showcase how MIA can be Datasets for atlas validation
used both as a reference of cell states as well as for further querying of For validation we collected public mouse and human scRNA-seq
gene expression across conditions. datasets (Table 2 and Supplementary Table 12) and downloaded their
expression count matrices and metadata from GEO and paper sup-
Methods plements. If raw counts were available, re-normalization was per-
Animal studies were conducted with adherence to relevant ethical formed with the Scanpy normalize_total function, otherwise, the
guidelines for the use of animals in research in agreement with German available pre-normalized data were used. For downstream analyses,
animal welfare legislation with the approved guidelines of the Society log(expr + 1)-transformed normalized expression was used. We manu-
of Laboratory Animals and the Federation of Laboratory Animal Science ally unified cell type annotation from original studies to a shared set of
Associations. The study was approved by the Helmholtz Munich Animal cell-type names by renaming existing labels. No further preprocessing
Welfare Body and by the Government of Upper Bavaria. was performed on these datasets. These datasets were not included
in the atlas and were always analyzed individually. In the text, we refer
Generation of new mouse samples included in the atlas to the GSE137909 dataset as the Feng dataset. Where necessary, we
Mice were housed in groups of two to four animals and maintained mapped genes across species based on ortholog information from
at 23 ± 1 °C and 45–65% humidity on a 12-h dark–light cycle with ad BioMart154 (Ensembl Genes v.103).
Nature Metabolism | Volume 5 | September 2023 | 1615–1637 1627

Article https://doi.org/10.1038/s42255-023-00876-x
Preprocessing of datasets for atlas building based on per-cell marker scores (for example, ε-cells in the P16 dataset).
Gene expression counts were calculated based on genome versions Here and in the below re-annotation of the integrated data we relied
described in Table 1 with 10x Genomics CellRanger (v.2.2.1–v.3.1.0)155. on the following cell type markers across multiple datasets, although
Each dataset was separately preprocessed with the below-described on the per-dataset level, we also used other markers, expressed in cell
steps, except when we note that a processing step was performed per subpopulations present in only some of the datasets. The marker list is
sample, and filtering thresholds were determined on a per-dataset level. acinar: Cpa1, Prss2; α: Gcg; β: Ins1, Ins2; δ: Sst; ductal: Krt19, Muc1, Sox9;
endothelial: Pecam1, Plvap; ε: Ghrl; γ: Ppy; immune: Cd52, Lyz2, Ptprc;
Ambient gene identification stellate-activated: Col1a2, Bicc1, Pdgfra; stellate-quiescent: Ndufa4l2,
To reduce the effect of ambient expression on embedding calculation Acta2, Cspg4, Rgs5; and Schwann: Cryab, Plp1, Sox10. Expected multi-
we removed the most prominent ambient genes, which were identified plet rates were computed and together with Scrublet scores used to
as described here. We selected likely empty droplets that contained determine which annotated multiplet cell types present true cells or
only ambient RNA based on having fewer than 100 counts. Gene propor- residual multiplets. We annotated β-cell states based on the expression
tions within empty droplets were computed on raw counts per sample, of known β-cell heterogeneity markers.
representing gene proportions within the ambient RNA. Genes with
the highest ambient proportion were selected with a dataset-specific Batch-wise preprocessing for integration
ambient proportion threshold, selecting genes as the union across We tested different methods for ambient expression correction: Cell-
samples, generating a set of approximately 20 genes per dataset. Owing Bender (v.0.2.0)162, SoupX (v.1.5.0)163 and DecontX (from celda v.1.5)164.
to the proportional nature of expression measurements a relatively We did not use CellBender preprocessed data further as we observed
high ambient proportion of some genes leads to lower proportions in non-homogeneous correction within clusters, namely some genes
other ambient genes. Thus, we reduced the ambient threshold when known to be cell type-specific, such as β-cell-specific Ins1 and Ins2,
some genes had a relatively high ambient proportion to also capture were removed partially and at different levels across cells within other
fewer ambient genes that are nevertheless known to strongly affect cell types. For other methods, different ambient correction strengths
ambient profiles, such as endocrine hormone genes. Additionally, were used and one or more were selected for integration per method.
a larger set of approximately 100 genes was generated with a more Non-ambient-corrected data were also used. Top ambient genes
permissive threshold that aimed to include top ambient genes so that were excluded, also in ambient corrected datasets (using the smaller
selecting more genes would no longer evidently increase the captured ambient gene set). The ambient correction method selected for final
cumulative ambient proportion given by the sum of the per-gene integration is described in the ‘Integration selection’ section. Genes
ambient proportions. previously marked as too lowly expressed on a per-dataset level were
also removed. To enable integration with samples as batches and future
Dataset quality control mapping of new samples onto the reference the data was per-sample
Empty droplet score was computed per sample with DropletUtils scran normalized and transformed with log(expr + 1). The batch-wise
(v.1.10.3)156 emptyDrops function using LogProb output for down- re-normalization was performed as scran size factors may not be com-
stream visual quality control assessment purposes. Cell-containing parable across multiple runs due to size factors being relative within
droplets as determined by the CellRanger pipeline were used in down- a dataset160. These additional batch differences can thus be learned
stream analyses. Cell filtering was performed based on guidelines to be corrected by the integration model. By performing batch-wise
published previously157, excluding cells with a low number of expressed normalization (here, batch is a sample) we ensure that the integration
genes, low total counts or high mitochondrial proportion and outliers model can account for this effect when removing batch effects. For scVI
with a very high number of total counts or expressed genes. Genes integration non-normalized data were used. Expression matrices of all
expressed in a very small number of cells and top ambient genes were samples were merged, retaining the intersection of genes. The 2,000
excluded for the purpose of annotation and integration. Doublets were HVGs obtained with the scIB (developmental version, last updated on
filtered out with Scrublet (v.0.2.1)158 scores computed per sample using 17 January 2022)41 hvg_batch function was used.
a manually set threshold to separate the scores into cross-cell type
doublet and potential non-doublet populations as proposed in the Integration selection
tutorial158, while ensuring that selected doublet cells mainly mapped For integration we used scVI v.0.7.0a5 (ref. 40) with hyperopt hyperpa-
into discrete cluster locations on the Uniform Manifold Approximation rameter optimization and scArches v.0.1.5 (ref. 42) with manual param-
and Projection (UMAP) embedding. The choice of the threshold was eter optimization. First, we performed integration on the annotated
set permissively, as indicated by the presence of some residual doublet data only to select scVI parameters with hyperopt (number of network
populations in the final atlas version. layers and their size, number of latent dimensions, reconstruction loss,
dropout rate, learning rate, gene dispersion and number of epochs) and
Dataset-wise cell annotation scArches parameters based on visual evaluation (different HVG selec-
To perform cell annotation within individual datasets normalization tion, integration strength regulated by the weight between reconstruc-
was performed per dataset with scran (v.1.16.0–1.18.7) pooled size tion and Kullback–Leibler divergence loss, number of network layers
factors159,160, data were log(expr + 1)-transformed and 2,000 highly and reconstruction metrics), to ensure that selected parameters lead
variable genes (HVGs) were selected with Scanpy using the cell_ranger to a reasonable integration. Afterward, integration was performed on
selection flavor and samples as batches. The cell cycle stage of each all data. Different integration methods and preprocessing combina-
cell was annotated using the Cyclone method161 as implemented in tions were evaluated with scIB metrics. We added a new biological
scran. For datasets without per-cell sex information, the sex was anno- conservation metric named Moran’s I conservation, which does not
tated based on Y-chromosome located HVGs with high expression. require cell-type annotation. For biological conservation evaluation
We assigned cells into insulin, glucagon, somatostatin and pancreatic we excluded unannotated and multiplet cells, except for Moran’s I,
polypeptide high or low groups per-sample based on scores from the which could be run on all cells. As annotation was available only for a
Scanpy score_genes function. Cell types were annotated in the follow- subset of cells the batch correction metrics were run both on all data,
ing datasets: P16, 4m, aged, mSTZ (healthy sample), db/db (healthy using clusters instead of cell-type labels and on the annotated data
samples), based on known pancreatic cell type markers followed by subset. We also performed evaluation on β-cells only, using β-cell
recursive subclustering until homogenous clusters were reached. states as cell labels, with different integration strengths. Top selected
Rare cell types that did not form a separate cluster were annotated integrations were run multiple times to better distinguish between
Nature Metabolism | Volume 5 | September 2023 | 1615–1637 1628

Article https://doi.org/10.1038/s42255-023-00876-x
random initialization and true performance variation. The best method and the genes were pooled across samples. These ambient genes were
(removed top ambient genes and scArches-cVAE) was selected based clustered based on expression across integrated cell clusters. Ambient
on summarized biological conservation and batch correction scores, gene clusters were assigned to non-β-cell originating ambient genes if
as described in scIB, with a special focus on β-cell state conservation. they had relatively low expression across all β-cell clusters compared
We also tested β-cell-specific integration, using β-cells defined to cell clusters coming from other cell types. Besides making the set
based on an integrated annotation (see below) with the same integra- of likely non-β-cell ambient genes, we used during interpretation a
tion settings as for the whole atlas, but with multiple different inte- per-gene metric that can indicate ambient gene origin, namely relative
gration strengths in scArches-cVAE. Batch correction evaluation was gene expression in a cell type compared to other cell types, with higher
run on all cells, using clusters instead of cell type labels and biological scoring genes being less likely ambient. As this metric was used for
preservation evaluation on cells that had state annotation. The results postnatal endocrine analyses the embryonic clusters were excluded as
were compared to metrics computed on the same set of cells from the they are not expected to contribute to ambience in postnatal samples.
whole atlas integration. The atlas subset was then subclustered using Leiden clustering with
For comparison, we also show unintegrated embedding, which was resolution of 2. Mean expression in cell clusters was maxabs-scaled
computed using the same set of genes as the final atlas integration. We across clusters, representing relative expression in each cluster. To
normalized expression using the Scanpy normalize_total function as determine the relative expression of a gene in a cell type we used the
scran normalization performed on individual samples, as used for inte- highest relative expression obtained across all cell clusters containing
gration, leads to lower comparability of normalization factors across predominantly that cell type.
samples. Data were log(expr + 1)-transformed and scaled, followed by In all further analyses where we needed to reduce the number
principal-component analysis (PCA)-embedding computation that was of cells due to computational constraints we prepared pseudobulk
used as the basis for UMAP. data (here, termed ‘fine pseudobulk’) by Leiden clustering with high
resolution (such as resolution of 20) to create tens or hundreds of
Integration evaluation with Moran’s I conservation clusters (depending on data size) that should capture the majority
We proposed a new biological conservation metric for comparison of heterogeneity within the data. This is akin to recently proposed
across integration runs without the need for cell type annotation that methods that aim at creating so-called ‘metacells’ that group together
determines how strongly genes are variable across the integrated cells without biological differences166,167. Pseudobulk expression was
embedding. Namely, if embedding captures biological variation at a computed as the mean of log(expr + 1)-transformed normalized expres-
finer scale, for example, within cell types, then the expression variation sion within each cluster. For DGE analysis on pseudobulk (here termed
of genes that are potential determinants of cell state differences ‘metadata-based pseudobulk’) we grouped cells based on their meta-
(for example, HVGs) should be non-random across the embedding. data, such as sample and cell type, as before suggested for single cell
The method first computes HVGs (g, 1,000 genes) on the expression DGE analysis168. Here, normalized counts were summed across cells
data with Scanpy highly_variable_genes function using cell_ranger and log(expr + 1)-transformation was not applied.
flavor and batch_key parameters. Moran’s I for these HVGs is then
computed on the integrated embedding (i) with Scanpy morans_i func- Identification of endocrine cell type markers
tion. This function uses information about each cell’s k-nearest neigh- For the identification of endocrine cell type markers one-versus-one
bors graph computed with Scanpy neighbors function on the integrated DGE analyses were performed with edgeR (v.3.32.1)169. For the post-
embedding with Euclidean distance metric. The final score is computed natal markers metadata-based pseudobulks of postnatal datasets
as the mean of per-gene scores. This score is rescaled to fall within range per cell type, sample and sex were created. We excluded embryonic,
[0,1], matching other scIB scores. This can be formulated as: doublet and endocrine proliferative cell types. The former cell type
was excluded as a minute number of postnatal cells mapped to the
g
1 embryonic clusters (Extended Data Fig. 1). The latter two cell type
g
∑
1
(ig)+1
groups were excluded as they share gene expression with matched
score=
2 non-doublet and non-proliferative cell types, which would prevent the
The final annotation of the integrated atlas identification of these genes as DGE markers. Lowly expressed genes
We defined cell types on the integrated atlas by consecutive Leiden165 were removed with edgeR and a single DGE test was fitted, using edgeR
subclustering with Scanpy, namely by manually selecting clusters to general linear model (GLM) with robust dispersion, with sample and
be subclustered as needed to separate cell types, relying on informa- sex as covariates and two-sided likelihood-ratio significance testing.
tion about previously annotated cells, hormone expression high/low To obtain one-versus-rest upregulated genes for each endocrine cell
assignment and quality metrics. Namely, empty droplets were identi- type the factors across cell types were compared. Marker genes were
fied based on low expression and high empty droplet probability and selected based on a false discovery rate (FDR) <0.05 and log fold change
doublet clusters based on higher doublet scores and expression of (FC) >1.5 against all other cell types. In the supplementary tables we
markers of multiple cell types. We compared the re-annotation to the reported the maximal adjusted P values across compared cell types and
annotation from original publications, for which we manually unified for logFC we reported 0 if logFC across comparisons had both nega-
cell type labels by renaming the labels to a shared set of names. tive and positive values and otherwise signed minimal logFC based on
As scran normalization performed per-sample is not comparable absolute value sorting. For embryonic markers, the embryonic dataset
across samples (described above) scran size factors were recalculated with cell type annotation from the original study60 was used. The Fev+
on the integrated cell clusters and the atlas was jointly re-normalized. cluster was excluded as it contained precursors of individual endocrine
In downstream analyses, we used this normalized data, except for the cell types with similar expressions as in the descendant cell types,
methods that required raw counts. which would prevent the identification of markers. Metadata-based
To disentangle biologically relevant differentially active genes pseudobulks were created per cell type and sample, whereas sex was
from genes whose expression is likely a result of ambient expression dif- not used as a covariate, as at this age strong sex differences were not
ferences in the downstream analyses, we defined genes that may be pre- expected. Endocrine cell-type markers were identified as for the post-
dominately ambiently expressed in a given cell type. Top ambient genes natal datasets. In the postnatal dataset, we used 52 samples and in the
likely not coming from β-cells were defined as follows. For each sample, embryonic dataset we used 4 samples, with some cell types being rep-
genes with high expression in empty droplets, containing fewer than resented in fewer samples and some samples containing data pooled
100 counts, were selected with a single threshold across all samples across multiple animals.
Nature Metabolism | Volume 5 | September 2023 | 1615–1637 1629

Article https://doi.org/10.1038/s42255-023-00876-x
Comparison of embryonic and postnatal endocrine cells later merge clusters that we could not interpret as separate based
We grouped α-, β- and δ-cells into three groups per cell type: embryo on the criteria described above while ensuring that we did not miss
(cells that were annotated as a certain endocrine cell type in the original any unique clusters.
embryo study and mapped into the embryo endocrine atlas cluster); Cluster-specific markers conserved across datasets were computed
embryo postnatal-like (cells from the embryo dataset that mapped into as follows. Data were subsetted to exclude low-quality clusters and the
one of the postnatal endocrine atlas clusters); and postnatal (cells from embryo dataset as it contained too few β-cells (fewer than 20 per sample
postnatal datasets that mapped into one of the postnatal endocrine across all β-cell clusters). Cell groups used for DGE were defined as a
atlas clusters). For embryo and embryo postnatal-like cell types, we combination of cluster and dataset, using for each cluster only datasets
computed what proportion of embryonic cells per sample-specific with a high proportion of cells in that cluster in at least one sample.
age group they represent. For each dataset-cluster group DGE analysis was performed with the
Scanpy rank_genes_groups t-test function against all other cell groups,
Reference mapping of the external mouse dataset except the ones from the same cluster, excluding genes that were lowly
The Feng dataset (query) was re-normalized per-sample with scran expressed in both clusters before DGE analysis. The number of samples
and log(expr + 1)-transformation to match atlas (reference) datasets per group varied across cell states, with the total number of considered
preprocessing. The reference scArches model was used to compute samples before grouping being 52, with some samples containing pooled
the query embedding, using samples as batches. For query β-cell map- animals. As markers, we selected genes that were significantly upregu-
ping analysis the cell type annotations from the original study31 were lated (FDR < 0.1 and logFC > 0) in all datasets across all other cell groups
used. A joint UMAP embedding of query and reference β-cells was and for plotting genes were prioritized based on the highest minimal
computed, as well as a UMAP with added reference embryonic β-cells, logFC across all comparisons. Genes were further filtered to select likely
using β-cells from the original study annotation60 that mapped into non-ambient genes by keeping only genes with relatively high expres-
the atlas embryo endocrine cluster, and reference proliferative β-cells, sion in β-cells (>0.7). Hemoglobin genes were also removed as they were
defined as endocrine proliferative cells that were previously annotated not caught by the relative expression filter as erythrocytes are absent
as highly expressing insulin, but not other hormones. Query β-cell from data, but the transcripts are still present in the ambient RNA.
states were predicted based on atlas coarse β-cell states with the addi- Markers of adult, immature and T2D model states were visually
tion of embryonic and proliferative β-cell groups. For cell type transfer validated on the external mouse dataset. The healthy β-cells were
a weighted k-NN classifier adapted from scArches manuscript42 was grouped by age and the STZ-treated cell groups were based on the
used with an uncertainty threshold of 0.75. administration of insulin.
Translation of markers to the human data was tested based on all
Comparison of diabetes models to human T1D and T2D collected human datasets with per-dataset one-versus-rest one-sided
To obtain T1D and T2D gene sets conserved across human datasets t-tests on cell level and P value significance threshold of 0.05. We also
the T1D or T2D cells were compared against cells from non-diabetic report log-based logFC between group means. The following cell
2
samples in each human dataset (the number of samples in each group groups were defined: T1D or T2D groups contained all cells annotated
varied across datasets; Supplementary Table 12 shows sample group as T1D or T2D and were used to test both known T1D or T2D markers as
sizes). Only genes expressed in at least 10% of diabetic or healthy cells well as our NOD or db/db + mSTZ markers, respectively and for other
per dataset were used. Genes with an FDR <0.25 and logFC >0.5 in at marker groups only healthy donor cells were used, with the adult set
least half of the datasets based on the Scanpy rank_genes_groups t-test used to test our adult mouse cluster and contained ages of 19–64 years,
function (two-sided Welch’s test on cell level) were selected. mature set used to test known maturity markers and contained ages of
Gene set enrichment was computed with hypeR (v.1.6.0)170 at the 19 years or more, aged male or female sets contained ages of 65 years
FDR threshold of 0.25 using Gene Ontology (GO), KEGG and Reactome or more and immature set ages of 18 years or less. Age groups were
gene sets from MSigDB (v.7.4.1). Before enrichment, each gene set was defined based on OLS HsapDv human life cycle stages definitions171. The
subsetted to genes present in the background that consisted of all number of samples varied across groups and datasets (Supplementary
genes used for the analysis (here, genes tested for DGE) and gene sets Table 12 provides more details).
containing less than five or more than 500 genes were removed. From
enriched gene sets with shared genes, we manually selected representa- Gene programs in β-cells
tive gene sets to be highlighted in the text. To define GPs we first identified genes variable across embedding and
Mouse diabetes model β-cells were scored for both the newly then clustered them based on coexpression (Fig. 5d), as described
defined and literature-based gene sets with Scanpy score_genes below. To identify variable genes low-quality coarse β-cell clusters
function on each dataset. Comparisons were performed between were excluded before the analysis as they could lead to high spatial
the following groups: in the 8–16wNOD dataset the 8-week (healthy) autocorrelation scores of genes associated with data quality. Lowly
versus 14- and 16-week samples (diabetic); in the mSTZ dataset con- expressed genes and the non-β-cell ambient gene set were removed.
trol (healthy) versus the mSTZ-treated sample (diabetic) and in the Moran’s I was used to assess the autocorrelation of expression across
db/db dataset control (healthy) versus db/db sham-operated samples the integrated embedding (all 15 dimensions). We observed a bias of
(diabetic). Gene set score distributions in healthy and diabetic groups genes expressed in fewer cells toward lower Moran’s I, which would lead
within each dataset (sample numbers for healthy mSTZ = 1, db/db = 2, to lowly expressed genes unjustly being less often selected as variable
8–16wNOD = 3; and diabetic mSTZ = 1, db/db = 2, 8–16wNOD = 6; some based on Moran’s I threshold. To account for this bias, we regressed
samples contained pooled animals) were compared using a two-sided out the effect of the number of cells expressing the gene on Moran’s I.
Mann–Whitney U-test on cell level and a natural-logarithm based logFC For this regression we used genes likely not to be truly variable across
was computed between distribution medians. the embedding, as explained below, to estimate the base-level effect
of expression sparsity across cells on Moran’s I. Genes likely not to be
Coarse β-cell states and their markers truly variable were selected as follows: most highly expressed genes
Clusters were computed with the Scanpy Leiden function and were (N cells ≥ 40,000 from a total of 99,361 cells) were excluded as they were
thereafter added descriptive annotation based on sample ratios deviating from the trend toward higher Moran’s I values, which was
across clusters, relying on sample metadata, quality scores and rela- likely due to their importance in β-cell function and thus higher vari-
tionships between clusters determined with PAGA. Initial clustering ability across the β-cell embedding. The remaining genes were binned
was performed with a relatively high resolution so that we could (N bins = 20) based on the number of cells in which they were expressed
Nature Metabolism | Volume 5 | September 2023 | 1615–1637 1630

Article https://doi.org/10.1038/s42255-023-00876-x
and the five genes with the lowest Moran’s I from each bin were selected quality. Control samples from the chem dataset were not used as they
for regression, representing the base-level (likely not biologically rel- showed lower integration of β-cells, indicating potential strong batch
evant variable) Moran’s I at certain expression strength. The regression effects, which could negatively affect the identification of variable
was fitted on the selected genes and then the corrected Moran’s I score gene groups conserved in healthy β-cells. Thus, healthy adult sam-
was computed as the residuals from regression for all genes for which ples from db/db, mSTZ and 4m datasets were used. For each sample,
the uncorrected Moran’s I score was initially computed. Finally, GPs lowly expressed genes were removed and a neighborhood graph
were defined by selecting genes with the highest corrected Moran’s I was computed on per-sample PC embedding for Moran’s I computa-
and clustering them using fine pseudobulk cell clusters as features with tion, as described in the ‘Gene programs in β-cells’ section. Here, we
hierarchical clustering and visually determined cutting threshold based adjusted the threshold for removing genes expressed in many cells
on a heat map of gene expression across pseudobulks. Gene set enrich- from Moran’s I score correction regression to expression in at least
ment of GPs was computed as for the human T1D and T2D conserved 30% of cells. Genes with high Moran’s I in all samples were selected.
genes. We supplemented GP gene set enrichment interpretation with To ensure that gene clusters are conserved across samples the genes
marker-based domain knowledge to support β-cell-specific functional were clustered based on the highest distance on per-sample fine
annotation, which is not fully encompassed by the more generic gene pseudobulks using hierarchical clustering. The cutting threshold
sets available in KEGG, GO and Reactome. was visually determined based on a heat map of gene expression
The ratio of variance explained by GPs per dataset was computed across per-sample pseudobulk. Gene group scores were compared
based on principal component (PC) regression. For each dataset, lowly to the expression of known β-cell functional and phenotypic markers
expressed genes were removed and 50 PCs were computed based on extracted from the literature, with marker correlations computed on
HVGs. Cells were scored for GP activities with the Scanpy score_genes per-sample pseudobulks and summarized as a mean of per-dataset
function (excluding genes missing from each dataset from GPs) to ana- means across per-sample scores. Gene set enrichment was computed
lyze how well GP scores of all or individual GPs explain each PC based as for β-cell GPs.
on regression R2 (coefficient of determination). The total variance To find the cells with the highest expression of each gene group
explained was computed as a sum of R2 across PCs weighted by the ratio we used Scanpy score_genes function on individual healthy adult sam-
of variance explained by each corresponding PC. For comparison, the ples, followed by selection of 50 cells with the highest score. As the
same procedure was used to evaluate variance explained by random Feng dataset had a low number of healthy adult β-cells we performed
gene groups of the same size as the GPs, repeating the procedure ten scoring on all control samples together and selected only the top 20
times to estimate the random distribution. For the analysis of explained cells per gene group.
variance in healthy mouse and human samples, only samples with at
least 100 β-cells were used and the explained variance was computed as Differential expression in T1D model and T2D model β-cells
described above, repeating the calculation for random gene groups 100 We performed DGE analysis on all samples from 8–16wNOD (n = 9)
times. The significance of the explained variance by GPs was computed and from db/db and mSTZ (n = 15, samples contained pooled animals)
as a one-sided empirical P value compared to the distribution for the datasets, excluding low-quality coarse β-cell clusters. A continuous
matched random gene group. disease process (Extended Data Fig. 10a) was computed with MELD
(v.1.0.0)174 on the integrated embedding as healthy sample densities
Fine β-cell states normalized over healthy and diseased densities, using for healthy and
Each cell was scored for each GP with the Scanpy score_genes function diseased the same set of samples as in the diabetes model comparison
followed by averaging within the fine pseudobulk clusters to speed to human diabetes-associated gene sets. In the db/db + mSTZ analysis,
up further analysis. The GP scores were used as features to cluster the final MELD healthy and diseased scores were computed as a mean
pseudobulk clusters into β-cell state clusters using hierarchical clus- over datasets-specific scores. We observe that the resulting process
tering followed by visual selection of the cutting threshold based on corresponds to the gradient from the healthiest (highest healthy sam-
GP activity purity within clusters and unique pattern of GPs across ple cell density within a region) to the most diabetically stressed cells
clusters. Each cell was assigned to the cluster of its pseudobulk group. (highest diabetes model sample cell density within a region), with the
The clusters were named based on the metadata of the samples with process value of individual cells being determined based on cell embed-
a large proportion of cells within the cluster. The resulting β-cell state ding location rather than just sample membership. Genes expressed
clusters were used to obtain a pruned PAGA graph, selecting a pruning in less than 5% of healthy or diabetic sample cells were removed. To
threshold that separated between high and low connectivities. assess linear change in gene expression along the disease process we
We analyzed GP-based molecular differences for individ- used diffxpy (v.0.7.4)175 two-sided Wald test that fits a negative binomial
ual datasets between healthy and diseased states (adult2 versus model to raw counts across cells using expression normalization size
db/db + mSTZ (for datasets db/db and mSTZ) and versus NOD-D factors as exposure. Dataset information was used as a covariate in the
(for dataset 8–16wNOD)) and two diseased states (db/db + mSTZ and db/db + mSTZ analysis. The DEGs were selected based on FDR < 0.05,
mSTZ for dataset mSTZ). All β-cells were scored for GP activity with the logFC (binary logarithm of the relevant model coefficient representing
Scanpy score_genes function and individual scores were normalized linear change) >1 and relative expression in β-cells >0.2, to keep only
across cells to [0,1] with winsorizing by removing the highest and low- genes that are less likely ambient, as described above. For comparison
est 20 cells for setting the scaling range. The per-dataset differences to the embryonic data the [0,1]-normalized expression of upregulated
between means of the normalized scores within clusters were then genes was plotted across fine β-cell states and embryonic clusters as
used for cluster comparison. annotated in the original study.
We manually extracted known markers of β-cell heterogeneity For both DGE analyses the up- and downregulated genes were sepa-
from the literature. For plotting across fine β-cell states we excluded rately hierarchically clustered on the whole β-cell fine pseudbulk data.
markers expressed in less than 1% of β-cells and plotted mean expres- Cutting thresholds were selected visually based on heat maps portray-
sion per cell state. A heat map was created with ComplexHeatmap ing gene expression grouped across fine pseudobulks. All β-cells were
(v.2.11.1)172,173. scored for DEG groups with the Scanpy score_genes function and the
scores were averaged within β-cell clusters. Gene set enrichment was
Conserved β-cell heterogeneity in healthy samples computed as described for human T1D and T2D genes. Gene member-
Low-quality coarse β-cell clusters were excluded as they could lead ship across groups was compared as the relative overlap normalized
to high spatial autocorrelation scores of genes associated with data by the size of the smaller group.
Nature Metabolism | Volume 5 | September 2023 | 1615–1637 1631

Article https://doi.org/10.1038/s42255-023-00876-x
The DEGs in NOD and db/db + mSTZ were compared to three maintained at 23 ± 1 °C and 45–65% humidity on a 12-h dark–light cycle
human datasets with T1D samples and one mouse and seven human with ad libitum access to diet (irradiated standard diet for rodents,
datasets with T2D samples, respectively. We scored cells for each DEG Altromin 1314, Altromin Spezialfutter) and water.
group activity with the Scanpy score_genes function, followed by [0,1] Mice pancreases were dissected and fixed (4% PFA–PBS, 24 h
normalization across cells and separately plotted cells from healthy at 4 °C). The organs were cryoprotected in a sequential gradient of
and diabetic samples. 7.5, 15 and 30% sucrose–PBS solutions (each solution 2 h at room
For analysis of the DGE patterns in relationship to the D-inter. temperature). Next, pancreases were incubated in 30% sucrose and
cluster the genes up- or downregulated in both NOD and db/db + mSTZ tissue-freezing medium (Leica) (1:1, overnight at 4 °C). Afterward,
were obtained. We plotted their expression per diabetes model datasets they were embedded using a tissue-freezing medium. Sections of
across the adult2, D-inter. and 14–16wNOD (for 8–16wNOD dataset) or 20-μm thickness were cut from each sample mounted on a glass slide
db/db + mSTZ (for db/db and mSTZ datasets) clusters. We normalized (Thermo Fisher Scientific).
gene expression across clusters in each dataset to [0,1]. We computed Islet isolation was performed by collagenase P (Roche) digestion of
the gene set enrichment of the shared DEGs as for human T1D and T2D the adult pancreas. We injected 3 ml collagenase P (1 mg ml−1) into the
genes. The GP differences between adult2 and D-inter. clusters were bile duct and the perfused pancreas was consequently dissected and
computed for individual datasets (db/db, mSTZ and 8–16wNOD) as placed into 3 ml collagenase P for 15 min at 37 °C. Then, 10 ml G-solution
described in the section ‘Fine β-cell states’. (HBSS (Lonza) + 1% BSA (Sigma)) was added to the samples followed
by centrifugation at 563g (Eppendorf Centrifuge 5910R) at 4 °C. After
Differential expression in T1D model and T2D model another washing step with G-solution, the pellets were resuspended
endocrine cells in 5.5 ml gradient preparation (5 ml 10% RPMI (Lonza) and 3 ml 40%
To compare DEGs across diabetes models and endocrine cell types we Optiprep (Sigma) per sample) and placed on top of 2.5 ml of the same
fitted a joint model with edgeR. Cells from healthy adults (datasets solution. To form a three-layer gradient, 6 ml G-solution was added on
4m, 8–16wNOD samples aged 8 weeks, db/db control, mSTZ control; the top. Samples were then incubated for 10 min at room temperature
n = 10, some samples contained pooled animals), a T1D model (dataset before subjecting to centrifugation at 523g (settings were acceleration
NOD_progression samples aged 14 and 16 weeks; n = 6) and T2D models 3, stopping 0; Eppendorf Centrifuge 5804R). Finally, the interphase
(datasets mSTZ and db/db, both without treatment; n = 3) were used between the upper and the middle layers of the gradient was collected
to compute metadata-based pseudobulks per disease status group, and filtered through a 70-μm nylon filter and washed with G-solution.
sample, dataset, sex and endocrine cell type. Lowly expressed genes Islets were handpicked under the microscope. For fixation, islets were
were removed with edgeR. A single expression model was fitted, using incubated in 4% PFA–PBS for 15 min at room temperature.
edgeR GLM with robust dispersion, with dataset and sex as covariates. For immunostaining, the cryosections were rehydrated and then
A two-sided likelihood-ratio test was used to compare model factors permeabilized (0.2% Triton X-100-HO for 30 min at room temperature).
2
for each T1D model or T2D model cell type to the corresponding Then, the samples were blocked in a blocking solution (PBS, 0.1% Tween-
healthy cell type to obtain the T1D model or T2D model effect per cell 20, 1% donkey serum and 5% FCS for 1 h at room temperature). Primary
type. The DEGs were selected based on FDR < 0.05, absolute logFC > 1 antibodies (Supplementary Table 13) were incubated for at least 4 h at
and relative expression in individual cell types >0.1 to focus on genes room temperature followed by three washes with PBX. The samples were
that are less likely to be ambiently expressed. Overlap between DEGs then incubated with secondary antibodies (Supplementary Table 13)
was computed accounting for DGE direction between the two groups. during 4–5 h of incubation. For the anti-Rbp4 antibody, we performed
Same direction DEGs across α-, δ- and γ-cells in both diabetes types antigen retrieval with a citric buffer (10 mM sodium citrate and 0.05%
were extracted and gene set enrichment was computed as for human Tween-20, pH 6) in addition to the above-described protocol. Finally,
T1D and T2D genes. the pancreatic sections were stained with 4,6-diamidino-2-phenylindole
(1:500 dilution in 1× PBS for 30 min). All images were obtained on a Leica
Sex differences in β-cells during aging microscope of the type DMI 6000. Images were analyzed using the LAS
Two datasets that contained a mixture of male and female cells were X v.3.5.6 and/or ImageJ Fiji-Win32 software.
used: P16 and aged. Each dataset was analyzed separately; both data-
sets had three samples per group with pooled animals within samples. Reporting summary
Cells from low-quality coarse β-cell clusters, genes expressed in less Further information on research design is available in the Nature Port-
than 5% of cells and non-β-cell ambient genes were removed. DGE folio Reporting Summary linked to this article.
analysis was performed with sex and samples as covariates using dif-
fxpy two-sided Wald test. We removed genes that could not be fitted, Data availability
as indicated by extremely small standard deviations of the regression Up-to-date data resource links are available from https://github.com/
coefficient (s.d. 2.2 × 10−162). DEGs were selected based on FDR < 0.05 theislab/mouse_cross-condition_pancreatic_islet_atlas. The two newly
and absolute logFC > 1. generated scRNA-seq datasets, the integrated atlas and the reference
DEGs between sexes in the aged dataset were separated by DGE mapped embedding of the Feng dataset were deposited to the GEO
direction and hierarchically clustered on the whole β-cell fine pseu- within super-series GSE211799. The atlas is also available as a cellxgene
dobulk data. Cutting thresholds were selected visually based on heat instance (https://cellxgene.cziscience.com/collections/296237e2-
map portraying gene expression across fine pseudobulks. All β-cells 393d-4e31-b590-b03f74ac5070). The scArches model for reference
were scored for DEG groups with the Scanpy score_genes function. mapping and an example code for reference mapping used for the
Feng dataset are available in https://github.com/theislab/mouse_
Laboratory validation of diabetes markers cross-condition_pancreatic_islet_atlas/tree/main/reference_map-
For diabetes markers validation we used healthy adult mice from ping. The following previously published datasets were included into
strains C57BL/6J (three males and three females, aged 2–4 months) the atlas: GSE132188, GSE161966, GSE128565, GSE174194, GSE144471,
and B6.BKS(D)-Leprdb/J (healthy db/db control), db/db T2D model GSE117770, GSE142465 (GSM4228185 to GSM4228199). The following
mice (three males aged 8 weeks) and NOD T1D model mice (three previously published datasets were used for validation: GSE83146,
females aged 8 weeks). For endocrine markers validation we used GSE137909, GSE148073, GSE81608, GSE198623, GSE81547, GSE86469,
postnatal healthy mice from strain C57BL/6J (two males and one female, GSE124742 (FACS), GSE124742 (patch-seq), GSE164875 (patch-seq),
at P9 stage). Mice were housed in groups of two to four animals and GSE101207, GSE154126 and GSE83139. Gene sets were obtained from
Nature Metabolism | Volume 5 | September 2023 | 1615–1637 1632

Article https://doi.org/10.1038/s42255-023-00876-x
MSigDB (v.7.4.1) and ortholog information was obtained from BioMart 20. Yzydorczyk, C., Mitanchez, D., Boubred, F. & Simeoni, U. in
(Ensembl Genes v.103). Glucose Intake and Utilization in Pre-Diabetes and Diabetes
(eds Watson, R. R. & Dokken, B. B.) 5–20 (Academic Press, 2015).
Code availability 21. Camunas-Soler, J. et al. Patch-seq links single-cell transcriptomes
All code is available at https://github.com/theislab/mouse_ to human islet dysfunction in diabetes. Cell Metab. 31, 1017–1031
cross-condition_pancreatic_islet_atlas. This includes both reproduc- (2020).
ibility code and an example of how new datasets can be mapped onto 22. Wang, Y. J. et al. Single-cell transcriptomics of the human
the atlas. endocrine pancreas. Diabetes 65, 3028–3038 (2016).
23. Oppenländer, L. et al. Vertical sleeve gastrectomy triggers
References fast β-cell recovery upon overt diabetes. Mol. Metab. 54,
1. Tritschler, S., Theis, F. J., Lickert, H. & Bottcher, A. Systematic 101330 (2021).
single-cell analysis provides new insights into heterogeneity and 24. Chan, J. Y., Luzuriaga, J., Bensellam, M., Biden, T. J. & Laybutt, D. R.
plasticity of the pancreas. Mol. Metab. 6, 974–990 (2017). Failure of the adaptive unfolded protein response in islets of obese
2. Bornstein, S. R., Ludwig, B. & Steenblock, C. Progress in islet mice is linked with abnormalities in β-cell gene expression and
transplantation is more important than ever. Nat. Rev. Endocrinol. progression to diabetes. Diabetes 62, 1557–1568 (2013).
18, 389–390 (2022). 25. In’t Veld, P. Insulitis in human type 1 diabetes: a comparison
3. Gentileschi, P., Bianciardi, E., Benavoli, D. & Campanelli, M. between patients and animal models. Semin. Immunopathol. 36,
Metabolic surgery for type II diabetes: an update. Acta Diabetol. 569–579 (2014).
58, 1153–1159 (2021). 26. Fasolino, M. et al. Single-cell multi-omics analysis of human
4. Jain, C., Ansarullah, Bilekova, S. & Lickert, H. Targeting pancreatic islets reveals novel cellular states in type 1 diabetes.
pancreatic β cells for diabetes treatment. Nat. Metab. 4, Nat. Metab. 4, 284–299 (2022).
1097–1108 (2022). 27. Thompson, P. J. et al. Targeted elimination of senescent β cells
5. Bakhti, M., Böttcher, A. & Lickert, H. Modelling the endocrine prevents type 1 diabetes. Cell Metab. 29, 1045–1060 (2019).
pancreas in health and disease. Nat. Rev. Endocrinol. 15, 155–171 28. Marquina-Sanchez, B. et al. Single-cell RNA-seq with spike-in cells
(2019). enables accurate quantification of cell-specific drug effects in
6. Miranda, M. A., Macias-Velasco, J. F. & Lawson, H. A. Pancreatic pancreatic islets. Genome Biol. 21, 106 (2020).
β-cell heterogeneity in health and diabetes: classes, sources, 29. Furman, B. L. Streptozotocin-induced diabetic models in mice
and subtypes. Am. J. Physiol. Endocrinol. Metab. 320, E716–E731 and rats. Curr. Protoc. 1, e78 (2021).
(2021). 30. Sachs, S. et al. Targeted pharmacological therapy restores
7. Benninger, R. K. P. & Kravets, V. The physiological role of β-cell β-cell function for diabetes remission. Nat. Metab. 2, 192–209
heterogeneity in pancreatic islet function. Nat. Rev. Endocrinol. (2020).
18, 9–22 (2022). 31. Feng, Y. et al. Characterizing pancreatic β-cell heterogeneity in
8. Liu, J. S. E. & Hebrok, M. All mixed up: defining roles for β-cell the streptozotocin model by single-cell transcriptomic analysis.
subtypes in mature islets. Genes Dev. 31, 228–240 (2017). Mol. Metab. 37, 100982 (2020).
9. Blum, B. et al. Functional β-cell maturation is marked by an 32. Wigger, L. et al. Multi-omics profiling of living human pancreatic
increased glucose threshold and by expression of urocortin 3. islet donors reveals heterogeneous β cell trajectories towards
Nat. Biotechnol. 30, 261–264 (2012). type 2 diabetes. Nat. Metab. 3, 1017–1031 (2021).
10. Nishimura, W., Takahashi, S. & Yasuda, K. MafA is critical for 33. Chen, C.-W. et al. Adaptation to chronic ER stress enforces
maintenance of the mature β cell phenotype in mice. Diabetologia pancreatic β-cell plasticity. Nat. Commun. 13, 4621 (2022).
58, 566–574 (2015). 34. Stožer, A. et al. From isles of Königsberg to islets of Langerhans:
11. Roscioni, S. S., Migliorini, A., Gegg, M. & Lickert, H. Impact of islet Examining the function of the endocrine pancreas through
architecture on β-cell heterogeneity, plasticity and function. Nat. network science. Front. Endocrinol. 13, 922640 (2022).
Rev. Endocrinol. 12, 695–709 (2016). 35. Mawla, A. M. & Huising, M. O. Navigating the depths and avoiding
12. Bader, E. et al. Identification of proliferative and mature the shallows of pancreatic islet cell transcriptomes. Diabetes 68,
β-cells in the islets of Langerhans. Nature 535, 430–434 1380–1393 (2019).
(2016). 36. Kaestner, K. H. et al. What is a β cell? – chapter I in the Human
13. Aguayo-Mazzucato, C. Functional changes in β cells during Islet Research Network (HIRN) review series. Mol. Metab. 53,
ageing and senescence. Diabetologia 63, 2022–2029 (2020). 101323 (2021).
14. Avrahami, D. et al. Aging-dependent demethylation of regulatory 37. Khin, P.-P., Lee, J.-H. & Jun, H.-S. A brief review of the mechanisms
elements correlates with chromatin state and improved β cell of β-cell dedifferentiation in type 2 diabetes. Nutrients 13,
function. Cell Metab. 22, 619–632 (2015). 1593 (2021).
15. Enge, M. et al. Single-cell analysis of human pancreas reveals 38. Halban, P. A. et al. β-cell failure in type 2 diabetes: postulated
transcriptional signatures of aging and somatic mutation mechanisms and prospects for prevention and treatment.
patterns. Cell 171, 321–330 (2017). Diabetes Care 37, 1751–1758 (2014).
16. Helman, A. et al. p16(Ink4a)-induced senescence of pancreatic β 39. Sahin, G. S., Lee, H. & Engin, F. An accomplice more than a
cells enhances insulin secretion. Nat. Med. 22, 412–420 (2016). mere victim: the impact of β-cell ER stress on type 1 diabetes
17. Shrestha, S. et al. Aging compromises human islet β cell function pathogenesis. Mol. Metab. 54, 101365 (2021).
and identity by decreasing transcription factor activity and 40. Lopez, R., Regier, J., Cole, M. B., Jordan, M. I. & Yosef, N. Deep
inducing ER stress. Sci. Adv. 8, eabo3932 (2022). generative modeling for single-cell transcriptomics. Nat. Methods
18. Yong, H. J., Toledo, M. P., Nowakowski, R. S. & Wang, Y. J. 15, 1053–1058 (2018).
Sex differences in the molecular programs of pancreatic 41. Luecken, M. D. et al. Benchmarking atlas-level data integration in
cells contribute to the differential risks of type 2 diabetes. single-cell genomics. Nat. Methods 19, 41–50 (2022).
Endocrinology https://doi.org/10.1210/endocr/bqac156 (2022). 42. Lotfollahi, M. et al. Mapping single-cell data to reference
19. Kleinert, M. et al. Animal models of obesity and diabetes mellitus. atlases by transfer learning. Nat. Biotechnol. 40, 121–130
Nat. Rev. Endocrinol. 14, 140–162 (2018). (2022).
Nature Metabolism | Volume 5 | September 2023 | 1615–1637 1633

Article https://doi.org/10.1038/s42255-023-00876-x
43. Butler, A., Hoffman, P., Smibert, P., Papalexi, E. & Satija, R. 66. Stone, V. M. et al. GPR120 (FFAR4) is preferentially expressed in
Integrating single-cell transcriptomic data across different pancreatic δ cells and regulates somatostatin secretion from
conditions, technologies, and species. Nat. Biotechnol. 36, murine islets of Langerhans. Diabetologia 57, 1182–1191 (2014).
411–420 (2018). 67. Rorsman, P. & Huising, M. O. The somatostatin-secreting
44. Aviv, R. et al. The human cell atlas. eLife https://doi.org/10.7554/ pancreatic δ-cell in health and disease. Nat. Rev. Endocrinol. 14,
elife.27041 (2017). 404–414 (2018).
45. Quake, S. R. A decade of molecular cell atlases. Trends Genet. 38, 68. Strowski, M. Z., Parmar, R. M., Blake, A. D. & Schaeffer, J. M.
805–810 (2022). Somatostatin inhibits insulin and glucagon secretion via two
46. Li, J. et al. Deep learning of cross-species single-cell landscapes receptors subtypes: an in vitro study of pancreatic islets from
identifies conserved regulatory programs underlying cell types. somatostatin receptor 2 knockout mice. Endocrinology 141,
Nat. Genet. 54, 1711–1720 (2022). 111–117 (2000).
47. Chen, K. et al. Single-cell RNA-seq transcriptomic landscape of 69. Omar-Hmeadi, M., Lund, P.-E., Gandasi, N. R., Tengholm, A. & Barg, S.
human and mouse islets and pathological alterations of diabetes. Paracrine control of α-cell glucagon exocytosis is compromised in
iScience 25, 105366 (2022). human type-2 diabetes. Nat. Commun. 11, 1896 (2020).
48. Sikkema, L. et al. An integrated cell atlas of the lung in health and 70. Nasteska, D. & Hodson, D. J. The role of β cell heterogeneity in islet
disease. Nat. Med. 29, 1563–1577 (2023). function and insulin release. J. Mol. Endocrinol. 61, R43–R60 (2018).
49. van Gurp, L. et al. Generation of human islet cell type-specific 71. Drigo, R. A. E. et al. Aging of human endocrine pancreatic cell
identity genesets. Nat. Commun. 13, 2020 (2022). types is heterogeneous and sex-specific. Preprint at bioRxiv
50. Lange, M. et al. CellRank for directed single-cell fate mapping. https://doi.org/10.1101/729541 (2019).
Nat. Methods 19, 159–170 (2022). 72. Chen, Y.-G., Mathews, C. E. & Driver, J. P. The role of NOD
51. Baron, M. et al. A single-cell transcriptomic map of the human Mice in type 1 diabetes research: lessons from the past and
and mouse pancreas reveals inter- and intra-cell population recommendations for the future. Front. Endocrinol. 9, 51 (2018).
structure. Cell Syst. https://doi.org/10.1016/j.cels.2016.08.011 73. Meyerovich, K., Ortis, F., Allagnat, F. & Cardozo, A. K. Endoplasmic
(2016). reticulum stress and the unfolded protein response in pancreatic
52. Xin, Y. et al. RNA sequencing of single human islet cells reveals islet inflammation. J. Mol. Endocrinol. 57, R1–R17 (2016).
type 2 diabetes genes. Cell Metab. 24, 608–615 (2016). 74. Coleman, D. L. Obese and diabetes: two mutant genes causing
53. Dziewulska, A., Dobosz, A. M. & Dobrzyn, A. High-throughput diabetes-obesity syndromes in mice. Diabetologia 14, 141–148
approaches onto uncover (epi)genomic architecture of type 2 (1978).
diabetes. Genes 9, 374 (2018). 75. Kobayashi, K. et al. The db/db mouse, a model for diabetic
54. Tarifeño-Saldivia, E. et al. Transcriptome analysis of pancreatic dyslipidemia: molecular characterization and effects of Western
cells across distant species highlights novel important regulator diet feeding. Metabolism 49, 22–31 (2000).
genes. BMC Biol. 15, 21 (2017). 76. Lenzen, S. The mechanisms of alloxan- and streptozotocin-
55. Su, Y. et al. Novel function of transthyretin in pancreatic α cells. induced diabetes. Diabetologia 51, 216–226 (2008).
FEBS Lett. 586, 4215–4222 (2012). 77. Eizirik, D. L., Pasquali, L. & Cnop, M. Pancreatic β-cells in type 1
56. DiGruccio, M. R. et al. Comprehensive α, β and δ cell and type 2 diabetes mellitus: different pathways to failure. Nat.
transcriptomes reveal that ghrelin selectively activates δ cells Rev. Endocrinol. 16, 349–362 (2020).
and promotes somatostatin release from pancreatic islets. 78. Fang, Z. et al. Single-cell heterogeneity analysis and CRISPR
Mol. Metab. 5, 449–458 (2016). screen identify key β-cell-specific disease genes. Cell Rep. 26,
57. Artner, I. et al. MafA and MafB regulate genes critical to β-cells in 3132–3144 (2019).
a unique temporal manner. Diabetes 59, 2530–2539 (2010). 79. Salinno, C. et al. CD81 marks immature and dedifferentiated
58. Huang, R., Bai, X., Li, X., Wang, X. & Zhao, L. Retinol-binding pancreatic β-cells. Mol. Metab. 49, 101188 (2021).
protein 4 activates STRA6, provoking pancreatic β-cell 80. Mizusawa, N. et al. Identification of protease serine S1 family
dysfunction in type 2 diabetes. Diabetes 70, 449–463 (2021). member 53 as a mitochondrial protein in murine islet β cells.
59. Zhang, J., McKenna, L. B., Bogue, C. W. & Kaestner, K. H. The Islets 14, 1–13 (2022).
diabetes gene Hhex maintains δ-cell differentiation and islet 81. Tritschler, S. et al. A transcriptional cross species map of
function. Genes Dev. 28, 829–834 (2014). pancreatic islet cells. Mol. Metab. https://doi.org/10.1016/
60. Bastidas-Ponce, A. et al. Comprehensive single cell j.molmet.2022.101595 (2022).
mRNA profiling reveals a detailed roadmap for pancreatic 82. Xin, Y. et al. Pseudotime ordering of single human β-cells reveals
endocrinogenesis. Development 146, dev173849 (2019). states of insulin production and unfolded protein response.
61. Bastidas-Ponce, A., Scheibner, K., Lickert, H. & Bakhti, M. Cellular Diabetes 67, 1783–1794 (2018).
and molecular mechanisms coordinating pancreas development. 83. Kiselev, V. Y., Andrews, T. S. & Hemberg, M. Challenges in
Development 144, 2873–2888 (2017). unsupervised clustering of single-cell RNA-seq data. Nat. Rev.
62. Johansson, K. A. et al. Temporal control of neurogenin3 activity Genet. 20, 273–282 (2019).
in pancreas progenitors reveals competence windows for 84. Brereton, M. F., Rohm, M. & Ashcroft, F. M. β-Cell dysfunction in
the generation of different endocrine cell types. Dev. Cell 12, diabetes: a crisis of identity? Diabetes Obes. Metab. https://doi.
457–465 (2007). org/10.1111/dom.12732 (2016).
63. Byrnes, L. E. et al. Lineage dynamics of murine pancreatic 85. Farack, L. et al. Transcriptional heterogeneity of β cells in the
development at single-cell resolution. Nat. Commun. 9, intact pancreas. Dev. Cell 48, 115–125 (2019).
3922 (2018). 86. Rui, J. et al. β Cells that resist immunological attack develop
64. Goudet, G., Delhalle, S., Biemar, F., Martial, J. A. & Peers, during progression of autoimmune diabetes in NOD mice. Cell
B. Functional and cooperative interactions between the Metab. 25, 727–738 (2017).
homeodomain PDX1, PBX, and Prep1 factors on the somatostatin 87. Kang, R. B. et al. Single-nucleus RNA sequencing of human
promoter*. J. Biol. Chem. 274, 4067–4073 (1999). pancreatic islets identifies novel gene sets and distinguishes
65. Gao, R., Yang, T. & Zhang, Q. δ-Cells: the neighborhood watch in β-cell subpopulations with dynamic transcriptome profiles.
the islet community. Biology 10, 74 (2021). Genome Med. 15, 30 (2023).
Nature Metabolism | Volume 5 | September 2023 | 1615–1637 1634

Article https://doi.org/10.1038/s42255-023-00876-x
88. Chu, C. M. J. et al. Dynamic Ins2 gene activity defines β-cell 112. Puri, S., Folias, A. E. & Hebrok, M. Plasticity and dedifferentiation
maturity states. Diabetes https://doi.org/10.2337/db21-1065 (2022). within the pancreas: development, homeostasis, and disease.
89. Tonne, J. M. et al. Global gene expression profiling of pancreatic Cell Stem Cell 16, 18–31 (2015).
islets in mice during streptozotocin-induced β-cell damage 113. Kim-Muller, J. Y. et al. Aldehyde dehydrogenase 1a3 defines
and pancreatic Glp-1 gene therapy. Dis. Model. Mech. 6, a subset of failing pancreatic β cells in diabetic mice. Nat.
1236–1245 (2013). Commun. 7, 12631 (2016).
90. Päth, G. et al. NUPR1 preserves insulin secretion of pancreatic 114. Cinti, F. et al. Evidence of β-cell dedifferentiation in human type 2
β-cells during inflammatory stress by multiple low-dose diabetes. J. Clin. Endocrinol. Metab. 101, 1044–1054 (2016).
streptozotocin and high-fat diet. Am. J. Physiol. Endocrinol. Metab. 115. Yang, Y. et al. Islet β-cell-produced NUCB2/nesfatin-1 maintains
319, E338–E344 (2020). insulin secretion and glycemia along with suppressing UCP-2 in
91. Puddu, A. et al. Update on the protective molecular pathways β-cells. J. Physiol. Sci. 69, 733–739 (2019).
improving pancreatic β-cell dysfunction. Mediators Inflamm. 116. Maejima, Y. et al. Nesfatin-1 inhibits voltage gated K+ channels in
2013, 750540 (2013). pancreatic beta cells. Peptides 95, 10–15 (2017).
92. Juliana, C. A. et al. ATF5 regulates β-cell survival during stress. 117. Li, X.-S., Yan, C.-Y., Fan, Y.-J., Yang, J.-L. & Zhao, S.-X. NUCB2
Proc. Natl Acad. Sci. USA 114, 1341–1346 (2017). polymorphisms are associated with an increased risk for type 2
93. Atkinson, M. A., Campbell-Thompson, M., Kusmartseva, I. & diabetes in the Chinese population. Ann. Transl. Med 8, 290 (2020).
Kaestner, K. H. Organisation of the human pancreas in health and 118. Lu, H., Yang, Y., Allister, E. M., Wijesekara, N. & Wheeler, M.
in diabetes. Diabetologia 63, 1966–1973 (2020). B. The identification of potential factors associated with the
94. Adams, M. T. & Blum, B. Determinants and dynamics of pancreatic development of type 2 diabetes: a quantitative proteomics
islet architecture. Islets 14, 82–100 (2022). approach. Mol. Cell. Proteom. 7, 1434–1451 (2008).
95. Carrano, A. C., Mulas, F., Zeng, C. & Sander, M. Interrogating islets 119. Hartley, T. et al. Endoplasmic reticulum stress response in
in health and disease with single-cell technologies. Mol. Metab. 6, an INS-1 pancreatic β-cell line with inducible expression of a
991–1001 (2017). folding-deficient proinsulin. BMC Cell Biol. 11, 59 (2010).
96. Noguchi, G. M. & Huising, M. O. Integrating the inputs that 120. Byun, H.-R., Choi, J. A. & Koh, J.-Y. The role of metallothionein-3 in
shape pancreatic islet hormone release. Nat. Metab. 1, streptozotocin-induced β-islet cell death and diabetes in mice.
1189–1201 (2019). Metallomics 6, 1748–1757 (2014).
97. Dai, X.-Q. et al. Heterogenous impairment of α cell function in 121. Viñuela, A. et al. Genetic variant effects on gene expression
type 2 diabetes is linked to cell maturation state. Cell Metab. 34, in human pancreatic islets and their implications for T2D. Nat.
256–268 (2022). Commun. 11, 4912 (2020).
98. Drigo, R. A. E. et al. Structural basis for δ cell paracrine regulation 122. Shrestha, N., De Franco, E., Arvan, P. & Cnop, M. Pathological
in pancreatic islets. Nat. Commun. 10, 3700 (2019). β-cell endoplasmic reticulum stress in type 2 diabetes: current
99. Rodnoi, P. et al. Neuropeptide Y expression marks partially evidence. Front. Endocrinol. 12, 650158 (2021).
differentiated β cells in mice and humans. JCI Insight 2, 123. Wang, S., Flibotte, S., Camunas-Soler, J., MacDonald, P. E. &
e94005 (2017). Johnson, J. D. A new hypothesis for type 1 diabetes risk: the
100. Jacovetti, C. & Regazzi, R. Mechanisms underlying the expansion at-risk allele at rs3842753 associates with increased β-cell INS
and functional maturation of β-cells in newborns: impact of the messenger RNA in a meta-analysis of single-cell RNA-sequencing
nutritional environment. Int. J. Mol. Sci. 23, 2096 (2022). data. Can. J. Diabetes https://doi.org/10.1016/j.jcjd.2021.03.007
101. Dalmas, E. Innate immune priming of insulin secretion. Curr. Opin. (2021).
Immunol. 56, 44–49 (2019). 124. Cefalu, W. T. et al. Heterogeneity of diabetes: β-cells, phenotypes,
102. Li, Y. et al. Revisiting the antigen-presenting function of β cells in and precision medicine: proceedings of an international
T1D pathogenesis. Front. Immunol. 12, 690783 (2021). symposium of the Canadian Institutes of Health Research’s
103. Aguayo-Mazzucato, C. et al. Acceleration of β cell aging Institute of Nutrition, Metabolism and Diabetes and the US
determines diabetes and senolysis improves disease outcomes. National Institutes of Health’s National Institute of Diabetes and
Cell Metab. 30, 129–142 (2019). Digestive and Kidney Diseases. Diabetes Care https://doi.org/
104. Kokkinopoulou, I., Diakoumi, A. & Moutsatsou, P. Glucocorticoid 10.2337/dci21-0051 (2022).
receptor signaling in diabetes. Int. J. Mol. Sci. 22, 11173 (2021). 125. Gurzov, E. N., Ortis, F., Bakiri, L., Wagner, E. F. & Eizirik, D. L. JunB
105. Stephens, S. B. et al. A VGF-derived peptide attenuates inhibits ER stress and apoptosis in pancreatic β cells. PLoS ONE 3,
development of type 2 diabetes via enhancement of islet β-cell e3030 (2008).
survival and function. Cell Metab. 16, 33–43 (2012). 126. Gannon, M., Kulkarni, R. N., Tse, H. M. & Mauvais-Jarvis, F.
106. Gurgul-Convey, E. Sphingolipids in type 1 diabetes: focus on Sex differences underlying pancreatic islet biology and its
β-cells. Cells 9, 1835 (2020). dysfunction. Mol. Metab. 15, 82–91 (2018).
107. Furuhashi, M. et al. Independent and distinct associations of 127. Brownrigg, G. P. et al. Sex differences in islet stress responses
FABP4 and FABP5 with metabolic parameters in type 2 diabetes support female β cell resilience. Mol. Metab. 9, 101678 (2023).
mellitus. Front. Endocrinol. 11, 575557 (2020). 128. Liu, G. et al. Single-cell RNA sequencing reveals sexually
108. Martens, G. A. et al. Clusters of conserved β cell marker genes for dimorphic transcriptome and type 2 diabetes genes in mouse
assessment of β cell phenotype. PLoS ONE 6, e24134 (2011). islet β cells. Genom. Proteom. Bioinform. 19, 408–422 (2021).
109. Van de Velde, S. et al. CREB promotes β cell gene expression by 129. Makino, S. et al. Breeding of a non-obese, diabetic strain of mice.
targeting its coactivators to tissue-specific enhancers. Mol. Cell. Jikken Dobutsu 29, 1–13 (1980).
Biol. 39, e00200-19 (2019). 130. Tramunt, B. et al. Sex differences in metabolic regulation and
110. Leu, S.-Y. et al. Loss of EGR-1 uncouples compensatory responses diabetes susceptibility. Diabetologia 63, 453–461 (2020).
of pancreatic β cells. Theranostics 10, 4233–4249 (2020). 131. Viloria, K. et al. Vitamin-d-binding protein contributes to the
111. Hong, K., Xu, G., Grayson, T. B. & Shalev, A. Cytokines maintenance of α cell function and glucagon secretion. Cell Rep.
regulate β-cell thioredoxin-interacting protein (TXNIP) via 31, 107761 (2020).
distinct mechanisms and pathways. J. Biol. Chem. 291, 132. Cabrera, O. et al. Glutamate is a positive autocrine signal for
8428–8439 (2016). glucagon release. Cell Metab. 7, 545–554 (2008).
Nature Metabolism | Volume 5 | September 2023 | 1615–1637 1635

Article https://doi.org/10.1038/s42255-023-00876-x
133. Szabat, M. et al. Kinetics and genomic profiling of adult human 157. Luecken, M. D. & Theis, F. J. Current best practices in single-cell
and mouse β-cell maturation. Islets 3, 175–187 (2011). RNA-seq analysis: a tutorial. Mol. Syst. Biol. 15, e8746 (2019).
134. Layden, B. T. et al. Regulation of pancreatic islet gene expression 158. Wolock, S. L., Lopez, R. & Klein, A. M. Scrublet: computational
in mouse islets by pregnancy. J. Endocrinol. 207, 265–279 (2010). identification of cell doublets in single-cell transcriptomic data.
135. Bearrows, S. C. et al. Chromogranin B regulates early-stage insulin Cell Syst. 8, 281–291 (2019).
granule trafficking from the Golgi in pancreatic islet β-cells. J. Cell 159. Lun, A. T. L., McCarthy, D. J. & Marioni, J. C. A step-by-step
Sci. 132, jcs231373 (2019). workflow for low-level analysis of single-cell RNA-seq data
136. Sidarala, V. & Kowluru, A. The regulatory roles of with Bioconductor. F1000Research https://doi.org/10.12688/
mitogen-activated protein kinase (MAPK) pathways in health and f1000research.9501.2 (2016).
diabetes: lessons learned from the pancreatic β-cell. Recent Pat. 160. Lun, A. T. L., Bach, K. & Marioni, J. C. Pooling across cells to
Endocr. Metab. Immune Drug Discov. 10, 76–84 (2017). normalize single-cell RNA sequencing data with many zero
137. Chang, C., Worley, B. L., Phaëton, R. & Hempel, N. Extracellular counts. Genome Biol. 17, 75 (2016).
glutathione peroxidase GPx3 and its role in cancer. Cancers 12, 161. Scialdone, A. et al. Computational assignment of cell-cycle stage
2197 (2020). from single-cell transcriptome data. Methods 85, 54–61 (2015).
138. Lebrun, P. et al. The suppressor of cytokine signalling 2 162. Fleming, S. J. et al. Unsupervised removal of systematic
(SOCS2) is a key repressor of insulin secretion. Diabetologia 53, background noise from droplet-based single-cell experiments
1935–1946 (2010). using CellBender. Nat. Methods https://doi.org/10.1038/s41592-
139. Zhang, Y. et al. Glucose potentiates β‐cell function by inducing 023-01943-7 (2023).
Tphl expression in rat islets. FASEB J. 31, 5342–5355 (2017). 163. Young, M. D. & Behjati, S. SoupX removes ambient RNA
140. Bertolino, P. et al. Activin B receptor ALK7 is a negative regulator contamination from droplet-based single-cell RNA sequencing
of pancreatic β-cell function. Proc. Natl Acad. Sci. 105, 7246–7251 data. Gigascience 9, giaa151 (2020).
(2008). 164. Yang, S. et al. Decontamination of ambient RNA in single-cell
141. Berger, C. & Zdzieblo, D. Glucose transporters in pancreatic islets. RNA-seq with DecontX. Genome Biol. 21, 57 (2020).
Pflug. Arch. 472, 1249–1272 (2020). 165. Traag, V. A., Waltman, L. & van Eck, N. J. From Louvain to Leiden:
142. Bunik, V. I. & Degtyarev, D. Structure-function relationships guaranteeing well-connected communities. Sci. Rep. 9, 5233 (2019).
in the 2-oxo acid dehydrogenase family: substrate-specific 166. Baran, Y. et al. MetaCell: analysis of single-cell RNA-seq data
signatures and functional predictions for the 2-oxoglutarate using K-nn graph partitions. Genome Biol. 20, 206 (2019).
dehydrogenase-like proteins. Proteins 71, 874–890 (2008). 167. Persad, S. et al. SSEACells infers transcriptional and epigenomic
143. Megill, C. et al. cellxgene: a performant, scalable exploration cellular states from single-cell genomics data. Nat. Biotechnol.
platform for high dimensional sparse matrices. Preprint at bioRxiv https://doi.org/10.1038/s41587-023-01716-9 (2023).
https://doi.org/10.1101/2021.04.05.438318 (2021). 168. Squair, J. W. et al. Confronting false discoveries in single-cell
144. Tiriveedhi, V. Impact of precision medicine on drug repositioning differential expression. Nat. Commun. 12, 5692 (2021).
and pricing: a too small to thrive crisis. J. Pers. Med. 8, 36 (2018). 169. Robinson, M. D., McCarthy, D. J. & Smyth, G. K. edgeR: a
145. Linsley, P. S., Greenbaum, C. J. & Nepom, G. T. Uncovering Bioconductor package for differential expression analysis of
pathways to personalized therapies in type 1 diabetes. Diabetes digital gene expression data. Bioinformatics 26, 139–140 (2010).
70, 831–841 (2021). 170. Federico, A. & Monti, S. hypeR: an R package for geneset
146. Unnikrishnan, R., Radha, V. & Mohan, V. Challenges Involved in enrichment workflows. Bioinformatics 36, 1307–1308 (2020).
incorporating personalised treatment plan as routine care of 171. Jupp, S., Burdett, T., Leroy, C. & Parkinson, H. E. A new ontology
patients with diabetes. Pharmgenom. Pers. Med. 14, 327–333 (2021). lookup service at EMBL-EBI. SWAT4LS 2, 118–119 (2015).
147. Fischer, D. S. et al. Sfaira accelerates data and model reuse in 172. Gu, Z., Eils, R. & Schlesner, M. Complex heatmaps reveal
single cell genomics. Genome Biol. https://doi.org/10.1186/ patterns and correlations in multidimensional genomic data.
s13059-021-02452-6 (2021). Bioinformatics 32, 2847–2849 (2016).
148. Li, D.-S., Yuan, Y.-H., Tu, H.-J., Liang, Q.-L. & Dai, L.-J. A protocol 173. Gu, Z. Complex heatmap visualization. iMeta https://doi.org/
for islet isolation from mouse pancreas. Nat. Protoc. 4, 1649–1652 10.1002/imt2.43 (2022).
(2009). 174. Burkhardt, D. B. et al. Quantifying the effect of experimental
149. Corbin, K. L. et al. A practical guide to rodent islet isolation and perturbations at single-cell resolution. Nat. Biotechnol. 39,
assessment revisited. Biol. Proced. Online 23, 7 (2021). 619–629 (2021).
150. Lange, A. et al. Fltp(T2AiCre): a new knock-in mouse line for 175. Fischer, D. diffxpy. https://diffxpy.readthedocs.io/en/latest/index.
conditional gene targeting in distinct mono- and multiciliated html (2020).
tissues. Differentiation 83, S105–S113 (2012). 176. Lee, H. et al. β Cell dedifferentiation induced by IRE1α deletion
151. Gegg, M. et al. Flattop regulates basal body docking and prevents type 1 diabetes. Cell Metab. 31, 822–836 (2020).
positioning in mono- and multiciliated cells. eLife https://doi.org/ 177. Xin, Y. et al. Single-cell RNAseq reveals that pancreatic
10.7554/elife.03842 (2014). β-cells from very old male mice have a young gene signature.
152. Wang, X., He, Y., Zhang, Q., Ren, X. & Zhang, Z. Direct comparative Endocrinology 157, 3431–3438 (2016).
analyses of 10x genomics chromium and Smart-seq2. Genom. 178. Lawlor, N. et al. Single-cell transcriptomes identify human islet
Proteom. Bioinform. 19, 253–266 (2021). cell signatures and reveal cell-type-specific expression changes
153. Wolf, F. A., Angerer, P. & Theis, F. J. SCANPY: large-scale single-cell in type 2 diabetes. Genome Res. 27, 208–222 (2017).
gene expression data analysis. Genome Biol. 19, 15 (2018). 179. Avrahami, D. et al. Single-cell transcriptomics of human islet
154. Kinsella, R. J. et al. Ensembl BioMarts: a hub for data retrieval ontogeny defines the molecular basis of β-cell dedifferentiation in
across taxonomic space. Database 2011, bar030 (2011). T2D. Mol. Metab. 42, 101057 (2020).
155. Zheng, G. X. Y. et al. Massively parallel digital transcriptional
profiling of single cells. Nat. Commun. 8, 14049 (2017). Acknowledgements
156. Lun, A. T. L. et al. EmptyDrops: distinguishing cells from empty We thank T. Walzthöni and X. Pastor Hostench for bioinformatics
droplets in droplet-based single-cell RNA sequencing data. support in the processing of raw scRNA-seq data provided at the
Genome Biol. 20, 63 (2019). Core Facility Genomics, Helmholtz Zentrum Munich, Neuherberg,
Nature Metabolism | Volume 5 | September 2023 | 1615–1637 1636

Article https://doi.org/10.1038/s42255-023-00876-x
Germany. We are grateful to the members of Theis and Lickert Additional information
laboratories and scientific support staff who provided manuscript Extended data is available for this paper at
feedback, especially A. Frishberg and N. Hennersdorf. This work https://doi.org/10.1038/s42255-023-00876-x.
was supported by funds from the Helmholtz Association, Helmholtz
Munich, the German Center for Diabetes Research and DZGIF (DZG Supplementary information The online version contains supplementary
Innovation Fund) topic ‘Gene and Cell Therapy’. L.Z. acknowledges material available at https://doi.org/10.1038/s42255-023-00876-x.
support by Bavarian Ministry of Science and the Arts in the framework
of the Bavarian Research Association ‘ForInter’ (Interaction of human Correspondence and requests for materials should be addressed to
brain cells). F.J.T. and H.L. acknowledge support by the European Heiko Lickert or Fabian J. Theis.
Union (ERC, DeepCell—101054957, BetaRegeneration—101054564).
Views and opinions expressed are those of the author(s) only and do Peer review information Nature Metabolism thanks Joan
not necessarily reflect those of the European Union or the European Camunas-Soler and the other, anonymous, reviewer(s) for their
Research Council. Neither the European Union nor the granting contribution to the peer review of this work. Primary Handling Editor:
authority can be held responsible for them. K.H. acknowledges Christoph Schmitt, in collaboration with the Nature Metabolism team.
financial support from Joachim Herz Stiftung via Add-on Fellowships
for Interdisciplinary Life Science and support from Helmholtz Reprints and permissions information is available at
Association under the joint research school ‘Munich School for www.nature.com/reprints.
Data Science’.
Publisher’s note Springer Nature remains neutral with regard to
Author contributions jurisdictional claims in published maps and institutional affiliations.
Project conceptualization was performed by K.H., F.J.T., H.L.,
M. Büttner, A.B.-P. and M. Bakhti. Data curation and computational Open Access This article is licensed under a Creative Commons
analyses were performed by K.H. Laboratory analyses were performed Attribution 4.0 International License, which permits use, sharing,
by A.B.-P., C.S., M.S., A.B. and A.M. Visualizations were prepared by adaptation, distribution and reproduction in any medium or format,
K.H., the original draft was written by K.H. with the help of A.B.-P. and as long as you give appropriate credit to the original author(s) and the
M. Bakhti and all authors reviewed the manuscript. Supervision was source, provide a link to the Creative Commons license, and indicate
provided by L.Z., M. Büttner, M. Bakhti, H.L. and F.J.T. if changes were made. The images or other third party material in this
article are included in the article’s Creative Commons license, unless
Funding indicated otherwise in a credit line to the material. If material is not
Open access funding provided by Helmholtz Zentrum München - included in the article’s Creative Commons license and your intended
Deutsches Forschungszentrum für Gesundheit und Umwelt (GmbH). use is not permitted by statutory regulation or exceeds the permitted
use, you will need to obtain permission directly from the copyright
Competing interests holder. To view a copy of this license, visit http://creativecommons.
F.J.T. consults for Immunai Inc., Singularity Bio B.V., CytoReason Ltd org/licenses/by/4.0/.
and Cellarity; and has an ownership interest in Dermagnostix GmbH
and Cellarity. The remaining authors declare no competing interests. © The Author(s) 2023
Nature Metabolism | Volume 5 | September 2023 | 1615–1637 1637

Article https://doi.org/10.1038/s42255-023-00876-x
Extended Data Fig. 1 | See next page for caption.
Nature Metabolism

Article https://doi.org/10.1038/s42255-023-00876-x
Extended Data Fig. 1 | Comparison of cell types assigned in original studies missing annotation are marked with NA. (d) Comparison of integration-based
and in integrated atlas re-annotation. (a) Atlas-level cell type re-annotation re-annotated and previously reported cell type labels. Datasets that did not have
within the atlas shown on UMAP, including low-quality and potential doublet previously reported annotation are not shown. Overlaps were normalized per
cells. (b) Cell types used for integration evaluation. Annotation was performed previously reported cell type. In the P16 dataset, the dotted rectangle indicates
for selected samples (colored in cells) per study; unannotated cells are marked rare Schwann cells that were merged with a larger population of stellate cells in
with NA. Some cell types were later renamed for the final atlas annotation the original annotation. In the embryonic dataset, the dotted circle indicates the
(for example, the annotations in panel b contain the name pericyte which was mapping of embryonic δ-cells to the postnatal δ-cells cluster. Abbreviations: ‘+’ -
later in panel a corrected to stellate activated). (c) Cell types as reported in the potential doublet, lowQ - low-quality, EP - endocrine progenitor/precursor, prlf.
original publications. Cell type names were unified across studies and cells with - proliferative, mat. - mature.
Nature Metabolism

Article https://doi.org/10.1038/s42255-023-00876-x
Extended Data Fig. 2 | Number of cells per cell type in each sample. Sample names are given as study_sampleDescription_sampleIdentifier. Some of the datasets
contained samples enriched for endocrine cells (Supplementary Table 1), which prevents direct cell type proportion comparison between samples with different cell
sorting.
Nature Metabolism

Article https://doi.org/10.1038/s42255-023-00876-x
Extended Data Fig. 3 | See next page for caption.
Nature Metabolism

Article https://doi.org/10.1038/s42255-023-00876-x
Extended Data Fig. 3 | Endocrine markers differ in embryonic and postnatal The first subplot in the row for either Ttr or Rbp4 experiment shows a zoomed-
datasets. (a) Comparison of endocrine markers in embryonic and postnatal data, out section, with the square denoting the zoomed-in region that is shown on
showing whether genes were selected as potential markers in each stage (color). the rest of the subplots, with an overlay of channels in the middle and individual
Genes missing from a stage-specific DGE analysis were assigned a logFC of 0. channels on the right. Scale bars represent 50 μM for zoomed-out images and
(b) Expression of Cer1 across embryonic cell types (original study annotation) 20 μM for zoomed-in images. The images are representative examples from the
and postnatal cell types (atlas-level re-annotation). (c) Validation of selected analysis of three independent animals. (d) Number of cells in each endocrine cell
endocrine markers with immunohistochemistry. Arrows indicate Ttr and Gcg group. Cell groups are as in Fig. 3. (e) Expression of embryonic Fev+ EP markers
double-positive α-cells (left) and Rbp4 and Sst double-positive δ-cells (right). from Bastidas-Ponce et al. (2019) across endocrine cell groups.
Nature Metabolism

Article https://doi.org/10.1038/s42255-023-00876-x
Extended Data Fig. 4 | Integrated embedding of β-cells from individual samples corresponds to biological conditions. The distribution density of cells from each
sample on a UMAP of the β-cell atlas subset. Sample names are reported with the sample description and identifier. The embryo dataset is not shown due to a small
number of cells within the β-cell cluster.
Nature Metabolism

Article https://doi.org/10.1038/s42255-023-00876-x
Extended Data Fig. 5 | See next page for caption.
Nature Metabolism

Article https://doi.org/10.1038/s42255-023-00876-x
Extended Data Fig. 5 | Different resolution β-cell states correspond state annotation given as a normalized distribution of each fine state across
to biological conditions. (a) Coarse β-cell states, including low-quality coarse states. (f) A UMAP embedding of male and female β-cells across ages.
clusters. (b) Fine β-cell states, including low-quality clusters. (c) and (d) Colored in are cells from datasets that have mixed sexes within samples, other
Coarse and fine, respectively, β-cell state proportions in each sample, also β-cells are displayed as a background. (g) Expression of Cfap126 (Flattop gene)
displaying corresponding sample metadata. Sample names are given as study_ across cell populations that were sorted based on the Flattop reporter system.
sampleDescription_sampleIdentifier. (e) Comparison of coarse and fine β-cell Abbreviations: hMT - high mitochondrial transcript read fraction.
Nature Metabolism

Article https://doi.org/10.1038/s42255-023-00876-x
Extended Data Fig. 6 | MIA-based β-cell markers are robust across mouse The ideal marker bar represents how we would expect markers of specific clusters
datasets, but do not directly translate to humans. (a) Expression of proposed to be expressed across the cell groups. (e) and (f) Translation of known and MIA-
β-cell state markers across coarse β-cell states per dataset (in brackets). based, respectively, β-cell state markers to human datasets. In each dataset (dot)
(b) Number of cluster-specific markers extracted per dataset and state or as the we compared marker expression within the relevant sample group to all other
intersection of all datasets within a state. (c) and (d) Expression of known and samples, showing a comparison lFC and statistical significance as well as the ratio
MIA-based, respectively, β-cell state markers on the external Feng mouse dataset. of cells expressing the gene in the target group. Abbreviations: ins - insulin.
Nature Metabolism

Article https://doi.org/10.1038/s42255-023-00876-x
Extended Data Fig. 7 | Reference mapping and cell state transfer for external proliferative (part of the ‘endocrine proliferative’ atlas cluster) and embryonic
mouse dataset β-cells reveals expected reference and query sample β-cells (as annotated in the original study of the embryonic dataset). (b) Label
relationships. (a) Joint embedding of the atlas (reference) and the external transfer from the atlas to query, using cell groups as described in a. Cells with low
mouse dataset (query). Left: All query samples, named as age, treatment and label-transfer probability were assigned to the uncertain group. Shown are the
replicate when multiple samples with the same age and treatment were present. ratios of each query sample predicted as a certain cell group.
Right: Reference cell groups showing coarse β-cell states, as shown in Fig. 5a, and
Nature Metabolism

Article https://doi.org/10.1038/s42255-023-00876-x
Extended Data Fig. 8 | Activity of GPs across β-cells helps in β-cells state for individual datasets. (f) Ratio of variance explained by GPs across datasets
interpretation. (a) Activity of GPs on UMAP of the β-cell atlas subset. (b) Activity compared to random groups of genes. (g) Relative variance explained by each GP,
of GPs across fine β-cell states normalized per GP across states. (c), (d), (e) scaled as a ratio of maximal absolute value per dataset.
Differences in GP activity between pairs of fine β-cell states (specified on y axis)
Nature Metabolism

Article https://doi.org/10.1038/s42255-023-00876-x
Extended Data Fig. 9 | Healthy β-cells contain five distinct variable gene density functions. (d) Localization of cells with the highest activity of the five
groups. (a) Pairwise comparison of the normalized activity of gene groups on gene groups on the atlas β-cell UMAP for individual health adult atlas samples
β-cells from healthy samples shown as kernel-estimated density plots colored (named as: dataset sample_metadata sample_name) and the healthy adult
by study. Lines represent regions containing 5, 34, 67, 95 and 99% of cells. Axes samples from the external dataset (Feng, GSE137909) mapped on top of the atlas.
represent the activity of the compared gene groups. (b) Mean gene group (e) Localization of virgin and non-virgin β-cells from Feng (GSE137909) dataset
activity within coarse β-cell clusters, normalized across clusters. (c) Per-sample on the integrated atlas UMAP as annotated in the original publication.
distribution of normalized gene group activities in β-cells shown as cumulative
Nature Metabolism

Article https://doi.org/10.1038/s42255-023-00876-x
Extended Data Fig. 10 | See next page for caption.
Nature Metabolism

Article https://doi.org/10.1038/s42255-023-00876-x
Extended Data Fig. 10 | Diabetes-related molecular changes of β-cells show STZ-treated) and healthy samples. Plot titles contain information on species
similarities and differences across dysfunctional states and translate to an (hs - human, mm - mouse), dataset and number of cells in healthy (H) and diabetic
external mouse dataset. (a) Design of DGE analysis showing original conditions (D) groups. Encircled are gene groups that translate to the external mouse
in each used dataset (dataset 8-16wNOD for NOD DGE, datasets db/db and mSTZ dataset. (c) Expression of genes upregulated in diabetic NOD or db/db+mSTZ
for db/db+mSTZ DGE) and axis used for fitting the DGE model. For NOD we cells shown across fine β-cell states and embryonic cell types as annotated in the
also show expression of a known T1D marker B2m. (b) Translation of diabetes original study. Cell color annotations are based on healthy and developmental
model DEG groups (T1D NOD, T2D db/db+mSTZ) to external human and mouse conditions. (d) Overlap between NOD and db/db+mSTZ DEG groups as a ratio of
datasets, indicated as normalized activity of gene groups in T1D or T2D (in mice the smaller group.
Nature Metabolism