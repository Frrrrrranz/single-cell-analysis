iScience
Article
Exploring the utility of snRNA-seq in profiling human
bladder tissue: A comprehensive comparison with
scRNA-seq
Graphical abstract Authors
BrianaSanto,EmilyE.Fink,
AlexandraE.Krylova,...,OliverWessely,
ByronH.Lee,AngelaH.Ting
Correspondence
ahting@mdanderson.org
In brief
Biologicalsciences;Cellbiology;
Transcriptomics
Highlights
d Multiplebladderanatomicalregionsweresampledtocapture
celltypediversity
d JointanalysisofscRNA-seqandsnRNA-seqwascompleted
tocomparetechnologies
d Non-codingRNAenrichmentinsnRNA-seqdataobscured
celltypeidentification
d SnRNA-seqapproachcouldcapturerarecelltypesand
betterresolvecellclusters
Santoetal.,2025,iScience28,111628
January17,2025ª2024TheAuthor(s).PublishedbyElsevierInc.
ll
https://doi.org/10.1016/j.isci.2024.111628

iScience
ll
OPENACCESS
Article
Exploring the utility of snRNA-seq in profiling
human bladder tissue: A comprehensive
comparison with scRNA-seq
BrianaSanto,1EmilyE.Fink,2,3AlexandraE.Krylova,1Yi-ChiaLin,4MohamedEltemamy,4AlvinWee,4OliverWessely,5
ByronH.Lee,6andAngelaH.Ting1,7,*
1Epigenetics&MolecularCarcinogenesis,M.D.AndersonCancerCenter,Houston,TX77054,USA
2GenomicMedicine,LernerResearchInstitute,ClevelandClinic,Cleveland,OH44195,USA
3CharlesRiverLaboratories,GarfieldHeights,OH44128,USA
4DepartmentofUrology,GlickmanUrologicalandKidneyInstitute,ClevelandClinic,Cleveland,OH44195,USA
5DepartmentofCardiovascular&MetabolicSciences,LernerResearchInstitute,ClevelandClinic,Cleveland,OH44195,USA
6DepartmentofUrology,M.D.AndersonCancerCenter,Houston,TX77054,USA
7Leadcontact
*Correspondence:ahting@mdanderson.org
https://doi.org/10.1016/j.isci.2024.111628
SUMMARY
Singlecellsequencingtechnologieshaverevolutionizedourunderstandingofbiologybymappingcelldiver-
sityandgeneexpressioninhealthyanddiseasedtissues.Whilesingle-cellRNAsequencing(scRNA-seq)has
been widely used, interest in single-nucleus RNA sequencing (snRNA-seq) is growing due to its benefits,
includingtheabilitytoanalyzearchivaltissuesandcapturerarecelltypesthatarechallengingtodissociate.
However,comparativestudiesacrosstissueshaveyieldedmixedresults,withsomereportingenhancedcell
typeretentionusingsnRNA-seqwhileothersfindingcelltypeidentificationtobechallenginginsnRNA-seq
data.TheGUDMAPconsortiumaimstoconstructamolecularatlasofthelowerurinarytract(LUT);thus,we
setouttodeterminethestrengthsandlimitationsofeachapproachincharacterizingLUTcelltypes.Usingthe
humanbladder,wedeterminedthatscRNA-seqofferedmorediscriminativegenesetsforidentificationwhile
snRNA-seqcouldfacilitatecaptureofpreviouslyunderrepresentedcelltypes.
INTRODUCTION brain, lung, breast, and PBMCs.2,4–8 Findings are mixed, with
kidneystudiesreportingsignificantincreaseinpodocytereten-
Single cell sequencing technologies have revolutionized our tion,4,8 while studies on breast report challenges in cell type
abilitytointerrogatebiologyinhealthanddisease,enablingthe identification.7 Through such studies, a concern has arisen—
mappingofcelltypediversityandexpressionsignatureswithin the enrichment of non-coding RNAs in differentially expressed
and across organ systems.1 While most studies to date have genes7 and the reduction in canonical markers. As a conse-
usedscRNA-seqformolecularmappingoftissues,anincreasing quence, cell type identification in single-nucleus exclusive
number of studies are exploring snRNA-seq profiling. Their studies, particularly in disease or when studying new biology,
reason for doing so is motivated by the proposed benefits of may prove to be a challenge. Thus, to establish which data
snRNA-seq,whichincludetheabilitytoanalyzearchivaltissues, typeisbestsuitedforthemolecularprofilingofhumananatomy,
thus increasing statistical power, and the potential to capture itisessentialtocompletecomparativestudiesformostifnotall
rarecelltypesinrobustnumbers.2,3 organandtissuetypes.
SelectstudieshavedemonstratedthatsnRNA-seqfacilitates Robust data collection is essential to ensure that generated
thecaptureofcells,suchasgliaandspecializedepithelia,that reference datasets are sensible, meaningful, and practical re-
oftenevaderobustquantificationbysnRNA-seq.1,2,4–7Thelow sourcesfortheresearch community.Towardtheobjectivesof
yield for such cell types has been attributed to their delicate the Genitourinary Development Molecular Anatomy Project
cellstructure,whichmaynotsurvivesinglecelldissociationpro- (GUDMAP)consortium,whichinitscurrentfundingcycleaims
tocol.Meanwhile,theisolationofnucleiforsnRNA-seqismore toconstructamolecularanatomyreferenceofthelowerurinary
feasible for suchcell types. To determine whethersnRNA-seq tract (LUT) in human and model organism,9,10 we set out to
profilingwillyieldmorerobustquantificationofatissue’scellular comparescRNA-seqandsnRNA-seqfortheirabilitytocapture
composition,somestudieshavecompletedhead-to-headcom- andcharacterizeLUTcelltypes.Wechosetofocusonthehu-
parisons of scRNA-seq and snRNA-seq cell type capture. man bladder given its complexity in cellular composition and
Currently, comparative studies have profiled human kidney, regionalanatomicaldiversity.11Ourhypothesiswasthatwhile,
iScience28,111628,January17,2025ª2024TheAuthor(s).PublishedbyElsevierInc. 1
ThisisanopenaccessarticleundertheCCBY-NC-NDlicense(http://creativecommons.org/licenses/by-nc-nd/4.0/).

iScience
ll
OPENACCESS Article
A B
C
D
E
(legendonnextpage)
2 iScience28,111628,January17,2025

iScience
ll
Article OPENACCESS
for specific cell types, snRNA-seq would provide for better lialcells,andDCNforfibroblasts.15Asaresult,wecouldassign
enrichment, scRNA-seq would provide more discriminative allremainingclusters(2,3,5,6,9–11,13)tothestromalcompart-
genesetsforcelltypeidentification andfunctionalannotation. ment. A comprehensive dot plot visualizing canonical markers
Totestourhypothesis,wecollected,sequenced,andcomputa- across pertinent bladder cell types was also constructed and
tionally integrated single-cell and single-nucleus samples from evaluatedtowardcompartmentassignment(FigureS1C).
pairedspecimensoriginatingfromeachofthefourmajorbladder
regions [dome, neck, ureteral orifice (UO), and ureterovesical Classificationoftheurothelialcells
junction(UVJ)]12andcomparedeachcelltype’ssingle-celland Re-analysisoftheurothelialsubsetresultedinthreeclusters(Fig-
single-nucleussubpopulationsbasedondifferentiallyexpressed ure 1C,UMAP).The differentialgene expressionanalysis(DEA)
genesandenrichedbiologicalprocesses. showedthateachclustercorrespondedtooneofthegeneralur-
othelial layers: the basal urothelium (KRT5+/KRT13+/KRT17+/
RESULTS MKI67+), the umbrella cells (UPK1A+/UPK1B+/UPK2+/UPK3A+/
UPK3B+/KRT20+),andtheintermediateortransitionalurothelium
Single-cellandsingle-nucleusprofilingofhuman (AKR1C2+/IL1RAPL2+/TP63+/GATA3+/CDHR5+) (Figure 1C, Dot
bladdercells Plot).13,16 The intermediate urothelial cluster was the largest of
To interrogate single-cell and single-nucleus technologies for thethreeclusters(8,108cells),followedbythebasal(5,179cells)
theirabilitytoprofilebladdercelltypes,weperformedjointsin- andtheumbrella(1,489cells)cellpopulations.Interestingly,the
gle-cell and single-nucleus analysis of cells collected from the intermediate cell population showed significant single nuclei
dome,neck,UO,andUVJofhumanbladdertissue.Histological- enrichment (16.1%), while the umbrella (90.7%) and the basal
lynormalhumanbladdertissuewasprocuredfromaDonation (98.9%)populationsweremadeupalmostentirelyofsinglecells
afterBrainDeathorgandonor.Theuseoftissuesfromasingle (Figure1C,BarPlot).
donorhelpedtominimizegeneexpressionvariabilityandallow
for a true head-to-head comparison between scRNA-seq and Classificationoftheimmunecells
snRNA-seq. Using multiple different bladder regions further Re-clustering of the immune subset resulted in nine clusters
added to the robustness of this comparison. Following tissue (Figure1D,UMAP).Followingdifferentialgeneexpressionanal-
collection, samples were immediately dissociated into single- ysis, we identified one cluster each of B Cells (CD79A+/
cellsuspensionsandprocessedforscRNA-seq.Inparallel,an CD79B+/MS4A1+), plasma cells (JCHAIN+/SLAMF7+/CD27+),
adjacent specimen from each bladder region was frozen and macrophage (C1QA+/C1QB+/C1QC+), dendritic cells (DC)
batch-processedforsnRNA-seqlater.Theaveragesequencing (CLEC10A+/CIITA+), monocytes (S100A8+/S100A9+), neutro-
depth across samples was 540.8M (Table S1). After quality phils(GK+/AQP9+/TREM1+),Tcells(Il7R+/CD8A+/CD8B+),natu-
control and filtering, a total of 29,834 cells comprised of ral killer (NK) cells (KLRD1+/CD247+/GZMB+), and mast cells
22,231 single cells and 7,603 single nuclei (Figure 1A), from (KIT+/TPSAB1+/TPSB2+) (Figure 1D, Dot Plot).15,17 The T cell
four human bladder regions each (dome, neck, UO, UVJ), cluster was the largest of the immune compartment with 736
were segregated into 14 clusters by unsupervised clustering cells,whilethesmallestwastheplasmacellclusterwith31cells.
(Figure S1A; Table S2). Samples from each bladder region Interestingly, macrophage (42.5%) and mast (32.7%) cells
and data type (single-cell and single-nucleus) were uniformly demonstrated significant single-nucleus enrichment, while
distributed throughout the UMAP (Figure S1B). To partition plasma (96.8%), DC (95.0%), monocyte (89.6%), neutrophil
UMAPclustersintothethreemajorcellularcompartmentsofhu- (100%), and NK cells (91.1%) had significant single-cell
manbladder—urothelium,stroma,andimmune—wevisualized enrichment. T cells, the largest immune cell population, were
established markers for each compartment as feature plots not enriched significantly for either data type (Figure 1D,
(Figure1B).Forthe urothelium, wepreviewed KRT5, amarker BarPlot).
foruroepithelialbasalcells,andUPK1A,amarkerforumbrella
cells.13,14 We found that clusters 0, 1, 4, and 12 comprised a Classificationofthestromalcells
urothelial island where the gradient from basal to umbrella Analysis of the stromal subset resulted in twelve clusters
expression could be discerned based on plotted makers. For (Figure 1E, UMAP). For each stromal cluster, established
the immune compartment, we plotted PTPRC, the leukocyte markersweredistinctlyexpressedwithinDEGsets,facilitating
common antigen, and IL7R, a marker of lymphoid and devel- unambiguous assignment of cell types. As expected, several
oping immune cells,14,15 thus identifying clusters 7 and 8 as distinct fibroblast clusters (PDGFRA+/DCN+/COL1A1+) were
the immune compartment. Lastly, to identify stromal clusters, observed. In this case, we identified five clusters which we
weplottedMYLKforsmoothmusclecells,PECAM1forendothe- refer to as myofibroblast (MYLK+/MYH11+), peri-urothelial
Figure1. Jointsingle-cellandsingle-nucleusprofilingofhumanbladdercells
(A)Distributionofsinglecellsandsinglenucleiperbladderregionbeforeandafterqualitycontrolfiltering.
(B) UMAP with assigned bladder compartments and feature plots for established urothelial, stromal, and immune markers that facilitated compartment
assignment.
(C–E)UMAPsoftheurothelial(C),immune(D),andstromal(E)compartmentsbasedongeneexpression.AdjacenttotheUMAPs,dotplotsforeachcorre-
spondingcompartmentshowtheexpressionlevelofknownmarkersacrosscellclustersidentifiedineachcompartment.Farrightbarplotsshowtheenrichment
ofsinglecellsandsinglenucleiineachcompartment.*Asterisksindicatestatisticallysignificantenrichment.
iScience28,111628,January17,2025 3

iScience
ll
OPENACCESS Article
A
B
(legendonnextpage)
4 iScience28,111628,January17,2025

iScience
ll
Article OPENACCESS
fibroblast (LAMC3+/PTCH1+/APOE+), lamina propria fibroblast markersfortheumbrellapopulationalignedwithestablishedur-
(GAS1+/PCOLCE2+/PI16+/MFAP5+), intra-muscular fibroblast othelialmarkers(e.g.,UPK2andUPK3A)andthetopDEGsdid
(C7+/PCOLCE2-), and CXCL14hi fibroblast (GPC3+/NFGR+/ notdistinguishthebasal,intermediate,andumbrellacellswell.
CXCL14+).14,15,18,19Inaddition,severaldistinctendothelialand Thisobservationwasparticularlyapparentfortheintermediate
smooth muscle cell clusters were identified. The endothelial cells, where top markers included non-coding RNAs (e.g.,
cell population comprised a more general endothelial cluster AC005064.1)andtheheatmapshowedhighlyvariableexpres-
(PECAM1+/GJA5-/SELP-/LYVE1-), that was not enriched for sionamongtheintermediatecells.Instarkcomparison,thetop
either arterial or venous markers exclusively, a venous markersbasedonsingle-celldataincludedcanonicalurothelial
cluster(SELP+/NRP1+),anarterialcluster(GJA5+/BMX+),anda markers (e.g., UPK2, UPK3B, KRT20, and CEACAM1) and
lymphatic cluster (LYVE1+/TFF3+/CD36+).14 With respect to demonstratedcell-typespecificpatternsofDEGexpressionfor
smooth muscle cells, we identified two distinct clusters corre- thebasal,intermediate,andumbrellacellpopulations.Tofurther
sponding to general smooth muscle cells (ACTA2+/ACTG2+/ evaluatehowwellDEGscomputedfromsingle-nucleusandsin-
DES+) and vascular smooth muscle cells (RGS5+/NOTCH3+/ gle-cellsubpopulationscouldhelpdeciphercelltypesandfunc-
MCAM+).14,19Lastly,weidentifiedasingleSchwanncellcluster tions, we performed gene set enrichment analysis using each
(CDH19+/NRXN+/XKR4+).20 cellsubpopulation’sDEGset.ItwasfoundthatDEGscomputed
Liketheurothelialandimmunecompartments,weassessed fromsingle-nucleussubpopulationscorrespondedtoverygen-
theenrichmentofsinglecellsandsinglenucleiforeachstromal eralbiologicalterms(TableS6),whereasthosecomputedfrom
cell type. Of the twelve clusters, the largest was the general single-cell subpopulations correctly indicated epithelial cells
Endothelial cell cluster, comprising 2,485 cells, and 94.6% of (Table S7). For example, umbrella single-nucleus DEGs high-
whichwereprocuredbythesingle-cellprotocol.Othercelltypes lighted ‘‘Anatomical structure development,’’ ‘‘Developmental
demonstratingsingle-cellenrichmentwereCXCL14hifibroblast process,’’ and ‘‘Multicellular organism development’’ as en-
(66.4%), venous endothelial (99.2%), arterial endothelial richedterms;althoughinpracticetheseareverygenericbiolog-
(76.5%), and vascular smooth muscle cell clusters (71.6%). icalprocessesthatcouldapplytoanycelltype.Meanwhile,um-
The next largest population was smooth muscle cells, where brellasingle-cellDEGssuggestedpertinentprocessessuchas
88.6%ofcellswereofsingle-nucleusorigin.Inadditiontothe ‘‘Epithelium development’’ and ‘‘Epithelial cell differentiation’’
smooth muscle cell cluster, significant single-nucleus enrich- (Figure2A,GeneOntologyBarPlot).
mentwasobservedinthemyofibroblast(71.5%),intra-muscular
fibroblast(57.7%),lymphaticendothelial(65.8%),andSchwann Assessmentofsingle-cellandsingle-nucleus
(87.5%)cellclusters.Peri-urothelialandlaminapropriafibroblast expressionprofilesintheimmunecells
clusters did not show significant enrichment of a particular Asdonefortheurothelialcompartment,weevaluatedhowwell
datatype. single-nucleusandsingle-celltopDEGsdifferentiatedeachim-
munecelltype,andwhichbiologicalprocesseswereenriched
Assessmentofsingle-cellandsingle-nucleus forallDEGs.Onceagain,single-celltopmarkerexpressionpro-
expressionprofilesintheurothelium videdforbetterseparationofimmuneclusters.Thesepatterns
To evaluate whether single-nucleus data would produce wereparticularlyapparentforthemacrophage,monocyte,and
discriminativecellmarkersforcelltypeidentification,wesubset T cell populations (Figure 2B, Heatmaps). For single-nucleus
each urothelial cluster into its single-cell and single-nucleus top DEGs, notable markers included LYVE1 and RNASE1 for
subpopulations and completed DEA comparing each cluster macrophage,TLR2formonocytes,andIL7RforTcells.Mean-
subpopulation (e.g., basal single-nucleus) against all other while, canonical markers were prominent in single-cell top
urothelial cluster subpopulations (e.g., intermediate and basal DEGs for macrophage (C1QA, C1QB, C1QC), monocytes
single-nucleus subpopulations) (Tables S3 and S4). Then, we (S100A8, S100A9), and T cells (IL7R, CD3D, CD3E, CD69).
plotted the top ten differentially expressed genes (DEGs) for Enriched biological processes were comparable between
each cluster subpopulation on a heatmap (Figure 2A, Heat- datatypes,withsingle-nucleusDEGshighlighting‘‘Lymphocyte
maps). For the single-nucleus cluster heatmap, only the top activation,’’ ‘‘T cell activation,’’ and ‘‘Leukocyte activation,’’
Figure2. Assessmentofsingle-cellandsingle-nucleusgeneexpressioninthebladderurothelialandimmunecellpopulations
(A)UMAPsshowtheurothelialcompartmentpartitionedbysingle-nucleusandsingle-cellinstances.Heatmapsshowthetoptendifferentiallyexpressedgenes
(DEGs)foreachurothelialcelltype.TheupperheatmapshowsDEGsforurothelialcelltype’ssingle-nucleussubpopulations,whilethelowerheatmapshows
thoseDEGscomputedforsingle-cellsubpopulations.Differentialexpressionanalysiswascompletedbycomparingaurothelialcelltype’ssingle-nucleusor
single-cellsubpopulationagainstallothercelltype’srespectivesubpopulations.Thecolorbaraboveeachheatmapindicateswhichheatmapentriesbelongto
eachurothelialcelltype(basal,intermediate,orumbrella,colorcodedthesameasinFigure1CUMAP).Barplotsshowenrichedbiologicalprocessesforthe
umbrellacellpopulationbasedonallsingle-nucleusorsingle-celldifferentiallyexpressedgenes.
(B)UMAPsshowtheimmunecompartmentbasedongeneexpressionandpartitionedbysingle-nucleusandsingle-cellinstances.Heatmapsshowthetopten
differentiallyexpressedgenes(DEGs)foreachimmunecelltypewithsufficientnucleiandcellsfordifferentialexpressionanalysis(macrophage,monocyte,and
Tcells).TheupperheatmapshowsDEGsforimmunecelltype’ssingle-nucleussubpopulationswhilethelowerheatmapshowsthoseDEGscomputedforsingle-
cellsubpopulations.Differentialexpressionanalysiswascompletedbycomparinganimmunecelltype’ssingle-nucleusorsingle-cellsubpopulationagainstall
othercelltype’srespectivesubpopulations.Thecolorbaraboveeachheatmapindicateswhichheatmapentriesbelongtoeachimmunecelltype(macrophage,
monocyte,andTcells,colorcodedthesameasinFigure1DUMAP).Barplotsshowenrichedbiologicalprocessesforthemacrophagecellpopulationbasedon
allsingle-nucleusorsingle-celldifferentiallyexpressedgenes.
iScience28,111628,January17,2025 5

iScience
ll
OPENACCESS Article
Figure3. Assessmentofsingle-cellandsingle-nucleusenrichmentinthestromalbladdercellpopulations
UMAPsshowthestromalcompartmentbasedongeneexpressionandpartitionedbysingle-nucleusandsingle-cellinstances.Heatmapsshowthetopten
differentiallyexpressedgenes(DEGs)foreachstromalcelltypewithsufficientnucleiandcellsfordifferentialexpressionanalysis(myofibroblast,peri-urothelial
fibroblast,laminapropriafibroblast,intra-muscularfibroblast,CXCL14hifibroblast,smoothmusclecells,vascularsmoothmusclecells,aswellasgeneral,
arterial,andvenousendothelialcells).TheleftheatmapshowsDEGsforstromalcelltype’ssingle-nucleussubpopulationswhiletherightheatmapshowsthose
(legendcontinuedonnextpage)
6 iScience28,111628,January17,2025

iScience
ll
Article OPENACCESS
andsingle-cellDEGshighlighting‘‘Regulationofimmunesystem CSPG4).Conversely,inthesingle-cellanalysis,weidentified9
process,’’‘‘Immunesystemprocess,’’and‘‘Lymphocyteactiva- cell clusters (Figures S3A and S3B) and observed attrition of
tion’’(Figure2B,GeneOntologyBarPlot).Overall,intheimmune theintramuscularfibroblastsubpopulationandlossofresolution
compartment,weobservedlessofadiscrepancybetweendata betweenSMCandVSMCcells.Theseresultsechoedthefind-
typesintheirabilitytohelpdeciphercelltypes. ings from the single cell/single nucleus proportions test in the
joint analysis (Figure 1E). When visualizing the top cell cluster
Assessmentofsingle-cellandsingle-nucleus markers, we also noted a higher number of non-coding RNAs
expressionprofilesinthestromalcells in the single-nucleus analysis (Figure S2C) when compared
Finally,whenweevaluatedhowwellsingle-nucleusandsingle- withthesingle-cellanalysis(FigureS3C).
cell top DEGs differentiated stromal cell types, separation
amongcelltypesappearedcomparablebetweensingle-nucleus DISCUSSION
andsingle-celltopDEGs(Figure3,Heatmaps;FiguresS1Dand
S1E).However,uponfurtherinspection,thesingle-nucleusdata Here,wedescribethejointanalysisofscRNA-seqandsnRNA-
showedenrichmentfornon-codingRNAsinthetop10DEGsfor seqdatafromhumandonorbladdertissues.Weprocuredtis-
several cell types while canonical cell markers were absent sues from the dome, neck, UO, and UVJ anatomical regions
(TableS3).Forexample,thesmoothmusclecellsingle-nucleus and generated scRNA-seq and snRNA-seq data from paired
subpopulation top DEGs included non-coding RNAs CHRM3 samples of each region from a single donor. To properly inte-
and AC079313.2, but lacked canonical markers such as gratethesetwodatatypes,wecompletedextensivequalitycon-
ACTA2, ACTG2, or MYH11. These canonical markers were, trol filtering and batch correction, leveraging an established
however,foundinthesmoothmusclecellsingle-cellsubpopula- Seuratworkflow.21Uponcelltypeidentification,wefurthereval-
tion, facilitating unambiguous cell type identification. Similar uatedwhichcelltypesdemonstratedsingle-nucleusenrichment
observationsweremadeforthefibroblastandvascularsmooth oversingle-cell.Foreachcellpopulationcomprisingamixofsin-
muscle cell populations, where canonical markers such as glecellsandsinglenuclei,wecompletedgenesetenrichment
PDGFRAandRGS,respectively,wereabsentintopsingle-nu- analysis separately for the single-cell and single-nucleus sub-
cleus DEGs but present in single-cell top DEGs (Table S4). A populationstoseewhatbiologicalprocesseswerehighlighted
formalChi-squaredanalysisfoundthatnon-codingRNAswere byeachcelltype’ssingle-cellandsingle-nucleusgenesets.In
significantly enriched in the single nucleus DEG list of arterial doing so, we demonstrated, through a data-driven approach,
and lymphatic endothelial cells, all fibroblast subpopulations, ananticipatedchallengewithsnRNA-seqdata;thedifficultyto
smooth muscle cells, and vascular smooth muscle cells deciphercelltypebasedontopmarkergenesandenrichedbio-
(TableS5). logicalprocessesalone.WhilejointanalysisofscRNA-seqand
Thedifferencebetweensingle-nucleusandsingle-cellDEGs snRNA-seqfacilitatedcellidentificationinourstudy,studiesus-
was even more apparent in the gene ontology analysis. Like ing single-nucleus data alone, and especially those studies
ouranalysisoftheurothelialcompartment,single-nucleusDEG featuringdiscoveryofdenovocelltypes,facetheaddedchal-
sets indicated very generic biological processes (Figure 3, lenge of deciphering non-coding RNA-predominated cluster
GeneOntologyBarPlots).For example,for theintra-muscular markersandvaguenucleus-orientedontologyterms.
fibroblast,smoothmusclecell,andarterialendothelialcellpop- Todate,fewstudieshavecompletedahead-to-headcompar-
ulations,toptermsincluded‘‘Neurondevelopment,’’‘‘Develop- isonofscRNA-seqandsnRNA-seqdata,andnonehavedoneso
mental process,’’ and ‘‘Multicellular organism development,’’ usingpairedsamplesfromhumanbladdertissues.Priorstudies
respectively. In stark contrast, single-cell DEG sets produced haveshownthattheuseofsnRNA-seqwouldfacilitatethecap-
pertinent termsincluding ‘‘Extracellular structure organization’’ ture and interrogation of cell types that have historically been
for intra-muscular fibroblast, ‘‘Muscle contraction’’ for smooth difficulttocaptureusingsingle-cellprotocols.Forexample,cells
musclecells,and‘‘Bloodvesselsystemdevelopment’’forarte- suchasglia,kidneypodocytes,andlungalveolarepitheliaand
rialendothelialcells.Subsequentlyrankedgeneontologyterms fibroblastsaredifficulttoisolateinrobustnumbersduringtissue
demonstratedasimilartrend,withvague,generalbiologyterms dissociationforscRNA-seq.2,4–6Theinabilitytoisolatesuchcell
comingfromsingle-nucleusDEGsets(TableS6)andcell-type types has negative implications for studies where those cell
specific and correctly associated terms coming from single- typesarethemajordriversofdiseasepathology,suchasalve-
cellDEGsets(TableS7). olarepitheliaandfibroblastsinlungfibrosis.2Ongoingstudies,
Sincewehadrobustnumbersofbothcellsandnucleiinthe includingours,aimtoidentifywhichcelltypesinwhichorgans
stromalcompartment,weadditionallyperformedindependent, and anatomical regions would be best quantified by snRNA
parallelanalysesofeachdatasource.Inthesingle-nucleusanal- sequencing.Bormannetal.22andWangetal.23demonstrated
ysis, we identified 13 stromal clusters (Figures S2A and S2B), how single-nucleus technology enables collection of glia in
includinganadditionalfibroblastsubtype(Fibroblast-6)andan high volume toward identification of cell and molecular signa-
additional VSMC resembling pericytes (VSMC2; positive for turesassociatedwitholigodendrocyte andastrocyteresponse
DEGscomputedforsingle-cellsubpopulations.Differentialexpressionanalysiswascompletedbycomparingastromalcelltype’ssingle-nucleusorsingle-cell
subpopulationagainstallothercelltype’srespectivesubpopulations.Thecolorbaraboveeachheatmapindicateswhichheatmapentriesbelongtoeachstromal
celltype(colorcodedthesameasinFigure1E).Barplotsshowenrichedbiologicalprocessesfortheintra-muscularfibroblast,smoothmusclecell,andarterial
endothelialcellpopulationsbasedonallsingle-nucleusorsingle-celldifferentiallyexpressedgenes.
iScience28,111628,January17,2025 7

iScience
ll
OPENACCESS Article
toischemicinjuryinstrokeandglioblastomarecurrence.5,6The endothelial cells, top marker gene expression and ontology
authors suggested that the morphology of glia hinders their analysis were inadequate for cell type identification. For
isolation by single-cell methods. Similarly, podocytes, which example, canonical markers for these cell types were signifi-
areknownfortheirdistinctandfragilemorphology,areoftenun- cantlyreducedinsingle-nucleusDEGsets.Inaddition,enriched
derrepresented in single-cell studies. In a recent work, Wu biologicalprocesseswereeithertoovagueforcelltypeidentifi-
et al.24 reported a 20-fold increase in podocyte retention for cation (e.g., anatomical structure and system development
samples processed by snRNA-seq.8 Like lung epithelia, fibro- for smooth muscle cells) or indicated the incorrect cell type
blasts,andglia,podocytequantificationisessentialtoevaluate (e.g.,smoothmusclecontractionforintra-muscularfibroblasts).
renaldiseasepathology.4,8 When these same cell types were investigated by single-
TheadvantagesofsnRNA-seqarenotlimitedtoenrichment cell analysis, canonical markers were well enriched in the top
for rare cell types. Single-nucleus technology can be readily tenDEGspercluster,ontologytermswerepertinent(e.g.,mus-
appliedtocryopreservedsamples,enablingresearcherstotap cle contraction and muscle structure development for smooth
into expansive and archival biospecimen collections and thus muscle cells), and overall separation among cell types based
hasbecomethemainstayforsomeofthelargeprofilingconsor- ongeneexpressiondatawasclearinheatmaps.Inthestromal
tiumssuchastheKidneyPrecisionMedicineProject(KPMP).1–3 compartment, the greatest advantage conferred by single-nu-
Additionally,snRNA-seqhasbeenfoundtosignificantlyreduce cleusdatawasthecollectionofasizableSchwanncellpopula-
dissociation-induced transcriptional stress responses in cells, tion.Priorstudiesreportlittleenrichmentofneuronalcelltypes
which have the potential to confound findings in pathological when profiling the LUT, likely due to the morphology of these
statesorcellswithdistinctmitochondrialsignatures.3,8snRNA- cells.14
seqhasalsohelpedreducenoiseinthetranscriptionalprofiling Whenwefurthercomparedthesingle-nucleusandsingle-cell
of macrophage, which due to their phagocytic function may datainindependentanalyses,additionalbenefitsofsnRNA-seq
contain other cell type’s transcriptomes when quantified by becameapparent.Whensingle-nucleusdatawasanalyzedbyit-
scRNA-seq.Despitethesebenefits,theenrichmentofnon-cod- self, increased resolution of cell type subpopulations were
ing RNAs cannot be ignored. When working with large scale observed, including additional fibroblast and vascular smooth
snRNA-seqdatasets,itisimportanttohavecontextforcelltypes musclecell populations.Wealsoobserved anon-codingRNA
in disease, informed byprior scRNA-seq studies, sothat non- enrichment in the top DEGs per stromal cell type. These
coding RNA enrichment does not obscure cell type identifica- observations are in stark contrast to the independent single-
tion.AsnotedbyKumaretal.,suchnon-codingRNAenrichment cellanalysis,whereinweobserveddecreasedcelltyperesolu-
confoundedcanonicalmarkerenrichmentforcommonepithelial tion.Limitedsamplesizenotwithstanding,itcannotbeignored
celltypes.7Approachestomanagenon-codingRNAenrichment that using non-coding RNA enriched single nucleus data may
includefilteringoutnon-codingRNAspriortosampleintegration facilitatebiologicalinsightsfromthehumanbladderthatwould
andbatchcorrectionsothathighlyvariablegenesusedinclus- otherwise be overlooked by purely single cell data. Interactive
tering are protein-coding exclusively, or as done in our study, visualizations of all processed data with cell and data type
integrateandco-analyzescRNA-seqandsnRNA-seqdatasets. annotationsareavailableattheNIH-CZICELLxGENEDiscover
Inourstudy,thejointanalysisofsnRNA-seqandscRNA-seq CellularVisualizationTool.
datasets allowed us to identify cell types with ease as well as
demonstrate thebenefitsanddisadvantages of single-nucleus Limitationsofthestudy
data for human bladder tissue. Across the urothelial, immune, In this work, we only had eight samples from a single human
and stromal compartments, we identified several cell types donor.Toensurecomprehensiveprofilingofcelltypediversity
whichshowedsignificantsingle-nucleusenrichment.Intheuro- in both healthy reference datasets and disease states, it is
thelialcompartment,wefoundthatintermediateurothelialcells essentialthatadditionalstudiesanalyzepairedscRNA-seqand
demonstrated significant single nucleus enrichment. Despite snRNA-seqdatawithalargersamplesize.Oursampleswere,
thisenrichment,intermediateurothelialaswellasbasalandum- however, taken from each of the four major bladder regions,
brellacellsingle-nucleussubpopulationsweredifficulttoidentify withpairedsamplingforsingle-nucleusandsingle-celldatagen-
basedontopmarkersandgeneontology.Meanwhile,urothelial eration,providingabalancedandanatomicallydiversesampling
celltypesidentifiedbyscRNA-seqshowedsignificantcanonical oftheorgan.Althoughwelackedspatialtranscriptomicvalida-
marker and epithelial process enrichment. In the immune tionofourfindings,allcanonicalmarkersusedforcelltypeiden-
compartment,wefoundmacrophageandmastcellstohavesig- tificationinthisstudyarereferencedfrompriorworksinthekid-
nificantsingle-nucleusenrichment.Interestingly,thetopdiffer- ney, bladder, ureter, and other regions of the LUT.12–14,18 We
entially expressed genes and gene ontology terms derived alsorecognizethatcurrentgeneontologydatabasesarelargely
from single-nucleus and single-cell immune subpopulations based on coding genes and thus biased against non-coding
were comparable. Identification of immune cell type was RNAs. However, single-nucleus studies such as ours present
possibleusingeitherthesingle-nucleusorthesingle-cellDEGs uniqueopportunitiestoaugmentexistingknowledgebaseswith
andbiologicalprocesses. non-coding RNA and biological process associations. In sum-
Thegreatestdiscrepancybetweensingle-nucleusandsingle- mary,ourresultsherehelpedtoestablishaframeworkforsam-
celldatawasseeninthestromalcompartment.Whileseveralcell ple preparation and data collection and analysis for human
types demonstrated significant single-nucleus enrichment, bladdertissuesinbothsexesandacrossthelifespantogenerate
includingsomefibroblasts,smoothmusclecells,andlymphatic aLUTcellatlasaspartofGUDMAP.
8 iScience28,111628,January17,2025

iScience
ll
Article OPENACCESS
RESOURCEAVAILABILITY REFERENCES
Leadcontact 1.Ding,J.,Adiconis,X.,Simmons,S.K.,Kowalczyk,M.S.,Hession,C.C.,
Correspondenceandrequestsformaterialsshouldbeaddressedtothelead Marjanovic, N.D., Hughes, T.K., Wadsworth, M.H., Burks, T., Nguyen,
contact,AngelaH.Ting(ahting@mdanderson.org). L.T.,etal.(2020).Systematiccomparisonofsingle-cellandsingle-nucleus
RNA-sequencingmethods.Nat.Biotechnol.38,737–746.
Materialsavailability
2.Koenitzer,J.R.,Wu,H.,Atkinson,J.J.,Brody,S.L.,andHumphreys,B.D.
Thisstudydidnotgeneratenewuniquereagents.
(2020).Single-nucleusRNA-sequencingprofilingofmouselung.Reduced
dissociationbiasandimprovedrarecell-typedetectioncomparedwith
Dataandcodeavailability
single-cellRNAsequencing.Am.J.Respir.CellMol.Biol.63,739–747.
d RawandprocessedsequencingdatahavebeendepositedinSRAand
3.Kim,N.,Kang,H.,Jo,A.,Yoo,S.-A.,andLee,H.-O.(2023).Perspectives
theGeneExpressionOmnibusandarepubliclyavailableasofthedate
on single-nucleus RNA sequencing in different cell types and tissues.
ofpublication.Accessionnumbersarelistedinthekeyresourcestable.
J.Pathol.Transl.Med.57,52–59.
Inaddition,interactivevisualizationsofallprocesseddatawithcelltype
anddatatypeannotationsareavailableattheNIH-CZICELLxGENE 4.Lake,B.B.,Chen,S.,Hoshi,M.,Plongthongkum,N.,Salamon,D.,Knoten,
Discover-CellularVisualizationToolandcanbeaccessedhere. A.,Vijayan,A.,Venkatesh,R.,Kim,E.H.,Gao,D.,etal.(2019).Asingle-nu-
d AlloriginalcodehasbeendepositedonGitHubandispubliclyavailable. cleusRNA-sequencingpipelinetodecipherthemolecularanatomyand
d Anyadditionalinformationrequiredtoreanalyzethedatareportedinthis pathophysiologyofhumankidneys.Nat.Commun.10,2832.
papercanberequestedfromtheleadcontact.
5.Bormann,D.,Knoflach,M.,Poreba,E.,etal.(2024).Single-nucleusRNA
sequencingrevealsglialcelltype-specificresponsestoischemicstroke
ACKNOWLEDGMENTS
inmalerodents.NatCommun15,6232.https://doi.org/10.1038/s41467-
024-5.
WeacknowledgethesupportofLifebancinprocuringbladdertissuesfromthe
6.Wang,L.,Jung,J.,Babikir,H.,Shamardani,K.,Jain,S.,Feng,X.,Gupta,
deceased organ donor for this research. This work is supported by U01
N.,Rosi,S.,Chang,S.,Raleigh,D.,etal.(2022).Asingle-cellatlasofglio-
DK131383 to O.W., B.H.L., and A.H.T. National Institute of Diabetes and
blastomaevolutionundertherapyrevealscell-intrinsicandcell-extrinsic
DigestiveandKidneyDiseases(NIDDK)fundsU01DK131383.
therapeutictargets.Nat.Can.(Ott.)3,1534–1552.
AUTHORCONTRIBUTIONS 7.Kumar,T.,Nee,K.,Wei,R.,He,S.,Nguyen,Q.H.,Bai,S.,Blake,K.,Pein,
M.,Gong,Y.,Sei,E.,etal.(2023).Aspatiallyresolvedsingle-cellgenomic
Conceptualization,B.H.L.andA.H.T.;formal analysis,B.S. andA.E.K.; re- atlasoftheadulthumanbreast.Nature620,181–191.
sources,B.H.L.,Y.L.,M.E.,andA.W.;investigation,B.S.,E.E.F.,andA.E.K.;
8.Wu,H.,Kirita,Y.,Donnelly,E.L.,andHumphreys,B.D.(2019).Advantages
software,B.S.;supervision,A.H.T.;writing–originaldraft,B.S.,B.H.L.,and
ofsingle-nucleusoversingle-cellRNAsequencingofadultkidney:rarecell
A.H.T.;writing–reviewandediting,E.E.F.,Y.L.,M.E.,A.W.,andO.W.;funding
types and novel cell states revealed in fibrosis. J. Am. Soc. Nephrol.
acquisition,O.W.,B.H.L.,andA.H.T.
30,23–32.
9.Harding,S.D.,Armit,C.,Armstrong,J.,Brennan,J.,Cheng,Y.,Haggarty,
DECLARATIONOFINTERESTS
B.,Houghton,D.,Lloyd-MacGilp,S.,Pi,X.,Roochun,Y.,etal.(2011).The
GUDMAPdatabase–anonlineresourceforgenitourinaryresearch.Devel-
Theauthorsdeclarenocompetinginterests.
opment138,2845–2853.
STAR+METHODS 10.McMahon,A.P.,Aronow,B.J.,Davidson,D.R.,Davies,J.A.,Gaido,K.W.,
Grimmond,S.,Lessard,J.L.,Little,M.H.,Potter,S.S.,Wilder,E.L.,etal.
Detailedmethodsareprovidedintheonlineversionofthispaperandinclude (2008). GUDMAP: the genitourinary developmental molecular anatomy
thefollowing: project.J.Am.Soc.Nephrol.19,667–671.
11.Abedini,A.,Zhu,Y.O.,Chatterjee,S.,Halasz,G.,Devalaraja-Narashimha,
d KEYRESOURCESTABLE
K.,Shrestha,R.,SBalzer,M.,Park,J.,Zhou,T.,Ma,Z.,etal.(2021).Uri-
d EXPERIMENTMODELANDSTUDYPARTICIPANTDETAILS
narysingle-cellprofilingcapturesthecellulardiversityofthekidney.J.Am.
B Humanbladderprocurement
Soc.Nephrol.32,614–627.
d METHODDETAILS
B Definitionofbladderregions 12.Liaw,A.,Cunha,G.R.,Shen,J.,Cao,M.,Liu,G.,Sinclair,A.,andBaskin,L.
B Singlecellisolation (2018).Developmentofthehumanbladderandureterovesicaljunction.
B Singlenucleusisolation Differentiation103,66–73.
B Sampleprocessingandlibrarypreparation 13.Yu,Z.,Liao,J.,Chen,Y.,Zou,C.,Zhang,H.,Cheng,J.,Liu,D.,Li,T.,
B scRNA-seqandsnRNA-seqdatajointanalysis Zhang,Q.,Li,J.,etal.(2019).Single-celltranscriptomicmapofthehuman
B scRNA-seqandsnRNA-seqsubsetanalysis andmousebladders.J.Am.Soc.Nephrol.30,2159–2176.
B scRNA-seqv.snRNA-seqgenesetanalysis
14.Fink,E.E.,Sona,S.,Tran,U.,Desprez,P.-E.,Bradley,M.,Qiu,H.,Eltem-
B IndependentscRNA-seqandsnRNA-seqanalysis
amy,M.,Wee,A.,Wolkov,M.,Nicolas,M.,etal.(2022).Single-celland
d QUANTIFICATIONANDSTATISTICALANALYSIS
spatialmappingIdentifycelltypesandsignalingNetworksinthehuman
ureter.Dev.Cell57,1899–1916.e6.
SUPPLEMENTALINFORMATION
15.Chen,Z.,Zhou,L.,Liu,L.,Hou,Y.,Xiong,M.,Yang,Y.,Hu,J.,andChen,K.
Supplementalinformationcanbefoundonlineathttps://doi.org/10.1016/j.isci. (2020). Single-cell RNA sequencing highlights the role of inflammatory
2024.111628. cancer-associatedfibroblastsinbladderurothelialcarcinoma.Nat.Com-
mun.11,5077.
Received:June3,2024 16.McConkey,D.J.,Lee,S.,Choi,W.,Tran,M.,Majewski,T.,Lee,S.,Siefker-
Revised:November1,2024 Radtke,A.,Dinney,C.,andCzerniak,B.(2010).Moleculargeneticsof
Accepted:December16,2024 bladdercancer:Emergingmechanismsoftumorinitiationandprogres-
Published:December18,2024 sion.Urol.Oncol.28,429–440.
iScience28,111628,January17,2025 9

iScience
ll
OPENACCESS Article
17. Zhong,J.,Ding,R.,Jiang,H.,Li,L.,Wan,J.,Feng,X.,Chen,M.,Peng,L., typesandnovelcellstatesrevealedinfibrosis.J.Am.Soc.Nephrol.30,
Li,X.,Lin,J.,etal.(2022).Single-cellRNAsequencingrevealsthemolec- 23–32.https://doi.org/10.1681/ASN.2018090912.
ularfeaturesofperipheralbloodimmunecellsinchildren,adultsandcen- 25.Satija,R.,Farrell,J.A.,Gennert,D.,Schier,A.F.,andRegev,A.(2015).
tenarians.Front.Immunol.13,1081889. Spatial reconstruction of single-cell gene expression data. Nat. Bio-
18. Apodaca,G.(2023).Definingthemolecularfingerprintofbladderandkid- technol.33,495–502.
neyfibroblasts.Am.J.Physiol.Ren.Physiol.325,F826–F856.
26.Macosko,E.Z.,Basu,A.,Satija,R.,Nemesh,J.,Shekhar,K.,Goldman,M.,
19. Joseph,D.B.,Henry,G.H.,Malewska,A.,Reese,J.C.,Mauck,R.J.,Ga- Tirosh,I.,Bialas,A.R.,Kamitaki,N.,Martersteck,E.M.,andTrombetta,
han, J.C., Hutchinson, R.C., Malladi, V.S., Roehrborn, C.G., Vezina, J.J.(2015).Highlyparallelgenome-wideexpressionprofilingofindividual
C.M.,andStrand,D.W.(2021).Single-cellanalysisofmouseandhuman
cellsusingnanoliterdroplets.Cell161,1202–1214.
prostaterevealsnovelfibroblastswithspecializeddistributionandmicro-
27.Stuart,T.,Butler,A.,Hoffman,P.,Hafemeister,C.,Papalexi,E.,Mauck,
environmentinteractions.J.Pathol.255,141–154.
W.M., 3rd, Hao, Y., Stoeckius, M., Smibert, P., and Satija, R. (2019).
20. Wei,Z.,Shu,S.,Zhang,M.,Xie,S.,Tang,S.,Nie,K.,andLi,H.(2021).A Comprehensive Integration of Single-Cell Data. Cell 177, 1888–1902.
subpopulationofSchwanncell-likecellswithnerveregenerationsigna- https://doi.org/10.1016/j.cell.2019.05.031.
tures is identified through single-cell RNA sequencing. Front. Physiol.
28.Hao,Y.,Hao,S.,Andersen-Nissen,E.,Mauck,W.M.,Zheng,S.,Butler,A.,
12,637924.
Lee,M.J.,Wilk,A.J.,Darby,C.,Zager,M.,andHoffman,P.(2021).Inte-
21. Sona,S.,Bradley,M.,andTing,A.H.(2023).Protocolsforsingle-cellRNA-
gratedanalysisofmultimodalsingle-celldata.Cell184,3573–3587.
seqandspatialgeneexpressionintegrationandinteractivevisualization.
STARProtoc.4,102047. 29.Miller,S.A.,Policastro,R.A.,Sriramkumar,S.,Lai,T.,Huntington,T.D.,La-
daika,C.A.,Kim,D.,Hao,C.,Zentner,G.E.,andO’Hagan,H.M.(2021).
22. Bormann,D.,Knoflach,M.,Poreba,E.,Riedl,C.J.,Testa,G.,Orset,C.,
LSD1andaberrantDNAmethylationmediatepersistenceofenteroendo-
Levilly,A.,Cottereau,A.,Jauk,P.,Hametner,S.,etal.(2024).Single-nu-
crineprogenitorsthatsupportBRAF-mutantcolorectalcancer.Cancer
cleus RNA sequencing reveals glial cell type-specific responses to
Res.81,3791–3805.
ischemic stroke in male rodents. Nat. Commun. 15, 6232. https://doi.
org/10.1038/s41467-024-50465-z. 30.Zappia,L.,andOshlack,A.(2018).Clusteringtrees:avisualizationforeval-
uatingclusteringsatmultipleresolutions.GigaScience7,giy083.
23. Wang,L.,Jung,J.,Babikir,H.,Shamardani,K.,Jain,S.,Feng,X.,Gupta,
N.,Rosi,S.,Chang,S.,Raleigh,D.,etal.(2022).Asingle-cellatlasofglio- 31.Patterson-Cross,R.B.,Levine,A.J.,andMenon,V.(2021).Selectingsingle
blastomaevolutionundertherapyrevealscell-intrinsicandcell-extrinsic cell clustering parameter values using subsampling-based robustness
therapeutictargets.Nat.Cancer3,1534–1552.https://doi.org/10.1038/ metrics.BMCBioinf.22,39.
s43018-022-00475-x. 32.Kolberg,L.,Raudvere,U.,Kuzmin,I.,Vilo,J.,andPeterson,H.(2020).
24. Wu,H.,Kirita,Y.,Donnelly,E.L.,andHumphreys,B.D.(2019).Advantages gprofiler2–anRpackageforgenelistfunctionalenrichmentanalysisand
ofsingle-nucleusoversingle-cellRNAsequencingofadultkidney:rarecell namespaceconversiontoolsetg:Profiler.F1000Research9,ELIXIR-709.
10 iScience28,111628,January17,2025

iScience ll
Article OPENACCESS
STAR+METHODS
KEYRESOURCESTABLE
| REAGENTorRESOURCE | SOURCE | IDENTIFIER |
| ----------------- | ------ | ---------- |
Biologicalsamples
| Humanbladdertissuesfrombraindead | Thispaper | NA  |
| -------------------------------- | --------- | --- |
donorpatientscollectedthroughLifeBanc.
Chemicals,peptides,andrecombinantproteins
| ACKLysisBuffer | ThermoFisherScientific | Cat#A1049201 |
| -------------- | ---------------------- | ------------ |
| SPRIselect     | Beckman                | Cat#B23317   |
Tissue-Tek(cid:2)O.C.T.Compound
|     | Sakura | Cat#4583 |
| --- | ------ | -------- |
Criticalcommercialassays
| PapainDissociationSystem             | Worthington | Cat#LK003150  |
| ------------------------------------ | ----------- | ------------- |
| ChromiumNextGEMSingleCell3ʹKitv3.1   | 10XGenomics | PN-1000268    |
| ChromiumNextGEMChipGSingleCellKit    | 10XGenomics | PN-1000120    |
| Chromiumi7MultiplexKit               | 10XGenomics | PN-120262     |
| LibraryConstructionKit               | 10XGenomics | PN-1000196    |
| DualIndexPlateTTSetA                 | 10XGenomics | PN-3000431    |
| AgilentHighSensitivityDNAKitReagents | Agilent     | Cat#5067-4626 |
| QuantiTectSYBRGreenPCRKit            | Qiagen      | Cat#204145    |
Depositeddata
| Single-CellandSingle-NucleusRNA-seq | Thispaper | PRJNA1111560 |
| ----------------------------------- | --------- | ------------ |
FASTQs
Processedsingle-cellandsingle-nucleus Thispaper GEO:GSE267964
RNA-seqdata
Processedsingle-cellandsingle-nucleus Thispaper https://cellxgene.cziscience.com/
| RNA-seqdata                 |     | collections/0e54d4de-44f0-4d50-8649- |
| --------------------------- | --- | ------------------------------------ |
| Andinteractivevisualization |     | b5c2bbe8f5d1                         |
Softwareandalgorithms
GitHub;Finketal.14
CodesforkedforSeuratdataintegration https://github.com/basanto/scRNA_
| andclusteringpipeline |     | Analysis_Developing_for_Human_Bladder_ |
| --------------------- | --- | -------------------------------------- |
Analysis
Codesusedfordifferentialexpressionand Thispaper;GitHub https://github.com/basanto/Human_
| geneontologyanalysis |     | Bladder_scRNA-seq_vs_snRNA-seq; |
| -------------------- | --- | ------------------------------- |
Zenodo[https://doi.org/10.5281/zenodo.
14446321]
| R   | CRAN | https://cran.r-project.org/ |
| --- | ---- | --------------------------- |
Satijaetal.25;Macoskoetal.26;
| Seurat(4.3.0.1) |     | https://cran.r-project.org/web/packages/ |
| --------------- | --- | ---------------------------------------- |
Stuartetal.27;Haoetal.28
Seurat/index.html
cellranger(7.1.0) 10XGenomics https://support.10xgenomics.com/single-
cell-gene-expression/software/pipelines/7.
1/release-notes
clustree(0.5.1) CRAN https://cran.r-project.org/web/packages/
clustree/index.html
argparser(0.7.1) CRAN https://cran.r-project.org/web/packages/
argparse/index.html
data.table(1.15.2) CRAN https://cran.r-project.org/web/packages/
data.table/index.html
| dplyr(1.1.4) | CRAN | https://cran.r-project.org/web/packages/ |
| ------------ | ---- | ---------------------------------------- |
dplyr/index.html
factoextra(1.0.7) CRAN https://cran.r-project.org/web/packages/
factoextra/index.html
(Continuedonnextpage)
iScience28,111628,January17,2025 e1

ll iScience
OPENACCESS Article
Continued
| REAGENTorRESOURCE | SOURCE | IDENTIFIER                               |
| ----------------- | ------ | ---------------------------------------- |
| ggplot2(3.5.0)    | CRAN   | https://cran.r-project.org/web/packages/ |
ggplot2/index.html
magrittr(2.0.3) CRAN https://cran.r-project.org/web/packages/
magrittr/index.html
parallelly(1.37.1) CRAN https://cran.r-project.org/web/packages/
parallelly/index.html
| stringr(1.5.0) | CRAN | https://cran.r-project.org/web/packages/ |
| -------------- | ---- | ---------------------------------------- |
stringr/index.html
| tibble(3.2.1) | CRAN | https://cran.r-project.org/web/packages/ |
| ------------- | ---- | ---------------------------------------- |
tibble/index.html
| tidyr(1.3.0) | CRAN | https://cran.r-project.org/web/packages/ |
| ------------ | ---- | ---------------------------------------- |
tidyr/index.html
scProportionTest(0.0.0.9000) GitHub;Milleretal.29 https://github.com/rpolicastro/
scProportionTest
scCustomize(2.1.2) CRAN https://cran.r-project.org/web/packages/
scCustomize/index.html
gprofiler2(0.2.3) CRAN https://cran.r-project.org/web/packages/
gprofiler2/index.html
ggcorrplot(0.1.4.1) CRAN https://cran.r-project.org/web/packages/
ggcorrplot/readme/README.html
htmlwidgets(1.6.4) CRAN https://cran.r-project.org/web/packages/
htmlwidgets/index.html
reshape2(1.4.4) CRAN https://cran.r-project.org/web/packages/
reshape2/index.html
patchwork(1.2.0) CRAN https://cran.r-project.org/web/packages/
patchwork/index.html
| qs(0.26.1) | CRAN | https://cran.r-project.org/web/packages/ |
| ---------- | ---- | ---------------------------------------- |
qs/index.html
| janitor(2.2.0) | CRAN | https://cran.r-project.org/web/packages/ |
| -------------- | ---- | ---------------------------------------- |
janitor/index.html
| future(1.33.0) | CRAN | https://cran.r-project.org/web/packages/ |
| -------------- | ---- | ---------------------------------------- |
future/index.html
| ggraph(2.1.0) | CRAN | https://cran.r-project.org/web/packages/ |
| ------------- | ---- | ---------------------------------------- |
ggraph/index.html
lattice(0.21.8) CRAN https://cran.r-project.org/web/packages/
lattice/index.html
| gridExtra(2.3) | CRAN | https://cran.r-project.org/web/packages/ |
| -------------- | ---- | ---------------------------------------- |
gridExtra/index.html
| grid(4.1.0) | CRAN | https://cran.r-project.org/web/packages/ |
| ----------- | ---- | ---------------------------------------- |
grid/index.html
Other
| FlowmiTMCellStrainers | Bel-Art | Cat#136800040 |
| --------------------- | ------- | ------------- |
EXPERIMENTMODELANDSTUDYPARTICIPANTDETAILS
Humanbladderprocurement
DonortissuewasmadeavailablethrougharesearchcollaborationwithLifebanc,anon-profitorganizationthatcoordinatesorgan
recoveryforuseintransplantationinmorethan80hospitalsinNortheastOhio.Underouragreement,Lifebancscreenspotentialdo-
norsforsuitability,includingcheckingtheapplicabledonorregistrytodetermineifapotentialdonorhasmadeadonordesignationas
recognizedunderapplicablestatelaw.Withfamilyconsent,LifebancofferstheLUTincludingthebladdertousforresearchprocure-
ment.Inthisstudy,onebladderwasprocuredfroma21-year-oldmaledonor,andeightdifferentsampleswereexcised,twofrom
eachmajorbladderregion(Dome,Neck,UreteralOrifice,UreterovesicalJunction).Onesamplefromeachbladderregionwasused
forsinglecelldissociation,andtheothersamplewasusedforsinglenucleusisolation.
e2 iScience28,111628,January17,2025

iScience
ll
Article OPENACCESS
METHODDETAILS
Definitionofbladderregions
Tocomprehensivelysamplebladdercelltypesanddiversityinembryologicorigin,wecollectedtissuesamplesfromthebladder
dome,neck,ureteral orifice (UO),andureterovesical junction (UVJ).Forthepurposes of thisstudy,andbased ontheliterature,
thebladderregionsweredefinedasfollows.Thebladderdome,orapex,wasobtainedfromtheanterosuperiorregionofthebladder
wherethemedialumbilicalligamententers.Thedomerepresentsthedistensiblepartofthebladder,whichaccommodatesurine
duringbladderfillingandexpelsurineduringmicturition.Thebladderneckwasobtainedfromtheconfluenceofthebladderandure-
thrainferiortothetrigone.Itactstofunnelurineintotheurethraduringvoidingandcontainstheinternalurethralsphincter,which
involuntarilycontractsduringstorageandrelaxesduringemptying.Theureteralorificewasobtainedfromthevisibleopeningof
theureterintothebladder.Theureterovesicaljunctionwastakenfromtheareasuperolateraltotheureteralorifice,whichcontains
theintramuralsegmentofureterandastroma-richanti-refluxmechanism.
Singlecellisolation
Understerileconditions(workingentirelywithinBSL2Biosafetycabinets),freshlydissectedhumanLUTtissuesfromeachdesig-
natedanatomiclocationareimmediatelywashedwithPBSandcentrifugedfor5minat1000xg.ThePBSisaspiratedoff,andthe
tissues are transferred to a sterile Petri dish where they are subsequently minced using sterile razor blades until a ‘‘paste-like’’
consistencyisachieved(<5min).ThetissuedigestioniscarriedoutusingthePapainDissociationSystem(WorthingtonBiochem-
ical Corporation) according to the manufactures instructions with minor modifications that were empirically determined and
optimal for human ureter and bladder tissues. Briefly, 5 mL of sterile Earle’s Balanced Salt Solution (EBSS) is added to one
vial of papain and equilibrated at 37(cid:1)C, and 500 mL EBSS is added to one vial of DNase and placed on ice. The minced tissue
is transferred to a 50 mL conical containing 5 mL papain and 500 mL DNase for incubation with shaking (70 rpm) at 37(cid:1)C for
1h.Using a P1000pipette, the tissue is gently pipetted up and down to check for proper digestion. 5.5 mL of ovoid inhibitor is
thenaddedtothetissuesuspensiontostopthedigestion.Themixtureisfilteredbypassingtheentirevolume((cid:3)11mL)through
a70mmcapfiltertoremovelargedebris.Thecellsuspensionissubsequentlycentrifugedat1000rpmfor5mintopelletcells,and
thesupernatantisdiscarded.Thecellpelletisgentlyre-suspendedin3mLACKlysisbufferandincubatedatroomtemperature
for3mintoremoveredbloodcells.Thecellsarethencentrifugedat1000rpmfor5min,washedwithanother5mLPBS,andre-
suspended in a volume of PBS appropriate for the cell pellet size. The re-suspended cells are then passed through a 40 mm
FLOWMI cell strainer and counted with trypan blue to note cell viability. The final cell concentration is recorded. An aliquot of
cellsuspensionfor10XGEMgenerationisthenpreparedaccording tothecellsuspensionvolumecalculatortableoftheChro-
miumNextGEM SingleCell30 Reagent Kitsv3.1userguide.
Singlenucleusisolation
Dissectedbladderregionswereembeddedinoptimalcuttingtemperature(O.C.T.)compound,snapfrozenwithdryice,andstored
at(cid:4)80(cid:1)Cuntiluse.WefollowedtheprotocolestablishedbytheKidneyPrecisionMedicineConsortium(KPMP)fornucleiisolation.4
Briefly,wecutten40mm-thickcryosectionsandplacedtissuesectionsinto1mLofice-coldnuclearextractionbuffer(NEB,20mM
TrispH8.0,329mMsucrose,5mMCaCl ,3mMMgAc ,0.1mMEDTA,0.1%TritonX-100with0.1%RNaseInhibitor).Usingap1000
2 2
pipettewiththetiptrimmedtoincreaseboresize,thetissuemixturewaspipettedupanddownatleast20timestodissolvetheO.C.T.
Themixturewasfurthermixedbypipettingupanddown10timesusingaregular,untrimmedp1000pipetteandthentransferredtoa
Douncehomogenizeronice.Thetissuewashomogenizedoniceusing5strokeswithpestleAfollowedby20strokeswithpestleB,
takingcaretominimizebubbleformation.Thehomogenizedmixturewasincubatedonicefor10minandthenpassedthrougha
40 mm FLOWMI cell strainer into a new 15 mL conical tube. The sample volume was brought up to 10 mL with ice-cold PBSE
(1xPBS,1mLEGTA)andcentrifugedat900gfor10minat4(cid:1)Ctopelletthenuclei.Finally,thenucleiwereresuspendedinice-
coldPBSEcontaining1%BSAformanualcounting.
Sampleprocessingandlibrarypreparation
Forbothsinglecellandsinglenucleusdata,weused10XGenomicsChromiumSingleCell30 ReagentsKitversion3.1.Wetar-
getedtorecover10,000cells/nucleipersampleunlessagivensamplehadfewerthan10,000totalcells/nuclei.Allsampleshad
>5,000cells/nuclei capturedforlibrarygenerationandsequencing.Followingthe10Xprotocol,weaddedthesingle-cell/single-
nucleussuspension,thegelbeads,andtheemulsionoiltothe10XGenomicsSingleCellChipGandrantheChromiumController.
Immediatelyfollowingthedropletgeneration,samplesweretransferredtoaPCR8-tubestrip(USAscientific),andreversetran-
scriptionwasperformedusingSimpliAmpthermalcycler(AppliedBiosystems).Followingreversetranscription,cDNAwasrecov-
eredusingtherecoveryreagentprovidedby10XGenomics.ThecDNAwascleanedupusingtheSilaneDynaBeadsaccordingto
the 10X Genomics user guide. The purified cDNA was amplified for 11 cycles and subsequently cleaned up using SPRIselect
beads(BeckmanCoulter).TodeterminethecDNAconcentrations,1:10dilutionofeachsamplewasanalyzedonanAgilentBio-
analyzerHighSensitivitychip.ThecDNAlibrarieswereconstructedaccordingtotheChromiumSingleCell30ReagentKitversion
3.1userguide.
iScience28,111628,January17,2025 e3

iScience
ll
OPENACCESS Article
scRNA-seqandsnRNA-seqdatajointanalysis
ForbothscRNAseq and snRNAseq samples, librarieswere pooled and sequencedto atarget depthof 50,000read pairs per
cell.De-multiplexedFASTQfileswereprocessedwithCellRanger(v7.1.0),wherereadsweremappedusingthecountpipeline
withthepre-builtreferencegenomerefdatagex-GRCh38-2020AandGTFfromGENECODEv32(GRCh28.p13).Summarysta-
tisticsforeachsample’salignmentperformancehavebeenprovidedinTableS1.Thedownstreamanalysiswasperformedus-
ingSeurat4.3.0.1inR25alongwithanestablishedRanalysispipeline.21Therawdata,comprisingof114,580cells(n=96,604
cells and n = 17,976 nuclei), was filtered for low-quality cells using QC thresholds determined by assessing the distribution
plots. Briefly, cells with mitochondrial reads >25% of total mapped reads, gene counts <500 or >12,000, and total mapped
readcounts<4,000werefilteredout,leaving40,097high-qualitycells(n=31,764cellsandn=8,333nuclei)forthedownstream
analysis.Seurat’sstandardworkflowwasfollowed.Datawereintegrated,orbatchcorrected,usingCCAandtheIntegrateData
functionality.Next,usingthe2,000mostvariablegenes,principalcomponents(PCs)werecomputed,andthefirst30PCswere
utilized to generate clustering at a resolution 0.25. Cell clusters were visualized using UMAP and annotated by marker gene
expression.Clusterlevelsimilaritywasassessedbycalculatingclustercorrelations(Pearson’s)basedonthetop2000variable
genes, which grouped the clusters into 3 major compartments – urothelial, stromal, and immune. Subset analysis for each
compartment was performed using the same Seurat workflow. Clustering optimization was performed using clustree and
chooseR.30,31
scRNA-seqandsnRNA-seqsubsetanalysis
Foreachsubsetanalysis,cellsfromclustersassignedtoagivencompartment(immune,stromal,orurothelial)wereprocessed
by the same analysis pipeline as described above, starting from raw gene counts. The subsets were subjected to additional
filtering and re-processing until any cross-compartment contamination was sufficiently removed. Potentially contaminating
clusters (e.g., suspected doublets) were removed ‘If the top100 differential marker list of a given cluster shows markers that
shouldbeexclusivelyexpressedbycellsofanothercompartment(e.g.,PDGFRAappearsamongtop100markersinanimmune
subsetcluster)’AND‘thecontaminatingmarkerisexpressedin>10%ofcellsinthatcluster’.Ifsuchparametersexist,thesub-
set was clustered usingthese parameters andsubjected to the same subset analysis workflow, while excludingthe contami-
natingcluster(s).Thisresultedin2,094immunecells(n=1,725cellsandn=369singlenuclei),12,964stromalcells(n=7,227
cellsandn=5,737singlenuclei),and14,776urothelialcells(n=13,279cellsandn=1,497singlenuclei).Eachsubsetdatawas
thenclusteredusing50PCsandaresolutionof0.4forimmune,40PCsandaresolutionof0.3forstromal,and25PCsanda
resolution of 0.1 for urothelial.
Foreachcompartment(immune,stromal,andurothelial),celltypeswerecalledusingcanonicalandestablishedmarkers.Thepro-
portionofsinglecellandsinglenucleusenrichmentforeachcellclusterwasthencomputedandstatisticalsignificance(p<0.05)was
assessedusingscProportionTest.29Asummaryofcellcounts,single-cellandsingle-nucleusenrichment,anddifferentialexpression
analysisforeachcelltypeisprovidedinTableS2.
scRNA-seqv.snRNA-seqgenesetanalysis
Whenbothsinglecellsandsinglenucleiwerepresentinsufficientnumbers(n>50each),weaimedtoassessthedifferentialgene
expressionofthesetwodatatypesforeachcapturedcelltype.Foreachcelltypecluster,whenapplicable,thesingle-cellandsingle-
nucleussubpopulationsweresubset,andthedifferentialgenelistforeachwasfoundusingSeurat’sFindMarkersfunction.Here,the
single-cell(orsingle-nucleus)subpopulation’sexpressionwascomparedagainsttheexpressionofthesingle-cell(orsingle-nucleus)
subpopulationofallothercelltypeswithinthecompartment(e.g.,immune).Theupregulatedmarkerswerefilteredineachlistusinga
thresholdofLog2FC>1.5andadjustedp-value(q)<0.05.GeneOntology(GO)enrichmentanalysisforeachcluster’ssingle-celland
single-nucleusgenelistwasperformedusinggprofiler2,andgeneontologybiologicalprocess,molecularfunctions,andcellcom-
ponents were recorded.32 We annotated each gene in Tables S3 and S4 with its GENCODE biotype information (https://www.
gencodegenes.org/pages/biotypes.html).Todeterminewhethernon-codingRNAenrichmentwasstatisticallysignificantinapartic-
ularcellanddatatype,wecompletedchi-squaretestsforassociationbetweentwocategoricalvariables,wherethe2x2tablewas
comprisedofthenumberofnon-codingRNAsandproteincodinggenesforaspecificcelltypecomparedbetweensinglecelland
singlenucleusgenelists(TableS5).
IndependentscRNA-seqandsnRNA-seqanalysis
Weanalyzedthesinglecellandsinglenucleusdataindependentlyfollowingidenticalanalysisworkflowasdescribedabove.Briefly,
thealignedsingle-cellorsingle-nucleusdatawerefilteredforhighqualitycells/nuclei,integrated,andclusteredwithoptimization.
Clusters belonging to the stromal, immune, and urothelial compartments were identified, and the cells/nuclei belonging to each
compartment were subset. For each compartment, cells/nuclei were reintegrated, and clustering optimization was completed.
Onlythestromalcompartmentcontainedrobustnumbersofbothcellsandnucleiformeaningfulcelltypeidentificationanddiffer-
entialgeneexpressionanalysis.
e4 iScience28,111628,January17,2025

iScience
ll
Article OPENACCESS
QUANTIFICATIONANDSTATISTICALANALYSIS
The proportionality of single cell or single nucleus subpopulations was assessed using scProportionTest, and significance was
definedatFDR<0.05andabs(Log2FC)>0.58.DifferentialexpressionanalysiswascompletedusingtheSeuratFindMarkerfunction
set to the default Wilcoxon Rank-Sum test. Significant differentially expressed genes were identified by filtering for an ab-
s(Log2FC)>1.5andq<0.05.Chi-squaretestsforassociationbetweentwocategoricalvariableswereusedtodeterminewhether
non-codingRNAenrichmentwasstatisticallysignificantinaparticularcellanddatatype,withsignificancesetatp<0.05.
iScience28,111628,January17,2025 e5