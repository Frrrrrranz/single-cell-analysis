nature genetics
Article https://doi.org/10.1038/s41588-022-01243-4
A spatially resolved atlas of the human
lung characterizes a gland-associated
immune niche
In the format provided by the
authors and unedited

Supplementary legends
Supplementary Table 1: Donor metadata. Information on age range, sex, BMI range, smoking status,
years smoking and ethnic origin of donors.
Supplementary Table 2: Sample information for single cell and single-nuclei RNA-seq runs.
Sample ID-s for scRNAseq and corresponding location, spatial code, material of cells/nuclei, protocol,
enrichment and dissociation notes, Donor ID-s with age, BMI, sex and smoking history if available, 10x
version, Gene expression sequencing run ID and corresponding BCR and TCR sample ID-s for single
cell RNA-seq samples. For snRNAseq, sample ID-s and corresponding information for snRNAseq runs
regarding pooling, donors, location, protocol and 10x version.
Supplementary Table 3: Sample information for Visium Spatial Transcriptomic sequencing runs. Sample
and image ID-s, location and donor information, permeabilisation time and Visium slide ID for Visium
spatial transcriptomics samples.
Supplementary Table 4: Cell type annotation comparisons.
Comparison of the finest level of annotations in the current study with the finest level of annotations from
the Integrated HLCA12, the previous most recent healthy lung cell atlas6 , the LungMAP integrated atlas13
and the corresponding ‘CellCards’ from the LungMAP literature review13.
Supplementary Table 5: Manual annotation of micro-anatomical tissue environments on Visium spatial
transcriptomics. Manual annotation indicates presence (y) of various tissue regions on every Visium
spatial transcriptomics sample. The annotations on the tissue can be seen as categories on the
accompanying loupe files stored in DCP and in the online portal.
Supplementary Table 6: Antibody information for IBEX and IHC staining. Staining cycle, antibody
protein names, clone, conjugate, Vendor, catalogue number and dilution used.
Supplementary Table 7: Proportions and numbers of cells from scRNA-seq and snRNA-seq data by
Location, Material and Donor. Cell type groups “Celltypes master high” as shown in Figure 1e.
Supplementary Table 8: Output of fGWAS analysis for Lung function (FEV1/FVC) study (Figure 2f).
Shown are the Log odds ratio (log OR), upper and lower confidence intervals (CI), p-value and FDR for
each cell type. LogORs have been directly obtained as the beta values from fGWAS analysis. p-values
were calculated using a two-sided Wald test on the coefficients, testing difference from 0.
Benjamini-Hochberg multiple testing correction was performed over the 76 cell types.
Supplementary Table 9: Overview of donor inclusion across study. Use of donor material for a particular
experiment (scRNAseq, snRNAseq, scVDJ-seq, fresh Visium, FFPE Visium, specific RNAscope/IHC
validation experiments).
Supplementary Table 10: Significantly upregulated genes from comparison of peribronchial fibroblasts
in COPD patients and controls from Adams et al. 2020 Sci Adv. scRNAseq. All 112 upregulated genes
are displayed, with a subset of these which are relevant for COPD highlighted in Extended data 4c.

Supplementary Figure 1: Overview of Spatial Transcriptomics slides used in the study. H&E staining as
well as the number of UMI counts per spot are visualised for each section. Full details for each sample is
in Supplementary Table 3. Scale bar: 2mm.
Supplementary Figure 2: Donors’ contribution to cell types. All identified cell types are seen across
multiple donors (at least 5) and shown graphically by proportions of cell types identified per donor in (a)
epithelial cells, (b) stroma and (c) immune cells. The effect of each donor contributing to the cell type
proportion was calculated using cell type proportion analysis with a Poisson linear mixed model
accounting for location, donor, sequencing material and dissociation protocol (d-f). The effect of donor as
fold change and Local True Sign Rate (LTSR) score are shown for master cell types as additional data to
Figure 1 (d), Fibroblasts as additional data to Figure 2 (e) and vasculature & SM as additional data to
Figure 3 (e). Cell type numbers shown in Supplementary Table 7 and in online portal.
Supplementary Figure 3: Gene expression changes from veins to arteries for pulmonary and systemic
circulation vascular endothelial and perivascular cell types. Visualisation of marker genes for cell types in
these tissue microenvironments along this gradient: (a) pulmonary endothelial axis: arterial to CapA to
venous cell types, (b) systemic endothelial axis: arterial to capillary to venous, (c) systemic smooth
muscle: smooth muscle to pericyte to IR-Ven-Peri, (d) pulmonary smooth muscle: smooth muscle (SM) to
pericyte.
Supplementary Figure 4: Unsupervised cell type co-localisation analysis on spatial transcriptomics
data. Cell2location non-negative factorisation (NMF) analysis was used to map cell types on tissue
sections and compared to the manual annotation. Cell abundance (manual annotations) and proportion
per factor (factor analysis) is shown in the dotplots by color and dot size. Cell type enrichment in the (a)
manually annotated regions of frozen Visium, and in the regions obtained by the clustering of spots into 8
(b), 11 (c) and 21 (d) unsupervised regions (factors). Different microenvironments are highlighted with
boxes of different colours. The consistencies between manual annotation and NMF microenvironments
are highlighted by solid lines. Additional microenvironments revealed by NMF analysis is shown with
dotted and dashed lines. (e) Mapping of epithelial factors from b (cyan and orange, factors 0, 1, 2, 7 and
9 in b) on a representative bronchi section with corresponding H&E. Scale shows mean UMI for each
factor in each Visium voxel. Scale bar: 1mm. Donors used for replicas are shown in Supplementary Table
9.
Supplementary Note 1. Cell type marker genes for all the described cell types.

Supplementary Figure 1
H&E, number of total UMI for all Visium spatial transcriptomics sections
Trachea
| WSA_LngSP10972075 (FFPE) | WSA_LngSP10972074 (FFPE) |     |
| ------------------------ | ------------------------ | --- |
WSA_LngSP8759310
Bronchi
WSA_LngSP9258468
| WSA_LngSP10193348 | WSA_LngSP8759312 |                  |
| ----------------- | ---------------- | ---------------- |
| WSA_LngSP8759313  | WSA_LngSP8759311 | WSA_LngSP9258464 |
| WSA_LngSP9258467  | WSA_LngSP9258463 |                  |
Parenchyma
WSA_LngSP10972072 (FFPE)
|     | WSA_LngSP10972073 (FFPE) | WSA_LngSP9258462 |
| --- | ------------------------ | ---------------- |
WSA_LngSP9258469
| WSA_LngSP9258466 | WSA_LngSP9258465 |     |
| ---------------- | ---------------- | --- |
WSA_LngSP10193347
| WSA_LngSP10193345 | WSA_LngSP10193346 |     |
| ----------------- | ----------------- | --- |

Supplementary Figure 2
b
| a                                                                  |                                                                               | Stroma                                                                                                        |                                                                                                              |                                                                            |                                                          |                                                                            | Immune                                                      |                                                                                                        |                                                                                      |                                  |
| ------------------------------------------------------------------ | ----------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------------------------- | ----------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | -------------------------------- |
|                                                                    |                                                                               |                                                                                                               |                                                                                                              |                                                                            | yromem_B evian_B AgI_amsalp_B GgI_amsalp_B tsalbamsalp_B | rotceffE/ME_4DC MRT_4DC MC/evian_4DC ME_8DC ARME/ME_8DC ME/MRT_8DC MRT_8DC | 1_CD 2_CD detavitca_CD diotycamsalp_CD CLI TIAM 1TIHC_orcaM | laititsretnI_orcaM 1RC3XC_WA_orcaM TM_vla_orcaM vla_orcaM gnidivid_orcaM ralucsavartni_orcaM LCC_orcaM | llec_tsaM etycoyrakageM etaidemretni_orcaM 41DC_etyconoM 61DC_etyconoM ih61DC_KN TKN | d11DC_KN thgirb65DC_KN ger_T Tdg |
| etycordnohC citahpmyL_ailehtodnE a-paC_ailehtodnE g-paC_ailehtodnE | mluP_trA_VE tsyS_trA_VE mluP_neV_VE tsyS_neV_VE etycorhtyrE laititnevda_orbiF | raloevla_orbiF gnitiurcer_enummi_orbiF tsalborbifoym_orbiF laihcnorbirep_orbiF lairdnohcirep_orbiF ailehtoseM | MSA_elcsuM tsyS_ireP_elcsuM mluP_ireP_elcsuM gnitiurcer_enummi_ireP_elcsuM MS_mluP_elcsuM tsys_trA_MS_elcsuM | lairuenodne_FAN lairuenirep_FAN gnitanileym_nnawhcS gnitanileymnon_nnawhcS |                                                          |                                                                            |                                                             |                                                                                                        |                                                                                      |                                  |
Epithelia
| c   |     |     |     |     | d   |     | Master cell types |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | --- | --- |
Donor
Muscle
A26
Fibroblast
|     |     |     |     | A32 |     |     | LE  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
VE
|     |     |     |     | A37 |     |     | AT1 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
AT2
A40
Erythrocyte
|     |     |     |     | A41 |     |     | Myeloid |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- |
T & NK
|     |     |     |     | A42 |     | Mast cell |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- |
B cell
A43
B plasma
A44
Ciliated
|     |     |     |     | A47 |     | Secretory |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- |
Basal
|     |     |     |     | A48 |     | Chondrocyte |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- |
SMG
| 1TA 2TA | lasaB detailiC lamosoretueD 2TA_gnidiviD lasaB_gnidiviD hsurB_n_etyconoI | lailehtipeoyM enircodneorueN lasaB_GMS tcuD_GMS suocuM_GMS | suoreS_GMS bulC_yroterceS telboG_yroterceS lasabarpuS |     |     |     |     |     |     |     |
| ------- | ------------------------------------------------------------------------ | ---------------------------------------------------------- | ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
Vasculature & SM
f
Cap-a
Cap-g
| e   |     |     |     |     |     | Peri-pulm |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- |
Fibroblasts
SM-pulm
E-Art-pulm
Endoneurial NAF
| Schwann myelinating |     |     |     |     |     | E-Ven-pulm |     |     |     |     |
| ------------------- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- |
IR-fibro
E-Art-syst
Mesothelial
| Fibro. peribronchial |     |     |     |     |     | E-Ven-syst |     |     |     |     |
| -------------------- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- |
Fibro. perichondrial
IR-Ven-Peri
Perineurial NAF
Peri-syst
Schwann nonmyel.
|     | Fibro-adv |     |     |     |     | ASM |     |     |     |     |
| --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Fibro-alv
| Myofibroblast |     |     |     |     |     | SM-Art-syst |     |     |     |     |
| ------------- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- |

Supplementary Figure 3
|     | Artery | Capillary |     | Vein |
| --- | ------ | --------- | --- | ---- |
a
Systemic
Vascular Endothelia
| E-Art-syst |     | Cap-g | E-Ven_syst |     |
| ---------- | --- | ----- | ---------- | --- |
Pulmonary
b
|     | E-Art-pulm |               Cap-a |     E-Ven-pulm |     |
| --- | ---------- | ------------------- | -------------- | --- |
| c   |            | Systemic            |                |     |
Perivascular cells
| SM-Art-syst |     | Peri-syst | IR-Ven-Peri |     |
| ----------- | --- | --------- | ----------- | --- |
d
Pulmonary
SM-pulm Peri-pulm

Supplementary Figure 4
Undefined
morphology
Arterial
vessel
Airway
smooth
muscle
Nerve
bundle
Cartilage Perichondrium SMG Small
airway
Multilayer
epithelium
Immune
infiltrate
Venous
vessel
Pulmonary
vessel
Parenchyma Tissue Mesothelium
a Manual annotation b 8 Factors c 11 Factors d 21 Factors
B_naive
T_reg Microenvironment key:
CD4_EM_Effector
CD8_EM
CD4_TRM
ILC Surface epithelium
gdT
CD8EM_EMRA Secretory Goblet
Macro_CHIT1
MAIT Ciliated
Macro_interstitial Basal
Macro_CCL
cDC1
Mast_cell
B_memory Submucosal gland
Monocyte_CD16
Monocyte_CD14 Serous glands
NKT
PB_fibro Mucous/duct glands
Macro_intravascular
Macro_intermediate Parenchyma
CD4_naive_CM
Macro_alv_MT AT2 niche
E_Ven_syst AT1 niche
IR_Ven_Peri
E_Ven_pulm
B_plasma_IgG Arterial vessel
B_plasmablast
LE Venous vessel
Fibro_adv
Myofibroblast Cartilage/perichondrium
Peri_syst Nerve bundle
IR_Fibro
Mesothelia Immune infiltrate
Dividing_Basal
Macro_AW_CX3CR1
Myoepithelial
SMG_Duct
B_plasma_IgA
SMG_Serous Observation type key:
SMG_Mucous
Neuroendocrine
SMG_Basal
Chondrocyte Manually resolved
PC_fibro
mSchwann microenvironments
nmSchwann
NAF_endoneurial
NAF_perineurial Microenvironments
E_Art_pulm
ASM resolved further by NMF
E_Art_syst analysis
SM_pulm
SM_Art_syst
Erythrocyte
Macro_dividing
AT1
Cap-a
Cap-g
AT2
Fibro_alveolar
Macro_alveolar
Peri_pulm
Megakaryocyte
Secretory_Club
Basal
Suprabasal
Ciliated
Secretory_Goblet
Deuterosomal
Ionocyte_n_Brush
NK_CD56bright 0.8
CD8_TRM
Dividing_AT2 0.6
NKCD11d
cDC2 0.4
pcDC
NK_CD16hi 0.2
CD8_TRM_EM
DC_activated 0.0
10-1
10-2
e Mapping of microenvironments from 11 factors
10-3
AT2 niche AT1 niche
Bronchi section
1 mm
Basal epithelium Ciliated epithelium Secretory Goblet
Cell
type
loadings
Mean
nUMI
Mean
nUMI
Cell
type
loadings

|     | ## Fibroblast markers | ## Smooth muscle markers |  # ILC |
| --- | --------------------- | ------------------------ | ------ |
Supplementary Note 1:
  'AREG','SOX4','KIT','TNFRSF18',
| Cell type markers |  #Fibroblast           | ##Smooth muscle                            |          |
| ----------------- | ---------------------- | ------------------------------------------ | -------- |
|                   |  'VCAN', 'PDGFRA',     |  'TAGLN', 'ACTA2','TPM2', 'MYH11', 'CNN1', |  # MAIT  |
'KLRB1','IL7R','IFNGR1','SLC4A10','TRAV1-2','TRBV6
|     | # Alveolar fibroblast          | #Smooth muscle (no pericytes) | -2','DUSP2', |
| --- | ------------------------------ | ----------------------------- | ------------ |
|     |  'TCF21', 'ITGA8',  'FGFR4',   |  'ACTG2', 'DES',              |              |
# NK_CD16hi
##Epithelial markers # Adventitial fibroblast #Airway smooth muscle 'FCER1G','GNLY','KLRF1','KIR2DL1','GZMB',
 'SFRP2', 'PI16','FBLN2', 'CD248', 'MFAP5',    'FGFBP2', 'NKG7',
|     |     | 'HPSE2','COL4A6','PRUNE2','NRP2','SEMA3E' |     |
| --- | --- | ----------------------------------------- | --- |
#AT1, Alveolar Type 1 epithelial cell, pneumocyte #Immune recruiting fibroblast , 'PCDH7', 'DOCK3', 'GPM6A','HS6ST3',   # NKT, also T cell and NK cell markers already in the
'AGER', 'RTKN2', 'CLIC5',   'CXCL12',      "LGR6",  'PRUNE2',  'BCHE', #'SCARA3',    marker gene list
|                                        |                                                   | 'SCUBE1',       |  'S1PR1','IL32',               |
| -------------------------------------- | ------------------------------------------------- | --------------- | ------------------------------ |
|  #AT2, Alveolar Type 2 epithelial cell | #Fibroblast, T reticular Cells in lymph nodes &   |                 |                                |
 'SFTPC', 'SFTPA1', 'SFTPA2', 'WIF1', 'HHIP', 'CA2', #Immune recruiting fibroblast #Smooth muscle systemic arteries # NK_CD11d
'ETV5' , 'WIF1', 'HHIP',  'CCL21', 'CCL19', 'GREM1',   'SORBS2',  'SYNM',  'PHLDA2', 'NET1',   'ITGAD','CD247','KIR3DX1','ITGAX', 'KLRC3',
|     |     |      |     |
| --- | --- | ---- | --- |
#Dividing #Follicular DC-s &  #Immune recruiting fibroblast #Muscle smooth vascular pulmonary # NK_CD56bright
 'MKI67','CDK1',  'TOP2A',  'CXCL13', 'FDCSP',   'ELN',  'COL1A1',   'TGM2',  'TNNT2',   'XCL1','CMC1','CD7','CCL3','NCR1','IL2RB','SRGN',
|                     |                 |              |          |
| ------------------- | --------------- | ------------ | -------- |
| #Ciliated           |  #Myofibroblast | ## Pericyte  | #  Tregs |
'GSTA1', 'DTHD1', 'DCDC2B',   'ITGBL1', 'ASPN', 'TSPAN8', 'LMOD1',   'NALCN',   'RGS5', "ABCC9", ‘CSPG4’  'FOXP3','CCR4','CTLA4','IL2RA','TNFRSF4','TIGIT',
|     | 'ITGBL1', 'WISP2', 'F2R',  'WIF1', 'CCDC68',   |                           |     |
| --- | ---------------------------------------------- | ------------------------- | --- |
 #Ciliated and Deuterosomal 'CHRM2',  #Pericyte Parenchyma (CSPG4 negative) # gdT
 'PIFO', 'FOXJ1' , 'CCDC78',                             'HIGD1B', 'COX4I2',  'PTN', 'LAMC3', 'MEST',  'KLRC2','TRDC','TRDV1','TRG-AS1','TRGC1','KIR2DL
|     | # Peribronchial Fibroblast: | 'KCNK3', | 4',  |
| --- | --------------------------- | -------- | ---- |
#Deuterosomal     "TMEM132C", "PAPPA", "COL13A1",
 'CDC20B', 'CDC20', 'FOXN4', 'CCNO', "ATRNL1", "PLPPR4", "LHFPL3", "RGN",  #Pericyte immune recruiting  #Erythrocyte
                           "CORIN" ,   'CCL19', 'CCL2', 'CXCL12', 'CCL21', 'FGF7',    'HBA1', 'HBA2', 'HBD', 'HBB',
 #Secretory_Club & Secretory_Goblet     'F13A1','LINC01436','FGF14',  'CHN1',  'TNC',  'CLSTN2', 'CHSY3' ,'FABP4', 'STEAP4',
'CEACAM6', 'SCGB1A1',  'PAPPA',   'PLCL1','NTRK3', 'SUGCT', 'PRDM6',
                    'ENOX1', 'ENTPD1',    'PDE3B',  'ATRNL1',  #Pericyte systemic  ## Myeloid
#Secretory_Club 'COL15A1', 'PAG1', 'SLC7A2',  "FRMD3", "SLC38A11",  'AIF1','LYZ',  'COTL1',
|  'SCGB3A2',   |     | "NEURL1B", "NCKAP5", "SLC38A11", |            |
| ------------- | --- | -------------------------------- | ---------- |
#Perichondrial fibroblast #DC_1, (cDC1, conventional dendritic cell 1)
#Secretory_Goblet   'KDR',   'FGFR2',  'TMTC1',  'COL12A1',  ##Immune markers  'CLEC9A', 'XCR1', 'C1orf54', 'WDFY4', 'LGALS2',
'MUC5AC', 'TSPAN8','CYP2F1', 'CEACAM5',   'CHI3L1',   'RUNX2', 'SCARA3',   'ZFHX4',   'DNASE1L3',
| 'VSIG2', 'FUT6',     | 'GRID2',  'PCDH11X', | # Immune  |                        |
| -------------------- | -------------------- | --------- | ---------------------- |
|                      |                      | 'PTPRC',  | #DC_1 and DC activated |
#SMG_Mucous, Sub-mucosal glands, mucous  #Chondrocyte  'IDO1',
| secreting cells |  'ACAN' ,'CHAD'  | ##Lymphoid |     |
| --------------- | ---------------- | ---------- | --- |
 'BPIFB2', 'MUC5B', 'TFF3','TFF1',                      ,'COL9A3','HAPLN1','COL2A1','CYTL1',   #DC activated
                      #B cell  'CCR7', 'BIRC3', 'RASSF4', 'TRAF1', 'EBI3',
#SMG_Serous, Sub-mucosal glands, serous  #Mesothelia  'CD19', 'CD79A',
secreting cells 'MSLN', 'UPK3B', 'WT1',  'CALB2', 'HP', 'PRG4',  'MS4A1','BANK1','LINC00926', 'BLK', #DC_2, (cDC2, conventional dendritic cell 2  )
 'PRR4', 'LPO', 'PIP','S100A1', 'PRB3', 'C6orf58',  'ITLN1',                        'CD1C',  'CLEC10A', 'FCGR2B', 'FCER1A',
'PRB4', 'ODAM', 'PRH2',          #B memory/ mature
|     | #Nerve-associated fibroblast (NAF) | 'CD27',  'TNFRSF13B',  | #Monocyte |
| --- | ---------------------------------- | ---------------------- | --------- |
#SMG_duct, Submucosal gland collecting duct  'NGFR', 'TENM2','EBF2',  'THBS4',                     'CD300E', 'FCN1',
| columnar cells |     | #B naive |                     |
| -------------- | --- | -------- | ------------------- |
 'CLU', 'PROM1', 'RARRES1', 'CCL28', 'ALDH1A3',  #Endoneurial NAF  'IGHD', 'FCER2', 'TCL1A',   #Monocyte_CD14
'PI3', 'MIA','KRT23', 'KRT7',   'ANGPTL7', 'APOD', 'AMD1',   'CDH19', 'TIAM1',   'S100A12', 'EREG', 'CD14',
    'SCGB3A1',    'RARRES1', 'ZNHIT6',  'KRT7',   'USP54',  #Proliferating cells, (Plasmablast if have
| 'WNT5B', |     | plasma cell markers) | #Monocyte_CD16 |
| -------- | --- | -------------------- | -------------- |
     #Perineurial NAF  'MKI67', 'CDK1',  'TOP2A',   'FCGR3A', 'LILRB2', 'LILRB1', 'MTSS1', 'FAM110A',
 # SMG Basal, Basal cells of the sub-mucosal   'PDZRN4', 'FGL2', 'SLC2A1', 'ITGA6',   'LRRC25', 'CDKN1C', 'ABI3',
| glands | 'SORBS1','STXBP6','SLC22A3',  | #Plasma cells |        |
| ------ | ----------------------------- | ------------- | ------ |
 'PTK2B', 'MMP2', 'COL14A1', 'NUAK1',"G0S2",                 'MZB1', 'SDC1',  #Macrophage
                       #Schwann 'C1QA', 'C1QB', 'C1QC', 'APOE', 'APOC1',
#Basal and suprabasal 'PLP1' ,'MPZ','S100B',  #B plasma IgG
'KRT5', 'TP63',  'S100A2',  'KRT6A', 'TNS4',   'IGHG1', 'IGHG3', 'IGHG2', #Macrophage alveolar, Macro_alv
#Myelinating Schwann   'MARCO', 'MCEMP1', 'INHBA', 'TREM1', 'ABHD5',
#Basal airway epithelia 'GLDN','CDH7','DRP2','NFASC',  'NCMAP',   #B plasma IgA 'PPARG', 'RETN',  'CD5L',  'FABP4',
 'MMP10', 'KRT14', 'DLK2', 'KRT15', 'COL17A1',  'MBP', 'PRX', 'MLIP',  'IGHA1', 'IGHA2',    'CCR10',
'LOXL4',  #Macrophage alveolar  metallothioneins
                           #Non-myelinating Schwann: #B plasma and DC plasmacytoid 'MT2A', 'MT1X', 'MT1G', 'MT1F', 'MT1H',
| #Suprabasal |    'ADGRB3', 'ADGRL3',  |  'JCHAIN',   |     |
| ----------- | ----------------------- | ------------ | --- |
'LY6D', 'PLAT','SERPINB4',                            'ARHGEF26','ADAM23','ARHGAP15','NRXN3',  #Macrophage CHIT1
                           'NRXN1', 'NCAM1',  'NCAM2', 'NLGN4X', 'NTM',  #DC plasmacytoid 'SPP1', 'PLA2G7',  'FOLR2', 'SLC1A3', 'SDC2',
#Ionocyte 'NKAIN3', 'CADM2', 'CHL1', 'CADM1',   'CLEC4C',  'PLD4', 'LILRA4', 'CXCR3', 'IL3RA', 'CHIT1', 'OTOA',
|  'FOXI1', 'CFTR',  'ASCL3',    | 'CDH19','GRIK2', 'DOCK5' ,'COL21A1', 'CDH19',  |      |     |
| ------------------------------ | ---------------------------------------------- | ---- | --- |
                     'CADM4' , 'SCN7A',  'SORBS2',  'STARD13',        #Macrophage interstitial
#Brush 'SLC35F1',  'SOX6', 'SCN9A','SOX10',    ## T& NK 'CXCL10', 'CXCL9',  "CXCL11",'GBP1', 'GBP5','GBP4',
'HEPACAM2', 'PLCG2', 'BIK',  'PPP2R2B', 'PCDH9', 'PTPRZ1',  'PRIMA1',  'GBP2', 'PSTPIP2', 'SLAMF7',
                          'PTPRJ',  'PDE1C','PLCE1',  'TENM3',  'TMOD2',     #  T cells 'WARS','STAT1','GCH1', 'APOL3',
#Neuroendocrine 'TTYH1',   'FRMD4A', 'FRMD5',    'FAM129A',       'CD3E','CD3G','CD3D',
 'CHGA', 'CALCA', 'ASCL1',  'CHGB', 'GRP' ,'BEX1',   'KIAA1217',  'KCNMB4','KHDRBS3',  #Macrophage intravascular
                 'L1CAM','ERBB3',    'HAND2-AS1',    'LGI4',   # CD4 T-cells 'LILRB5','F13A1', 'STAB1', 'RNASE1', 'MAF', 'FOLR2',
 #Myoepithelial and Basal 'FIGN',   'ITGB4',  'IQGAP2', 'XKR4',  'IQGAP2',      'CD4','CD40LG','CCR6','CXCR6',  "LYVE1",
| "TP63",  "KRT14", "KRT15", "KRT5",  "KRT17",    | 'HAND2',  'ZSWIM6'  |            |                 |
| ----------------------------------------------- | ------------------- | ---------- | --------------- |
| 'USP31',                                        |                     | # CD4_TRM  | #Macrophage CCL |
##Endothelial markers     'CCL4', 'CCL20', 'CCL4L2', 'CXCL3',  'CXCL8',
#Myoepithelial and muscle 'ITGA1','ITGAE','ZNF683','CCL4','CCL5','PFN1' 'CCL20', 'IL1B', 'CXCL5', 'CXCL2',
 "ACTG2", 'ACTA2', 'TAGLN', 'CNN1',   #Endothelia , 'GZMA','GZMB',
 'PECAM1',  #note CCL4, CCL5,PFN1, GZMA, GZMB are  # Macro airway CX3CR1
#Myoepithelial                         expressed in CD8 and NK, but for CD4 they   'CX3CR1', 'RGS1', 'C3',  'PALD1',  'MEF2C',
 'LAMA1', 'PLD5',  'FHOD3', #Endothelia vascular are expressed mainly in the TRM population 'DOCK4','EPB41L2', 'ADAM28',
 'AQP1', 'VWF',                            'SERPINB9', 'ST6GAL1',  'FCGBP',  'SRGAP1',
|     |     | #  CD4_naive/CM | 'NFATC2', 'IGSF21', 'BCL2', |
| --- | --- | --------------- | --------------------------- |
#Endothelia lymphatic  'LTB','LEF1','CD28','KLF2','SELL',         'SFMBT2',  'ATP8B4', 'INPP5D',  'SLC4A7',
 'CCL21',   'PROX1',  'FLT4',  'SIGLEC8', 'SIGLEC10',   'PLD4',  'HAMP',
|     |                                       | #  CD8           |            |
| --- | ------------------------------------- | ---------------- | ---------- |
|     | #Endothelia vascular capillary, Cap-g |  'CD8A','CD8B',  | #Mast_cell |
 'CA4',   'FCN3',  'SLC6A4',  'IL7R',    'TPSAB1', 'TPSB2', 'CPA3', 'HPGDS', 'MS4A2',
|     |                                                 | # CD8_EM/EMRA                   | 'SLC18A2', 'TPSD1', 'RGS13', 'HDC', |
| --- | ----------------------------------------------- | ------------------------------- | ----------------------------------- |
|     | #Endothelia vascular capillary, Cap-a / Car4 /  |  'GZMH','KLRG1','PFN1','GZMA',  |                                     |
|     | Aerocyte                                        |                                 |  #Megakaryocyte                     |
 'HPGD', 'EDNRB', 'IL1RL1', 'S100A3',  #CD8_TRM/EM 'TUBB1', 'ANK1', 'PF4',  'TUBB1', 'CMTM5','PCSK6',
            'GZMK','EOMES','DTHD1','CRTAM', 'LYST', 'STON2', 'PRKAR2B', 'SYTL4', 'LTBP1',
|     | #Endothelia vascular arterial | 'TNIP3',                                     |                           |
| --- | ----------------------------- | -------------------------------------------- | ------------------------- |
|     |  'GJA5',  'DKK2', 'BMX',      |                                              | #Platelets/megakaryocytes |
|     |                               | # CD8_TRM                                    | 'PF4', 'GP9',             |
|     | #Endothelia vascular venous   | 'GZMB','CCL4','CCL5','ITGA1','PDCD1','ITGAE' |                           |
|     |  'SELE', 'ACKR1', 'PLVAP',    | ,'ZNF683',                                   |                           |
#Endothelia vascular venous pulmonary
 'CPE', 'DKK3', 'PDZRN4', 'EFEMP1', 'CDH11',
"PTGS1", "MMRN1", "PKHD1L1", "HDAC9",
#Endothelia vascular venous systemic
 'COL15A1', 'ZNF385D', 'EBF1', 'TSHZ2',
"FLRT2", "OLFM1", "CPXM2", "TPD52L1",