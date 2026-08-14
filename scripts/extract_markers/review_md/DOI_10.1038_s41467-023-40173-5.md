| Article   |              |       |           | https://doi.org/10.1038/s41467-023-40173-5 |     |
| --------- | ------------ | ----- | --------- | ------------------------------------------ | --- |
| Guided    | construction |       | of single | cell reference                             |     |
| for human | and          | mouse | lung      |                                            |     |
1,2 ,MichaelP.Morley3,4,5,ChengJiang1,YixinWu1,
| Received:31May2022 |     | MinzheGuo   |                       |                  |     |
| ------------------ | --- | ----------- | --------------------- | ---------------- | --- |
|                    |     | GuangyuanLi | 6,YinaDu1,ShuyangZhao | 1,AndrewWagner1, |     |
Accepted:13July2023 AdnanCihanCakar1,MichalKouril 6,KangJin 6,NathanGaddis7,
JosephA.Kitzmiller1,KathleenStewart3,4,MariaC.Basil3,4,SusanM.Lin3,4,
|     |     | YunYing3,4,ApoorvaBabu3,4,KathrynA.Wikenheiser-Brokamp |     |     | 1,8,9, |
| --- | --- | ------------------------------------------------------ | --- | --- | ------ |
Checkforupdates KyuShikMun10,11,AnjaparavandaP.Naren10,GeremyClair 12,
|                                 |     | JoshuaN.Adkins | 12,GloriaS.Pryhuber | 13,RaviS.Misra13,  |                  |
| ------------------------------- | --- | -------------- | ------------------- | ------------------ | ---------------- |
|                                 |     |                | 2,6,TimothyL.Tickle | 14,NathanSalomonis | 2,6,XinSun15,16, |
| ;,:)(0987654321 ;,:)(0987654321 |     | BruceJ.Aronow  |                     |                    |                  |
EdwardE.Morrisey3,4,5,JeffreyA.Whitsett 1,2,NHLBILungMAPConsortium*&
1,2,6
YanXu
Accuratecelltypeidentificationisakeyandrate-limitingstepinsingle-cell
dataanalysis.Single-cellreferenceswithcomprehensivecelltypes,repro-
ducibleandfunctionallyvalidatedcellidentities,andcommonnomenclatures
aremuchneededbytheresearchcommunityforautomatedcelltypeanno-
tation,dataintegration,anddatasharing.Here,wedevelopacomputational
pipelineutilizingtheLungMAPCellCardsasadictionarytoconsolidatesingle-
celltranscriptomicdatasetsof104humanlungsand17mouselungsamplesto
constructLungMAPsingle-cellreference(CellRef)forbothnormalhumanand
mouselungs.CellRefsdefine48humanand40mouselungcelltypescatalo-
guedfromdiverseanatomiclocationsanddevelopmentaltimepoints.We
demonstratetheaccuracyandstabilityofLungMAPCellRefsandtheirutility
forautomatedcelltypeannotationofbothnormalanddiseasedlungsusing
multipleindependentmethodsandtestingdata.Wedevelopuser-friendlyweb
interfacesforeasyaccessandmaximalutilizationoftheLungMAPCellRefs.
Single-cell RNA-seq (scRNA-seq) analysis is being widely applied in publishedscRNA-seqdatasetasareferenceforsupervisedclassifica-
biomedicalresearch,enablingthestudyofcomplexorgans,suchas tion of user-supplied datasets include the lack of comprehension
thelung,atunprecedentedscaleandresolution,andtransformingour (missingcelltypes),inclusionofspeculativecelltypes/statesthathave
understandingoforgandevelopmentanddisease1–4.Accuratecelltype not been functionally validated, technology specific-biases in the
identificationisanecessarystepinsingle-celldataanalysisthatusually referenceorquery,andinsufficientpowertorepresenttherepertoire
requirestime-consumingprocessestooptimizecomputationalpara- of common healthy lung cell types. The lack of common cell type
metersfollowedbymanualinspectionthatrequiresdomainexpertise. nomenclatures and guidelines for single cell transcriptomic studies
WiththeincreasingnumberofpublishedscRNA-seqdatasetsandthe alsocreatessubstantialtechnicalchallengesfordataintegrationand
release of large-scale cell atlases, advanced computational tools5–7 comparison.Therefore,single-cellreferenceswithcomprehensivecell
have been developed using annotated datasets to predict celliden- types,functionallyvalidatedcellidentities,andstandardizednomen-
tities in new datasets. Common issues related with the use of a clature are much needed by the research community to optimize
Afulllistofaffiliationsappearsattheendofthepaper. *Alistofauthorsandtheiraffiliationsappearsattheendofthepaper.
e-mail:minzhe.guo@cchmc.org;yan.xu@cchmc.org
1
| NatureCommunications|(        2023)1  | 4:4566  |     |     |     |     |
| ------------------------------------- | ------- | --- | --- | --- | --- |

| Article |     |     |     |     |     |     |     |     |     | https://doi.org/10.1038/s41467-023-40173-5 |     |     |     |     |
| ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------ | --- | --- | --- | --- |
automatedcelltypeannotationandfacilitatedataintegration,sharing, CellRefs.Theseinterfacesincludetheuseoftherecentlydeveloped
andcollaboration. Azimuthinterface5,whichenablesresearchinvestigatorstoannotate
Agrowingnumberofcommunity-wideeffortshavebeendevoted theirownscRNA-seqdatasetautomaticallyusingtheLungMAPCell-
tothedevelopmentofcommoncelltypenomenclature,includingcell Refs, via automated supervised classification, prior user-annotation
type ontologies of the Human Cell Atlas8 and mammalian brain9. comparison, and exploration against the CellRef for any scRNA-seq
Recently,theLungMAPconsortiumproducedaLungMAPCellCards10,
|     |     |     |     |     |     |     |     | input | dataset. | We developed | functions | to facilitate | evaluation | of  |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | -------- | ------------ | --------- | ------------- | ---------- | --- |
arigorouscatalogoflungcellsbasedonacommunity-wideeffortthat automated cell type annotation results using CellRef marker genes.
synthesizes current functional and single-celldata from humanand Using multiple independent methods and testing data, and bench-
mouselungsintoacomprehensiveandpracticalcellularcensusoflung marking acrossdifferent lung atlases,we demonstrate the accuracy
cells.ThecurrentversionofLungMAPCellCardscatalogsmajorlung andstabilityofLungMAPCellRefsandtheirutilityforautomatedcell
celltypesandnumerousimmunecellsubtypes,spanningthecellular typeannotationofbothnormalanddiseasedlungs.Thepresentgui-
heterogeneity present in diverse regions of normal lung, including dedapproachisimplementedinRandisapplicableforCellRefcon-
trachea,bronchi,submucosalglands(SMG),andlungparenchyma10.
structionforotherorgans.
Thesecommoncelltypenomenclatureeffortsprovideascaffoldand
Results
| guideline |     | for the | ongoing | development | of  | a comprehensive | lung |     |     |     |     |     |     |     |
| --------- | --- | ------- | ------- | ----------- | --- | --------------- | ---- | --- | --- | --- | --- | --- | --- | --- |
single-cellreference for single-cellgenomicsanalysis.In addition to DatacollectionandguidedconstructionofaLungMAPsingle-
| curation,computationalmethodsarefurtherneededtoutilizecare- |     |     |     |     |     |     |     | cellreference |     |     |     |     |     |     |
| ----------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- |
fullycuratedliteratureknowledgeasguidelinestoaccuratelyidentify The LungMAP CellCards catalogued majorlung celltypes and their
celltypesusingintegratedsingle-celldatasets. associatedmarkergenesinmultipleregionsofnormallung,including
trachea,bronchi,SMG,andlungparenchyma10.ToconstructaLung-
|     | Here, | we present | a guided | approachfor |     | cellatlasconstruction |     |     |     |     |     |     |     |     |
| --- | ----- | ---------- | -------- | ----------- | --- | --------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
identification
that directs the of lung reference cell populations MAP humanlung CellRef in accordance with the CellCards,wecol-
accordingtoadictionaryofpre-compiledcelltypetermsandmole- lected 10 large-scale sc/snRNA-seq datasets (8 published and 2
cularmarkersderivedfromCellCards.Thepipelineconsistsoftwokey unpublished)fromthefourregionsofhumanlung(Fig.1A):Haber-
steps,firstidentifyingaseedpopulationforeachcelltypewhichbest mann et al.11 (n=10 donors; parenchyma), Reyfman et al.12 (n=8
representsthecellidentityinthedictionary,thenmappingallcellsto donors; parenchyma), Adams et al.13 (n=28 donors; parenchyma),
theseedsbasedontranscriptomicsimilaritytoconstructacomplete Deprezetal.14(n=9donors;trachea/bronchi/parenchyma),Travaglini
single-cell reference, termed CellRef. Using this approach, we con- et al.15 (n=3 donors; bronchi/parenchyma), Goldfarbmuren et al.16
structed and released a CellRef consisting of a total of 48 normal (n=15donors;trachea),Wangetal.(n=3,smallairway,neonatal/early
humanlungcelltypes,whichwenamedLungMAPHumanLungCell- pediatric samples excluded), Melms et al.3 (n=7, parenchyma),
Ref.Usingthesameapproach,weidentifiedseedcellsfor40mouse CCHMC LungMAP cohort (n=5, bronchus SMG, unpublished) and
lungcelltypesandconstructedtheLungMAPMouseLungDevelop- UPennLungMAPcohort(n=16,parenchyma,unpublished).Thiscol-
mentCellRef.Wedeployedthisresourceasmultipleuser-friendlyweb lectioncontainsdatafromsimilarnumbersoffemaleandmaledonors
interfacestofacilitateeasyaccessandmaximizeuseoftheLungMAP (n=48and55,respectively;1unannotated)(Fig.1A;Supplementary
|     | A                 | 10 single cell datasets, 104 donors |     |         |     |        |     |                  |     |                 |     |                       |     |     |
| --- | ----------------- | ----------------------------------- | --- | ------- | --- | ------ | --- | ---------------- | --- | --------------- | --- | --------------------- | --- | --- |
|     |                   |                                     |     |         |     |        |     | Sex              |     | Age             |     | Single cell library   |     |     |
|     |                   | Region                              |     | Samples |     | Cellls |     |                  |     |                 |     |                       |     |     |
|     |                   | Trachea                             |     | 24      |     | 55955  |     |                  |     |                 |     |                       |     |     |
|     | Submucosal glands |                                     |     | 5       |     | 11774  |     |                  |     |                 |     |                       |     |     |
|     |                   | Bronchi                             |     | 17      |     | 38639  |     |                  |     |                 |     |                       |     |     |
|     |                   |                                     |     |         |     |        |     | Female (48, 47%) |     | 10-19 (6, 6%)   |     | 10x 3’ v2 sc(95, 64%) |     |     |
|     |                   | Parenchyma                          |     | 102     |     | 398888 |     |                  |     | 20-29 (22, 21%) |     | 10x 3’ v3 sc(31, 21%) |     |     |
Male (55, 53%)
|     |     |       |     |     |     |        |     |     |     | 30-39 (21, 20%) |     | 10x 3’ v3 sn(10, 7%) |     |     |
| --- | --- | ----- | --- | --- | --- | ------ | --- | --- | --- | --------------- | --- | -------------------- | --- | --- |
|     |     | Total |     | 148 |     | 505256 |     |     |     | 40-49 (12, 12%) |     | 10x 5’ sc(12, 8%)    |     |     |
50-59 (15, 15%)
60-69 (19, 18%)
|     | B   |     |     |     |     |     |     |     |     | 70-80 (8, 8%) |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- |
Dictionary (LungMAP CellCards)
|     | sc/snRNA-seq |     |     |     |     | Cell type |     | Marker genes |     |     |     |     |     |     |
| --- | ------------ | --- | --- | --- | --- | --------- | --- | ------------ | --- | --- | --- | --- | --- | --- |
datasets
|     |     |     |                  |     |     | Alveolar type 1 cells (AT1)   |     | AGER, RTKN2, SEMA3B         |            |     |     |     |         |     |
| --- | --- | --- | ---------------- | --- | --- | ----------------------------- | --- | --------------------------- | ---------- | --- | --- | --- | ------- | --- |
|     |     |     |                  |     |     | Inflammatory monocytes (iMON) |     | CD14, FCN1, VCAN, no FCGR3A |            |     |     |     |         |     |
|     |     |     |                  |     |     | …                             |     | …                           |            |     |     |     |         |     |
|     |     |     | Data integration |     |     | Candidate clusters            |     |                             | Seed cells |     |     |     | CellRef |     |
Prediction1
|     |     |     |     |     | Single cell |     |     | Single cell |     |     |     | Consensus  |     |     |
| --- | --- | --- | --- | --- | ----------- | --- | --- | ----------- | --- | --- | --- | ---------- | --- | --- |
|     |     |     |     |     | ranking     |     |     | ranking     |     |     |     | Prediction |     |     |
Predi…ction 2
Unbiased
|     |     | …   |     |     | clustering |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Prediction n
Mapping to Seed cells
Fig.1|Datacollectionandtheguidedsingle-cellreference(CellRef)con- fortheLungMAPCellRefconstructionguidedbyusingLungMAPCellCardsasacell
| structionpipeline.ACharacteristicsofthecollectionofsinglecell/nucleus |     |     |     |     |     |     |     | typedictionary. |     |     |     |     |     |     |
| --------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | --- | --- | --- | --- | --- |
(sc/sn)RNA-seqdatasetsfromnormalhumanlungsamples.BSchematicworkflow
2
| NatureCommunications|(        2023)1  |     |     |     | 4:4566  |     |     |     |     |     |     |     |     |     |     |
| ------------------------------------- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Article https://doi.org/10.1038/s41467-023-40173-5
Data1).Themedianageofdonorswas41years(interquartilerange with the CellRef Seed to form the LungMAP Human Lung CellRef
[IQR],29−61years;1unannotated).Dataweregeneratedfromthree (347,970cells)(Fig.2B,SupplementaryFigs.1–3,“Methods”).
10xchromiumsinglecelllibraries:SingleCell3’sequencingkitbased The CellRef includes the following CellCards cells: 12 epithelial
onv2/v3andSingleCell5’chemistry.Intotal,505,256lungcellsfrom (AT1,AT2,basal,ciliated,goblet,myoepithelial[MEC],mucous,PNEC,
148 sc/snRNA-seq of normal human lung samples from 104 donors secretory, serous, Tuft cells, and ionocytes); 5 endothelial (arterial,
were used for LungMAP human lung CellRef construction (Supple- venous,lymphaticendothelial,capillary1,and2cells),8mesenchymal
mentaryData1). (alveolar fibroblast 1 and 2 [AF1, AF2], airway and vascular smooth
Theintegrationofsuchalargeandcomplexsingle-celldatacol- muscle cells [ASMC, VSMC], mesothelial cells, chondrocytes, peri-
lection is challenging due to the huge batch differences associated cytes,andmyofibroblasts[SCMF]),and16immunecelltypes(alveolar
with both biological (i.e., different donor and different anatomic and interstitial macrophage [AM, IM], inflammatory and patrolling
regions)andtechnicalvariations(e.g.,samplepreparationsbydiffer- monocytes [iMON, pMON], mast/basophils, neutrophils, B, plasma,
entprotocolsfromdifferentresearchinstitutions).Toperformaccu- NK,ILC,cDC1,cDC2,pDC,CD8+T,CD4+T,andTregulatory[Treg]
ratesingle-cellreferenceconstruction,wedevelopedacomputational cells).Inadditiontotheknownlungcelltypes,weextendedthedic-
pipelinewhichcombinesbatchcorrection,unsupervisedcellcluster- tionarytoincorporate7celltypesthatarenotyetintheCellCardsbut
ing, single-cell ranking, power analysis, and automated cell type have marker genes reported in recent scRNA-seq studies and are
annotationtoconsolidatesingle-celldatasetsandannotatecelliden- selectively expressed in our unbiasedly identified cell clusters,
tities guided by a pre-defined cell type dictionary (i.e., LungMAP including deuterosomal cells14 (DEUP1, FOXN4, CDC20B), suprabasal
CellCards)(Fig.1B).Weutilizedbothpositiveandnegativemarkersto cells14(SERPINB4,KRT19,NOTCH3),systemicvenousendothelialcells21
improvethesensitivitytodistinguishcelltypessharingsimilargene (SVEC;markergenes:COL15A1,ABCB1,ACKR1),maturedendriticcell
expressionpatternsandmarkergenes,forexample,lunggobletcells subset (maDC; marker genes: CCR7, CCL19, LAD1), megakaryocyte/
(MUC5AC+/MUC5B+) and SMG mucous (MUC5AC-/MUC5B+). The platelets15,22(ITGA2B,ITGB3),SMGductcells(MIA,ALDH1A3,RARRES1),
pipelineconsistsoffourmajorsteps(Fig.1B,“Methods”).First,wetried andrespiratoryairwaysecretorycells(RAS;markergenes:SCGB3A2,
themutualnearestneighbor(MNN)matchingmethodinMonocle3, KLK11,SOX4).WecombinedSMGbasalandSMGductcellsintoone
Seurat’s reciprocal principal component analysis (RPCA) based mixedtype,SMGBasal/Ductcell,sincetheirmarkergeneswereco-
integration5 and Harmony17 for batch correction. In addition, we expressedinthesamecellclusterinourdataintegration.Similarly,we
appliedarecentlydescribedclusterstabilityassessmentframeworkto combined mast and basophil cells into a mixed Mast/Basophil cell
quantitatively assess and compare the cluster stability of different type.Thesemixedcelltypeslikelyresultfromthelackofclearknown
integrationmethodsbasedonthreeindependentstatisticalmetricsto markersorinsufficientnumbersofcellsinthesubtypestodistinguish
quantitivelyassessthedataintegration18.MNNoutperformsRPCAand theheterogeneityoftheclusterinthecurrentCellRef.Weperformed
HarmonyonboththeUMAPinspectionandclusterstabilitymetrics uniform manifold approximation and projection for dimension
measurement,wethereforesetthemutualnearestneighbor(MNN) reduction(UMAP)analysisontheLungMAPHumanLungCellRef.All
matching method in Monocle 3 as default, and Seurat’s reciprocal cells,fromtracheatoalveoli,wereprojectedintoacommonUMAP
principalcomponentanalysis(RPCA)basedintegrationandHarmony space and showed clear separations by the predicted cell iden-
as alternatives (Supplementary Fig. 1). Next, seed identification was tities(Fig.2B).
performed(steps2and3inFig.1B).Thisisauniquefeatureofour ToevaluatecellidentitiesinthehumanlungCellRefSeed,we
approach.Weaimtoidentifyacoresetofcellsthatbestmatchtothe preformed the following validation analyses. Cell type marker
identity of each cell type in the CellCards dictionary. We perform geneswerefoundtobeselectivelyexpressedintheircorrespond-
unbiasedclusteringanalysisanddeterminecandidatecellclustersfor ingseedcells,themajorityhavinghighcelltypespecificexpression
eachcelltype based on the expression of marker genes inthe dic- frequencies, suggesting that the identities of the seed cells were
tionary.Theuseofunsupervisedclusteringinthisstepprovidesan consistentwiththecelltypedictionary(Fig.2C).Tofurthervalidate
opportunitytodiscovernewcelltypesthatarenotyetdefinedinthe the identities of the seed cells, we created pseudo-bulk gene
dictionary.Toidentifythebestseedcells,wedevelopedasingle-cell expressionprofilesforeachcelltypebyaveraginggeneexpression
rankingmethodthatfirstrankscellsbasedonexpressionofeachcell initsseedcells,measuredtheircorrelations,andperformedhier-
specificmarkergeneintheCellCardsdictionaryandthenaggregates archicalclusteringanalysis,demonstratingthatcelltypeswerefirst
therankingsofthosemarkersforagivencelltypetoidentifyseedcells unbiasedlyclusteredbytheirmajorcelllineagesandthenbysub-
for the cell type. We performed a power analysis to determine the lineages (Fig. 2D). The pseudo-bulk profile of SMG myoepithelial
minimumnumberofseedcellsrequired.Thelaststepisconsensus cells(MEC)co-clusteredwithmesenchymalcellsandwaspositively
label transfer. We applied multiplemachine learning methods (e.g., correlatedwithbothSMGBasal/Ductcellsandsmoothmusclecells,
Seurat’slabeltransferandSingleR)tomapallothercellstotheseed consistentwith theircomplex cellnature. UMAPanalysisshowed
cellsanddeterminetheircelltypesbasedontheseedannotation.Cells that the seed cells formed dense cell clusters and clearly dis-
thathaveconsistentcelltypepredictionsinallmethodswillbeinclu- tinguishedallcelltypesexceptcloselyrelatedTcellsubtypes(i.e.,
ded in the CellRef. The last step can be repeated to include newly TregandILCareclusteredwithCD8/4Tcells),supportingdistinct
collecteddatasetsintotheCellRefbymappingthemtotheseedcells. transcriptomicpatternsofcelltypesintheCellRefSeedandahigh
Weimplementedthiscell-type-dictionaryguidedCellRefconstruction similarityoftheseedcellsforeachcelltype(Fig.2A).Insummary,
pipeline in R and hosted its development and documentation in using our guided approach, we developed the LungMAP Human
github:https://github.com/xu-lab/CellRef19. LungCellRefSeed,acollectionofseedcellsfor48normallungcell
types which can serve as a simplified version of CellRef with cell
TheLungMAPHumanLungCellRef identitiesinaccordancewithacelltypedictionaryderivedfromthe
Usingthisguidedapproachandacelltypedictionaryderivedfrom LungMAPCellCards.
LungMAPCellCards(SupplementaryData2),weidentified8,080seed TovalidatethesimilarityofcellidentitiesintheCellRefSeed
cellsrepresenting48normalhumanlungcelltypes,termedLungMAP and the full CellRef, we created pseudo-bulk profiles for the cell
HumanLungCellRefSeed(Fig.2A).Next,wemappedallothercellsin typesintheCellRef,combinedthemwiththepseudo-bulkprofiles
ourcollectiontotheCellRefSeedcellsandpredictedcelltypeanno- generatedusingtheCellRefSeed,measuredcorrelationsamongall
tationsusingtwoindependentmethods,SeuratLabelTransfer5,20and pseudo-bulkprofiles,andperformedhierarchicalclusteringanaly-
SingleR6.Cellswithconsistentcelltypeannotationswerecombined sis.LiketheCellRefSeed,thepseudo-bulkprofilesofthecelltypes
NatureCommunications|( 2023)1 4:4566 3

Article https://doi.org/10.1038/s41467-023-40173-5
in the full CellRef were also first clustered by their major cell TheLungMAPMouseLungDevelopmentCellRef
lineagesandthenbysub-lineages.Moreover,eachofthemwaswell Usingthesameapproach,weconstructedacelltypedictionarybased
correlatedwiththepseudo-bulkprofileofthesamecelltypecre- ontheLungMAPCellCardstodefinecelltypesinmouselungduring
atedusingtheCellRefSeed(Fig.2D).Takentogether,theseresults perinataldevelopment,identifiedseedcellsforeachcelltype(termed
validated the identitiesofcelltypesin ourconstructed LungMAP LungMAPMouseLungDevelopmentCellRefSeed”),andconstructeda
HumanLungCellRef. CellRef for mouse lung development (denoted as LungMAP Mouse
NatureCommunications|( 2023)1 4:4566 4

Article https://doi.org/10.1038/s41467-023-40173-5
Fig.2|TheconstructionofLungMAPHumanLungCellRef.AUniformmanifold markergenesderivedfromLungMAPCellCards.DReconstructionofcelllineage
approximationandprojection(UMAP)visualizationofseedcellsrepresenting48 relationshipsusinghierarchicalclusteringanalysisofcelltypepseudo-bulkgene
lungcelltypesofnormalhumanlung,termedLungMAPHumanLungCellRefSeed. expressionprofiles.ColorrepresentsPearson’scorrelationvalueofpseudo-bulk
Cellswerecoloredbytheirpredictedseedidentities.BUMAPvisualizationofthe expressionprofiles.Labelsendingwith“.Seed”representpseudo-bulkprofiles
completesingle-cellreferencefornormalhumanlung,denotedasLungMAP createdbyaveraginggeneexpressioninthecellsofeachcelltypeinthehuman
HumanLungCellRef,whichcontains347,970cellsfrom104donorsanddefines48 lungCellRefSeed,whilelabelsendingwith“.CellRef”representpseudo-bulkpro-
celltypesinnormalhumanlung.Cellswerecoloredbytheirpredictedidentities. filescreatedusinggeneexpressionofeachcelltypeinthecompletehumanlung
CValidationoftheseedcellidentityusingtheexpressionofcelltypeselective CellRef.
Fig.3|TheconstructionofLungMAPMouseLungDevelopmentCellRef.AThe identitiesusingexpressionofcelltypeselectivemarkergenes.ELineagerelation-
developmentaltimepointsofmouselungsingle-celltranscriptomedatausedfor shipsamongmouselungcelltypeswerereconstructedusinghierarchicalcluster-
theguidedCellRefconstruction.BUniformmanifoldapproximationandprojec- inganalysisusingpseudo-bulkgeneexpressionprofiles.ColorrepresentsPearson’s
tion(UMAP)visualizationoftheseedcellsrepresenting40celltypesofthe correlationvalueofpseudo-bulkexpressionprofiles.Labelsendingwith“.Seed”
developingmouselung,termedLungMAPMouseLungDevelopmentCellRefSeed. representpseudo-bulkprofilescreatedbyaveraginggeneexpressioninthecellsof
Cellswerecoloredbypredictedseedidentities.CUMAPvisualizationofCellReffor eachcelltypeinthemouselungCellRefSeed,whilelabelsendingwith“.CellRef”
normalmouselungdevelopment,namedLungMAPMouseLungDevelopment representpseudo-bulkprofilescreatedusinggeneexpressionofeachcelltypein
CellRef.Cellswerecoloredbytheirpredictedidentities.DValidationofseedcell thecompletemouselungCellRef.
Lung Development CellRef) using Drop-seq of mouse lungs markergenes,UMAPvisualizationofcelltypes,pseudo-bulkexpres-
(n=95,658, 8 time points, 17 samples) from embryonic day 16.5 to sion and hierarchical clustering analysis-based cell lineage recon-
postnatalday28(Fig.3,SupplementaryFig.4,SupplementaryData3, struction,andcelltypespecificsignaturegeneidentification(Fig.3).
4).Becauseofthetimecoursedesign,themouselungCellRefincluded TheconstructionofthisLungMAPmouselungCellRefinparallelwith
moredevelopmentalprogenitorcellsandtransitionalcellstatesthan the human lung CellRef will enable cross comparisons for better
theLungMAPHumanLungCellRef,including,Sox9+/Id2+distalepi- understandingofhowthecelltypesinmouselungrelatetothehuman
thelial progenitor cell23,24, an AT1/AT2 cell population22,25 expressing lungandhowdatafrommousestudiesintheliteraturerelatetohuman
bothAT1(Ager,Hopx)andAT2(Lamp3,Sftpc,Abca3)cellmarkersin disease.ThemouseCellRefswillcontinuetobeexpandedwithadult
conjunctionwithCldn4,Krt19,andKrt8(signaturegenesofrecently timepointsandmurineinjuryinthefuture.
reportedPATS26,DATP27,orADI28cells),Foxf1+/Kit+endothelialpro-
genitorcells(EPC)29,andproliferativemesenchymalprogenitor(PMP) Interactiveweb-toolsforsearchanddisplayoftheLungMAP
cells30,31(Fig.3).Intotal,40mouselungcelltypeshavebeenidentified CellRefs
withtheguidanceofthemouselungcelltypedictionary(Fig.3,Sup- Tofacilitatedatasharingandbroaduseoftheresource,wedeveloped
plementaryData4).Cellidentitieswereverifiedusingexpressionof severaluser-friendlywebportalstohosttheLungMAPCellRefsonline,
NatureCommunications|( 2023)1 4:4566 5

A B Expression Distribution
Cell type specific gene expression patterns
Frequency Sensitivity
Fold change -log(value)
C
D
including the LGEA LungMAP CellRef page for human and mouse “Gene Expression Query”, “Cell Type Query”, and “Cell Signature
(https://research.cchmc.org/pbge/lunggens/CellRef/LungMapCellRef. Query”.The“GeneExpressionQuery”enablesuserstoinputanygene
html), scViewer-Lite, and ShinyCell for CellRef human (https://app. ofinteresttovisualizetheexpressionpatternsandassociatedstatistics
lungmap.net/app/shinycell-human-lung-cellref) and mouse lung inUMAP,Box,NotchedBox,Beeswarm,Scatterplot,andbi-directional
(https://app.lungmap.net/app/shinycell-mouse-lung-cellref). These barcharts(Fig.4A,B).The“CellTypeQuery”enablesuserstoselect
tools provide highly interactive search, analyzing, and visualization anyoneofthepre-definedcelltypesandobtaincell-typeinformation
functionalitiesforuserstoexploreandreanalyzecelltypeandgene collectedbyLGEAincludingcellselectivemarkergenes,transcription
expressionpatternsprovidedbytheLungMAPCellRefs(Fig.4,Sup- factors,andsurfacemarkers,ligandsandreceptors)aswellasalinkto
plementaryFig.6).TheLGEACellRefpageenablesuserstoperform theLungMAPCellCards29(Fig.4C).The“CellSignatureQuery”function
noisserpxe
dezilamroN
Article https://doi.org/10.1038/s41467-023-40173-5
Fig.4|OnlineinteractiveexplorationofLungMAPCellRefSeedusingLung typewasdeterminedusinganonparametricbinomialtest47forsingle-cellRNA-seq
GeneExpressionAnalysis(LGEA)webportal.TheLungMAPHumanLungCellRef databycomparingtheexpressionofFOXJ1inthecelltypewithitsexpressioninall
Seedwascomprisedof8080seedcellsrepresenting48normallungcelltypes. othercellsintheCellRefSeed.SeeFig.4sourcedatatablefornumberofcellsin
AThe“GeneExpressionQuery”interfaceallowsuserstoinputageneofinterest eachcelltype.CLGEAhostscomprehensivecellinformationrelatedwiththequery
(top)andvisualizeoftheexpressionofthequeriedgeneinUMAPembeddingsof celltype.D“CellSignatureQuery”functionretrievessignaturegeneexpression
cells(bottom),Colorsrepresenttheseedcellidentities(bottomleft)orthe statisticsofagivencelltypeandbar-plotvisualizationofsignaturegenesexpres-
expressionoftheinputgene(bottomright).BVisualizationofthegeneexpression sionacrossallcelltypesintheCellRefSeed.Pvaluesweredeterminedusinga
pattern(top:expressiondistribution;middle:expressionfrequencyandsensitivity; nonparametricbinomialtest47forsingle-cellRNA-seqdatabycomparinggene
bottom:foldchangeandp-valueofdifferentialexpression)acrossallcelltypesin expressionintheciliatedcells(n=200cells)withallothercells(n=7880cells)in
theCellRefSeed.Boxcenterlines,boundsofthebox,andwhiskersindicate theCellRefSeed.In(A)and(B),FOXJ1expressionwasshownasexample.In(C)and
medians,firstandthirdquartiles,andminimumandmaximumvalueswithin (D),Ciliatedcellswereusedasexample.
1.5×IQR(interquartilerange)oftheboxlimits,respectively.Pvalueforeachcell
NatureCommunications|( 2023)1 4:4566 6

Article https://doi.org/10.1038/s41467-023-40173-5
provides cell type selective signature genes identified using the dataset(10-foldcrossvalidationwithinCellRefsamples)orbasedon
LungMAP CellRefs, along with interactive tables and bargraph that priorknowledge(i.e.,knownmarkersandgeneontologyterms).First,
enablesuserstosearchdifferentialexpressionstatisticsandcompare weappliedthevalidationfunctionsinourpipeline(Fig.5A,“Methods”)
themeangeneexpressionacrossallcelltypes(Fig.4D).scViewer-liteis to evaluate the accuracy of cell type predictions based on prior
a R shiny based app that allows for comparative viewing of gene knowledge.AsshowninFig.5D–IandSupplementaryFig.7,predicted
expressionand/orothermetadataoverlappedondimensionreduc- celltypeswerewellseparatedandformedclusters.Cell-type-specific
tionplotsandviolinplots.Userscanalsoselectandhighlightcellsof markergenesfromCellCardswereselectivelyexpressedineachpre-
interest(SupplementaryFig.6).Inadditiontothesetwonewlydevel- dicted cell type, supporting the concordance of the cell identities
opedwebinterfaces,LungMAPCellRefscanbeinteractivelyexplored (Fig.5E,F,SupplementaryFig.7).Celltypespecificsignaturegenes
inLungMAPwebportalusingShinyCell32basedwebinterfaces(https:// were identified using widely accepted criteria (adjusted p value of
lungmap.net/cell-cards, “CellRef scRNA-seq” tab). CellRef-ShinyCell Wilcoxonrank-sumtest<0.1,expressionfrequency>=20%,andfold
allows cell-cell or gene-gene comparison and gene co-expression change>=1.5)(Fig.5G,H).Functionalenrichmentanalysisofcelltype
analysis,moreimportantly,weincorporatedageandsexvariablesinto signaturegeneswasusedtofurthervalidatethepredictedcelliden-
the CellRef-ShinyCell App, to enable users to depict the age/sex- tities.Forexample,predictedAT2cellswerefunctionallyenrichedin
dependentgeneexpressioninUMAPandcell-typedistributions. “surfactanthomeostasis”and“lipid/phospholipid/fattyacidmetabolic
processes”(Fig.5I,top).ToppCell(https://toppcell.cchmc.org/)ana-
AutomatedcelltypeannotationusingtheLungMAPCellRefs lysisshowedthatthepredictedsignaturegeneswereconsistentwith
WedevelopedLGEA,ShinyCell,andscViewer-lite-basedwebinterfaces genes selectively expressed in normal AT2 cells identified in inde-
foruserstoexploreandanalyzeexpressionpatternsofnormallung pendentsingle-cellstudiesofhumanlung35,36(Fig.5I,bottom).Next,
cellsandgenesofinterestwithouttheneedforcomputationalcoding. we evaluated the CellRef performance using external datasets
Another powerful use of the LungMAP CellRefs is to use them for GSM5388411/12/1333. After mapping and comparison of the CellRef
automatedcelltypeannotationofusers’ownsingle-celldatasetsto prediction to the original published cell type annotations, we mea-
facilitate analysis and standardization of cell type prediction and suredtheCellRefperformancebasedonmultiplemetrics,including
annotations. To achieve this goal, we built our CellRef Seeds and precision,recall,accuracy,F1score,andMatthewscorrelationcoeffi-
CellRefsintoRobjectsinaccordancewithSeuratreferencemapping cient(MCC)(“Methods”).Themedianvaluesofallmetricsaregreater
pipeline5, 20. Azimuth (https://satijalab.org/azimuth) instances were than0.92(SupplementaryFig.8),supportingthehighconsistencyof
establishedatLungMAP.net(https://lungmap.net/cell-cards,“CellRef the automated CellRef cell type prediction with the original cell
Azimuth”tab)toenableuserstouploadtheirowndatasetsforonline annotations.Last,weperformeda10-foldcrossvalidationofcelltype
automated cell type annotation using our CellRefs (Fig. 5A) and identification within both human and mouse LungMAP CellRefs
explorationofanygenefeaturesontheprojectedUMAPorinViolin (“Methods”).Briefly,werandomlypartitionedthedataintheCellRef
plots. Additionally, to facilitate evaluation of automated cell type into10similarparts,used9partsastrainingdatatopredictcelltypes
annotation results, we developed functions in our R pipeline to intheremainingpartandmeasuredtheperformanceofthepredic-
visualize the expression of CellRef markers across all predicted cell tionsbasedonF1scoreandMatthewscorrelationcoefficient(MCC)
types,identifycelltypesignaturegenesandtheirassociatedfunctional whichquantifiedtheconsistenciesofthepredictedidentitieswiththe
annotations,andcompileallvisualizationandevaluationresultsintoa CellRefidentitiesofthetestpart.Werepeatedthetrainingandtesting
singleevaluationreportusingRmarkdown(Fig.5A). 10timesandusedadifferentpartasthetestingdataeachtime.Both
the LungMAP human and mouse lung CellRefs achieved high cross
UsecasesdrivenevaluationofLungMAPsingle-cellreferences validationperformancewith~0.92medianF1andMCCscoresforthe
forautomatedcelltypeannotation humanlungCellRefand0.98medianF1andMCCscoresforthemouse
AnnotationofscRNA-seqofnormalhumanlung.Wecollectedpub- lungCellRef,respectively(SupplementaryFig.9).
lished scRNA-seq datasets of normal human lung samples to inde- Insummary,evaluationsbasedonpriorknowledgeorusinginter-
pendentlyevaluatetheaccuracyoftheautomatedcelltypeannotation dataset and intra-dataset demonstrate the high performance and
usingtheLungMAPCellRefs.Thedatasetswerefromnormalhuman accuracy of human and mouse lung CellRef cell type annotations,
lungsamplesof2monthsto45yearsofageandweregeneratedusing support the general applicability of automated CellRef cell type
10Xchromium3’(GSM5388411/12/1333andGSM4504966/6734;aligned annotationfornewdatafromscRNA-seqoflung.
to hg38 reference genome) and 5’ (GSM40354721; aligned to hg19 Amongthetestingdatasets,GSM4035472showedrelativelylower
referencegenome)platforms. consistencyscorethanothers(Fig.5C).Thisisaspecialdatasetintwo
Foreachtestdata,weusedboththehumanlungCellRefSeedand ways.Itwasgeneratedusing10XSingleCell5’assaywhileothertesting
CellRef to predict cell type annotations using Azimuth’s reference sampleswereusing10XSingleCell3’assays.Thisdatasetwasaligned
mappingalgorithm5,20.Morespecifically,weusedtheSeuratv4Find- using hg19 while others used hg38. We included this dataset for a
TransferAnchors and MapQuery functions. During the reference proof-of-concept that CellRef can map cell types for datasets from
mapping,apredictionscore(between0and1)wascalculatedforeach differentprotocolandreferenceversions.Thedifferenceislikelydue
cell, reflecting the confidence associated with the predicted cell tothecombinationofdifferentlibraryandreferencegenomeversions.
annotation.Bydefault,weusedthemeanvalueminusonestandard Nevertheless,morethan75%cellsfromthisdatasetcanbeconsistently
deviation as the cutoff for the prediction score; cells within the mapped using the CellRef and CellRef Seed when using the default
threshold are considered to be confidently mapped to the CellRef cutoff(Fig.5C).
annotations.Usingthiscutoff,80.28%cellsinthetestdatasetcanbe ApplicationtoscRNA-seqofhumanlungdiseases.Wepreviously
confidentlyannotated using the CellRefin comparison with 80.84% performed single-cell transcriptomic analyses of lung samples from
usingtheCellRefSeed,suggestingthatsimilarnumbersofcellscanbe patients with lymphangioleiomyomatosis1 and identified a unique
confidently predicted using both the complete human lung CellRef population of cells termed LAMCORE that were readily distinguished
andtheCellRefSeed(Fig.5B,C).PredictionsusingtheCellRefSeed from endogenous lung cell types and shared closest transcriptomic
werecomputationallyefficient,taking~1mintoannotatea10xchro- similaritytouterinemyocytesinbothnormalandLAMuteri1.Inthe
miumscRNA-seqof4000–8000cells. presentwork,were-alignedthisdatasettothehg38referencegenome
We evaluated CellRef performance via multiple independent and performed automated cell type annotationusing the LungMAP
approaches including using inter-dataset (external data) and intra- HumanLungCellRefSeed.Atotalof31celltypeswerepredictedfrom
NatureCommunications|( 2023)1 4:4566 7

Article https://doi.org/10.1038/s41467-023-40173-5
thetwoLAMlungs(Fig.6A–C)incomparisonwith18celltypespre- highly enriched in IPF lungs11 (Fig. 6G, left panel). Using this data,
dictedfromtheoriginalpublication1.Celltypepredictionswerelargely CellRef predicted 37 cell types and identified more endothelial and
consistentwiththeoriginalclustering-basedannotations1,butmore rareepithelialcellsubtypes(e.g.,PNECandionocytes)(Fig.6E).Most
cellsubtypesnotreportedintheoriginalstudycanbedistinguished importantly,themedianpredictionscoreofKRT5-/KRT17+cellswas
usingCellRef.Importantly,thepreviouslyidentifiedLAMCOREcells(73 thelowestamongallcells(Fig.6F,G,rightpanel);significantlylower
cells)hadthelowestaveragepredictionscorebelowthecutoffline thanourdefaultcutoffthreshold,suggestingthatthiscellpopulation
(Fig.6D),supportingthenotionthatthisLAMCOREcellpopulationwas cannotbeconfidentlymappedtoanyofthenormallungcelltypesin
notsimilartonormallungcelltypesinthepresentLungMAPCellRef. CellRefandlikelyrepresentsanatypicalorpathogeniccellpopulation.
Inthesecondusecase,weusedanidiopathicpulmonaryfibrosis Insummary,theseusecasesprovideproof-of-principleexamplesthat
(IPF)lungscRNA-seqdataset(GSE135893,10XSingleCell5’,19sam- CellRefcanbeusedtoassistanalysisoflungdiseasedataandidentify
ples,12IPFlungs)(Fig.6E–G).Habermannetal.reportedtheidentifi- potentialdisease-relatedcellclusters.Furthermorphologicalanalyses
cation of 31 cell types including a previously unrecognized KRT5-/ andfunctionalvalidationsarethenneededtoidentifyandcharacterize
KRT17+pathologic,ECM-producingepithelialcellpopulationthatwas anyabnormalcelltypesoratypicalcellstates.
NatureCommunications|( 2023)1 4:4566 8

Article https://doi.org/10.1038/s41467-023-40173-5
Fig.5|CelltypeannotationandevaluationusingtheLungMAPHumanLung suprabasalcellswerecombinedinprediction.DUMAPvisualizationofcellswith
CellRef.ASchematicworkflowoftheautomatedcelltypeannotationandeva- predictionscores≥defaultcut-off(mean-1standarddeviation)andpredicted
luationpipeline.BDistributionsofcelltypepredictionscoresineachtestdata. annotationswithatleast5cells.Cellswerecoloredbyautomatedcelltypeanno-
PredictionscoresusingCellRefSeed(yellowbars)arecomparabletothoseusing tationsusingtheCellRefSeedasreference.Datafromdifferentdonorswereinte-
thecompleteCellRef(bluebars).Predictionscores(between0and1)werecalcu- gratedusingSeurat’sreciprocalprincipalcomponentsanalysis(RPCA)pipeline.
latedbytheSeuratv4MapQueryfunctionforeachcell.Boxcenterlines,boundsof EEvaluationofcelltypeannotationsusingCellRefcelltypemarkersfromSup-
thebox,andwhiskersindicatemedians,firstandthirdquartiles,andminimumand plementaryData2.FPercentagesofcelltypemarkers(SupplementaryData2)that
maximumvalueswithin1.5×IQR(interquartilerange)oftheboxlimits,respectively. aredifferentiallyexpressedintheircorrespondingcelltypepredictions(n=34cell
GSM5388411:6228cells,GSM5388412:8329cells,GSM5388413:7143cells, types)in(D).Dataareshownusingviolinplotwithdotanderrorbarsrepresenting
GSM4504966:8381cells,GSM4504967:8043cells,GSM4035472:5767cells. mean±SEM.GHeatmapvisualizationofexpressionofcelltypespecificdifferen-
CConsistencyofcelltypepredictionsusingtheCellRefSeedandCellRefineach tiallyexpressedgenes(DEGs).HThenumberofDEGsforeachpredictedcelltype.
testdata.Consistencypercentages(yaxis)werecalculatedforcellsineachtest ISignificantlyenrichedfunctionalannotationsusingDEGsofthepredictedAT2
dataset(color)passingdifferentthresholdsofpredictionscores(xaxis). cells:mostenrichedGeneOntologyBiologicalProcesses(top)andToppCellGene
D–HEvaluationofautomatedcelltypeannotationsforthreeofourtestdata Sets(bottom).FunctionalenrichmentanalysiswasperformedusingToppGene
(GSM5388411/12/13,threescRNA-seqofnormalhumanlungs).Evaluationofthe (https://toppgene.cchmc.org/enrichment.jsp).Theminimumfalsediscoveryrate
otherthreetestdatasampleswereshowninSupplementaryFig.7.Basaland (FDR)wassetto1e−300.PleaseseeFig.2fordefinitionsofcelltypeabbreviations.
Benchmarkanalysisofcelltypeaccuracyandstabilityofthe (Fig.7C).UsingtheCellRefmarkers,CellRefout-performedHLCAin
LungMAPHumanLungCellRef thiscase(Pvalue=8.345E−07)(Fig.7C).
In addition to CellRef, prior healthy lung cell atlases have been Next, we assessed and compared performance of CellRef and
reported, including Travaglini et al.15 which included data from 3 HLCAusingthedatafromfirstversionofhumanlungatlas15asthetest
humanlungs,andtherecentlyreleasedintegratedversionofHuman data.AfterthemappingusingtheCellRefSeedandHLCA,wefound
LungCellAtlas(HLCA)37,38.TheHLCAcorereferencewasused,which that43outof48(89.6%)CellRefand48outof58(82.8%)HLCAcell
defined58lungcelltypes/statesbasedonanintegrationofsingle-cell typeswerepredictedandmostofthepredictionshadaone-to-one
RNA-seqdatafrom167healthysamplesfrom107individualsfrom14 mapping (38 out of 43 CellRef clusters) (Fig. 8A–D).Disagreements
datasets37. include CellRef interstitial macrophages (IM) which was subdivided
Toassessandbenchmarktheaccuracyofcelltypeidentification intoHLCAmonocyteandDCsubsetsandCellRefsuprabasalcellswas
and marker genes prediction, we compared LungMAP human lung subdividedintoHLCABasalrestingandsuprabasalcells.Viceversa,
CellRefwithHLCAusingmultipleindependentapproaches.First,we HLCA myofibroblasts was subdivided into SCMF and ASMC in Cell-
accessedtheoverallsimilarity/distinctionofthetwoatlasesbasedon Ref prediction; HLCA CD8 T cells weresubdivided into CD8 T, NK,
correlationanalysisofpseudo-bulkexpressionofhighlyvariablegenes Tregs,andILCinCellRefprediction;plateletsandTuftcellswereonly
(see “Methods” for details). Although the cell type names are not predictedbyCellRefwhilesomealveolarmacrophagesubtypessuch
identical,thecorrelationsofcelltypepseudo-bulkprofilesbetween asmonocyte-derivedmacrophages,alveolarmacrophageproliferating
HLCAandCellRefwerehighlyconsistentamongthefourmajorlung wereonlypredictedbyHLCA.Hence,allthreeversionsofLungAtlas
celllineages(Fig.7A).Withineachlineage,mostCellRefandHLCAcells arehighlyconsistent,withthedifferentatlasesprovidingpotentially
have a one-to-one mapping (Fig. 7A). In addition, each reference diverse resolution levels resulting in some discrete lung cell
identifiedseveraluniquelungcelltypesorstates(i.e.,celltypesdonot populations.
cluster together between the two references). Among these, the To quantitatively assess the validity of the cell population pre-
chondrocytes, myoepithelial (MEC), ILC, Treg, and neutrophil cells dictionsbetweenCellRefandHLCA,weappliedthreedistinctcluster
were unique in our CellRef, while subpleural fibroblast, AT2 pro- stability measurements in the recently published single-cellintegra-
liferating,andTcellproliferatingwereuniqueinHLCA.Wesummar- tion framework scTriangulate18.Inbrief,scTriangulateaimsto com-
izedtheone-to-onemappedcelltypesandtheuniquecelltypes/states parethebiologicalstabilityofconflictingclustersamongstmultiple
intheSupplementaryFig.10.Insummary,theconsensusacrossthe annotations,suchthateachsingle cell can be assigned tothemost
twolungatlasesisveryhigh,providingfurtherassuranceofaccuracy. stableannotation.Thestabilitymetricsincludereclassificationstatis-
Byidentificationofcommonanduniquecellidentitiesacrossthetwo tics(SCCAF)39,centroid-basedreassignment(Reassign)18,andmarker
atlases,oureffortsrepresentaninitialstandardizationsteptobegin genespecificity(Termfrequency-InverseDocumentfrequencyorTF-
mappingacomplexcellgroupwithmultiplenamesacrossdifferent IDF)18.SCCAFandReassignmetricsmeasurewhethertheatlasleadsto
lungatlases. definitivecellpopulationpredictionsandwithhighconfidence(i.e.,
Next,weassessedandcomparedtheaccuracyofcelltypeiden- cellscanbereproduciblyre-classifiedtotheseclusters).AhigherTFIDF
tificationandcellselectivemarkerpredictionviareceiveroperating scoresuggeststherearemoreunique/informativemarkersassociated
characteristic(ROC)curveanalysisofcelltypeselectivemarkergenes withthedefinedcluster.ApplyingthesestabilitymetricstoCellRefand
rankingexpressioninthepredictedcells,amethodwedevelopedand HLCA on the test data from Travaglini et al., we observed that, on
incorporated into SINCERA pipeline30 (“Methods”). Using this average,CellRefproducedslightlyhigherSCCAFandReassignscores
approach,weperformedthesingle-cellrankingbasedontheexpres- as compared to HLCA; while HLCA produced slightly higher TF-IDF
sionofthemarkergenesofeachcelltypeandcomparedtherankings scorethanCellRef (Fig. 8E). Similarly, when applying these stability
againstthecelltypeannotationsinreferencetoobtainanareaunder metricstoCellRefandHLCAusingtheirowndatacollections,CellRef
ROCcurve(AUC)foreachcelltype.AhigherAUCrepresentsahigher produced slightly higher scores on SCCAF and TF-IDF; as well as a
accuracyofcelltypeidentificationinareference.Toensurethefair significantly higher score on cell re-assignment (p=0.011) as com-
comparison,wefirstcalculatedtheAUCsformappedcelltypepairs pared to HLCA (Supplementary Fig. 11). scTriangulate leverages the
betweenthetworeferencesusingthecelltypemarkergenesidentified computedstabilityscorestofurtherassessthemarginalimportanceof
byHLCA.AsshowninFig.7B,theaverageAUCof97.7%isachievedfor eachannotation(CellRefandHLCA)usingacooperativegametheory
CellRef, slightly higher than97.2% for HLCA but with no significant framework.scTriangulatepredictedthat50%(n=24/48)oftheCellRef
difference (P value=0.262). Next, we performed the same analysis celltypestobeofhigherconfidence(AEC,AF1,AF2,AM,ASMC,CD8T,
usingthecelltypemarkergenesidentifiedbyCellRef(Supplementary cDC1, cDC2, Ciliated, Goblet, Ionocyte, LEC, Platelet, pMON, Supra-
Data 5). The results were consistent (CellRef: 98.8%; HLCA: 96.1%) basal, SVEC, VSMC), compared to 46% (n=27/58) of the HCLA cell
NatureCommunications|( 2023)1 4:4566 9

Article https://doi.org/10.1038/s41467-023-40173-5
types(AT2,aCAP,Pericyte,Mesothelium,Peribronchialfibroblastsand numberofdatabatchesintheneighborhoodofeachcell,and(ii)cLISI
Adventitial fibroblasts, etc.) (Fig. 8D). Hence, both atlases provide thatmeasuresthenumberofcelltypesintheneighborhoodofeach
uniqueandinformativepredictions,eachwithdistinctbenefits. cell.BasedontheassumptionofLISI,iLISIscoresareclosetothebatch
Next,wecompareddataintegrationinthehumanlungCellRef numbersforawellmixingofbalanceddatabatches,meanwhilethe
andHLCAusingLocalInverseSimpson’sIndex(LISI)17,whichcalculates idealcLISIscoreiscloseto1forawellseparationofcelltypesinthe
twometricsforeachcellintheintegration:(i)iLISIthatmeasuresthe integration.SincethetotalnumberofbatchesinCellRefandHLCAare
NatureCommunications|( 2023)1 4:4566 10

Article https://doi.org/10.1038/s41467-023-40173-5
Fig.6|ApplicationofLungMAPHumanLungCellReftodiseaselungs.AUMAP applicationofCellReftoapublishedscRNA-seqofhumanlungswithidiopathic
visualizationofapublishedscRNA-seqofhumanlungswithLAM1.Cellcolors pulmonaryfibrosis(IPF)11.EUMAPvisualizationofcellspredictedusingtheCellRef
representcellidentitiespredictedinGuoetal.,2020,includingauniquedisease- Seed.Basalandsuprabasalwerecombined,Tcellsubsets,andmonocytesubsets
relatedcellpopulation,namedLAMCOREcells(magentacellcluster).BUMAP werecombinedintheprediction.FUMAPvisualizationofcellscoloredbythe
visualizationsofcellspredictedusingtheCellRefSeedasreference.Basaland predictionscores.GLeft:UMAPvisualizationofcellscoloredbytheoriginalcell
suprabasalcellswerecombinedintheprediction.Predictionscores(between0and identities(n=31celltypes;abbreviationsweredefinedinHabermannetal.11).Right:
1)werecalculatedbytheSeuratv4MapQueryfunctionforeachcell.Cellswith boxplotvisualizationofthedistributionofpredictionscoresineachoftheoriginal
predictionscore>=thedefaultcutoff(i.e.,themeanminus1standarddeviation cellidentities.Theblackandredhorizontallinerepresentsthemeanand(1stan-
value)wereshown.Threesingletoncelltypepredictionswerenotincluded. darddeviationlowerthanthemean)valueofthepredictionscores,respectively.
CEvaluationofcelltypepredictionsusingexpressionofrepresentativeCellRef Thedisease-associatedKRT5-/KRT17+cellshadpredictionscoresbelowthecutoff
markergenes.Megaka./Platelet:Megakaryocyte/Platelet.DDistributionsofthecell line.Thenumberofdatapointsineachboxplotin(B)and(G)canbefoundinFig.6
typepredictionscoresineachoftheoriginalcellidentities(n=18celltypes; sourcedatatable.In(D)and(G),Boxcenterlines,boundsofthebox,andwhiskers
abbreviationsweredefinedinGuoetal.1).Theblackandredhorizontalline indicatemedians,firstandthirdquartiles,andminimumandmaximumvalues
representsthemeanand(1standarddeviationlowerthanthemean)valueofthe within1.5×IQR(interquartilerange)oftheboxlimits,respectively.PleaseseeFig.2
predictionscores,respectively.E–GUMAPandboxplotvisualizationsof fordefinitionsofCellRefcelltypeabbreviations.
different,foreachreference,wecalculatedtheiLISIscoresforcells includedintheCellCardsbutreportedinrecentscRNA-seqanalyses,
withineachcelltypeandnormalizedthescoresbythetotalnumberof including deuterosomal cells14, suprabasal cells14, systemic venous
batchesineachcelltype.TheoveralldistributionsofiLISIscoresin endothelial cells21, mature dendritic cell subset, SMG duct cells,
bothCellRefandHLCAarenotideal,onaverageabout15%forCellRef, respiratory airway secretory cells (RAS, a recently identified multi-
and5%forHLCA,respectively(SupplementaryFig.11),likelydueto potent secretory cell population in respiratory bronchioles), and
thatbothatlaseswereconstructedusinglargecollectionsofhetero- megakaryocyte/platelets15,22.DuringtheCellRefconstruction,wedis-
geneousdatafromdifferentbiologicalregionsandconditionsrather coveredcellclustersselectivelyexpressingmarkergenesofthesenew
thanawell-designedbalancedcohort.WespeculatewhetherLISIisa celltypes,andthuswehaveincludedthesecelltypesintotheLung-
suitableapproachtoevaluatelarge-scaleheterogenoussingle-celldata MAPHumanLungCellRef.Wewillcontinuetoincorporatemorecell
integration.Nevertheless,CellRefconsistentlyoutperformsHLCAon typesinaccordancewithnewfindingsfromsinglecelland/orfunc-
themeasurementsofiLISI,andhasthecLISIscorescloseto1,indi- tionalstudies.
cating a well separation of the CellRef cell types (Supplemen- To our best knowledge, two earlier versions of human lung
taryFig.11). references15,37havebeenpublishedorareinpreprint.Wecompared
Last, we evaluated the LungMAP mouse lung CellRef using the andincorporatedthefirstlungreferenceintoourCellRefconstruction.
threestabilitymetricscalculatedbyscTriangulate18andthemarker- Further,wecarefullycomparedallannotatedcelltypesintherecently
basedAUCanalysis30(“Methods”andSupplementaryData6).Results released integrated version of Human Lung Cell Atlas (HLCA) with
supportedthehighaccuracy,clusterstability,andmarkerspecificityof LungMAPCellRefbasedonthehighlyvariablegenesfromHLCAand
ourmouselungreferencecelltypes(SupplementaryFig.12;meanAUC CellRef.Althoughnotallcelltypenamesareidentical,themajorityof
95.8, mean SCCAF score: 0.970, mean Reassign score: 0.881, mean theHLCAannotatedcellsalignwellwithaclearlydefinedcelltypein
TFID10score:0.892). LungMAP CellRef. Furthermore, each reference identified several
uniquelungcelltypesorstates(i.e.,cellsthatdon’taligntoanygiven
Discussion cellclusterintheotherreference).Inaddition,weperformedaseries
In the present study, we developed a computational approach to of benchmark studies to compare the two integrative lung atlases
integrate large scale and heterogeneous sc/snRNA-seq datasets and including ROC-based analyses to cross-validating the accuracies of
constructedcomprehensivelungsingle-cellreferences,termedLung- sharedcelltypeidentifiesinbothreferencesandusedscTriangulate18,
MAP HumanLung CellRef and LungMAP Mouse Lung Development arecentlydescribedclusterstabilityassessmentframeworktoquan-
CellRef,inaccordancewithawell-definedcelltypedictionaryderived titativelyassessandcomparetheclusterstabilityofthetwoatlases
from LungMAP CellCards10. Evaluation functions were developed in baseduponthreeindependentstatisticalmetrics.Wefoundthatcell
our pipeline to perform fast and comprehensive evaluation of the typepredictionsusingCellRefandHLCAwerehighlyconsistent,with
predicted cell type annotations. User-friendly web interfaces were discrete and stable populations in both atlases. Each reference had
developed to facilitate access, visualization, and utilization of the approximatelyanequalpercentageofcelltypepredictionsthatwere
LungMAP CellRefs. For advanced users who are interested in anno- more confident in one than the other. Hence, both atlases provide
tatingtheirowndatasetsusingtheLungMAPCellRefs,weestablished uniqueandinformativepredictions,withbenefitstoeachatlas.Gen-
Azimuthinstancestosupportonlineautomatedcelltypeannotations eratingaconsensusblueprintofnormalhumanlungwithunifiedcell
ofusers’ownscRNA-seqorindependentlyproducedcompendiums. ontologyandnomenclatureisfundamentallyimportantandchallen-
Regarding the choice of the classification algorithm (Azimuth), this ging,requiringcrossconsortiaeffortsandopendiscussionsamongthe
algorithm leverages Seurat’s label transfer method, which performs pulmonaryresearchcommunityatlarge.Oureffortshereinrepresent
wellinpriordiversebenchmarkingevaluationstudies40andhasbeen thebeginningofinitiativestobuildaconsensusatlasbymappinga
broadlyused.Importantly,itiscurrentlythefastestandmostacces- complexcellgroupwithmultiplenamesacrossdifferentlungatlases.
sibleapproachforreference-basedlabeltransfer,datapre-processing Furthercross-teamdiscussionsandcomparisonsareneededtoreach
andexploration,andiscompatiblewithdatasetscontaininghundreds the ultimate goal of a unified nomenclature and standardized data
ofthousandsofcellsprocessinginjustafewminutes.LungMAPplans processing that are needed to create an enduring resource for the
toupdatethespecificversionofAzimuthasitisupdatedinthefuture. researchcommunity.
TheLungMAPHumanLung CellRefcontains a total of347,970 ThepresentLungMAPCellRefshasseveraluniquefeatures:(1)We
cellsand48well-definedlungcelltypes,coveringmajorcellularhet- developedacomputationalpipelineandaguidedapproachtocon-
erogeneityinthefourregions:trachea,bronchi,SMG,andlungpar- struct and evaluate the reference which can be reused for future
enchyma. The CellRef identified cell types mapped to the cell type updates of LungMAP CellRef or references of otherorgans; (2) The
nomenclature in the LungMAP CellCards10. In addition, based on LungMAPCellRefidentifiescelltypesinaccordancewiththeLungMAP
unbiasedclusteringanalysis,weidentifiedcelltypesthatarenotyet CellCards10,arigorouscatalogoflungcellsvalidatedbybothsinglecell
NatureCommunications|( 2023)1 4:4566 11

Article https://doi.org/10.1038/s41467-023-40173-5
andfunctionalstudies.TheCellCards10curationeffort,isnowapan- DuringCellRefconstruction,weidentifiedthebestseedpopulations
consortium effort which includes multiple laboratories outside of foreachcelltype(CellRefSeeds),whichwasnotonlyusedtoconstruct
LungMAPtodefinestandardizedcellpopulations,labels,markers,and thecompleteCellRefbutcanbeindependentlyusedforautomated
functionaldescriptions,leveragedbyCellRef.Thus,weconsiderCell- celltypeannotationandonlinevisualizationwithimprovedcompu-
Ref a more knowledge driven as opposed to solely cluster driven, tational efficiency and hardware requirements; (4) We constructed
which in our view represents a sustainable and reliable model; (3) LungMAPCellRefforbothhumanandmouse,thetwomostcommonly
NatureCommunications|( 2023)1 4:4566 12

Article https://doi.org/10.1038/s41467-023-40173-5
Fig.7|AssessmentofcelltypepredictionaccuracyoftheLungMAPHuman valuesusingviolinplots.Middle:AUCvaluesforeachofthemappedcelltypes.
LungCellRef.AHeatmapvisualizationofPearson’scorrelationsofcelltypes Right:usingCellRefAF2(HLCAadventitialfibroblasts)asanexampletoshowthe
betweenthehumanlungCellRefandtheHumanLungCellAtlas(HLCA)37.A ROCcurveslabeledwithAUCvaluesand90%confidenceinterval.CAUCsvaluesfor
pseudo-bulkprofilewascreatedforeachcelltypeofeitherCellReforHLCAby eachofthemappedcelltypes(n=42)intheCellRef(orange)andHLCA(blue)
averagingeachgene’sexpressioninthecellsofthecelltype.Celltypeswere calculatedusingthecelltypeselectivemarkergenesidentifiedbyCellRef(Sup-
clusteredintofourmodules,eachcorrespondingtooneofthefourmajorcell- plementaryData5).Left:summaryoftheAUCvaluesusingviolinplots.Middle:
lineages.CorrespondencesofCellRefandHLCAcelltypeswithineachofthefour AUCvaluesforeachofthemappedcelltypes.Right:usingCellRefAF2(HLCA
moduleswereshownbasedonthehierarchicalclusteringanalysis.B,CAssessment adventitialfibroblasts)asanexampletoshowtheROCcurveslabeledwithAUC
ofcelltypeaccuracybasedonmarkergeneexpression.BAreaunderthereceiver valuesand90%confidenceinterval.Inboth(B)and(C),theblackdotanderrorbars
operatingcharacteristic(ROC)curve(AUC)valuesforeachofthemappedcell representmean±SEM.pvaluerepresentssignificanceofdifferenceassessedusing
types(n=42)inCellRef(orange)andHLCA(blue)calculatedusingthecelltype two-tailedpairedWelch’sttest.CellRefcelltypeabbreviationsaredescribed
selectivemarkergenesidentifiedfromtheHLCAstudy.Left:summaryoftheAUC inFig.2.
Fig.8|AssessmentofcelltypestabilityofautomatedannotationusingCellRef. calculatedusingscTriangulate,includingreclassificationaccuracy(SCCAFand
A,BUMAPprojectionofscRNA-seq(Travaglinietal.15,n=3humanlungs)with reassign)ormarkergenespecificity(TF-IDFscore),forallAzimuthassignedCellRef
AzimuthprojectedcelltypeannotationsusingtheLungMAPHumanLungCellRef orHLCAcellpopulations(n=42cellpopulationspredictedusingtheCellRefSeed;
Seed(A)orusingtheHumanLungCellAtlas(HLCA)37(B)asthereference. n=48cellpopulationspredictedusingHLCA)inTravaglinietal.2020.Theblack
CCorrespondingcell-populationassignmentsofCellRefandHLCA(mapping dotsanderrorbarsrepresentmean±SEM.pvaluerepresentssignificanceofdif-
percentagerelativetoCellRef).DCellscoloredby“winning”annotationsfrom ferenceassessedusingtwo-tailedunpairedWelch’sttest.PleaseseeFig.2for
CellReforHLCAdeterminedbyscTriangulatebasedonstabilityassessments definitionsofCellRefcelltypeabbreviations.
(showninE)annotations.EViolinplotvisualizationofstabilitymetricscores
NatureCommunications|( 2023)1 4:4566 13

Article https://doi.org/10.1038/s41467-023-40173-5
usedspecies,andprovideoptionsforuserstouseeitherscRNA-seqor HospitalMedicalCenterInstitutionalAnimalCareandUseCommittee
snRNA-seqbasedCellRefseparatelybasedupontheinputsequence inaccordancewithNIHguidelines.
typetoachievebetterperformanceoncelltypeannotation;(5)Web
portalsweredeveloped byour LungMAP research centersand data Collectionandpre-processingofsinglecell/singlenucleus
coordinationcentertofacilitateresourcesharingandmaximizeuseof RNA-seqofhumanlung
theconstructedreferencesbytheresearchcommunity. We collected eight published and two unpublished sc/snRNA-seq
Whiletheseeffortsillustratethepowerofreference-guidedclas- datasetsofhumanlungforLungMAPhumanlungsingle-cellreference
sification from a comprehensive reference, we note there are still construction.Forthepublisheddatasets,uniquemolecularidentifier
several areas for improvement in both CellRef and independent (UMI)countmatrixofgeneexpressioninsinglecellsweredownloaded
initiatives.First,thecurrentiterationofCellRefsdoesnotyetclearly fromGeneExpressionOmnibus(GEO),EuropeanGenome-phenome
definethespectrumofpossibleimmunesub-populationsandtransi- Archive(EGA),orSynapse.orgusingthefollowingaccessionnumbers:
tional cell states. Such populations are likely to vary with age and GSE12296012, GSE13589311, GSE13417416, GSE1368322, GSE16138213,
disease.Antibody-basedapproaches,e.g.,CITE-seqorflowcytometry, EGAS0000100408214, GSE1715243, syn2104185015. For all datasets,
are likely to aid in the annotation of lung immune cell sub- hg38-alignment-based data from normal/control lung samples
populations41. Future lineage/compartment specific reference con- wereused.
structionswillbeusefulinprovidingenhancedresolutionsandgran- TheCCHMCLungMAPcohortperformedscRNA-seqexperiments
ularityatsub-celltypeandcelltransitionalstateslevels.Further,the of human lung submucosal glands (SMG) obtained from five de-
current data collections do not have sufficient statistical power for identifiednormallungs.WeisolatedSMGtissue(~1mminlong)from
preciseannotationofcertainrarelungcelltypes,e.g.,SMGductcells. thehumanlungbronchusbymicrodissectionunderastereomicro-
RegionspecificLaserCaptureMicrodissection(LCM)andcellsorting scope (Leica M165 FC) using fine scissors and forceps, followed by
willbeusefulinidentifyingandcapturingrarelungcelltypesandtheir dissociatingtheSMGincocktailofprewarmeddigestionsolutionof
RNAexpressionpatterns.Finally,thereareuniquedisease-associated 0.2mg/mLcollagenaseII(ThermoFisher;cat.no.1710105)and0.1mg/
cell-populations, including infiltrating cell populations, which will mLDNaseI(Sigma-Aldrich;cat.no.DN25)inPneumaCult-EXmedium
likelynecessitatetheclassificationandinclusionofdiseasespecificcell (Stem cell technologies; cat. no. 05008) containing 1% Penicillin-
populationsandcell-states1,11.Thus,dataintegrationandannotations Streptomycin (Thermo Fisher; cat. no. 15-140-163) for 30min. The
acrossindependentlyderivednormalhealthyanddiseaseatlasesor dissociatedsinglecellswerefilteredusingastrainer(100µm;Corning;
clusteringsolutionsarealikelyanewdirectionforfutureatlasefforts. cat.no.431752)andcentrifugedat300×gfor5min,thesupernatant
In summary,wedevelopedacomputationalpipelineutilizinga wasdiscarded.ThesinglecellswereresuspendedwithHanks’Balanced
celltypedictionarytoconsolidatesingle-celltranscriptomicdatasets SaltSolution(ThermoFisher;cat.no.88284)andanalyzedusinga10x
and constructed LungMAP CellRefs and CellRef Seeds for normal SingleCell3’v3sequencingkitfollowingtheprotocolprovidedbythe
human and mouse lung. CellRef Seed has an equivalent prediction company.Sequencingreadalignmenttothehg38humangenomeand
powerandproducesconsistentcellannotationasthefullCellRef,but UMI-based gene expression matrix generation were performed for
with significantly improved computational efficiency and hardware eachsampleusing10xCellRangerv5.
requirements;facilitatingutilizationforautomatedcelltypeannota- ThenormalsamplesusedfortheUPenncohortinthisstudywere
tionandonlinevisualization,addressingasignificantcomputational fromde-identifiednon-usedlungs.scRNA-seqexperiments(10xSingle
challenge for single-cell reference applications. Using independent Cell3’v2andv3chemistry)wereperformedasdescribedinBasiletal.4.
datasets,wedemonstratedtheutilityofCellRefsforautomatedcell Inbrief,pleuraandvisibleairways/bloodvesselsweredissectedaway,
type annotations of normal lung and for potential identification of mechanicallymincedinto~2mmpieces,andprocessedintoasingle-
disease-relatedcellsbasedontheirdeviationfromnormalpulmonary cellsuspension.Afterasingle-cellsuspensionwasobtained,cellswere
cells.OurCellRefs,alongwiththedevelopedanalyticandweb-based loadedontoaGemCodeinstrument(10xGenomics,Pleasanton,CA,
tools, are freely available to the pulmonary research community to USA)togeneratesingle-cellbarcodeddroplets(GEMs)accordingto
facilitatehypothesisgeneration,researchdiscovery,andidentification themanufacture’sprotocol.Theresultinglibrariesweresequencedon
ofcelltypealterationsindiseaseconditions. anIlluminaHiSeq2500orNovaSeqinstrument.
Methods Data pre-processing. Forpublished datasets with original cell type
Ethicalapproval annotations, we included cellsselected in the originalanalyses.For
UPenn LungMAP cohort used samples from de-identified non-used published datasets without original cell type annotations (Reyfman
lungsdonatedfororgantransplantationviaanestablishedprotocol et al.12) and unpublished datasets (UPenn LungMAP cohort and
(PROPEL,approvedbyUniversityofPennsylvaniaInstitutionalReview CCHMCLungMAPcohort),thefollowingqualitycontrol(QC)criteria
Board)withinformedconsentinaccordancewithinstitutionalandNIH wereappliedtocellprefiltering,including500–7500expressedgenes,
procedures, and provided by next of kin or healthcare proxy. All lessthan25%ofUMIsmappedtomitochondrialgenes,andlessthan
patientinformationwasremovedbeforeuse.Thisusedoesnotmeet 50,000totalUMIs.ForscRNA-seqdatafromDonor29intheCCHMC
thecurrentNIHdefinitionofhumansubjectresearch,butallrelevant LungMAPcohort,weused1500–7500asthecriterionforthe“number
guidelinesandregulationsandallinstitutionalproceduresrequiredfor ofexpressedgenes”basedonitsuniquecelldistributions.Afterpre-
human subject research were followed throughout the reported filtering, Scrublet42 (v0.2.3) was performed to identify and remove
experiments. CCHMC LungMAP cohort used de-identified human potentialdoubletcellsfromeachdatasample.Intotal,505,256cells
bronchus samples provided by the Marsico Lung Institute Tissue from148sc/snRNA-seqsamplesfrom104donorswereusedasinput
ProcurementandCellCultureCoreattheUniversityofNorthCarolina, forourguidedpipelinetoconstructthesingle-cellreferenceofnormal
ChapelHill,NC(UNC)fromlungtransplantorgandonors.Participants humanlung.
didnotreceivemonetarycompensationandconsentwasobtainedby
United Network for Organ Sharing affiliated Organ Procurement MiceandDrop-seqofmouselungdevelopment
Organizations(UNCOfficeofHumanResearchEthicsprotocol#03- C57BL/6Jmice(JacksonLaboratories),embryonicdays(E)16.5,18.5to
1396).Formousestudy,animalprotocols(2C12114,2015-0060,2018- postnataldays(PND)1,3,7,10,14,28,wereusedforsingle-cellRNA-
0072, and 2021-0053) were approved by the Cincinnati Children’s seq experiments using Drop-seq43. All mice were time mated. The
NatureCommunications|( 2023)1 4:4566 14

Article https://doi.org/10.1038/s41467-023-40173-5
presenceofavaginalplugwasdefinedasE0.5.PND1wasdefinedas thatisrankedcons(cid:1)istentlybet(cid:3)terthanexpectedunderanullhypoth-
24±6hafterbirth. esis derived from R ∣x2P . Cells passing selection criteria were
xi i
Lung dissection, single cell suspension, and Drop-seq library usedascandidatesforcelltypemapping.
preparation of mouse lungs weredescribed inthe Methods of Guo Usingtheclusteringandsinglecellrankingresults,wedetermine
etal.22.DatafromPND1waspublishedinGuoetal.22.Thealignmentof candidatecellclustersforeachcelltypeiasfollows.Letφ bethesetof
i
paired-end sequencereads to mouse genome (mm10) and the gen- cellspassePdselectioncriteria(bydefault,significancescore<0.1)cells
eration of digitalexpression matrix were processed using Drop-seq inR and bethecellclustersthatweobtainedfromtheunbiased
i
tools (https://github.com/broadinstitute/Drop-seq/, v2.3.0) with clustering analysis. WePcalculate the precision and recall values
defaultparameters.Theexpressionmatrixwasgeneratedbycounting for each cluster σ 2 as follows: precisionði,jÞ=∣φ \σ∣=∣σ∣,
j i j j
thenumberofuniquemolecularidentifiers(UMIs)pergenepercell.In recallði,jÞ=∣φ \σ∣=∣φ∣,where∣φ∣and∣σ∣denotethenumberofcells
i j j j j
total,geneexpressionin17Drop-seqsamplesfromeighttimepoints inφ andσ,respectively,and∣φ \σ∣denotesthenumberofcellsin
j j i j
(SupplementaryData3)ofmouselungdevelopmentweregenerated. bothσ j andφ Pj .Thecandidatecellclustersforcelltypeiisdetermined
For each data sample, the following pre-processing steps wereper- as A =fσ 2 ∣precisionði,jÞ≥F,recallði,jÞ≥S,F2½0,1(cid:2),S2½0,1(cid:2)g. By
i j
formed. EmptyDrops44 in the Bioconductor package DropletUtils default,weuseF=0.05andS=0.25.AQCinspectionofthecandidate
(v1.4.3) was used to identify cell barcodes with expression profiles cellclustersisrecommendedtoensuretheaccuracyfortheCellRef
significantlydeviatedfromtheprofilesofemptydropletsineachdata construction.
samplewiththeparameters:lower=100,FDR<0.01.Filterswerethen In summary, in step 2, we use unsupervised clustering in con-
appliedtokeepcellswith400–7500genes,lessthan40,000UMIs, jugationwithmarker-basedsingle-cellrankingtoselectmostrelevant
and less than 10% UMIs mapped to mitochondrial genes. Potential cellgroupscandidates.Theuseofunbiasedclusteringbeforeseedcell
doublet cells in each sample were predicted and removed using identification can also provide an opportunity to discover new cell
Scrublet42. Ambient background RNAs were cleaned from gene typesthathavenotyetbeendefinedinthedictionary.Forexample,if
expression in each cell using SoupX (v1.6.2) using contamination the marker genes of a newly reported cell type are co-selectively-
fractionsautomaticallyestimatedfromdata. expressedinourcellclusters,thisnewcelltypeandmarkergenesare
addedtothecelltypedictionaryandthenincludedinthedownstream
Guidedconstructionofsingle-cellreference seedcellidentificationandCellRefconstruction.
Our guided single-cell reference (CellRef) construction workflow (iii)Seedcellidentification.Inthisstep,weaimtoidentifycellsthat
consistsoffourmajorsteps:dataintegration,candidatecellcluster bestrepresenttheidentityofeachcelltypeusingsingle-cellranking
identification, seed cell identification, and consensus prediction for basedonmarkergenesinthedictionary.Thesecellswillthenserveas
CellRef. We compiled a cell type dictionary containing a list of cell seedstoconstructtheCellRef.Foracelltypei,wefirstidentifycells
types and associated marker genes, including positive (selectively withexpressionofanynegativemarkersofiorexpressedlessthantwo
expressedinthecelltype)andnegative(noexpressioninthecelltype) positivemarkersofiandremovethosecellsfromA (thecandidatecell
i
markers.Werequiredatleasttwopositivemarkersforeachdefined clustersofcelltypeithatweidentifiedinstep2).Usingtheremaining
celltypetobeincludedinourCellRefconstruction. cellsinA,weperformsinglecellrankingusingthepositivemarkersofi
i
(i)Dataintegration.Multiplealgorithmshavebeenintegratedinto as described in step 2 and generate an aggregated ranking of cells.
ourRworkflow,includingmutualnearestneighbor(MNN)matching45, Top-rankedcellsintheaggregatedlistwillbeselectedastheseedcells
reciprocal principal component analysis (RPCA) in Seurat20 (v4.1.0), forcelltypei.
andHarmony17(v0.1.0).Bydefault,weusethealign_cdsfunctionin (iv)Consensusprediction.Onceallseedcellsareidentified,weuse
Monocle3(v1.0.0)toperformMNNmatchingbaseddataintegration themtopredictcelltypeannotationsofallcellsinthecollectionusing
andbatchcorrection.ThisisbasedontheUMAPinspectiononthe twoindependentautomatedcelltypeannotationalgorithms,Seurat’s
batchremovaleffectsandclusterstabilitymetricsmeasurementafter label transfer5,20 and SingleR6 (v1.6.1). For the Seurat’s label transfer
applyingdifferentintegrationmethods.Beforeintegration,wemerge basedprediction,weintegratescRNA-seqdataofthe“seed”cellsusing
datafromalldatasetsintoasinglegeneexpressionmatrix,useitto SCTransform normalization based reciprocal principal component
constructaMonocle3cell_data_setobject,andusethepreprocess_cds analysis(RPCA)integration,performSCTransformnormalizationon
functioninMonocle3tonormalizedatatoaddressreaddepthdif- geneexpressionineachofourcollecteddatasets,andpredictcelltype
ferences,regressoutcellcycleeffectsandmitochondrialpercentage annotationsusingtheMapQueryfunctioninSeuratv4.Apredictedcell
differences,and calculate principalcomponents representing major typeandanassociatedpredictionscorewereassignedtoeachquery
variancesinthedata. cellbasedontranscriptomicsimilaritybetweenthequerycellandthe
(ii)Candidatecellclusteridentification.Usingtheintegrateddata, “seed”cells.Cellswithlowpredictionscores(bydefault,lowest10%)
weidentifycandidatecellclustersforeachcelltypelistedinthedic- wereexcludedfromtheCellRefconstruction.FortheSingleR-based
tionary using a combination of unbiased clustering algorithm and prediction,wenormalizegeneexpressionintheseedcellsandina
marker-basedsingle-cellranking.Weperformunsupervisedclustering querydatasetbytotalUMIspercellandusetheSingleRfunctionwith
analysistogroupcellsintodistinctcellclustersbasedontranscriptomic defaultparameterstopredictcelltypeannotationsforthequerycells.
similarity. By default, we perform clustering using the Leiden Weremovedpoor-qualityorambiguouspredictionsusingtheprune-
algorithm46implementedinthecluster_cellsfunctioninMonocle3. Scores function. Let Y be the set of cells with consistent cell type
Followed by the clustering analysis, we perform a “single cell predictions in both methods. We calculated a k-nearest-neighbor
ranking”foreachcelltypeilistedinthedictionary.LetP bethesetof purity(kNN-purity)metricforeachcellinY,measuringthepercentage
i
positivemarkergenesofcelltypei.Foreachmarkergenex2P,we ofthecell’sknearestneighbors(bydefault,k=20)thathavethesame
i
identifyZ ,asetofcellswithpositive(>0)zscore-scaleexpressionof celltypeprediction.ThecompleteCellRefwascomprisedoftheseed
xi
x,andgenerateR ,arankingofcellsinZ inthedescendingorder cellsandthecellsthathaveconsistentcelltypepredictionsinboth
xi xi
b(cid:1)asedonzs(cid:3)core-scaledexpressionofx.Wethenaggregateallrankings methodsandwithkNN-purity>=0.6.
R ∣x2P intoasingleglobalrankingofcells,denotedasR,forthe
xi i i
celltypei,aimingtoidentifycellsthatarerankedhighlybymultiple ConstructionoftheLungMAPHumanLungCellRef
cell type marker genes. The aggregation was performed using an Weconstructedacelltypedictionaryfornormalhumanlung(alistof
order-statistics-based robust rank aggregation algorithm, which celltypesandtheirassociatedmarkergenes)basedonthecelltypes
assignsascoretoeachcellinR torepresentsignificanceofthecell andmarkergeneslistedintheLungMAPCellCards10.Inaddition,we
i
NatureCommunications|( 2023)1 4:4566 15

Article https://doi.org/10.1038/s41467-023-40173-5
extended the dictionary to include seven human lung cell types dictionarytoincludeprogenitorandtransitionalcellsreportedin
reportedinrecentsingle-cellstudiesbutnotyetinCellCards,including recent single-cell studies, including Sox9+/Id2+ distal epithelial
systemic venous endothelial cell (SVEC), deuterosomal cell, sub- cells23,24, AT1/AT2 cell, Foxf1+/Kit+ endothelial progenitor cells29,
mucosalgland(SMG)ductcell,megakaryocyte/platelets,suprabasal andproliferativemesenchymalprogenitorcells30,31.WeusedSeurat
cell,maturedendritic cell (maDC),and respiratoryairwaysecretory toperformSCTransformbaseddatanormalizationandperformed
cell(RAS).Intotal,48celltypesaredefinedinthedictionary. UMAP analysis on the identified LungMAP Mouse Lung Develop-
Usingthiscelltypedictionary,weperformedtheguidedCellRef ment CellRef Seed and the constructed LungMAP Mouse Lung
construction described above using seven scRNA-seq datasets. The DevelopmentCellRef.
originaldatawerealignedtothreeversionsof10xCellRangerhg38
referencegenome.Toreducetheimpactofreferencegenomediffer- AutomatedCellRefannotationofscRNA-seqofnormaland
ences on the data integration, we used the expression of 32,278 diseasedhumanlung
common gene features (based on Ensembl IDs) among the three We downloaded and processed published scRNA-seq datasets from
referencegenomeversionstoperformdataintegration(considering normal and disease human lung to demonstrate the utility of auto-
104donorsasindividualbatches)andcandidatecellclusteridentifi- matedcelltypeannotationusingtheLungMAPhumanlungCellRefs.
cationasdescribedabove.Acurationwasperformedonthecandidate ProcesseddataofscRNA-seqofnormalhumanlungweredown-
cellclusterassignmentbyinspectionofmarkergenesexpressionin loaded fromGEO using access numbers GSM5388411, GSM5388412,
thecellclusters.Basedonthecuratedcandidatecellclustersforeach GSM5388413, GSM4504966, GSM4504967, and GSM4035472. For
celltype,weselecteduptothetop200cellswiththelowestscoresas GSM5388411, GSM5388412, and GSM5388413, cells reported in the
theseedcellsforacelltype.Intotal,8080seedcellswereidentifiedfor original study33 (n=6228, 8329, and 7143 cells, respectively) were
48normalhumanlungcelltypes.Wenamedthiscollectionofseed included. For GSM4504966, GSM4504967, and GSM403547, cells
cellsastheLungMAPHumanLungCellRefSeed.Tofacilitatetheuseof (n=8381,8034,and5767,respectively)passingthefollowingcriteria
theCellRefSeedforautomatedcelltypeannotation,wenormalized wereincluded:atleast500expressedgenesandlessthan10%ofUMIs
geneexpressionintheseedcellsofeachdatasetsusingSCTransform, mappedtomitochondrialgenes.
integrateddatafromdifferentdatasetsusingtheRPCApipeline,and For scRNA-seq of human lung with lymphangioleiomyomatosis
performedUMAPanalysisontheintegrateddata. (LAM), we re-processed the data using hg38 reference genome and
Weperformedapoweranalysisanddeterminedtheminimum selected cells (n=12,374) reported in the publication1 for the auto-
cellnumbersrequiredforalungcelltypetoachieveapower>=0.8. mated CellRef annotation. For scRNA-seq of human lung with idio-
Theanalysiswasperformedasfollows.First,aCohen’sdeffectsize pathic pulmonary fibrosis (IPF), we downloaded the Seurat object
wascalculatedforeachcelltypeusingtheaveragedmeanexpres- (GSE135893_ILD_annotated_fullsize.rds.gz)fromGEOGSE135893.Data
sion and variance of all genes in the cell type of each individual (n=57,682cells)from19scRNA-seqsamplesfrom12IPFlungswere
donorwhencomparedtothoseinalltheothercells.Wegrouped usedfortheautomatedCellRefannotation.
effect size values to the following categories: small (0:2≤d<0:5), Automated CellRef annotation of eachtesting dataset was per-
medium (0:5≤d<0:7), large (d≥0:7) and then used the gPower formed using the Seurat reference mapping algorithm5,20 (Find-
softwaretocalculateasamplesizerequiredbyeachcelltypeusing TransferAnchors and MapQuery functions) using the LungMAP
thefollowingparameters:alpha=0.01,two-tailedttest,beta=0.2, Human Lung CellRef or LungMAP HumanLung CellRef Seed asthe
allocationration=1.Basedonthecalculation,aminimumof50cells reference. FindTransferAnchors was run with the following para-
isrequiredtoreachthestatisticalpower.44outofthe48human meters: normalization.method = ‘SCT’, reference.reduction = ‘pca’,
lungcelltypesmeetthecriteria;4celltypeshadlessthan50seed dims = 1:200. MapQuery was run with the following parameters:
cellsidentified,includingchondrocytes(n=6),ILC(n=14),mega- reference.reduction=‘pca’,reduction.model=‘umap’.
karyocyte/platelets(n=29),maDC(n=34).
Using the identified seed cells, we further predicted cell type EvaluationofautomatedCellRefannotationbasedonprior
annotationsforallothercellsinthe10datasetscollected.BothSeurat’s knowledge
label transfer and SingleR were applied as described above. The We developed an R script to evaluate cell type annotations pre-
LungMAPHumanLungCellRef(n=347,970cells)wascomprisedof dictedbytheLungMAPCellRefsbasedonpriorknowledge(CellRef
theseedcellsandthecellswithconsistentcelltypepredictionsand markers, cell type signature genes, and enriched gene sets or
withkNN-purityscores>=0.6.157,286cellsthatdidnotpassthecri- pathways). Currently, the functions include: (i) Dotplot visualiza-
teriawerenotincluded,consideringthecurrentversionofCellRefis tionofexpressionlevelsandfrequenciesofCellRefmarkergenesin
guidedbyaknowledge-basedcelldirectory,thosecellsmayinclude eachofthepredictedcelltypes.Selectiveandabundantexpression
transitionalstatesorcelltypesthathavenotyetdefinedbythecurrent ofmarkergenesintheircorrespondingcelltypes(pvalueoftwo-
CellRef. tailed Wilcoxon rank-sum test <0.05, fold change>=1.5 and
To facilitate the use of the LungMAP Human Lung CellRef for expressionpercentage>=0.2)indicateaconcordanceofcelliden-
automated cell type annotation, we normalized gene expression in titiesinthepredictionsandintheCellRef.(ii)Identificationofsig-
eachdonor in the CellRefusing SCTransform,integrated datafrom nature genes for each of the predicted cell types. By default, the
differentdonorsusingtheRPCApipeline,andperformedUMAPana- identification was performed using Seurat’s FindAllMarkers func-
lysisontheintegrateddata.DuringtheRPCAintegration,weidentified tionbasedonthefollowingcriteria:adjustedpvalueoftwo-tailed
“anchors” using the FindIntegrationAnchors function, filtered out Wilcoxonrank-sumtest<0.1,pct>=20%,andfoldchange>=1.5.A
“anchors”mappingcellswithdifferentcelltypepredictions,andthen sufficient number of signature genes (e.g., >=50 genes) would be
used the remaining “anchors” for data integration using the Inte- expected to define a distinct cell type. (iii) Gene sets functional
grateDatafunction. enrichmentanalysis(GeneOntologyBiologicalProcess,Pathways)
associatedwiththeidentifiedcelltypesignaturegenes.Functional
ConstructionoftheLungMAPMouseLungDevelopmentCellRef enrichment analysis was performed using R package gprofiler2
Weconstructedacelltypedictionaryformouselung(Supplemen- (v0.2.1). Given scRNA-seq data with automated cell type annota-
taryData4)basedonourconstructeddictionaryderivedfromthe tions,theRscriptcangeneratethevisualizationsandevaluations
LungMAP CellCards. In addition, because of the developmental for all predicted cell types at once and compile results into an
design of the mouse data, we extended the mouse lung cell type evaluationreportusingRmarkdown.
NatureCommunications|( 2023)1 4:4566 16

Article https://doi.org/10.1038/s41467-023-40173-5
EvaluationofautomatedCellRefcelltypeannotationusing assignmentaccuracybymeasuringthefractionofcellsineachcluster
originalannotationsofpublishedscRNA-seqdata thatcanbere-classifiedtoitsowncentroid.TFIDF10scoresmeasure
We downloadedthe originalcelltypeannotation (45 cell types and cluster marker gene specificity by the strength of the 10th most
states)33 of scRNA-seq of adult human lung (GSM5388411, exclusivelyexpressedfeatureinacluster.TheHLCAcorereference
GSM5388412,andGSM5388413)fromGEOusingGSE178360.Thecell (v1.0) was downloaded as an h5ad file from the cellxgene (https://
type nomenclature and resolutions in the original annotation were cellxgene.cziscience.com/).WeappliedscTriangulatetotheLungMAP
differentfromtheCellRefannotations.Tomatchthecellpopulations HumanandMouseLungCellRefsandtheHLCA,separately,calculated
inthetwoannotationsforcomparison,weperformedthefollowing: the SCCAF, Reassign, and TFIDF10 scores for each cell type in the
(i) exclude cell types or states with less than 50 cells, (ii) exclude human lung CellRef, mouse lung CellRef, and HLCA. LogNormalize
uniquecelltypes/statesthatwereonlypresentinoneannotation,and geneexpressiondatawasusedinthecalculations.ForCellRef,weused
(iii)mergedcellsub-populationsthatweredefinedatdifferentgran- theannotationsof48humanlungand40mouselungcelltypes.For
ularitiesbetweentheoriginalandtheCellRefannotations.Afterthe HLCA, we used the ann_finest_level original annotation of 58 cell
processing,24matchedcellpopulationswereusedforthecompar- types37.
ison,includingAT1,AT2,basal,secretory,SCGB3A2+,ciliated,CAP1, WealsoassessedthestabilityofhumanlungCellRefandHLCAby
CAP2,arterial/venous/lymphatic/systemicvenousendothelial,airway/ projecting their annotations tothe previously-reported human lung
vascular smooth muscle, alveolar fibroblast, macrophage, dendritic, scRNA-seqatlas15,whichwasdownloadedasanh5adfilefromcellx-
monocyte, B, plasma, mast/basophil, neutrophil, natural killer, and gene(https://cellxgene.cziscience.com/)andsuppliedasaninputto
T cells. For each cell population, we calculated precision, recall, Azimuth instances for the cell type annotation using the LungMAP
accuracy, F1 score, and Matthews correlation coefficient (MCC) to Human Lung CellRef Seed (https://app.lungmap.net/app/azimuth-
quantifytheconsistencybetweentheoriginalandCellRefannotations. human-lung-cellref-seed) and the integrated HLCA (https://app.
These metrics are defined as follows: precision=TP=ðTP+FPÞ, azimuth.hubmapconsortium.org/app/human-lung-v2). The mapped
recall=TP=ðTP+FNÞ, accuracy=ðTP+TNÞ=ðTP+TN+FP+FNÞ, annotationsfromtheCellRefandHLCAwereanalyzedandvisualized
F1=2×ðprpecffiffiiffiffisffiffiiffioffiffiffinffiffiffiffi×ffiffiffirffiffieffiffifficffiffiaffiffiffilffilffiffiÞffi = ffiffiffiðffipffiffiffirffiffieffiffifficffiffiiffisffiffiiffiffioffiffinffiffiffiffi+ffiffiffiffirffiffieffifficffiffiaffiffiffilffiffilffiÞffiffi,ffiffiffiaffiffinffiffiffidffiffiffiffiMffiffiffiffiCffiffiffiffiffiC=ðTP×TN(cid:3) (UMAP)inscTriangulate18usingdefaultprogramoptions.
FP×FNÞ= ðTP+FPÞ×ðTP+FNÞ×ðTN+FPÞ×ðTN+FNÞ. For a cell
populationi,TP(TruePositive)representsthepercentageofpopula- AssessmentofcelltypeidentitymappingbetweenCellRefand
tionicellspredictedbytheCellRefthatwerealsoidentifiedaspopu- HLCAusingpseudo-bulk-basedcorrelationanalysis
lationicellsintheoriginalannotation;FP(FalsePositive)represents Toassessthecellidentityandmappingofcelltypesinthehumanlung
thepercentageofpopulationicellspredictedbytheCellRefthatwere CellRef and HLCA, we first created a pseudo-bulk gene expression
notinthepopulationioftheoriginalannotation;TN(TrueNegative) profileforeachcelltypebyaveragingtheexpressionofeachgeneofall
representsthepercentageofcellsnotannotatedaspopulationibythe cells in the given cell type. Then Seurat’s FindVariableFeatures was
CellRefandwerealsonotinthepopulationioftheoriginalannotation, used to find the top2000highly variable genes (HVGs)among the
FN(FalseNegative)representsthepercentageofcellsnotannotatedas pseudo-bulkprofilesoftheCellRef,denoteHVG1,andtheHVGsamong
populationibytheCellRefbutwereinthepopulationioftheoriginal thepseudo-bulkprofilesoftheHLCA,denoteHVG2.Wetooktheunion
annotation. ofHVG1andHVG2andkeptthegenesthatarepresentinbothrefer-
ences, resulting in 2501 HVGs. We performed zscore scaling of the
EvaluationofCellRefcelltypeannotationsusing10-foldcross expressionof2501genesamongtheCellRefandtheHLCApseudo-
validation bulkprofiles,separately.Pearson’scorrelationsamongallthepseudo-
Weperformed10-foldcrossvalidationforbothLungMAPhumanand bulk profiles of CellRef and HLCA were calculated using the scaled
mouseCellRefs.Ineachcase,werandomlydividedthedatainto10 expression of 2501 HVGs. Hierarchical clustering analysis was per-
equalpartsusingtheKFoldfunctionintheRpackagerBayesianOpti- formed using R package pheatmap (v1.0.12) using the correlation
mization(v1.2.0).Thepartitionswereperformedforeachcelltypeso matrixasinput.
thateachofthe10datapartscontainssimilarcelltypedistributions.
Celltypeswithmorethan500cellswereusedinthecrossvalidation Marker-basedassessmentofcelltypeaccuracyusingreceiver
analysissothateachdatapartcontainedmorethan50cellsofeachcell operatorcharacteristics(ROC)analysis
type.Thedesignisbasedonourpoweranalysiswhichdeterminedthat Inthisanalysis,weusedareaundertheROCcurve(AUC)toassessthe
50istheminimumcellnumbersrequiredforalungcelltypetoachieve accuracyofeachcelltypeinasingle-cellreferencebasedonitscon-
a power>=0.8. For each round of validation, we used 9 parts as sistencywiththeexpressionofcelltypeselectivemarkergenes.LetX
trainingdatatopredictcelltypesoftheremainingpart(testingdata) bethesetofallcellsinthereference,X (cid:4)Xbethecellsofcelltypeiin
i
usingtheSeuratreferencemappingalgorithm.Intotal,10runsofthe thereference,andY bethesetofmarkergenesofthecelltypei.For
i
trainingandtestingwereperformed.Ateachrun,adifferentdatapart eachmarkergeney2Y ,wegeneratedarankingofXaccordingtothe
i
was used as the testing data and the prediction performance was decreasingorderofthezscore-transformedexpressionofyinX.Then
measured by calculating an F1 score and a Matthews correlation wegeneratedaglobalrankingofX bymergingalltherankingsbyY
i
coefficient(MCC)foreachcelltypeinthetestingdata.Wereported usingtheaggregateRanksfunctionintheRpackageRobustRankAg-
thedistributionsoftheF1andMCCscoresofallcelltypesinacross greg (v1.2.1). The AUC score for the cell type i was calculated by
validation analysis and considered the median scores as the overall comparing this global ranking with the cell type annotation in the
performance. reference, i.e., all cells in X were considered as positive instance;
i
otherwise, negative. The AUC scores were calculated using the roc
Celltypestabilityanalysis functioninthepROC(v1.18.0)packagewithdefaultparameters.
We calculated cell type stability metrics (SCCAF39, Reassign18, ThehumanlungCellRefcelltypeselectivemarkersweregener-
TFIDF1018) using scTriangulate18 (v0.12.0, https://github.com/ atedbyincludingdictionarymarkergenes(SupplementaryData2)and
frankligy/scTriangulate).Single-cellclusteringassessmentframework topselectivelyexpressedmarkersforeachcelltype.Upto10marker
(SCCAF) randomly splits data into a training and a testing set, con- geneswereselectedforeachcelltypeusingthefollowingcriteria.For
sidersallfeaturesinthetrainingsettobuildaclassifiertopredictcell each cell type in the human lung CellRef, we identified its specific
labelsofatestingsetandcomparewiththereferenceannotationsin differentiallyexpressedgenes(DEGs)inCellRefandCellRefSeedusing
theCellRefsorHLCA.Thereassignscoresmeasurecell-to-clusterre- thefollowingcriteria:adjustedpvalueoftwo-tailedWilcoxonrank-
NatureCommunications|( 2023)1 4:4566 17

Article https://doi.org/10.1038/s41467-023-40173-5
sumtest<0.1,expressionpercentage>=30%,foldchangeofaverage “LMEX0000004396”.Drop-seqofmouselungdatausedinthemouse
expression>=1.5,andrecall>10%.Top-rankedcelltypespecificDEGs lung CellRef are available in the Gene Expression Omnibus under
(rankedbyfoldchangeinaverageexpression)werecombinedwiththe accessioncode“GSE122332”andintheLungMAP.netunderaccession
knownmarkersgenestoformtheCellRefcelltypeselectivemarker code “LMEX0000004397”. Published single cell RNA-seq of human
gene list(Supplementary Data5,upto 10genes foreachofthe 48 lung data used in the evaluation analysis are available in the Gene
CellRef human lung cell types). DE tests were performed using the Expression Omnibus under accession codes “GSE178362”,
FindAllMarkers function in Seurat (v4.1.0) with the following para- “GSE135893”,“GSE135851”,and“GSE149563”.TheHLCAcorereference
meters:test.use=”wilcox”,assay=”RNA”,only.pos=T.Therecallofa (version 1.0) used in the benchmarking analysis is available at FAS-
geneexpressioninacelltypewascalculatedasthenumberofcellsin TGenomics under accession code “dataset-427f1eee6dd44f50-
thecelltypewithpositiveexpression(>0)ofthegenedividedbythe bae1ab13f0f3c6a9 [https://beta.fastgenomics.org/datasets/detail-
totalnumberofcellswithpositiveexpressionofthegene.Usingthe dataset-427f1eee6dd44f50bae1ab13f0f3c6a9]”.Webinterfacesforthe
same approach, the mouse lung CellRef cell type selective marker humanandmouselungCellRefsareavailableatLungGeneExpression
geneswereselected(SupplementaryData6,upto10markergenesper Analysis (LGEA) web portal (https://research.cchmc.org/pbge/
cell type) and used for the AUC based assessment of mouse lung lunggens/CellRef/LungMapCellRef.html) and LungMAP.net (https://
CellRef. The human and mouse CellRef markers are also openly lungmap.net/cell-cards/,“CellRefscRNA-seq”tab).Allotherdatasup-
accessible at LGEA CellRef (https://research.cchmc.org/pbge/ portingthefindingsofthisstudyareavailablewithinthearticleandits
lunggens/CellRef/LungMapCellRef.html). The HLCA predicted mar- supplementaryfiles.Anyadditionalrequestsforinformationcanbe
kersgenesweredownloadedfromSikkemaetal.37,whichcontainsup directedto,andwillbefulfilledby,theleadcontact.Sourcedataare
to10genesforeachofthe58HLCAcelltypes. providedwiththispaperin‘SourceData.zip’.
Assessmentofsingle-celldataintegrationusingtheLocal Codeavailability
InverseSimpson’sIndex(LISI)metrics ThecodeofLungMAPCellRefconstructionpipelineandthecodeto
WeassessedthedataintegrationintheLungMAPCellRefsandHLCA reproducetheanalysesareavailableonGitHub:https://github.com/
using the LISI metrics (https://github.com/immunogenomics/LISI, xu-lab/CellRef19.
v1.0),includingintegrationLISI(iLISI)andcell-typeLISI(cLISI).Givena
single-celldataintegration(CellReforHLCA),aniLISIscorewascal-
culatedforeachcellineachcelltypeusingthecompute_lisifunctionin References
LISIpackagewiththefollowingparameters:theUMAPcoordinatesof 1. Guo,M.etal.Single-celltranscriptomicanalysisidentifiesaunique
allcellsintheselectedcelltypeandthebatchinformation(donoror pulmonarylymphangioleiomyomatosiscell.Am.J.Respir.Crit.Care
datasample)ofallcellsintheselectedcelltype.Wenormalizedthe Med.202,1373–1387(2020).
iLISIscoreofeachcellusingthetotalnumberofbatchesinthecelltype 2. Wang,A.etal.Single-cellmultiomicprofilingofhumanlungs
ofthecell.Givenanintegratedsingle-celldata,acLISIscorewascal- revealscell-type-specificandage-dynamiccontrolofSARS-CoV2
culatedforeachcellusingthecompute_lisifunctioninLISIpackage hostgenes.Elife9,https://doi.org/10.7554/eLife.62522
withthefollowingparameters:theUMAPcoordinatesandthecelltype (2020).
informationofallcellsintheintegration.FortheCellRef,weusedthe 3. Melms,J.C.etal.Amolecularsingle-celllungatlasoflethalCOVID-
annotationof48celltypesforthecLISIcalculation.FortheHLCA,we 19.Nature595,114–119(2021).
used the ann_finest_level annotation of 58 cell types for the cLISI 4. Basil,M.C.etal.Humandistalairwayscontainamultipotent
calculation. secretorycellthatcanregeneratealveoli.Naturehttps://doi.org/10.
1038/s41586-022-04552-0(2022).
Statisticalanalysis 5. Hao,Y.etal.Integratedanalysisofmultimodalsingle-celldata.Cell
Statisticalanalysesofdifferencesintheareaunderthereceiveroper- 184,3573–3587.e3529(2021).
atingcharacteristicscurves(AUCs),celltypestabilityscores,anddata 6. Aran,D.etal.Reference-basedanalysisoflungsingle-cell
integrationscoreswereperformedinR(v4.1.0)usingWelch’sttest sequencingrevealsatransitionalprofibroticmacrophage.Nat.
(two-tailed, unequal variance). Multiple testing correction was per- Immunol.20,163–172(2019).
formed using Bonferroni correction. The results are expressed as 7. Abdelaal,T.etal.Acomparisonofautomaticcellidentification
violinplotsorboxplotsrepresenting25%,50%,and75%quantiles,with methodsforsingle-cellRNAsequencingdata.GenomeBiol.20,
mean±SD orSEMerror bars, asnoted in individualfigurelegends. 194(2019).
Differential expression analysis of single-cell gene expression was 8. Osumi-Sutherland,D.etal.CelltypeontologiesoftheHumanCell
performedintheRpackageSeurat(v4.1.0)usingtwo-tailedWilcoxon Atlas.Nat.CellBiol.23,1129–1135(2021).
rank-sumtest. 9. Miller,J.A.etal.Commoncelltypenomenclatureforthe
mammalianbrain.Elife9,https://doi.org/10.7554/eLife.
Reportingsummary 59928(2020).
Further information on research design is available in the Nature 10. Sun,X.etal.Acensusofthelung:CellCardsfromLungMAP.Dev.
PortfolioReportingSummarylinkedtothisarticle. Cell57,112–145.e112(2022).
11. Habermann,A.C.etal.Single-cellRNAsequencingrevealsprofi-
Dataavailability broticrolesofdistinctepithelialandmesenchymallineagesin
Published single cell/nucleus RNA-seq of human lung used in the pulmonaryfibrosis.Sci.Adv.6,eaba1972(2020).
human lung CellRef are available in the Gene Expression Omnibus 12. Reyfman,P.A.etal.Single-celltranscriptomicanalysisofhuman
under accession codes “GSE135893”, “GSE136831”, “GSE122960”, lungprovidesinsightsintothepathobiologyofpulmonaryfibrosis.
“GSE134174”, “GSE161382”, “GSE171524”, in the European Genome- Am.J.Respir.Crit.CareMed.199,1517–1536(2019).
phenomeArchiveunderaccessioncode“EGAS00001004082[https:// 13. Adams,T.S.etal.Single-cellRNA-seqrevealsectopicandaberrant
ega-archive.org/studies/EGAS00001004082]”,andintheSynapse.org lung-residentcellpopulationsinidiopathicpulmonaryfibrosis.Sci.
under accession code “syn21041850 [https://www.synapse.org/#! Adv.6,eaba1983(2020).
Synapse:syn21041850]”.TheLungMAPCCHMCandUPenndataused 14. Deprez,M.etal.Asingle-cellatlasofthehumanhealthyairways.
inthisstudyareavailableintheLungMAP.netunderaccessioncode Am.J.Respir.Crit.CareMed.202,1636–1645(2020).
NatureCommunications|( 2023)1 4:4566 18

Article https://doi.org/10.1038/s41467-023-40173-5
15. Travaglini,K.J.etal.Amolecularcellatlasofthehumanlungfrom 37. Sikkema,L.etal.Anintegratedcellatlasofthehumanlunginhealth
single-cellRNAsequencing.Nature587,619–625(2020). anddisease.PreprintatbioRxivhttps://doi.org/10.1101/2022.03.10.
16. Goldfarbmuren,K.C.etal.Dissectingthecellularspecificityof 483747(2022).
smokingeffectsandreconstructinglineagesinthehumanairway 38. Sikkema,L.etal.Anintegratedcellatlasofthelunginhealthand
epithelium.Nat.Commun.11,2485(2020). disease.Nat.Med.29,1563–1577(2023).
17. Korsunsky,I.etal.Fast,sensitiveandaccurateintegrationofsingle- 39. Miao,Z.etal.Putativecelltypediscoveryfromsingle-cellgene
celldatawithHarmony.Nat.Methods16,1289–1296(2019). expressiondata.Nat.Methods,https://doi.org/10.1038/s41592-
18. Li,G.etal.Decisionlevelintegrationofunimodalandmultimodal 020-0825-9(2020).
singlecelldatawithscTriangulate.Nat.Commun.14,406(2023). 40. DePasquale,E.A.K.etal.cellHarmony:cell-levelmatchingand
19. Guo,M.etal.Guidedconstructionofsinglecellreferencefor holisticcomparisonofsingle-celltranscriptomes.NucleicAcids
humanandmouselung.github.com/xu-lab/CellRef,https://doi. Res.47,e138(2019).
org/10.5281/zenodo.8111545(2023). 41. Seumois,G.&Vijayanand,P.Single-cellanalysistounderstandthe
20. Stuart,T.etal.ComprehensiveIntegrationofSingle-CellData.Cell diversityofimmunecelltypesthatdrivediseasepathogenesis.J.
177,1888–1902.e1821(2019). AllergyClin.Immunol.144,1150–1153(2019).
21. Schupp,J.C.etal.Integratedsingle-cellatlasofendothelialcellsof 42. Wolock,S.L.,Lopez,R.&Klein,A.M.Scrublet:computational
thehumanlung.Circulation144,286–302(2021). identificationofcelldoubletsinsingle-celltranscriptomicdata.Cell
22. Guo,M.etal.SinglecellRNAanalysisidentifiescellularhetero- Syst.8,281–291.e289(2019).
geneityandadaptiveresponsesofthelungatbirth.Nat.Commun. 43. Macosko,E.Z.etal.Highlyparallelgenome-wideexpressionpro-
10,37(2019). filingofindividualcellsusingnanoliterdroplets.Cell161,
23. Morrisey,E.E.&Hogan,B.L.Preparingforthefirstbreath:genetic 1202–1214(2015).
andcellularmechanismsinlungdevelopment.Dev.Cell18, 44. Lun,A.T.L.etal.EmptyDrops:distinguishingcellsfromempty
8–23(2010). dropletsindroplet-basedsingle-cellRNAsequencingdata.Gen-
24. Rawlins,E.L.,Clark,C.P.,Xue,Y.&Hogan,B.L.TheId2+distaltip omeBiol.20,63(2019).
lungepitheliumcontainsindividualmultipotentembryonicpro- 45. Haghverdi,L.,Lun,A.T.L.,Morgan,M.D.&Marioni,J.C.Batch
genitorcells.Development136,3741–3745(2009). effectsinsingle-cellRNA-sequencingdataarecorrectedby
25. Treutlein,B.etal.Reconstructinglineagehierarchiesofthedistal matchingmutualnearestneighbors.Nat.Biotechnol.36,
lungepitheliumusingsingle-cellRNA-seq.Nature509, 421–427(2018).
371–375(2014). 46. Traag,V.A.,Waltman,L.&vanEck,N.J.FromLouvaintoLeiden:
26. Kobayashi,Y.etal.Persistenceofaregeneration-associated,tran- guaranteeingwell-connectedcommunities.Sci.Rep.9,
sitionalalveolarepithelialcellstateinpulmonaryfibrosis.Nat.Cell 5233(2019).
Biol.22,934–946(2020). 47. Shekhar,K.etal.Comprehensiveclassificationofretinalbipolar
27. Choi,J.etal.InflammatorysignalsinduceAT2cell-deriveddamage- neuronsbysingle-celltranscriptomics.Cell166,1308–1323.e1330
associatedtransientprogenitorsthatmediatealveolarregenera- (2016).
tion.CellStemCell27,366–382.e367(2020).
28. Strunz,M.etal.AlveolarregenerationthroughaKrt8+transitional Acknowledgements
stemcellstatethatpersistsinhumanlungfibrosis.Nat.Commun. WethankallmembersoftheLungMAP2consortiumfortheirinput
11,3559(2020). anddiscussion.WethanktheLungMAP2externaladvisorycommittee
29. Wang,G.etal.Generationofpulmonaryendothelialprogenitor fortheirinsights.WethankScottRandellandMarsicoLungInstitute
cellsforcell-basedtherapyusinginterspeciesmouse-ratchimeras. TissueProcurementandCellCultureCoreforprovidingthehuman
Am.J.Respir.Crit.CareMed.204,326–338(2021). bronchialsamplesforthesubmucosalglandscRNA-seqdatagen-
30. Guo,M.,Wang,H.,Potter,S.S.,Whitsett,J.A.&Xu,Y.SINCERA:a eration.ThisresearchwassupportedbytheNHLBI(U01HL122642and
pipelineforsingle-cellRNA-seqprofilinganalysis.PLoSComput. U01HL148856toJ.A.W.andY.X.;U01HL134745toJ.A.W.andY.X.;
Biol.11,e1004575(2015). R01HL153045toY.X.;U01HL148867toX.S.,U01HL148857toE.E.M.,
31. Bridges,J.P.etal.Glucocorticoidregulatesmesenchymalcell U01HL148860toJ.N.A.andG.C.,U01HL148861andU01HL122700to
differentiationrequiredforperinatallungmorphogenesisand G.S.P.,U24HL148865toB.J.A.andN.S.),NIDDK(P30DK117467to
function.Am.J.Physiol.LungCellMol.Physiol.319, A.P.N.,J.A.W.,Y.X.,K.M.,andK.A.W.-B.),andtheLAMFoundation
L239–L255(2020). (LAM0150C01-22toM.G.).
32. Ouyang,J.F.,Kamaraj,U.S.,Cao,E.Y.&Rackham,O.J.L.ShinyCell:
simpleandsharablevisualisationofsingle-cellgeneexpression
data.Bioinformatics,https://doi.org/10.1093/bioinformatics/ Authorcontributions
btab209(2021). Conceptualization:M.G.andY.X.Writing:M.G,Y.X.,andJ.A.W.Data
33. KadurLakshminarasimhaMurthy,P.etal.Humandistallungmaps collectionandprocessing:M.G.,M.P.M,Y.W.,S.Z.,andA.W.Datagen-
andlineagehierarchiesrevealabipotentprogenitor.Nature604, eration:J.A.W.,K.A.W.-B.,J.A.K.,K.M.,A.P.N.,E.E.M.,K.S.,M.C.B.,S.M.L.,
111–119(2022). andY.Y.CellRefconstruction:M.G.andY.X.Benchmarkanalysis:C.J.,
34. Zepp,J.A.etal.Genomic,epigenomic,andbiophysicalcuescon- G.L.,M.G.,Y.X,N.S.,andA.C.C.Webportals:Y.D.,M.P.M.,A.W.,M.K.,
trollingtheemergenceofthelungalveolus.Science371,https:// K.J.,N.G.,A.B.,A.C.C.,B.J.A.,T.L.T.,andN.S.Cellidentityandmarkers
doi.org/10.1126/science.abc3172(2021). selection:M.G.,Y.X.,X.S.,E.E.M.,J.A.W.,B.J.A.,G.S.P.,R.S.M.,J.N.A.,and
35. Madissoon,E.etal.scRNA-seqassessmentofthehumanlung, G.C.Fundingacquisition:J.A.W.,Y.X.,X.S.,E.E.M,G.S.P.,J.N.A.,G.C.,
spleen,andesophagustissuestabilityaftercoldpreservation. B.J.A.,T.L.T.,andN.S.Allauthorsreviewedandapprovedthefinal
GenomeBiol.21,1(2019). version.
36. VieiraBraga,F.A.etal.Acellularcensusofhumanlungsidentifies
novelcellstatesinhealthandinasthma.Nat.Med.25, Competinginterests
1153–1163(2019). Theauthorsdeclarenocompetinginterests.
NatureCommunications|( 2023)1 4:4566 19

Article https://doi.org/10.1038/s41467-023-40173-5
Additionalinformation OpenAccessThisarticleislicensedunderaCreativeCommons
SupplementaryinformationTheonlineversioncontains Attribution4.0InternationalLicense,whichpermitsuse,sharing,
supplementarymaterialavailableat adaptation,distributionandreproductioninanymediumorformat,as
https://doi.org/10.1038/s41467-023-40173-5. longasyougiveappropriatecredittotheoriginalauthor(s)andthe
source,providealinktotheCreativeCommonslicense,andindicateif
Correspondenceandrequestsformaterialsshouldbeaddressedto changesweremade.Theimagesorotherthirdpartymaterialinthis
MinzheGuoorYanXu. articleareincludedinthearticle’sCreativeCommonslicense,unless
indicatedotherwiseinacreditlinetothematerial.Ifmaterialisnot
PeerreviewinformationNatureCommunicationsthankstheanon- includedinthearticle’sCreativeCommonslicenseandyourintended
ymous,reviewer(s)fortheircontributiontothepeerreviewofthiswork. useisnotpermittedbystatutoryregulationorexceedsthepermitted
use,youwillneedtoobtainpermissiondirectlyfromthecopyright
Reprintsandpermissionsinformationisavailableat holder.Toviewacopyofthislicense,visithttp://creativecommons.org/
http://www.nature.com/reprints licenses/by/4.0/.
Publisher’snoteSpringerNatureremainsneutralwithregardtojur- ©TheAuthor(s)2023
isdictionalclaimsinpublishedmapsandinstitutionalaffiliations.
1ThePerinatalInstituteandSectionofNeonatology,PerinatalandPulmonaryBiology,CincinnatiChildren’sHospitalMedicalCenter,3333BurnetAvenue,
Cincinnati,OH45229,USA.2DepartmentofPediatrics,UniversityofCincinnatiCollegeofMedicine,3230EdenAvenue,Cincinnati,OH45267,USA.
3DepartmentofMedicine,UniversityofPennsylvania,Philadelphia,PA19104,USA.4Penn-CHOPLungBiologyInstitute,UniversityofPennsylvania,Phila-
delphia,PA19104,USA.5DepartmentofCellandDevelopmentalBiology,UniversityofPennsylvania,Philadelphia,PA19104,USA.6DivisionofBiomedical
Informatics,CincinnatiChildren’sHospitalMedicalCenter,3333BurnetAvenue,Cincinnati,OH45229,USA.7RTIInternational,Durham,NC27709,USA.
8DivisionofPathologyandLaboratoryMedicine,CincinnatiChildren’sHospitalMedicalCenter,3333BurnetAvenue,Cincinnati,OH45229,USA.9Depart-
mentofPathology&LaboratoryMedicine,UniversityofCincinnatiCollegeofMedicine,3230EdenAvenue,Cincinnati,OH45267,USA.10Divisionof
PulmonaryandCriticalCareMedicine,DepartmentofMedicine,Cedars-SinaiMedicalCenter,LosAngeles,CA90048,USA.11BoardofGovernorsRegen-
erativeMedicineInstitute,Cedars-SinaiMedicalCenter,LosAngeles,CA90048,USA.12BiologicalSciencesDivision,PacificNorthwestNationalLaboratory,
Richland,WA99352,USA.13DepartmentofPediatricsDivisionofNeonatology,UniversityofRochesterMedicalCenter,Rochester,NY14642,USA.14Data
SciencesPlatform,TheBroadInstitute,Cambridge,MA02142,USA.15DepartmentofPediatrics,UniversityofCaliforniaatSanDiego,9500GilmanDr.,La
Jolla,CA92093,USA.16DepartmentofBiologicalSciences,UniversityofCaliforniaatSanDiego,9500GilmanDr,LaJolla,CA92093,USA.
e-mail:minzhe.guo@cchmc.org;yan.xu@cchmc.org
NHLBILungMAPConsortium
SaraLin17
17NationalHeart,Lung,andBloodInstitute,NationalInstitutesofHealth,Bethesda,MD20892,USA.
NatureCommunications|( 2023)1 4:4566 20