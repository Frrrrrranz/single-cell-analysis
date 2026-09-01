Article https://doi.org/10.1038/s41467-024-52052-8
The single-cell transcriptomic atlas iPain
fi
identi es senescence of nociceptors as a
therapeutical target for chronic pain
treatment
Received:7May2024 PrachTechameena 1,2,XiaonaFeng1,2,KaiwenZhang 1&SaidaHadjab 1
Accepted:21August2024
Chronicpainremainsasignificantmedicalchallengewithcomplexunderlying
mechanisms,andanurgentneedfornewtreatments.Ourresearchbuiltand
Checkforupdates
utilizedtheiPainsingle-cellatlastostudychronicpainprogressionindorsal
rootandtrigeminalganglia.Wediscoveredthatsenescenceofasmallsubset
ofpain-sensingneuronsmaybeadriverofchronicpain.Thismechanismwas
observedinanimalmodelsafternerveinjuryandinhumanpatientsdiagnosed
withchronicpainordiabeticpainfulneuropathy.Notably,treatmentwith
senolytics,drugsthatremovesenescentcells,reversedpainsymptomsinmice
post-injury.Thesefindingshighlighttheroleofcellularsenescenceinchronic
paindevelopment,demonstratethetherapeuticpotentialofsenolytictreat-
ments,andunderscorethevalueoftheiPainatlasforfuturepainresearch.
Currently,around20%ofadultssufferfromchronicpain,whichwould project within the spinal cord or the pons where the pain signal is
correspondtoover1.2billionpeopleworldwide,makingitaglobal transmitted and integrated locally and sent to upper brain centers
healthcare crisis1. While there are treatments available, these often whereitisperceivedasapainsensation.
provideonlypartialreliefifatall,andcomewithadversesideeffects Theintroductionofsingle-cellRNAsequencing(scRNA-seq)has
andariskofdrugabuse2,3.Thesetreatmentsalsocenteronpainsig- enabledthetransformativeadvancementinourunderstandingofthe
nalingmodulationanddonotaddresstheunderlyingmolecularand intricatefunctionaldiversityofdisorderdevelopmentmuchlikethe
cellularcausesofchronicpain.Abetterunderstandingofthemole- comprehensive atlases created in other fields such as cancer7 and
cularchangesunderlyingchronicpainprogressioncouldenablethe neurologicaldisorders8.Inasubstantialefforttocreateatlaseswith
development of innovative, non-addictive therapeutic strategies to further gene coverage than already available and with chromatin
effectively alleviate chronic pain. Thus, understanding the mechan- dynamicinformation,weintegrateddiversesinglecell(sc)orsingle-
ismsinvolvedinpainchronificationhaveremainedcrucialforunco- nuclei (sn) RNA-seq from peer-reviewed datasets with our in-house
veringnewtherapeuticavenues. datasets5,9–17 (Table 1), with the aim to further unveil the molecular
Painsensationisconveyedperipherallybytheactivationofpain- signaturesgoverningthedevelopmentandpersistenceofthedifferent
sensingneurons,ornociceptors,whosecellbodiesresideintheper- types of chronic pain while also focusing on uncovering a shared
ipheral sensory ganglia (mostly in the dorsal root ganglia, DRG, mechanism among diverse pain models. With our somatosensory
alongside the spinal cord and in the trigeminal ganglia, TG). Those atlasescallediPainavailableonCELLxGENEbrowser,wehaveestab-
neurons are of different subtypes that are classified as peptidergic lished a foundational frameworkthat builds upon and extends pre-
(PEPs),non-peptidergic(NPs),C-LowThresholdmechanoreceptor(C- vious research efforts5,11 and is crucial for investigating the
LTMRs), and a subtype of somatostatin positive neurons (SST)4–6. developmentofchronicpain,whenoriginatinginthefirstanatomical
Nociceptors send peripheral nerve endings throughout the whole relay of pain pathway, either in the DRG (iPainDRG) or in
body,innervatingtheskin,duramater,anddeeptissue.Centrally,they theTG(iPainTG).UsingiPainDRG,ourresultsidentifythesenescence
1LaboratoryofNeurobiologyofPain&Therapeutics,DepartmentofNeuroscience,KarolinskaInstitutet,Stockholm,Sweden.2Theseauthorscontributed
equally:PrachTechameena,XiaonaFeng. e-mail:saida.hadjab@ki.se
NatureCommunications|( 2024)1 5:8585 1
;,:)(0987654321 ;,:)(0987654321

| Article |     |     |     | https://doi.org/10.1038/s41467-024-52052-8 |     |     |     |
| ------- | --- | --- | --- | ------------------------------------------ | --- | --- | --- |
Table1|Thetableindicatingthedatasources,single-cell/ Supplementary Fig. 3b). These atlases, with their detailed cell-type-
nucleitechnologies,GeneExpressionOmnibusaccession specific markers and chromatin accessibility profiles, can serve as
numbers,andtissuesincludediniPain valuablereferencesfortheresearchcommunitystudyingtheunder-
|        |        |     | lying mechanisms | of chronic           | pain (Fig. | 1d, h; and Supplementary |             |
| ------ | ------ | --- | ---------------- | -------------------- | ---------- | ------------------------ | ----------- |
| Source | Method | GEO | Tissue           |                      |            |                          |             |
|        |        |     | Data 2–3).       | Finally, the atlases | allow for  | the integration          | of datasets |
Renthaletal.5
|     | snRNA-seq(inDrops) | GSE154659 | DRG |     |     |     |     |
| --- | ------------------ | --------- | --- | --- | --- | --- | --- |
sequencedbyanysequencingtechnologies.
| Wangetal.9     | scRNA-seq(10×) | GSE155622 | DRG |     |     |     |     |
| -------------- | -------------- | --------- | --- | --- | --- | --- | --- |
| Avrahametal.10 | scRNA-seq(10×) | GSE158892 | DRG |     |     |     |     |
Cellstateprogressiontowardschronicpainanddriving
| Zhangetal.11 | scRNA-seq(10×) | GSE216039 | DRG mechanism |     |     |     |     |
| ------------ | -------------- | --------- | ------------- | --- | --- | --- | --- |
Sharmaetal.12 scRNA-seq(10×) GSE139088 DRG Tobetterunderstandtheprogressionofcellstatechangesinsensory
|                 |                      |           | neurons during | chronic pain, | we used | the iPainDRG dataset, | as it |
| --------------- | -------------------- | --------- | -------------- | ------------- | ------- | --------------------- | ----- |
| Parpaiteetal.13 | scRNA-seq(SS2/Patch) | GSE168032 | DRG            |               |         |                       |       |
includesmorepainmodelsthaniPainTGandcoversthewhole-time
| Techameena_Multi | snMulti-omics(10×) | GSE253345 | DRG |     |     |     |     |
| ---------------- | ------------------ | --------- | --- | --- | --- | --- | --- |
chronification.
Techameena_SS3_DRG snRNA-seq(SS3) GSE253345 DRG course of pain Indeed, all pain models used in the
datasetareknowntodevelopwithin1–3days,peakat2–3weeks,and
| Yangetal.14 | snATAC-seq(10×) | GSE197289 | TG  |     |     |     |     |
| ----------- | --------------- | --------- | --- | --- | --- | --- | --- |
persistforweeksthereafter21.Therefore,wechosetocovertheanalysis
| Yangetal.14 | snRNA-seq(10×/inDrops) | GSE197289 | TG  |     |     |     |     |
| ----------- | ---------------------- | --------- | --- | --- | --- | --- | --- |
ofthestudyupto28dayspost-injury,wherethepainischronicand
Jiaetal.15 scRNA-seq(BD) GSE213105 TG wellestablished,andintheatlas,severalmodelsshare28-daytime-
Liuetal.17 scRNA-seq(BD) GSE186421 TG pointspresumablyreinforcingtheanalysis.UsingiPainDRG,wefurther
Nguyenetal.16 isolatedandre-clusteredneuronsfromthenociceptivelineageinDRG,
|     | scRNA-seq(DropSeq) | GSE101984 | TG  |     |     |     |     |
| --- | ------------------ | --------- | --- | --- | --- | --- | --- |
Techameena_SS3_TG snRNA-seq(SS3) GSE253345 TG thenvisualizedwithUniformManifoldApproximationandProjection
(UMAP)toexaminethemolecularchangesfollowinginjury(Fig.2a–d;
SupplementaryFig.4a).
ofasubsetofnociceptorcellsasa common mechanismacrossthe Weobservedthattheneuronsdistributeinapatternthatreflects
variousrodentpainmodels,aswellasinhumanswithchronicpain. dynamicsbasedontheirexperimentaltimepointandconnectionsto
Our data further reveal that treatment with senolytic compounds naïve or injury states (Fig. 2b–d and Supplementary Fig 4a). In the
rescues hyperalgesia and allodynia associated with chronic pain in UMAPvisualization,neuronsatanaïve(0day)statearelocatedatthe
mice,demonstrating significanttherapeutic potential and a rolefor periphery,whileneuronspost-injurybegintoshifttowardthecenter.
the senescence process in chronic pain disorders independent By28days,thisphenotypereversed,andmostneuronsreturnedtothe
ofaging. periphery of the graph (Fig. 2d). To investigate these molecular
|     |     |     | changes further, | we classified | the generated | Leiden clusters | where |
| --- | --- | --- | ---------------- | ------------- | ------------- | --------------- | ----- |
Results those spatially distinct areas were classified into “woPain” (without
CreationofiPain,asomatosensoryatlasthatcaptureschronic pain)and“wPain”(withpain)macrostatesbasedontheiralignment
paindevelopment with the “Reference” state (naïve and sham conditions) or not,
In recent years, numerous efforts have been made to generate sc/ respectively(Fig.2c).Differentialexpressionanalysisconfirmedthat
the“wPain”categorywasassociatedwithupregulatedgenesrelatedto
snRNA-seqdatasetsofthemouseDRGandTGindiversemodelsof
chronicpain(Fig.1;SupplementaryData1).Thesedatasetsofferdif- axon regeneration and axon guidance, suggesting a regenerative
ferentsamplingtimepointsandpainmodelsatvariousstagesofpro- molecularprogramfollowinginjury,aspreviouslyreported22,23(Sup-
gression,providingtheopportunitytocreatecomprehensiveatlases. plementaryData4).
However,thelackofalignmentamongtheuniquegenesandmole- Importantly, the “wPain” and “woPain” macrostates could be
culesidentifiedineachdatasetduetotheuseofdifferentisolation furtherbrokendownintomicrostatestorefinecellprogressionover
methods and sequencing technologies can be a challenge for inte- time. These microstates, combined with injury timepoints, were
grationofdifferentdatasets.Toovercomethis,wehaveusedvaria- namedReference,Moving,Pain,Recovery,andLastingPain(Fig.2e).
tional autoencoder (VAE)-based integration models like scANVI18, TheReferencestate(timepoint0) representsuninjured cells,natu-
MULTIVI19,andscGLUE20(Fig.1;SupplementaryFig.1;Supplementary rally within “woPain”. The Pain state represents the neurons in
Fig. 2; Supplementary Fig. 3), which can effectively harmonize the “wPain”excludingtimepoint28days.Cellsin“wPain”at28dayspost-
datasets,controlforbatchcorrectionwhileconservingthebiological injurywerelabeledasbeingintheLastingPainstate.Remainingcells
informationtocapturetheentirespectrumofmoleculardynamicsand at post-injury timepoints but exhibited in “woPain” were further
diversityassociatedwithpainchronicityintheDRGandTGindifferent distinguished:theearlyphaseofpaindevelopment(upto1.5days)as
Moving,andthelaterphase(1.5–28days)asRecovery.Thiscategor-
chronicpainmodelsandatdifferenttimepoints(Fig.1b,f;andSup-
izationwasbasedontheobservationthatallcellswereinthe“wPain”
plementaryFig.3).TheiPainDRGatlas,whichintegrates191,798cells
from7sources(in-housegenerate:4468cellsfrommultiomeand625 macrostateatthe1.5-daytimepoint,while“woPain”statecellswere
cells from Smart-seq3), represents a comprehensive resource for seen both before and after. Therefore, cells in “woPain” prior to
understandingthemoleculardynamicsinsomatosensoryneuronsin 1.5dayswereassumedtobeMovingtowardPain, whilecells after
response to injury and the progression of pain chronification, with wereinRecoveryfromPain.
RNAandATACinformationprovidedforeachsinglecell(multiomic Importantly,thedefinedmicrostateswereunbiasedlyrecovered
velocity24
datasetallowfortheuseofMultiVIwithATACimputationtoallcells as pain dynamics states using RNA (computed from
eventocellsthatdidnotoriginallyprovideATACmodality,Supple- CytoTrace25 score) (Fig. 2e and Supplementary Fig. 4b) and PAGA
mentaryFig.2aforworkflow,SupplementaryFig.3aforatlascontent). graph analysis26 (Supplementary Fig. 4c). We also performed Gen-
Of note, the combination of all these modalities allows the use of eralizedPerronCluster-ClusterAnalysis(GPCCA)usingRNAvelocity
integrationmethodscompatiblewiththeimputationofmissinggenes, transitionmatrixandobservedahighdegreeofalignmentwhenwe
thereforeincreasing the gene coverage. Similarly,the iPainTG atlas, color-codedtheGPCCAresultsbyourowndefinedstates.Notethat
which integrates 87,838 cells from five diverse sources (in-house thisanalysiswasperformedforeachnociceptorsubtypewithsimilar
generated:124cellsfromSmart-seq3),providesinsightsintotheTG’s
|     |     |     | results(SupplementaryFig.4d).Altogetherthese |     |     | resultsunbiasedly |     |
| --- | --- | --- | -------------------------------------------- | --- | --- | ----------------- | --- |
responsetovariouspainconditions(unlikeiniPainDRG,noteverycell indicatethatthenociceptorscaptured intheatlasdynamicallypro-
in iPainTG has ATAC modality, Supplementary Fig. 2b and gressbetweendifferentmicrostatesinchronicpainmodels.
2
| NatureCommunications|(        2024)1  | 5:8585  |     |     |     |     |     |     |
| ------------------------------------- | ------- | --- | --- | --- | --- | --- | --- |

Article https://doi.org/10.1038/s41467-024-52052-8
We therefore extracted the driver genes within nociceptors (Supplementary Data 5), with dynamic activity along the CytoTrace
responsible for the microstates transition and performed cell-cell pseudotime.Sox11wasidentifiedasthesoletranscriptionfactor(TF)
communication analysisto comprehend the originof cellular chan- thatconsistentlyrankedamongthetopfivedrivergenesinallnoci-
gescenteringonthecommunicationbetweennociceptors,immune ceptorsubtypes(Fig.2fandSupplementaryData5).WeusedSCENIC
cells,andsatelliteglialcells.Forthedrivergeneswithinnociceptors, to identify the regulons associated with the molecular programs
the analysis based on the terminal states revealed that many responsibleforcontrollingthedynamiccellstatetransitionofnoci-
genes belonged to the “regeneration-associated genes” RAGs22,23 ceptorsandcombineditwithananalysisofATACpeaks’accessibility
NatureCommunications|( 2024)1 5:8585 3

Article https://doi.org/10.1038/s41467-024-52052-8
Fig.1|iPain:anintegratedatlasofsomatosensorychangesacrossdiverse datasources,datamodalities,andintegrationmodelsappliedtoconstructiPainTG.
neuropathicpainmodels.aAschematicrepresentingthedatasources,data fAschematictovisualizevarioustypesofinjurymodelsandtimepointsincludedin
modalities,andintegrationmodelsappliedtoconstructiPainDRG.bAschematicto iPainTG.gUMAPplotsofiPainTGindicatingvariousdatasetsfromdifferentsour-
visualizevarioustypesofinjurymodelsandtimepointsincludediniPainDRG. ces(left),andwithdatafromourlabhighlighted(right).hLeft,aUMAPplotof
cUMAPplotsofiPainDRGindicatingvariousdatasetsfromdifferentsources(left), iPainTGatlascoloredby18differentcelltypespredictedfromscANVImodeland
andwithdatafromourlabhighlighted(right).dLeft,aUMAPplotofofiPainDRG celltypeswerecolor-codedasseeninadotplotontheright.Right,adotplot
atlascoloredby18differentcelltypespredictedfromthescANVImodel,andcell representingthetopgenemarkersforeachcelltype.fMouseheadandTG
typeswerecolor-codedasseeninadotplotontheright.Right,adotplotrepre- iconswerecreatedwithBioRender.comreleasedunderaCreativeCommons
sentingthetop3genemarkersforeachcelltype.eAschematicrepresentingthe Attribution-NonCommercial-NoDerivs4.0Internationallicense.
afterinjury(Fig.2gandSupplementaryFig.4e,f).Identifiedregulons Upon evaluating this with the CytoTrace score which demon-
includedAtf3,Jun,andSox11.Particularly,Sox11regulonactivitywas stratedalowerpotentialforcellplasticityafterinjuryinasubsetof
foundtoincreaseaspseudotimeprogressedandremainedelevatedin nociceptors (Supplementary Fig. 4b), we formulated a hypothesis
the Lasting Pain state, in contrast to Atf3 and Jun regulons, which suggesting thatthe persistenceof pain inthe chronic injury model
exhibitedaninitialincreaseinactivityfollowedbyadecline(Supple- might be attributed to the persistence of injury-induced senescent
mentaryFig.5a–f).ThissuggestedthatSOX11isapotentialdrivergene cells which are unable to reverse their phenotype to the Reference
forthedevelopmentandmaintenanceofneuropathicpain,afinding state. To test this hypothesis, we initially identified senescent cells
thatwasrecentlyconfirmedinvivo27,furthersupportingtherobust- among the nociceptive lineage cells by computing a gene module
nessofouranalysis. scorebasedonthegeneslistedinSenMayo.Upontheevaluationofthe
Todeciphercell-cellcommunicationpatterns(Fig.2h),wecom- score,weobservedthattheSenMayoz-scoreincreasedineverytypeof
binedallcelltypes,includingnon-neuronalcells,andemployedtensor neuropathicpainmodelwhencomparedtothecontrol(Fig.3c).Sta-
decomposition28(Fig.2h,i;SupplementaryFig.4g;andSupplementary tisticaltestingoftheSenMayoz-scorerevealedahighenrichmentof
Data6).Thismethodextractsmulticellulargeneexpressionpatterns senescentcellularcharacteristicswithinnociceptorsfollowinginjury
that vary across different cell types, pain models (contexts), and inallpainmodelsexceptPaclitaxel(Fig.3c),acrossthedynamicstates
timepointstounbiasedlyidentifygroupsofmolecularligand-receptor (Fig.3d)andforallnociceptorssubtypes,regardlessofthebiological
pairsinvolvedincell-to-cellinteractions.Inouranalysis,thesegroups, sexes (Fig. 3e). Additionally, the SenMayo z-score was found to be
alsocalled“Factors”,capturehowmolecularchangesinnociceptors significantlylowerintheRecoverystatewhencomparedtothePain
are related to interactions with immune and satellite glial cells in andLastingPainstates(Fig.3d).Interestingly,everysubtypeofthe
Referenceandnon-Reference(Moving,Pain,Recovery,andLastingPain) nociceptivelineagecellsexhibitedtheincreaseoftheSenMayoz-score
states (Supplementary Fig. 4g). Six Factors were revealed, amongst whenwecomparedthePainstatetoReferencestate.Wethenverified
whichFactor3exhibitedthegreatestchangesbetweenReferenceand thetimecourseofsenescencedevelopmentinsilico(Fig.3f)andin
non-Reference conditions while affecting all pain models that are vivobydetectingtheSenescence-AssociatedBeta-galactosidase(SA-β-
included in the iPainDRG (Supplementary Fig. 4g). We, therefore, Gal)staininginDRGafternerveinjury(CCI,Fig.3g,h).Weidentifieda
conductedageneenrichmentanalysisusingPROGENypathwayson senescent phenotype in a subset of nociceptors, which were char-
thereceptor-ligandpairscharacterizingFactor3tounderstandtheir acterizedbyhighexpressionoftheneuronalnucleimarker(NeuN)and
biologicalsignificance.Thep53pathwaywasthemostenrichedpath- theirsmallersize(Fig.3i).Furthermore,theinjurywasaccompaniedby
wayforthisFactor,underlyingupregulationofthep53pathwayduring anincreasednuclearexpressionofthesenescencemarkerp21starting
painprogression(Fig.2j).Notably,thedistributionofthep53,p21,and from day 7 post-injury34 (Supplementary Fig. 5g, h). These in vivo
p16 tumor suppressor genes within this “Factor” correlated with findings support the reliability of using the SenMayo z-score as a
expressionofthesegenespost-injuryconditionsinouratlas(Supple- hallmarkofsenescenceinourinsilicoanalysis.
mentaryFig.5g).Thepresenceofthesegenestogetherstronglysug- ForTG,theatlascoveredlimitedtimepointsforproperanalysis.
gestedaprocessofcellularsenescenceduringpainchronification29–31. We, therefore, assessed the SenMayo z-score in a pain model of
compressionofthetrigeminalrootentryzone(TREZ)oftheTGnerve,
Developmentandpersistenceofpainandsenescenceof modelingexcruciatingpaindisorderssuchastrigeminalneuralgia(TN,
pain-sensingneurons also called the suicidal disease)35, and cluster headache (CH, a tri-
Theconceptofcellularsenescencewasinitiallydiscoveredindividing geminalautonomiccephalalgia)whicharebothassociatedwithnerve
cellsbutlaterextendedtoincludepost-mitoticcells,correlatingthis compressionbybloodvessels(calledmicrovascularcompression)36.
processwithaginginvarioustissues.Cellularsenescenceinvolvescells Todothis,weusedthebulkRNA-seqdataset37fromtheratmodelwith
alteringtheircharacteristicphenotypeinresponsetostress,resulting TNtocomputethescore.WeidentifiedaclearincreaseintheSenMayo
in adistinctsecretoryphenotype,calledtheSenescenceAssociated z-scorecomparedtocontrolconditionssuggestingthatboththeDRG
Secretory Phenotype (SASP), and characterized by the release of andTGusesenescenceasapainchronificationmechanism(Fig.3j).
inflammatorycytokines,growthfactors,andproteases.SASPoperates WethenassessedtheSenMayoz-scoreinhumansamplesfocus-
throughdiversemechanisms,ofteninvolvingautocrineorparacrine ingontheDRG(TGdatasetor samplesfrompain sufferersare not
signaling.Tofacilitatestandardizedandstreamlinedsenescenceana- currentlyavailableonlinenorinbiobank).SenMayoz-scorewasele-
lysis,theMayoClinichasrecentlyintroducedtheSenMayogeneset32, vated in DRG from human patients diagnosed with chronic pain
encompassinganextensivecollectionofSASP-relatedgenes(Supple- (Fig.4a)irrespectiveoftheirbiologicalage(Fig.4b,c),inanonline
mentaryData7).Usingthismethod,weidentifiedSASP-positivecells dataset38.Deconvolutionintocelltypesusinghumanreferencemap39
byselectingthosewithinthetop10percentoftheSenMayoz-score (Fig.4d–f;SupplementaryFig.5i)showedthatthenociceptors(Fig.4g)
(Fig.3a,b)andhighlightedtheminthescatterplot,depictingGenAge haveaSenMayoz-scoresignificantlyelevatedinchronicpaincondi-
score(genesetassociatedwithaginginmodelorganisms)inrelation tion,furtheremphasizingtheinvolvementofsenescenceinnocicep-
to CellAge score (gene set associated with aging in human cells)33 torsinhumanwithchronicpain.Similarresultswereobservedwhen
(Fig.3a,bandSupplementaryData8).Thisanalysisdemonstratedthat theSenMayoz-scorewas appliedtoDRGbulk-seq40extractedfrom
cellsaffected by injuryexhibited advancementin both GenAge and patientswithdiabetesneuropathy(Fig.4h,i).Theseresultsinhumans
CellAgecomparedtonaïvecells. supportthetranslationalvalueofourfindings.Importantlyinmice,the
NatureCommunications|( 2024)1 5:8585 4

Article https://doi.org/10.1038/s41467-024-52052-8
senescencescorewassignificantlyhigherinallpainmodels,regardless targetingsenescencecells,knownassenolyticagents,havebeenwell
ofthebiologicalsex(Fig.3c,e). characterized and are used already in preclinical and clinical trials.
Senolyticdrugscapitalizeonsenescent-cellanti-apoptoticpathways
Targetingsenescentcellstreatschronicpain.Whilethepresenceof (SCAPs)41.Disruptingtheexpressionofproteinswithinthesepathways
senescent neurons in peripheral somatosensory neurons was unex- canleadtotheselectiveeliminationofsenescentcellswhilepreserving
pected in the context of chronic pain independent of aging, drugs neighboringcellsandtissuephysiology.Thesenolyticagentsusedin
NatureCommunications|( 2024)1 5:8585 5

Article https://doi.org/10.1038/s41467-024-52052-8
Fig.2|Temporalmoleculardynamicsofnociceptorsandpainstatesduring pseudotime.gHeatmapsshowingthechromatinaccessibilityofpeakscorre-
neuropathicpain.aAUMAPplotofthenociceptivelineagecellsfromiPainDRG spondingtothepromoterregionofAtf3,Sox11,Flrt3genesasactualinjurytime-
coloredbytheirrespectivesubtypes.bAUMAPplotofthenociceptivelineagecells pointsprogressed.TheATACpeakregionsareshownonthelowerright.hA
highlightedbyLeidenclusters.cAUMAPplotofthenociceptivelineagecells schematicofcell-to-cellcommunicationbetweennociceptorsandimmunecells.
highlightedbythepainstateidentifiedbyaggregationofLeidenclusters.dUMAP iChorddiagramindicatingthecommunicationintensitybetweensubtypesof
plotsofthenociceptivelineagecellshighlightedinpinkbyactualinjurytimepoints. nociceptors,immunecells,andsatellitegliaatdifferentinjurytimepoints.jAbar
eUMAPplotsofthenociceptivelineagecellscoloredbydifferentstatesinthepain plotofpathwaysbeingenrichedinFactor3,identifiedtobethefactorwiththe
dynamicswithembeddedvelocityarrowsfromCytoTrace.fHeatmapsrepresent- mostdifferencesintermsofcontextloadingbetweenReferenceandnon-Reference
ingtheexpressionoftop5drivergenespernociceptivesubtypesasafunctionof (Moving,Pain,Recovery,andLastingcombined)cells.
thisstudyincludedthebioavailablesmallmoleculeinhibitorsofB-cell behaviors in a mouse model of chronic pain, suggesting a role of
lymphoma-2protein(Bcl-2)familyproteins,suchasNavitoclax(ABT- senescentcellsinsustaininganeuropathicpainphenotype.Ourdata
263),Venetoclax,andproteolysistargetingchimera(PROTAC)com- providefunctionalevidencefortheroleofsenescentcellsinthepro-
pound,PROTACBcl-XLdegrader,thelatteraimingatcontrollingthe gressionandpersistenceofchronicpaininasex-independentmanner.
linkedsideeffectsthatthisclassofmoleculeshasonthrombocytes Thisstudyrevealsadynamic“intrinsic”shiftingeneexpression
counts. patterns in time following peripheral nerve injury. A common tran-
Totestthehypothesisthattargetingsenescentcellscouldsup- scriptomic signature across all subtypes is Sox11. SOX11 is a tran-
presshypersensitivitytopaininachronicpainmodel,wegavethese scription factor involved in nervous system development and in
varioussenolyticagentsorvehiclestomicewhichhavebeensubjected neurogenesisin adults whereit induces the expression ofneuronal
toChronicConstrictionInjury(CCI)anddevelopedhyperalgesiaand traits42,43.Thissuggestsaroleintheregenerationprocess.However,
allodyniabyday7(Fig.5a).Remarkably,micetreatedwithsenolytic whiletheexpressionoftheknownregeneration-associatedgeneslike
agents exhibited significantly less or no signs of mechanical pain 4 Atf3andJunincreasesatearlytimepointspost-injury,theydecrease
weekspostnerveinjurywhencomparedwithbaselineorvehicleatthe later. In contrast, Sox11 remains elevated at a later timepoint, sug-
same timepoint (Fig. 5b). The drugs however did not significantly gesting a different role than regeneration which would align with
impactthermalsensationduringthetimeframeoftheexperimentorat persistentpaindevelopmentandmaintenance.Interestingly,inrela-
theadministereddoses.Therestorationofnormalpainbehaviorwas tiontochronicpainaroleofSox11waspreviouslypredictedusingthe
associated with the selective removal of at least 50% of SA-β- neuropathicpainmodelofsparednerveinjury44,andinasex-stratified
galactosidase positive cells, on average, among the small diameter, genome-wideassociationstudyofMultisiteChronicPain(MCP),SOX11
peripherin-positivesneuronsforalldrugs(Fig.5c,d).Ultimately,the wasshowntobeassociatedwithMCPinfemales44.Finally,itisnow
removed cells represent a small fraction of the total peripherin- reportedusinglossandgainoffunctionthatSOX11hasanimportant
positiveneurons.Moreover,bodyweightremainedunchanged(Sup- role in the initiation and maintenance of neuropathic pain25. Those
plementaryFig.5j)throughouttheexperimentandbloodcountswere findingsfurthersupporttheresourcefulnessofiPain.Moreover,our
similar between the drug-treated and control groups (Fig. 5e), indi- approachandourworkflowdifferfromacross-speciesatlas45,which
cating thatthesenolytic compoundsdid notshow obvious adverse alsointegratesdatafrommultiplesources,butfocusesonaddressing
systemic effects and did not significantly affect the thrombocytes molecularconservationacrossdifferentspecies.Incontrast,iPainis
counts(Fig.5e).Importantly,asacontroltoassessthespecificroleof specificallytailoredtochartingthetrajectoryofchronicpaindevel-
thesenolyticcompoundsonpain-sensingneuronsandtocontrolfor opmentinatargetedmanner.
off-targeteffects,wetestedthemiceforanxietybalanceandmotor Previous research has linked cellular senescence with chronic
skills(Fig.5f,g,andSupplementaryFig.5k,l).Nosignificantdifference pain, specifically in the spinal cord46,47, presumably as a secondary
wasobservedwhencomparingthedrug-treatedmicetothecontrol processoccurringseveralmonthsafterinjuryandexhibitingamale-
conditions. These results provide a more comprehensive under- specificeffect46incertaincases.Nevertheless,usingsenolyticstotreat
standingoftheeffectsofthesenolyticcompoundshighlightingtheir the spinalcordlocally did not provide sustained relief from neuro-
selective impact on mechanical hypersensitivity without affecting pathicpain,indicatingthatthisapproachdidnotaddresstheprimary
othersensorymodalitiesorgeneralhealthparameters. mechanismunderlyingneuropathicpaininthestudiedmodel.How-
Togetherthesedataindicatethatasenescenceprocessoccursina ever,ourstudyfoundthattheconnectionbetweencellularsenescence
subset of nociceptive neurons in various chronic pain models and andchronicpainbeginsjustaftertheacutephase,andislinkedtothe
participatesinthepersistenceofthepainstateandthattargetingthese onsetofneuropathic/chronicpain.Weobservedsenescenceinnoci-
senescentcellsrepresentsapromisingtreatmentoptionforpatients ceptorsacrossvariousmodelsofperipheralnerveinjuryandinflam-
affectedwithchronicpain. mation, as well as in the TG for the TREZ compression model.
Furthermore,wediscoveredthatthiseffectisnotsex-specific;both
Discussion maleandfemaleanimalsshowedsimilarlevelsofcellularsenescence
The extensive prevalence of chronic pain in the human population innociceptors.Thissuggestsanunderlyingmechanismdifferentfrom
alignswiththepressingneedtodevelopnovelapproachestomedical thosepreviouslyreported.Lastly,whileourstudyfocusesonyoung
treatment.Amajorlimitationtoprogressinthisfieldhasbeenalackof andmiddle-agedadultanimals,thismechanismmightalsofunctionor
comprehensive understanding of the overall phenotypic alterations even intensify in older individuals in which the development of a
thatunderliethedysfunctionofnociceptiveneuronsfollowingnerve senescentphenotypeinnociceptorsfollowingnerveinjuryorincon-
injury, leading to the onset of the chronic pain state. Our study trolconditionsmightbemoreeasilyinduced48.
introducesanintegratedpainatlas(iPain)forsystematicallyexploring Inconclusion,oursingle-celltranscriptomicatlasescouldprovide
the trajectory of chronic pain development through the analysis of substantialadvances in drug discovery efforts bydefining cellsand
single-cellomicsdatafromvarioussources.Asalientdiscoveryfrom pathwaysrelevanttopaindisordersfollowingperipheralnerveinjury.
ourresearchistheconsistentinductionofasenescencephenotypein Our discovery suggests an alternative therapeutic approach to the
thetranscriptomeofasubsetofsomatosensoryneurons,principallyin currentlylimitedoptionsforchronicpaintreatment,ahypothesisthat
nociceptors, following peripheral nerve injury, a phenomenon has been validated in mice with translational potential for human
observed in both rodents and human datasets. Pharmacologically subjects according to in silicoanalysisof chronic pain patients and
targeting senescent cells further proved effective in rescuing pain patientswithdiabetespainfulneuropathy.Theselectiveremovalofthe
NatureCommunications|( 2024)1 5:8585 6

Article https://doi.org/10.1038/s41467-024-52052-8
Fig.3|Senescenceofnociceptorsinpainmodelsinmicewithchronicpain. 100µm.hAbarplotofmeanvalues±SEMrepresentingthequantificationofSA-β-
a,bScatterplotsofnociceptivelineagecells.Cellswereplottedbasedontheir Galactosidaseareaininjuredconditionwithstatisticalleveltodenotethesig-
CellAge(x-axis)andGenAge(y-axis)scoresandcoloredbySenMayoz-score(a)and nificantlevelofthepositiveareaineachtimepointafterinjurywhencomparedto
SASPidentity(b).cBoxplotscomparingtheSenMayoz-scoreofnociceptiveline- theday0(nsP>0.05;*P<0.05;0.876,0.0465,0.0259,0.0129weretheP-valuesof
agecellsfromdifferentneuropathicpainmodelsandcontrol.dBoxplotsofmul- D1,D7,D14,andD28respectively.Thetestwasdonewithone-sidedMann–Whitney
tiplecomparisonscomparingSenMayoz-scoreofnociceptivelineagecellsfrom testU).Thequantificationwasderivedfrom12DRGsamples(L4-L6)of4animalsat
differentstatesofpaindynamicswiththeReferencestate(nsP>0.05;***P<0.001, eachtimepoint,exceptforD14wheretherewere10DRGsamples.iStainingimages
Mann–WhitneyU).Thestatisticwasderivedfrom18,409cellsinReference;7808 representingtheco-stainingofSA-β-GalactosidaseandNeuNwhenmerged.jLeft,
cellsinMoving;15,893cellsinPain;28,199cellsinRecovery;and654cellsinLasting. schemerepresentingamodeloftrigeminalneuralgia(TN)inrats,byTrigeminal
eBoxplotsofmultiplecomparisonscomparingSenMayoz-scoreofdifferentsub- EntryZone(TREZ)compression.Right,AboxplotrepresentingtheSenMayo
typesofthenociceptivelineagecellsfromReferenceandPainstates.Fromtopto z-scorebetweenshamandTNconditionsinTGtissueRNA-seqdatafromTaoetal.37
bottom,cellsfrombothsexestogether;cellsfromfemalemice;andcellsfrommale (n=2samplesfromshamandn=3samplesfromTN).jSchemeontheleftwas
mice(*P<0.05,Mann–WhitneyU).fBarplotrepresentingtheincreasedproportion createdwithBioRender.comreleasedunderaCreativeCommonsAttribution-
ofSASPcellsasinjurytimeprogressed.gSA-β-Galactosidasestainingimagesof NonCommercial-NoDerivs4.0Internationallicense.Sourcedataareprovidedasa
DRGbeforeandafterinjuryinmicewithCCImodel,scalebardenotesalengthof SourceDatafile.
fewdysfunctional,senescentneuronsmaybeaworthwhiletrade-offto senescent cells through apoptosis induction is a straightforward
achieve lasting well-being for the patient, especially in the case of method,andtherearevariousagentsdemonstratingtheeffectiveness
excruciatingpainconditionswithlimitedoptions,suchasTNandCH ofsenolyticagentsinvivo,aswellasinclinicaltrials39.Therefore,the
whicharelinkedtotrigeminalnervecompression36. use of senolytics represents a promising approach in managing
Thecurrentclinicaldevelopmentofseveralsenolyticcompounds, chronicpain.
includingthoseusedinthisstudy,foranti-agingandcancer-related
diseases,supportsthestrategyoftargetingsenescencetotreatper- Methods
sistentpaininhumans.Thisprogresssuggeststhesesenolyticcom- The basic analysis of the data was done with the functions from
pounds could soon be repurposed for treating chronic pain and Scanpy49package(v1.9.3)ofPython3(v3.10.10)anddefaultparameters
headache disorders resulting from nerve tissue injury. Targeting accordingtoScanpypipelineunlessotherwisespecified.
NatureCommunications|( 2024)1 5:8585 7

Article https://doi.org/10.1038/s41467-024-52052-8
Fig.4|Senescenceinhumanswithchronicpainanddiabeticpainfulneuro- knownpainconditions.gAboxplotcomparingtheSenMayoz-scorefromhuman
pathy.aAschemedepictinghumansamplenomenclature(NnoPain,PPain).bA nociceptivelineagecellsofdifferentpainstatesafterbulkdeconvolutiontosingle-
boxplotshowingthattheaverageagebetweenpatientswithpainwasnotsig- cellwithasteriskstodenotethelevelofsignificance(***P=3.545×10−91,one-sided
nificantlydifferentfrompatientswithoutpain(nsP>0.05,one-sidedt-test).cA Mann–WhitneyU)Therewere7418neuronsfromcontrolgroupand6198neurons
boxplotrepresentingtheSenMayoz-scorewithindicatedstatisticalsignificancefor frompatientswithpain.hBoxplotshowingthattheaverageagesbetweenpatients
thehigheraveragescoreinpatientswithpain(*P=0.0415,one-sidedt-test).For withdiabeticpainfulneuropathyandthecontrolcohortwerenotsignificantly
bandcn=17DRGsamplesofthenoPain(control)cohortandn=33DRGsamples different(nsP>0.05,one-sidedt-test).iBoxplotrepresentingtheSenMayoz-score
ofpatientsinthePaingroup.dLeft,aUMAPplotofhDRGsingle-nucleiRNA withindicatedstatisticalsignificanceforthehigheraveragescoreinpatientswith
sequencingfromJungetal.39,cellsusedtocreatethereferencecellsusedfor diabeticpain(*P=0.00952,one-sidedt-test).Bonferronicorrectionwasperformed
deconvolutionofbulkintosinglecells.Right,aUMAPplotofdeconvolvedcells toadjustformultiplehypothesistestingonthisfigurewhenappropriatewitha
fromhDRGbulkRNA-seqcoloredbydifferentcelltypes.eAheatmapplotrepre- family-wiseerrorrateof0.05.Boxplotsindicatethemedianatthecenter,upper
sentingtheSpearmancorrelationbetweenthecelltypesofthereferencecount andlowerquartilesattheboundsofthebox,whiskersareatminimaandmaxima.
matrix(_ref)andthereconstructedcountmatrixfromdeconvolution(_decon).fA SourcedataareprovidedasaSourceDatafile.
UMAPplotofdeconvolvedcellsfromhDRGbulkRNA-seqcoloredbydifferent
Mice compoundorvehiclecontrol(10%DMSOincornoil)wasadministered
Cohortsofadultmiceofbothbiologicalsexes,agedfrom8to12weeks byoralgavageoncedailyforeither10consecutivedays(Navitoclax
wereusedforsequencinginallthedifferentpublishedstudies5,9–13.Our CAS No. CAS. 923564-51-6 or Venetoclax CAS No. 1257044-40-8) or
sequencing data on TG and DRG were obtained from mice aged onceweeklyfor2weeksPROTACBcl-xLdegrader(CASNo.2920415-
between8and12weeksusingtheSmart-seq3Xpress,10xmultiomic 08-1).
technologies,iniPainthesemicearereferredtoasyoung.Amiddle-
aged cohort (34–62 weeks) was processed using 10x multiomic FullbloodCount
sequencing,iniPainthesemicearereferredtoasaged.Foralldetails Mice were deeply anesthetized with isoflurane. The full blood was
onbiologicalsex,andthenumberofcellspertimepointsseetablesin takenfromtheheartsofthemiceandkeptinabloodcollectiontube
Fig.S2andtheCellxGene50iPain(iPain). (containingEDTA)forfurthertestingbyIDEXXBioAnalytics.
For the senescence kinetic and for the drug treatment experi-
ment,cohortsofmiceagedbetween17and27weeksofbothsexes(3 Chronicconstrictiveinjurymicemodel
malesand3femalespergroup)wereused. Chronicconstrictioninjuryofthesciaticnerve(CCI)hasbeenwidely
AllthemicewereonaC57BL/6backgroundandwerekeptundera describedwithminordifferencesinrodents51–53.Briefly,micewerefirst
12-hlight–darkcycle,at24°Cwithunlimitedfoodandwater.Allanimal anesthetizedwithisoflurane,andasmallincisionwasmadeatthemid-
care and experimental procedures were permitted by the Ethical thigh level on the right side. Ligatures (7–0 surgical silk) were tied
CommitteeonAnimalExperiments(StockholmNorthcommittee)and looselyaroundthesciaticnervewithapproximately0.5mmbetween
conductedaccordingtoTheSwedishAnimalAgency’sProvisionsand ligatures.Andthen,theskinwasclosedbya5–0silksuture.
Guidelines for Animals Experimentation recommendations. Ethical
permitnumbers9702-2018and17396-2022. Pain-relatedbehavioraltests
MechanicalsensitivitywasassessedbythevonFreytestinanup-down
Drugadministration testingparadigmaspreviouslydescribed54,55.Briefly,micewereplaced
The senolytic compounds were given orally, by gavage. The stock inglasscylindersona6×6mmwiremeshgridfloorandwereallowed
solutionwasdilutedas10%DMSOincornoilpriortoadministration. toacclimatefor20–60min.Theplantarsurfaceofthehindpawwas
The treatment starts seven days post CCI injury, the senolytic stimulatedwithaseriesofcalibratedmonofilaments(vonFreyhairs;
NatureCommunications|( 2024)1 5:8585 8

Article https://doi.org/10.1038/s41467-024-52052-8
Stoelting,IL)rangingbetween0.008and2gandwithdrawalorjerking CA,UnitedStates)waspreciselyaimedatthemiddleoftheplantar
ofthepawisrecordedasthepainthreshold.Miceweretested6times surfaceofthemicethroughtheglasssheet.Thelaserintensitywasset
oneachpawfollowingthetestingparadigm. to30%andacutofflatencyof20swassettoavoidtissuedamage.
ThermalsensitivitywasassessedbytheHargreavesthermalpaw Noxiousmechanicalsensitivitywasassessedbypinpricktestas
withdrawaltestaspreviouslydescribed56,57.Briefly,micewereplacedin previously described with minor modification58. Briefly, mice were
Plexiglaschambersontopofaglasssheetandwereallowedtoaccli- placedinPlexiglaschambersontopofaglasssheetandwereallowed
matefor20–60min.Athermalstimulator(IITCInc.,WoodlandHills, toacclimatefor20–60min.A25-gaugeneedleconnectedwitha1g
NatureCommunications|( 2024)1 5:8585 9

Article https://doi.org/10.1038/s41467-024-52052-8
Fig.5|Senolyticcompoundsprovidepainreliefinamousemodelof treatmentconditions(nsP>0.05;*P<0.05,one-sidedt-test;Veh10andVeh2were
neuropathicpain.aSchemeofchronicconstrictioninjury(CCI)painmodeland comparedwithNT;ABTandVenwerecomparedwithVeh10;PBcl-xLwascom-
experimentaltimelinefortreatmentandbehaviortests.bUpper,linegraphs paredwithVeh2).ThequantificationwasderivedfromDRG(L4)from4mice,
representingvonFreywithdrawalthresholdatbaseline(“B”)anddifferenttime- exceptthevehiclegroupwhereDRG(L4)from6micewereused.eBarplotsfor
pointsafterinjuryfordifferenttreatmentconditionsonipsilateral(toppanel)and wholebloodcountoferythrocytesandthrombocytesforeachtreatmentcondition
contralateralside(bottompanel)(nsP>0.05;*P<0.05;***P<0.001,two-sided (nsP>0.05;*P<0.05,two-sidedt-test).fBarplotsdepictingresultsfromthe
pairedt-test).Lower,barplotscomparingpinprickscorefromthesameanimalsat RotaRodtestforeachtreatmentconditionbutABT-263(nottested)(nsP>0.05,
baseline(“B”,beforeinjury)withthepinprickscoreatdifferenttreatmentcondi- two-sidedt-test).gBarplotsdepictingresultsfromthebeamwalktest(width
tionsatday28afterinjury(CCI28).NotethatfortheABT-263treatment,thecontrol 11mm)foreachtreatmentconditionbutABT-263(nottested)(nsP>0.05,two-
conditionisvehicle28dayspostCCI(“VCCI28”)and(nsP>0.05;*P<0.05; sidedt-test).6micewereemployedineachgroupforthebehaviortest,exceptthe
***P<0.001),two-sidedpairedt-test(comparingto“B”)ortwo-sidedunpairedt-test vehiclegroupwhere11micewereemployed.Bonferronicorrectionwasperformed
(comparingto“VCCI28”).cImagesofDRGtreatedwiththevehicleatCCIday28, toadjustformultiplehypothesistestingwhenappropriatewithafamily-wiseerror
stainedwithPeripherin(top)andSA-β-Galactosidase(bottom).Arrowsindicate rateof0.05.Allbarplotsandlinegraphsrepresentthemeanvalues±SEM.Noteon
somedouble-positiveneuronsforperipherinandSA-β-Galactosidaseasanexam- abbreviation,Uninj:Uninjured;NT:NoTreatment;Veh10:Vehicle(10dosesof
ple.dBarplotforstainingquantificationdepictingtheproportionofSA-β- DMSO);Veh2:Vehicle(2dosesofDMSO);ABT:ABT-263;Ven:Venetoclax;andPBcl-
GalactosidasepositivetoperipherinpositivecellsatCCIday28inthedifferent xL:ProtacBcl-xL.SourcedataareprovidedasaSourceDatafile.
filament(von Frey hairs; Stoelting,IL) wasapplied uniformlytothe function.7=traversesbeamnormallywithnomorethantwofootslips;
plantarsurfaceofthehindpawwithoutpenetratingtheskin.Ascore 6=traversesbeamsuccessfullyandusesaffectedlimbinmorethan
system was used according to the extent of the response. 0=no 50% of the steps; 5=traverses beam successfully and uses affected
response;1=move,lookaroundtoseewhathappened;2=briefquick limb in less than 50% of the steps; 4=traverses beam and places
liftorwithdrawalorremovalawayofhindpaw;3=briefquickshakes affectedlimbonhorizontalsurfaceatleastonce;3=traversesbeamby
of the hind paw, or jumps; 4=high frequency of shaking, licking, draggingaffectedlimbs;2=theanimalscannottraversebutwereable
flinching,orguarding.Miceweretested4timesoneachpawwitha to place limbs on horizontal surface and maintain balance; 1=the
waitingtimeof5min58,59. animalcannottraverseandwereunabletoputaffectedlimbonhor-
izontalsurface.
Anxietyandbalancemotorfunction-relatedbehavior Forrotarod,theequipmentfromUgoBasileS.R.L.model47,600
assessments wasusedwithastartspeedof4rpm/min,amaxspeedof40rpm,anda
Anxietywasassessedbytheopenfieldtest(OFT)andelevatedplus rampspeedof1.8min(20rpm/min).Micewereplacedontherotating
maze (EPM) tests60,61. For OFT, animals were placed in a roofless dowelsettominimumspeedandallowedtohabituatefor5minonthe
45×45cm square arena enclosed with 40cm walls and allowed to firsttrial.Atotalof8trialswereperformedforeachanimalwitharest
explorefor15minwhilebeingrecordedbyacamerasecuredonthe timeofatleast5minbetweeneachtrialinthehomecage.Thetimeand
ceiling. Tracking and analysis were done using the EthoVision XT final rpm of the mouse at falling or the first occurrence of passive
software where the arena was further partitioned into two zones: rotation (clinging to the dowel) were used as indicators of motor
center(squareareaof22.5×22.5cminthemiddleofthearena)and function.Thefirst2trialswereseenashabituationtrialsandthelast5
periphery(restofarenaclosetowalls).Theproportionoftimespentin trialsweretakenforanalysis.
thetwodifferentzoneswithrespecttothecenter-pointofeachanimal
wasusedasanindicatorofanxiety. Senescence-associatedβ-galactosidasestaining
ForEPM,animalswereplacedinaplus(+)shapedarenaelevated Miceweredeeplyeuthanizedwithisofluraneandperfusedwithpre-
at60cmfromthegroundandallowedtoexplorefor5minwhilebeing cooledPBS.L4-L6DRGswerequicklydissected,immediatelyfrozen,
recordedbyacamerasecuredontheceiling.Trackingandanalysis and then quickly imbedded inoptimalcutting temperature embed-
were done using the EthoVision XT software where the arena was dingmedium(OCT).TheSA-β-galactosidaseactivitywasdetectedby
partitionedaccordingtoitsdesign:twoclosedarmsoppositetoeach using a SA-β-galactosidase staining kit (Cell Signaling Technology,
otherthatareeach6×35cmenclosedby15cmwalls,twoopenarms #9860)atPH6.0accordingtothemanufacturer’sinstructionswith
oppositetoeachotherwith6×35cmwhichareallconnectedtoone minormodification. Briefly, DRG sections wererinsed twice by PBS
anotherbyasmall6x6cmcenterarea.Thetotaldistancetraveled,and beforefixation,followedbyx-gal(PH6.0)staining.4daysafterincu-
the proportion of time spent in the different types of zones with bation(at37°C),thestainingsolutionwasremoved,rinsedthreetimes
respecttothecenter-pointofeachanimalwereusedasindicatorsof withPBS,sealed,andthenimmediatelytakenimaging.
anxiety.
Motor coordination was assessed by beam walk and rotarod Immunostaining
tests62–65. For the beam walk test, each animal and some bedding The snap-frozen DRG tissues were collected as described above (in
materialwasfirstplacedfor2minforhabituationinsidethegoalbox, “Methods” section, SA-β-galactosidase staining section). The snap-
which is 12×12×12cm elevated to 64cm from the ground and frozenDRGtissuewaseitherfreshlysectionedandthenfixedinPFA
enclosedonallsidesexceptfortheentryside.Aroundbeamwitha overnightat4°C,orreusedfromSA-β-galactosidasestaining(double
diameterof11mm(Small)andalengthof105cmwereused.Thetest staining).DRGsectionswerewashedwithPBS,andpermeabilizedwith
beamwasplacedstraightwiththeendpointinfrontofthegoalbox 0.3%PBSTfor10min,followedbyincubationinblockingbuffer(PBS
parallel to the ground with start and finishlines defined for a total containing 0.25% Triton X-100 and 1% bovine serum albumin) for
lengthof80cminthemiddleofthebeam.Animalswerefirsthabi- 30min at room temperature (RT). And then, DRG sections were
tuated on a 20 mm beam until the ability to fully cross the beam incubatedwithprimaryantibody(dilutedinblockingbuffer)at4°C
withouthesitationwasdemonstrated.Atotalofthreetrialswereper- overnight.After3washeswithblockingbuffer,asecondaryantibody
formedonthe11mmbeam,withatleast1minrestbetweentrialsinthe (1:1000,dilutedinblockingbuffer)wasappliedfor1hatRT.Cellswere
goalbox.Eachtrialwasrecordedoncameraandthetimerequiredfor then incubated in DAPI solution (D212, Wako) for another 10min,
themousetocrossthebeamfromstarttofinishandtheusageofthe followedby3washeswithPBS.Imageswereobtainedwithafluores-
injured leg as a scoring system were used as indicators of motor cencemicroscopeorconfocalmicroscope.
NatureCommunications|( 2024)1 5:8585 10

Article https://doi.org/10.1038/s41467-024-52052-8
The following primary antibodies were used: anti-p21 antibody Preprocessingthelab-generateddata
(1:100, gift from Doctor Sylvain Peuget), anti-peripherin (1:200; DRG10xmultiomics.ThesamplesweresequencedonNovaSeq6000
ab39374,Abcam),anti-NeuN(1:200;MAB377,MerckMillipore). (NovaSeq Control Software 1.7.5/RTA v3.4.4) with a 50nt(Read1)
−8nt(Index1)−24nt(Index2)−49nt(Read2)(ATACpart)and28nt(Read1)
Imaging −10nt(Index1)−10nt(Index2)−90nt(Read2) (GEX part) setup using
Brightfield images were acquired using the Zeiss Axio Imager.Z2. ‘NovaSeqStandard’workflowin‘S2’modeflowcell.TheBcltoFastQ
ImageswereanalyzedwithImageJ(v1.52h)by(1)manualsegmenta- conversion was performed using bcl2fastq_v2.20.0.422 from the
tionofganglionwhileexcludinglargefibers;(2)generalisolationofthe CASAVA software suite. The quality scale used is Sanger/phred33/
blue stain with the Color Deconvolution plugin66,67 with the built-in Illumina1.8+.Thesequencedreadsofeachsamplewerealignedusing
BrilliantBluevector;(3)thresholdingbypixelintensityfrom5to185 CellRangerArcpipelineversion2.0.2tothemousegenome(mm10).
withLi’smethodand(4)positivestainidentificationbytheAnalyze After the alignment, the chromatin peaks from each sample were
Particlesfunction(sizeinclusionfrom400-Infinity).Identifiedpositive aggregatedtogethertoobtainacommonpeaksetwith“aggr”function
regionswererefinedmanuallybeforemeasurementoftheareawhich fromCellRangerArc.ThecountmatriceswereloadedintoPython3as
weresummedandnormalizedagainstthetotalareaofthesegmented AnnDataobjects.Thequalitycontrolwasdonebyremovingfeatures
DRGtodeterminethepercentagepositiveareaforeachDRG.Statis- thatweredetectedinlessthan3cells,andcellswithathenaturallog
ticalsignificancewascalculatedwiththeMann–WhitneyUtest. pseudocount(log1p)ofthenumberofgenesorpeakslessthan4and
morethan9wereremoved.Cellswithpercentmitochondrialgenesof
DRGdissociationandsingle-nucleiisolation51–53 morethan1.5andatotalUMIcountofmorethan20,000werealso
Miceweredeeplyeuthanizedbyisofluraneandperfusedwith4%pre- filteredout.
cooledPBS.L4-L6DRGswerecollectedat14daysafterCCIinjuryin
agedmiceorfromyoungmice(withoutinjury),andthenimmediately Smart-seq3DRG&TG.Thesequencedreadswerealignedusingthe
put on dry ice. Frozen tissues are stored at −80°C before nuclei zUMIspipelinewhichmakesuseoftheSTAR-SOLO70alignmenttool,
isolation. andthereferencegenomewasmouse(mm39).Afteralignment,the
Isolationofnucleifromfrozentissuewasperformedasdescribed countmatriceswereloadedintoPython3foranalysis.Furthermore,
bytheAllenInstituteforBrainScience68,69.Allstepswereperformedin thecountmatriceswerefilteredtoonlyyieldhigh-qualitycells.For
4°C.Briefly,tissueswerehomogenizedin2mlchilledhomogenization DRG,genesfoundinlessthan20cells,andcellswithlessthan1000
buffer(10mMTrispH8,250mMSucrose,25mMKCl,5mMMgCl2, geneswerefilteredout.ForTG,genesdetectedinlessthan3cells,and
0.1mMDTT,1×Proteaseinhibitorcocktail,0.2U/μlRNasinPlus,0.1% cellswithmorethan3percentofmitochondrialgenesandlessthan
Triton X-100), and filtered through 70µm and 30µm cell strainers. 2000detectedgeneswereremoved.
Nucleipelletswerecollectedby10min,900×gsuspension,andthen
resuspendedin250μlchilledhomogenizationbuffer.Finally,debris MainUMAPofDRG
wasremoved by Iodixanol 25–29%, and the nuclei pellet was resus- TheAnnDataobjectswereconcatenatedtocreateaunifiedAnnData
pended.Forsingle-nucleiMultiomicsequencing,thenucleipelletwas object,andwemadeuseoftwomodelswhichwerebasedonthescVI71
resuspendedin30µL1×chillednucleibuffer(10xGenomics,2000207) framework(v0.20.3)fortheintegrationofDRGdata.First,wetrained
andthenproceededimmediatelyforsingle-nucleiMultiomicsequen- thescVImodeltointegratetheDRGcellsunbiasedlyon3000highly
cingprotocol.Forneuron-specific-single-nucleiRNAsequencing,the variable genes. The model architecture was designed to obtain 50
nuclei pellet wasresuspended in 500ul blocking buffer (1× PBS,1% dimensionsinthelatentspacewith5hiddenlayersand128nodesper
BSA,0.2U/μlRNaseinhibitor)forfluorescent-activatednucleisorting hiddenlayer,wherethedistributionofgenelikelihoodwasnegative
andSmart-seq3xpress. binomial.ThenweconstructedascANVImodelbasedonthetrained
scVImodeltoobtainthelatentspacethatcouldclearlyseparatethe
Fluorescent-activatednucleisortingandsingle-nucleiRNA respectivecelltypesforvisualization.Weusedthecell-typenomen-
sequencing(Smart-seq3xpressand10xMultiomicsequencing) clature from Renthal et al. 5 to train the model and perform label
Toenablesortingofnucleiderivedfromneurons,nucleisuspension transfer. The scANVI model was trained until the model was con-
was incubated with anti-NeuN PE-conjugated antibody (1:500, verged.Afterthemodelsweretrained,thelatentspacesfromscVIand
FCMAB317PE,Merck)for 30minonice. Next, nuclei pellet wascol- scANVI were extracted. The neighbor graph was built from 50
lected by 5min, 400×g suspension, and resuspended in PBS con- dimensionswith100neighborsandthemethodtocalculatethedis-
taining 0.1μg/mL DAPI (D3571, Invitrogen) and 0.2U/ul RNase tancewascosinebasedonthelatentspacefromscANVI.Theprojec-
inhibitor.SingleNeuN+andDAPI+nucleiweresortedintoeachwellof tionofUMAPofconstructedfromtheneighborgraphwithparameter
a 384-well plate containing 0.3µL lysis reaction mix by a flow cyt- min_dist=0.5beforeplotting.
ometer(DBFACSAriaFusionorBDFACSAriaIII)at4°C.Gatingwas
performed based on DAPI and phycoerythrin signal of NeuN. After Featureimputation
sorting,eachplatewasimmediatelyspundownandstoredat−80°C Next,wetraintheMultiVImodeltoimputedforthemissingfeatures
before single-nuclei RNA sequencing with Smart-seq3xpress. The acrossdatamodalitiesbyusingourlab-generatedmultiomicsdataas
smart-seq3xpress protocol was performed by Rickard Sandberg’s an anchor. We aimed to impute as many features as possible. The
Group,KarolinskaInstitute.NucleiisolatedforsinglenucleiMultiomic MultiVI was constructed by using the default parameters and was
sequencing were stained with DAPI and sent for sequencing by traineduntilitconverged.Totrainthemodel,weemployedNVIDIA
EukaryoticSingleCellGenomicsFacilityatSciLifeLab,Stockholm. A100GPUtobeabletoholdthecountmatrixontheVRAM,andthis
resource was provided by the National Academic Infrastructure for
ObtainingandpreprocessingthepubliclyavailablescRNA- SupercomputinginSweden(NAISS).Afterthetraining,theimputation
seqdata ofthegeneexpressionmodalitywasdonebycallingget_normalize-
ThecountmatricesandassociatedmetadataofDRGwereobtained d_expression method from the model, while the chromatin accessi-
fromtheGeneExpressionOmnibus(GEO)withthefollowingaccession bilitymodalitywasimputedusingget_accessibility_estimatesmethod
numbers presented on Table 1. Additionally, the data were pre- withcustomparametersofthreshold=0.1,normalize_cells=True,and
processedaccordingtotheoriginalpapersbeforebeingloadedinto normalize_regions=True.Theimputedmatriceswerethenmultiplied
Python3asAnnDataobjects. by10,000.
NatureCommunications|( 2024)1 5:8585 11

Article https://doi.org/10.1038/s41467-024-52052-8
Analysisofthenociceptivelineagecells thetop10percentileandassignedthemasSASP.Tostudytherelative
Thenociceptivelineagecellswereselectedandsubsettoyieldhigh- ageofSASPcells,weperformedgenesetenrichmentanalysiswiththe
resolution clusters.The neighbor graph and UMAP projection were run_gsea function from the decoupleR73 package to extract the
calculatedusingthesameparametersasmentionedabove.Thenwe enrichmentscoresofGenAgeandCellAgegenesets.Thiswasdoneon
clustered the nociceptive lineage cells with the Leiden clustering the normalized unscaled imputed gene expression count matrix.
algorithmat0.1resolution.Tovisualizethedistributionofcellsalong Mann–Whitney U test was performed to test for the statistical sig-
thetimekineticafterinjury,theembedding_densitymethodfromthe nificanceoftheSenMayoscorebetweenthenaïveandinjurygroups.
ScanpypackagewasutilizedtocomputethecelldensityontheUMAP
projection for cells at different timepoints. Next, we ran the AnalysisofhumanDRGRNA-seqwithin
pySCENIC72pipelinetocalculatetheregulonactivityinthenociceptive FortheanalysisofhumanDRGRNA-seq,wefirstobtainedthebulk
lineage.Yet,notallTFshadtheinformationforregulonsandthuswe RNA-seqdataofdifferentpainconditionsofneuron-richsamplesfrom
fittheunivariatelinearmodel(ULM)fromthedecoupleR73packageby Rayetal.38.AsthecountmatrixwasnormalizedusingtheTPMmethod,
usingtheRNAexpressionofeachcellasanindependentvariableand we multiplied 1e6 to the matrix to unnormalize it back to the raw
theinteractionweightofeachTFfromtheadjacencytablefrompyS- transcriptcountvalues.Thenwenormalizedtherawcounttoobtain
CENICasatarget.Thet-valueoftheslopeofthefittedmodelrepre- thetotaltranscriptcountpersampleafternormalizationequaltothe
sentedtheTFactivity. medianofthetotaltranscriptcountforthatsamplebeforenormal-
ization.Thenormalizedcountmatrixwaslog-transformedandscaled
Cellstatepotency withlog1pandscalefunctionsfromScanpy.SenMayoscorewascal-
The relative cell state potency of the nociceptive lineage cells was culatedwiththescore_genefunctiononthescaledcountmatrix.
calculated in R using the CytoTrace package. Before running Cyto- RegardingthedeconvolutionofhDRG,weretrievedthesnRNA-seq
Trace,wereconstructedtherawcountmatrixofthegeneexpression ofhDRGundernormalconditionsfromJungetal.39withtheaccession
datafromtheimputednormalizedcountwiththePyTorchdistribution numberGSE201654fromGEO.Thedatawaspreprocessedandanalyzed
moduleforthenegativebinomialdistribution.Afterthereconstruc- asdescribedintheoriginalpaper.Thedeconvolutionwasdoneusinga
tion,theAnnDataobjectwasconvertedintoaSingleCellExperiment VAE-based model called Bulk2Single provided by the omicverse76
(SCE)objectusingrpy2andanndata2riPythonpackages.Oncecon- packageinPython3.ThebulkRNA-seqdataofhDRGwasseparatedinto
verted,weranCytoTraceonthereconstructedrawcountmatrixwith twocountmatrices,onefromdonorswithoutknownpainconditions
datasourcespassedtothebatchparameter.TheCytoTracewasnor- andtheotherfromdonorswithpain.Asthedatawassplitintwo,we
malizedtohavetherangefrom0to1.ThenwecalculatedtheCyto- trainedtwomodelsseparatelyfor3500epochseach.Afterthetraining,
Trace pseudotime by taking the difference between 1 and the the predicted snRNA-seq count matrices were reconstructed and
normalizedCytoTracescore.Weperformedanindependentt-testwith mergedforfurtheranalysis.Thereweremorethan250,000cellsgen-
7000 random permutations on the CytoTrace scores between the eratedbythemodelsintotal.Weprocessedandclusteredthematrix
naïveandinjurystateswiththeSciPypackagetoconfirmthatthescore accordingtoScanpyworkflowwiththeLeidenclusteringalgorithm,and
inthenaïvestatewassignificantlyhigherthanthatoftheinjuredstate. wenoticedthattherewasalotofnoisewithinthegenerateddataas
there were many clusters comprised of 50–1000 cells. Thus, Leiden
Temporalanalysisofnociceptivesubtypes clusterswithlessthan900cellswereremovedtoretaincellswithclean
WeemployedCellRank74(v2.0.0)toperformthetemporalanalysisof signals.Furthermore,weselectedonlynociceptivecellstocalculatethe
eachnociceptivesubtypebetweencontrolandpainstatesbasedon SenMayoscoreafterscalingthecountmatrix.
RNAmodality.Foreachsubtype,wemadeuseoftheCytroTracekernel RegardingtheanalysisofhDRG,wenotedthatthecellpropor-
fromCellRanktocomputethetransitionmatrix.Thenwepassedthe tionsbetweenthereferencesnRNA-seqandthedeconvolutionofbulk
transition matrix CytroTrace kernel to Generalized Perron Cluster- RNA-seqwerenotequal.Thisresultwasexpectedasweperformedthe
ClusterAnalysis(GPCCA)fortheidentificationofterminalstatesand deconvolutiononthesamplesfromthegroupbeingclassifiedbythe
fate probability toward the terminal states with n_states=3. With authorsasneuron-richsamples36(51outof70samples),tofocusour
GPCCA,weidentifiedthelineagedrivergenesthatdrovethetransition analysisonnociceptivelineagecells.Thedeconvolutionyielded~60%
ofcellstowardtheterminalstateofpain.Ageneralizedadditivemodel neurons whereas the reference snRNA-seq contained a more repre-
wasutilizedtofittheexpressionprofileforeachgeneasafunctionof sentativepopulationofthecelltypesinDRGwitharound~2%neurons.
pseudotime to visualize the expression trend of the lineage driver WethusappliedabroadclassificationonthehDRGincontrasttothe
genes.Furthermore,wealsoappliedthesameanalyticalapproachon single-cellanalysisinmicemodel,aswesuspectedthatthedeconvo-
theregulonslevelcalculatedfromSCENIC. lutionmodelcouldnotperformwellinclassifyingthehigh-resolution
celltypes(neuronalsubtypes)thatwerecloselyrelatedtoeachother
Cell-cellcommunication due to it being trained on the reference sample with lower neuron
The inference of cell-cell communication (CCC) was done with the representation. Nevertheless, even with the broad classification the
LIANA+75 package (v0.1.8). Here,wepassed the count matrix ofthe model seems to have some difficulties in clearly distinguishing
atlasasinputtotherank_aggregate.by_samplenfunctionofLIANAand betweenthetwoneuronalcelltypesofNFsandnociceptorsthatare
weselected“mouseconsensus”astheresourceforCCCinference.Due morehighlycorrelatedthanothercelltypes(Fig.4h).Despitethis,the
tomulti-conditionsandmulti-timepointsinformationheldwithinthe Spearmancorrelationstillindicatedthehighestcorrelationbetween
atlas,thecommunicationswereverycomplex.Thus,tensordecom- thetranscriptomeprofilesofthenociceptorsidentifiedintherefer-
position was employed to extract meaningful communications as encesnRNA-seqandthedeconvolvedRNA-seqnociceptors,indicating
factors.Thiswasaccomplishedbycallingrun_tensor_cell2cell_pipeline theapplicabilityofthemodel.WethenproceededtoperformaSen-
functionprovidedbythecell2cell28package. MayoscorecomparisonbetweentheNoPainandPaingroupstofind
thatitisincreasedinthePaingroupindicatingforcellularsenescence,
Identificationofsenescence aligningwithourotherresults.
TheSenMayogenescorewascalculatedbasedonthescaleddataof
theimputedgeneexpressioncountmatrixbyusingthescore_genes AnalysisofhumanDRGRNA-seqwithdiabeticneuropathy
function from the Scanpy package. The SenMayo gene set can be ThecountmatrixwasobtainedfromHalletal.40.Thecountmatrixwas
foundinSupplementaryData7.Additionally,weselectedcellswithin normalized into transcript per million and pseudo-log transformed.
NatureCommunications|( 2024)1 5:8585 12

Article https://doi.org/10.1038/s41467-024-52052-8
The effect of different sexes was regressed out with Scanpy’s 4. Usoskin,D.etal.Unbiasedclassificationofsensoryneurontypesby
regress_outfunction.Sampleswiththeiragesbeingoutliersbetween large-scalesingle-cellRNAsequencing.Nat.Neurosci.18,
thehealthyanddiabeticgroupswereremoved;theseweresamples 145–153(2015).
withagesbelow30andagesabove60.TheSenMayoscorewascal- 5. Renthal,W.etal.Transcriptionalreprogrammingofdistinctper-
culatedafterthematrixwasbeingscaled.TheZ-scoreofSenMayowas ipheralsensoryneuronsubtypesafteraxonalinjury.Neuron108,
computed beforeperforming a one-sided t-testto statistically com- 128–144.e9(2020).
parethescoresbetweenhealthyanddiabeticgroups. 6. Kupari,J.etal.Singlecelltranscriptomicsofprimatesensory
neuronsidentifiescelltypesassociatedwithchronicpain.Nat.
UMAPofTG Commun.12,1510(2021).
FortheTG,wegenerateanintegratedatlasseparatelyforTGusing 7. Couturier,C.P.etal.Single-cellRNA-seqrevealsthatglioblastoma
scGLUE20(v0.3.2),byfirstcomputingthelatentspacerepresenta- recapitulatesanormalneurodevelopmentalhierarchy.Nat.Com-
tionofeachsourceandmodalityandpassingthemasinput.Forthe mun.11,3406(2020).
latentspacerepresentationofRNA,weupdatedtheweightsofthe 8. Otero-Garcia,M.etal.Molecularsignaturesunderlyingneurofi-
scANVImodeltrainedontheDRGdatatoobtaintheupdatedlatent brillarytanglesusceptibilityinAlzheimer’sdisease.Neuron110,
spaceoftheRNAgeneexpressionmodalityfortheTGdatasets.LSA 2929–2948.e8(2022).
wasperformedontheATACmodalitytoobtainthelatentsemantic 9. Wang,K.etal.Single-celltranscriptomicanalysisofsomatosensory
indexing from the TG datasets. Furthermore, scGLUE required an neuronsuncoverstemporaldevelopmentofneuropathicpain.Cell
additionalinputbesidesthelatentspacerepresentationswhichwas Res.31,904–918(2021).
theguidancegraph.Theguidancegraphwasconstructedusingthe 10. Avraham,O.etal.Profilingsensoryneuronmicroenvironmentafter
highly variable features from RNA and ATAC as described in the peripheralandcentralaxoninjuryrevealskeypathwaysforneural
original paper20. After the inputs were prepared, the model was repair.eLife10,e68457(2021).
trainedwiththedefaultparameters.Oncethemodelwastrained, 11. Zhang,C.etal.scRNA-sequencingrevealssubtype-specifictran-
weextractedcellembeddingfromthemodeltobuildaneighbor scriptomicperturbationsinDRGneuronsofPirtEGFPfmicein
graphusing“cosine”asametric.TheUMAPwascomputedfromthe neuropathicpaincondition.eLife11,e76063(2022).
neighborgraph.Tofacilitateuswithcell-typeannotation,weper- 12. Sharma,N.etal.Theemergenceoftranscriptionalidentityin
form label transfer using the scANVI model that was previously somatosensoryneurons.Nature577,392–398(2020).
updatedwiththeweights. 13. Parpaite,T.etal.Patch-seqofmouseDRGneuronsrevealscandi-
dategenesforspecificmechanosensoryfunctions.CellRep.37,
Statisticalanalysis 109914(2021).
ThestatisticalanalysisandtestsweredoneinPython3withthe“stats” 14. Yang,L.etal.Humanandmousetrigeminalgangliacellatlas
modulefromtheSciPyv1.10.1package.Thedatawereeitherimported implicatesmultiplecelltypesinmigraine.Neuron110,
as DataFrame or Array through Pandas v2.0.3 or Numpy v1.22.4 1806–1821.e8(2022).
packagerespectively.Ingeneral,at-testwasappliedwhenthedata 15. Jia,S.etal.Single-cellRNAsequencingrevealsdistincttranscrip-
followedanormaldistribution.Otherwise,theMann–WhitneyUtest tionalfeaturesofthepurinergicsignalinginmousetrigeminal
wasperformedifthe datadid notappearto follow the normal dis- ganglion.Front.Mol.Neurosci.15,1038539(2022).
tribution.Forthebehavioranalysiswithpaireddatapairedt-testwas 16. Nguyen,M.Q.,Wu,Y.,Bonilla,L.S.,vonBuchholtz,L.J&Ryba,N.J.
used for comparison, where an independent t-test was used on P.Diversityamongsttrigeminalneuronsrevealedbyhigh
unpaireddata. throughputsinglecellsequencing.PLoSONE12,e0185543(2017).
17. Liu,Q.etal.Transcriptionalalterationsofmousetrigeminalgang-
Reportingsummary lionneuronsfollowingorofacialinflammationrevealedbysingle-
Further information on research design is available in the Nature cellanalysis.Front.Cell.Neurosci.16,885569(2022).
PortfolioReportingSummarylinkedtothisarticle. 18. Xu,C.etal.Probabilisticharmonizationandannotationofsingle-
celltranscriptomicsdatawithdeepgenerativemodels.Mol.Syst.
Dataavailability Biol.17,e9620(2021).
Thesequencingdataandcountmatrices generatedfrom this study 19. Ashuach,T.etal.MultiVI:deepgenerativemodelfortheintegration
havebeendepositedintheGeneExpressionOmnibus(GEO)database ofmultimodaldata.Nat.Methods20,1222–1231(2023).
under accession code GSE253345. All the datasets with their GEO 20. Cao,Z.-J.&Gao,G.Multi-omicssingle-celldataintegrationand
accessionsusedtogenerateiPaincanbefoundinTable1.Theinter- regulatoryinferencewithgraph-linkedembedding.Nat.Biotechnol.
activevisualizationoftheatlasescanbeaccessedthroughCELLxGENE 40,1458–1466(2022).
platformfromthe ChanZuckerberg Initiative (iPain) and UCSC cell 21. TheConditionofNeuropathicPain.inNeuropathicPain:Causes,
browser77.Sourcedataareprovidedwiththispaper. ManagementandUnderstanding(eds.Toth,C.&Moulin,D.E.)
33–100(CambridgeUniv.Press,Cambridge,2013).
Codeavailability 22. Ma,T.C.&Willis,D.E.WhatmakesaRAGregenerationassociated?
Thescriptforthecoreanalysisofthisworkcanbefoundathttps:// Front.Mol.Neurosci.8,43(2015).
github.com/PrachTecha/Hadjab_iPain. 23. Huebner,E.A.&Strittmatter,S.M.Axonregenerationintheper-
ipheralandcentralnervoussystems.ResultsProbl.CellDiffer.48,
References 339–351(2009).
1. Yong,R.J.,Mullins,P.M.&Bhattacharyya,N.Prevalenceofchronic 24. LaManno,G.etal.RNAvelocityofsinglecells.Nature560,
painamongadultsintheUnitedStates.Pain163,e328(2022). 494–498(2018).
2. QueremelMilani,D.A.&Davis,D.D.PainManagementmedications. 25. Gulati,G.S.etal.Single-celltranscriptionaldiversityisahallmarkof
inStatPearls(StatPearlsPublishing,TreasureIsland,FL,2023). developmentalpotential.Science367,405–411(2020).
3. TheLancetRegionalHealth–Americas.Opioidcrisis:addiction, 26. Wolf,F.A.etal.PAGA:graphabstractionreconcilesclusteringwith
overprescription,andinsufficientprimaryprevention.LancetReg. trajectoryinferencethroughatopologypreservingmapofsingle
HealthAm.23,100557(2023). cells.GenomeBiol.20,59(2019).
NatureCommunications|( 2024)1 5:8585 13

Article https://doi.org/10.1038/s41467-024-52052-8
27. Le,D.etal.Neuropathicpaindevelopmentfollowingnerveinjuryis 48. Donovan,L.J.etal.Agingandinjurydriveneuronalsenescencein
mediatedbySOX11-ARID1A-SOCS3transcriptionalregulationinthe thedorsalrootganglia.PreprintatbioRxivhttps://doi.org/10.1101/
spinalcord.Mol.Biol.Rep.51,281(2024). 2024.01.20.576299(2024).
28. Armingol,E.etal.Context-awaredeconvolutionofcell–cellcom- 49. Wolf,F.A.,Angerer,P.&Theis,F.J.SCANPY:large-scalesingle-cell
municationwithTensor-cell2cell.Nat.Commun.13,3665(2022). geneexpressiondataanalysis.GenomeBiol.19,15(2018).
29. Mijit,M.,Caracciolo,V.,Melillo,A.,Amicarelli,F.&Giordano,A.Role 50. Program,C.S.-C.B.etal.CZCELL×GENEDiscover:asingle-celldata
ofp53intheregulationofcellularsenescence.Biomolecules10, platformforscalableexploration,analysisandmodelingofaggre-
420(2020). gateddata.PreprintatbioRxivhttps://doi.org/10.1101/2023.10.30.
30. Schmitt,C.A.etal.Asenescenceprogramcontrolledbyp53and 563174(2023).
p16INK4acontributestotheoutcomeofcancertherapy.Cell109, 51. Sommer,C.Neuropathicpainmodel,chronicconstrictioninjury.in
335–346(2002). EncyclopediaofPain(edsSchmidt,R.F.&Willis,W.D.)1290–1292
31. Hafner,A.,Bulyk,M.L.,Jambhekar,A.&Lahav,G.Themultiple (Springer,Berlin,Heidelberg,2007).
mechanismsthatregulatep53activityandcellfate.Nat.Rev.Mol. 52. Bennett,G.J.&Xie,Y.-K.Aperipheralmononeuropathyinratthat
CellBiol.20,199–210(2019). producesdisordersofpainsensationlikethoseseeninman.Pain
32. Saul,D.etal.Anewgenesetidentifiessenescentcellsandpredicts 33,87–107(1988).
senescence-associatedpathwaysacrosstissues.Nat.Commun.13, 53. Guan,Y.etal.Mas-relatedG-protein–coupledreceptorsinhibit
4827(2022). pathologicalpaininmice.Proc.NatlAcad.Sci.USA107,
33. deMagalhães,J.P.,Curado,J.&Church,G.M.Meta-analysisofage- 15933–15938(2010).
relatedgeneexpressionprofilesidentifiescommonsignaturesof 54. Chaplan,S.R.,Bach,F.W.,Pogrel,J.W.,Chung,J.M.&Yaksh,T.L.
aging.Bioinformatics25,875–881(2009). Quantitativeassessmentoftactileallodyniaintheratpaw.J.Neu-
34. Saito-Diaz,K.,Street,J.R.,Ulrichs,H.&Zeltner,N.Derivationof rosci.Methods53,55–63(1994).
peripheralnociceptive,mechanoreceptive,andproprioceptive 55. Bonin,R.P.,Bories,C.&DeKoninck,Y.Asimplifiedup-down
sensoryneuronsfromthesamecultureofhumanpluripotentstem method(SUDO)formeasuringmechanicalnociceptioninrodents
cells.StemCellRep.16,446–457(2021). usingvonFreyfilaments.Mol.Pain.10,26(2014).
35. Luo,D.,Luo,L.,Lin,R.,Lin,L.&Lin,Q.Brain-derivedneurotrophic 56. Hargreaves,K.,Dubner,R.,Brown,F.,Flores,C.&Joris,J.Anewand
factorandGlialcellline-derivedneurotrophicfactorexpressionsin sensitivemethodformeasuringthermalnociceptionincutaneous
thetrigeminalrootentryzoneandtrigeminalganglionneuronsofa hyperalgesia.Pain32,77–88(1988).
trigeminalneuralgiaratmodel.Anat.Rec.303,3014–3023 57. Feng,X.etal.Directinhibitionofmicrogliaactivationbypretreat-
(2020). mentwithbotulinumneurotoxinaforthepreventionofneuropathic
36. Mjåset,C.&Russell,M.B.Secondarychronicclusterheadachedue pain.Front.Neurosci.15,760403(2021).
totrigeminalnerverootcompression.ActaNeurol.Scand.122, 58. Rinwa,P.etal.DemiseofnociceptiveSchwanncellscausesnerve
373–376(2010). retractionandpainhyperalgesia.Pain162,1816–1827(2021).
37. Tao,R.etal.UsingRNA-seqtoexplorethehubgenesinthetri- 59. Yoon,C.,Wook,Y.Y.,Sik,N.H.,Ho,K.S.&Mo,C.J.Behavioralsigns
geminalrootentryzoneofratsbycompressioninjury.PainPhysi- ofongoingpainandcoldallodyniainaratmodelofneuropathic
cian24,E573–E581(2021). pain.Pain59,369–376(1994).
38. Ray,P.R.etal.RNAprofilingofhumandorsalrootgangliareveals 60. La-Vu,M.,Tobias,B.C.,Schuette,P.J.&Adhikari,A.Toapproachor
sexdifferencesinmechanismspromotingneuropathicpain.Brain avoid:anintroductoryoverviewofthestudyofanxietyusingrodent
146,749–766(2023). assays.Front.Behav.Neurosci.14,145(2020).
39. Jung,M.etal.Cross-speciestranscriptomicatlasofdorsalroot 61. Walf,A.A.&Frye,C.A.Theuseoftheelevatedplusmazeasan
gangliarevealsspecies-specificprogramsforsensoryfunction. assayofanxiety-relatedbehaviorinrodents.Nat.Protoc.2,
Nat.Commun.14,366(2023). 322–328(2007).
40. Hall,B.E.etal.Transcriptomicanalysisofhumansensoryneuronsin 62. Carter,R.J.,Morton,J.&Dunnett,S.B.Motorcoordinationand
painfuldiabeticneuropathyrevealsinflammationandneuronal balanceinrodents.Curr.Protoc.Neurosci.15,8.12.1–8.12.14(2001).
loss.Sci.Rep.12,4729(2022). 63. Tung,V.W.K.,Burton,T.J.,Dababneh,E.,Quail,S.L.&Camp,A.J.
41. Chaib,S.,Tchkonia,T.&Kirkland,J.L.Cellularsenescenceand Behavioralassessmentoftheagingmousevestibularsystem.J.Vis.
senolytics:thepathtotheclinic.Nat.Med.28,1556–1568 Exp.https://doi.org/10.3791/51605(2014).
(2022). 64. Deacon,R.M.J.Measuringmotorcoordinationinmice.J.Vis.Exp.
42. Bergsland,M.,Werme,M.,Malewicz,M.,Perlmann,T.&Muhr,J.The https://doi.org/10.3791/2609(2013)
establishmentofneuronalpropertiesiscontrolledbySox4and 65. Luong,T.N.,Carlisle,H.J.,Southwell,A.&Patterson,P.H.
Sox11.GenesDev.20,3475–3486(2006). Assessmentofmotorbalanceandcoordinationinmiceusingthe
43. Bhattaram,P.etal.OrganogenesisreliesonSoxCtranscription balancebeam.J.Vis.Exp.https://doi.org/10.3791/2376(2011).
factorsforthesurvivalofneuralandmesenchymalprogenitors. 66. Ruifrok,A.C.&Johnston,D.A.Quantificationofhistochemical
Nat.Commun.1,9(2010). stainingbycolordeconvolution.Anal.Quant.Cytol.Histol.23,
44. Chen,P.etal.IdentificationofSlc6a19osandSOX11astwonovel 291–299(2001).
essentialgenesinneuropathicpainusingintegratedbioinformatic 67. Landini,G.,Martinelli,G.&Piccinini,F.Colourdeconvolution:stain
analysisandexperimentalverification.Front.Neurosci.15, unmixinginhistologicalimaging.Bioinformatics37,
627945(2021). 1485–1487(2021).
45. Bhuiyan,S.A.etal.Harmonizedcross-speciescellatlasesoftri- 68. AllenInstituteforBrainScience.IsolationofNucleifromHumanor
geminalanddorsalrootganglia.Sci.Adv.10,eadj9173(2024). NHPBrainTissue.protocols.iohttps://doi.org/10.17504/protocols.
46. Muralidharan,A.etal.Long-termmale-specificchronicpainvia io.ewov149p7vr2/v3(2024).
telomere-andp53‑mediatedspinalcordcellularsenescence.J. 69. Parekh,S.,Ziegenhain,C.,Vieth,B.,Enard,W.&Hellmann,I.zUMIs-
Clin.Invest.132,e151817(2022). afastandflexiblepipelinetoprocessRNAsequencingdatawith
47. Paramos-de-Carvalho,D.etal.Targetingsenescentcellsimproves UMIs.GigaScience7,giy059(2018).
functionalrecoveryafterspinalcordinjury.CellRep.36, 70. Kaminow,B.,Yunusov,D.&Dobin,A.STARsolo:accurate,fastand
109334(2021). versatilemapping/quantificationofsingle-cellandsingle-nucleus
NatureCommunications|( 2024)1 5:8585 14

Article https://doi.org/10.1038/s41467-024-52052-8
RNA-seqdata.PreprintatbioRxivhttps://doi.org/10.1101/2021.05. data:P.T.,X.F.,K.Z,andS.H.Computationalanalysisandintegrated
05.442755(2021). atlases:P.T.undersupervisionofS.H.Figures:P.T.andS.H.withinput
71. Gayoso,A.etal.APythonlibraryforprobabilisticanalysisofsingle- fromallco-authors.Draftingofmanuscript:P.T.,K.Z.,andS.H.withinput
cellomicsdata.Nat.Biotechnol.40,163–166(2022). fromX.F.
72. VandeSande,B.etal.AscalableSCENICworkflowforsingle-cell
generegulatorynetworkanalysis.Nat.Protoc.15,2247–2276 Funding
(2020). OpenaccessfundingprovidedbyKarolinskaInstitute.
73. Badia-i-Mompel,P.etal.decoupleR:ensembleofcomputational
methodstoinferbiologicalactivitiesfromomicsdata.Bioinform. Competinginterests
Adv.2,vbac016(2022). S.H.isaninventoronpendingpatentsdescribingsenolyticcompounds
74. Lange,M.etal.CellRankfordirectedsingle-cellfatemapping.Nat. forthetreatmentofaheadachedisorderand/orchronicpain(applica-
Methods19,159–170(2022). tionnumbers#2351493-8and#2450321-1).Theotherauthorsdonot
75. Dimitrov,D.etal.LIANA+:anall-in-onecell-cellcommunication havecompetinginterests.
framework.PreprintatbioRxivhttps://doi.org/10.1101/2023.08.19.
553863(2023). Additionalinformation
76. Zeng,Z.etal.Asinglepipelineforexploringtheentiretran- SupplementaryinformationTheonlineversioncontains
scriptomeuniverse.PreprintatbioRxivhttps://doi.org/10.1101/ supplementarymaterialavailableat
2023.06.06.543913(2023). https://doi.org/10.1038/s41467-024-52052-8.
77. Speir,M.L.etal.UCSCCellBrowser:visualizeyoursingle-celldata.
Bioinformatics37,4578–4580(2021). Correspondenceandrequestsformaterialsshouldbeaddressedto
SaidaHadjab.
Acknowledgements
TheauthorsaregratefultoProfessorFrancoisLallemendandteam PeerreviewinformationNatureCommunicationsthanksYiZhangand
membersfordiscussionandproofreadingthemanuscript.Theauthors theotheranonymousreviewer(s)fortheircontributiontothepeer
aregratefultoProfessorPatrikErnforsandteammembers,especially reviewofthiswork.Apeerreviewfileisavailable.
DoctorsJieSuandMingdongZhangfortraininginperformingpain
modelsandpainbehaviorassessments.Theauthorsaregratefulto Reprintsandpermissionsinformationisavailableat
DoctorMarekBartosovicforthediscussiononepigenomicanalysis.The http://www.nature.com/reprints
authorsthankDoctorOlgaKharchenkofordrawings,DoctorSylvain
Peugetforthegiftofthep21antibody.Theauthorswouldliketo Publisher’snoteSpringerNatureremainsneutralwithregardtojur-
acknowledgetheKIinnovation,Bicfacility,theBFCfacility,theAnimal isdictionalclaimsinpublishedmapsandinstitutionalaffiliations.
BehaviorCoreFacilityatKarolinskaInstitutet,theEukaryoticSingleCell
Genomics(ESCG)Facility,andtheNationalGenomicsInfrastructure OpenAccessThisarticleislicensedunderaCreativeCommons
(NGI)attheScienceforLifeLaboratory,Sweden,forthesc/snRNA-seq. Attribution4.0InternationalLicense,whichpermitsuse,sharing,
TheauthorsacknowledgesupportfromtheNationalGenomicsInfra- adaptation,distributionandreproductioninanymediumorformat,as
structureinStockholmfundedbyScienceforLifeLaboratory,theKnut longasyougiveappropriatecredittotheoriginalauthor(s)andthe
andAliceWallenbergFoundationandtheSwedishResearchCouncil, source,providealinktotheCreativeCommonslicence,andindicateif
andSNIC/UppsalaMultidisciplinaryCenterforAdvancedComputa- changesweremade.Theimagesorotherthirdpartymaterialinthis
tionalScienceforassistancewithmassivelyparallelsequencingand articleareincludedinthearticle’sCreativeCommonslicence,unless
accesstotheUPPMAXcomputationalinfrastructure.Thecomputations indicatedotherwiseinacreditlinetothematerial.Ifmaterialisnot
anddatahandlingwereenabledbyresourcesprovidedbytheNational includedinthearticle’sCreativeCommonslicenceandyourintended
AcademicInfrastructureforSupercomputinginSweden(NAISS)par- useisnotpermittedbystatutoryregulationorexceedsthepermitted
tiallyfundedbytheSwedishResearchCouncilthroughgrantagreement use,youwillneedtoobtainpermissiondirectlyfromthecopyright
no.2022-06725.S.H.,P.T.,andK.Z.aresupportedbytheKIDfundingat holder.Toviewacopyofthislicence,visithttp://creativecommons.org/
KarolinskaInstitutet,S.H.andX.F.aresupportedbytheWennerGren licenses/by/4.0/.
Foundation.S.H.wasfurthersupportedbyStratNeuro,TystaSkolan,the
SwedishResearchCouncil,andHjärnfonden. ©TheAuthor(s)2024
Authorcontributions
Studydesignandsupervision:S.H.Tissuecollectionandacquisitionof
data:X.F.,K.Z.,P.T.,andS.H.Animalbehavior:X.F.andK.Z.Analysisof
NatureCommunications|( 2024)1 5:8585 15