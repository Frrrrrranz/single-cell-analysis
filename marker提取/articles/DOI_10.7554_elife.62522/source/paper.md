RESEARCHARTICLE
Single-cell multiomic profiling of human
lungs reveals cell-type-specific and age-
dynamic control of SARS-CoV2 host genes
Allen Wang1†*, Joshua Chiou2,3†, Olivier B Poirion1†, Justin Buchanan1†,
Michael J Valdez2,3†, Jamie M Verheyden3, Xiaomeng Hou1, Parul Kudtarkar3,
Sharvari Narendra3, Jacklyn M Newsome3, Minzhe Guo4,5, Dina A Faddah6,
Kai Zhang7, Randee E Young3,8, Justinn Barr3, Eniko Sajti3, Ravi Misra9,
Heidie Huyck9, Lisa Rogers9, Cory Poole9, Jeffery A Whitsett4,5, Gloria Pryhuber9,
Yan Xu4,5, Kyle J Gaulton3*, Sebastian Preissl1*, Xin Sun3,10*,
NHLBI LungMap Consortium11
1Center for Epigenomics & Department of Cellular & Molecular Medicine, University
of California, San Diego, San Diego, United States; 2Biomedical Sciences Graduate
Program, University of California San Diego, La Jolla, United States; 3Department of
Pediatrics, University of California-San Diego, La Jolla, United States; 4Division of
Neonatology, Perinatal and Pulmonary Biology, Cincinnati Children’s Hospital
Medical Center, Cincinnati, United States; 5Divisions of Pulmonary Biology and
Biomedical Informatics, University of Cincinnati College of Medicine, Cincinnati,
United States; 6Vertex Pharmaceuticals, San Diego, United States; 7Ludwig Institute
for Cancer Research, La Jolla, United States; 8Laboratory of Genetics, Department
of Medical Genetics, University of Wisconsin-Madison, Madison, United States;
9Department of Pediatrics and Clinical & Translational Science Institute, University
of Rochester Medical Center, Rochester, United States; 10Department of Biological
*Forcorrespondence:
a5wang@health.ucsd.edu(AW); Sciences, University of California-San Diego, La Jolla, United States; 11NIH,
kgaulton@health.ucsd.edu(KJG); Bethesda, United States
spreissl@health.ucsd.edu(SP);
xinsun@health.ucsd.edu(XS)
†Theseauthorscontributed
equallytothiswork Abstract RespiratoryfailureassociatedwithCOVID-19hasplacedfocusonthelungs.Here,we
presentsingle-nucleusaccessiblechromatinprofilesof90,980nucleiandmatchedsingle-nucleus
Competinginterest:See
transcriptomesof46,500nucleiinnon-diseasedlungsfromdonorsof~30weeksgestation,~3years
page21
and~30years.Wemappedcandidatecis-regulatoryelements(cCREs)andlinkedthemtoputative
Funding:Seepage22 targetgenes.WeidentifieddistalcCREswithage-increasedactivitylinkedtoSARS-CoV-2host
Received:27August2020
entrygeneTMPRSS2inalveolartype2cells,whichhadimmuneregulatorysignaturesandharbored
Accepted:08November2020 variantsassociatedwithrespiratorytraits.Atthe3p21.31COVID-19risklocus,acandidatevariant
Published:09November2020 overlappedadistalcCRElinkedtoSLC6A20,ageneexpressedinalveolarcellsandwithknown
functionalassociationwiththeSARS-CoV-2receptorACE2.Ourfindingsprovideinsightinto
Reviewingeditor: EdwardE
regulatorylogicunderlyinggenesimplicatedinCOVID-19inindividuallungcelltypesacrossage.
Morrisey,Universityof
Pennsylvania,UnitedStates Morebroadly,thesedatasetswillfacilitateinterpretationofrisklociforlungdiseases.
CopyrightWangetal.This
articleisdistributedunderthe
termsoftheCreativeCommons Introduction
AttributionLicense,which
Amidst the ongoing COVID-19 pandemic, understanding how SARS-CoV-2 infects and impacts the
permitsunrestricteduseand
redistributionprovidedthatthe lungs has become an urgent priority. Not only do the lungs act as a critical barrier that protects
originalauthorandsourceare against inhaled pathogens such as viruses, it is also a site of many COVID-19 symptoms including
credited. theprimarycauseofCOVID-19mortality,acuterespiratorydistresssyndrome(ARDS).Thelungsare
Wang,Chiou,Poirion,etal.eLife2020;9:e62522.DOI:https://doi.org/10.7554/eLife.62522 1of28

Researcharticle DevelopmentalBiology GeneticsandGenomics
composed of an elaborate airway tree that conducts air to and from the alveoli, the gas-exchange
units. In an average human adult lungs, an estimated 480 million alveoli give rise to approximately
140 m2 of gas-exchange surface area (Ochs et al., 2004). Airway and alveolar epithelium constitute
the respiratory barrier that is exposed to inhaled pathogens. Respiratory epithelial cells are at the
frontline of infection, although some pathogens that have bypassed the barrier can infect other cell
types. The human airway epithelium is composed of luminal cells and basal cells (Tata and Rajago-
pal, 2017). Luminal cells include club cells and goblet cells that moisturize the air and trap patho-
gens, as well as ciliated cells that sweep out inhaled particles. These luminal cells are underlined by
basalcells,whichserveasprogenitorswhenluminalcellsarelostafterinfection(Hoganetal.,2014;
Kim, 2017). The alveolar epithelium is composed of alveolar type 1 cells (AT1s), which are flat and
line the gas–blood interface to facilitate gas exchange; and alveolar type 2 cells (AT2s), which pro-
duce surfactant to reduce surface tension and protect against pathogens (Whitsett and Weaver,
2015). While SARS-CoV-2 likely infects both the airway and alveolar regions of the lungs, it is the
damagetothealveolarregionthatcausesARDS(Duetal.,2020).
There are several large-scale studies, including efforts from LungMap and the Human Cell Atlas,
whichaimtodefinecelltypeswithinthehumanlungsusingsingle-celltranscriptomicsasthecentral
modality (Reyfman et al., 2019; Schiller et al., 2019; Travaglini et al., 2020; Xu et al., 2016). In
contrast, there isapaucity ofsingle-celldata focusedonmapping cis-regulatory elements (CREs)in
the human genome that are active in specific lung cell types. CREs associate with combinations of
transcription factors to drive spatiotemporal patterns of gene expression (Moore et al., 2020) and
enablecell-specificresponsestointra-andextra-cellularsignals,forexample,aging(BoothandBru-
net, 2016) and inflammation (Smale and Natoli, 2014). Furthermore, complex disease-associated
variants identified in genome-wide association studies (GWAS) are enriched in CREs
(Mauranoetal.,2015;Pickrell,2014).Therefore,acomprehensiveatlasofcell-typeresolvedCREs
in the human lungs will facilitate investigation of the gene regulatory mechanisms responsible for
lungcell-typeidentity,function,androleinbiologicalprocessessuchasviralentry,aswellasuncov-
eringtheeffectsofgeneticvariationoncomplexlungdisease.
Accessible or ‘open’ chromatin is a hallmark of CREs and can be used to localize candidate cis-
regulatoryelements(cCREs).Chromatinaccessibilitycanbeassayedusing‘bulk’or‘ensemble’tech-
niquessuchasDNase-seqandATAC-seq(Buenrostroetal.,2013;Thurmanetal.,2012).Toover-
come limitations regarding tissue heterogeneity inherent in such assays, technologies such like
single-cell ATAC-seq have been developed to map the epigenome and gene regulatory programs
within component cell types (Buenrostro et al., 2015; Chen et al., 2018; Cusanovich et al., 2015;
Cusanovich etal., 2018;Lareau et al., 2019;Satpathy et al., 2019). Accessible chromatin profiles
derivedfromsinglecellscanelucidatecell-type-specificcCREs,transcriptionalregulatorsdrivingele-
ment activity, and putative target genes linked to distal cCREs through single-cell co-accessibility
(Cusanovich et al., 2018; Lareau et al., 2019; Pliner et al., 2018; Preissl et al., 2018;
Satpathy et al., 2019). Importantly, human sequence variants affecting complex traits and diseases
are enriched in non-coding sequences (Maurano et al., 2015; Pickrell, 2014). Thus, cell-type-spe-
cificprofiles derivedfromsingle-cellchromatin accessibilitydata canhelpprioritizethe celltypes of
actionandfunctionofthesevariants(Chiouetal.,2019;Corcesetal.,2020).
EpidemiologydataofUScasesreportedbytheCDChasconsistentlydemonstratedthattherate
ofhospitalization ordeath fromCOVID-19 issignificantly loweramong childrencompared to adults
or elderly individuals, amidst caution that children can still be infected and transmit the virus
(CDC,2020a;CDC,2020b).Therearelikelymanyreasonsthatunderlietheage-associateddifferen-
ces, including different expression levels of viral entry proteins and different immune resilience to
viralinfection.Definingthemechanismunderlyingtheapparentreducedsusceptibilityofchildrento
COVID-19willinformhowwecantransferthisadvantagetoadultandelderlypopulations.
Both in silico structural modeling and biochemical assays have implicated several key host pro-
teinsforSARS-CoV-2infection.ACE2hasbeendemonstratedasthereceptorfornotonlytheorigi-
nal SARS-CoV, but also SARS-CoV-2 (Hoffmann et al., 2020; Lan et al., 2020; Yan et al., 2020).
Based on literature from the original SARS-CoV as well as emerging data from SARS-CoV-2,
TMPRSS2andCTSLcleavetheviralspikeprotein,therebyfacilitatefusionoftheviruswithhostcells
(Huanget al.,2006;Matsuyamaetal.,2020;Reinke etal.,2017;Wallsetal., 2020;Zhou etal.,
2016).Inparticular,TMPRSS2hasbeenshowntobeessentialforcoronavirusviralentrywhileCTSL
is dispensable (Hoffmann et al., 2020; Shirato et al., 2018; Zhou et al., 2015). BSG encodes
Wang,Chiou,Poirion,etal.eLife2020;9:e62522.DOI:https://doi.org/10.7554/eLife.62522 2of28

Researcharticle DevelopmentalBiology GeneticsandGenomics
anotherreceptorthatcanbindtotheSARS-CoVspikeprotein(Chenetal.,2005)andFURINenco-
des a protease with a putative target site in SARS-CoV-2, adding both genes to the list of host
machineryhighjackedbythevirus(Coutardetal.,2020;Wallsetal.,2020).Inthisstudy,wefocus
onthegenesencodingthesefiveproteins,ACE2,TMPRSS2,CTSL,BSG,andFURIN,anddetermine
theirexpressionandassociatedcis-regulatorylandscapeatsingle-cellresolutioninthenon-diseased
humanlungs.
Tocontributetoourunderstandingofgeneregulationinthehumanlungsduringagingandhow
suchregulationgoesawryandcontributestodisease,includingSARS-CoV-2infection,wegenerated
donor-matched single-nucleus RNA-seq and single-nucleus ATAC-seq data across neonatal, pediat-
ric,andadultlungswiththreedonorsineachgroup.Usingthesedatasets,weprofiledgeneexpres-
sion dynamics at cell-type resolution of SARS-CoV-2 host entry genes ACE2, TMPRSS2, CTSL, BSG,
and FURIN and revealed cCREs underlying these changes for ACE2 and TMPRSS2, genes that
encode theprimary receptor and fusion protein. We further profiled non-coding sequence variation
in cCREs associated with TMPRSS2 that may impact regulatory activity and might contribute to dif-
ferentialsusceptibilitytoSARS-CoV-2infectionbyaffectingTMPRSS2expression.Finally,wedemon-
strated the value of this resource in interpreting emerging genetic risk of respiratory failure in
COVID-19byannotatingtherecentlyidentified3p21.31locus(Ellinghausetal.,2020).
Results
Single-nucleus accessible chromatin and transcriptional profiles from
neonatal, pediatric, and adult human lung tissues
To generate an age and cell-type resolved atlas of chromatin accessibility and gene expression in
thehumanlungs,weperformedsingle-nucleusATAC-seq(snATAC-seq)andsingle-nucleusRNA-seq
(snRNA-seq) on non-diseased lung tissue sourced from the NIH funded LungMap Human Tissue
Core. Tissue samples spanned three donor age groups: ~30-week-old gestational age (GA, prema-
turelyborn,30wkGA),~3-year-old(3yo),and~30-year-old(30yo)(metadatainSupplementaryfile1).
After batch correction and filtering of low-quality nuclei and likely doublets, we clustered and ana-
lyzedatotalof90,980single-nucleusaccessiblechromatinprofiles(Figure1A,andFigure1—figure
supplement 1A–D, Supplementary file 2). We identified 19 clusters representing epithelial (AT1-
alveolar type 1, AT2-alveolar type 2, club, ciliated, basal, and pulmonary neuroendocrine), mesen-
chymal (myofibroblast, pericyte, matrix fibroblast 1, and matrix fibroblast 2), endothelial (arterial,
lymphatic, capillary 1 and capillary 2), and hematopoietic cell types (macrophage, B-cell, T-cell, NK
cell, and enucleated erythrocyte) (Figure 1A). Supporting these cluster annotations, we observed
cell-type-specific patterns of chromatin accessibility at known marker genes for each cell type
(Figure1B,andFigure1—figuresupplement2A).Wesimilarlyclusteredthe46,500single-nucleus
transcriptomes, which passed QC criteria from the donor and sample-matched snRNA-seq data
(Figure 1C, and Figure 1—figure supplement 1E–H, Supplementary file 2). These clusters repre-
sented all major cell types in the small airway region of the lungs (Figure 1C,D, and Figure 1—fig-
ure supplement 2B). Importantly, these clusters overlapped those identified from snATAC-seq,
highlightedbyaclusterofrarepulmonaryneuroendocrinecells(PNECs)representedinbothmodali-
ties(Figure1A–D,Figure1—figuresupplement2A,B).
Cell-type-specific expression and regulation of SARS-CoV-2 host cell
entry genes
To gain insight into how viral entry is regulated in host cell types, we set out to identify the CREs
predicted to regulate SARS-CoV-2 cell entry factors and to pinpoint the cell types in which they
exert their effects. Toward this goal, we first identified the discrete cell types that express ACE2,
TMPRSS2, CTSL, BSG, and FURIN. We detected ACE2 transcript in very few nuclei (total 80 nuclei)
in the normal lungs and these nuclei were enriched within the epithelial lineage (Figure 2A, Fig-
ure 2—figure supplement 1A, Supplementary file 3). This is consistent with exceptionally low
ACE2 expression in multiple tissues analyzed in recent publications (Muus et al., 2020; Qi et al.,
2020;Sungnaketal.,2020;Zhaoetal.,2020;Ziegleretal.,2020;Zouetal.,2020).Inourdata,
AT2 cells had the highest number of ACE2+ nuclei, accounting for 48.8% of all ACE2-expressing
nuclei (39 out of total 80 ACE2+ nuclei) (Figure 2—figure supplement 1A, Supplementary file 3).
Wang,Chiou,Poirion,etal.eLife2020;9:e62522.DOI:https://doi.org/10.7554/eLife.62522 3of28

Researcharticle DevelopmentalBiology GeneticsandGenomics
Figure1.Single-nucleusatlasofchromatinaccessibilityandtranscriptomesinthehumanlungs.(A)UMAP(UniformManifoldApproximationand
Projection)embedding(McInnesetal.,2018)andclusteringresultsofsnATAC-seqdatafrom90,980single-nucleuschromatinprofilesfromten
donors:prematureborn(30weekGAforgestationalage,n=3),4-month-old(n=1),threeyo(n=3)and30yo(n=3).Forlibraryqualitycontrolsee
Figure1—figuresupplement1A–D.(B)DotplotofmarkergenesfromsnRNA-sequsedforclusterannotation.ForadditionalgenesseeFigure1—
figuresupplement2A.(C)UMAPembedding(McInnesetal.,2018)andclusteringresultof46,500snRNA-seqdatafromninedonors:premature
born(30weekGA),threeyo,30yo,n=3pertimepoint,identifies31clusters.Eachdotrepresentsanucleus.Spread-outgraydotscorrespondtonuclei
ofunclassifiedcells.ForlibraryqualitycontrolseeFigure1—figuresupplement1E–H.(D)DotplotofmarkergenesfromsnRNA-sequsedforcluster
annotation.ForadditionalgenesseeFigure1—figuresupplement2B.
Theonlineversionofthisarticleincludesthefollowingfiguresupplement(s)forfigure1:
Figuresupplement1.QualitycontrolofsnATAC-seqandsnRNA-seqdatasets.
Figuresupplement2.Expressionandchromatinaccessibilityatmarkergenelociusedforannotation.
Wang,Chiou,Poirion,etal.eLife2020;9:e62522.DOI:https://doi.org/10.7554/eLife.62522 4of28

Researcharticle DevelopmentalBiology GeneticsandGenomics
Figure2.snATAC-seqanalysisofhumanlungsrevealscandidatecis-regulatoryelementsforACE2andTMPRSS2.(A)Dotplotillustratingcluster-
specificgeneexpressionofcandidateSARS-CoV-2cellentrygenes.Forviolinplotsillustratingcluster-specificgeneexpressionpleaseseeFigure2—
figuresupplement1A–E.(B)Dotplotillustratingcluster-specificgenebodychromatinaccessibilityofcandidateSARS-CoV-2cellentrygenes.(C)
Unionsetofpeaks(verticallines)identifiedinallclusterssurroundingACE2and15peaksthatshowedco-accessibilitywiththeACE2promoter(red
lines,co-accessibilityscore>0.05)viaCicero(Cusanovichetal.,2018).(D)ZoomintoACE2locusandgenomebrowsertracksofsnATAC-seqsignal
(Robinsonetal.,2011).ACE2promoterregionhighlightedbyredbox.(E)Unionsetofpeaks(verticallines)identifiedinallclusterssurrounding
TMPRSS2and73peaksthatshowedco-accessibilitywiththeTMPRSS2promoter(redlines,co-accessibilityscore>0.05)viaCicero(Cusanovichetal.,
2018).(F)ZoomintoTMPRSS2locusandgenomebrowsertracksofsnATAC-seqsignal(Robinsonetal.,2011).TMPRSS2promoterregionhighlighted
byredbox.ForgenomebrowsertracksofBSG,FURIN,CTSLpleaseseeFigure2—figuresupplement1F.
Figure2continuedonnextpage
Wang,Chiou,Poirion,etal.eLife2020;9:e62522.DOI:https://doi.org/10.7554/eLife.62522 5of28

Researcharticle DevelopmentalBiology GeneticsandGenomics
Figure2continued
Theonlineversionofthisarticleincludesthefollowingfiguresupplement(s)forfigure2:
Figuresupplement1.GeneexpressionandchromatinaccessibilityforSARS-COV-2cellentrygenes.
Incomparison,TMPRSS2transcriptsweredetectedinmanymorecells(total6547nuclei,Figure2A,
Figure2—figuresupplement1B,Supplementaryfile3).MostTMPRSS2-expressingcellswereepi-
thelial cells including AT1 and AT2 cells and airway cells such as club, ciliated and goblet cells
(Figure 2A, Figure 2—figure supplement 1B, Supplementary file 3). Within the AT2 population,
TMPRSS2 was detected in 3,315/7,226 nuclei, or 45.8% of the AT2 cells (Figure 2—figure supple-
ment 1B). Importantly, 21 of the 39 ACE+ AT2 cells also expressed TMPRSS2 (Supplementary file
3). The other three candidate genes of SARS-CoV-2 host cell entry CTSL, BSG and FURIN were
expressedinalargenumberofAT1,AT2,matrixfibroblast1,2,andM1macrophagecells,aswellas
a small number of cells in additional cell types (Figure 2A, Figure 2—figure supplement 1C–E,
Supplementaryfile3).
We next assessed cell-type resolved chromatin accessibility at candidate SARS-CoV-2 entry
genes. Consistent with their gene expression, both ACE2 and TMPRSS2 were primarily accessible
throughouttheirgenebodyinalveolarcellssuchasAT1,AT2,andairwaycellssuchasclub,ciliated,
andbasalcells(Figure2B).Conversely,theCTSLgenebodyexhibitedchromatinaccessibilityacross
epithelialcells,mesenchymalcells,endothelialcells,andmacrophages(Figure2B,Figure2—figure
supplement 1F). BSG and FURIN alsoshowed broadchromatin accessibilitypatterns with the high-
est activity in endothelial cells, such as capillaries (Figure 2B, Figure 2—figure supplement 1F).
Together,bothgeneexpressionandchromatinaccessibilitysuggestthatamongcelltypesconstitut-
ing the barrier exposed to inhaled pathogens, both the airway and alveolar epithelial cells express
genescriticalforSARS-CoV-2entry.
Cell-type-specific expression profiles are largely established by distal CREs such as enhancers
(ENCODEProjectConsortium,2012;Mooreetal.,2020;Kundajeetal.,2015).ToidentifycCREs
predicted to control cell-type-restricted expression of the SARS-CoV-2 viral entry genes, we first
aggregated nuclei within each cell type. We then called accessible chromatin sites from the aggre-
gated profiles using MACS2 (Zhang et al., 2008). Overall, we mapped 398,385 cCREs across all
lung cell types. Distal cCREs can be linked to putative target genes by measuring co-accessibility
withpromoterregions,asithasbeenshownthatco-accessiblesitestendtobeinphysicalproximity
in the nucleus (Pliner et al., 2018). As such, we identified sites co-accessible with the ACE2,
TMPRSS2, CTSL, FURIN, and BSG promoters using a modified implementation of Cicero
(Plineretal.,2018).AttheACE2locus,weidentified15sitesco-accessiblewiththeACE2promoter
(Figure2C,D,Supplementaryfile4).Wespeculatethatthemodestnumberofco-accessiblesitesis
likely due to the small percentage of ACE2+ nuclei (Figure 2A, Figure 2—figure supplement 1A).
Incomparison,attheTMPRSS2locus,weidentified73accessiblechromatinsitesco-accessiblewith
the TMPRSS2 promoter (Figure 2E,F, Supplementary file 4). Finally, at the CTSL, FURIN, and BSG
lociweidentified73,213,and64accessiblechromatinsitesco-accessiblewiththeirrespectivegene
promoters(Supplementaryfile4).Thiscollectionofcell-typeresolvedcCREsassociatedwithSARS-
CoV-2 host genes (Supplementary file 4) will be crucially important for follow-up studies to deter-
minehowhostcellgenesareregulatedandhowgeneticvariationwithintheseelementscontributes
toinfectionrateanddiseaseoutcomes.
CREs linked to TMPRSS2 are part of an age-related regulatory program
in AT2 cells
AT2cellsareanabundantepithelialcelltypeinthealveolarregionofthelungswhereCOVID-19dis-
rupts respiration. Consequently, we focused on AT2 cells to evaluate viral entry gene dynamics
across donor age groups (Figure 3). We observed a higher fraction of AT2 cells expressing ACE2
and TMPRSS2 in adult lungs as compared to pediatric samples in our small cohort (n = 3 per age
group,Figure3A,B).Notably,theseobservedage-relatedincreaseinexpressionofthesetwogenes
is consistent with findings from a parallel report spearheaded by the Human Cell Atlas (HCA) that
included pediatric data as part of a large-scale meta-analysis (Muus et al., 2020; Schuler et al.,
2020). In contrast to the percentage of AT2 cells expressing these genes, the expression levels per
Wang,Chiou,Poirion,etal.eLife2020;9:e62522.DOI:https://doi.org/10.7554/eLife.62522 6of28

Researcharticle DevelopmentalBiology GeneticsandGenomics
Figure3.Age-increasinggeneexpressionandaccessiblechromatininAT2cellsexhibitssignaturesofimmuneregulationandharborsTMPRSS2-linked
sitesofchromatinaccessibility.(A)DifferentialanalysiswasperformedonAT2cellsbetweenthreeageswithreplicates(n=3perstage).(B)Fractionof
AT2cellswithexpressionofACE2(left)andTMPRSS2(right)in30wkGA,3yoand30yohumanlungsamples.Alldataarerepresentedasmean±SD.p
valuesderivedfromunpaired,two-tailedt-tests.ForexpressiondataofBSG,CTSL,FURINpleaseseeFigure3—figuresupplement1A.(C)Log
Figure3continuedonnextpage
Wang,Chiou,Poirion,etal.eLife2020;9:e62522.DOI:https://doi.org/10.7554/eLife.62522 7of28

Researcharticle DevelopmentalBiology GeneticsandGenomics
Figure3continued
normalizedexpressionofTMPRSS2inAT2cells.DisplayedaremedianexpressionvaluesforAT2cellsinindividualsampleswithatleast1UMI(unique
molecularidentifier).(D)DifferentialanalysiswasperformedonAT2cellsusingpairwisecomparisonsbetweenthreeageswithreplicates(n=3per
stage).(E)K-meansclusteranalysis(K=5)ofrelativeaccessibilityscores(seeMaterialsandmethods)for22,845age-dynamicpeaks(FDR<0.05,
EdgeR)(Robinsonetal.,2010)inAT2cells.ClustersIIIandIVshowincreasingaccessibilitywithageandcontainnineTMPRSS2-co-accessiblesites.(F)
GREAT(McLeanetal.,2010)analysisofelementsingroupcIII(leftpanel)andcIV(rightpanel)showsenrichmentofimmune-relatedgeneontology
terms.(G)TranscriptionfactormotifenrichmentanalysisofelementsincIIIandcIV.(H)K-meansclusteranalysis(K=6)ofTMPRSS2-co-accessiblesites
basedontherelativepercentageofAT2cellswithatleastonefragmentoverlappingeachpeak.Redbarsindicatedynamicpeaksidentifiedfrompair-
wisedifferentialanalysis(FDR<0.05,EdgeR)(Robinsonetal.,2010).(I)LocusrestricteddifferentialanalysisofTMPRSS2-linkedpeakswithincreased
accessibilityinAT2withage(toppanelin3H).Dataarerepresentedasmean±SD.Blackasterisk,p<0.05(independentt-test);Redasterisk,FDR<0.05
(EdgeR)(Robinsonetal.,2010)fromdynamicpeakanalysis.ForadditionalsitesandpromoteraccessibilityofTMPRSS2pleaseseeFigure3—figure
supplement1B,C.(J)GenomebrowserrepresentationoffourTMPRSS2-linkedpeaksacrossagegroups(Robinsonetal.,2011).
Theonlineversionofthisarticleincludesthefollowingsourcedataandfiguresupplement(s)forfigure3:
Sourcedata1.NormalizedexpressionvaluesforTMPRSS2inAT2cells.
Figuresupplement1.GeneexpressionofadditionalSARS-COV-2cellentrygenesandchrmatinaccessibilityofpeaklinkedtoTMPRSS2duringaging.
nucleus were similar across different age groups for either ACE2 (no nucleus had >1 UMI detected)
orTMPRSS2(Figure3C).Notably,wedidnotobserveanage-relatedtrendfortheothercandidate
viralentrygenesBSG,CTSL,FURIN(Figure3—figuresupplement1A).
WenextleveragedoursnATAC-seqdatatoidentifycCREspredictedtocontrolcell-type-specific
and age-related gene expression of SARS-CoV-2 cell entry genes. We focused on TMPRSS2 as it is
essential for coronavirus entry into host cells (Hoffmann et al., 2020; Shirato et al., 2018;
Zhouetal.,2015).ComparedtoACE2,TMPRSS2wasdetectedinsufficientnumberofcellstoallow
uspowertoaddressitsregulation.HavingidentifiedcCREspredictedtoregulateTMPRSS2expres-
sion (Figure 2E,F), we speculated that some of these sites could modulate the age-associated
increase of TMPRSS2 expressing AT2 cells (Figure 3B). To examine this in an unbiased fashion, we
first identified genome-wide chromatin sites in AT2 cells that show dynamic accessibility across
donor age groups. We tested all possible pairwise age comparisons between AT2 signal from each
ofthethreegroupsof30wkGA,3yo,and30yodonorswhileaccountingfordonortodonorvariability
(Figure 3D, see Materials and methods). Overall, we identified 22,745 age-linked sites in AT2 cells,
which exhibitedsignificant differences(FDR <0.05)inanypairwisecomparison (Figure 3D,E).Clus-
teringofthesedynamicpeaksrevealedfivepredominantgroupsofage-linkedchromatinaccessibil-
ity patterns (cI-cV, Figure 3E). Given the sample size limitation (n = 3 per age group), we
acknowledge that the statistical significance of these observed dynamic changes will require further
corroboration using datasets from additional donor samples. Nevertheless, we reasoned that
because these changes are observable despite modest sample size, the trends provide informative
biologicalinsights.
Ofthesedynamicpeaks,weidentifiedtwoclustersofAT2sitesexhibitingincreasingaccessibility
withageincludingseveralsiteslinkedtocandidategenesforSARS-CoV-2hostgenes,mostnotably
nine sites co-accessible with TMPRSS2 (cIII 30yo enriched and cIV 3yo + 30yo, Figure 3E). Intrigu-
ingly, these two age-increasing co-accessible site containing clusters were enriched for processes
relatedtoviralinfection,immuneresponseandinjuryrepairsuchasviralreleasefromhostcell,inter-
feron-gamma mediated signaling pathway, and positive regulation of ERBB signaling pathway
(Figure 3F, Supplementary file 5). Also, these age-dependent clusters were enriched for pheno-
typessubstantiatedinmousestudies,suchaspulmonaryepithelialnecrosis,increasedmonocytecell
number, and chronic inflammation (Figure 3F, Supplementary file 5). We observed an enrichment
of sequence motifs within these clusters for transcription factors controlling endoderm cell fate
(FOXA,HNF1),lungcellfate(NKX),AT2cellfate(CEBP)andAT2cellsignaling(ETS)(Maedaetal.,
2007;Morriseyetal.,2013;MorriseyandHogan,2010).Furthersupportingimmuneregulationof
AT2 cell gene expression, we observed an enrichment of motifs for factors involved in immune
Wang,Chiou,Poirion,etal.eLife2020;9:e62522.DOI:https://doi.org/10.7554/eLife.62522 8of28

Researcharticle DevelopmentalBiology GeneticsandGenomics
signaling such as STAT, IRF, and FOS/JUN (Au-Yeung and Horvath, 2018; Mogensen, 2018;
Figure3G,Supplementaryfile6).
To complement the genome-wide unbiased approach which identified 9 TMPRSS2 co-accessible
sites as age-increasing (Figure 3E), we next assessed in a locus restricted manner how many of the
73 co-accessible sites (Figure 2D) showed increased accessibility with age in AT2 cells. Overall, we
identified 10 additional cCREs co-accessible with TMPRSS2, which exhibited patterns of increasing
accessibility with age for a total of 19 age-increasing TMPRSS2-linked cCREs, 17 of which were sta-
tistically significant, with the caveat of modest sample size (N = 3 per age group) (FDR < 0.05 via
EdgeR and/or p<0.05 via independent t-test, Figure 3H,I, Figure 3—figure supplement 1C,
Supplementaryfile4).Whenviewedingenomiccontext,severalofthesesitesshowedaclearage-
linkedincreaseinreaddepthlikelyreflectingahigherfractionofaccessiblenuclei(Figure3J).Nota-
bly, accessibility at the TMPRSS2 promoter did not exhibit differential accessibility with age
(Figure3J,Figure3—figuresupplement1B)emphasizingalikelyroleofdistalcCREsinregulating
age-increasingTMPRSS2expressioninAT2cells.
Genetic variants predicted to affect age-increased TMPRSS2-linked
cCREs are associated with respiratory phenotypes and TMPRSS2
expression
MappingdistalcCREslinkedtoTMPRSS2allowedustonextidentifynon-codingsequencevariation
that might affect cis-regulatory activity and contribute to inter-individual differences in TMPRSS2
expressionandtheriskoflungdisease.Wethereforecharacterizedgeneticvariationinthe19cCREs
withage-increasedchromatinaccessibilityandlinkedtoTMPRSS2inAT2s(Figure3H,I).
In total, 2270 non-singleton sequence variants in the gnomAD v3 database (Karczewski et al.,
2019) overlapped age-increasing cCREs linked to TMPRSS2 in AT2s. To determine which of these
variants might affect regulatory activity in AT2 cells, we first identified variants
inpredictedsequencemotifsoftranscriptionfactor(TF)familiessuchasCEBP,ETS,NKX,FOXA,IRF
and STAT which were enriched in AT2 cCREs. In total we identified 1100 variants in a
predictedmotifforoneormoreoftheseTFs(Figure4A,Supplementaryfile7).Wefurtherapplied
amachinelearningapproach(deltaSVM)(Leeetal.,2015)tomodelAT2chromatinaccessibilityand
identified 212 variants with significant predicted effects (FDR < 0.1) on AT2 chromatin accessibility
(Figure4A,Supplementaryfile7).Amongmotif-boundvariants,50werecommon(definedhereas
minorallelefrequency[MAF]>1%)ofwhich10furtherhadpredictedeffectsonAT2chromatinacces-
sibility using deltaSVM (Lee et al., 2015; Figure 4A, Supplementary file 7). Common variants with
predicted function generally had consistent frequencies across populations, although multiple var-
iants, for example rs35074065, were much less common in East Asians (MAF = 0.005) relative to
otherpopulations(EuropeansMAF=0.45,SouthAsianMAF=0.37,AfricanMAF=0.12).
We next determined whether common variants with predicted AT2 regulatory effects were asso-
ciatedwithphenotypesrelatedtorespiratoryfunction,infection,medicationuseorothertraitsusing
GWAS summary statistic data generated using the UK Biobank (UKBB) (Sudlow et al., 2015).
Among the 10 common variants that were both TF motif-disrupting and had predicted effects on
AT2 chromatin accessibility, the most significant association was between rs35074065 and emphy-
sema (p=5.64 (cid:2) 10(cid:0)7) (Figure 4B). This variant also had evidence for association with asthma
(p=6.7 (cid:2) 10(cid:0)4). Furthermore, the majority of these variants (9/10) were nominally associated
(p<1(cid:2)10(cid:0)2) with at least one phenotype related to respiratory function or respiratory medication
useincludingbronchiectasis(rs462903p=2.0(cid:2)10(cid:0)4,rs9974995p=7.1(cid:2)10(cid:0)4),bacterialpneumonia
(rs2838089 p=2.4(cid:2)10(cid:0)4), COPD (rs1557372 p=2.9 (cid:2) 10(cid:0)3), asthma (rs8127290 p=1.4(cid:2)10(cid:0)3) and
medicationsusedtotreatasthmasuchasserevent(rs220266p=3.1(cid:2)10(cid:0)4,rs62219349p-5.3(cid:2)10(cid:0)3)
(Figure4B).
Given that common AT2 variants showed predicted regulatory function and association with
respiratory disease, we next asked whether these variants regulated the expression of TMPRSS2
using human lung eQTL (expression quantitative trait loci) data from the GTEx v8 release
(GTExConsortium,2020).AmongvariantstestedforassociationinGTEx,weobservedahighlysig-
nificanteQTLforTMPRSS2expressionatrs35074065(p=3.9(cid:2)10(cid:0)11)aswellasmorenominaleQTL
evidenceatrs1557372(p=2.9(cid:2)10(cid:0)5)andrs9974995(p=3.5(cid:2)10(cid:0)6).Furthermore,infine-mapping
datafromGTEx,rs35074065hadahighposteriorprobability(PPA=41.6%)andthereforelikelyhas
a direct casual effect on TMPRSS2 expression (Figure 4C). This variant further disrupted predicted
Wang,Chiou,Poirion,etal.eLife2020;9:e62522.DOI:https://doi.org/10.7554/eLife.62522 9of28

Researcharticle DevelopmentalBiology GeneticsandGenomics
Figure4.Geneticvariantspredictedtoaffectage-increasingAT2accessiblechromatinareassociatedwithrespiratoryphenotypesandTMPRSS2
expression.(A)Top:genomebrowserviewofAT2siteslinkedtoTMPRSS2activityandthosewithage-dependentincreaseinaccessibility.Middle:
Numberofnon-singletongeneticvariantsingnomADv3mapping(Karczewskietal.,2019)ineachage-dependentsitepredictedtodisruptbinding
ofAT2-enrichedTFmotifs.Bottom:Commonvariants(minorallelefrequency>0.05inatleastonepopulation)predictedtobindAT2-enrichedTF
motifs,color-codedbyTFfamily.Motif-boundvariantsthatalsohavepredictedeffects(FDR<0.10)onAT2accessiblechromatinindeltaSVMmodels
(Leeetal.,2015)highlightedinred.(B)AssociationofcommonvariantswithpredictedAT2effects(motif-disrupting+deltaSVM)withhuman
phenotypesintheUKBiobank(Lab,2020).Themajorityoftestedvariantsshowatleastnominalevidence(p<0.005)forassociationwithphenotypes
relatedtorespiratorydisease,infectionand/ormedication.(C)Fine-mappingprobabilitiesforanTMPRSS2expressionQTLinhumanlungsamples
fromtheGTExprojectreleasev8(GTExConsortium,2020).Thevariantrs35074065hasthehighestcasualprobability(PPA=0.42)fortheeQTL,maps
inanage-dynamicAT2siteandispredictedtodisruptbindingofIRFandSTATTFs.Variantsarecoloredbasedonr2withrs35074065in1000
GenomesProjectdatausingallpopulations(Autonetal.,2015).(D)Estimatedcelltypeproportionsfor515humanlungsamplesfromGTExderived
usingcell-type-specificexpressionprofilesforcelltypeswithmorethan500cellsfromsnRNA-seqdatageneratedinthisstudy.(E)Associationp-values
betweenrs35074065genotypeandTMPRSS2lungexpressionafterincludinganinteractiontermbetweengenotypeandestimatedcell-type
proportionsforeachsample.WeobservedstrongereQTLassociationwhenincludinganinteractionwithAT2cellproportionaswellasmacrophage
proportion.
Wang,Chiou,Poirion,etal.eLife2020;9:e62522.DOI:https://doi.org/10.7554/eLife.62522 10of28

Researcharticle DevelopmentalBiology GeneticsandGenomics
sequence motifs for IRF and STAT transcription factors, where the TMPRSS2-increasing allele dis-
rupted motif binding, suggesting that its effects may be mediated through interferon signaling and
anti-viralprograms(Figure4C).
As the TMPRSS2 eQTL at rs35074065 was identified in bulk lung samples, we finally sought to
determine the specific cell types driving the effects of this eQTL. Using cell-type-specific gene
expression profiles derived from our snRNA-seq data, we estimated the proportions of 14 different
cell types present in the 515 bulk lung RNA-seq samples from GTEx v8 (GTEx Consortium, 2020;
Figure 4D). We then tested for association between rs35074065 and TMPRSS2 expression while
including estimated cell-type proportions for each sample in the eQTL model in addition to the
covariatesusedintheoriginalGTExanalysis.Weobservedhighlysignificantassociationwheninclud-
ingAT2cellproportion(p=3.8(cid:2)10(cid:0)18)aswellasmacrophageproportion(p=4.0(cid:2)10(cid:0)12),support-
ingthe possibility that the TMPRSS2 eQTL at rs35074065 acts through AT2 cells and macrophages,
which is in line with TMPRSS2-expressing cell types in the lungs (Figure 4E, Figure 2A, Figure 2—
figuresupplement1B).
Fine-mapping risk variants for COVID-19 respiratory failure at the
3p21.31 locus to lung cell-type-specific chromatin sites
Recently the first genome-wide association study of SARS-CoV-2 identified several loci influencing
risk of respiratory failure in SARS-CoV-2 infection (Ellinghaus et al., 2020). Among these loci, risk
variantsatthe3p21.31locusmappedexclusivelytonon-codingsequences(Ellinghausetal.,2020).
Wehypothesizedthatthislocusmayaffectgeneregulationinthelungsandusedourlungcell-type-
specificchromatinaccessibilityandgeneexpressionmaptoannotate3p21.31riskvariants.
Fine-mapping of the 3p21.31 signal resulted in 22 total candidate causal variants. Among these,
twofine-mappedvariantsoverlappedalungcell-typecCRE:rs17713054(posteriorprobability[PPA]
=0.04),whichmapped inacCREaccessibleinepithelial(AT1/2,basal,club,ciliated)andmesenchy-
mal (matrix fibroblast 1/2, myofibroblast) cells with the highest signal in AT2 cells, and rs76374459,
(PPA = 0.02), which mapped in a cCRE accessible in erythrocytes (Figure 5A). We determined
whether these two variants disrupted predicted sequence motifs for relevant TFs. For rs17713054,
theminor(andriskincreasing)alleleAwaspredictedtobindCEBPAandCEBPBmotifs(Figure5B),
which were broadly enriched in age-related cCREs in AT2 cells (Figure 2G). In further support of
CEBPbindingtothislocus,thisvariantoverlappedaCEBPBChIP-seqsiteidentifiedintheENCODE
project (ENCODE Project Consortium, 2012; Wang et al., 2012; Figure 5B). At rs76374459, the
riskalleleCwaspredictedtodisruptbindingofSPI1amongotherTFsandoverlappedaSPI1ChIP-
seq site in ENCODE (ENCODE Project Consortium, 2012; Wang et al., 2012; Figure 5—figure
supplement 1). Candidate causal variants at the 3p21.31 signal also showed evidence for nominal
association with respiratory phenotypes for example bronchiectasis medication (rs76374459
p=2.0(cid:2)10(cid:0)3), emphysema (rs17713054 p=1.4(cid:2)10(cid:0)2), and chronic bronchitis (rs17712877
p=1.1(cid:2)10(cid:0)2),amongotherassociations.
Given multiple fine-mapped variants at 3p21.31 overlapping lung cCREs, we next identified
potential target genes of variant activity. We linked sites harboring risk variants to target genes
using our single-cell co-accessibility data. The site harboring rs17713054 was co-accessible with the
promoter region of multiple genes including SLC6A20, LIMD1, SACM1L, and CCRL2 (Figure 5C).
Among these genes, SLC6A20, which encodes a proline transporter, was expressed predominantly
in AT2 cells and had low expression in other cell types (Figure 5D). We then asked whether
rs17713054 wasassociated with the expression oflinked targetgenes inthe lungs using eQTL data
in GTEx v8 (GTEx Consortium, 2020). While there were no significant associations, we observed
nominal association with SLC6A20 where the minor (and risk increasing) allele A had increased
expression(p=8.09(cid:2) 10(cid:0)3).Wefurthertestedrs17713054forassociationwithSLC6A20expression
includingestimatedcell-type proportionsforeachlungsample intheeQTL model (asinFigure 4E,
see Materials and methods). We observed strongest association when including AT2 or AT1/AT2-
like cell proportion (p=4.09 (cid:2) 10(cid:0)3, p=8.00 (cid:2) 10(cid:0)4) (Figure 5E), supporting the possibility that
rs17713054regulatesSLC6A20expressioninAT2cells.Theseresultsilluminatecandidatecausalvar-
iants mapping in lung cell-type cCREs at the 3p21.31 locus and their putative target genes, which
shouldhelpguidedetailedfollow-upstudyofthemechanismofhowthislocuscontributestorespi-
ratoryfailureinSARS-CoV-2infection.
Wang,Chiou,Poirion,etal.eLife2020;9:e62522.DOI:https://doi.org/10.7554/eLife.62522 11of28

Researcharticle DevelopmentalBiology GeneticsandGenomics
Figure5.Fine-mappedriskvariantsatthe3p21.31locusassociatedwithrespiratoryfailureinSARS-CoV-2overlaplungcell-typechromatinsites.(A)
Genomebrowserview(Robinsonetal.,2011)showingposteriorprobability(PPA)ofvariantsinthefine-mappingcrediblesetatthe3p21.31
associationsignalandlungcell-type-specificaccessiblechromatinprofiles.Crediblesetvariantsthatdirectlyoverlaplungcell-typechromatinsitesare
highlighted.Readdepthvaluesrepresentcountspermillion(CPM).(B)Variantrs17713054overlapsasiteactiveinAT2andotherepithelialcellsand
boundbyCEBPBamongotherTFs,andtheminoralleleAispredictedtobindaCEBPmotif.Forin-depthanalysisofrs76374459seeFigure5—figure
supplement1.Readdepthvaluesrepresentcountspermillion(CPM).(C)Co-accessiblelinksbetweenthesiteharboringrs17713054(bluebox)and
otherchromatinsites,includingthepromoterregionsoffourgenesSLC6A20,LIMD1,SACM1LandCCRL2(graybox).Theheightofeachlink
representsthestrengthofco-accessibility(Cusanovichetal.,2018).(D)ExpressionofSLC6A20acrosslungcelltypes,whereeachdotrepresentsa
nucleus.ThehighestexpressionobservedwasinAT2cells.(E)Associationp-valuesbetweenrs17713054genotypeandSLC6A20lungexpressionafter
includinganinteractiontermbetweengenotypeandestimatedcell-typeproportionsforeachsample.WeobservedstrongesteQTLassociationwhen
includinganinteractionwithAT1/AT2-likeandAT2cellproportion.
Theonlineversionofthisarticleincludesthefollowingfiguresupplement(s)forfigure5:
Figuresupplement1.Molecularcharacterizationofvariantrs76374456.
Discussion
Inthisstudy,weinterrogatedchromatinaccessibilityandgeneexpressioninthehumanlungsatsin-
gle-cell resolution and identified cCRE predicted to control expression of SARS-CoV2 host entry
genes.ThelungscameintofocusduringtheCOVID-19pandemicsincerespiratoryfailureisamajor
complicationandcauseofdeath(Duetal.,2020).Notably,symptoms,severity,andprogressionof
COVID-19 vary considerably between age and population groups (CDC, 2020a; CDC, 2020b). Our
sample-matched snATAC-seq and snRNA-seq datasets from three postnatal stages enabled us to
interrogate age-associated dynamics in gene expression and chromatin accessibility. While we
focusedonCOVID-19relatedgenesinthisstudy,thesedatasetswillmorebroadlyfacilitatein-depth
analysisofcell-typeresolveddynamicsofgeneregulatoryprocessesinthehumanlungs.
Using our datasets, we not only corroborated recent findings that the host entry genes ACE2,
encoding the receptor for the viral spike protein, and TMPRSS2, encoding a serine protease for
priming of the spike protein, were detected in a higher proportion of AT2 cells in adult lungs
Wang,Chiou,Poirion,etal.eLife2020;9:e62522.DOI:https://doi.org/10.7554/eLife.62522 12of28

Researcharticle DevelopmentalBiology GeneticsandGenomics
compared to pediatric lungs (Muus et al., 2020; Schuler et al., 2020), but also identified cCREs
linked to TMPRSS2 and highlighted 19 cCREs with age-increased accessibility. Notably, an increase
inaccessibilityatseveralofthesecCREspredatestheonsetofgeneexpressionincrease,suggesting
that, although AT2 cells in childhood stages express lower TMPRSS2, the cells may have already
acquired the regulatory potential for higher TMPRSS2 expression. Because these cCREs are pre-
dicted toact downstream ofimmuneand inflammatory signals, oneplausible implication isthat dif-
ferences in baseline levels of immune/inflammation signaling between children and adults may
impactsusceptibilitytoinfectionbydirectlyregulatingtheexpressionofviralentrygenes.Itisworth
noting that these age-related observations are made with the caveat that the sample size of this
studyismodest(n=3individualspergroup).Follow-upstudieswithlargercohortswillbeimportant
toreinforcethesignificanceofthesefindings.
WhileACE2 was detected inasmall number ofcellsand mostly confined to AT2cells, TMPRSS2
was expressed in a higher fraction of nuclei predominantly from the epithelial lineage (Qi et al.,
2020; Waradon Sungnak et al., 2020; Zhao et al., 2020; Ziegler et al., 2020; Zou et al., 2020).
Thismay indicatethatlowACE2levelsmightrepresentaratelimitingstep forviralentry. However,
wecaution that inhibiting ACE2 expression may have unintended consequence.Aside from being a
viralreceptorgene,ACE2isalsorequiredforprotectingthelungsfrominjury-inducedacuterespira-
tory distress phenotypes, the precise cause of COVID-19 mortality (Imai et al., 2005). Thus, inhibit-
ing ACE2 expression may compromise the ability of the lungs to sustain damage. In comparison,
Tmprss2 mutant mice show no defects at baseline and are more resistant to the original SARS-CoV
infection (Iwata-Yoshikawa et al., 2019; Kim et al., 2006). Thus, manipulating the expression of
genessuchasTMPRSS2mayrepresentasaferpathtolimitSARS-CoV-2viralentry.TMPRSS2isalso
involved in the entry of other respiratory viruses such as influenza, suggesting that modulating its
expression may also be effective in deterring entry and spread of other viruses (Limburg et al.,
2019).
To explore potential avenues for manipulating the expression of viral entry genes, we identified
transcriptionfactorsenrichedincCREswithincreasedchromatinaccessibilityinadultAT2cellscom-
pared to younger AT2 cells. These included transcription factors involved in stress and immune
responses. For example, key interferon pathway-related factors STAT and IRF have binding sites in
theage-increasedcCREslinkedtoTMPRSS2.ThelikelycausalTMPRSS2eQTLvariantrs35074065is
predicted to disrupt STAT and IRF binding, raising the possibility that STAT and/or IRF binding at
this site may directly control TMPRSS2 gene expression. Further experimental follow-up studies will
beneededtovalidatetheeffectofthesevariantsonTFbindingandTMPRSS2expression,forexam-
pleusingelectrophorecticmobilityshiftassays(EMSA),enhancer/promoterreporterassays,genome
editingofinvitromodelssuchasalveolarorganoids(Dobrindtetal.,2020;Jacobetal.,2017).Itis
interestingthatmultiplevariantslinkedtoTMPRSS2wereassociatedwithpulmonaryfunctionorpul-
monarydiseasemedicationuse.Suchassociationprovidesplausiblelinksforhowpre-existingcondi-
tionsmaymodifyresponsetoinfections.
Finally, and highlighting the utility of our cCRE maps, we reveal a non-coding variant at the
3p21.32 locus risk for COVID-19 related respiratory failure (Ellinghaus et al., 2020) overlapping an
AT2cell-activedistalcCRE.Importantlythisvariant(rs17713054)overlapsabindingsiteforCEBP,a
cardinaltranscription factorforAT2 cellgeneexpression (Xu etal., 2012).Amongtheputative tar-
get genes for this cCRE was SLC6A20 which was predominantly expressed in AT2 cells. In Xenopus
oocytes, ACE2 expression promotes SLC6A20 protein levels, localization to plasma membrane and
itsfunctioninprolineaminoacidtransport(Vuille-dit-Billeetal.,2015).Conversely,inAce2mutant
mice, proline transport, presumably via SLC6A20, was severely disrupted (Singer et al., 2012). Fur-
therfunctionalstudieswillberequiredtovalidatethemoleculareffectofthisvariantonTFbinding,
enhancer activity and gene regulation in AT2 cells. However, this locus exemplifies how our data
provideafoundationtogeneratetestablehypothesesofhowriskvariantsmechanisticallycontribute
tolungdisease,inthiscasethatchangesinSLC6A20expressioninAT2cellsmayimpactseverityof
SARS-CoV-2infectionofthelungs.
Overall, our study serves as a resource for evolving analyses of gene regulation in the human
lungs at cell-type resolution. Moreover, our cCRE maps will also facilitate the interpretation of non-
coding genetic variants associated with a broad spectrum of lung diseases including COVID-19 sus-
ceptibility and disease severity from emerging GWAS in larger cohorts. We note that this work is a
product of the NHLBI-funded LungMap consortium, and our joint goal is to provide the community
Wang,Chiou,Poirion,etal.eLife2020;9:e62522.DOI:https://doi.org/10.7554/eLife.62522 13of28

| Researcharticle |     |     | DevelopmentalBiology | GeneticsandGenomics |
| --------------- | --- | --- | -------------------- | ------------------- |
with fundamental knowledge of the human lungs to guide the effort to combat COVID-19. We
established a web portal to disseminate these datasets to the community: https://www.lungepige-
nome.org/.
|     | Materials | and methods |     |     |
| --- | --------- | ----------- | --- | --- |
Keyresources table
Reagenttype
| (species)or |             | Sourceor           |             | Additional  |
| ----------- | ----------- | ------------------ | ----------- | ----------- |
| resource    | Designation | reference          | Identifiers | information |
| Peptide,    | Tn5         | doi:https://doi.   |             |             |
| recombinant |             | org/10.1101/615179 |             |             |
protein
| Chemical  | NEBNext              | NEB           | Cat#M0541L |     |
| --------- | -------------------- | ------------- | ---------- | --- |
| compound, | High-Fidelity        |               |            |     |
| drug      | 2(cid:2)PCRMasterMix |               |            |     |
| Chemical  | RNasin               | Promega       | Cat#N211B  |     |
| compound, | Ribonuclease         |               |            |     |
| drug      | Inhibitor            |               |            |     |
| Chemical  | DRAQ7                | CellSignaling | Cat#7406   |     |
compound,
drug
| Commercial | ChromiumSingle | 10xGenomics | Cat#1000075 |     |
| ---------- | -------------- | ----------- | ----------- | --- |
| assayorkit | Cell30 Library |             |             |     |
Construction
Kitv3
| Commercial | Chromium     | 10xGenomics | Cat#1000153 |     |
| ---------- | ------------ | ----------- | ----------- | --- |
| assayorkit | Single-CellB |             |             |     |
ChipKit
| Commercial | Chromiumi7    | 10xGenomics | Cat#120262 |     |
| ---------- | ------------- | ----------- | ---------- | --- |
| assayorkit | MultiplexKit, |             |            |     |
96rxns
| Chemical  | SPRISelect | BeckmanCoulter | Cat#B23319 |     |
| --------- | ---------- | -------------- | ---------- | --- |
| compound, | reagent    |                |            |     |
drug
| Software, | CellRanger    | 10xGenomics       |     | Software |
| --------- | ------------- | ----------------- | --- | -------- |
| algorithm | software      | (https://support. |     |          |
|           | packagev3.0.2 | 10xgenomics.com/  |     |          |
single-cell-gene-
expression/software/
downloads/latest)
| Software, | Seuratv3.1.4 | https://satijalab. | RRID:SCR_016341 |     |
| --------- | ------------ | ------------------ | --------------- | --- |
| algorithm |              | org/seurat/        |                 |     |
doi:10.1016/j.
cell.2019.05.031
| Software, | DoubletFinder | https://github.     | RRID:SCR_018771 |     |
| --------- | ------------- | ------------------- | --------------- | --- |
| algorithm |               | com/chris-mcginnis- |                 |     |
ucsf/DoubletFinder
doi:10.1016/j.
cels.2019.03.003
| Software, | GraphPad     | www.graphpad.com | RRID:SCR_002798 |     |
| --------- | ------------ | ---------------- | --------------- | --- |
| algorithm | Prismversion |                  |                 |     |
8.0.0
| Software, | Trimgalore | https://www.    | RRID:SCR_011847 |     |
| --------- | ---------- | --------------- | --------------- | --- |
| algorithm | (v.0.4.4)  | bioinformatics. |                 |     |
babraham.ac.uk/
projects/trim_galore/
| Software, | BWA       | http://bio-bwa.  | RRID:SCR_010910 | Software |
| --------- | --------- | ---------------- | --------------- | -------- |
| algorithm | (v.0.7.1) | sourceforge.net/ |                 |          |
doi:10.1093/
bioinformatics/btp324
Continuedonnextpage
Wang,Chiou,Poirion,etal.eLife2020;9:e62522.DOI:https://doi.org/10.7554/eLife.62522
14of28

| Researcharticle |     |     | DevelopmentalBiology | GeneticsandGenomics |
| --------------- | --- | --- | -------------------- | ------------------- |
Continued
Reagenttype
| (species)or |             | Sourceor    |                 | Additional  |
| ----------- | ----------- | ----------- | --------------- | ----------- |
| resource    | Designation | reference   | Identifiers     | information |
| Software,   | Samtools    | http://www. | RRID:SCR_002105 | Software    |
| algorithm   | (v.1.10)    | htslib.org/ |                 |             |
doi:10.1093/
bioinformatics/btp352
Software, Picard http://broadinstitute. RRID:SCR_006525 Software
| algorithm |                  | github.io/picard/   |                 |          |
| --------- | ---------------- | ------------------- | --------------- | -------- |
| Software, | scanpy           | https://github.     | RRID:SCR_018139 | Software |
| algorithm | (v.1.4.4.post1)  | com/theislab/scanpy |                 |          |
| Software, | Harmony(v.0.1.0) | https://github.     |                 | Software |
| algorithm |                  | com/immunogenomics/ |                 |          |
harmony
doi:10.1038/
s41592-019-0619-0
| Software, | Cicero(v.1.4.4) | https://github.    |     | Software |
| --------- | --------------- | ------------------ | --- | -------- |
| algorithm |                 | com/cole-trapnell- |     |          |
lab/cicero-release
doi:10.1016/j.
molcel.2018.06.044
| Software, | liftOver | https://genome. | RRID:SCR_018160 | Software |
| --------- | -------- | --------------- | --------------- | -------- |
| algorithm |          | ucsc.edu/cgi-   |                 |          |
bin/hgLiftOver
| Other | gnomADv3 | http://gnomad. | RRID:SCR_014964 | Database |
| ----- | -------- | -------------- | --------------- | -------- |
broadinstitute.org/
doi:10.1038/
s41586-020-2308-7
| Other | JASPAR2020 | http://jaspar. | RRID:SCR_003030 | Database |
| ----- | ---------- | -------------- | --------------- | -------- |
genereg.net
doi:10.1093/
nar/gkz1001
Software, FIMO(v.4.12.0) http://meme- RRID:SCR_001783 Software
| algorithm |     | suite.org/ |     |     |
| --------- | --- | ---------- | --- | --- |
doi:10.1093/
bioinformatics/
btr064
| Software,          | deltaSVM       | http://www.                              |     |     |
| ------------------ | -------------- | ---------------------------------------- | --- | --- |
| algorithm          |                | beerlab.org/deltasvm/doi:10.1038/ng.3331 |     |     |
| Software,algorithm | MuSiC(v.0.1.1) | https://github.                          |     |     |
com/xuranw/MuSiC
doi:10.1038/
s41467-018-08023-x
Software,algorithm Python https://www.python.org/ RRID:SCR_008394
Software,algorithm R(v.3.5.1) https://www.r-project.org/ RRID:SCR_001905
Software,algorithm Go(v.1.12.1) https://golang.org/ RRID:SCR_017096
Software,algorithm NumPy(v.1.16.1) https://numpy.org/ RRID:SCR_008633 pythonlibrary
Software,algorithm Scikit-learn(v.0.20.1) https://scikit- RRID:SCR_002577 pythonlibrary
learn.org/stable/
Software,algorithm seaborn(v.0.9.0) https://seaborn. RRID:SCR_018132 pythonlibrary
pydata.org/api.html
Software,algorithm MatPlotLib(v.0.9.0) http://matplotlib. RRID:SCR_008624 pythonlibrary
sourceforge.net
Software,algorithm ATACdemultiplex https://gitlab.com/ suiteofsoftwares
|     | (v.0.46.12) | Grouumf/         |     | writteninGOfor |
| --- | ----------- | ---------------- | --- | -------------- |
|     |             | ATACdemultiplex/ |     | snATACanalysis |
Continuedonnextpage
Wang,Chiou,Poirion,etal.eLife2020;9:e62522.DOI:https://doi.org/10.7554/eLife.62522
15of28

Researcharticle DevelopmentalBiology GeneticsandGenomics
Continued
Reagenttype
(species)or Sourceor Additional
resource Designation reference Identifiers information
Software,algorithm edgeR(v.3.22.5) http://bioconductor. RRID:SCR_012802 Rlibrary
org/packages/
release/bioc/html/
edgeR.htmldoi:10.1093/
bioinformatics/btp616
Software,algorithm Matrix(v.1.2–15) https://cran.r- Rlibrary
project.org/web/
packages/Matrix/
index.html
Software,algorithm Stringr(v.1.4.0) https://www. Rlibrary
rdocumentation.
org/packages/
stringr/versions/1.4.0
Software,algorithm Cicero(v.1.0.14) https://www. Rlibrary
bioconductor.org/
packages/release/
bioc/html/cicero.html
doi:10.1016/j.
molcel.2018.06.044
Software,algorithm HOMER(v4.11.1) http://homer. RRID:SCR_010881 Perlpackage
ucsd.edu/homer/
download.html
doi:10.1016/j.
molcel.2010.05.004
Software,algorithm rGREAT(v.1.20) https://www. forGREAT: Rlibrary
bioconductor.org/ RRID:SCR_005807
packages/release/
bioc/html/rGREAT.
htmlforGREAT:
doi:10.1038/nbt.1630
Human subjects and tissue collection
Donor lung samples were provided through the federal United Network of Organ Sharing via
National Disease Research Interchange (NDRI) and International Institutefor Advancement ofMedi-
cine(IIAM)andenteredintotheNHLBILungMAPBiorepositoryforInvestigationsofDiseasesofthe
Lung(BRINDL)attheUniversityofRochesterMedicalCenteroverseenbytheIRBasRSRB00047606,
aspreviouslydescribed(Ardini-Poleske etal.,2017;Bandyopadhyayetal., 2018).Portions (0.25–
1.0 cm3) of small airway region of right middle lobe (RML) lung tissue were frozen in cryovials over
liquidnitrogenandplacedat(cid:0)80˚Cforstorage.Uponrequest,whilekeptfrozenondryice,atissue
piece(approximately100mg)waschippedoffthesample.Thesesmallersampleswerethenshipped
incryovialstoUCSDonanabundanceofdryice.
Single-nucleus ATAC-seq data generation
Combinatorial barcoding single-nucleus ATAC-seq was performed as described previously with
modifications (Chiou et al., 2019; Fang et al., 2019; Cusanovich et al., 2015; Preissl et al., 2018)
and using new sets of oligos for tagmentation and PCR (Supplementary file 8). Briefly, for each
sample,lungtissuewashomogenizedusingmortarandpestleonliquidnitrogen.1mlnucleiperme-
abilization buffer (10 mM Tris-HCL [pH 7.5], 10 mM NaCl, 3 mM MgCl2, 0.1% Tween-20 [Sigma],
0.1% IGEPAL-CA630 [Sigma] and 0.01% Digitonin [Promega] in water; Corces et al., 2017) was
added to 30 mg of ground lung tissue and tissue was resuspended by pipetting for 8–15 times.
Nuclei suspension was incubated for 10 min at 4˚C and filtered with 30 mm filter (CellTrics). Nuclei
were pelleted with a swinging bucket centrifuge (500 x g, 5 min, 4˚C; 5920R, Eppendorf), resus-
pended in 500 mL high salt tagmentation buffer (36.3 mM Tris-acetate (pH = 7.8), 72.6 mM potas-
sium-acetate,11mMMg-acetate,17.6%DMF)andcountedusingahemocytometer.Concentration
was adjusted to 2000 nuclei/9 mL, and 2000 nuclei were dispensed into each well of one 96-well
plate. For tagmentation, 1 mL barcoded Tn5 transposomes (Fang et al., 2019) was added using a
Wang,Chiou,Poirion,etal.eLife2020;9:e62522.DOI:https://doi.org/10.7554/eLife.62522 16of28

Researcharticle DevelopmentalBiology GeneticsandGenomics
BenchSmart 96 (Mettler Toledo), mixed five times and incubated for 60 min at 37˚C with shaking
(500rpm).ToinhibittheTn5reaction,10mLof40mMEDTAwereaddedtoeachwellwithaBench-
Smart 96 (Mettler Toledo) and the plate was incubated at 37˚C for 15 min with shaking (500 rpm).
Next,20mL2xsortbuffer(2%BSA,2mMEDTAinPBS)wasaddedusingaBenchSmart96(Mettler
Toledo). All wells were combined into a FACS tube and stained with 3 mM Draq7 (Cell Signaling).
UsingaSH800(Sony),202nnucleiweresortedperwellintoeight96-wellplates(totalof768wells)
containing 10.5 mL EB (25 pmol) primer i7, 25 pmol primer i5, 200 ng BSA (Sigma). Preparation of
sortplatesandalldownstreampipettingstepswereperformedonaBiomeki7AutomatedWorksta-
tion (Beckman Coulter). After addition of 1 mL 0.2% SDS, samples wereincubated at 55˚C for7 min
with shaking (500rpm). 1mL12.5%Triton-X was added toeach well to quench the SDS. Next,12.5
mL NEBNext High-Fidelity 2 (cid:2) PCR Master Mix(NEB) were added and samples were PCR-amplified
(72˚C5min,98˚C30s,(98˚C10s,63˚C30s,72˚C60s)(cid:2)12cycles,heldat12˚C).AfterPCR,allwells
were combined. Libraries were purified according to the MinElute PCR Purification Kit manual (Qia-
gen)using avacuummanifold(QIAvac 24plus,Qiagen) andsizeselectionwasperformedwith SPRI
Beads (Beckmann Coulter, 0.55x and 1.5x). Libraries were purified one more time with SPRI Beads
(BeckmannCoulter,1.5x).LibrarieswerequantifiedusingaQubitfluorimeter(Lifetechnologies)and
the nucleosomal pattern was verified using a Tapestation (High Sensitivity D1000, Agilent). The
librarywassequencedonaHiSeq4000orNextSeq500sequencer(Illumina)usingcustomsequencing
primers withfollowing read lengths: 50+10 +12+50 (Read1+Index1 +Index2+Read2). Primer
andindexsequencesarelistedinSupplementaryfile8.
Single-nucleus RNA-seq data generation
Droplet-based Chromium Single-Cell 3’ solution (10x Genomics, v3 chemistry) (Zheng et al., 2017)
wasusedtogeneratesnRNA-seqlibraries.Briefly,30mgpulverizedlungtissuewasresuspendedin
500 mL of nuclei permeabilization buffer (0.1% Triton-X-100 (Sigma-Aldrich, T8787), 1X protease
inhibitor, 1 mM DTT, and 0.2 U/mL RNase inhibitor (Promega, N211B), 2% BSA (Sigma-Aldrich,
SRE0036) in PBS). Sample was incubated on a rotator for 5 min at 4˚C and then centrifuged at 500
rcf for 5 min (4˚C, run speed 3/3). Supernatant was removed and pellet was resuspended in 400 mL
of sort buffer (1 mM EDTA 0.2 U/mL RNase inhibitor (Promega, N211B), 2% BSA (Sigma-Aldrich,
SRE0036) in PBS) and stained with DRAQ7 (1:100; Cell Signaling, 7406). 75,000 nuclei were sorted
usingaSH800sorter(Sony)into50mLofcollectionbufferconsistingof1U/mLRNaseinhibitorin5%
BSA;theFACSgatingstrategysortedbasedonparticlesizeandDRAQ7fluorescence.Sortednuclei
were then centrifuged at 1000 rcf for 15 min (4˚C, run speed 3/3) and supernatant was removed.
Nuclei were resuspended in 35 mL of reaction buffer (0.2 U/mL RNase inhibitor (Promega, N211B),
2% BSA (Sigma-Aldrich, SRE0036) in PBS) and counted on a hemocytometer. 12,000 nuclei were
loaded onto a Chromium Controller (10x Genomics). Libraries were generated using the Chromium
Single-Cell30 Library ConstructionKit v3 (10xGenomics, 1000075)with the ChromiumSingle-Cell B
Chip Kit (10x Genomics, 1000153) and the Chromium i7 Multiplex Kit for sample indexing (10x
Genomics, 120262) according to manufacturer specifications. CDNA was amplified for 12 PCR
cycles. SPRISelect reagent (Beckman Coulter, B23319) was used for size selection and clean-up
steps.FinallibraryconcentrationwasassessedbyQubitdsDNAHSAssayKit(Thermo-FischerScien-
tific) and fragment size was checked using Tapestation High Sensitivity D1000 (Agilent) to ensure
that fragment sizes were distributed normally about 500 bp. Libraries were sequenced using the
NextSeq500 and a HiSeq4000 (Illumina) with these read lengths: 28 + 8 + 91 (Read1 + Index1 +
Read2).
Single-nucleus RNA-seq analysis
Sequencing reads were demultiplexed (cellranger mkfastq) and processed (cellranger count) using
the Cell Ranger software package v3.0.2 (10x Genomics). Reads were aligned to the human refer-
ence hg38 (Cell Ranger software package v3.0.2). Reads mapping to intronic and exon sequences
wereretained.ResultingUMIfeature-barcodecountmatriceswereloadedintoSeurat(Stuartetal.,
2019). All genes representedin >= 3nuclei and cellswith 500–4000 detected genes wereincluded
fordownstreamprocessing.UMIcountswerelog-normalizedandscaledbyafactorof10,000using
the NormalizeData function. Top 3000 variable features were identified using the FindVariableFea-
tures function and finally scaled using the ScaleData function. Barcode collisions were removed for
Wang,Chiou,Poirion,etal.eLife2020;9:e62522.DOI:https://doi.org/10.7554/eLife.62522 17of28

Researcharticle DevelopmentalBiology GeneticsandGenomics
individual datasets using DoubletFinder (McGinnis et al., 2019) with following parameters:
pN=0.15andpK=0.005,anticipatedcollisionrate=10%.Clusterswereassignedadoubletscore
(pANN) and classification as ‘doublet’ or ‘singlet’; called doublets and cells with a pANN score >0
were removed. UMI matrices for datasets were merged and corrected for batch effects due to
experimentdate,donor,andsexusingtheHarmonypackage(Korsunskyetal.,2019).UMAPcoor-
dinates (McInnes et al., 2018) and clustering were performed using the RunUMAP, FindNeighbors,
and FindClusters functions in Seurat with principal components 1–23. 25–26, and 28. Clusters were
annotated,andputativedoubletsasdefinedbyexpressionofcanonicallymutuallyexclusivemarkers
were excluded from analysis; remaining cells were re-clustered using the previously described
parameters. Final cluster annotation was done using canonical markers. For genes of interest, e.g.
ACE2,TMPRSS2,nucleiwithatleastoneUMIforthegenewereconsidered‘expressing’.Toanalyze
changes in percentage of nuclei expressing we performed two-tailed unpaired t-tests using Graph-
Pad Prism version 8.0.0 for Windows, GraphPad Software, San Diego, California USA, www.graph-
pad.com.
Single-nucleus ATAC-seq analysis
For each sequenced snATAC-Seq libraries, we obtained four FASTQ files paired-end DNA reads as
wellasthecombinatorialindexesfori5(768differentPCRindices)andT7(96differenttagmentation
indices;Supplementaryfile8).Weselectedallreadswith<=2mistakesperindividualindex(Ham-
mingdistancebetweeneachpairofindicesis4)andsubsequentlyintegratedthefullbarcodeatthe
beginning of the read name in the FASTQ files (https://gitlab.com/Grouumf/ATACdemultiplex/).
Next, we used trim galore (v.0.4.4) to remove adapter sequences from reads prior to read align-
ment. We aligned reads to the hg19 reference genome using bwa mem (v.0.7.17) (Li and Durbin,
2009) and subsequently used Samtools (Li et al., 2009) to remove unmapped, low map quality
(MAPQ <30), secondary, and mitochondrial reads. We then removed duplicate reads on a per-cell
basis using MarkDuplicates (BARCODE_TAG) from the Picard toolkit. As an initial quality cutoff, we
set a minimum of 1000 reads (unique, non-mitochondrial) and observed 120,090 cells passing this
threshold.
We used a previously described pipeline to identify snATAC-seq clusters (Chiou et al., 2019).
Briefly,weusedscanpy(Wolfetal.,2018)touniformreaddepth-normalizeandlog-transformread
counts within 5 kb windows. We then identified highly variable (hv) windows (min_mean = 0.01,
min_disp = 0.25) and regressed out the total read depth across hv windows (usable counts) within
each experiment. We then merged cells across experiments and extracted the top 50 PCs, using
Harmony (Korsunsky et al., 2019) to correct for potential confounding factors including donor-of-
origin and biological sex. We used Harmony-corrected components to build a nearest neighbor
graph (n_neighbors = 30) using the cosine metric, which was used for UMAP visualization (min_d-
ist=0.3)andLeidenclustering(resolution=1.5)(McInnesetal.,2018;Traagetal.,2019).
Priortothefinalclustering results,weperformed iterativeclustering toidentifyand removecells
mappingtoclusterswithaberrantquality metrics.First, weremoved3,183cellsmappinginclusters
with low read depth. Next, we removed 20,718 cells mapping in clusters with low fraction of reads
in peaks. Finally, we re-clustered the cells at high resolution and removed 5,209 cells mapping in
potential doublet sub-clusters. On average, these sub-clusters had higher usable counts, promoter
usage, and accessibility at more than one marker gene promoter. After removing all of these cells,
our finalclustersconsisted of90,980cells. Toidentify markergenesfor eachcluster,weusedlinear
regression models with gene accessibility as a function of cluster assignment and usable counts
acrosssinglecells.
Computing relative accessibility scores
We define an accessible locus as the minimal genomic region that can be bound and cut by the
enzyme. We use L(cid:26)N to represent the set of all accessible loci. We further define a pseudo-locus
as the set of accessible loci that relates to each other in a certain meaningful way (for example,
nearby loci, loci from different alleles). In this example, pseudo-loci correspond to peaks. We use
fd j d (cid:26)Lg to represent the set of all pseudo-loci. Let a be the accessibility of accessible locus l,
i i l
where l2L. We define the accessibility of pseudo-locus d as A ¼ a , that is, the sum of accessi-
i i X k
k2di
bility of accessible loci associated with di. Let C be the library complexity (the number of distinct
j
Wang,Chiou,Poirion,etal.eLife2020;9:e62522.DOI:https://doi.org/10.7554/eLife.62522 18of28

Researcharticle DevelopmentalBiology GeneticsandGenomics
moleculesinthelibrary)ofcellj.AssumingunbiasedPCRamplification,thentheprobabilityofbeing
sequencedforanyfragmentinthelibraryis:s ¼1(cid:0) 1(cid:0) 1 k,wherek isthetotalnumberofreads
j (cid:16) Cj (cid:17) j j
for cell j. If we assume that the probability of a fragment present inthe library is proportional to its
accessibility and the complexity of the library, then we can deduce that the probability of a given
locuslincelljbeingsequencedis:p /aCs.Foranypseudo-locusd,thenumberofreadsind for
lj l j j i i
celljfollowsthePoissonbinomialdistribution,anditsmeanism ¼ p /Cs a ¼CsA.Given
ij X kj j jX k j j i
k2di k2di
XOij
a pseudo-locus (or peak) by cell count matrix O, we have: O ¼ m . Therefore, A ¼Z j ,
X ij X ij i
j j XCjsj
j
where Z is a normalization constant. When comparing across different samples the relative accessi-
bilitymay bedesirableastheysumuptoaconstant,i.e. A ¼1(cid:2)106.Inthiscase,wecanderive
X i
i
XOij
A ¼ j (cid:3)106.
i
XOij
ij
Calculating the relative percent of cells with accessibility at a locus
Tocorrectforbiasesoccurringfromdifferentialreaddepthsbetweenclusters,weusedthefollowing
strategytodeterminetherelativeratioofcellswithaccessibilityatagivenlocus.Wedefinedtheset
ofaccessiblelociLofagivendatasetDasthegenomicregionscoveredbythesetpeaksPinferred
from D. We define X the set of cells from D, and S a partitioning of X. For a given partition S 2S
i
andforeachfeaturep 2P,wecomputedm theratioofcellsfrom S withatleastonereadoverlap-
j ij i
ping p. We then defined the score s of loci p in S as s ¼106: mij . We finally define the relative
j ij j i ij
Xmij
j2P
ratioofcellsnormalizedacrossthedifferentclustersasRS ¼ sij .
ij
Xsij
i2S
Associating promoters to candidate distal regulatory elements
To identify AT2 co-accessible loci linked to the promoters of TMPRSS2, ACE2, FURIN, BSG, and
CTSL, we utilized an ensemble approach comprising multiple runs of Cicero analysis. We first per-
formed an independent Cicero analysis for each cluster using a genomic window of 1e6 base pairs.
In addition, we enriched these co-accessible links with five runs of cicero analysis using each time a
random subset of 15,000 cells from the entire set of nuclei and a genomic window of 250000 base
pairs. We then merged the co-accessibility links detected in the five analysis by creating an array of
ciceroscoresforeachlink.WefinallyperformedaT-testforeachlinktoassessiftheaveragecicero
scorewasdifferentfrom0andfilteredlinkswithap-value<0.10.Secondly,wedefinedthepromoter
regions of TMPRSS2, ACE2, FURIN, BSG, CTL, CTSL, and SLC6A20 as the 1000 bp regions sur-
rounding the TSS gene transcripts related to protein-coding. Finally, we used the pooled list of co-
accessibleelementstoidentifyalltheaccessiblechromatinsiteslinkedtothepromoters.
Identification and clustering of AT2 peaks with changes in chromatin
accessibility genome-wide
We used EdgeR (Robinson et al., 2010) to identify differential accessible peaks between each of
pair of time points. As input we used the 122,352 peaks in AT2 cell. Dataset ID and sex were used
as technical covariates. Sites with False Discovery Rate (FDR) < 0.05 after Benjamini-Hochberg cor-
rection were considered significant. Next, we performed K-means using the relative accessibility
scorewithalocixtimepointsmatrix.WeusedKfrom5to8andcomputedtheDavis-Bouldinindex
to determine the best K to partition the loci. let R ¼
ðsxþsy Þ
with s the average distance of each
xy dxy x
sample from cluster x and d the distance between the centroids of clusters x and y. The Davies-
xy
Bouldin index is defined as DB¼ 1 max R and low DB scores indicate better partitioning. We
K x X ;y2 x6¼y (cid:0) xy (cid:1)
obtainedanoptimalpartitionwithK=5.
Wang,Chiou,Poirion,etal.eLife2020;9:e62522.DOI:https://doi.org/10.7554/eLife.62522 19of28

Researcharticle DevelopmentalBiology GeneticsandGenomics
Identification of AT2 peaks with changes in chromatin accessibility at
candidate gene loci
The ensembleofcellsX fromDcanbedivided per timepoint,cell subtype,or donor.Weidentified
for individual donors the relative % of cells with at least one read in peaks associated with ACE2,
TMPRSS2, FURIN, BSG, and CTSL promoters. As a background to calculate the relative % of cells,
weusedthemergedsetofpeaksfromalltheclusters.Then,wecomputedat-testfortwoindepen-
dentsampleswithequalvarianceforeachpairofcategories:30wkGA,3yoand30yo.Foreachele-
ment the relative % of cells were used as measurement variable and the timepoint as nominal
variable.
Annotation of genomic elements
The GREAT algorithm (McLean et al., 2010) was used to annotate distal genomic elements using
thefollowingsettings:twonearestgeneswithin1Mb.
Transcription factor related analyses
DenovomotifenrichmentanalysisingenomicelementswasperformedusingHOMER(Heinzetal.,
2010)withstandardparameters.
Predicting variant effects on TF binding and chromatin accessibility
To compile a comprehensive set of variants to test, we downloaded lists of variants from gnomAD
v3 (Karczewski et al., 2019) and filtered out variants that were singletons or indels longer than 3
bp. We then used the liftOver (Tyner et al., 2017) utility to transform GRCh38 into GRCh37/hg19
coordinates, and identified variants overlapping age-dependent AT2 sites linked to TMPRSS2. For
each variant we obtained sequence surrounding each variant allele and predicted sequence motifs
from the JASPAR database (Fornes et al., 2020) using FIMO (Grant et al., 2011), and focused on
motifsofTF families enrichedinage-dependentAT2 chromatin. Weconsidered variants with apre-
dictionforatleastonealleletohaveallelicTFbinding.WenextuseddeltaSVM(Leeetal.,2015)to
predicttheeffectsofvariantsonchromatinaccessibilityinAT2cells.First,weextractedthesequen-
ces underlying sites co-accessible with the TMPRSS2 promoter. As described previously
(Chiou et al., 2019), we trained a sequence-based model of AT2 cell chromatin accessibility and
used it to predict effects for all possible combinations of 11mers. We extracted sequences in a 19
bp window around each variant (±9 bp flanking each side). Finally, we calculated deltaSVM z-scores
foreachvariantbypredictingdeltaSVMscores,randomlypermuting11mereffectsandre-predicting
deltaSVM scores, and using the parameters of the null distribution to calculate deltaSVM z-scores.
From the z-scores, we calculated p-values and q-values and defined variants with significant effects
using a threshold of FDR < 0.1. We identified common variants defined as minor allele fre-
quency>0.01inatleastonemajorpopulationgroup.
Phenotype associations for predicted effect variants
WedownloadedUKbiobankround2GWAScombinedsexresults(Lab,2020;Sudlowetal.,2015).
We used broad disease categories from the ICD-10-CM to classify ICD10 phenotypes, except for
ICD10codesrelatingtounclassifiedsymptoms,externalcausesofmorbidity,andfactorsinfluencing
health status and contact with health services. We combined all non-cancer, self-reported diseases
intoasinglecategory(self-reported)aswellasalltreatmentsandmedications(medication).Wethen
extracted GWAS association results for variants that were not tagged as low confidence variants,
had significant deltaSVM effects (Lee et al., 2015), and mapped in TMPRSS2-linked aging-related
sites. From these variants, we removed one (rs199938061) which was in perfect linkage disequilib-
riumwithanothervariant.
Annotating risk variants at the 3p21.31 locus
We obtained 95% credible sets of fine-mapped variants at the 3p21.31 locus reported in a recent
GWAS study of SARS-CoV-2 with severe lung disease (respiratory failure). As variant coordinates
were reported in hg38, we manually lifted over variants to hg19 by matching rs IDs to their corre-
sponding genomic coordinates in hg19. We then identified credible set variants overlapping lung
cell type chromatin sites. For variants overlapping a site, we obtained sequence surrounding each
Wang,Chiou,Poirion,etal.eLife2020;9:e62522.DOI:https://doi.org/10.7554/eLife.62522 20of28

Researcharticle DevelopmentalBiology GeneticsandGenomics
variantalleleandpredictedsequencemotifsfromtheJASPARdatabase(Fornesetal.,2020)using
FIMO(Grantetal.,2011).
Deconvoluting lung expression QTLs
We used MuSiC (v.0.1.1) (Wang et al., 2019) to estimate the proportions of lung cell types
with>500cellsfromourscRNA-seqdatasetinlungbulkRNA-seqsamplesfromtheGTExv8release
(GTEx Consortium, 2020). We combined cell-type labels for capillary (distal and proximal), macro-
phages (M1 and M2), matrix fibroblasts (1 and 2), and NK/T cells. We modeled the relationship
between TMM-normalized TMPRSS2 or SLC6A20 expression as a function of the interaction
between genotype and cell-type proportion, while considering the covariates used in the original
GTEx data including sex, sequencing platform, PCR, five genotype PCs, and 59 inferred PCs from
the expression data. From the original inferred PCs, we excluded inferred PC one because it was
highly correlatedwithAT2 cell-typeproportion (Spearman r=0.67).Including additionalcovariates
in the model such as age, body-mass index or smoking status did not have meaningful impact on
theresults.
Statistics
While there was norandomization ofsamples, and investigators werenot blinded to the specimens
being investigated, clustering of single nuclei based on transcripts and chromatin accessibility was
performed in an unbiased and unsupervised manner, and cell types were assigned after clustering.
Nostatisticalmethodswereusedtopredeterminesamplesizes.Tocomparefractionofpositivecells
between samples across ages, a two-tailed unpaired t-test was used. For genome-wide differential
accessibility analysisof snATAC-seq peaks, pairwise comparisons between donor age groups (n = 3
per age group) were carried out using EdgeR (Robinson et al., 2010) with a cutoff of FDR < 0.05.
For locus restricted differential accessibility analysis of snATAC-seq peaks, pairwise comparisons
between donor age groups (n = 3 per age group) were made using independent t-test with the
same variance assumption. Statistic methods used for other analysis are detailed in the specific
methodandresultssections.
Code availability
Custom code for processing snATAC-seq datasets is available here: https://github.com/kjgaulton/
pipelines/tree/master/lung_snATAC_pipeline; Wang, 2020; copy archived at swh:1:rev:
2d215946323af71e9d2b158a580c2cf3b41dd5f3.
Custom code used for demultiplexing and downstream analysis for snATAC data is available
here: https://gitlab.com/Grouumf/ATACdemultiplex/-/tree/master/ATACdemultiplex, https://gitlab.
com/Grouumf/ATACdemultiplex/-/blob/master/scripts/.
Acknowledgements
We are incredibly grateful to the families who have generously given such precious gifts to support
this research. We thank all the members of the LungMAP Consortium for their collaborations. We
thankDr.BingRen,Dr.MaikeSander,membersoftheSunlab,Gaultonlab,RenlabandtheUCSD
CenterforEpigenomicsforinsightfuldiscussions.WethankSKuanforsequencingandBLiforbioin-
formatics support. We thank K Jepsen and the UCSD IGM Genomics Center for sequencing the
snRNAseq libraries. We thank the QB3 Macrolab at UC Berkeley for purification of the Tn5
transposase.
Additional information
Competinginterests
Dina A Faddah: employee of and holds stock in Vertex Pharmaceuticals. Kyle J Gaulton: does con-
sultingforGenentech.Theotherauthorsdeclarethatnocompetinginterestsexist.
Wang,Chiou,Poirion,etal.eLife2020;9:e62522.DOI:https://doi.org/10.7554/eLife.62522 21of28

Researcharticle DevelopmentalBiology GeneticsandGenomics
Funding
Funder Grantreferencenumber Author
NationalHeart,Lung,and 1U01HL148867 AllenWang
BloodInstitute JamieMVerheyden
SebastianPreissl
XinSun
NationalHeart,Lung,and U01HL122700 GloriaPryhuber
BloodInstitute
HumanTissueCore U01HL122700 GloriaPryhuber
HumanTissueCore HL148861 GloriaPryhuber
Thefundershadnoroleinstudydesign,datacollectionandinterpretation,orthe
decisiontosubmittheworkforpublication.
Authorcontributions
Allen Wang, Kyle J Gaulton, Sebastian Preissl, Conceptualization, Data curation, Formal analysis,
Supervision,Fundingacquisition,Methodology,Writing-originaldraft,Projectadministration,Writ-
ing-review andediting;Joshua Chiou,Datacuration, Formalanalysis, Writing-originaldraft,Writ-
ing-reviewandediting;OlivierBPoirion,MichaelJValdez,Datacuration,Formalanalysis,Writing-
review and editing; Justin Buchanan, Data curation, Formal analysis, Investigation, Writing - review
and editing; Jamie M Verheyden, Validation, Investigation, Writing - review and editing; Xiaomeng
Hou, Investigation; Parul Kudtarkar, Dina A Faddah, Data curation; Sharvari Narendra, Visualization;
JacklynMNewsome,MinzheGuo,KaiZhang,EnikoSajti,YanXu,Formalanalysis;RandeeEYoung,
JustinnBarr,Validation;RaviMisra,HeidieHuyck,LisaRogers,CoryPoole,NHLBILungMapConsor-
tium, Resources; Jeffery A Whitsett, Supervision; Gloria Pryhuber, Resources, Funding acquisition;
XinSun,Conceptualization,Datacuration
AuthorORCIDs
AllenWang https://orcid.org/0000-0001-9870-7888
JoshuaChiou http://orcid.org/0000-0002-4618-0647
JamieMVerheyden https://orcid.org/0000-0003-4116-8507
KyleJGaulton https://orcid.org/0000-0003-1318-7161
SebastianPreissl https://orcid.org/0000-0001-8971-5616
XinSun https://orcid.org/0000-0001-8387-4966
DecisionletterandAuthorresponse
Decisionletterhttps://doi.org/10.7554/eLife.62522.sa1
Authorresponsehttps://doi.org/10.7554/eLife.62522.sa2
Additional files
Supplementaryfiles
. Supplementary file 1. Donor metadata tables. Sheet 1: 30wkGA - 30yo: Donor ID, age, sex, race,
clinical pathology diagnosis (clinPathDx), gestational age, overall quality of the lung tissue assess-
ment, type of death and cause of death were listed. Not shown are data on body weight, body
height, total lung weight and radial alveolar count assessment of alveolarization. All were all within
normallimitsforage.Abbreviations:DCD:donoraftercardiacdeath;DBD:donorafterbraindeath;
GA:gestationalage;RDS:respiratorydistresssyndrome.
. Supplementaryfile2.Summarystatisticsforsequencinglibraries.
. Supplementaryfile3.Clustercompositionandnumberandfractionofnucleiexpressingcandidate
forSARS-CoV2cellentry.
. Supplementary file 4. Annotation of peaks co-accessible with candidate genes for SARS-CoV2 cell
entry and age-associated changes of chromatin accessibility of peaks co-accessible with TMPRSS2
promoter.
Wang,Chiou,Poirion,etal.eLife2020;9:e62522.DOI:https://doi.org/10.7554/eLife.62522 22of28

Researcharticle DevelopmentalBiology GeneticsandGenomics
. Supplementaryfile5.GREATanalysisofpeaksincreasingwithageinAT2cells(groupscIIIandcIV
inFigure3F).
. Supplementary file 6. De novo motif enrichment analysis of peaks increasing with age inAT2 cells
(groupscIIIandcIVinFigure3F).
. Supplementary file 7. Genetic variants with predicted functional effects on sites linked to
TMPRSS2.
. Supplementaryfile8.IndexesandprimersequencesforsnATAC-seqlibraries.
. Transparentreportingform
Dataavailability
Processeddataincludingthefulllistofpeaksareavailablefordownloadandcanbeexploredusing
thewebportal https://www.lungepigenome.org.Rawsequencingfileshas beensubmittedtoLung-
MapDataCollectingCoreandwillbesubmittedtodbGAP.SourcedataforFigure1—figuresupple-
ment 1 is available as Supplementary file 2; Source data for Figure 3B and Figure 3—figure
supplement1AisavailableasSupplementaryfile3.SourcedataforFigure3EisavailableasSupple-
mentaryfile4.SourcedataforFigure3FisavailableasSupplementaryfile5.SourcedataforFigure
3Gis availableas Supplementary file6.Source datafor Figure4Aisavailable as Supplementary file
7.
Thefollowingdatasetwasgenerated:
Databaseand
Author(s) Year Datasettitle DatasetURL Identifier
WangA, ChiouJ, 2020 SingleNucleusMultiomicProfiling https://www.ncbi.nlm. NCBIGene
PoirionOB, Bucha- RevealsAge-DynamicRegulationof nih.gov/geo/query/acc. ExpressionOmnibus,
nanJ, ValdezMJ, HostGenesAssociatedwithSARS- cgi?acc=GSE161383 GSE161383
VerheydenJM, Hou CoV-2Infection
X, GuoM, News-
omeJM, Kudtarkar
P, FaddahDA,
ZhangK, YoungRE,
BarrJ, MisraR,
HuyckH, RogersL,
PooleC, Whitsett
JA, PryhuberG, Xu
Y, GaultonKJ,
PreisslS, SunX
References
Ardini-PoleskeME,ClarkRF,AnsongC,CarsonJP,CorleyRA,DeutschGH,HagoodJS,KaminskiN,MarianiTJ,
PotterSS,PryhuberGS,WarburtonD,WhitsettJA,PalmerSM,AmbalavananN,LungMAPConsortium.2017.
LungMAP:themolecularatlasoflungdevelopmentprogram.AmericanJournalofPhysiology-LungCellular
andMolecularPhysiology313:L733–L740.DOI:https://doi.org/10.1152/ajplung.00139.2017,PMID:28798251
Au-YeungN,HorvathCM.2018.Transcriptionalandchromatinregulationininterferonandinnateantiviralgene
expression.Cytokine&GrowthFactorReviews44:11–17.DOI:https://doi.org/10.1016/j.cytogfr.2018.10.003,
PMID:30509403
AutonA,BrooksLD,DurbinRM,GarrisonEP,KangHM,KorbelJO,MarchiniJL,McCarthyS,McVeanGA,
AbecasisGR,1000GenomesProjectConsortium.2015.Aglobalreferenceforhumangeneticvariation.Nature
526:68–74.DOI:https://doi.org/10.1038/nature15393,PMID:26432245
BandyopadhyayG,HuyckHL,MisraRS,BhattacharyaS,WangQ,MerenessJ,LillisJ,MyersJR,AshtonJ,
BushnellT,CochranM,Holden-WiltseJ,KatzmanP,DeutschG,WhitsettJA,XuY,MarianiTJ,PryhuberGS.
2018.Dissociation,cellularisolation,andinitialmolecularcharacterizationofneonatalandpediatrichumanlung
tissues.AmericanJournalofPhysiology-LungCellularandMolecularPhysiology315:L576–L583.DOI:https://
doi.org/10.1152/ajplung.00041.2018,PMID:29975103
BoothLN,BrunetA.2016.Theagingepigenome.MolecularCell62:728–744.DOI:https://doi.org/10.1016/j.
molcel.2016.05.013,PMID:27259204
BuenrostroJD,GiresiPG,ZabaLC,ChangHY,GreenleafWJ.2013.Transpositionofnativechromatinforfast
andsensitiveepigenomicprofilingofopenchromatin,DNA-bindingproteinsandnucleosomeposition.Nature
Methods10:1213–1218.DOI:https://doi.org/10.1038/nmeth.2688,PMID:24097267
Wang,Chiou,Poirion,etal.eLife2020;9:e62522.DOI:https://doi.org/10.7554/eLife.62522 23of28

Researcharticle DevelopmentalBiology GeneticsandGenomics
BuenrostroJD,WuB,LitzenburgerUM,RuffD,GonzalesML,SnyderMP,ChangHY,GreenleafWJ.2015.
Single-cellchromatinaccessibilityrevealsprinciplesofregulatoryvariation.Nature523:486–490.DOI:https://
doi.org/10.1038/nature14590,PMID:26083756
CDC.2020a.COVIDViewweek31.https://www.cdc.gov/coronavirus/2019-ncov/covid-data/pdf/covidview-08-07-
2020.pdf[AccessedAugust7,2020].
CDC.2020b.ProvisionalCOVID-19deathcountsbysex,age,andstate.https://data.cdc.gov/NCHS/Provisional-
COVID-19-Death-Counts-by-Sex-Age-and-S/9bhg-hcku[AccessedAugust7,2020].
ChenZ,MiL,XuJ,YuJ,WangX,JiangJ,XingJ,ShangP,QianA,LiY,ShawPX,WangJ,DuanS,DingJ,Fan
C,ZhangY,YangY,YuX,FengQ,LiB,etal.2005.FunctionofHAb18G/CD147ininvasionofhostcellsby
severeacuterespiratorysyndromecoronavirus.TheJournalofInfectiousDiseases191:755–760.DOI:https://
doi.org/10.1086/427811,PMID:15688292
ChenX,MiragaiaRJ,NatarajanKN,TeichmannSA.2018.Arapidandrobustmethodforsinglecellchromatin
accessibilityprofiling.NatureCommunications9:5345.DOI:https://doi.org/10.1038/s41467-018-07771-0,
PMID:30559361
ChiouJ,ZengC,ChengZ,HanJY,SchlichtingM,HuangS,GaultonKJ.2019.Singlecellchromatinaccessibility
revealspancreaticisletcelltype-andstate-specificregulatoryprogramsofdiabetesrisk.bioRxiv.DOI:https://
doi.org/10.1101/693671
CorcesMR,TrevinoAE,HamiltonEG,GreensidePG,Sinnott-ArmstrongNA,VesunaS,SatpathyAT,RubinAJ,
MontineKS,WuB,KathiriaA,ChoSW,MumbachMR,CarterAC,KasowskiM,OrloffLA,RiscaVI,KundajeA,
KhavariPA,MontineTJ,etal.2017.AnimprovedATAC-seqprotocolreducesbackgroundandenables
interrogationoffrozentissues.NatureMethods14:959–962.DOI:https://doi.org/10.1038/nmeth.4396,
PMID:28846090
CorcesMR,ShcherbinaA,KunduS,GloudemansMJ,Fre´sardL,GranjaJM,LouieBH,EulalioT,ShamsS,
BagdatliST,MumbachMR,LiuB,MontineKS,GreenleafWJ,KundajeA,MontgomerySB,ChangHY,Montine
TJ.2020.Single-cellepigenomicanalysesimplicatecandidatecausalvariantsatinheritedrisklocifor
alzheimer’sandParkinson’sdiseases.NatureGenetics52:1158–1168.DOI:https://doi.org/10.1038/s41588-
020-00721-x,PMID:33106633
CoutardB,ValleC,deLamballerieX,CanardB,SeidahNG,DecrolyE.2020.Thespikeglycoproteinofthenew
coronavirus2019-nCoVcontainsafurin-likecleavagesiteabsentinCoVofthesameclade.AntiviralResearch
176:104742.DOI:https://doi.org/10.1016/j.antiviral.2020.104742,PMID:32057769
CusanovichDA,DazaR,AdeyA,PlinerHA,ChristiansenL,GundersonKL,SteemersFJ,TrapnellC,ShendureJ.
2015.Multiplexsinglecellprofilingofchromatinaccessibilitybycombinatorialcellularindexing.Science348:
910–914.DOI:https://doi.org/10.1126/science.aab1601,PMID:25953818
CusanovichDA,HillAJ,AghamirzaieD,DazaRM,PlinerHA,BerletchJB,FilippovaGN,HuangX,ChristiansenL,
DeWittWS,LeeC,RegaladoSG,ReadDF,SteemersFJ,DistecheCM,TrapnellC,ShendureJ.2018.ASingle-
CellatlasofinVivoMammalianChromatinAccessibility.Cell174:1309–1324.DOI:https://doi.org/10.1016/j.
cell.2018.06.052,PMID:30078704
DobrindtK,HoaglandDA,SeahC,KassimB,O’SheaCP,IskhakovaM,BrennandKJ.2020.Commongenetic
variationinhumansimpactsinvitrosusceptibilitytoSARS-CoV-2infection.bioRxiv.DOI:https://doi.org/10.
1101/2020.09.20.300574
DuY,TuL,ZhuP,MuM,WangR,YangP,WangX,HuC,PingR,HuP,LiT,CaoF,ChangC,HuQ,JinY,XuG.
2020.Clinicalfeaturesof85fatalcasesofCOVID-19fromWuhanAretrospectiveobservationalstudy.
AmericanJournalofRespiratoryandCriticalCareMedicine201:1372–1379.DOI:https://doi.org/10.1164/
rccm.202003-0543OC
EllinghausD,DegenhardtF,BujandaL,ButiM,AlbillosA,InvernizziP,Ferna´ndezJ,PratiD,BaselliG,AsseltaR,
GrimsrudMM,MilaniC,AzizF,Ka¨ssensJ,MayS,WendorffM,WienbrandtL,Uellendahl-WerthF,ZhengT,Yi
X,etal.2020.GenomewideassociationstudyofsevereCovid-19withrespiratoryfailure.TheNewEngland
JournalofMedicine383:2020283.DOI:https://doi.org/10.1056/NEJMoa2020283
ENCODEProjectConsortium.2012.AnintegratedencyclopediaofDNAelementsinthehumangenome.
Nature489:57–74.DOI:https://doi.org/10.1038/nature11247,PMID:22955616
FangR,PreisslS,HouX,LuceroJ,WangX,MotamediA,ShiauAK,MukamelEA,ZhangY,BehrensMM,Ecker
JR,RenB.2019.SnapATAC:acomprehensiveanalysispackageforsinglecellATAC-seq.bioRxiv.DOI:https://
doi.org/10.1101/615179
FornesO,Castro-MondragonJA,KhanA,vanderLeeR,ZhangX,RichmondPA,ModiBP,CorreardS,
GheorgheM,Baranasˇic´ D,Santana-GarciaW,TanG,Che`nebyJ,BallesterB,ParcyF,SandelinA,LenhardB,
WassermanWW,MathelierA.2020.JASPAR2020:updateoftheopen-accessdatabaseoftranscriptionfactor
bindingprofiles.NucleicAcidsResearch48:D87–D92.DOI:https://doi.org/10.1093/nar/gkz1001,
PMID:31701148
GrantCE,BaileyTL,NobleWS.2011.FIMO:scanningforoccurrencesofagivenmotif.Bioinformatics27:1017–
1018.DOI:https://doi.org/10.1093/bioinformatics/btr064,PMID:21330290
GTExConsortium.2020.TheGTExconsortiumatlasofgeneticregulatoryeffectsacrosshumantissues.Science
369:1318–1330.DOI:https://doi.org/10.1126/science.aaz1776,PMID:32913098
HeinzS,BennerC,SpannN,BertolinoE,LinYC,LasloP,ChengJX,MurreC,SinghH,GlassCK.2010.Simple
combinationsoflineage-determiningtranscriptionfactorsprimecis-regulatoryelementsrequiredfor
macrophageandBcellidentities.MolecularCell38:576–589.DOI:https://doi.org/10.1016/j.molcel.2010.05.
004,PMID:20513432
Wang,Chiou,Poirion,etal.eLife2020;9:e62522.DOI:https://doi.org/10.7554/eLife.62522 24of28

Researcharticle DevelopmentalBiology GeneticsandGenomics
HoffmannM,Kleine-WeberH,SchroederS,Kru¨gerN,HerrlerT,ErichsenS,SchiergensTS,HerrlerG,WuNH,
NitscheA,Mu¨llerMA,DrostenC,Po¨hlmannS.2020.SARS-CoV-2cellentrydependsonACE2andTMPRSS2
andisblockedbyaclinicallyprovenproteaseinhibitor.Cell181:271–280.DOI:https://doi.org/10.1016/j.cell.
2020.02.052,PMID:32142651
HoganBL,BarkauskasCE,ChapmanHA,EpsteinJA,JainR,HsiaCC,NiklasonL,CalleE,LeA,RandellSH,Rock
J,SnitowM,KrummelM,StrippBR,VuT,WhiteES,WhitsettJA,MorriseyEE.2014.Repairandregeneration
oftherespiratorysystem:complexity,plasticity,andmechanismsoflungstemcellfunction.CellStemCell15:
123–138.DOI:https://doi.org/10.1016/j.stem.2014.07.012,PMID:25105578
HuangIC,BoschBJ,LiW,FarzanM,RottierPM,ChoeH.2006.SARS-CoV,butnotHCoV-NL63,utilizes
cathepsinstoinfectcells:viralentry.AdvancesinExperimentalMedicineandBiology581:335–338.
DOI:https://doi.org/10.1007/978-0-387-33012-9_60,PMID:17037556
ImaiY,KubaK,RaoS,HuanY,GuoF,GuanB,YangP,SaraoR,WadaT,Leong-PoiH,CrackowerMA,Fukamizu
A,HuiCC,HeinL,UhligS,SlutskyAS,JiangC,PenningerJM.2005.Angiotensin-convertingenzyme2protects
fromsevereacutelungfailure.Nature436:112–116.DOI:https://doi.org/10.1038/nature03712,
PMID:16001071
Iwata-YoshikawaN,OkamuraT,ShimizuY,HasegawaH,TakedaM,NagataN.2019.TMPRSS2contributesto
virusspreadandimmunopathologyintheairwaysofmurinemodelsaftercoronavirusinfection.Journalof
Virology93:18.DOI:https://doi.org/10.1128/JVI.01815-18
JacobA,MorleyM,HawkinsF,McCauleyKB,JeanJC,HeinsH,NaCL,WeaverTE,VedaieM,HurleyK,HindsA,
RussoSJ,KookS,ZachariasW,OchsM,TraberK,QuintonLJ,CraneA,DavisBR,WhiteFV,etal.2017.
Differentiationofhumanpluripotentstemcellsintofunctionallungalveolarepithelialcells.CellStemCell21:
472–488.DOI:https://doi.org/10.1016/j.stem.2017.08.014,PMID:28965766
KarczewskiKJ,FrancioliLC,TiaoG,CummingsBB,Alfo¨ldiJ,WangQ,MacArthurDG.2019.Variationacross
141,456humanexomesandgenomesrevealsthespectrumofloss-of-functionintoleranceacrosshuman
protein-codinggenes.bioRxiv.DOI:https://doi.org/10.1101/531210
KimTS,HeinleinC,HackmanRC,NelsonPS.2006.PhenotypicanalysisofmicelackingtheTmprss2-encoded
protease.MolecularandCellularBiology26:965–975.DOI:https://doi.org/10.1128/MCB.26.3.965-975.2006,
PMID:16428450
KimCF.2017.Intersectionsoflungprogenitorcells,lungdiseaseandlungCancer.EuropeanRespiratoryReview
26:170054.DOI:https://doi.org/10.1183/16000617.0054-2017,PMID:28659499
KorsunskyI,MillardN,FanJ,SlowikowskiK,ZhangF,WeiK,BaglaenkoY,BrennerM,LohPR,RaychaudhuriS.
2019.Fast,sensitiveandaccurateintegrationofsingle-celldatawithharmony.NatureMethods16:1289–1296.
DOI:https://doi.org/10.1038/s41592-019-0619-0,PMID:31740819
KundajeA,MeulemanW,ErnstJ,BilenkyM,YenA,Heravi-MoussaviA,KheradpourP,ZhangZ,WangJ,Ziller
MJ,AminV,WhitakerJW,SchultzMD,WardLD,SarkarA,QuonG,SandstromRS,EatonML,WuYC,
PfenningAR,etal.2015.Integrativeanalysisof111referencehumanepigenomes.Nature518:317–330.
DOI:https://doi.org/10.1038/nature14248,PMID:25693563
LabN.2020.UK-Biobank.http://www.nealelab.is/uk-biobank/[AccessedAugust1,2018].
LanJ,GeJ,YuJ,ShanS,ZhouH,FanS,ZhangQ,ShiX,WangQ,ZhangL,WangX.2020.Structureofthe
SARS-CoV-2spikereceptor-bindingdomainboundtotheACE2receptor.Nature581:215–220.DOI:https://
doi.org/10.1038/s41586-020-2180-5,PMID:32225176
LareauCA,DuarteFM,ChewJG,KarthaVK,BurkettZD,KohlwayAS,PokholokD,AryeeMJ,SteemersFJ,
LebofskyR,BuenrostroJD.2019.Droplet-basedcombinatorialindexingformassive-scalesingle-cellchromatin
accessibility.NatureBiotechnology37:916–924.DOI:https://doi.org/10.1038/s41587-019-0147-6,PMID:31235
917
LeeD,GorkinDU,BakerM,StroberBJ,AsoniAL,McCallionAS,BeerMA.2015.Amethodtopredictthe
impactofregulatoryvariantsfromDNAsequence.NatureGenetics47:955–961.DOI:https://doi.org/10.1038/
ng.3331,PMID:26075791
LiH,HandsakerB,WysokerA,FennellT,RuanJ,HomerN,MarthG,AbecasisG,DurbinR,1000Genome
ProjectDataProcessingSubgroup.2009.Thesequencealignment/MapformatandSAMtools.Bioinformatics
25:2078–2079.DOI:https://doi.org/10.1093/bioinformatics/btp352,PMID:19505943
LiH,DurbinR.2009.FastandaccurateshortreadalignmentwithBurrows-Wheelertransform.Bioinformatics25:
1754–1760.DOI:https://doi.org/10.1093/bioinformatics/btp324,PMID:19451168
LimburgH,HarbigA,BestleD,SteinDA,MoultonHM,JaegerJ,JangaH,HardesK,KoepkeJ,SchulteL,
KoczullaAR,SchmeckB,KlenkH-D,Bo¨ttcher-Friebertsha¨userE.2019.TMPRSS2isthemajoractivating
proteaseofinfluenzaAvirusinprimaryhumanairwaycellsandinfluenzaBvirusinhumantypeIIpneumocytes.
JournalofVirology93:19.DOI:https://doi.org/10.1128/JVI.00649-19
MaedaY,Dave´ V,WhitsettJA.2007.Transcriptionalcontroloflungmorphogenesis.PhysiologicalReviews87:
219–244.DOI:https://doi.org/10.1152/physrev.00028.2006,PMID:17237346
MatsuyamaS,NaoN,ShiratoK,KawaseM,SaitoS,TakayamaI,NagataN,SekizukaT,KatohH,KatoF,Sakata
M,TaharaM,KutsunaS,OhmagariN,KurodaM,SuzukiT,KageyamaT,TakedaM.2020.Enhancedisolation
ofSARS-CoV-2byTMPRSS2-expressingcells.PNAS117:7001–7003.DOI:https://doi.org/10.1073/pnas.
2002589117,PMID:32165541
MauranoMT,HaugenE,SandstromR,VierstraJ,ShaferA,KaulR,StamatoyannopoulosJA.2015.Large-scale
identificationofsequencevariantsinfluencinghumantranscriptionfactoroccupancyinvivo.NatureGenetics
47:1393–1401.DOI:https://doi.org/10.1038/ng.3432,PMID:26502339
Wang,Chiou,Poirion,etal.eLife2020;9:e62522.DOI:https://doi.org/10.7554/eLife.62522 25of28

Researcharticle DevelopmentalBiology GeneticsandGenomics
McGinnisCS,MurrowLM,GartnerZJ.2019.DoubletFinder:doubletdetectioninSingle-CellRNAsequencing
datausingartificialnearestneighbors.CellSystems8:329–337.DOI:https://doi.org/10.1016/j.cels.2019.03.003
McInnesL,HealyJ,SaulN,GroßbergerL.2018.UMAP:uniformmanifoldapproximationandprojection.Journal
ofOpenSourceSoftware3:861.DOI:https://doi.org/10.21105/joss.00861
McLeanCY,BristorD,HillerM,ClarkeSL,SchaarBT,LoweCB,WengerAM,BejeranoG.2010.GREATimproves
functionalinterpretationofcis-regulatoryregions.NatureBiotechnology28:495–501.DOI:https://doi.org/10.
1038/nbt.1630,PMID:20436461
MogensenTH.2018.IRFandSTATtranscriptionfactors-Frombasicbiologytorolesininfection,protective
immunity,andprimaryimmunodeficiencies.FrontiersinImmunology9:3047.DOI:https://doi.org/10.3389/
fimmu.2018.03047,PMID:30671054
MooreJE,PurcaroMJ,PrattHE,EpsteinCB,ShoreshN,AdrianJ,KawliT,DavisCA,DobinA,KaulR,HalowJ,
VanNostrandEL,FreeseP,GorkinDU,ShenY,HeY,MackiewiczM,Pauli-BehnF,WilliamsBA,MortazaviA,
etal.2020.ExpandedencyclopaediasofDNAelementsinthehumanandmousegenomes.Nature583:699–
710.DOI:https://doi.org/10.1038/s41586-020-2493-4,PMID:32728249
MorriseyEE,CardosoWV,LaneRH,RabinovitchM,AbmanSH,AiX,AlbertineKH,BlandRD,ChapmanHA,
CheckleyW,EpsteinJA,KintnerCR,KumarM,MinooP,MarianiTJ,McDonaldDM,MukouyamaY,PrinceLS,
ReeseJ,RossantJ,etal.2013.MolecularDeterminantsofLungDevelopment.AnnalsoftheAmericanThoracic
Society10:S12–S16.DOI:https://doi.org/10.1513/AnnalsATS.201207-036OT
MorriseyEE,HoganBL.2010.Preparingforthefirstbreath:geneticandcellularmechanismsinlung
development.DevelopmentalCell18:8–23.DOI:https://doi.org/10.1016/j.devcel.2009.12.010,
PMID:20152174
MuusC,LueckenMD,EraslanG,WaghrayA,HeimbergG,SikkemaL.2020.Integratedanalysesofsingle-cell
atlasesrevealage,gender,andsmokingstatusassociationswithcelltype-specificexpressionofmediatorsof
SARS-CoV-2viralentryandhighlightsinflammatoryprogramsinputativetargetcells.bioRxiv.DOI:https://doi.
org/10.1101/2020.04.19.049254
OchsM,NyengaardJR,JungA,KnudsenL,VoigtM,WahlersT,RichterJ,GundersenHJ.2004.Thenumberof
alveoliinthehumanlung.AmericanJournalofRespiratoryandCriticalCareMedicine169:120–124.
DOI:https://doi.org/10.1164/rccm.200308-1107OC,PMID:14512270
PickrellJK.2014.Jointanalysisoffunctionalgenomicdataandgenome-wideassociationstudiesof18human
traits.TheAmericanJournalofHumanGenetics94:559–573.DOI:https://doi.org/10.1016/j.ajhg.2014.03.004,
PMID:24702953
PlinerHA,PackerJS,McFaline-FigueroaJL,CusanovichDA,DazaRM,AghamirzaieD,SrivatsanS,QiuX,
JacksonD,MinkinaA,AdeyAC,SteemersFJ,ShendureJ,TrapnellC.2018.Ciceropredictscis-Regulatory
DNAinteractionsfromSingle-Cellchromatinaccessibilitydata.MolecularCell71:858–871.DOI:https://doi.
org/10.1016/j.molcel.2018.06.044
PreisslS,FangR,HuangH,ZhaoY,RaviramR,GorkinDU,ZhangY,SosBC,AfzalV,DickelDE,KuanS,ViselA,
PennacchioLA,ZhangK,RenB.2018.Single-nucleusanalysisofaccessiblechromatinindevelopingmouse
forebrainrevealscell-type-specifictranscriptionalregulation.NatureNeuroscience21:432–439.DOI:https://
doi.org/10.1038/s41593-018-0079-3,PMID:29434377
QiF,QianS,ZhangS,ZhangZ.2020.SinglecellRNAsequencingof13humantissuesidentifycelltypesand
receptorsofhumancoronaviruses.bioRxiv.DOI:https://doi.org/10.1101/2020.02.16.951913
ReinkeLM,SpiegelM,PleggeT,HartleibA,NehlmeierI,GiererS,HoffmannM,Hofmann-WinklerH,WinklerM,
Po¨hlmannS.2017.DifferentresiduesintheSARS-CoVspikeproteindeterminecleavageandactivationbythe
hostcellproteaseTMPRSS2.PLOSONE12:e0179177.DOI:https://doi.org/10.1371/journal.pone.0179177,
PMID:28636671
ReyfmanPA,WalterJM,JoshiN,AnekallaKR,McQuattie-PimentelAC,ChiuS,FernandezR,AkbarpourM,
ChenC-I,RenZ,VermaR,Abdala-ValenciaH,NamK,ChiM,HanS,Gonzalez-GonzalezFJ,SoberanesS,
WatanabeS,WilliamsKJN,FlozakAS,etal.2019.Single-CellTranscriptomicAnalysisofHumanLungProvides
InsightsintothePathobiologyofPulmonaryFibrosis.AmericanJournalofRespiratoryandCriticalCare
Medicine199:1517–1536.DOI:https://doi.org/10.1164/rccm.201712-2410OC
RobinsonMD,McCarthyDJ,SmythGK.2010.edgeR:abioconductorpackagefordifferentialexpressionanalysis
ofdigitalgeneexpressiondata.Bioinformatics26:139–140.DOI:https://doi.org/10.1093/bioinformatics/
btp616,PMID:19910308
RobinsonJT,Thorvaldsdo´ttirH,WincklerW,GuttmanM,LanderES,GetzG,MesirovJP.2011.Integrative
genomicsviewer.NatureBiotechnology29:24–26.DOI:https://doi.org/10.1038/nbt.1754,PMID:21221095
SatpathyAT,GranjaJM,YostKE,QiY,MeschiF,McDermottGP,OlsenBN,MumbachMR,PierceSE,Corces
MR,ShahP,BellJC,JhuttyD,NemecCM,WangJ,WangL,YinY,GiresiPG,ChangALS,ZhengGXY,etal.
2019.Massivelyparallelsingle-cellchromatinlandscapesofhumanimmunecelldevelopmentandintratumoral
Tcellexhaustion.NatureBiotechnology37:925–936.DOI:https://doi.org/10.1038/s41587-019-0206-z,
PMID:31375813
SchillerHB,MontoroDT,SimonLM,RawlinsEL,MeyerKB,StrunzM,VieiraBragaFA,TimensW,Koppelman
GH,BudingerGRS,BurgessJK,WaghrayA,vandenBergeM,TheisFJ,RegevA,KaminskiN,RajagopalJ,
TeichmannSA,MisharinAV,NawijnMC.2019.Thehumanlungcellatlas:aHigh-Resolutionreferencemapof
thehumanlunginhealthanddisease.AmericanJournalofRespiratoryCellandMolecularBiology61:31–41.
DOI:https://doi.org/10.1165/rcmb.2018-0416TR,PMID:30995076
Wang,Chiou,Poirion,etal.eLife2020;9:e62522.DOI:https://doi.org/10.7554/eLife.62522 26of28

Researcharticle DevelopmentalBiology GeneticsandGenomics
SchulerBA,HabermannAC,PlosaEJ,TaylorCJ,JetterC,KappME.2020.Age-determinedexpressionof
primingproteaseTMPRSS2andlocalizationofSARS-CoV-2infectioninthelungepithelium.bioRxiv.
DOI:https://doi.org/10.1101/2020.05.22.111187
ShiratoK,KawaseM,MatsuyamaS.2018.Wild-typehumancoronavirusesprefercell-surfaceTMPRSS2to
endosomalcathepsinsforcellentry.Virology517:9–15.DOI:https://doi.org/10.1016/j.virol.2017.11.012,
PMID:29217279
SingerD,CamargoSM,RamadanT,Scha¨ferM,MariottaL,HerzogB,HuggelK,WolferD,WernerS,Penninger
JM,VerreyF.2012.DefectiveintestinalaminoacidabsorptioninAce2nullmice.AmericanJournalof
Physiology-GastrointestinalandLiverPhysiology303:G686–G695.DOI:https://doi.org/10.1152/ajpgi.00140.
2012,PMID:22790597
SmaleST,NatoliG.2014.Transcriptionalcontrolofinflammatoryresponses.ColdSpringHarborPerspectivesin
Biology6:a016261.DOI:https://doi.org/10.1101/cshperspect.a016261,PMID:25213094
StuartT,ButlerA,HoffmanP,HafemeisterC,PapalexiE,MauckWM,HaoY,StoeckiusM,SmibertP,SatijaR.
2019.ComprehensiveintegrationofSingle-Celldata.Cell177:1888–1902.DOI:https://doi.org/10.1016/j.cell.
2019.05.031,PMID:31178118
SudlowC,GallacherJ,AllenN,BeralV,BurtonP,DaneshJ,DowneyP,ElliottP,GreenJ,LandrayM,LiuB,
MatthewsP,OngG,PellJ,SilmanA,YoungA,SprosenT,PeakmanT,CollinsR.2015.UKbiobank:anopen
accessresourceforidentifyingthecausesofawiderangeofcomplexdiseasesofmiddleandoldage.PLOS
Medicine12:e1001779.DOI:https://doi.org/10.1371/journal.pmed.1001779,PMID:25826379
SungnakW,HuangN,Be´cavinC,BergM,QueenR,LitvinukovaM,Talavera-Lo´pezC,MaatzH,ReichartD,
SampaziotisF,WorlockKB,YoshidaM,BarnesJL,HCALungBiologicalNetwork.2020.SARS-CoV-2entry
factorsarehighlyexpressedinnasalepithelialcellstogetherwithinnateimmunegenes.NatureMedicine26:
681–687.DOI:https://doi.org/10.1038/s41591-020-0868-6,PMID:32327758
TataPR,RajagopalJ.2017.Plasticityinthelung:makingandbreakingcellidentity.Development144:755–766.
DOI:https://doi.org/10.1242/dev.143784,PMID:28246210
ThurmanRE,RynesE,HumbertR,VierstraJ,MauranoMT,HaugenE,SheffieldNC,StergachisAB,WangH,
VernotB,GargK,JohnS,SandstromR,BatesD,BoatmanL,CanfieldTK,DiegelM,DunnD,EbersolAK,Frum
T,etal.2012.Theaccessiblechromatinlandscapeofthehumangenome.Nature489:75–82.DOI:https://doi.
org/10.1038/nature11232,PMID:22955617
TraagVA,WaltmanL,vanEckNJ.2019.FromlouvaintoLeiden:guaranteeingwell-connectedcommunities.
ScientificReports9:5233.DOI:https://doi.org/10.1038/s41598-019-41695-z,PMID:30914743
TravagliniKJ,NabhanAN,PenlandL,SinhaR,GillichA,SitR,KrasnowMA.2020.Amolecularcellatlasofthe
humanlungfromsinglecellRNAsequencing.bioRxiv.DOI:https://doi.org/10.1101/742320
TynerC,BarberGP,CasperJ,ClawsonH,DiekhansM,EisenhartC,FischerCM,GibsonD,GonzalezJN,
GuruvadooL,HaeusslerM,HeitnerS,HinrichsAS,KarolchikD,LeeBT,LeeCM,NejadP,RaneyBJ,Rosenbloom
KR,SpeirML,etal.2017.TheUCSCgenomebrowserdatabase:2017update.NucleicAcidsResearch45:D626–
D634.DOI:https://doi.org/10.1093/nar/gkw1134,PMID:27899642
Vuille-dit-BilleRN,CamargoSM,EmmeneggerL,SasseT,KummerE,JandoJ,HamieQM,MeierCF,Hunziker
S,Forras-KaufmannZ,KuyumcuS,FoxM,SchwizerW,FriedM,LindenmeyerM,Go¨tzeO,VerreyF.2015.
HumanintestineluminalACE2andaminoacidtransporterexpressionincreasedbyACE-inhibitors.Amino
Acids47:693–705.DOI:https://doi.org/10.1007/s00726-014-1889-6,PMID:25534429
WallsAC,ParkYJ,TortoriciMA,WallA,McGuireAT,VeeslerD.2020.Structure,function,andantigenicityof
theSARS-CoV-2spikeglycoprotein.Cell181:281–292.DOI:https://doi.org/10.1016/j.cell.2020.02.058,
PMID:32155444
WangJ,ZhuangJ,IyerS,LinX,WhitfieldTW,GrevenMC,PierceBG,DongX,KundajeA,ChengY,RandoOJ,
BirneyE,MyersRM,NobleWS,SnyderM,WengZ.2012.Sequencefeaturesandchromatinstructurearound
thegenomicregionsboundby119humantranscriptionfactors.GenomeResearch22:1798–1812.DOI:https://
doi.org/10.1101/gr.139105.112,PMID:22955990
WangX,ParkJ,SusztakK,ZhangNR,LiM.2019.Bulktissuecelltypedeconvolutionwithmulti-subjectsingle-
cellexpressionreference.NatureCommunications10:380.DOI:https://doi.org/10.1038/s41467-018-08023-x,
PMID:30670690
WangA.2020.analyticaltools.GitHub.2d21594.https://github.com/kjgaulton/pipelines/
WaradonSungnakNH,Be´cavinC,BergM.2020.SARS-CoV-2entrygenesaremosthighlyexpressedinnasal
gobletandciliatedcellswithinhumanairways.arXiv.https://arxiv.org/abs/2003.06122.
WhitsettJA,WeaverTE.2015.Alveolardevelopmentanddisease.AmericanJournalofRespiratoryCelland
MolecularBiology53:1–7.DOI:https://doi.org/10.1165/rcmb.2015-0128PS,PMID:25932959
WolfFA,AngererP,TheisFJ.2018.SCANPY:large-scalesingle-cellgeneexpressiondataanalysis.Genome
Biology19:15.DOI:https://doi.org/10.1186/s13059-017-1382-0,PMID:29409532
XuY,WangY,BesnardV,IkegamiM,WertSE,HeffnerC,MurraySA,DonahueLR,WhitsettJA.2012.
Transcriptionalprogramscontrollingperinatallungmaturation.PLOSONE7:e37046.DOI:https://doi.org/10.
1371/journal.pone.0037046,PMID:22916088
XuY,MizunoT,SridharanA,DuY,GuoM,TangJ,Wikenheiser-BrokampKA,PerlA-KT,FunariVA,GokeyJJ,
StrippBR,WhitsettJA.2016.Single-cellRNAsequencingidentifiesdiverserolesofepithelialcellsinidiopathic
pulmonaryfibrosis.JCIInsight1:e90558.DOI:https://doi.org/10.1172/jci.insight.90558
YanR,ZhangY,LiY,XiaL,GuoY,ZhouQ.2020.StructuralbasisfortherecognitionofSARS-CoV-2byfull-
lengthhumanACE2.Science367:1444–1448.DOI:https://doi.org/10.1126/science.abb2762,PMID:32132184
Wang,Chiou,Poirion,etal.eLife2020;9:e62522.DOI:https://doi.org/10.7554/eLife.62522 27of28

Researcharticle DevelopmentalBiology GeneticsandGenomics
ZhangY,LiuT,MeyerCA,EeckhouteJ,JohnsonDS,BernsteinBE,NusbaumC,MyersRM,BrownM,LiW,Liu
XS.2008.Model-basedanalysisofChIP-Seq(MACS).GenomeBiology9:R137.DOI:https://doi.org/10.1186/
gb-2008-9-9-r137,PMID:18798982
ZhaoY,ZhaoZ,WangY,ZhouY,MaY,ZuoW.2020.Single-cellRNAexpressionprofilingofACE2thereceptor
ofSARS-CoV-2.bioRxiv.DOI:https://doi.org/10.1101/2020.01.26.919985
ZhengGX,TerryJM,BelgraderP,RyvkinP,BentZW,WilsonR,ZiraldoSB,WheelerTD,McDermottGP,ZhuJ,
GregoryMT,ShugaJ,MontesclarosL,UnderwoodJG,MasquelierDA,NishimuraSY,Schnall-LevinM,Wyatt
PW,HindsonCM,BharadwajR,etal.2017.Massivelyparalleldigitaltranscriptionalprofilingofsinglecells.
NatureCommunications8:14049.DOI:https://doi.org/10.1038/ncomms14049,PMID:28091601
ZhouY,VedanthamP,LuK,AgudeloJ,CarrionR,NunneleyJW,BarnardD,Po¨hlmannS,McKerrowJH,Renslo
AR,SimmonsG.2015.ProteaseinhibitorstargetingcoronavirusandFilovirusentry.AntiviralResearch116:76–
84.DOI:https://doi.org/10.1016/j.antiviral.2015.01.011,PMID:25666761
ZhouN,PanT,ZhangJ,LiQ,ZhangX,BaiC,HuangF,PengT,ZhangJ,LiuC,TaoL,ZhangH.2016.
GlycopeptideantibioticspotentlyinhibitcathepsinLinthelateendosome/Lysosomeandblocktheentryof
ebolavirus,middleeastrespiratorysyndromecoronavirus(MERS-CoV),andsevereacuterespiratorysyndrome
coronavirus(SARS-CoV).JournalofBiologicalChemistry291:9218–9232.DOI:https://doi.org/10.1074/jbc.
M116.716100,PMID:26953343
ZieglerCGK,AllonSJ,NyquistSK,MbanoIM,MiaoVN,TzouanasCN,CaoY,YousifAS,BalsJ,HauserBM,
FeldmanJ,MuusC,WadsworthMH,KazerSW,HughesTK,DoranB,GatterGJ,VukovicM,TaliaferroF,Mead
BE,etal.2020.SARS-CoV-2receptorACE2isanInterferon-Stimulatedgeneinhumanairwayepithelialcells
andisdetectedinspecificcellsubsetsacrosstissues.Cell181:1016–1035.DOI:https://doi.org/10.1016/j.cell.
2020.04.035,PMID:32413319
ZouX,ChenK,ZouJ,HanP,HaoJ,HanZ.2020.Single-cellRNA-seqdataanalysisonthereceptorACE2
expressionrevealsthepotentialriskofdifferenthumanorgansvulnerableto2019-nCoVinfection.Frontiersof
Medicine14:185–192.DOI:https://doi.org/10.1007/s11684-020-0754-0,PMID:32170560
Wang,Chiou,Poirion,etal.eLife2020;9:e62522.DOI:https://doi.org/10.7554/eLife.62522 28of28