Resource
A human fetal lung cell atlas uncovers proximal-
distal gradients of differentiation and key regulators
of epithelial fates
Graphical abstract Authors
PengHe,KyungtaeLim,DaweiSun,...,
JohnC.Marioni,KerstinB.Meyer,
EmmaL.Rawlins
Correspondence
e.rawlins@gurdon.cam.ac.uk
In brief
Multiomicanalysisofhumanfetallungs
from5–22post-conceptionweeksunveils
cell-lineagetrajectoriesacrossdifferent
celltypesduringdevelopmentandwill
providefreshinsightsintolungdisease
progressioninadults.
Highlights
d Spatiotemporalatlasofhumanlungdevelopmentidentifies
144celltypes/states
d Trackingthedevelopmentaloriginsofmultiplecelltypes,
includingnewprogenitors
d Functionaldiversityoffibroblastsindistinctanatomical
signalingniches
d ExperimentalvalidationofTFscontrollingneuroendocrine
cellheterogeneity
Heetal.,2022,Cell185,4841–4860
December8,2022ª2022TheAuthor(s).PublishedbyElsevierInc.
ll
https://doi.org/10.1016/j.cell.2022.11.005

ll
OPENACCESS
Resource
A human fetal lung cell atlas uncovers
proximal-distal gradients of differentiation
and key regulators of epithelial fates
PengHe,1,2,15KyungtaeLim,3,15DaweiSun,3,13,15JanPatrickPett,1QuitzJeng,3KrzysztofPolanski,1ZiqiDong,3
LiamBolt,1,11LauraRichardson,1LiraMamanova,1,12MonikaDabrowska,1AnnaWilbrey-Clark,1EloMadissoon,1,2
ZewenKelvinTuong,1,4EmmaDann,1ChenquSuo,1,5IsaacGoh,6MasahiroYoshida,7MarkoZ.Nikolic(cid:1),7SamM.Janes,7
XiaolingHe,8RogerA.Barker,8SarahA.Teichmann,1,9,14JohnC.Marioni,1,2,10,14KerstinB.Meyer,1,14
andEmmaL.Rawlins3,14,16,*
1WellcomeSangerInstitute,Hinxton,CambridgeCB101SA,UK
2EuropeanMolecularBiologyLaboratory,EuropeanBioinformaticsInstitute(EMBL-EBI),WellcomeGenomeCampus,Cambridge,UK
3WellcomeTrust/CRUKGurdonInstitute,DepartmentofPhysiology,DevelopmentandNeuroscience,UniversityofCambridge,Cambridge
CB21QN,UK
4MolecularImmunityUnit,UniversityofCambridgeDepartmentofMedicine,Cambridge,UK
5DepartmentofPaediatrics,CambridgeUniversityHospitals,HillsRoad,CambridgeCB20QQ,UK
6BiosciencesInstitute,NewcastleUniversity,NewcastleuponTyne,NE24HH,UK
7LungsforLivingResearchCentre,UCLRespiratory,UniversityCollegeLondon,London,UK
8JohnvanGeestCentreforBrainRepair,DepartmentofClinicalNeurosciencesandWellcome-MRCCambridgeStemCellInstitute,
UniversityofCambridge,Cambridge,UK
9DepartmentofPhysics,CavendishLaboratory,UniversityofCambridge,CambridgeCB30HE,UK
10CancerResearchUKCambridgeInstitute,UniversityofCambridge,Cambridge,UK
11Presentaddress:GenomicsEngland,HinxtonCB101DR,UK
12Presentaddress:CSGenomics,CambridgeCB12JH,UK
13Presentaddress:BroadInstituteofMassachusettsInstituteofTechnologyandHarvard,Cambridge,MA02142,USA
14Seniorauthor
15Theseauthorscontributedequally
16Leadcontact
*Correspondence:e.rawlins@gurdon.cam.ac.uk
https://doi.org/10.1016/j.cell.2022.11.005
SUMMARY
We present a multiomic cell atlas of human lung development that combines single-cell RNA and ATAC
sequencing,high-throughputspatialtranscriptomics,andsingle-cellimaging.Couplingsingle-cellmethods
withspatialanalysishasallowedacomprehensivecellularsurveyoftheepithelial,mesenchymal,endothelial,
anderythrocyte/leukocytecompartmentsfrom5–22post-conceptionweeks.Weidentifypreviouslyunchar-
acterizedcellstatesinallcompartments.Theseincludedevelopmental-specificsecretoryprogenitorsanda
subtypeofneuroendocrinecellrelatedtohumansmallcelllungcancer.Ourdatasetsareavailablethrough
ourwebinterface(https://lungcellatlas.org).Toillustrateitsgeneralutility,weuseourcellatlastogenerate
predictionsaboutcell-cellsignalingandtranscriptionfactorhierarchieswhichwerigorouslytestusingorga-
noidmodels.
INTRODUCTION tors and predict differentiation trajectories and potential gene
regulatory networks. This will provide a baseline for studying
Single-cell mapping of cell states in the adult human lung in adulthomeostasisanddisease.
healthanddiseaseisbeingperformedatincreasingresolution,1 Thelungbudsarespecifiedinthehumanforegutendodermat
providing a foundation for understanding lung cellular physi- (cid:1)5 post-conception weeks (pcw).4,5 Subsequent morphogen-
ology.Theadultlunghaslowratesofcellturnover,2,3makingit esisisdrivenbybranchingofthedistal-mostbudtips.Thebud
difficulttocapturetransitionstatesandprogenitors.Moreover, tip epithelium comprises SOX9+, ID2+ multipotent progenitors
therearedevelopmental-specificcellstatesthatdonotexistin that self-renew during branching.6–9 As the bud tip epithelium
theadult.Ahigh-resolutioncellatlasoftheembryonicandfetal branches into the surrounding mesoderm, the epithelial
humanlungwillidentifydevelopmentalprecursorsandprogeni- cells that remain in the stalk region start to differentiate into
Cell185,4841–4860,December8,2022ª2022TheAuthor(s).PublishedbyElsevierInc. 4841
ThisisanopenaccessarticleundertheCCBYlicense(http://creativecommons.org/licenses/by/4.0/).

ll
OPENACCESS Resource
(legendonnextpage)
4842 Cell185,4841–4860,December8,2022

ll
Resource OPENACCESS
bronchiolar(airway,(cid:1)5–16pcw)andlater(from(cid:1)16pcw)into approximation and projection(UMAP)(Figure1A), onwhich we
alveolar epithelium.5 The pattern of growth from multipotent manuallyannotatedfibroblast,epithelial,endothelial,anderythro-
epithelial progenitors at the distal tips means that the position cyte/leukocytelineages(Figure1B).Plottingthecell-typedistribu-
ofacellalongtheproximal-distalaxisofthelungepithelialtree tion against time (excluding trypsin/CD326-treated samples,
isastrongpredictorofitsmaturity.Themorematurecells,which showninFigureS1B)showedthatfibroblastswerethemostprom-
exitedthetipfirst,aremoreproximal,whereasthemostimma- inentcell,particularlyinyoungerlungs(Figure1C).Leukocytesand
ture cell states, which exited the tip recently, are found in the erythrocyteswereobservedinalllungssampled,withB,T,andNK
tip-adjacent (stalk) regions.10 In other words, space reflects cellsbecomingprominentfrom15pcw(Figure1C).
timeinlungdevelopment. Therefore, couplingsingle-cellstate Furthercell-typeannotationwasperformedbasedonmarker
analysis to in vivo spatial visualization can provide high genes(TableS1),resultinginassignmentof144celltypes/states
confidence in the identification of novel progenitor cells in the (Figure1D).Sampleagewasastrongdeterminantofclustering
developing lung. Moreover, detailed spatial analysis of cell (c2 = 163,727, p z 0), reflecting progressive cell maturity over
states allows cell identity designations to be compared to time (Figure 1E). Clusters mostly grouped into three distinct
moretraditionalhistologicaldefinitions. regions which we categorized as early (5, 6 pcw), mid (9–11
Wehavegeneratedahigh-resolutionsingle-cellatlasofhuman pcw),andlate(15–22pcw)stages.Cellcyclephase(FigureS1M,
lungdevelopmentusingacombinationofscRNA-seq,scATAC- c2=25,361,pz0)anddissectedregion(Figure1F,c2=968,p=
seq,VisiumSpatialTranscriptomics,andmRNAinsituhybridiza- 8.9E-131) were also associated with clustering. However, the
tionusinghybridizationchainreaction(HCR).11Combiningthese dissection region was only prominent for a small number of
datasourceshasallowedustoidentify144cellstates/typesin proximally located cell types (Figure 1F), suggesting that most
5–22pcwlungsamples.Theseincludepreviouslyuncharacter- proximal-to-distalregionsoftheairwaystructurewerestillrepre-
izedprogenitorcellstates,transitionpopulations,andasubtype sentedinbothdissectedregionsofthelung.Epithelialcellswere
ofneuroendocrinecellrelatedtoasubtypeofhumansmallcell mostly derived from the trypsin-treated and CD326-enriched
lung cancer (SCLC). We observe increasing cell maturation samples, although airway smooth muscle, myofibroblasts, and
overtime,withmanycellstatesidentifiedinadultlungsalready alveolarfibroblastswerealsoenrichedhere(FigureS1M’).Periph-
presentat22pcw.Wehaveusedouratlastomakepredictions eralnervoussystem(PNS)cellsandchondrocyteswereonlyob-
aboutprogenitorcellstates,signalinginteractions,andlineage- tainedfrom5–6pcwlungs,likelycorrelatingwithlowerextracel-
defining transcription factors, and we demonstrate how these lularmatrix(ECM)complexityinyoungerlungsand/orincreased
canbeefficientlytestedusingageneticallytractablehumanfetal fragilityofolderneurons.PNScellswereclusteredandassigned
lungorganoidmodel.Thedatasetsareavailableforinteractive tocelltypes,butscarcityprecludedfurtheranalysis(Figure1D,
analysisathttps://lungcellatlas.org. S1N, and S1N’). Data integration and logistic regression-based
comparisonshowedthatgeneexpressionofourannotatedcells
RESULTS correspondswelltothoseofadultlungs14(FiguresS2A–S2C).
Asingle-cellatlasofhumanlungdevelopment Adifferentiationtrajectoryofairwayprogenitorstates
comprising144cellstates liesalongthedevelopinglungdistal-to-proximalaxis
Weobtainedhumanembryonicandfetallungsfrom5–22pcwfor The epithelial cells separate by age (Figures 2A and 2B), with
scRNA-seq and scATAC-seq. To focus on differentiation, we manybasalcells,MUC16+ciliatedcells,andsecretorycellsen-
deeplysampled15,18,20,and22pcwlungsandseparatedprox- richedintheproximallydissectedtissue(Figures2BandS1O).
imalanddistalregions,whileleavinglungsat5,6,9,and11pcw The most immature epithelial progenitors are tip cells: SOX9+
intact.Weusedamixtureofcelldissociationmethodstoobtain multipotent progenitors located at the distal branching tips of
abalancedmixtureofcelltypes(Figure1A)andproducedhigh- the respiratory tree.8 Tip cells were separated into early (5,6
quality transcriptome (Figure S1A; average > 2,400 genes/cell) pcw), mid (9–11 pcw) and late (15–22 pcw) populations
andDNAaccessibility(FiguresS1KandS1L;average>18,000 (Figures2Aand2B)withbothsharedandstage-specificmarkers
fragments/nucleus) data. After iterative clustering (Figures S1C (Figure2C).OntheepithelialUMAP,eachtippopulationclusters
andS1D),removalofdoublet-drivenclusters(FiguresS1E,S1G, closely with adjacent stalk cells (SOX9LO/-, PDPNLO, HOPXLO)
S1G’,andS1G’’),stressedorlow-qualityclusters(exceptthose andairwayprogenitors(CYTL1LO/+,PCP4+,SCGB3A+/LO)(Fig-
expressingknownmarkers,suchaserythroid)(FiguresS1I,S1I’, ure2A).Thetip,stalk,andairwayprogenitorscanbevisualized
and S1I’’), clusters composed of cells from only one sample in adistal-proximal sequencein the tissueat all stagestested
whenreplicatesareavailable,andclustersofcellsfromotheror- (10–16 pcw) (Figures 2E, S3A, and S1B, Video S1), consistent
gans(FigureS1H)12,13andmaternalcellevaluation(FiguresS1F withthemostproximalcellsbeingthemostmature.Thesethree
andS1J),wepresent71,752cellsshownasauniformmanifold celltypesformapredicteddifferentiationtrajectoryfrommid-tip
Figure1. Dataandexperimentaloverview
(A)OverviewofsamplecollectionforscRNA-seq(circles)andscATAC-seq(squares)experimentsfromwholelung(purple),distal(red),andproximal(blue)
regions,cellprocessingandbroadclustering;clusternumberreferstothedataportal(https://lungcellatlas.org).
(BandC)UMAPrepresentation(B)andcell-typeproportion(C)of71,752good-qualitycells,indicatingepithelial,endothelial,fibroblast,andleukocyte/erythroid
compartments.
(D–F)UMAPvisualizationbycelltype/state(D),developmentalstage(E),anddissectionregion(F).SeealsoFiguresS1andS2.
Cell185,4841–4860,December8,2022 4843

ll
OPENACCESS Resource
(legendonnextpage)
4844 Cell185,4841–4860,December8,2022

ll
Resource OPENACCESS
to mid-stalk to mid-airway progenitor that branches into the luminalproximalsecretorycellpopulationswerelocatedinthe
neuroendocrine,orsecretory,lineages(Figure2D). proximal cartilaginous airways and were MUC16+(Figures 2C,
2G, 2H, S3E, and S3F). Detailed spatial-temporal analysis of
Twosubtypesofneuroendocrinecellsarepresentinthe 10–21 pcw airways revealed that the proportion of proximal
developingairways secretoryprogenitorsdecreasedwithdevelopmentalage,while
Consistentwithpreviousdata,15theearliestdifferentiatedepithe- proximalsecretorycells1and2increased(FiguresS4A–S4C),
lialcellsdetectedwereneuroendocrine(NE)cellsin5pcwlungs consistent with a progenitor function for proximal secretory
(Figures2A–2C).WeidentifiedtwotypesofNEcells:classicalpul- progenitors.
monaryNE cells (GRP+) and GHRL+ NE cells (TTR+, GHRL+) in
agreement with a recent human fetal cell atlas.13 We observed Otherairwaycells
increasingmaturityofNEcellsovertime(specificpopulationsde- Wedetectedciliatedcells(FOXJ1+,ALOX15+)from11pcw,inter-
notedasprecursorsontheUMAP).Inaddition,anintermediateNE spersedwithsecretory/clubcells(Figures2A–2C,S3H,S4A,and
population,aputativetransitionstate,connectedthetwoNEcells S4B).Rarerdeuterosomalcells(FOXJ1+,CDC20B+)appearedat
(Figure2A).At11pcw,GRP+pulmonaryNEcellswereobserved thesametime(Figures2A–2C).MUC16+ciliatedcells(FOXJ1+,
closertothebuddingtips,suggestingthattheybegintoformprior DNAH+,MUC16LO)werealsodetectedfrom11pcwbutconfined
totheGHRL+NEcells(Figure2F).Thisspatialdifferencewasnot toproximaldissectedregions(Figures2A–2CandS3H).Theywere
apparentintheoldestsampleswherebothGRP+andGHRL+cells locatedinpatchesinthemostproximalcartilaginousairways(Fig-
wereobservedatallairwaylevels,althoughlessabundantdistally ureS3I)andlikelyrepresentMUC16+secretorycellsgenerating
(FigureS3C).MouseGhrl+NEcellswerenotdetectedinre-anal- ciliatedcells,assuggestedintheadult.19–21Basalcells(TP63+,
ysisofpublished mouse data,16,17orspatially.18However,Ghrl F3+) were present from 9 pcw (Figures 2A–2C and S3J) and
isexpressedinmouseciliatedcellsthatclusterwithhumanfetal more frequent in proximal regions (Figures 2C, S4A, and S4B).
GHRL+NEcells(FigureS2D).17 Rarercells(ionocytes,tuft)thathavebeenidentifiedinadultair-
wayswerenotpresentinoursingle-celldata.However,wefound
Multiplesecretorycellsubtypesintheproximal putative ionocytes (FOXI1+; 4/4 lungs) and putative tuft cells
cartilaginousairways (POU2F3+;2/4lungs)inthemostproximalcartilaginousairways
Weannotated5sub-typesofdifferentiatingsecretorycellsand of21–22pcwlungsections(FigureS4E),suggestingtheybegin
one proximal secretory progenitor. (1) The proximal secretory to differentiate mid-gestation. Moreover, we reproducibly de-
progenitors (SCGB3A2+, SCGB1A1-, SCGB3A1-/LO, CYTL1+) tected a small population of MUC5AC+, ASCL1+ cells in 9–11
weredetectedinthesingle-cellatlasat9pcw,prominentat11 pcwlungs(Figures2A–2C).Thesewerelocalizedtotheproximal
pcw,butrarerinolderlungsconsistentwithaprogenitorstate non-cartilaginousairwayswheretheyappearedassolitary,some-
(Figures2A–2C,and2G).(2)Clubcells(SCGB3A2+,SCGB1A1+, whatbasal,non-columnarcells(FigureS3K).Wehypothesizethat
SCGB3A1-,SPDEF-,MUC16-)weredetectedfrom15pcwinthe they are an unknown progenitor, consistent with their transient
single-celldata(Figures2A–2C,and2G),or12pcwinthetissue appearance and the observation that Ascl1+ NE cells in adult
localized in clusters more distally, but dispersed in the more mice can generate club, ciliated, and mucous cells following
proximalnon-cartilaginousregions(FigureS3D).(3)Submucosal injury.22,23
gland (SMG) secretory cells (LTF+, SCGB3A1+, SPDEF+) were
detected from 15 pcw in the single-cell data, located in SMG Predictedairwayepithelialdifferentiationtrajectories
ducts and likely to be a precursor of serous and/or mucous- Adetailedspatiotemporalanalysisofmajorairwayepithelialcell
secretingSMGcells(Figures2A–2C,2G,andS3G).(4)Proximal typesfrom10–21pcwconfirmsthatcellmaturationbeginsmore
secretory1(SCGB1A1LO,SCGB3A2+,SCGB3A1+)and(5)prox- proximally.Anexampleislackofciliatedandclubcellsinthedistal
imalsecretory2(SCGB1A1+,SCGB3A2+,SCGB3A1+)appeared non-cartilaginous airways at 10–12 pcw but presenceat 15–21
from 11 pcw (Figure 2A–2C, 2G–2H, and S3E). Both were pcw(FiguresS4A–S4D).Conversely,airwayprogenitorsarefound
SPDEF+, MUC5B+, SERPINA1+ (Figure 2I), suggesting they throughout the non-cartilaginous airways at 10–12 pcw but
differentiateintogobletormucouscells.Bycontrast,(6)proximal restrictedtoterminalairwaysby15–21pcw(FiguresS4A–S4D).
secretory 3 (SCGB1A1+, SCGB3A2LO/-, SCGB3A1+) was de- Inaddition,proximalsecretorycellsarespatiallyrestrictedtothe
tected from 15 pcw and was SPDEF- (Figures 2A–2C), but cartilaginousairways,whileclubcellsarefoundinthenon-cartilag-
CYP2F1+, MUC4+, and KRT4+(Figures 2G and 2J). All three inousregions(FiguresS4A–S4D).
Figure2. Epithelialcelltypes,states,andlocationsoverdevelopmentaltime
(AandB)UMAPvisualizationofepithelialcells,coloredbycelltypes(A),stage(B,left),andregion(B,right).
(C)Dotplotdescribingdifferentialmarkergeneexpressionlevelforepithelialcells.
(D)UMAPvisualizingthepredictedepithelialcelllineagetrajectoryusingscvelo;inset:developmentalage.
(EandF)InsituHCRat11(F)and12(E)pcw.(E)SOX9(tipepithelium,white),CYTL1(red),SCGB3A2(green).(F)GHRL+(GHRL+neuroendocrine,red),GRP+
(pulmonaryneuroendocrine,green).
(G)Dotplotshowingdifferentialmarkergenesacrosssecretorycellsubtypes.
(H)InsituHCRat19pcwusingSCGB1A1(red),SCGB3A2(green),andSCGB3A1(white).
(IandJ)Differentiallyenrichedgenesintheproximalsecretorycellsubtypes.SPDEF(I,I’),SERPINA1(I’’),CYP2F1(J),MUC4(J’),andKRT4(J’’)allwhite;MUC5B
(I’)andSCGB1A1allred,andSCGB3A2green.DAPI,nuclei.Scalebars,50mm.SeealsoFiguresS3,S4,andS5.
Cell185,4841–4860,December8,2022 4845

ll
OPENACCESS Resource
(legendonnextpage)
4846 Cell185,4841–4860,December8,2022

ll
Resource OPENACCESS
This spatial separation means that predicted differentiation SCGB3A2-GFP+ cells fromthe samelungs (FigureS5H). When
trajectoriesthatcombineproximalsecretorycellsandclubcells singlecellswereplacedintoanFGF-containingdifferentiationme-
(Figure2,D)canrevealgeneraltrendsbutarelikelytobeover- dium,27distalSCGB3A2-GFP+cellsproducedbasal,ciliated,and
simplified.Wethereforepredictedmid-(FiguresS5A–S5C)and maturesecretorycells(FiguresS5I–S5M).Thisdemonstratesthat,
late-stage (Figures S5D–S5F) airway lineage trajectories sepa- consistentwiththetrajectoryanalysis,theairwayprogenitorsare
rately. In both cases, basal cells formed discrete clusters on competenttodifferentiateintoairwaylineages.
theUMAPs(FiguresS5A’andS5D’).Trajectoryinferenceanal- In summary, we have identified multiple epithelial progenitor
ysis suggests a differentiation route from mid-tip to stalk to states(tip,stalk,airwayprogenitor,andproximalsecretorypro-
airwayprogenitorstoproximalsecretoryprogenitorsandprox- genitor) and differentiating airwaycells that localizetoa spatial
imal secretory cells (Figure S5B), consistent with sample age differentiationgradientalongtheproximal-distalaxisoftheepithe-
(FigureS5B’).Visualizinggeneexpressionalongtheinferredtra- lium(summarizedinFiguresS3LandS4D).Moreover,weidentify
jectory shows mid-tip and stalk cells are similar (Figure S5C). GHRL+neuroendocrinecellsthatdonotexistinthemouse.
Stalkcellslosesometipmarkers,includingFOXP2andSOX9,
andgainasmallnumberofgenes,includingPDPNandAGER. Lateepithelialtipcellsacquirealveolaridentitypriorto
By contrast, the newly defined airway progenitors upregulate alveolardifferentiation
marker genes associated with airway fates, including CYTL1, Tipcellsexpressacoresetoftip-specificmarkers(SOX9+,ETV5+,
CLDN4,andSCGB3A224,25(FigureS5C).Asimilardifferentiation TESC+,TPPP3+,andSTC1+)atallstagessampled(Figures2A–
trajectorywaspredictedfromlate-tiptolate-stalktolate-airway 2C).We observeda gradual decrease in tip markerexpression
progenitortoclubcells(FigureS5E),althoughtheoldesttipand andanincreaseinalveolartype2(AT2)cellgeneexpressionin
stalk cells included in this analysis may produce alveolar line- tipcellswithdevelopmentalage(Figure2C).By15pcwtheAT2
ages (Figures S5E’, 3C, 3E, S6A, and S6B). Visualizing gene markersSFTPCandSFTPAweredetectedreadilyinlate-tipcells
expressionalongtheinferredlate-airwaytrajectoryshowsthat where they were co-expressed with lower levels of core tip
the late-tip and stalk cells are transcriptionally similar and un- markers(Figures3Aand3B).Thelatetipisatranscriptionalstate
dergogeneexpressionchangesanalogoustomid-tipandstalk thathasnotbeendetectedindevelopingmouselungs.17,28The
(lossofSOX9,FOXP2;gainofPDPN,AQP5;FigureS5F). changeinexpressionprofilethatisobserveduponthetransition
Theseanalysespredictthatcellsexitthetiptothestalkstate,fol- tolatetipscorrelateswithachangeinthepredicteddifferentiation
lowedbygainofairwayprogenitoridentitybeforecommitmenttoa trajectoryfromlate-tipcellstolate-stalktofetalAT2andAT1cells
specificdifferentiationstatethatlikelydependsonlocalsignaling (Figures3Cand3D;withoutlatestalkinS6A).However,trajectory
cues.Althoughwecannotpredicttheoriginofthebasalcellsusing inferenceanalysisatthistransitionalstageischallenging.Itislikely
trajectoryinferencemethods,wehypothesizethattheyarederived thatsomeofthelate-tipcellsproducetheterminalbranchesofthe
fromacolumnarprogenitor(possiblytheairwayprogenitor)butwill conducting airways (Figures S5D–S5F). Moreover, the inferred
themselvesactasprogenitor/stemcellsfollowingdifferentiation connections between mid-tip and late-tip cells are weak (Fig-
analogoustopreviousobservationsinmice.26 ure 3C), and we cannot exclude a novel origin for late-tip cells
Ourtrajectoryinference(FiguresS5A–S5F)predictsthatairway perhaps emerging as new buds from a stalk position, although
progenitorswilldifferentiatereadilytoairwaycelltypes.At9–10 this hypothesis is not strongly supported by our analysis (Fig-
pcw, CYTL1+ and SCGB3A2+ airway progenitors are found ure 2D). Nevertheless, throughout this period, similar to earlier
throughout the airway tree (Figures 2E, S3B, S3D, S3L, S4A, stages,late-tipcellsremainSOX9+andlate-stalkcellsturnofftip
S4B,andS4D).Weisolatedairwayprogenitorsusingacombina- markersandacquirePDPN/AGER(FiguresS3AandS6D).
tion of distal non-cartilaginous airway micro-dissection and AsmallnumberofAT2cellsappearinthesingle-celldatafrom
transduction with a lentiviral SCGB3A2 transcriptional reporter 15pcwbutaremoreprominentfrom22pcw(Figure2A).Simi-
(SCGB3A2-GFP,FigureS5G).FreshlyisolateddistalSCGB3A2- larly, ataround 16 pcw, late-tipcells (SOX9+,TPPP3+,SFTPC+)
GFP+ cells were SOX9LO, CYTL1HI, SCGB1A1LO, SCGB3A2LO, wereclearlyvisualizedinthetissue,butdifferentiatingAT2cells
andSCGB3A1LOcomparedtotip/stalkcellsandmoreproximal (SOX9LO/-,TPPP3LO/-,SFTPC+)wererare(Figures3Fand3G,and
Figure3. Lateepithelialtipcellsacquireanalveolarprogenitoridentity
(AandB)InsituHCRat11(AandB),15(B),and19(A)pcw.(A)SFTPC(green),TPPP3(red),SOX9(white).(B)SFTPC(green),SFTPA1(red),STC1(white).Dashed
linesrepresenttipepithelium.
(CandD)UMAPvisualizationofearlytolatetip,latestalk,fetalAT1andAT2cells,coloredbycelltypes(C)andstages(C’);PAGAanalysis(C’’);Monocle3
trajectories(D).
(E)Geneexpressionheatmapoftrajectorycoloredin(D).
(F)InsituHCRat16,19,and21pcw,SFTPC(green),TPPP3(red),andSOX9(white).Whitelines/redarrows:columnartipprogenitors,SFTPC+/SOX9+/high/
TPPP3+.Arrowheads/dashedlinesinstalk/airsacregions:cuboidaldifferentiatingfetalAT2cells,SFTPC+/SOX9low/-/TPPP3low/-.Asterisks(*)representprimitive
airsacs.
(G)QuantificationofcuboidalSFTPC+/SOX9low/-fetalAT2cellsinstalk/airsacregionsin(F).TheSFTPC+tipepithelialcellswereexcludedbytheircolumnar
morphologyandmarkerexpression(SOX9low/-).Mean±SD,n>7.Significanceevaluatedbyone-wayANOVAwithTukeymultiplecomparisonpost-test;ns:not
significant,*p<0.05,**p<0.01,***p<0.001,****p<0.0001.
(HandI)InsituHCRanalysisat21pcw.FetalAT2SFTPC+andNAPSA+(arrowheads;HandI)andfetalAT1SFTPC(cid:3)/MMP28+/SPOCK2+(arrows;I).
(J)Diagramoftheacquisitionofalveolarprogenitoridentitybylateepithelialtips,followedbydifferentiationtofetalAT2andAT1lineages.DAPI,nuclei.Scale
bars,50mm.SeealsoFigureS6.
Cell185,4841–4860,December8,2022 4847

ll
OPENACCESS Resource
(legendonnextpage)
4848 Cell185,4841–4860,December8,2022

ll
Resource OPENACCESS
S6C). Over the following weeks, the size of the tip regions lymphatic ECs (PROX1+, STAB1+, and UCP2LO), showing that
decreased and more differentiating AT2 cells were detected capillaries and lymphatic vessels are distinct from the earliest
(Figures3Fand3G).At21pcw,smallernumbersoflate-tipcells stagesoflungdevelopmentandthatarterialspecificationbegins
persist, and AT2 cells (SOX9-, SFTPC+, NASPA+, ETV5+) were priortovenous(FigureS1T).Atlaterstages,trajectoryanalysis
foundscatteredthroughoutthedevelopingairsacs(Figures3H predictsthatbothmid-andlate-Capcellsgeneratearterialand
andS6E–S6J).Consistentwiththepredictedchangeintipfate venousECs(FigureS7A).Aerocytes(CA4LO,S100A3+),capillary
potential(Figures3C–3E),late-tipcells(16–20pcw)grownasor- ECsspecializedforgasexchangeandleukocytetrafficking,30,31
ganoidsretainedalate-tipphenotypeinvitroandmorereadily were observed at 20–22 pcw around the developing air sacs
differentiatedtomatureAT2cellsthanorganoidsderivedfrom (Figure S7B). Microvasculature specification therefore occurs
earlierdevelopmentalstages.29 relativelylateinhumanfetallifecoincidentwiththedevelopment
In our single-cell atlas, differentiating AT1 cells were first ofAT1cells.
visible at 18 pcw but more prominent by 22 pcw (Figures 2A– Broad markers of arterial and venous specification were
2C).Similarlyintissuesections,AT1cellswerenotdetectedat clear in sections at 20 pcw (Figures S7C and S7D). Three
17 pcw (Figure S6H). However, by 20 pcw, differentiating AT1 distinct arterial ECs were detected. GRIA2+ and arterial ECs
cells(SPOCK2LO,SFTPC-)werevisible,andat21pcw,AT1cells (DKK2+, SSUH2+) form a continuous differentiation trajectory
(SPOCK2+,SFTPC-)wereinterspersedwithAT2cellsliningthe in pseudotime (Figure S7A) with GRIA2+ ECs likely to be a
developingairsacs(Figures3I,S6I,andS6J).Insections,AT1 moreimmatureform.TheOMD+ECs(GJA5+,DKK2+,PTGIS+,
markerswereonlydetectedincellswhichhadnoorextremely and OMD+) cluster with arterial ECs and are more proximal
low levels of SFTPC (Figures S6H–S6J). Moreover, SFTPC- (Figure S1O). By contrast, venous ECs (PVLAP+, ACKR3+,
negative cells were always observed in the stalk regions from and HDAC9+) do not have clear subclusters. Systemic and
16pcwonwards(Figure3F).Thesedataareconsistentwithan pulmonary circulation ECs have been found in adult lungs32;
alveolar epithelial differentiation model in which, from (cid:1)16 we cannot detect these in fetal lungs. Two major lymphatic
pcw, the late-tip progenitors first exit the tip state, turning off ECs were detected: lymphatic ECs (PROX1+, STAB1+, and
AT2cellmarkers,andenterthelate-stalkcellstate,priortoiniti- UCP2LO) and SCG3+ lymphatic ECs (PROX1+, SCG3+) (Fig-
atingAT1orAT2celldifferentiationinresponsetolocalsignaling ure S7E). SCG3+ lymphatic ECs resemble a lymphatic valve
cues(Figure3J).Furthermore,thelate-stalkcellsareconnected population.33
toAT2,AT1,andlateairwayprogenitorsintrajectoryinference
analysis (Figures 2D, 3C, and 3D), supporting our hypothesis Hematopoieticcelltypesinthedevelopinglung
thatatallstagesoflungdevelopment,cellsexitthetipandenter At the early stages (5–6 pcw) when arterial, capillary, and
astalkstatepriortodifferentiation. lymphatic ECs were present, embryonic erythrocytes,
Integrationofourfetalcellatlaswithadultdatarevealedhigh HMOX1+ erythroblasts, and a small number of macrophages
correlation between expected groups: fetal airway progenitors and ILC progenitors were detected, representing the early
withadultsecretoryclubcells,fetalandadultciliatedanddeuter- progenitorsofhematopoiesis.After11pcw,relativenumbers
osomalcells,andproximalsecretoryfetalcellswithadultgoblet oflymphoidandmyeloidcellsincreased,dominatedbymac-
cells(FigureS2A).TheAT2andAT1cellswedetectinthefetal rophages;ILCs;anddendritic,NK,T,andBcells(Figures1C–
lungsclustercloselywiththeadult(Pearsoncorrelationcoeffi- 1E, S1P,-S1R, and S1T). Immature T cells are largely absent
cients:fetal-adultAT20.66;AT10.80).However,thefetalcells fromtheatlas,consistentwiththerestrictionofTcelldevelop-
areimmatureanddifferingeneexpressiontotheiradultcounter- menttothethymus.Incontrast,arangeofearlyBcellprecur-
parts(FigureS2G). sors and the ILC precursor were detected. TCR and BCR
scRNA-seq supported cell-type identities and subdivision
Lungendothelialcellsexhibitearlyspecializationinto (Figures S1Q’’ and S1R’’). We compared our atlas with a
arterialandvenousidentities pan-fetal human atlas13 and found that leukocytes were
At5–6pcw,theendothelialcells(ECs)comprisedcapillary(early transcriptionally highly similar to those of other organs
Cap: THY1+, CD24+), GRIA2+ arterial (GRIA2+, GJA5+), and (Figure S1S).
Figure4. Diversemesenchymalcelltypeslocalizetodistinctnichesinthedevelopinghumanlung
(A)UMAPvisualizationofmesenchymalcells.
(B)Dotplotofmesenchymaldifferentialmarkergeneexpression.
(C)UMAPvisualizationofmesenchymalcellscoloredbystage.
(D)Visiumspatialfeatureplotsvisualizingadventitialfibroblasts,airwayfibroblasts,ASPN+chondrocytes,andmyofibroblast-2on17and20pcwlungsections.
Scoresareconservativeestimatesofcell-typeabundancepervoxel.
(E–H)InsituHCRassay(E–H)andimmunostaining(G).
(E)Adventitialfibroblasts(SFRP2,white/PI16,red;arrowheads),ECs(PECAM1,green).
(F)Alveolarfibroblasts(WNT2white;FGFR4red),tipcells(SFTPCgreen).Asterisks(*myofibroblasts).
(G)Airwayfibroblasts(S100A4red;AGTR2white),smoothmuscle(ACTA2green,dashedline).
(H)Myofibroblasts(KCNK17white,CXCL14red;arrowheads),tipcells(SFTPC,green).DAPI,nuclei.Scalebars,50mm.
(I)UMAPvisualizationofcelltypes(I)andstage(I’)andPAGAanalysis(I’’)offibroblastdifferentiationtrajectories.
(JandK)UMAPswithMonocle3trajectories(J)andselectedtrajectorygeneexpressionheatmaps(K)formidtiptoadventitialfibroblasts(top),alveolarfibroblasts
(middle),orairwayfibroblasts(bottom).SeealsoFigureS7.
Cell185,4841–4860,December8,2022 4849

ll
OPENACCESS Resource
(legendonnextpage)
4850 Cell185,4841–4860,December8,2022

ll
Resource OPENACCESS
Developmentaltrajectoriesofmesenchymalcells describedrolesprovidingstructuralsupporttotheperivascularre-
The broad fibroblast cluster comprises fibroblasts, myofibro- gion.37 Alveolar fibroblasts (WNT2+, FGFR4+) were observed
blasts, airway and vascular smooth muscle (ASM and vSMC), throughoutthelung,particularlysurroundingtipcellsandmicro-
pericytes, mesothelium, and chondrocytes (Figures 4A and vasculature(Figure4F).Theywereenrichedingenesassociated
4B). Airway fibroblasts and chondrocytes were proximally withactinorganization,focaladhesions,andmorphogenesis,as
enriched and mesothelium distally enriched (Figures 4D wellassignalingmolecules(Figures4J,4K,andS7J).Adventitial
and S1O). Cell clusters separated by age (Figure 4C). ASM and alveolar fibroblasts expressed shared and unique genes
cellswereobservedfrom9pcw,consistentwithpreviousimmu- (adventitial: SERPINF1, SFRP2, and PI16; alveolar:FGFR4 ,
nostaining,8 and showed increasing maturity over time VEGFD;Figure4K).Bycontrast,theairwayfibroblasts(AGTR2+,
(Figures 4A–4C). Two distinct populations of vSMC were S100A4+;noteS100A4isexpressedinvariousimmuneandairway
observed throughout the time course, vSMC1 (NTRK3+, epithelialcells)wereadjacenttotheASMandhighlyenrichedin
NTN4+, and PLN-) and vSMC2 (NTRK3+, NTN4+, and PLN+) signalingmoleculesassociatedwithmorphogenesis(Figures4D,
(Figures 4A and 4B), and were intermingled around the same 4G,4J,4K,andS7J).Wedidnotdetectlipofibroblasts,38meaning
vesselsontissuesections(FiguresS7FandS7H).vSMC1was thattheyareeitherrare,formlaterthan22pcw,ordonotform
enriched in genes relating to ECM organization and cell adhe- distinctclustersinalllungdatasets.14Endothelialandfibroblast
sion,andvSMC2fortranscriptsencodingcontractilityproteins populationsalignwellbetweenfetalandadultdata(FiguresS2B
and signaling molecules (Figure S7G). Intermingling of vSMC andS2C),butwithsomeuniquedevelopmentalstates,suchas
subtypeswithdifferentlevelsofcontractilityproteinsisseenin fetalearly/mid-fibroblastsandmyofibroblasts.
adult lungs34; our developmental observation suggests that Myofibroblasts formed three distinct groups in our single-
theserepresentnormalfunctional/ontologicaldifferences,rather celldata.Myofibroblast1(CXCL14+,KCNK17+,CT45A3+,and
thanpathology.Pericytes(FAM162B+)werevisualizedadjacent THBDLO)appearedat9pcwandpersistedto20pcw.Myofibro-
tothemicrovascularendothelium(FigureS7I). blast 2 (CXCL14+, KCNK17+, CT45A3+, and THBDHI) and
Themostcommoncellsisolatedfrom5–15pcwlungswerefi- myofibroblast 3 (CXCL14+, KCNK17+, CT45A3-, and THBD-)
broblasts (Figure 1C). At 5–6 pcw, early fibroblasts (SFRP2+, were predominantly identified at 22 pcw (Figures 4A and 4B).
WNT2+)predominated,althoughmultiplepopulationswerede- Throughoutdevelopment,myofibroblasts(CXCL14+,KCNK17+)
tected(Figures4Aand4B).In9–11pcwlungs,earlyfibroblasts were visualized surrounding the developing stalk region
hadmaturedintomidfibroblasts(WNT2+,FGFR4LO)whichcan of the epithelium, suggesting a close signaling relationship
promoteepithelialtipcellfate.35Intheoldestlungssequenced, (Figures4D,4H,S7K,andS7L).Althoughnotdetectedinsignifi-
therewerethreedistinctfibroblasts:adventitial(SFRP2+,PI16+), cantnumbersinthescRNA-seqdatauntil22pcw,weseemyofi-
airway(AGTR2+,S100A4+),andalveolar(WNT2+,FGFR4+)with broblast2(PDGFRA+,THBDHI,andNOTUM+)aroundthestalk
distinctlocations(Figures4A,4B,and4D–4G).Inaddition,anin- epithelium from 15 pcw (Figures 4D, S7L, S7N, and S7O), the
termediatefibroblastconnectedthemorematurefibroblastson samepositionasmyofibroblast1.Theappearanceofmyofibro-
theUMAP(Figures4Aand4B),possiblyrepresentingatransi- blast2iscoincidentwiththeacquisitionofAT2markersbythe
tionalstate.Pseudotimeanalysispredictedadifferentiationhier- late-tipcellsandmaybeamorematurestateofmyofibroblast
archyfromtheearlyandmidfibroblaststoadventitialfibroblasts, 1.Myofibroblast2wasenrichedingeneexpressionassociated
withalveolarandairwayfibroblastsformingseparatebranches with cell contractility and focal adhesions, as well as WNT
(Figures4I–4K).Alternatively,theintermediatefibroblastpopula- signaling (Figures S7N and S7O). Co-expression of the Wnt-
tionmayindicatelineageplasticityaspreviouslysuggested.36 responsive genes LEF1, NOTUM, and NKD1 suggests that
Thethreemajorfibroblasttypesin15–22pcwlungsexpressed myofibroblast2isrespondingtolocalWntexpression(WNT2is
highlevelsofgenesassociatedwithECMorganizationbuthad highinalveolarfibroblasts)andproducingthesecretedWntin-
distinctgeneexpressionpatternsandspatiallocalization.Adven- hibitor NOTUM,potentially toregulatelocalcell patterning.By
titialfibroblasts(SFRP2+,PI16+)surroundedthelargerbloodves- contrast,myofibroblast3hashigherexpressionofgenesassoci-
sels(Figure4D).Theyformeddiffuselayersofcellssurroundingthe atedwithECMorganizationandavarietyofsignalingmolecules,
tightly packed concentric rings of ECs, pericytes, and vSMCs includingC7,RSPO2,andBMPER(FigureS7N).Myofibroblast3
(Figures 4E and S7H). Adventitial fibroblasts were enriched in waslocalizedtothedevelopingairsacs(FigureS7M),ratherthan
genesassociatedwithECMorganizationandsignaling,including thestalkepithelium,andislikelytobeaprecursorofthealveolar
BMP,TGFb,andWNT(Figures4J,4K,andS7J),consistentwith myofibroblasts.17,39
Figure5. Signalingligand-receptorinteractionsinspecificniches
(A–C)Curatedligand-receptorinteractionpredictionsfromCellPhoneDBinairway(A),alveolar(B),andadventitial(C)niches.Dotplotsvisualizegeneexpression
bycelltype;dashedarrowsindicatethepredicteddirectionofsignalingfromligandstoreceptors.
(D–F)Immunofluorescence/HCR.S100A4/S100A4,airway fibroblasts; ACTA2, ASM;CD44, tipepithelium;PECAM1,ECs. Airwayfibroblasts/ASM forma
boundary(dashedlines)betweenalveolarandairwayregions.Linesarebetweenairwayfibroblasts/SMCsandairwayepithelium.DAPI,nuclei.Scalebars,50mm.
(G) Organoids were cultured in FGF7/10-containing medium, in the presence (self-renewal medium; SNM) or absence (differentiation medium; DM) of
CHIR99021,for30days.
(H)qRT-PCRquantificationnormalizedtoorganoidsculturedinSNM.Significanceevaluatedbytwo-wayANOVAwithTukeymultiplecomparisonpost-test;
*p<0.05,**p<0.01,***p<0.001;n=6organoidlines.
(I) Whole-mount immunofluorescence of lung organoids cultured in self-renewal medium (upper) and differentiation medium (lower). DAPI, nuclei. Scale
bar,25mm.
Cell185,4841–4860,December8,2022 4851

ll
OPENACCESS Resource
(legendonnextpage)
4852 Cell185,4841–4860,December8,2022

ll
Resource OPENACCESS
Signalingnichesinlungdevelopment onourscRNA-seqdata(Figure6A).Noteverycellstatedetected
WeusedCellPhoneDB40topredictsignalinginteractionscontrol- by scRNA-seq was distinguishable by scATAC-seq, consistent
lingcellfate.Wefocusedon15–22pcwcellsand,basedonthe with previous work.13,44 For example, separate early-tip, stalk,
localizationofthe major fibroblast populations (Figures4E–4G), andairwayprogenitorclusterswerediscernedbyscRNA-seq(Fig-
analyzedsignalingwithinthreeniches.Theairwaynicheincludes ure2A),butacombinedclusterwithstrongsimilaritytoallthreecell
airwayfibroblasts,lateairwaySMCs,andairwayepithelialcells. types was detected by scATAC-seq (Figure 6A). Nevertheless,
The alveolar niche includes alveolar fibroblasts, aerocytes, late therewasbroadagreementbetweenthescRNA-seqandATAC-
Capcells,late-tipcells,AT1,andAT2.Finally,theadventitialniche seq data in terms of capturing cell types, including many of
includesadventitialfibroblasts,arterialendothelium,OMD+endo- the novel/lesser-known cell types we identified by scRNA-seq
thelium,andvascularsmoothmusclecells.CellPhoneDBpredicts (mid and late tip, mid and late airway progenitors, GHRL+ NE,
numeroussignalinginteractions(TableS2)thatwecuratedbyplot- MUC16+ ciliated, dueterosomal, airway fibroblasts, aerocytes,
ting the expression of ligand-receptor pairs representing major andSCG3+lymphaticendothelialcells).
signalingpathways(Figures5A–5C).Weobservedexpectedinter- We analyzed TF binding motifs in the unique/enriched open
actions,includinghighlevelsofNotchligandsandreceptorsand chromatinregionsineachclusterandplottedthetopTFmotifs
CXCL12-CXCR4 signaling in the adventitial niche (Figure5C).41 percelltype(TableS4).Asexpected,TFsbelongingtothesame
Similarly, expected signaling predicted in the alveolar niche familyarefrequentlyenrichedinthesamecelltypeduetosimilar-
includedaerocytestolatecapcells(ALPN-ALPNR)andalveolar itiesintheirbindingmotifs.Thisanalysisrevealedsomeexpected
epithelial cells to microvascular ECs (VEGFA-FLT1/FLT4/KDR) TFsignatures,forexampleTCF21inthefibroblasts,45GRHL,and
(Figure5B).30,31 FOXA1/2inepithelium,46,47andSOX17inarterialendothelium.48
Airway fibroblasts were predicted to signal via TGFb3 and ExaminingepithelialcellsandfocusingonTFsexpressedinthe
BMP4tothe airwayepithelium, consistentwithrolesforthese correspondingcelltypeinthescRNA-seqdata(Figures6Band
signalsinhumanbasalcellspecificationanddifferentiation.42,43 6C, marked by asterisk in 6B), TEAD motifs were enriched in
AirwayfibroblastsandASMwerealsopredictedtosignaltothe mid-stalk cells, consistent with a key role for Yap,49 NKX2.1 in
epitheliumviaFGF7/18toFGFR2/3andnon-canonicalWNT5A AT1/AT2 cells,50 KLF factors in secretory cells and AT1/AT2,51
to FZD/ROR (Figure 5A). By contrast, although FGF and WNT and TP63 in basal cells.52 Unexpected TF signatures included
signalinginteractionswerealsopredictedinthealveolarniche, HNF1Binlate-tipcellsandZBTB7Ainearly-tip/stalk/airwaypro-
interactionswerebasedonlowerlevelsofFGFbuthigherlevels genitors. We focused on the pulmonary and GHRL+ NE cells,
ofcanonicalWNT2anditsreceptor(Figure5B).Thepredicted whichclusterclosely(Figures2Aand6A).ASCL1isrequiredfor
FGF and WNT signaling interactions in the alveolar niche and mouseNEcelldifferentiation,53,54andthismotifisstronglyassoci-
late-tipcellsareconsistentwiththerequirementofthesefactors atedwithbothpulmonaryandGHRL+NEcells(Figure6B).Howev-
for long-term self-renewal of human distal tip organoids.8,29 er, both cell types also respectively have specific TF motifs
Tissuestaining showed thatalthoughFGF7 isexpressed fairly includingNEUROD1andRFX6intheGHRL+NEs,andTCF4and
ubiquitously, the airway fibroblasts and ASM form a distinct IDinthepulmonaryNEs(Figure6B).Consistentwiththis,there
barrier between the airway epithelium and the WNT2 aredistinct,uniqueregionsofopenchromatin,especiallyinthe
expression(Figures5D–5F).Basedonthesedata,wepredicted neighborhood of cell-type-specific genes such as GRP and
thatremovingcanonicalWNTbutretainingFGFsignalingwould GHRL(Figure6Dand6E).
promoteairwaydifferentiationinthehumandistaltiporganoids Wehaveproducedahigh-resolutionscATAC-seqdatasetfor
(Figure5G).Indeed,weobservedrobust basal,secretory,and thedevelopinghumanlungs,whichishighlyconsistentwithour
ciliated cell differentiation in response to FGF-containing me- scRNA-seq data. Mining these data provides hypotheses for
dium(Figures5Hand5I). lineage-determiningTFsinlungdevelopment.
scATAC-seqanalysisidentifiesputativecellfate Transcriptionalcontrolofneuroendocrinecellsubtype
regulators formation
SinglecellATAC-seqprovidesanindependentmethodofassess- PulmonaryNEandGHRL+NEcellssharetheexpressionofmany
ingcellular-levelgeneregulationbasedonopenchromatinregions TFs and open chromatin regions but are transcriptionally
and allows cell-type-specific TFs to be predicted. After tissue distinct.InourscRNA-seqdata,theywerebothobservedalong
dissociation, the single-cell suspensions were split, and half of amaturationtrajectoryandsharedclassicalNEmarkers(CHGA,
the cells wereprocessed for nuclear isolation and scATAC-seq SYP),butdifferedinTFandhormoneexpression(Figures7Aand
(Figure1A).Followingqualitycontrolanddoubletremoval,67scA- 7B).AthirdNEpopulation(intermediateNE)clusteredbetween
TAC-seqclusterscomprising(cid:1)100Kcellswereobtained,andla- pulmonaryandGHRL+NEcellswithintermediategeneexpres-
bel transfer was used to annotate scATAC-seq clusters based sion(Figures7Aand7B),althoughitdidcontainasmallnumber
Figure6. DNAaccessibilityandmotifenrichmentrevealedbyscATAC-seq
(A)Single-cellDNAaccessibilityprofilesmappedonto2DUMAP.Coloredforcellstates.
(B)Top10enrichedmotifsinthemarkerpeaksamongepithelialcelltypes/states.Statisticalsignificanceisvisualizedasaheatmapaccordingtothecolorbar
below.TranscriptionfactorsconcordantlyexpressedbasedonscRNA-seqdataaremarkedwithasterisks.
(C)Expressiondotplotoftheconcordanttranscriptionfactorsfrom(B)inepithelialcelltypes.
(DandE)Readcoveragetracksofinsilicoaggregated‘‘pseudo-bulk’’epithelialclustersovertheGRPlocus(D)andGHRLlocus(E).SeealsoTableS4.
Cell185,4841–4860,December8,2022 4853

ll
OPENACCESS Resource
(legendonnextpage)
4854 Cell185,4841–4860,December8,2022

ll
Resource OPENACCESS
of cells expressing the unique marker NEUROG3. Pseudotime and are required for endocrine cell differentiation in various or-
trajectory analysis suggested that pulmonary NE and GHRL+ gans.53,54,60,61 We also selected the GHRL+NE-specific RFX6
NE cells were derived from airway progenitors/stalk cells and (Figure S8E) and NKX2.2 (Figure 7B), the pan-NE PROX1 (Fig-
that intermediate NEs are an additional transition population ure7B),and,ascontrols,thebasalcell-specificTFsDeltaNTP63,
(Figures S8A and S8B). Transition states between pulmonary TFAP2A, PAX9, and mNeonGreen-3xNLS. Overexpression of
NEandGHRL+NEwereobservedinsections(FigureS8C).We PROX1orNKX2-2didnotresultinNEgeneupregulationbased
therefore postulated that pulmonary NE precursors could ac- onqRT-PCR(datanotshown),andtheseTFswerenotfollowed
quireNEUROG3andconverttoGHRL+NEfate(Figure7C),or up.Theotherfactorsresultedinincreasedexpressionofbasalor
vice-versa—GHRL+ precursors converting to pulmonary NE NEmarkerscomparedtomNeonGreen-3xNLScontrols,andthe
fate.Insections,ASCL1wasco-expressedwithGRP,butrarely experiments were repeated using scRNA-seq. Individual TFs
withGHRL.WealsoobservedASCL1single-positivecells,likely were overexpressed from a doxycycline-inducible construct for
representing pulmonary NE precursors (Figure 7D). NEUROD1 3days,andorganoidsweremaintainedintheself-renewing(tip
wasco-expressedwithGHRLbutalsoobservedwithGRP(Fig- cell-promoting)mediumthroughouttorigorouslyassaytheline-
ure7E),whereasNEUROG3wasco-expressedwithASCL1and/ age-determining competence of the TF (Figures 7H and S8F),
or NEUROD1, supporting a role in a transition population followedbyscRNA-seq.
(FigureS8D). Whenmappedtoepithelialcellsofourfetallungatlas,thema-
Differential expression of ASCL1 and NEUROD1 defines A- jorityofthemNeonGreen-3xNLSexpressingorganoidcellspro-
andN-typehumanSCLC,whichlikelyderivesfromNEcells.55 jectedtomid-tiporstalkcellsasexpected(Figure7I),whereas
Interestingly,thesetwoTFscoincidewiththescRNA-seqmarker overexpressionofDeltaNTP63resultedinbasalcell-likelineages
genesandscATAC-seqTFmotifenrichmentofourfetalNEcells (FigureS8G)consistentwithapreviousreport.62Overexpression
(Figures6Band7B).WegeneratedSCLCfeaturegenelists18and ofRFX6,TFAP2A,orPAX9didnotresultinthepredictedlineage
performed gene signature scoring, showing that the A-type progression at a transcriptome level (Figure S8G). However,
signatureresemblespulmonaryNEs,whereastheNtyperesem- ASCL1-overexpressing organoids progressed into pulmonary
bles GHRL+ NEs (Figure 7F). These data suggest that either NE precursors (Figure 7I), and NEUROD1 overexpression
there are two different NE cells of origin for human SCLCs or promoteddifferentiationintoGHRL+NEprecursors(Figure7I).
that SCLCs reuse developmental mechanisms, as suggested NEUROG3 overexpression also led to GHRL+ NE precursor
by some mouse models.56 We have been unable to detect formation (Figure S8G), suggesting that the GHRL+ NE
GHRL+NEs in the adult airways usingHCR (5biological repli- lineage is the destination of the intermediate NE population
cates). However, a small number of GHRL+ cells are present (Figure7C).
within a tuft cell cluster in an integrated adult lung cell atlas The50 differencesbetweenthetransgenesandendogenous
containing2.2millioncells,57suggestingthatGHRL+NEscould TFs allowed us to distinguish these transcripts and infer gene
beararecellstateintheadultairways.Giventheirrelevanceto regulation hierarchy. We observed autoregulation of ASCL1,
humandisease states,weusedoursingle-cell atlastopredict NEUROD1, NEUROG3, and RFX6 (Figure S8H). By contrast,
NE lineage-defining TFs and test these using our organoid NKX2-2andPROX1wereupregulatedbyotherTFs,indicating
system. We reasoned that overexpression of lineage-defining they are relatively low in the hierarchy (Figure S8H). NKX2-2
TFs in lung tip organoids8,58 would promote cell-type-specific and PROX1 expression in the organoid assay matched their
differentiation. expression in NE cells in vivo (Figures 7B and S8H), showing
MultipleTFsweredifferentiallyexpressedbetweenpulmonary that this assay recapitulated key features of the TF network.
NEandGHRL+NEcells(Figure7B).WeusedSCENICanalysis TheseexperimentstestedGRNpredictionsfromthesingle-cell
ofgeneregulatorynetworks(GRNs)59along a predicted airway atlas,confirmedthepredictedlineagetrajectory,andprovided
progenitor to GHRL+ NE trajectory (Figures S8A and S8B) to afoundationforstudyinghumanSCLC.Thisissignificantgiven
identify putative lineage-defining TFs (Figure 7G). ASCL1, that there is no evidence that GHRL+ NE cells are present in
NEUROD1, and NEUROG3 all emerged aspotential key nodes mice,18makingtheuseofmousemodelsdifficult.
Figure7. ASCL1andNEUROD1regulatetheformationoftwosubtypesofneuroendocrinecells
(A)Zoom-inUMAPplotofNElineages.
(B)DotplotshowingselectedgeneexpressioninNElineages.
(C)SchematicmodelofNElineageformation.
(D)Left:HCR,GRP(green),GHRL(red),ASCL1(white).Right:mean±SEMofASCL1+celltypes,N=3humanfetallungs,n=243ASCL1+cells.
(E)Left:HCR,GRP(green),NEUROD1(red),GHRL(white).Right:mean±SEMofNEUROD1+celltypes:N=2,11pcwhumanfetallungs,n=129;N=3,12pcw
humanfetallungs,n=132.Scalebars,25mm.
(F)GenesignaturescoringofA-typeandN-typeSCLCfeaturesintheepithelialUMAP.
(G)ScenicanalysisofpredictedTFnetworkgoverningmidtipprogenitorcellstopulmonaryNEandGHRL+NE.TrajectoryandcolorcodingmatchFiguresS8A
andS8B.
(H)Organoidsfrom8pcwhumanfetallungsweretransducedwithDoxycycline(Dox)-inducibleTF,ormNeonGreen-NLS,lentivirus.Transducedorganoidswere
isolatedbyflowcytometrybasedonTagRFPexpression,seededinMatrigelfor10–13dayspriortoDoxtreatment.Organoidcellswereharvested3dayspost-
DoxforscRNA-Seq.N=3organoidlines.
(I)Left:referenceUMAPofprimaryhumanfetallungepithelium.Midandright:scRNA-SeqoforganoidsoverexpressingmNeonGreen-NLS,ASCL1,orNEUROD1
projectedontotheprimarydata.SeealsoFigureS8.
Cell185,4841–4860,December8,2022 4855

ll
OPENACCESS Resource
DISCUSSION binding site analyses and require future validation. Trajectory
inferenceanalysesarelargelybasedontranscriptomicsimilar-
Usingacombinationofsingle-cellandspatialapproaches,we itieswithoutground-truthdirectionality,orareunabletohandle
haveidentified144celltypes,orstates,inthedevelopinghuman complexexpressionkineticsingroupsofgenes.67Fortheserea-
lungsacrossthe5–22pcwperiod.Wetakeadvantageofaknown sons,wefedMonocle368withstartingandendpointsguidedby
proximal-distalgradientinepithelialdifferentiationtoidentifypro- knownbiologicalfeaturesofthedata(ageandspatialarrange-
genitor and differentiating states in the developing airway, mentofcells).Furthermore,validationassaysforlineageanalysis
includinganeuroendocrinecellsubtyperelatedtoSCLC.More- in human systems rely on in vitro experiments. These usually
over,analysisofthemesenchymalcompartmentidentifiedthree definedifferentiationcompetenceanddonotnecessarilymean
nicheregionswithdistinctsignalinginteractions,allowingusto thataspecificdifferentiationrouteoccursinvivo.Theclustering
identifysignalingconditionsthataresufficientforairwaydifferen- of our scRNA-seq and scATAC-seq data are in broad agree-
tiationofhumanembryoniclungorganoids.WetestedGRNpre- ment. However, many motifs enriched in cell-type-specific
dictionsforNEcelldifferentiationinanorganoidsystem,allowing peaksbelongtoTFsnotdetectedbyscRNA-seq.Thisdiscor-
ustoidentifylineage-definingTFsandprovidedirectionalityto dance might be due to differing sensitivity of the two assays,
theinferreddifferentiationtrajectory.Thisstudyprovidesapara- transcriptionfactorlatency,andtheincompletenessofthemotif
digmforcombiningsingle-celldatasetswithspatialanalysisof databases.
thetissueandfunctionalanalysesinahumanorganoidsystem Wehavecomparedtheidentityoffetalandadulthumanlung
toprovidemechanisticinsightsintohumandevelopment. cellsandhaveseenmanyfetal-adultsimilarities.Nevertheless,
Ourdatasuggestthatatallstagesoflungdevelopment,cells thereareapproximatelythreedecadesbetweentheoldestfetal
exitthetipandenterastalkstatepriortodifferentiation.Wepro- andyoungestadulthumanlungsamplessequenced,includinga
pose that human alveolar epithelial differentiation also follows rapidperiodofpostnatalgrowthandmorphogenesis,puberty,
this model, using a tip-stalk-AT2 or AT1 fate decision pattern andunknowninfections/environmentalinsults.Itwillbeimpor-
(Figure 3). This is different to the prevailing cellular models of tant to sequence additional lungs and, when possible, to fill
mousealveolardevelopment:earlycellfaterestriction17,63and theagegap.Moreover,ourmouse-humanfetallungcellcom-
bipotentprogenitorswithAT1/2characteristics.64 parisonsareaffectedbybothtechnical(experimentalprotocols
Airway, adventitial, and alveolar fibroblasts are localized in and annotation granularity) and biological differences (size
distinctnicheregionsandparticipateindifferentsignalinginter- and gestation rate). It will be informative in the future to
actions.Airwayandadventitialfibroblastsbothexpressunique make comparisons with a range of fetal lungs, including
combinationsofsignalingmoleculesandalsoformphysicalbar- larger, long-developing species such as pig and sheep, to
riers between the neighboring airway epithelium or vascular distinguishbetweendifferencesduetospecies,size,andgesta-
endotheliumandthewidespreadalveolarfibroblasts(Figures4 tionperiod.
and5).Similarly,wecharacterizeapopulationofmyofibroblasts
that contacts the developing epithelial stalk region and ex- STAR+METHODS
presseshighlevelsofthesecretedWnt-inhibitor,NOTUM(Fig-
ure S7O), whereas alveolar fibroblasts express high levels of
Detailedmethodsareprovidedintheonlineversionofthispaper
thecanonicalWNT2ligand(Figure4).Inaseparatestudy,using
andincludethefollowing:
surfacemarkersidentifiedinthissingle-cellatlas,wespecifically
isolatedalveolarfibroblastsandmyofibroblast2cellsforco-cul- d KEYRESOURCESTABLE
ture experiments with late-tip organoids.29 Those experiments d RESOURCEAVAILABILITY
confirmed that a three-way signaling interaction between B Leadcontact
alveolarfibroblasts,myofibroblast2cells,andlate-tipcellscan B Materialsavailability
controlhumanAT2spatialpatterning. B Dataandcodeavailability
WefindthatGHRL+NEcellsaretranscriptionallysimilartothe d EXPERIMENTALMODELANDSUBJECTDETAILS
NEUROD1+NsubtypeofSCLC(Figure7).Ourfunctionalana- B Humanlungtissue
lysesofNEcelldifferentiationinorganoidswillprovidetoolsto d METHODDETAILS
testthesehypotheses.Mousestudiesshowthatfetaltranscrip- B Cellisolationfor10XsinglecellRNAandATACseq
tionalandchromatincellstatesareaccessedduringthenormal B Humanfetallungorganoidmaintenance
processoftissueregenerationandmaycontributetoneoplasm B Humanfetallungorganoidbronchiolardifferentiation
inchronicinflammation.65,66DetailedATAC-seqdatasetsarenot B IsolationandairwaydifferentiationofSCGB3A2+distal
yetavailableforhumanlungdisease.Ourhigh-qualityATAC-seq andproximalairwaycells
atlaswillprovideabaselineforfurtheranalyseswhenadultchro- B RNA extraction, cDNA synthesis, and qRT-PCR
matinaccessibilitylungatlasesarepublished.Insummary,our analysis
multi-componentatlasisacommunityresourceforfutureana- B Humanfetallungorganoidimmunofluorescence
lysesofhumandevelopment,regeneration,anddisease. B Plasmidcloning
B Lentiviruspackaging
Limitationsofthestudy B Lentivirustransduction
Weprovideacarefullyannotated,descriptivecellatlasresource. B Overexpression of transcription factors and
Many conclusions are derived from trajectory inference or TF scRNA-Seq
4856 Cell185,4841–4860,December8,2022

ll
| Resource |     |     |     |     |     |     |     |     |     |     |     | OPENACCESS |     |
| -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- |
B In situ hybridization chain reaction and Investigation:K.L.,D.S.,Q.J.,Z.D.,L.B.,L.R.,L.M.,M.D.,A.W.,andM.Y.Re-
immunofluorescence sources:E.M.,X.H.,R.A.B.,andS.M.J.DataCuration:P.H.,K.L.,D.S.,E.M.,
B Librarygenerationandsequencing Z.K.T.,E.D.,C.S.,andI.G.Writing–originaldraft:P.H.,K.L.,D.S.,J.P.P.,
|     |     |     |     |     |     |     |     | K.B.M., and | E.L.R. Writing | – review | and editing: | P.H., K.L., | D.S., K.B.M., |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | -------------- | -------- | ------------ | ----------- | ------------- |
B Visiumspatialtranscriptomics
|     |     |     |     |     |     |     |     | E.L.R., S.A.T., | and J.B.M. | Supervision: | M.Z.N., | R.A.B., | S.A.T., J.B.M., |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | ---------- | ------------ | ------- | ------- | --------------- |
B Readsmappingandquantification
|     |     |     |     |     |     |     |     | K.B.M.,and | E.L.R. Funding | Acquisition: | K.L., E.M., | J.P.P., | R.A.B., M.Z.N., |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | -------------- | ------------ | ----------- | ------- | --------------- |
B VDJanalysis
S.A.T.,J.B.M.,K.B.M.,andE.L.R.
| B   | Single-cell | RNA-seq |     | processing | and | cell | type |     |     |     |     |     |     |
| --- | ----------- | ------- | --- | ---------- | --- | ---- | ---- | --- | --- | --- | --- | --- | --- |
annotation
DECLARATIONOFINTERESTS
B
ArtefactevaluationandremovalforscRNA-seqdata
B Visiumspatialtranscriptomicsdataanalysis S.A.T.isamemberoftheScientificAdvisoryBoardforthefollowingcom-
|     |     |     |     |     |     |     |     | panies: Biogen, | Foresite | Labs, GSK, | Qiagen, CRG | Barcelona, | Jax Labs, |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | -------- | ---------- | ----------- | ---------- | --------- |
B Differentialgeneexpressionalongtrajectories
SciLifeLab,andAllenInstitute.SheisaconsultantforGenentechandRoche.
B CellPhoneDBanalysis
Sheisco-founderofTransitionBioandamemberoftheBoard.Z.K.T.has
B Velocityanalysis
receivedconsultingfeesfromSyntenyBiotechnologiesforactivitiesunrelated
B Generegulatorynetworkanalysis
tothiswork.
| B   | Comparing | fetal | neuroendocrine |     |     | transcriptome |     |                       |     |     |     |     |     |
| --- | --------- | ----- | -------------- | --- | --- | ------------- | --- | --------------------- | --- | --- | --- | --- | --- |
|     | withSCLC  |       |                |     |     |               |     | INCLUSIONANDDIVERSITY |     |     |     |     |     |
B ComparingscRNA-seqdatasetsofthefetallungand
otherstudies Oneormoreoftheauthorsofthispaperself-identifiesasanunderrepresented
B Single-cellATAC-seqprocessingandannotation ethnicminorityintheirfieldofresearchorwithintheirgeographicallocation.
Oneormoreoftheauthorsofthispaperself-identifiesasamemberofthe
| B   | Comparing | organoid |     | scRNA-seq | with | fetal | lung |     |     |     |     |     |     |
| --- | --------- | -------- | --- | --------- | ---- | ----- | ---- | --- | --- | --- | --- | --- | --- |
LGBTQIA+community.
scRNA-seq
d QUANTIFICATIONANDSTATISTICALANALYSIS
Received:December13,2021
B HCRimageanalysis
Revised:August11,2022
| B   | Statisticalanalysisforcell-typecompositionbiases |     |     |     |     |     |     | Accepted:November3,2022 |     |     |     |     |     |
| --- | ------------------------------------------------ | --- | --- | --- | --- | --- | --- | ----------------------- | --- | --- | --- | --- | --- |
Published:December8,2022
B Markergenecalculation
REFERENCES
SUPPLEMENTALINFORMATION
1.Carraro,G.,andStripp,B.R.(2022).Insightsgainedinthepathologyof
Supplementalinformationcanbefoundonlineathttps://doi.org/10.1016/j.cell.
|     |     |     |     |     |     |     |     | lung | disease through | single-cell | transcriptomics. |     | J. Pathol. 257, |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | --------------- | ----------- | ---------------- | --- | --------------- |
2022.11.005.
494–500.
2.Blenkinsopp,W.K.(1967).Proliferationofrespiratorytractepitheliumin
ACKNOWLEDGMENTS
therat.Exp.CellRes.46,144–154.
WewouldliketoacknowledgetheGurdonInstituteImagingFacility,andthe
3.Rawlins,E.L.,andHogan,B.L.M.(2008).Ciliatedepithelialcelllifespan
CellularGeneticsITandPhenotypinggroup,NewPipelineGroupandDNA inthemousetracheaandlung.Am.J.Physiol.LungCellMol.Physiol.
| pipelinesofSangerInstitute;MennaClatworthyandMuzzHaniffaandR.E., |     |     |     |     |     |     |     | 295,L231–L234. |     |     |     |     |     |
| ---------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- |
C.S.,E.D.,I.G.,M.H.,C.D.,andW.S.fordiscussionsoncell-typeannotations;
4.Burri,P.H.(1984).Fetalandpostnataldevelopmentofthelung.Annu.
andM.P.,A.P.,S.L.,W.K.T.,P.M.,andC.T.forinformaticssupport.K.L.issup-
Rev.Physiol.46,617–628.
portedbytheBasicScienceResearchProgramthroughtheNationalResearch
5.Nikolic(cid:1),M.Z.,Sun,D.,andRawlins,E.L.(2018).Humanlungdevelop-
| Foundation | of Korea | (NRF) | funded | by the | Ministry | of Education |     |       |                 |     |                 |             |      |
| ---------- | -------- | ----- | ------ | ------ | -------- | ------------ | --- | ----- | --------------- | --- | --------------- | ----------- | ---- |
|            |          |       |        |        |          |              |     | ment: | recent progress | and | new challenges. | Development | 145, |
(2018R1A6A3A03012122).D.S.issupportedbyaWellcomeTrustPhDstu-
dev163485.https://doi.org/10.1242/dev.163485.
| dentship (109146/Z/15/Z) |     | and | the Department | of  | Pathology, | University | of  |     |     |     |     |     |     |
| ------------------------ | --- | --- | -------------- | --- | ---------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
Cambridge.P.H.holdsanon-stipendiaryresearchfellowshipatStEdmund’s 6.Rawlins,E.L.,Clark,C.P.,Xue,Y.,andHogan,B.L.M.(2009).TheId2+
College,UniversityofCambridge.E.M.issupportedbyESPODfellowshipof distaltiplungepitheliumcontainsindividualmultipotentembryonicpro-
EMBL-EBIandSangerInstitute.J.P.P.issupportedbytheMSCAPostdoc- genitorcells.Development136,3741–3745.
toral Fellowship. E.L.R. is supported by the MRC (MR/P009581/1; MR/ 7.Alanis,D.M.,Chang,D.R.,Akiyama,H.,Krasnow,M.A.,andChen,J.
S035907/1) and acknowledges the Gurdon Institute Core support from (2014).Twonesteddevelopmentalwavesdemarcateacompartment
the Wellcome Trust (203144/Z/16/Z) and Cancer Research UK (C6946/ boundaryinthemouselung.Nat.Commun.5,3923–4015.
A24843).Z.D.issupportedbyaWellcomeTrustPhDstudentship(222275/ 8.Nikolic(cid:1),M.Z.,Caritg,O.,Jeng,Q.,Johnson,J.A.,Sun,D.,Howell,K.J.,
Z/20/Z).R.A.B.issupportedbytheNIHRCambridgeBiomedicalResearch Brady,J.L.,Laresgoiti,U.,Allen,G.,Butler,R.,andZilbauer,M.(2017).
Centre (BRC-1215-20014) and was an NIHR senior investigator. K.B.M., Humanembryoniclungepithelialtipsaremultipotentprogenitorsthat
J.C.M.,andS.A.T.acknowledgefundingfromtheMRC(MR/S035907/1)and
canbeexpandedinvitroaslong-termself-renewingorganoids.Elife
| from Wellcome | (WT211276/Z/18/Z |     | and | Sanger | core grant | WT206194). |     |     |     |     |     |     |     |
| ------------- | ---------------- | --- | --- | ------ | ---------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
6,e26575.https://doi.org/10.7554/eLife.26575.
| M.Z.N. acknowledges |     | funding | from a | MRC Clinician | Scientist | Fellowship |     |           |                   |       |                 |            |             |
| ------------------- | --- | ------- | ------ | ------------- | --------- | ---------- | --- | --------- | ----------------- | ----- | --------------- | ---------- | ----------- |
|                     |     |         |        |               |           |            |     | 9.Miller, | A.J., Hill, D.R., | Nagy, | M.S., Aoki, Y., | Dye, B.R., | Chin, A.M., |
(MR/W00111X/1),theRosetreesTrust(M899),andActionMedicalResearch
|     |     |     |     |     |     |     |     | Huang,S.,Zhu, | F.,White,E.S.,Lama, |     | V.,andSpence,J.R. |     | (2018). |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ------------------- | --- | ----------------- | --- | ------- |
(GN2911).ThisworkwaspartlyundertakenatUCLH/UCL,whichreceiveda
Invitroinductionandinvivoengraftmentoflungbudtipprogenitorcells
| proportion | of funding | from the | Department | of Health’s | NIHR | Biomedical |     |     |     |     |     |     |     |
| ---------- | ---------- | -------- | ---------- | ----------- | ---- | ---------- | --- | --- | --- | --- | --- | --- | --- |
derivedfromhumanpluripotentstemcells.StemCellRep.10,101–119.
ResearchCentre’sfundingscheme.
10.Rawlins,E.L.,Ostrowski,L.E.,Randell,S.H.,andHogan,B.L.M.(2007).
Lungdevelopmentandrepair:contributionoftheciliatedlineage.Proc.
AUTHORCONTRIBUTIONS
Natl.Acad.Sci.USA.104,410–417.
Conceptualization:P.H.,K.L.,D.S.,K.B.M.,andE.L.R.Methodology:P.H.,
11.Trivedi,V.,Choi,H.M.T.,Fraser,S.E.,andPierce,N.A.(2018).Multidi-
K.L.,andD.S.Software:P.H.FormalAnalysis:P.H.,J.P.P.,K.P.,andZ.K.T. mensional quantitative analysis of mRNA expression within intact
|     |     |     |     |     |     |     |     |     | Cell185,4841–4860,December8,2022 |     |     |     | 4857 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------------------------- | --- | --- | --- | ---- |

ll
OPENACCESS Resource
vertebrateembryos.Development145,dev156869.https://doi.org/10. strictions of embryonic p63+ progenitors establish distinct stem cell
1242/dev.156869. poolsinadultairways.Dev.Cell44,752–761.e4.
12. He,P.,Williams,B.A.,Trout,D.,Marinov,G.K.,Amrhein,H.,Berghella,L., 27.Hawkins,F.J.,Suzuki,S.,Beermann,M.L.,Barilla`,C.,Wang,R.,Villa-
Goh,S.T.,Plajzer-Frick,I.,Afzal,V.,andPennacchio,L.A.(2020Jul).The corta-Martin, C., Berical, A., Jean, J.C., Le Suer, J., and Matte, T.
changingmouseembryotranscriptomeatwholetissueandsingle-cell (2021). Derivation of airway basal stem cells from human pluripotent
resolution.Nature583,760–767. stemcells.CellStemCell28,79–95.e8.
13. Cao,J.,O’Day,D.R.,Pliner,H.A.,Kingsley,P.D.,Deng,M.,Daza,R.M., 28.Negretti,N.M.,Plosa,E.J.,Benjamin,J.T.,Schuler,B.A.,Habermann,
Zager,M.A.,Aldinger,K.A.,Blecher-Gonen,R.,Zhang,F.,andSpiel- A.C.,Jetter,C.S.,,Gulleman,P.,Bunn,C.,Hackett,A.N.,andRansom,
mann,M.(2020).Ahumancellatlasoffetalgeneexpression.Science M.(2021).Asingle-cellatlasofmouselungdevelopment.Development
370, eaba7721. https://science.sciencemag.org/content/370/6518/ 148,dev199512.https://doi.org/10.1242/dev.199512.
eaba7721. 29.Lim,K.,Donovan,A.P.A.,Tang,W.,Sun,D.,He,P.,Teichmann,S.A.,
14. Madissoon,E.,Oliver,A.J.,Kleshchevnikov,V.,Wilbrey-Clark,A.,Polan- Marioni,J.C.,Meyer,K.B.,Brand,A.H.,andRawlins,E.L.(2022).Orga-
ski,K.,Orsi,A.R.,Mamanova,L.,Bolt,L.,Richoz,N.,Elmentaite,R.,,and noidmodellingofhumanfetallungalveolardevelopmentrevealsmech-
Pett,J.P.(2021).Aspatialmulti-omicsatlasofthehumanlungrevealsa anismsofcellfatepatterningandneonatalrespiratorydisease.CellStem
novel immune cell survival niche. Preprint at bioRxiv. https://www. Cell.PublishedonlineDecember8,2022.https://doi.org/10.1016/j.stem.
biorxiv.org/content/10.1101/2021.11.26.470108v1. 2022.11.013.
15. Cutz,E.,Gillan,J.E.,andBryan,A.C.(1985).Neuroendocrinecellsinthe 30.Gillich,A.,Zhang,F.,Farmer,C.G.,Travaglini,K.J.,Tan,S.Y.,Gu,M.,
developinghumanlung:morphologicandfunctionalconsiderations.Pe- Zhou,B.,Feinstein,J.A.,Krasnow,M.A.,andMetzger,R.J.(2020).Capil-
diatr.Pulmonol.1,S21–S29. larycell-typespecializationinthealveolus.Nature586,785–789.
16. Negretti,N.M.,Plosa,E.J.,Benjamin,J.T.,Schuler,B.A.,ChristianHab- 31.VilaEllis,L.,Cain,M.P.,Hutchison,V.,Flodby,P.,Crandall,E.D.,Borok,
ermann,A.,Jetter,C.,Gulleman,P.,Taylor,C.J.,Nichols,D.,Matlock, Z.,Zhou,B.,Ostrin,E.J.,Wythe,J.D.,andChen,J.(2020).Epithelial
B.K.,,andGuttentag,S.H.(2021).ASinglecellatlasoflungdevelopment. vegfa specifies a distinct endothelial population in the mouse lung.
Preprint at bioRxiv. https://www.biorxiv.org/content/10.1101/2021.01. Dev.Cell52,617–630.e6.
21.427641v3. 32.Schupp,J.C.,Adams,T.S.,Cosme,C.,Jr.,Raredon,M.S.B.,Yuan,Y.,
17. Zepp,J.A.,Morley,M.P.,Loebel,C.,Kremp,M.M.,Chaudhry,F.N.,Basil, Omote, N., Poli, S., Chioccioli, M., Rose, K.A., and Manning, E.P.
M.C.,Leach,J.P., Liberti,D.C.,Niethamer, T.K.,andYing,Y.(2021). (2021). Integrated single-cell atlas of endothelial cells of the human
Genomic,epigenomic,andbiophysicalcuescontrollingtheemergence lung.Circulation144,286–302.
ofthelungalveolus.Science371,eabc3172.https://doi.org/10.1126/ 33.Takeda,A.,Hollme´n,M.,Dermadi,D.,Pan,J.,Brulois,K.F.,Kaukonen,
science.abc3172. R.,Lo¨nnberg,T.,Bostro¨m,P.,Koskivuo,I.,andIrjala,H.(2019).Single-
18. Borromeo,M.D.,Savage,T.K.,Kollipara,R.K.,He,M.,Augustyn,A.,Os- cellsurveyofhumanlymphaticsunveilsmarkedendothelialcellhetero-
borne,J.K.,Girard,L.,Minna,J.D.,Gazdar,A.F.,Cobb,M.H.,andJohn- geneity and mechanisms of homing for neutrophils. Immunity 51,
son,J.E.(2016).ASCL1andNEUROD1revealheterogeneityinpulmo- 561–572.e5.
nary neuroendocrine tumors and regulate distinct genetic programs. 34.Frid,M.G.,Dempsey,E.C.,Durmowicz,A.G.,andStenmark,K.R.(1997
CellRep.16,1259–1272. Jul).Smoothmusclecellheterogeneityinpulmonaryandsystemicves-
19. Deprez,M.,Zaragosi,L.E.,Truchi,M.,Becavin,C.,RuizGarcı´a,S.,Ar- sels.Importanceinvasculardisease.Arterioscler.Thromb.Vasc.Biol.
guel,M.J.,Plaisant,M.,Magnone,V.,Lebrigand,K.,andAbelanet,S. 17,1203–1209.
(2020).Asingle-cellatlasofthehumanhealthyairways.Am.J.Respir. 35.Hein,R.F.C.,Wu,J.H.,Holloway,E.M.,Frum,T.,Conchola,A.S.,Tsai,
Crit.CareMed.202,1636–1645. Y.H.,Wu,A.,Fine,A.S.,Miller,A.J.,Szenker-Ravi,E.,,andYan,K.S.
20. Carraro,G.,Langerman,J.,Sabri,S.,Lorenzana,Z.,Purkayastha,A., (2022).R-SPONDIN2+mesenchymalcellsformthebudtipprogenitor
Zhang, G., Konda, B., Aros, C.J., Calvert, B.A., and Szymaniak, A. niche during human lung development. Dev. Cell. https://doi.org/10.
(2021).Transcriptionalanalysisofcysticfibrosisairwaysatsingle-cell 1016/j.devcel.2022.05.010.
resolution reveals altered epithelial cell states and composition. Nat. 36.Kumar,M.E.,Bogard,P.E.,Espinoza,F.H.,Menke,D.B.,Kingsley,D.M.,
Med.27,806–814. andKrasnow,M.A.(2014).Mesenchymalcells.Definingamesenchymal
21. VieiraBraga,F.A.,Kar,G.,Berg,M.,Carpaij,O.A.,Polanski,K.,Simon, progenitornicheatsingle-cellresolution.Science346,1258810.
L.M.,Brouwer,S.,Gomes,T.,Hesse,L.,andJiang,J.(2019).Acellular 37.Dahlgren,M.W.,andMolofsky,A.B.(2019Oct).Adventitialcuffs:regional
censusofhumanlungsidentifiesnovelcellstatesinhealthandinasthma. hubsfortissueimmunity.TrendsImmunol.40,877–887.
Nat.Med.25,1153–1163.
38.Travaglini,K.J.,Nabhan,A.N.,Penland,L.,Sinha,R.,Gillich,A.,Sit,R.V.,
22. Yao,E.,Lin,C.,Wu,Q.,Zhang,K.,Song,H.,andChuang,P.T.(2018). Chang,S.,Conley,S.D.,Mori,Y.,andSeita,J.(2020).Amolecularcell
Notchsignaling controlstransdifferentiationofpulmonaryneuroendo- atlasofthehumanlungfromsingle-cellRNAsequencing.Nature587,
crinecellsinresponsetolunginjury.StemCell.36,377–391. 619–625.
23. Ouadah,Y.,Rojas,E.R.,Riordan,D.P.,Capostagno,S.,Kuo,C.S.,and 39.Li,R.,Li,X.,Hagood,J.,Zhu,M.S.,,andSun,X.(2020).Myofibroblast
Krasnow,M.A.(2019).Rarepulmonaryneuroendocrinecellsarestem contraction is essential for generating and regenerating the gas-ex-
cellsregulatedbyRb,p53,andNotch.Cell179,403–416.e23. changesurface.J.Clin.Invest.130,2859–2871.
24. Kaarteenaho,R.,Merikallio,H.,Lehtonen,S.,Harju,T.,and Soini, Y. 40.Efremova,M.,Vento-Tormo,M.,Teichmann,S.A.,andVento-Tormo,R.
(2010).Divergentexpressionofclaudin-1,-3,-4,-5and-7indeveloping (2020).CellPhoneDB:inferringcell–cellcommunicationfromcombined
humanlung.Respir.Res.11,59. expression of multi-subunit ligand–receptor complexes. Nat. Protoc.
25. Guha,A.,Vasconcelos,M.,Cai,Y.,Yoneda,M.,Hinds,A.,Qian,J.,Li,G., 15,1484–1506.
Dickel,L.,Johnson,J.E.,andKimura,S.(2012).Neuroepithelialbody 41.Herbert,S.P.,andStainier,D.Y.R.(2011).Molecularcontrolofendothe-
microenvironmentisanicheforadistinctsubsetofClara-likeprecursors lialcellbehaviourduringbloodvesselmorphogenesis.Nat.Rev.Mol.Cell
inthedevelopingairways.Proc.Natl.Acad.Sci.USA.109,12592–12597. Biol.12,551–564.
26. Yang,Y.,Riccio,P.,Schotsaert,M.,Mori,M.,Lu,J.,Lee,D.K.,Garc´ıa- 42.Miller,A.J.,Yu,Q.,Czerwinski,M.,Tsai,Y.H.,Conway,R.F.,Wu,A.,Hol-
Sastre,A.,Xu,J.,andCardoso,W.V.(2018).Spatial-temporallineagere- loway,E.M.,Walker,T.,Glass,I.A.,andTreutlein,B.(2020).Invitroand
4858 Cell185,4841–4860,December8,2022

ll
Resource OPENACCESS
invivodevelopmentofthehumanairwayatsingle-cellresolution.Dev. ease. Preprint at bioRxiv. https://www.biorxiv.org/content/10.1101/
Cell53,117–128.e6. 2022.03.10.483747v1?ct=.
43.Mou,H.,Vinarsky,V.,Tata,P.R.,Brazauskas,K.,Choi,S.H.,Crooke, 58.Sun,D.,Evans,L.,Perrone,F.,Sokleva,V.,Lim,K.,Rezakhani,S.,Lutolf,
A.K.,Zhang,B.,Solomon,G.M.,Turner,B.,andBihler,H.(2016).Dual M.,Zilbauer,M.,,andRawlins,E.L.(2021).Afunctionalgenetictoolbox
SMAD Signaling Inhibition Enables Long-Term Expansion of Diverse forhumantissue-derivedorganoids. Elife10,e67886. https://doi.org/
EpithelialBasalCells.CellStemCell19,217–231. 10.7554/eLife.67886.
44.Domcke,S.,Hill,A.J.,Daza,R.M.,Cao,J.,O’Day,D.R.,andPliner,H.A. 59.Aibar, S., Gonza´lez-Blas, C.B., Moerman, T., Huynh-Thu, V.A., Imri-
(2020).Ahumancellatlasoffetalchromatinaccessibility.Science370, chova,H.,Hulselmans,G.,Rambow,F.,Marine,J.C.,Geurts,P.,and
eaba7612. https://science.sciencemag.org/content/370/6518/eaba7612. Aerts,J.(2017).SCENIC:single-cellregulatorynetworkinferenceand
abstract. clustering.Nat.Methods14,1083–1086.
45.Quaggin,S.E.,Schwartz,L.,Cui,S.,Igarashi,P.,Deimling,J.,Post,M., 60.Mellitzer,G.,Beucher,A.,Lobstein,V.,Michel,P.,Robine,S.,Kedinger,
andRossant,J.(1999).Thebasic-helix-loop-helixproteinpod1iscriti- M.,andGradwohl,G.(2010).Lossofenteroendocrinecellsinmicealters
callyimportantforkidneyandlungorganogenesis.Development126, lipidabsorptionandglucosehomeostasisandimpairspostnatalsurvival.
5771–5783. J.Clin.Invest.120,1708–1721.
46.Gao,X.,Vockley,C.M.,Pauli,F.,Newberry,K.M.,Xue,Y.,Randell,S.H., 61.Naya,F.J.,Huang,H.P.,Qiu,Y.,Mutoh,H.,DeMayo,F.J.,Leiter,A.B.,
Reddy,T.E.,andHogan,B.L.M.(2013).Evidenceformultiplerolesfor andTsai,M.J.(1997).Diabetes,defectivepancreaticmorphogenesis,
grainyhead-like2intheestablishmentandmaintenanceofhumanmuco- andabnormalenteroendocrinedifferentiationinBETA2/neuroD-deficient
ciliaryairwayepithelium.Proc.Natl.Acad.Sci.USA110,9356–9361. mice.GenesDev.11,2323–2334.
47.Wan,H.,Dingle,S.,Xu,Y.,Besnard,V.,Kaestner,K.H.,Ang,S.L.,Wert,
62.Warner,S.M.B.,Hackett,T.L.,Shaheen,F.,Hallstrand,T.S.,Kicic,A.,
S.,Stahlman,M.T., and Whitsett, J.A. (2005).Compensatory rolesof
Stick,S.M.,andKnight,D.A.(2013).Transcriptionfactorp63regulates
Foxa1 and Foxa2 during lung morphogenesis. J. Biol. Chem. 280,
keygenesandwoundrepairinhumanairwayepithelialbasalcells.Am.
13809–13816.
J.Respir.CellMol.Biol.49,978–988.
48.Corada,M.,Orsenigo,F.,Morini,M.F.,Pitulescu,M.E.,Bhat,G.,Nyqvist,
63.Frank,D.B.,Penkala,I.J.,Zepp,J.A.,Sivakumar,A.,Linares-Saldana,R.,
D.,Breviario,F.,Conti,V.,Briot,A.,andIruela-Arispe,M.L.(2013).Sox17
Zacharias,W.J.,Stolz,K.G.,Pankin,J.,Lu,M.,andWang,Q.(2019).
isindispensableforacquisitionandmaintenanceofarterialidentity.Nat.
Earlylineagespecificationdefinesalveolarepithelialontogenyinthemu-
Commun.4,2609.
rinelung.Proc.Natl.Acad.Sci.USA116,4362–4371.
49.vanSoldt,B.J.,Qian,J.,Li,J.,Tang,N.,Lu,J.,andCardoso,W.V.(2019).
64.Treutlein,B.,Brownfield,D.G.,Wu,A.R.,Neff,N.F.,Mantalas,G.L.,Espi-
Yapanditssubcellularlocalizationhavedistinctcompartment-specific
noza,F.H.,Desai,T.J.,Krasnow,M.A.,andQuake,S.R.(2014).Recon-
rolesinthedevelopinglung.Development146,dev175810.https://doi.
structinglineagehierarchiesofthedistallungepitheliumusingsingle-
org/10.1242/dev.175810.
cellRNA-seq.Nature509,371–375.
50.Kimura,S.,Ostrin,E.J.,andChen,J.(2019).Transcriptionalcontrolof
65.Larsen,H.L.,,andJensen,K.B.(2021).Reprogrammingcellularidentity
lungalveolartype1celldevelopmentandmaintenancebyNKhomeobox
duringintestinalregeneration.Curr.Opin.Genet.Dev.70,40–47.
2-1.Proc.Natl.Acad.Sci.USA116,20545–20555.https://www.pnas.
org/content/116/41/20545.short. 66.Jadhav,U.,Saxena,M.,O’Neill,N.K.,Saadatpour,A.,Yuan,G.C.,Her-
bert,Z.,Murata,K.,andShivdasani,R.A.(2017).DynamicReorganiza-
51.Liberti,D.C.,Liberti,W.A.,III,Kremp,M.M.,Penkala,I.J.,Cardenas-Diaz,
tion of Chromatin Accessibility Signatures during Dedifferentiation of
F.L.,Morley,M.P.,Babu,A.,Zhou,S.,Fernandez,R.J.,,III,andMorrisey,
SecretoryPrecursorsintoLgr5+ Intestinal StemCells. CellStemCell
E.E.(2022).Klf5definesalveolarepithelialtype1celllineagecommitment
21,65–77.e5.
during lung development and regeneration. Dev. Cell57, 1742–1757.
https://doi.org/10.1016/j.devcel.2022.06.007. 67.BarileM.,Imaz-RosshandlerI.,InzaniI.,GhazanfarS.,NicholsJ.,Marioni
J.C., Guibentif, C., and Go¨ttgens, B. Coordinated Changes in Gene
52.Rock,J.R.,Onaitis,M.W.,Rawlins,E.L.,Lu,Y.,Clark,C.P.,Xue,Y.,Ran-
ExpressionKineticsUnderliebothMouseandHumanErythroidMatura-
dell,S.H.,andHogan,B.L.M.(2009).Basalcellsasstemcellsofthe
tion Genome Biol., 22(1), pp.1-22 https://doi.org/10.1101/2020.12.21.
mouse trachea and human airway epithelium. Proc. Natl. Acad. Sci.
423773
USA106,12771–12775.
53.Ito,T.,Udaka,N.,Yazawa,T.,Okudela,K.,Hayashi,H.,Sudo,T.,Guil- 68.Trapnell,C.,Cacchiarelli,D.,Grimsby,J.,Pokharel,P.,Li,S.,Morse,M.,
lemot,F.,Kageyama,R.,andKitamura,H.(2000).Basichelix-loop-helix Lennon,N.J.,Livak,K.J.,Mikkelsen,T.S.,andRinn,J.L.(2014).Thedy-
transcriptionfactorsregulatetheneuroendocrinedifferentiationoffetal namicsandregulatorsofcellfatedecisionsarerevealedbypseudotem-
mousepulmonaryepithelium.Development127,3913–3921. poralorderingofsinglecells.Nat.Biotechnol.32,381–386.
54.Borges,M.,Linnoila,R.I.,vandeVelde, H.J.,Chen,H.,Nelkin,B.D., 69.Choi,H.M.T.,Schwarzkopf,M.,Fornace,M.E.,Acharya,A.,Artavanis,
Mabry,M.,Baylin,S.B.,andBall,D.W.(1997).Anachaete-scutehomo- G.,Stegmaier,J.,Cunha,A.,andPierce,N.A.(2018).Third-generation
logueessentialforneuroendocrinedifferentiationinthelung.Nature386, insituhybridizationchainreaction:multiplexed,quantitative,sensitive,
852–855. versatile, robust. Development 145, dev165753. https://doi.org/10.
1242/dev.165753.
55.Gay,C.M.,Stewart,C.A.,Park,E.M.,Diao,L.,Groves,S.M.,Heeke,S.,
Nabet,B.Y.,Fujimoto,J.,Solis,L.M.,andLu,W.(2021).Patternsoftran- 70.Mimitou,E.P.,Cheng,A.,Montalbano,A.,Hao,S.,Stoeckius,M.,Legut,
scriptionfactorprogramsandimmunepathwayactivationdefinefour M.,Roush,T.,Herrera,A.,Papalexi,E.,andOuyang,Z.(2019).Multi-
majorsubtypesofSCLCwithdistincttherapeuticvulnerabilities.Cancer plexeddetectionofproteins,transcriptomes,clonotypesandCRISPR
Cell39,346–360.e7. perturbationsinsinglecells.Nat.Methods16,409–412.
56.Ireland,A.S.,Micinski,A.M.,Kastner,D.W.,Guo,B.,Wait,S.J.,Spain- 71.CondeC.D.,Domı´nguezCondeC.,XuC.,JarvisL.B.,GomesT.,Howlett
hower,K.B.,Conley,C.C.,Chen,O.S.,Guthrie,M.R.,andSoltero,D. S.K.,Rainbow,D.B.,Suchanek,O.,King,H.W.,andMamanova,L.Cross-
(2020).MYCdrivestemporalevolutionofsmallcelllungcancersubtypes tissue immune cell analysis reveals tissue-specific adaptations and
byreprogrammingneuroendocrinefate.CancerCell38,60–78.e12. clonal architecture in humans Preprint at.bioRxiv. Available from:
https://doi.org/10.1101/2021.04.28.441762
57.Sikkema,L.,Strobl,D.,Zappia,L.,Madissoon,E.,Markov,N.S.,Zara-
gosi,L.,Ansari,M.,Arguel,M.J.,Apperloo,L.,Becavin,C.,,andBerg, 72.KaminowB.,YunusovD.,andDobinA.STARsolo:accurate,fastandver-
M.(2022).Anintegratedcellatlasofthehumanlunginhealthanddis- satilemapping/quantificationofsingle-cellandsingle-nucleusRNA-seq
Cell185,4841–4860,December8,2022 4859

ll
OPENACCESS Resource
data.PreprintatbioRxivhttps://www.biorxiv.org/content/10.1101/2021. 90.Gu,Z.,Eils,R.,andSchlesner,M.(2016).Complexheatmapsrevealpat-
05.05.442755.abstract ternsandcorrelationsinmultidimensionalgenomicdata.Bioinformatics
73. Lun,A.T.L.,Riesenfeld,S.,Andrews,T.,Dao,T.P.,Gomes,T.,andpar- 32,2847–2849.https://doi.org/10.1093/bioinformatics/btw313.
ticipants in the 1st Human Cell Atlas Jamboree, and Marioni, J.C. 91.Hahsler,M.,Hornik,K.,andBuchta,C.(2008).Gettingthingsinorder:an
(2019). EmptyDrops: distinguishing cells from empty droplets in introductiontotheRPackageseriation.J.Stat.Softw.25,1–34.https://
droplet-basedsingle-cellRNAsequencingdata.GenomeBiol.20,63. doi.org/10.18637/jss.v025.i03.
74. Gadala-Maria,D.,Yaari,G.,Uduman,M.,andKleinstein,S.H.(2015). 92.LaManno,G.,Soldatov,R.,Zeisel,A.,Braun,E.,Hochgerner,H.,Petu-
Automatedanalysisofhigh-throughputB-cellsequencingdatareveals khov,V.,Lidschreiber,K.,Kastriti,M.E.,Lo¨nnerberg,P.,andFurlan,A.
a high frequency of novel immunoglobulin V gene segment alleles. (2018).RNAvelocityofsinglecells.Nature560,494–498.
Proc.Natl.Acad.Sci.USA112,E862–E870.
93.Bergen,V.,Lange,M.,Peidli,S.,Wolf,F.A.,andTheis,F.J.(2020).Gener-
75. Stephenson,E.,Reynolds,G.,Botting,R.A.,Calero-Nieto,F.J.,Morgan,
alizingRNAvelocitytotransientcellstatesthroughdynamicalmodeling.
M.D.,Tuong,Z.K.,Bach,K.,Sungnak,W.,Worlock,K.B.,andYoshida,
Nat.Biotechnol.38,1408–1414.
M.(2021).Single-cellmulti-omicsanalysisoftheimmuneresponsein
COVID-19.Nat.Med.27,904–916. 94.VandeSande,B.,Flerin,C.,Davie,K.,DeWaegeneer,M.,Hulselmans,
G.,Aibar,S.,Seurinck,R.,Saelens,W.,Cannoodt,R.,andRouchon,Q.
76. Wolf, F.A., Alexander Wolf, F., Angerer, P., and Theis, F.J. (2018).
(2020). A scalable SCENIC workflow for single-cell gene regulatory
SCANPY:large-scalesingle-cellgeneexpressiondataanalysis.Genome
networkanalysis.Nat.Protoc.15,2247–2276.
Biol.19,1–5.https://doi.org/10.1186/s13059-017-1382-0.
77. Litvin(cid:3)ukova´,M.,Talavera-Lo´pez,C.,Maatz,H.,Reichart,D.,Worth,C.L., 95.Moerman,T.,AibarSantos,S.,BravoGonza´lez-Blas,C.,Simm,J.,Mor-
Lindberg,E.L.,Kanda,M.,Polanski,K.,Heinig,M.,andLee,M.(2020). eau,Y.,Aerts,J.,andAerts,S.(2019).GRNBoost2andArboreto:efficient
Cellsoftheadulthumanheart.Nature588,466–472. andscalableinferenceofgeneregulatorynetworks.Bioinformatics35,
2159–2161.
78. Madissoon,E.,Wilbrey-Clark,A.,Miragaia,R.J.,Saeb-Parsy,K.,Mahbu-
bani,K.T.,Georgakopoulos,N.,Harding,P.,Polanski,K.,Huang,N.,and 96.Imrichova´,H.,Hulselmans,G.,Atak,Z.K.,Potier,D.,andAerts,S.(2015).
Nowicki-Osuch,K.(2019).scRNA-seqassessmentofthehumanlung, i-cisTarget2015update:generalizedcis-regulatoryenrichmentanalysis
spleen,andesophagustissuestabilityaftercoldpreservation.Genome inhuman,mouseandfly.NucleicAcidsRes.43,W57–W64.
Biol.21,1. 97.Lopez,R.,Regier,J.,Cole,M.B.,Jordan,M.I.,andYosef,N.(2018).Deep
79. Popescu,D.M.,Botting,R.A.,Stephenson,E.,Green,K.,Webb,S.,Jar- generativemodelingforsingle-celltranscriptomics.Nat. Methods15,
dine,L.,Calderbank,E.F.,Polanski,K.,Goh,I.,andEfremova,M.(2019). 1053–1058.
Decodinghumanfetalliverhaematopoiesis.Nature574,365–371. 98.Pedregosa,F.,Varoquaux,G.,Gramfort,A.,Michel,V.,Thirion,B.,Grisel,
80. Vento-Tormo, R., Efremova, M., Botting, R.A., Turco, M.Y., Vento- O.,Blondel,M.,Prettenhofer,P.,Weiss,R.,Dubourg,V.,,andVander-
Tormo,M.,Meyer,K.B.,Park,J.E.,Stephenson,E.,Polan(cid:1)ski,K.,and
plas,J.(2011).Scikit-learn:MachineLearninginPython.J.Mach.Learn.
Goncalves,A.(2018).Single-cellreconstructionoftheearlymaternal– Res.12,2825–2830.
fetalinterfaceinhumans.Nature563,347–353.
99.Granja,J.M.,Corces,M.R.,Pierce,S.E.,Bagdatli,S.T.,Choudhry,H.,
81. Kleshchevnikov,V.,Shmatko,A.,Dann,E.,Aivazidis,A.,King,H.W.,Li, Chang,H.Y.,andGreenleaf,W.J.(2021).ArchRisascalablesoftware
T.,Elmentaite,R.,Lomakin,A.,Kedlian,V.,andGayoso,A.(2022).Cell2- packageforintegrativesingle-cellchromatinaccessibilityanalysis.Nat.
locationmapsfine-grainedcelltypesinspatialtranscriptomics.Nat.Bio- Genet.53,403–411.
technol.40,661–671.
100.Yu,G.,Wang,L.G.,Han,Y.,andHe,Q.Y.(2012).clusterProfiler:anR
82. Stuart,T.,Butler,A.,Hoffman,P.,Hafemeister,C.,Papalexi,E.,Mauck,
Package for Comparing Biological Themes Among Gene Clusters.
W.M., III, Hao, Y., Stoeckius, M., Smibert, P., and Satija, R. (2019).
OMICS A J. Integr. Biol. 16, 284–287. https://doi.org/10.1089/omi.
Comprehensiveintegrationofsingle-celldata.Cell177,1888–1902.e21.
2011.0118.
83. Hafemeister,C.,andSatija,R.(2019).Normalizationandvariancestabi-
101.Schneider,C.A.,Rasband,W.S.,andEliceiri,K.W.(2012).NIHImageto
lizationofsingle-cellRNA-seqdatausingregularizednegativebinomial
ImageJ:25yearsofimageanalysis.Nat.Methods9,671–675.
regression.GenomeBiol.20,296.
84. Polan(cid:1)ski,K.,Young,M.D.,Miao,Z.,Meyer,K.B.,Teichmann,S.A.,and 102.Heaton,H.,Talman,A.M.,Knights,A.,Imaz,M.,Gaffney,D.J.,Durbin,R.,
Hemberg,M.,andLawniczak,M.K.N.(2020).Souporcell:robustclus-
Park,J.E.(2020).BBKNN:fastbatchalignmentofsinglecelltranscrip-
teringofsingle-cellRNA-seqdatabygenotypewithoutreferencegeno-
tomes.Bioinformatics36,964–965.
types.Nat.Methods17,615–620.
85. Haghverdi,L.,Buettner,F.,andTheis,F.J.(2015).Diffusionmapsfor
high-dimensionalsingle-cellanalysisofdifferentiationdata.Bioinformat- 103.Megill,C.,Martin,B.,Weaver,C.,Bell,S.,Prins,L.,Badajoz,S.,McCand-
ics31,2989–2998. less,B.,Pisco,A.O.,Kinsella,M.,Griffin,F.,andKiggins,J.(2021).cellx-
gene:aperformant,scalableexplorationplatformforhighdimensional
86. Wolf,F.A.,Hamey,F.K.,Plass,M.,Solana,J.,Dahlin,J.S.,Go¨ttgens,B.,
sparse matrices. Preprint at bioRxiv. https://www.biorxiv.org/content/
Rajewsky,N.,Simon,L.,andTheis,F.J.(2019).PAGA:graphabstraction
10.1101/2021.04.05.438318v1.abstract.
reconcilesclusteringwithtrajectoryinferencethroughatopologypreser-
vingmapofsinglecells.GenomeBiol.20,59. 104.Young,M.D.,andBehjati,S.(2020).SoupXremovesambientRNAcontam-
87. Traag,V.A.,Waltman,L.,andvanEck,N.J.(2019).FromLouvaintoLei- inationfromdroplet-basedsingle-cellRNAsequencingdata.GigaScience
den:guaranteeingwell-connectedcommunities.Sci.Rep.9,1–2.https:// 9, giaa151. https://academic.oup.com/gigascience/article/9/12/giaa151/
doi.org/10.1038/s41598-019-41695-z. 6049831.
88. Cao, J., Spielmann, M., Qiu, X., Huang, X., Ibrahim, D.M., Hill, A.J., 105.Wolock,S.L.,Lopez,R.,andKlein,A.M.(2019).Scrublet:computational
Zhang, F., Mundlos, S., Christiansen, L., and Steemers, F.J. (2019). identificationofcelldoubletsinsingle-celltranscriptomicdata.CellSyst.
Thesingle-celltranscriptionallandscapeofmammalianorganogenesis. 8,281–291.e9.
Nature566,496–502.https://doi.org/10.1038/s41586-019-0969-x. 106.Zhang,Y.,Liu,T.,Meyer,C.A.,Eeckhoute,J.,Johnson,D.S.,Bernstein,
89. Moran,P.A.P.(1950).Notesoncontinuousstochasticphenomena.Bio- B.E.,Nusbaum,C.,Myers,R.M.,Brown,M.,Li,W.,andLiu,X.S.(2008).
metrika37,17–23. Model-basedanalysisofChIP-Seq(MACS).GenomeBiol.9,R137.
4860 Cell185,4841–4860,December8,2022

ll
Resource OPENACCESS
STAR+METHODS
KEYRESOURCESTABLE
| REAGENTorRESOURCE | SOURCE | IDENTIFIER |
| ----------------- | ------ | ---------- |
Antibodies
Mousemonoclonalanti-ACTA2 ThermoFisherScientific Cat#MA1-06110;RRID:AB_557419
PE-conjugatedMousemonoclonal BioLegend Cat#344104;RRID:AB_2255842
anti-THBD(CD141)
Rabbitmonoclonalanti-PDGFRA CellSignalingTechnology Cat#3174;RRID:AB_2162345
Rabbitpolyclonalanti-S100A4 Proteintech Cat#16105-1-AP;RRID:AB_11042591
APC-conjugatedRatmonoclonalanti-CD44 ThermoFisherScientific Cat#17-0441-82;RRID:AB_469390
| Rabbitpolyclonalanti-SOX9 | Merck | Cat#AB5535;RRID:AB_2239761 |
| ------------------------- | ----- | -------------------------- |
Sheeppolyclonalanti-PDPN R&Dsystems Cat#AF3670;RRID:AB_2162070
Ratmonoclonalanti-E-cadherin ThermoFisherScientific Cat#13-1900;RRID:AB_2533005
Chickenpolyclonalanti-KRT5 BioLegend Cat#905901;RRID:AB_2565054
Rabbitpolyclonalanti-SCGB1A1 Proteintech Cat#10490-1-AP;RRID:AB_2183285
Mousemonoclonalanti-FOXJ1 ThermoFisherScientific Cat#14-9965-80;RRID:AB_1548836
| Rabbitmonoclonalanti-SCGB3A2 | Abcam | Cat#14-9965-80; |
| ---------------------------- | ----- | --------------- |
RRID:N/A
| Mousepolyclonalanti-SCGB3A1 | NovusBiological | Cat#MAB27901; |
| --------------------------- | --------------- | ------------- |
RRID:N/A
Biologicalsamples
| Organoidline:HDBR-L13393,15909 | HDBRLondon                   | N/A |
| ------------------------------ | ---------------------------- | --- |
| Organoidline:BRC1943,1915,     | BrainRepairCenter,University | N/A |
| 2174,2315,2316                 | ofCambridge                  |     |
Chemicals,peptides,andrecombinantproteins
| ProteinaseKsolution | ThermoFisherScientific       | Cat#AM2546    |
| ------------------- | ---------------------------- | ------------- |
| N2supplement        | ThermoFisherScientific       | Cat#17502001  |
| B27supplement       | ThermoFisherScientific       | Cat#12587001  |
| N-acetylcysteine    | Merck                        | Cat#A9165     |
| EGF                 | PeproTech                    | Cat#AF-100-15 |
| FGF10               | PeproTech                    | Cat#100-26    |
| FGF7                | PeproTech                    | Cat#100-19    |
| Noggin              | PeproTech                    | Cat#120-10C   |
| R-spondin           | StemCellInstitute,University |               |
ofCambridge
| CHIR99021 | StemCellInstitute,University |     |
| --------- | ---------------------------- | --- |
ofCambridge
| SB431542      | bio-techne | 1614   |
| ------------- | ---------- | ------ |
| cAMP          | Merck      | B5386  |
| IBMX          | Merck      | I5879  |
| Y-27632       | Merck      | 688000 |
| Dexamethasone | Merck      | D4902  |
| Doxycycline   | Merck      | D9891  |
Criticalcommercialassays
| ChromiumSingleCellV(D)JKits(v1)   | 10Xgenomics |     |
| --------------------------------- | ----------- | --- |
| VisiumSpatialGeneExpressionSlide& | 10Xgenomics |     |
ReagentsKit
| ChromiumNextGEMSingleCellATACKits(v1) | 10Xgenomics |        |
| ------------------------------------- | ----------- | ------ |
| In-Fusion(cid:2)HDCloningPlus         | Takara      | 638910 |
(Continuedonnextpage)
Cell185,4841–4860.e1–e9,December8,2022 e1

ll
OPENACCESS Resource
Continued
| REAGENTorRESOURCE | SOURCE | IDENTIFIER |
| ----------------- | ------ | ---------- |
Depositeddata
| scRNA-seqandscV(D)Joflungtissue | ArrayExpress | E-MTAB-11278 |
| ------------------------------- | ------------ | ------------ |
| scRNA-seqoflungorganoids        | ArrayExpress | E-MTAB-11267 |
| Visiumspatialtranscriptomics    | ArrayExpress | E-MTAB-11265 |
| scATAC-seqoflungtissue          | ArrayExpress | E-MTAB-11266 |
Oligonucleotides
| Primer:TCRg/dlibraryPCR1-R1_hTRDC: | Mimitouetal.70 | N/A |
| ---------------------------------- | -------------- | --- |
AGCTTGACAGCATTGTACTTCC
Mimitouetal.70
| Primer:TCRg/dlibraryPCR1-R1_hTRGC |     | N/A |
| --------------------------------- | --- | --- |
TGTGTCGTTAGTCTTCATGGTGTTCC
| Primer:TCRg/dlibraryPCR2-R2_hTRDC | Mimitouetal.70 | N/A |
| --------------------------------- | -------------- | --- |
TCCTTCACCAGACAAGCGAC
Mimitouetal.70
| Primer:TCRg/dlibraryPCR2-R2_hTRGC |     | N/A |
| --------------------------------- | --- | --- |
GATCCCAGAATCGTGTTGCTC
| SI-PCRprimer:AATGATACGGCGACCACCG | Mimitouetal.70 | N/A |
| -------------------------------- | -------------- | --- |
AGATCTACACTCTTTCCCTACACGACGC*T*C
RecombinantDNA
Plasmid:pLenti-tetON-KRAB-dCas9-DHFR- Sunetal.58 Addgene:#167935
EF1a-TagRFP-2A-tet3G
| Plasmid:pLenti-tetON-mNeonGreen-3XNLS-EF1a- | thismanuscript | N/A |
| ------------------------------------------- | -------------- | --- |
TagRFP-2A-tet3G
| Plasmid:pLenti-tetON-ASCL1-EF1a- | thismanuscript | N/A |
| -------------------------------- | -------------- | --- |
TagRFP-2A-tet3G
| Plasmid:pLenti-tetON-NEUROD1-EF1a- | thismanuscript | N/A |
| ---------------------------------- | -------------- | --- |
TagRFP-2A-tet3G
| Plasmid:pLenti-tetON-NEUROG3-EF1a- | thismanuscript | N/A |
| ---------------------------------- | -------------- | --- |
TagRFP-2A-tet3G
| Plasmid:pLenti-tetON-RFX6-EF1a- | thismanuscript | N/A |
| ------------------------------- | -------------- | --- |
TagRFP-2A-tet3G
| Plasmid:pLenti-tetON-TFAP2A-EF1a- | thismanuscript | N/A |
| --------------------------------- | -------------- | --- |
TagRFP-2A-tet3G
| Plasmid:pLenti-tetON-DeltaNP63- | thismanuscript | N/A |
| ------------------------------- | -------------- | --- |
EF1a-TagRFP-2A-tet3G
| Plasmid:pLenti-tetON-PAX9-EF1a- | thismanuscript | N/A |
| ------------------------------- | -------------- | --- |
TagRFP-2A-tet3G
| Plasmid:pLenti-tetON-NKX2-2- | thismanuscript | N/A |
| ---------------------------- | -------------- | --- |
EF1a-TagRFP-2A-tet3G
| Plasmid:pLenti-tetON-PROX1- | thismanuscript | N/A |
| --------------------------- | -------------- | --- |
EF1a-TagRFP-2A-tet3G
Softwareandalgorithms
python-genomics thismanuscript https://github.com/brianpenghe/python-genomics
Seurat3-plus thismanuscript https://github.com/brianpenghe/Seurat3-plus
ImageJ(version:2.1.0) 101 https://imagej.nih.gov/ij/;RRID:SCR_003070
GraphPadPrismsoftware(version:9.1.0) GraphPadSoftwareInc. GraphPadPrism(https://graphpad.com);
RRID:SCR_015807
FlowJosoftware(version:10.0.0) FlowJo,LLC FlowJo(https://www.flowjo.com/);
RRID:SCR_008520
Wolfetal.76
Scanpy(version:1.5.0,1.8.1) https://github.com/theislab/scanpy
bbknn(version:1.5.1) Polan(cid:1)skietal.84 https://github.com/Teichlab/bbknn
Bergenetal.93
| Scvelo(version0.2.3) |     | https://github.com/theislab/scvelo |
| -------------------- | --- | ---------------------------------- |
Monocle3(version:1.0.0) 68,88 https://github.com/cole-trapnell-lab/monocle3
(Continuedonnextpage)
e2 Cell185,4841–4860.e1–e9,December8,2022

ll
Resource OPENACCESS
Continued
REAGENTorRESOURCE SOURCE IDENTIFIER
pySCENIC(version:0.11.2) 59,94 https://github.com/aertslab/pySCENIC
ComplexHeatmap(version2.6.2) Guetal.90 https://github.com/jokergoo/ComplexHeatmap
seriation(version:1.3.0) Hahsleretal.91 https://github.com/mhahsler/seriation
souporcell(version:2.0) Heatonetal.102 https://github.com/wheaton5/souporcell
ArchR(version:1.0.1) Granjaetal.99 https://github.com/GreenleafLab/ArchR
cellxgene(version:0.16.7) Megilletal.103 https://github.com/chanzuckerberg/cellxgene
clusterProfiler(version:3.18.1) Yuetal.100 https://github.com/YuLab-SMU/clusterProfiler
STARsolo(version:2.7.3a) Kaminowetal.72 https://github.com/alexdobin/STAR/blob/
master/docs/STARsolo.md
EmptyDrop Lunetal.73 https://github.com/MarioniLab/DropletUtils
cellranger(versions:3.0.2,4.0.0) 10Xgenomics https://github.com/10XGenomics/cellranger
cellranger-atac(version:1.2.0) 10Xgenomics https://github.com/10XGenomics/cellranger-atac
SoupX(version:1.4.5) Youngetal.104 https://github.com/constantAmateur/SoupX
dandelion(version:0.1.10) Stephensonetal.75 https://github.com/zktuong/dandelion
Scrublet(version0.2.1) Wolocketal.105 https://github.com/swolock/scrublet
macs2(version:2.2.7.1) Zhangetal.106 https://github.com/macs3-project/MACS
SpaceRanger(version:1.1.0) 10Xgenomics https://support.10xgenomics.com/spatial-
gene-expression/software/pipelines/latest/
what-is-space-ranger
Seurat(version3.2.2) Stuartetal.82 https://github.com/satijalab/seurat
sklearn(version:0.24.2) Pedregosaetal.98 https://github.com/scikit-learn/scikit-learn
CellPhoneDB(version:2.1.7) Vento-Tormoetal.80 https://github.com/Teichlab/cellphonedb/
RESOURCEAVAILABILITY
Leadcontact
Furtherinformationandrequestsforresourcesandreagentsshouldbedirectedtoandwillbefulfilledbytheleadcontact,EmmaL.
Rawlins(elr21@cam.ac.uk).
Materialsavailability
Human lung organoid lines used in this study are available from the lead contact, Emma L. Rawlins (elr21@cam.ac.uk), with a
completedMaterialsTransferAgreement.
Dataandcodeavailability
d SequencingdatahavebeendepositedatArrayExpressandENAandarepubliclyavailable.Accessionnumbersarelistedinthe
keyresourcestable.Processedsequencingdataandmicroscopydatareportedinthispaperareavailableathttps://fetal-lung.
cellgeni.sanger.ac.uk/.ATAC-seqpseudobulkcoverageprofilescanbebrowsedathttps://genome.ucsc.edu/s/brianpenghe/
scATAC_fetal_lung20211206
d AlloriginalcodehasbeendepositedatGitHubandispubliclyavailableasofthedateofpublication.Linksarelistedinthekey
resourcestable.
d Anyadditionalinformationrequiredtoreanalyzethedatareportedinthisworkisavailablefromtheleadcontactuponrequest.
EXPERIMENTALMODELANDSUBJECTDETAILS
Humanlungtissue
HumanembryonicandfetallungtissueswereprovidedfromterminationsofpregnancyfromCambridgeUniversityHospitalsNHS
FoundationTrustunderpermissionfromNHSResearchEthicalCommittee(96/085)andtheMRC/WellcomeTrustHumanDevelop-
mentalBiologyResource(LondonandNewcastle,UniversityCollegeLondon(UCL)siteRECreference:18/LO/0822;Newcastlesite
RECreference:18/NE/0290;Project200419;www.hdbr.org).Sampleagerangedfrom4to23weeksofgestation(post-conception
weeks;pcw).Stagesofthesamplesweredeterminedaccordingtotheirexternalphysicalappearanceandmeasurements.Sample
names and gestational ages are listed in Table S3. None of the samples used for the current study had any known genetic
Cell185,4841–4860.e1–e9,December8,2022 e3

ll
OPENACCESS Resource
abnormalities.Samplegenderwasunknownatthetimeofcollection,butmolecularly-inferredsamplegenderisavailableontheweb
interface(https://lungcellatlas.org).
EthicalapprovalfortheadulthumanlungsampleswasgivenbytheSouthCentralHampshireBResearchEthicsCommittee(REC
reference18/SC/0514,IRASproject:245471)administeredthroughtheUniversityCollegeLondonHospitalsNHSFoundationTrust.
HumanadultlungsampleswerealsoobtainedfromRoyalPapworthHospitalTissueResearchBank(RECreference:18/EE/0269).
METHODDETAILS
Cellisolationfor10XsinglecellRNAandATACseq
ProximalanddistalregionsforhumanfetallungsamplesR15pcwwereseparatedasindicatedinFigure1andmincedwithscissors.
Wholefetallungsamples<15pcwweredirectlymincedwithscissors.Mincedtissuesweretransferredintoa15mLFalcontubeand
mixedwith5mLofdissociationsolution(collagenase,0.125mg/ml,Sigma,C9891-100MG;dispase,1U/ml,Merck,4942078001;
DNaseI, 0.1 mg/mL, Merck, D4527-10KU). The mixture was incubated in a shaker incubator at 37(cid:4)C with horizontal shaking at
135rpmfor30min(after15minofincubation,themixturewastrituratedwith10mLstraightpipette).5mLofterminationsolution
(2%fetalbovineseruminPBS)wasaddedtoterminatethedigestionreaction.Abriefspinat100Xgwasperformedtopelletlarge
tissuepieces.Thesupernatantwaspassedthrougha40mmfilterandcellsamplesextractedforthesinglecellRNAandATACseq
protocols.Anylargeundigestedpieceswerefurthertrypsinizedwith3mLof5Xtrypsin(TrypsinEDTAX10,ThermoFisherScientific,
15400054)for3–6minin37(cid:4)Cwaterbathstofurtherexposeepithelialcells.Thereactionwasstoppedusing5mLoftermination
solution, filtered through a 40 mm cell strainer and collected. Cells were pelleted at 500X g for 5 min at 4(cid:4)C. If the pellets were
red,aredbloodcell(RBC)removal stepwas performedbyresuspendingcellsin1XRBClysisbuffer(ThermoFisher,00-4300-
54) for 3 min at room temperature. RBC lysis buffer was neutralised with 10 mL of termination solution. The cell suspension
waspassedthrougha40mmfilteragain.Forsomeofthetrypsinizedcells,aCD326(EpCAM)MACSenrichment(MiltenyiBiotec,
130-061-101)wasperformedtofurtherenrichepithelialcells.Cellswerecounted,pelletedandresuspendedinappropriatevolume
with PBS/0.04%BSA and single cell RNA and ATAC seq was carried out using 10X Chromium Single Cell V(D)J Kits (v1) and
ChromiumNextGEMSingleCellATACKits(v1),respectively.
Humanfetallungorganoidmaintenance
Humanfetallungorganoidswerederivedandmaintainedaspreviouslydescribed.8Inbrief,humanfoetallungtissuesweretreated
withDispase(8U/mlThermoFisherScientific,17105041)atroomtemperature(RT)for2mintodigestmesenchymalconnections.
Mesotheliumandmesenchymalcellswerecarefullyremovedbyneedles.Branchingepithelialtipsweremicro-dissectedbyneedles,
transferredintoMatrigel(356231,Corning)andseededina24welllow-attachmentplate(M9312-100EA,Greiner)with4–5tipsper
50mLMatrigeldomeperwell.Theplatewasincubatedat37(cid:4)Cfor5–10minuntiltheMatrigeldomessolidified.600mLofself-renew-
ing medium containing: N2 (1: 100, Thermo Fisher Scientific, 17502001), B27 (1: 50, Thermo Fisher Scientific, 12587001),
N-acetylcysteine(1.25mM),EGF(50ng/mL,PeproTech,AF-100-15),FGF10(100ng/mL,PeproTech,100–26),FGF7(100ng/mL,
PeproTech,100-19),Noggin(100ng/mL,PeproTech,120-10C),R-spondin(5%v/v,StemCellInstitute,UniversityofCambridge),
CHIR99021(3mM,StemCellInstitute,UniversityofCambridge)andSB431542(10mM,bio-techne,1614),wasadded.Organoids
wereculturedunderstandardtissuecultureconditions(37(cid:4)C,5%CO2),maintainedinself-renewingmediumandpassagedbyme-
chanicallybreakingusingP200pipettesevery4–7days.
Humanfetallungorganoidbronchiolardifferentiation
Theprogenitororganoidswereexpandedinself-renewalmediuminBME(BasementMembraneExtract,R&DSystems,3533-010-
02).Forairwaydifferentiation,theorganoidsweredissociatedbyTrypLEandculturedinthedifferentiationmedium(AdvDMEM+++,
1XB27,1XN2,1.25mMN-acetylcysteine,100ng/mLFGF10,100ng/mLFGF7,50nMDexamethasone,0.1mMcAMP,0.1mM
IBMX,10mMY-27632)for15–30days.
IsolationandairwaydifferentiationofSCGB3A2+distalandproximalairwaycells
Human fetal lungs at 8–11 pcw were carefully separated, and tip/stalk, distal airway, and proximal airway regions were further
dissectedusingfineforcepsunderadissectingmicroscope(FigureS5G).Thetissuefragmentswereenzymaticallydigestedintosin-
glecellsbytreatingthemindissociationsolutioncontaining0.125mg/mLCollagenase,1U/mlDispaseand0.1U/mlDNAase,ina
rotatingincubatorfor20minat37(cid:4)C.Thecellsweretreatedwith1XRBClysisbuffer(ThermoFisher,00-4300-54),andwereenriched
byCD326MACSbeadsaccordingtothemanufacturer’sinstructions.Theenrichedepithelialcellsfromdistalandproximalregions
wereinfectedwithalentivirushabouringSCGB3A2promoter-drivenEGFPwithEF1apromoterdriven-TagRFP.Next,theinfected
TagRFPcellsweresortedbyEGFPexpressionbyFACSandanalysedbyqRT-PCRafter48h(FiguresS5GandS5H).Thesorted
distalandproximalSCGB3A2-GFPpositivecellswereculturedfor28and45daysintheairwaydifferentiationmedium.
RNAextraction,cDNAsynthesis,andqRT-PCRanalysis
Theculturedlungorganoidswerecollectedandlysed.TotalRNAwasextractedaccordingtotheRNeasyMiniKit(Qiagen,74004)
procedure.cDNAsynthesiswasperformedusingHigh-CapacitycDNAReverseTranscriptionKit(AppliedBiosystems,4368814)and
e4 Cell185,4841–4860.e1–e9,December8,2022

ll
Resource OPENACCESS
thesynthesisedcDNAwasdiluted1:20fortheqRT-PCRreaction(SYBRGreenPCRMasterMix;AppliedBiosystems,4309155).
PrimersequenceinformationislistedinTableS5.Datawerepresentedasfold-change,calculatedbyddCtmethod,usingACTB
asareferencegenecontrol.
Humanfetallungorganoidimmunofluorescence
ThedifferentiatedorganoidswerereleasedfromtheBMEandfixedin4%PFAat4(cid:4)Cfor30min.Thentheorganoidswerewashedin
PBS,incubatedin0.3%PBTX(0.3%TritonX-100inPBS)at4(cid:4)Cfor1h,andblocked(1%bovineserumalbumin,5%normaldonkey
serum,0.3%TritonX-100inPBS)at4(cid:4)Covernight.Theorganoidswereincubatedwithprimaryantibodies:SCGB3A2(1:800,Abcam,
ab181853), KRT5 (1: 500, BioLegend, 905901), E-cadherin (1: 500; Thermo Fisher Scientific, 13-1900), SOX9 (1: 400; Merck,
AB5535), SCGB1A1 (1: 800, Proteintech, 10490-1-AP), SCGB3A1 (1:200, Novus Biological, MAB27901), FOXJ1 (1: 300, eBio-
science,14-9965-80)at4(cid:4)Covernight.TheorganoidswerewashedbyPBSandfurtherincubatedwithsecondaryantibodies(donkey
anti-chicken488,1:1000,JacksonImmunoresearch,703-545-155;donkeyanti-mouse594,1:1000,Invitrogen,A-21203;donkey
anti-rabbit594,1:1000,Invitrogen,A-21207;donkeyanti-rat647,1:1000,JacksonImmunoresearch,712-605-153;donkeyanti-rab-
bit647,1:1000,Invitrogen, A-31573). AfterDAPIstaining(1mg/mL)at4(cid:4)Cfor1hour,theorganoids wereprocessedthrougha
thiodiethanolseries(25%,50%,75%and97%v/vconcentrationinPBS)at4(cid:4)Cforimaging.
Plasmidcloning
cDNAsforgenesASCL1,NEUROD1,NEUROG3,RFX6andPAX9werepurchasedfromGenscript.cDNAsforgeneTFAP2Aand
mNeonGreen-3XNLSweregiftsfromAzimSurani’sGroup.cDNAforDeltaNTP63waspurchasedfromIDTasagBlockfragment.
cDNA sequences were cloned into a Doxycycline inducible vector pLenti-tetON-KRAB-dCas9-DHFR-EF1a-TagRFP-2A-tet3G
(Addgene:#167935)58usingXhoIandBamHIsitesbyInfusioncloning(Takara,638910).
A promoter region (chr5:147,878,065 + 147,878,803; 739 bp) of SCGB3A2 was amplified using primers: 50-AATTGAATCCCA
GGTTTTTCAAAAGACACT-30 and50-GACAGTTATCTGGGATATTTTTCAGGAGTTT-30.Theampliconswereclonedintoalentiviral
vector, pLenti-(promoter)-EGFP/EF1a-TagRFP by Infusion (Takara, 638909). Plasmids used in this study will be deposited to
Addgene.
Lentiviruspackaging
Wepackagedthelentivirusasdescribedpreviously.58Inbrief,HEK293Tcellsweregrownin10-cmdishesto70–80%confluence.
Lentiviral vector (10 mg) was co-transfected with packaging MD2.G (3 mg, Addgene plasmid # 12259), psPAX2 (6 mg, Addgene
plasmid#12260)andpAdVAntage (3mg,E1711,Promega) usingLipofectamine 2000TransfectionReagent(11668019,Thermo
FisherScientific)accordingtomanufacturer’sprotocol.Mediumwasrefreshedthenextmorning.Lentiviruscontainingcellmedium
washarvestedat24and48haftermediumrefreshingandpooledtogether.Cellfragmentswereremovedby300Xgcentrifugation.
Supernatantwasthenpassedthrougha0.45mmfilter.LentiviruswasconcentratedusingLenti-X(cid:3)Concentrator(631232,Takara)
accordingtothemanufacture’sinstructions.Lentiviruspelletsweredissolvedin400mLPBS,aliquotedandfrozenin(cid:3)80(cid:4)C.
Lentivirustransduction
Lentivirustransductionwasperformedaspreviouslydescribed.58Inbrief,humanfetallungorganoidsderivedfrom3independent
donorswereincubatedwithprewarmedTrypLEfor10minwithtriturationafter5min.Organoidsinglecellsandsmallfragments
were collected, counted, pelleted and resuspended to around 100K cells/500 mL self-renewing medium with ROCKi (10 mM
Y-27632). 0.5–2 mL of lentivirus was added and incubated overnight. Organoid cells were harvested the next morning, pelleted
andre-seededintoMatrigel.
OverexpressionoftranscriptionfactorsandscRNA-Seq
After3daysoflentivirustransduction,organoidsweredissociatedbyincubationwithprewarmedTrypLEfor10minwithtrituration
after5min.TagRFPpositivecellsweresorted(20–40%ofTagRFPpositiverate),seededbacktoMatrigelandallowedtorecoverfor
10–12dayswithself-renewingmediumplusROCKi(10mMY-27632).OrganoidsweretreatedwithDoxycycline(2mg/mL)for3days.
OrganoidswerethenfullydissociatedintosinglecellsbyincubationwithprewarmedTrypLE(ThermoFisherScientific,12605028)for
15–20minwithtriturationevery5min.Organoidcellswerecounted,pelleted,resuspendedinproperamountsofPBS/0.04%BSA
andproceededtoscRNA-Seqaccordingto10XChromiumSingleCellV(D)JKitmanual.
Insituhybridizationchainreactionandimmunofluorescence
InsituHCRv3.0wasperformedaccordingtothemanufacturer’sprotocol(MolecularInstruments.69Probesweredesignedaccord-
ingtothemanual,andamplifierswithbuffersweresuppliedbyMolecularInstruments.Allthesequenceinformationoftheprobesis
listedinTableS5.Inbrief,thefrozenhumantissuesectionsfixedin4%PFA/DEPC-treatedPBSwerecutinto20mmslicesandrinsed
innuclease-freeultrapurewater,followedby10mg/mLproteinaseKsolution(ThermoFisherScientific,AM2546)for2minat37(cid:4)C.
ForinsituHCRwithimmunostaining,thetissuesliceswerepermeabilizedin0.3%Triton-X/DEPC-treatedPBSfor5minatroomtem-
perature,avoidingthetreatmentoftheproteinaseKsolution.Next,thetissuesliceswereincubatedwith2pmolofprobesat37(cid:4)C
overnight. After washing, the slices were treated with 6 pmol of the amplifiers at room temperature overnight. The amplifiers,
Cell185,4841–4860.e1–e9,December8,2022 e5

ll
OPENACCESS Resource
consistingofapairofhairpinsconjugatedtofluorophores,Alexa488,546,or647,wereusedatfinalconcentrationof0.03mM.Then,
excesshairpinswererinsedin5XSSC(sodiumchloridesodiumcitrate)solutioncontaining0.1%TritonX-100.Nucleiwerecounter-
stainedwithDAPI.FortheimmunostainingfollowingtheinsituHCR,thetissuesliceswereincubatedwithablockingsolutioncon-
taining5%NDS,1%BSA,0.1%Triton-XinDEPC-treatedPBSatroomtemperaturefor1hafterthehairpinamplification.Afterrinsing
withDEPC-treatedPBS,treatedwithprimaryantibodiesagainstACTA2(1:500;ThermoFisherScientific,MA1-06110),THBD(1:100;
PE-conjugated;BioLegend,344104),PDGFRA(1:200;CellSignalingTechnology,3174),S100A4(1:200;Proteintech,16105-1-AP),
CD44 (1:200; Thermo Fisher Scientific, 17-0441-82), SOX9 (1: 200, Merck, AB5535), PDPN (1:200; R&D Systems, AF3670), or
E-cadherin(1:500;ThermoFisherScientific,13-1900)overnight.Secondaryantibodiesweretreatedfor3hatroomtemperature.
ThetissuewaswashedthreetimesinDEPC-treatedPBSatroomtemperatureandcounterstainedwithDAPI.Imageswerecollected
underLeicaSP8confocalmicroscope.
Librarygenerationandsequencing
ChromiumSingleCell5’V(D)JReagentKits(V1.0chemistry)wereusedforscRNAseqlibraryconstruction.Geneexpressionlibraries
(GEX)andV(D)Jlibrarieswerepreparedaccordingtothemanufacturer’sprotocol(10XGenomics)usingindividualChromiumi7Sam-
pleIndices.Librariesforgamma/deltaTCRvariableregionswereamplifiedaspreviouslydescribed.70,71GEXandV(D)Jwerepooled
in1:0.1ratiorespectivelyandsequencedonaNovaSeq6000S4orIlluminaHiSeq4000Flowcell(paired-end(PE),150-bpreads)
aimingforaminimumof50,000PEreadspercellforGEXlibrariesand5,000PEreadspercellforV(D)Jlibraries.
Visiumspatialtranscriptomics
Fetallungsamplesat12–20postconceptionweek(pcw)fromtheHDBR,upto0.5cm3insize,wereembeddedinOCTandflash-
frozenindry-icecooledisopentane.Twelve-microncryosectionswerecutontoVisiumslides,haematoxylinandeosinstainedand
imagedat20XmagnificationonaHamamatsuNanozoomer2.0HTBrightfield.Thesewerethenfurtherprocessedaccordingtothe
10XGenomicsVisiumprotocol,usingapermeabilizationtimeof18minfor12–17pcwsamplesand24minfor19pcwandolder
samples.Imageswereexportedastiledtiffsforanalysis.Dual-indexedlibrarieswerepreparedasinthe10XGenomicsprotocol,
pooledat2.25nMandsequencedin4samplesperIlluminaNovaseqSPflowcellwithreadlengthsof28bpforR1,10bpfori7index,
10bpfori5index,90bpforR2.
Readsmappingandquantification
scRNA-seq data were mapped with STARsolo 2.7.3a72 to the 10X distributed GRCh38 reference, version 3.0.0, derived from
Ensembl93.Cellcallingwaspost-processedwithanimplementationofEmptyDrops73extractedfromCellRanger3.0.2(distributed
asemptydropsonPyPi).Fortransducedorganoidcells,exogenousgeneswereaddedtothereferenceasappropriatefororganoids,
withthetransgenesequencetruncated(length(R2)-1)bpaftertheendofthesyntheticpromotertoavoidreadsfromendogenous
transcriptsbeingmappedontotransgenes.Forsingle-cellV(D)Jdata,readsweremappedwithCellRanger4.0.0tothe10Xdistrib-
utedVDJreference,version4.0.0.VisiumreadsweremappedwithSpaceRanger1.1.0tothe10XdistributedGRCh38reference,
version 3.0.0, derived from Ensembl 93 for consistency with the single cell data. scATAC reads were mapped with Cellranger-
atac1.2.0toreferenceGRCh38-1.2.0.
VDJanalysis
BothTCRandBCRcontigscontainedinrespectiveall_contigs.fastaandall_contig_annotations.csvfileswerere-annotatedwith
igblastn (v1.17.1) using reference sequences curated from IMGT database (downloaded 01-Aug-2021) as per described with
changeo(v1.0.0).ForBCRcontigs,heavychainconstantregioncallswerere-annotatedusingblastn(v2.12.0+)againstcuratedse-
quencesofCH1regionscorrespondingtorespectiveisotypeclassesfromIMGT.BCRheavychainV-genealleleswerecorrectedfor
individualgenotypesusingtigger(v1.0.0).74Contigswerethenfilteredforbasicqualitycontrolasdescribedpreviously.75Briefly,the
followingoccurrenceswouldleadtoremovalofcontigsfromfurtheranalysis:i)contigswereannotatedwithV,D,Jorconstantgene
callsthatarenotfromthesamelocus;ii)multiplelong/heavychaincontigspresentinthesamecell;iii)therewereonlyshort/light
chaincontigsinacell;and/oriv)therearemultipleshort/lightchaincontigsinacell.Cellswithmultiplecontigswerenevertheless
retainedifa)contigswereassessedtohaveidenticalV(D)Jsequencesbutwereassignedtoadifferentcontigbycellranger-vdj(pre-
sumablyduetodifferencesinnon-V(D)Jelements);b)UMIcountdifferenceswerelargeinwhichcasethecontigwiththehighestUMI
countisretained;andc)onlyIgMandIgDwerebothassignedtoacell.Thesecheckswereallperformedusingdandelion75singularity
container(v0.1.10).
Single-cellRNA-seqprocessingandcelltypeannotation
CountmatriceswereloadedintoScanpyandconcatenated.Cellsexpressingnomorethan200genes,andgenesdetectedinno
morethan5cells,wereremoved.Cellshavingmorethan20%oftheirreadsmappedtomitochondriawerealsodiscarded.Counts
werethendividedbytotalcountsandmultipliedbyafactorof10000,followedbylogtransformation,allimplementedinScanpy’s
(cid:1) (cid:3)
defaultsetting.76Y = ln PXij ,10000 + 1 ,whereX istherawcountofithgeneinjthcell.
ij n
i=1
Xij ij
e6 Cell185,4841–4860.e1–e9,December8,2022

ll
Resource OPENACCESS
Featuregeneswereselectedinthreesteps:Foreachsample,highlyvariablegeneswerecalculatedusingScanpy’sdefaultset-
tingsthatextractgeneswithhighestdispersion(variancedividedbymean)valuesoflog-transformedcounts.Next,highlycorrelated
genesforeachsamplewereextractedusingtheDeepTreealgorithmdescribedin,12reimplementedinourpython-genomicstoolkit.
Genesextractedinatleasttwosamplesweremergedasthefinalfeaturegenelist.Thelog-transformedcountsofthesegeneswere
thenscaledaftercell-cyclescoreswereregressedoutusingScanpy’sdefaultscoringandregressionfunctions.Usingthetop50PCs
and10neighborswithresolutionat0.01,initialclusteringwasgenerated,yielding10majorclusters(FigureS1C)correspondingto
different compartments. These clusters were subsequently and recursively subclustered, curated and annotated manually
(FigureS1D).AnnotationwasbasedonmarkerssummarisedinTableS1.
ArtefactevaluationandremovalforscRNA-seqdata
DoubletswereevaluatedusingScrubletinabatch-by-batchfashion(FigureS1G).Tocaptureraredoubletclusters,wedevelopeda
method for Doublet Cluster Labeling (DouCLing, Figure S1E). Briefly, we calculated relative marker genes for each subcluster
comparedtoothersubclustersinthesameparentallargecluster.Thenthesemarkergeneswereusedtoscoreallthecellsinthe
atlas.Ifthetop-scoringcells(abovethemeanscoreofthecurrentsubcluster)aremostly(>60%)fromanotherlargecluster,the
clustersareflaggedasdoublet-like(FigureS1G’).Wethenremoveddoublet-likeclustersbasedonthesetwomethodswithmanual
curation(FigureS1G’’).
MaternallyderivedcellswereevaluatedbasedonSNPvariationsbetweenthetranscribedpaternalgenomeinthefetusesandthe
maternalcounterpartsinthematernalcells.Todothis,weindexedandpooledsamplesfromthesamedonorinto‘‘Supersamples’’.
ThenweappliedSouporcelltocompareknowncommonvariantscapturedinscRNA-seqreads,settingthesamplenumberto2.
Supersampleswithoutmaternalcellswouldsplitintotwoequal-sizedgroupswhileothersupersampleswouldputativelycapture
maternal cells as a minor genotype group (Figure S1F). Based on this analysis, maternal-like cells do not contribute to scRNA-
seq clusters (Figure S1J) and were thus kept for downstream analysis. For libraries with two multiplexed donors, we only used
theSouporcellworkflowtodemultiplexthedonorswithoutmaternalgeneticdetection.
Low-qualitycellswouldusuallyhavearelativelyhighpercentageofmitochondriareads(FigureS1I’)oralownumberofgenesde-
tected(FigureS1I).Basedonthesewemanuallycuratedandremovedlow-qualityclusters(FigureS1I’’).
Anadditionalfourclustersofcontaminantscomingfromotherorganswerefurtherremoved(FigureS1H).Thesewerecardiomyo-
cytes (ACTN2+ MYH6+),77 esophagus epithelial cells (SOX2+ TP63+ TRH+,78 APOA1+ APOA2+)79 and cytotrophoblasts from the
placenta(PAGE4+GSTA3+).80
Visiumspatialtranscriptomicsdataanalysis
TwomethodswereusedsidebysidetopredictcellcompositionsoftheVisiumdatasets.MappedVisiumandfilteredscRNA-seq
data (removing cell types that have fewer than 20 cells) were both fed into the default pipeline of the cell2location algorithm,81
with the default detection alpha set to 20. The q05_cell_abundance was used as a conservative estimate of cell abundance in
eachvoxel.Thismethodwasusedtogeneratefigurepanelsinthismanuscript.Inthealternativemethod,mappedVisiumcount
matricesandscRNA-seqcountmatrices(afterartefactremoval)werebothimportedintoSeurat382andtransformedusingSCTrans-
form,83 with mitochondria percentage of scRNA-seq data regressed out. Next, the scRNA-seq data were subsetted into a
‘‘pcw11,15,18’’subgroupanda‘‘pcw18,20,22’’subgroupforcell-typeprediction.ThepredictionwasdoneforeachVisiumlibrary
usingitscorrespondingscRNA-seqsubgroupfollowingthedefaultlabeltransferpipelineofSeuratusingthetop50PCs.Weprovide
theresultsofbothmethodsonourdataportal.
Differentialgeneexpressionalongtrajectories
ThesinglecelltranscriptomicsdatawaspreprocessedusingScanpy76version1.8.1.Thecellcycleeffectwasregressedoutusing
scanpy.pp.regress_outandbatchcorrectionwasperformedusingbbknn,84beforedenoisingtheknn-graphusingdiffusionmaps85
withscanpy.tl.diffmapandapplyingPAGA86withscanpy.tl.pagatoexaminetheconnectivitiesbetweencelltypes.ThefinalUMAPs
werecomputedusingtheresultsofPAGAonLeiden87clustersaspreviouslydescribed.86DataandUMAPswereexportedintoR,
andmonocle368,88wasusedtofindaprincipalgraphanddefinepseudotime.Differentiallyexpressedgeneswerethencomputed
alongpseudotimeusingagraph-basedtest(morans’I)88,89andtheprincipalgraphinmonocle3,whichallowsidentificationofgenes
upregulatedatanypointinpseudotime.TheresultswerevisualisedwithheatmapsusingthecomplexHeatmap90andseriation91
packages,aftersmoothinggeneexpressionwithsmoothingsplinesinR(smooth.spline,df=12).
CellPhoneDBanalysis
Filteredsingle-cellRNA-seqdatawerepartitionedintoearly-(5-6pcw),middle-(9–11)andlate-stage(15–22)subsetsandgrouped
intobroadcelltypes.ThesedatasetswereusedasinputforCellPhoneDB80(command:cellphonedbmethodstatistical_analysis
–database v2.0.0 –threads 20 –counts-data gene_name –project-name FetalLungBroad –subsampling –subsampling-log False
–subsampling-num-cells = $TotalCellNumber –iterations = 10000 –result-precision = 4). Interaction pairs were manually curated
fromtheoutputs.
Cell185,4841–4860.e1–e9,December8,2022 e7

ll
OPENACCESS Resource
Velocityanalysis
Velocityanalysis92wasperformedusingscvelo93version0.2.3.Thepreprocesseddatasetwasmergedwithsplicedandunspliced
readcountscomputedwithvelocyto,beforeusingscvelo.pp.moments,scvelo.tl.velocityandscvelo.tl.velocity_graphtocompute
velocitiesusingthestochasticmodeinscvelo.
Generegulatorynetworkanalysis
TheScenicpipeline59,94wasused(pySCENICversion0.11.2)topredicttranscriptionfactorsandputativetargetgenesregulated
throughoutneuroendocrinecelldifferentiation.First,generegulatoryinteractionswerecalculatedbasedonco-expressionacross
thesinglecelldatasetwithGRNBoost2,95followedbypruninginteractionsusingknownTFbindingmotifsandtheconstructionof
datasetspecificregulatorymodules(regulons).96RegulonswerethenscoredineachindividualcellusingAUCell.Cellsoftheneuro-
endocrinedifferentiationtrajectorycomputedwithmonocle3(asdescribedabove)wereselected.Theregulontargetgeneswere
filteredfordifferentiallyexpressedgenesalongpseudotimeforthistrajectory.AnetworkofTFsandtargetgeneswasthencon-
structedbylinkingindividualregulons.
ComparingfetalneuroendocrinetranscriptomewithSCLC
A-typeandN-typesignatureswereselectedfrompreviousdata‘ASCL1HighandNEUROD1HighGeneSignaturesandtheStratified
PrimaryTumorSamples’.18Top10geneswiththehighestfoldenrichmentwereselectedtoscoreepithelialcells,usingScanpy’s
tl.score_genesfunction.
ComparingscRNA-seqdatasetsofthefetallungandotherstudies
Annotated scRNA-seq adult lung datasets,14 the multi-organ scRNA-seq dataset,13 and the mouse scRNA-seq dataset17 were
downloaded.OrthologsweretranslatedfrommousetohumancounterpartsusingENSEMBLbiomart.scVI97wasusedtointegrate
ourfetallungscRNA-seqandtheMadissoonetal.andZeppetal.data(human-mouseorthologsonly),withsampleIDsandproject
IDsbothincludedascategoricalcovariatekeys(otherparameters:n_latent=30,encode_covariates=True,dropout_rate=0.2,
n_layers=2,early_stopping=True,train_size=0.9,early_stopping_patience=45,max_epochs=400,batch_size=1024,limit_
train_batches=20,use_gpu=True).ThelatentvariablescalculatedbyxcVIwerefedintoScanpy’spl.correlation_matrixfunction
to calculate and visualise correlation scores. A logistic regression model was trained based on the fine-grained cell-types for
each of the multi-organ data, using sklearn.linear_model.LogisticRegression.98 The trained model was then used to predict the
celltypesofsingle-celltranscriptomicprofilesofthefetallung(FigureS1O).
Single-cellATAC-seqprocessingandannotation
Cellranger-atacoutputswereloadedintoandprocessedbyArchR.99Thetop50dimensionswereusedforLSIandnobatcheffect
was carried out to preserve weak biological features. Doublets were removed using ArchR’s default settings. Cells with
TSSEnrichmentscore<8orReadsInTSS<1000werediscarded.Initialclusteringwasperformedatresolution=0.01tobeconsistent
withscRNA-seq,resultingin7largeclusterscorrespondingtocompartments.Theseclusterswerefurthersubclustered,similartothe
workflowforscRNA-seq.
Toannotatecelltypesanddoublets,theannotatedscRNA-seqdatasetwasloadedintoSeurat3bySeurat3-plusandintegratedto
scATAC-seqdatausingArchR.Thepredictedcelltype/statelabelswereusedasamajorreferenceforannotation.Clustersmapped
toscRNA-seqdoubletclusterswereremoved.Clusterswithhighfractionsofblacklistedreadswerealsomanuallydiscarded.
Peakswerethencalledbasedonpseudo-bulkcoveragesbymacs2.Markerpeakswerecalculatedwithdefaultsettings.Motifs
fromcis-bpdatabasethatareenrichedinmarkerpeakswerecalculatedandplotted.
ComparingorganoidscRNA-seqwithfetallungscRNA-seq
OrganoidscRNA-seqdatawereimportedandfilteredinthesamewayasdescribedabove.Organoiddatawerethenprojectedonto
fetaltissuedatabyScanpy’stl.ingestfunction.DonorsweredemultiplexedusingSouporcellwithk=3donors,basedoncommon
variants.
QUANTIFICATIONANDSTATISTICALANALYSIS
HCRimageanalysis
InsituHCRimageswereanalyzedusingImageJ(https://imagej.nih.gov/ij/)forquantificationandstatisticalanalysis.Cellsexpressing
airwaylineagemarkersalongdistaltoproximalairwayaxisatdifferentages,mid(10–12pcw)andlate(15–21pcw)stages,were
counted(FigureS4B).Formeasuringtheproportionofproximalsecretorylineagecellswithinproximalcartilaginousairwayregions,
thefetaltissuesectionsat10–12,15–16,and19–21pcwwereanalysedbasedonexpressionpatternsofSCGB3A2,SCGB3A1,and/
orSCGB1A1(FigureS4C).Mean,SD,1-wayANOVA,and2-wayANOVAwerecalculatedusingthePrismsoftware(GraphPadPrism).
Significancewasevaluatedby1or2-wayANOVAwithTukeymultiplecomparisonpost-test;ns=notsignificant,*p<0.05,**p<0.01,
***p<0.001,****p<0.0001.
e8 Cell185,4841–4860.e1–e9,December8,2022

ll
Resource OPENACCESS
Statisticalanalysisforcell-typecompositionbiases
Chi-squaredtestofindependencewasperformedforsamplegestationage,cell-cyclestageandproximal/distaldissectionregions
against cell type categories. For proximal/distal biases, Fisher exact test was used for each cell type and Benjamini-Hochberg
correctionwasperformedformultipletesting.
Wealsovisualisedtheeffectsizeforcellcompositionbiasesoverdevelopmentalageandproximal/distaldissectioninFigureS1O.
Afterremovingtheclustersthatarespecifictotheveryearlystagesinlowabundance(suchasneuronalclusters),cellnumbercounts
werenormalisedagainsttotalnumbercountsperstage.Themeandevelopmentalstageforeachclusterwascalculatedbasedonthe
empiricaldistributionbasedontheaforementionednormalisedcounts,denotedbyx.Theweightedprobabilityyofproximalrepre-
sentationwascalculatedasthefrequencyofcellsfromproximalsamplesnormalisedagainsttotalnumbersofcellsfromproximal
samples,ignoringwhole-lungsamples.ThexandyvalueswerecalculatedforFigureS1O.
(cid:4)P
| X2 2              | C             | t n C                       |
| ----------------- | ------------- | --------------------------- |
| = ;               | =P t(cid:5);s | (cid:4) t P=t1 t ;s (cid:6) |
| x t sp sjt wherep | sjt           |                             |
|                   | 2 2           | C t n C                     |
| s = 5             | s = 5         | t;s t =t 1 t;s              |
(cid:4)
C C
| y =      | (cid:4) t;prox prox | (cid:4) |
| -------- | ------------------- | ------- |
| t        | +C                  |         |
| C t;prox | C prox t;dist       | C dist  |
where(x,y)arethexandycoordinatesofacelltypet,sisthepostconceptionweek,C isthenumberofcellslabelledascelltypet
t t t,s
atstages,C andC arethenumbersofcellslabelledascelltypetcomingfromproximalanddistalsamples,respectively.
t,prox t,dist
Markergenecalculation
Ambrient RNA was removed withSoupX 1.4.5 with default parameters. Using the corrected count matrices, Scanpy.tl.rank_ge-
nes_groupswasappliedwithdefaultsettingsbutkeepingallthegenes.TheserankedgeneswerethenfilteredusingScanpy.tl.fil-
ter_rank_genes_groups with max_out_group_fraction = 0.25 and min_fold_change = 2. To compare specific cell types in the
samecompartment,Scanpy.tl.rank_genes_groupswasappliedforeachcelltypewithonlytheothercelltypesofthiscompartment
asareference.Over-representationanalysis(hypergeometrictest)withgenesetsfromGOBP,KEGGandMSigDBwasperformed
usingtheclusterProfilerRpackage.100
Cell185,4841–4860.e1–e9,December8,2022 e9

ll
Resource OPENACCESS
Supplemental figures
(legendonnextpage)

ll
OPENACCESS Resource
FigureS1. QualitycontrolforscRNA-seqandscATAC-seqdataandclusteringoverviewof144celltypesorcellstates,relatedtoFigures1
andS7
(A)Distributionsofthenumberofgenesdetectedpercell,groupedby10Xlibraries.
(B)ProportionsofbroadcelltypesinsamplestreatedwithTrypsinandTrypsinplusEPCAMenrichmentfollowingcolorcodesinFigure1C.
(C)Initialclustersofdata-separatingcompartments,beforesubclustering.
(D–F)Workflowsoftherecursivesubclusteringmethod(D),theDoubletClusterLabeling(DouCLing)methodtoidentifydoublet-drivenclusters(E),andinference
ofmaternalcellsusingSouporcell(F).
(G)DoubletscoresbyScrublet(G),inferreddoubletclustersbyDouCLing(G’),andcellsincurateddoubletclusters(G’’).
(H)Cellsinclustersofcellscomingfromotherorgans.Markergenesinparentheses.
(I)Numberofgenes(I),percentageofmitochondrialreads(I’),andcellsincuratedlow-qualitycellclusters(I’’)wereprojectedonUMAP.
(J)Inferredmaternalcells.
(KandL)scATAC-seqqualitymetricsoffragmentdetectionpercell(K)andreadsmappedintranscription-startsites(L).
(M)Allofthecurated144clustersofsinglecellsprojectedonUMAPspaceoftranscriptomes,coloredbyinferredcell-cyclephase(M),anddissociation/
enrichmentstrategy(M’).
(N)CellsfromtheinitialPNScluster(C7)projectedonUMAPspaceoftranscriptomes,coloredbycelltype/state(N)andselectedfeaturegenesofcelltypes/
states(N’)intheinitialPNScluster.
(O)Spatiotemporalbiasesofcelltypes.Celltypesareshownasdots,withxrepresentingtheweightedaverageofdevelopmentalstages,yrepresentingthescore
ofproximalenrichment,andthesizecorrespondingtotheclustersize.
(P)UMAPembedding(P)anddotplots(P’)ofmyeloidcelltypes/states.
(Q)UMAPembedding(Q),dotplots(Q’),andenrichmentofeachclassofimmunereceptorsbasedonabTCR,gdTCR,andBCR-enrichedscRNA-seq(Q’’),inT,
NK,andILClymphoidcellcompartments.
(R)UMAPembedding(R),dotplots(R’),andenrichmentofimmunereceptorsbasedonBCR-enrichedscRNA-seq(R’’),inBlymphoidcellcompartment.
(S)Predictedorgan-of-sourcewithhighestscoresforcellsshowninFigure1,basedonthereferenceatlasinCaoetal.13
(T)UMAPvisualizationoferythroidandendothelialcellscoloredbycelltypes/states(T),stages(T’),anddotplotdescribingdifferentialmarkergeneexpression
levelbycelltype(T’’).

ll
Resource OPENACCESS
(legendonnextpage)

ll
OPENACCESS Resource
FigureS2. ComparingfetallungscRNA-seqwithadulthumanandmouselungscRNA-seq,relatedtoFigure1
(A–F)CorrelationsofscVIlatentvariablesbetweenhumanfetallungcellclustersandthoseofpreviouslyannotatedadultcellclusters1(A–C)andmouselungcell
clusters2(D–F),focusingonepithelial(A,D),fibroblast(B,E),andendothelial(C,F)compartments.
(G)Expressionofgenessharedoruniquetofetal/adultlungAT1/AT2cellclusters.

ll
Resource OPENACCESS
(legendonnextpage)

ll
OPENACCESS Resource
FigureS3. SpatialanalysisofairwayepithelialcellsinthedevelopinghumanlungsbyinsituHCR,relatedtoFigure2
(A)Tipandstalkepithelialcellsindistalregionsoffetallungsat17pcw,immunostainedusingantibodiesagainstCD36(tipepithelialcells,red),PDPN(stalk
epithelialcells,white),andE-cadherin(epithelium,cyan).
(BandB’)Airwayprogenitorcellsindistalfetallungsat10(B)and16(B’)pcw.TheairwayprogenitorcellsmarkedbySOX9-/CYTL1+/SCGB3A2+arelocated
proximallytotheCYTL1-/SCGB3A2-stalk.SCGB1A1indicatesclubcells(B,white).SFTPCismainlyexpressedinthetipandpartlylocatedinstalkregions
(B’,green).
(C)GHRL+neuroendocrine(dashedline,red)andGRP+pulmonaryneuroendocrinecells(arrow,green)infetallungsat22pcw.SFTPCindicatestipepithelial
cells(white).
(D)Airwayprogenitor(arrowhead)andclubcells(arrow)innon-cartilaginousairwayregionsoffetallungsat12pcwaremarkedbySCGB3A2+/SCGB1A1-and
SCGB3A2+/SCGB1A1+,respectively.Tip,stalk,airwayprogenitor,andclubcellsarelocalizedprogressivelymoreproximallyfromthedistaltipregionstothe
proximalnon-cartilaginousairwayregions.SCGB3A2(green),SCGB1A1(red).
(E)Proximalsecretory1(arrowhead)and2(arrow)aredistinguishablebythepresenceorabsenceofSCGB1A1expression,eachmarkedbySCGB3A1+/
SCGB1A1low/-/MUC16low/-andSCGB3A1+/SCGB1A1+/MUC16low/+,respectively,intheproximalcartilaginousairwayin15pcwfetallungs.MUC16+onlycells
areMUC16+ciliatedcells.SCGB3A2(green),SCGB1A1(red),MUC16(white).
(F)Proximalsecretory2(arrowhead)and3(arrow)aredistinguishablebythepresenceorabsenceofSCGB3A2andMUC16expression,markedbySCGB3A2+/
SCGB1A1+/MUC16low/+andSCGB3A2low/-/SCGB1A1+/MUC16+,respectively,intheproximalcartilaginousairwayoffetallungsat15pcw.SCGB3A2(green),
SCGB1A1(red),MUC16(white).
(G)Submucosalglandcells(arrow)locatedinSMGsaremarkedbystrongLTFexpressionwithSCGB3A1+/SCGB3A2-intheproximalcartilaginousairway
regionsoffetallungsat15pcw.SCGB3A2(green),LTF(red),SCGB3A1(white).
(H)CiliatedcellsandsecretorycellsaredistinguishablebyexpressionofFOXJ1(red)orSCGB3A2(green)inthenon-cartilaginousairwayregionsat19pcwlungs.
Ciliatedcells(arrowhead),FOXJ1+/SCGB3A2-;secretorycells(arrow),FOXJ1-/SCGB3A2+.
(I)MUC16+ciliatedcells(dashedline),ciliatedcells(dashedcircle),andsecretorycells(arrow)locatedintheproximalcartilaginousairwayregionsoffetallungsat
19pcw.TheMUC16+ciliatedcellsexpressMUC16(white)withaweaklevelofFOXJ1(red),whereastheciliatedcellsonlyexpressstrongFOXJ1withoutMUC16
expression.SCGB3A2(green).
(JandJ’)Proximalbasalcells(J,dashedline)linethebasallayeroftheproximalcartilaginouspseudostratifiedairwayinfetallungsat19pcwandaremarkedby
TP63(red),F3(white),andIGFBP3(green).Incontrast,onlyafewTP63+basalcells(J’,red,arrowheads)areobservedinthenon-cartilaginous,non-pseu-
dostratifiedairwayregions.
(K)ASCL1+pulmonaryneuroendocrine(arrow)andMUC5AC+/ASCL1+progenitors(arrowhead)inthenon-cartilaginousairwayregionsoffetallungat12pcw.
MUC5AC(green),ASCL1(red),SCGB3A2(white).DAPI,nuclei.Scalebars,50mm.
(L)Diagramdescribingspatiallocationofepithelialcelltypesobservedinthedevelopinghumanlungs.

ll
Resource OPENACCESS
(legendonnextpage)

ll
OPENACCESS Resource
FigureS4. Spatiotemporallocation,distribution,andquantificationofmajorepithelialcelltypesalongthedistal-to-proximalaxisofthe
developinglungs,relatedtoFigure2
(A)InsituHCRanalysisoffetalhumanlungtissuesatmid(10–12pcw)andlate(15–21pcw)stages,showingspatiotemporallocationanddistributionofmajor
epithelialcelltypesalongthedistaltoproximalaxisofthedevelopinglungs.Thelungregionsweredividedforimagingintotip,stalktoterminalairway,distalto
proximalnon-cartilaginousairway,andproximalcartilaginousairway.
(B)Quantificationofcellsexpressingmarkergenesofairwaylineagesalongtheairwayregionsatmid(10–12pcw,upper)andlate(15–21pcw,lower)stages.
SCGB3A2,airwayprogenitors/allsecretorylineagecells;CYTL1,airwayprogenitorcells;NDUFA4L2,club/proximalsecretorycells;FMO2,club/proximal
secretorycells;FOXJ1,ciliatedcells;TP63,basalcells;SCGB1A1,club/proximalsecretorycells;SCGB3A1,proximalsecretorycellsubtypes1–3.Significance
wasevaluatedby1-wayANOVAwithTukeymultiplecomparisonpost-test;n=3biologicalreplicates;ns:notsignificant,*p<0.05,**p<0.01,***p<0.001,
****p<0.0001.
(C)Proportionofproximalsecretoryprogenitorcells,proximalsecretorycellsubtypes1–3withintheproximalcartilaginousairwayregionsbyages,at10–12,15–
16,and19–21pcw.Thesecretorycellsintheproximalcartilaginousairwayregionswerecounted:ProxSecretoryProg,SCGB3A2+SCGB3A1(cid:3)SCGB1A1-;Prox
Secretory1,SCGB3A2+SCGB3A1+SCGB1A1-;ProxSecretory2,SCGB3A2+SCGB3A1+SCGB1A1+;ProxSecretory3,SCGB3A2(cid:3)SCGB3A1+SCGB1A1+.Club
cellslocatedinthenon-cartilaginousairwayregionswereexcluded.Significancewasevaluatedby2-wayANOVAwithTukeymultiplecomparisonpost-test;n=4
biologicalreplicates;ns:notsignificant,*p<0.05,**p<0.01,***p<0.001.
(D)Diagramdescribingspatiotemporaldistributionofmajorcell-typemarkersalongthedistaltoproximalaxisofthedevelopinglungs,atmidandlatestages.Mid
stageonly,blue;Latestageonly,red;Mid-to-latestages,green.Arrowsindicatenarrowed(CYTL1)orexpanded(NDUFA4L2,FOXJ1)distributionaftermid-to
late-stagetransition.
(E)InsituHCRanalysisofrarecelltypemarkersofputativeionocytes(FOXI1yellow)andtuftcells(POU2F3,red).E-cadherin,green.DAPI,nuclei.Scale
bar,50mm.

ll
Resource OPENACCESS
(legendonnextpage)

ll
OPENACCESS Resource
FigureS5. Trajectoryanalysisofairwaylineagedifferentiationviaairwayprogenitorcellsinthedevelopinghumanlung,relatedtoFigure2
(AandA’)UMAPvisualization(A)andPAGAanalysis(A’)ofalineagetrajectoryfrommid-tiptoproximalsecretorylineagecells,includingproximalsecretory
progenitorandproximalsecretorycellsubtypes1to3.Midandlatebasalcellswereshowntobedisconnectedfromotherproximalsecretorycelltypesinthe
PAGAanalysis(A’).
(BandC)TrajectoryUMAPs,bycelltype(B)andstages(B’),andtherelevantgeneexpressionheatmap(C)displayingtheselectedlineagetrajectoryfrommid-tip
toproximalsecretorycellsubtypes1and2,analyzedbyMonocle3.(NotethatthegraylinesinUMAPindicateallofthepredicteddifferentiationpathsfromauser-
definedstartingpoint.).(D,D’)UMAPvisualization(D)andPAGAanalysis(D’)ofalineagetrajectoryfromlatetip,latestalk,andlateairwayprogenitor,toclubcells.
Basalcells,includinglatebasal,proximalbasal,andSMGbasalcellswereshowntobeleftoutofthetrajectoryastheydonotconnectclearlytotheothercell
typesinthisanalysis(D’).
(EandF)TrajectoryUMAPs,bycelltypes(E)andstages(E’),andtherelevantgeneexpressionheatmap(C)showingtheselectedlineagetrajectoryfromlate-tipto
clubcells,analyzedbyMonocle3.
(G)PurificationofdistalSCGB3A2-GFP+airwaycellsfromhumanfetallungtissuesat8–11pcw.TheepithelialcellswereisolatedusingEPCAMmagnetic
microbeads(MACS)fromthedissecteddistalandproximalairwaytissues,followedbyinfectionwithlentivirushabouringSCGB3A2promoter-drivenGFP.The
SCGB3A2-GFPpositivecellfractionsweresortedandanalyzedbyFACSafter48handinvitroculturedfor28and45daysintheairwaydifferentiationmedium.
(H)GeneexpressionprofileofthefreshlypurifiedSCGB3A2-GFPpositivecellsderivedfromdistalandproximalairwaytissueswereinvestigatedbyqRT-PCR
andcomparedwithdissectedtipcells.SOX9,distaltipprogenitormarker.CYTL1,airwayprogenitormarker.SCGB1A1andSCGB3A2,airway/secretorycell
lineagemarkers.SCGB3A1,proximalsecretorycellmarker.DatawasnormalizedtoSCGB3A2-GFPnegativecellsderivedfromdistaltip/stalktissues;mean±
SDof3biologicalreplicates.Significancewasevaluatedby1-wayANOVAwithTukeymultiplecomparisonpost-test;*p<0.05,**p<0.01,***p<0.001.(I)Gene
expressionanalysisoftheinvitroculturedSCGB3A2-GFPpositivecells(airwayprogenitors)derivedfromdistalairwaytissuesbyqRT-PCR.Airwayorganoids
wereformedfromtheSCGB3A2-GFPpositivecellsandcollectedatDay0,14,and28daysafterculturefortheanalysis.DatawerenormalizedtoSCGB3A2-GFP
negativecellsderivedfromdistaltip/stalktissues;mean±SDof4biologicalreplicates.Significancewasevaluatedby1-wayANOVAwithTukeymultiple
comparisonpost-test;ns:notsignificant,*p<0.05,**p<0.01.(J-M)Immunofluorescenceanalysisoftwobiologicallyindependent,SCGB3A2-GFP+cell-derived
airwayorganoidsculturedintheairwaydifferentiationmediumfor28(J-L)and45(M)days.SCGB1A1(J,red),airwayprogenitor/secretorycellmarker.TP63(K,
red),basalcellmarker.FOXJ1(L,magenta),ciliatedcellmarker.SCGB3A1(M,red),proximalsecretorycellmarker.DAPI,nuclei.Scalebar,50mm.

ll
Resource OPENACCESS
(legendonnextpage)

ll
OPENACCESS Resource
FigureS6. LateepithelialtipcellsdifferentiatetoAT2andAT1cells,relatedtoFigure3
(AandB)UMAPvisualization(A)ofalineagetrajectoryfromearly/mid/latetiptofetalAT2andAT1cellsandtherelevantgeneexpressionheatmap(B)showingthe
selectedlineagetrajectoryanalyzedbyMonocle3.
(C)InsituHCR(TPPP3andSFTPC)andimmunostaining(SOX9)analysisof15pcwfetallung,describingSOX9+TPPP3+SFTPC+tipepithelialprogenitors(lines)
andSOX9(cid:3)TPPP3(cid:3)SFTPC+fetalAT2cellpopulation(dashedcircles)liningthestalk.
(D)Immunostainingof21pcwfetallungusingantibodiesagainstSOX9(red),PDPN(white),andE-cadherin(green).Arrowsindicatethelate-tipcellpopulation,
whichdoesnotco-expressthestalkmarker,PDPN.
(E–G)InsituHCRanalysisof19(F)and21pcw(E,G)fetallungs,showingtheSFTPC+fetalAT2cellpopulation(arrowheads)liningthedevelopingairsacs.Arrows
indicateSFTPC+late-tipcells.(E)SFTPC(red).(F,G)NAPSA(white;F)andETV5(red;G)overlapwithSFTPCinthefetalAT2cells.
(H–J)InsituHCRanalysisofdistallungregionsat17(H),20(I),and21(J)pcw,visualizingSFTPC(cid:3)/SPOCK2-stalkcellsandSFTPC(cid:3)fetalAT1cells(arrows).
SFTPC(cid:3)/SPOCK2-stalkcellsat17pcw(H)begantoexpressSPOCK2(red)at20pcw(I)andfurtherdevelopedtofutureAT1cells(SFTPC(cid:3)/SPOCK2+)at21pcw
(J).Dashedcircles(I)andarrowheads(J)indicatefetalAT2cells.Dashedline(J)showsfetalAT1cellsliningthedevelopingairsacs.DAPI,nuclei.Scale
bars,50mm.

ll
Resource OPENACCESS
(legendonnextpage)

ll
OPENACCESS Resource
FigureS7. SpatialanalysisofendothelialandmesenchymalcelltypesinthedevelopinghumanlungsbyinsituHCRassayandimmuno-
staining,relatedtoFigure4
(A)TrajectoryUMAPandPAGAplotvisualizingpotentialendothelialcelllineagehierarchyfromMid/Latecapillaryendothelialcellstoarterialendothelialcells,
aerocytes,orvenousendothelialcellscoloredbycelltypesandstages.
(B–E)InsituHCRanalysisofdistallungregionsat20(C,D),and21(B,E)pcw.
(B)Aerocytes(S100A3+red/CA4+white),capillaryendothelium(CA4+white),andallendothelialcells(PECAM+,green).
(C)Arterialendothelialcells(GJA5+red),(D)venousendothelialcells(ACKR3+white),andallendothelialcells(PECAM+,green).
(E)Lymphaticendothelialcells(PROX1+white)andallendothelialcells(PECAM+,green).DAPI,nuclei.Scalebars,50mm.
(F)VascularSMC1and2aresurroundingarterialendothelialcells(PECAM1+,dashedline),eachmarkedbyNTN4+/PLN(cid:3)/low(vSMC1,arrows)andNTN4+/
PLN+/high(vSMC2,lines).
(G)DotplotdescribingdifferentialgeneexpressionbetweenvascularSMC1and2.
(H)VascularSMCsandadventitialfibroblastsin17pcwfetallung.NDUF4AL2+red/NTRK3+vSMCs(arrows)aresurroundedbyNDUF4AL2-/NTRK3+adventitial
fibroblasts(arrowheads).PECAM1(green)indicatesanendothelialcelltube.
(I)FAM162B+pericytes(red)aresurroundingPECAM1+endothelialcells(green)inthemicrovascularregions.
(J)Dotplotdescribingdifferentialmarkergeneexpressionlevelbetweenalveolar,adventitialandairwayfibroblasts.
(K–M)Immunostainingoffetallungtissuesat11(K),15(L),and21(M)pcw,tovisualizemyofibroblastpopulations:Myofibroblast-1(K)and(cid:3)2(L)surroundingthe
developingstalkepithelialtubes,andMyofibroblast-3(M)surroundingthedevelopingairsacs.ACTA2+/PDGFRA+Myofibroblast-1(THBDweak;K)and(cid:3)2
(THBDhigh,arrows;L).PDGFRA+Myofibroblast-3at21pcwdoesnotexpressACTA2(arrows;M).
(N)Dotplotdescribingdifferentialgeneexpressionlevelbetweenmyofibroblast-2and-3.Themyofibroblast-2populationshowedenrichedexpressionofWnt
signalingassociatedgenes,e.g.,NOTUM,LEF1,andDACH2.
(O)InsituHCRassayof17pcwfetallungtissues.Myofibroblast-2expressesNOTUM(red),aWntantagonist,toblocklocalWntsignalsfromalveolarfibroblasts
(white,WNT2)tothestalkepithelium.DAPI,nuclei.Scalebars,50mm.

ll
Resource OPENACCESS
(legendonnextpage)

ll
OPENACCESS Resource
FigureS8. TranscriptionfactorregulatorynetworkcontrollingNEsubtypes,relatedtoFigure7
(A)Selectedtrajectoryfrommid-tipcellstoGHRL+NEcellsviaIntermediateNEs,atransitioncellpopulation.
(B)Heatmapofgenesdifferentiallyexpressedalongthetrajectory.
(C)RepresentativeHCRimagesshowingthetransitionbetweentwotypesofNEcells.GRP(green),NEUROD1(red),GHRL(white).#1labeledGRP+NEUR-
OD1lowGHRL-cells,whichhavejuststartedthetransitionfromGRP+pulmonaryNE/precursorcells.#2labeledGRPlowNEUROD1+GHRLlowcells,intransitionto
GHRL+NEcells.#3labeledGRP-NEUROD1+GHRL+,GHRL+NEcells.Right:Mean±SEMofNEUROD1+celltypes.11pcw:N=2fetallungs,n=129NEUROD1+
cells;12pcwN=3fetallungs,n=132NEUROD1+cells.Scalebars,25mminallpanels.
(D)RepresentativeHCRimagesshowingNEUROG3co-expressionwithASCL1andNEUROD1.Dashedwhitelineslabelrepresentativecellsshowingdifferent
combinationsofthethreetranscriptionfactors,furtherindicatedby#1-#5labeling.ASCL1(cyan),NEUROG3(red),NEUROD1(yellow).
(E)RepresentativeHCRimagesshowingRFX6expressioninGHRL+NEcells.DashyellowlinelabeledGRP+RFX6-pulmonaryNEcells.Scalebars,25mminall
panels.
(F)Representativeepifluorescentmicroscopicimagesshowingorganoidmorphologyafter3daysofmNeonGreen-3xNLS(control),ASCL1,orNEUROD1
overexpression.
(G)ScRNA-seqresultsoforganoidtranscriptionfactoroverexpressionoverlayonhumanfetallungscRNA-seqasareference.
(H)scRNA-seqresultsoftranscriptionfactoroverexpression;organoiddataonlyintheUMAP.Selectedtranscriptionfactorexpressionwasshowninthemiddle
panel.AregulatorynetworkoftheselectedtranscriptionfactorsweredrawnbasedontheorganoidOEdataatthebottomofthepanel.(Notethatthearrowsdo
notnecessarilydenotedirectinteractions).