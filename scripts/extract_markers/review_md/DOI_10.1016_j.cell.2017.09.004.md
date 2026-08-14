Article
Single-Cell Analysis of Human Pancreas Reveals
Transcriptional Signatures of Aging and Somatic
Mutation Patterns
Graphical Abstract Authors
MartinEnge,H.EfsunArda,
MarcoMignardi,JohnBeausang,
RitaBottino,SeungK.Kim,
StephenR.Quake
Correspondence
quake@stanford.edu
In Brief
Agingisassociatedwithincreased
transcriptionaldysregulationandlossof
identityatthesingle-celllevel
Highlights
d RNA-seqofsinglecellsfromdonorsallowsdetectionof
stochasticage-relatederrors
d Cellsfromolderdonorshaveincreasedtranscriptionalnoise
andsignsoffatedrift
d Endocrinepancreascellsdisplayanoxidativestress-related
mutationalsignature
d Cellularstressandmetabolicgenesarehighincellswith
accumulationoferrors
Engeetal.,2017,Cell171,321–330
October5,2017ª2017ElsevierInc.
http://dx.doi.org/10.1016/j.cell.2017.09.004

Article
| Single-Cell |     | Analysis        |         |     | of  | Human      | Pancreas |     |     |     |     |
| ----------- | --- | --------------- | ------- | --- | --- | ---------- | -------- | --- | --- | --- | --- |
| Reveals     |     | Transcriptional |         |     |     | Signatures |          |     |     |     |     |
| of Aging    |     | and             | Somatic |     |     | Mutation   | Patterns |     |     |     |     |
MartinEnge,1,6H.EfsunArda,2MarcoMignardi,1,5JohnBeausang,1RitaBottino,4SeungK.Kim,2
andStephenR.Quake1,3,4,7,*
1DepartmentofBioengineeringandAppliedPhysics,StanfordUniversity,Stanford,CA94305,USA
2DepartmentofDevelopmentalBiology,StanfordUniversitySchoolofMedicine,CA94305,USA
3ChanZuckerbergBiohub,SanFrancisco,CA94158,USA
4InstituteofCellularTherapeutics,AlleghenyHealthNetwork,320EastNorthAvenue,Pittsburgh,PA15212,USA
5DepartmentofInformationTechnology,UppsalaUniversity,SwedenandSciLifeLab,Uppsala,SwedenSE-75105
6Presentaddress:DepartmentofOncology-Pathology,KarolinskaInstitutetandKarolinskaUniversityHospital,17176Stockholm,Sweden
7LeadContact
*Correspondence:quake@stanford.edu
http://dx.doi.org/10.1016/j.cell.2017.09.004
SUMMARY quences (Vijg, 2004). However, due to technical constraints, it
haspreviouslybeendifficulttostudytheseprocessesinhumantis-
As organisms age, cells accumulate genetic and sueoratthewholetranscriptomelevel.Inparticular,littleisknown
epigeneticerrorsthateventuallyleadtoimpairedor- about the mutational load on post-mitotic cells that cannot be
ganfunctionorcatastrophictransformationsuchas expandedinculture.StudiesonCAGrepeatsinmousebrain(Go-
cancer.Becauseagingreflectsastochasticprocess niteletal.,2008)haveshownthatage-dependentsomaticmuta-
|               |     |           |       |             |      |          | tion rates | in post-mitotic | cells might | be higher than | previously |
| ------------- | --- | --------- | ----- | ----------- | ---- | -------- | ---------- | --------------- | ----------- | -------------- | ---------- |
| of increasing |     | disorder, | cells | in an organ | will | be indi- |            |                 |             |                |            |
anticipated.Becausethesemutationalprocessesoperateinchro-
| vidually | affected | in different |     | ways, | thus | rendering |     |     |     |     |     |
| -------- | -------- | ------------ | --- | ----- | ---- | --------- | --- | --- | --- | --- | --- |
bulk analyses of postmitotic adult cells difficult to nologicaltimeratherthannumberofcelldivisions,ananalysisof
|     |     |     |     |     |     |     | humancells | froma large | agespanratherthanfromshort-lived |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ----------- | -------------------------------- | --- | --- |
interpret.Here,wedirectlymeasuretheeffectsofag-
modelorganismsisneeded.However,suchasystematicsurvey
| ing in human |     | tissue by | performing |     | single-cell | tran- |     |     |     |     |     |
| ------------ | --- | --------- | ---------- | --- | ----------- | ----- | --- | --- | --- | --- | --- |
ofhumantissuefromdifferentageshasnotbeenperformed.
scriptome analysis of 2,544 human pancreas cells Thepancreasfunctionsbothasanendocrineandanexocrine
| from eight | donors | spanning |     | six decades |     | of life. We |     |     |     |     |     |
| ---------- | ------ | -------- | --- | ----------- | --- | ----------- | --- | --- | --- | --- | --- |
glandandisassociatedwithillnessessuchastypeIIdiabetes,
| find that | islet | endocrine | cells | from | older | donors |     |     |     |     |     |
| --------- | ----- | --------- | ----- | ---- | ----- | ------ | --- | --- | --- | --- | --- |
thathaveaconsiderableage-relateddiseaserisk.Theexocrine
display increasedlevels oftranscriptionalnoiseand functionismediatedbyacinarcellsproducingenzymesforthe
potentialfatedrift.Bydeterminingthemutationalhis- digestivesystem,whiletheendocrinefunctionismediatedbyis-
letsofLangerhans,wherethemajorcelltypesarea-cells,b-cells,
toryofindividualcells,weuncoveranovelmutational
d-cells,andpancreaticpolypeptide(PP)cells.Previously,single-
| signature | in  | healthy aging | endocrine |     | cells. | Our re- |     |     |     |     |     |
| --------- | --- | ------------- | --------- | --- | ------ | ------- | --- | --- | --- | --- | --- |
sults demonstrate the feasibility of using single-cell cell RNA sequencing (scRNA-seq) on primary tissue has been
usedtostudyheterogeneitywithincelltypesandtofurtherrefine
| RNA sequencing |          | (RNA-seq) |         | data from | primary         | cells |                |                                 |            |                |             |
| -------------- | -------- | --------- | ------- | --------- | --------------- | ----- | -------------- | ------------------------------- | ---------- | -------------- | ----------- |
|                |          |           |         |           |                 |       | them—for       | the pancreas,                   | see Muraro | et al. (2016), | Segerstolpe |
| to derive      | insights | into      | genetic | and       | transcriptional |       |                |                                 |            |                |             |
|                |          |           |         |           |                 |       | etal.(2016),Li | etal.(2016),andWangetal.(2016). |            |                | However,    |
processesthatoperateonaginghumantissue. scRNA-seqalsoprovidesanidealframeworktostudynoisypro-
cessesthatactonsinglecells,suchasaging.Thus,toovercome
INTRODUCTION theprevioustechnicaldifficultiesinstudyingcellularaging,we
analyzedsinglehumancellsfromdonorsofawidespectrumof
Aginginhigher-ordermetazoansistheresultofagradualaccumu- ages.Usingthisapproachallowsustodetectfeaturesofaging
lationofcellulardamage,whicheventuallyleadstoadeclineintis- that are not coordinated across many cells but rather affect
| sue function | and | fitness (Lo´pez-Otı´n |     | et al., | 2013). | Because the |     |     |     |     |     |
| ------------ | --- | --------------------- | --- | ------- | ------ | ----------- | --- | --- | --- | --- | --- |
differentcellsrandomlyandtoquantifythemwithhighprecision.
fundamentalprocessesinvolvedinagingaffectsinglecellsina
stochasticmanner,theyhavebeendifficulttostudysystematically
| inprimaryhumantissue.Studiesofselectedgenesinmiceindi- |     |     |     |     |     |     | RESULTS |     |     |     |     |
| ------------------------------------------------------ | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- |
catethatagingpostmitoticcellsoftheheartdisplayatranscrip-
tionalinstability(Baharetal.,2006)thatisnotobservedinactively AComprehensiveSurveyofSinglePancreaticCells
renewingcellpopulationssuchasthoseofthehematopoieticsys- fromHumanDonorsacrossDifferentAges
tem(Warrenetal.,2007).Anaccumulationofgeneticaberrations To investigate the effect of physiological aging on pancreatic
hasbeensuggestedtounderlietranscriptionaldysregulationby epithelial cells, we obtained pancreata from eight previously
affectingpromoterandenhancerelementsaswellasexonicse- healthydonorsoperationallydefinedasjuvenile(ages1month,
|     |     |     |     |     |     |     | Cell171,321–330,October5,2017ª2017ElsevierInc. |     |     |     | 321 |
| --- | --- | --- | --- | --- | --- | --- | ---------------------------------------------- | --- | --- | --- | --- |

Figure1. AComprehensiveSurveyofSingleCellsSampledfromHumanPancreasacrossDifferentAges
(A)tSNEplotof2,544successfulscRNA-seqlibrariesfromeightdonors.Eachpointrepresentsonecellandpointsarepositionedtoretainpairwisedistancesas
determinedbyPearsoncorrelationofthe500mosthighlyexpressedgenes.Cellidentityisindicatedbymarkergeneexpression.
(B)FractionofcellsthatexpresstheagingassociatedgeneCDKN2A(p16)injuvenile(0–6years),youngadult(21–22years),andmiddle-aged(38–54years)
donorsincreaseswithage(p=3.1E-3,n=8,linearregression.)Barsaremean±SEM(n=2–3).
(C)Boxplotoftranscriptionalnoiseinb-cells,plottedbyagegroup.Higherageisassociatedwithincreasedwhole-transcriptomecell-to-cellvariabilitywithincell
type(p=6.67E-9,n=384).Boxesindicatethemiddlequartiles,separatedbymedianline.Whiskersindicatelastvalueswithin1.53theinterquartilerangefor
thebox.
(D)ViolinplotsshowtheratioofInsulin–GlucagonproteinstainingatthesitesofInsulin(INS,n=5,801)andGlucagon(GCG,n=3,254)RNAhybridizationspots.
(E)BoxplotofLog2countspermillion(CPM)ofcell-atypicalglucagontranscriptinbcells(left),andinsulintranscriptsina-cells(right),incellsfromjuvenile
(0–6years),youngadult(21–22years)andmiddle-aged(38–54)donors.Boxesindicatethemiddlequartiles,separatedbymedianline.Whiskersindicatelast
valueswithin1.53theinterquartilerangeforthebox.
SeealsoFigureS1andTablesS1,S2,andS3.
5years,and6years),youngadult(ages21yearsand22years), The fraction of cells expressing known markers of organismal
andadult/middleaged(ages38years,44years,and54years). aging, such as CDKN2A (p16INK4A), were associated with age
Singlepancreaticcellswerepurifiedbyflowcytometryandtheir (Figure 1B) consistent with prior studies using bulk RNA-seq
mRNAexpressionanalyzedusingscRNA-seq(Picellietal.,2014) on larger donor cohorts (Arda et al., 2016; Chen et al., 2011);
with transcript abundance expressed as counts per million however, overall we observed only modest systematic age-
(CPM)andthequalityofindividualcellsassessedusinganauto- dependenttranscriptionalchangesformanyage-specificgenes
mated quality control pipeline (see STAR Methods for details). (FiguresS1AandS1B;TablesS2andS3).Frominvestigationson
Dimensionalityreductionanalysis(tSNE)ofdatafromalldonors asmallpanelofgenesinthemouseheart(Baharetal.,2006),it
led to consistent clustering of different cell types into distinct haspreviouslybeensuggestedthatagingistheresultofanin-
regions (Figure 1A), indicating an absence of donor- or crease in transcriptional instability rather than a coordinated
sequencing-relatedbatcheffects. transcriptional program. To test whether this observation can
be generalized to a full transcriptional profile in human tissue,
TranscriptionalInstabilityandFateDriftinCellsfrom wemeasuredthetranscriptionalnoisewithincelltypesanddo-
OlderDonors norsusingestimatesbasedonEuclideandistance(FigureS1C)
The large span of donor ages (z6 decades), allowed us to and Pearson correlation as a fraction of technical error (Fig-
assess the effect of organismal aging at the single-cell level. ure1C).Bothmethodsindicatedincreasedtranscriptionalnoise
322 Cell171,321–330,October5,2017

Figure2. GeneExpressionChangesAssoci-
atedwithTranscriptionalNoise
(A)Expressionofcell-typical(INSforb-cells,GCG
for a-cells) and non-typical hormone in cells,
ranked by transcriptional noise. Dots represent
individualcells,lineisrunningmean,withk=n/5
(k=69forbcellsand199foracells).
(B) Organismal age and expression of stress-
related genes are strongly associated with tran-
scriptional noise. All genes were tested for
associationwithtranscriptionalnoise(linearrank
regression), shown are the top genes by coeffi-
cient,withFDR<1E-3.Heatmapshowsloessfit.
Rowsmarkedwithablackboxindicategenesthat
areassociatedwithresponsetostress(Yuetal.,
2015;Daugaardetal.,2007;Panenietal.,2013;
Tooneetal.,2001).
SeealsoFigureS2andTableS4.
in samples from older donors compared to samples from etal.,2014,2016;KasarandBrown,2016),manyofwhichcan
young adults and children, demonstrating age-dependent belinkedtospecificmutationalprocesses.However,thesesig-
transcriptionalnoise(p=3.01E(cid:1)11,n=2,544,forPearsonand natures are dominated by processes associated with tumor
p<1E-16,n=80,000forEuclidean,linearregression)without growthand only3outof 21suchsignatureshave beenlinked
changesincellularcomposition(FigureS1D). toagingintumorsororganoidculturesofstemcells(Alexandrov
Asubsetofa-cellsandb-cellssimultaneouslyexpressedboth etal.,2015;Blokzijletal.,2016).Post-mitoticcellsareespecially
Insulin(INS)andGlucagon(GCG)mRNA—aresultthatisconsis- difficult to study, because they cannot be clonally expanded.
tentwithpriorstudies(Blodgettetal.,2015;Xinetal.,2016;Kat- Thus,verylittleisknownaboutthemutationalprocessesthatop-
sutaetal.,2010)andthatweverifiedusinginsituRNAstaining erateontheterminallydifferentiatedcellsthatmakeupmostof
(Figures 1D and S2). scRNA-seq revealed that the fraction of ourbody.Todirectlystudymutationalsignaturesthatareactive
a- or b-cells co-expressing both Insulin and Glucagon mRNA in healthy tissue, we developed a computational method for
increased significantly with advancing age (Figure 1E, GCG in determining genetic variation within single cells using scRNA-
b-cells: p = 1.74E-27, n = 348; INS in a-cells: p = 5.38E-10, seqdataandvalidatedthemethodusingdeepwhole-genome
n = 998, linear regression). As expected, cells with high levels sequencing (see STAR Methods). Using this method, we
oftranscriptionalnoisealsoexpressmorecell-atypichormone compiled a catalog of putative somatic and constitutional
(Figure 2A). Thus, increasing numbers of cells with ‘‘atypical’’ (donor-specific germline) mutations from the 2,544 pancreas
hormone mRNA expression is emblematic of age-dependent cells together with 398 previously published single cells from
transcriptionalinstability,andsuch‘‘fatedrift’’suggestsaphys- adulthumanbrain(Darmanisetal.,2015).Wealsocompileda
iological basis for declining endocrine function, in spite of similarcatalogofclonalvariationwithin73cellsfromGP5dcolon
increased hormone secretion, in the aging pancreas (Chang cancer cells cultured in vitro (Figure 3A). We used synthetic
andHalter,2003;DeTata,2014). spike-in RNA (ERCC control) as an internal control, which al-
Weperformedlinearregressionongeneexpressionlevelsasa lowedustosiftouttechnicalartifacts,removing92.6%ofthese
functionofnoiserank(batchcorrectedandwithincelltype)to falsepositivecalls(FigureS3C).Further,weusedwholegenome
investigatewhetheranysystematicgeneexpressiondifferences sequencing data to benchmark our method of separating so-
accompanyanincreaseintranscriptionalnoise.AsshowninFig- matic substitutions from germline variation, with the majority
ure 2B, stress response genes such as FOSB, HSPA1A, and (67.4%) of putative somatic mutations being absent from
JUND were most highly associated with increasing transcrip- genomiccalls.Somaticsubstitutionswereenrichedinuntrans-
tional noise, supporting an aging paradigm that implicates lated regions of transcripts such as the 30UTR (p = 1.40E-32,
cellularstressinage-relatedpathology(Harman,1965). pairedttest,n=73)andalsoenrichedformutationsresulting
in codons that do not alter the amino acid sequence (Figures
AnalysisofSingleNucleotideVariantsinscRNA-Seq 3BandS5H).Asexpected,thevastmajorityofputativesomatic
DataRevealsCell-Type-SpecificSomaticSubstitutions substitutionswereobservedinonlyonecelleach(FigureS3A),
andNeuronalmRNAEditing indicatingthatthemethodisspecifictosomaticvariation.Sub-
AgingisaccompaniedbytheaccumulationofsomaticDNAsub- stitutioncallswereveryrareinlowcopy-numbertranscriptsand
stitutions,andthepatternofsomaticsubstitutionsinacellde- greatly enriched in high copy-number transcripts, while ERCC
pendsonthemutationalprocessesthatcausethem.Agrowing callswerenot(FiguresS3C–S3E),precludingthepossibilityofli-
bodyofdatafromtumorgenomeshasuncoveredamultitudeof brarypreparationartifactsbeingamajorsourceofsubstitution
suchmutationalsignatures(Alexandrovetal.,2013b;Nik-Zainal calls. Whereas low expressed transcripts often showed allelic
Cell171,321–330,October5,2017 323

Figure3. SomaticMutationProfilesDerivedfromSinglePrimaryHumanCells
(A)Substitutionratesforeachtypeofsubstitutioninthethreedatasets.Somaticsubstitutionratesweremorethanfivetimesashighinpancreasasinbrain
(2.74310(cid:1)6versus0.52310(cid:1)6),whereasgermlinesubstitutionratesweresimilarbetweenthetwo.Asexpected,therateofclonalsubstitutionsinthetumorcell-
line(GP5d)isseveralfoldhigherthangermlineratesinprimarytissue.
(B)Somaticsubstitutionsarestronglyenrichedonuntranslatedregionscomparedtogermlinesubstitutions.Barsaremean±SEM,n=73.
(C)Comparisonofrelativemutationratesofsingle-nucleotidesubstitutionsinthecontextofthenucleotideimmediately50ofthealteredbase.Differentsub-
stitutiontypesareseparatedbyboxeswiththesubstitutiontypeindicated(e.g.,C>A:CtoAtransversion).TherelativesubstitutionrateforC>Tsubstitutions
withinaCpGcontext,andT>Csubstitutionsishigherinbrainthanintheothertissuestested(p=6.38E-61andp=1.89E-17,respectively;Wilcoxontest,
n=2,544forpancreas,n=73forgp5d,andn=332forbrain).
(D) Detecting mRNA editing in brain samples. Shown is the number of splice site substitutions in the GRIA2 gene. T > C substitutions mapping to the
transcribed((cid:1))strand,correspondingtoadeninesubstitutedforguanineinthetranscribedRNA,arehighlyenrichedwhereasothersubstitutiontypesremainat
baselinelevels.InlayshowsmeannumberofGRIA2substitutionspercellforthethreedatasets,brainishighlyenrichedinsuchsubstitutions(p=5.40E-19.Bars
aremean±SEM,n=2,544forpancreas,n=3323forbrain,andn=73forGP5d).
SeealsoFigureS3.
imbalanceatheterozygousalleles,highlyexpressedgenesdid what was previously found for postmitotic brain cells (Lodato
not(FigureS3G),suggestingthatthemaindriverofallelicimbal- et al., 2015). Synthetic control RNA substitution rates were
ance was bursty gene expression rather than early cycle PCR similarbetweencelltypesofthepancreasandrepresentalower
errors.Somaticmutationratesexceedthetechnicalerrorrates leveloftechnicalnoiseinthemeasurement.Thus,analyzingthe
duetoamplificationandsequencingerror,asmeasuredbyinter- rawsequencereadsfromscRNA-seqdataallowsustodeter-
nalspike-incontrolsofsyntheticRNAincludedineachsingle- mine the mutational history of primary tissues as well as the
cellexperiment(Figure3A). clonalvariationinatumorcellline.
Toinvestigatepatternsofsomaticmutations,wedetermined BecauseweareanalyzingprocessedmRNAratherthanDNA,
therates(substitutionsperbasepair)ofthesixpossiblesingle our method can potentially be used to uncover systematic
nucleotidesubstitutionsineachcell.Singlecellsfrompancreas mRNAeditingeventsinadditiontoDNAsubstitutions.mRNAed-
hadamarkedlyhigheroverallrate(>5-fold)ofsomaticvariation iting is a controlled cellular process found in neuronal lineage
comparedtobraintissue(Figure3A),andtherewereconsider- cells,whereadenosineresiduesareconvertedtoinosine,result-
able differences also between cell types in the pancreas (Fig- inginT>Csubstitutionsonthetranscribedstrand.Todetermine
ure S3B), whereas we only observed small fluctuations in the whethermRNAeditingcanbedetectedusingourmethod,we
number of substitutions on ERCC control RNA from the same analyzed substitutions in the glutamate receptor GRIA2 gene,
cells(FigureS3C,redbars).However,ratesofC>Tsubstitutions whichisawell-knowntargetformRNAeditingatsplicejunctions
inaCpGdinucleotidecontext,knowntodeaminatespontane- (Higuchietal.,1993).Thisgeneisexpressedinbothendocrine
ouslywhenmethylated,andT>Csubstitutionswererelatively cells and brain cells, making a direct comparison possible.
higher in brain compared to pancreas (Figure 3C), in line with ConsistentwithmRNAeditingbeingspecifictoneurons,T>C
324 Cell171,321–330,October5,2017

Figure4. MutationalSignaturesDerivedfromscRNA-SeqData
(A)Single-nucleotidesubstitutionsin3,003cellsfrompancreas,brain,andthecoloncancercelllineGP5dwereorganizedintomutationalsignaturesusingnon-
negativematrixfactorizationfollowedbyagglomerativehierarchicalclustering.Barplotillustratesthepercentofmutationsattributedtoeachsubstitutiontypein
eachofthethreesignatures(S1–S3,left)andthefourexcludedsignatures(SC1–SC4,right).Colorsasin(A).Panelbelowthebarplotindicatesselectionitemsfor
determiningwhethertoexcludethesignature.Green,causeforinclusion;red,causeforexclusion.Bottompaneldenotesthepresenceofasignature(columns)in
acelltype(rows),withcolorscaleindicatingstrengthofsignatureasmediansubstitutionrateforcellsoftheindicatedtype.Blueboxesdenotesignificant
associationbetweensignatureloadanddonorage.BottomrowindicatesequivalentsignaturesfromAlexandrovetal.(2013b).
(B)Strandspecificitydiffersbetweencelltypes.Mutationswereannotatedbasedonwhetherthemutatedpyrimidineoccurredonthetranscribed((cid:1))orun-
transcribed(+)strand.Barsrepresentmean±SEMofrawsubstitutioncountsinendocrinecells(left)andbraincells(right).Notethatendocrinecellshaveastrong
strandbiasforthetranscribedstrandforC>A,C>G,andC>Tsubstitutions(p=1.00E-79,1.37e-28,and6.40E-34,respectively;Wilcoxontest,n=1,429)
previouslyobservedinoxidativestress-relatedtumorsignatures,whilebrainhasabiasforT>Csubstitutionsonthetranscribedstrand(p=3.41E-11;Wilcoxon
test,n=466)similartotumorsignature12(Alexandrovetal.,2013b).
(C)SignatureS2iscomposedoftwosub-signaturescorrespondingtocancersignatures1and6.ViolinplotshowC>TsubstitutionswithaprecedingGasa
fractionofallsubstitutionsinacell,whichisahallmarkofcancersignature6andthatseparatesGP5dandbraincells(p=7.156E-11;Wilcoxontest,n=73for
GP5dandn=332forbraincells).
SeealsoFigureS4andTablesS6andS7.
substitutionsinGRIA2occurredalmostexclusivelyinbraincells. (similartoAlexandrovetal.[2013a],seeSTARMethodsforde-
AmorepreciseanalysisoftheGRIA2splicesitesconfirmedthis tails) on the substitution rates of single cells (Figures 4A and
becausethesesiteswerehighlyenrichedinT>Csubstitutions S4).TheNMFanalysisalsoactsasasecondfilterforfalse-pos-
onthetranscribedstrand(Figure3D). itivesubstitutioncallsbyorderingsubstitutionsduetotechnical
artifactssuchasPCRerrorsintotheirownsignatures.Thus,we
EndocrineCellsDisplayaSpecificMutationalSignature excludedsignatureswithahighdegreeofsimilaritytothesubsti-
RelatedtoOxidativeStress tutionratesofthenegativecontrolRNA,lackingcell-typespec-
Toidentifythemutationalsignatures(S1–S3,SC4–SC7)thatun- ificity or positive age association, or with a very low signal
derlie the observed substitution rates, we used non-negative (excludedsignaturesSC4–SC7inFigure3A,seeSTARMethods
matrix factorization (NMF) followed by hierarchical clustering fordetails).
Cell171,321–330,October5,2017 325

Figure 5. The Genomic DNA in Pancreatic
Islets Are Highly Enriched in Oxidized
Guanine
(A)Pancreaticb-cellDNAisenrichedinoxidized
guanosine. Nuclear staining intensity of anti
8-OxoguanosineantibodywasquantifiedforINS-
positiveorINS-negativecells,fromthesameim-
ages.SlidesweretreatedwithRNasesoastoonly
measure oxidized bases on DNA. Bar plot in-
dicatesmean±SEM(p=7.30E-57;Wilcoxontest,
n=769b-cells,10,713non-isletcells.).
(B) Left: representative micrograph with 8-Ox-
oguanosineinmagentaandnuclearstain(DAPI)in
gray (scale bar, 50 mm). Right: insulin protein
stainingofthe sameregion.Insulin-positive islet
cellmassisatbottomleft,boundaryindicatedwith
orangeline.
(C)Pancreaticb-cellRNAismarginallyenrichedin
oxidizedguanosine.Cytoplasmicstainingintensity
of anti 8-Oxoguanosine antibody was quantified
forINS-positivebcellsandINS-negativecellsfrom
thesameslides.Barplotindicatesmean±SEM
(p = 9.5E-22, 1,239 b-cells, 21,048 surrounding
cells).
(D) Left: representative micrograph with 8-Ox-
oguanosineinmagentaandnuclearstain(DAPI)in
gray. Right: insulin protein staining of the same
region.INS-positiveisletcellmassboundaryindi-
catedwithorangeline.Scalebar,50mm.
SeealsoFigureS5.
TheS1signature(highrateofC>A,followedbyC>Gand preferencetooccuronthetranscribedstrandinendocrinecells,
C > T substitutions), and S3 signature (highly elevated rate of butnotinbraincells,consistentwithguanineoxidationdriving
T>Csubstitutions),werecell-type-specificsignatures,withS1 signatureS1(Figure4B).Takentogether,signatureS1appears
found in the endocrine pancreas and S3 in the brain. The S2 to be a novel, strand-specific mutational signature that is en-
signature was highly enriched in clonal variation within the riched in transcribed genes and that bears the hallmarks of
mismatchrepair-deficientGP5dcellline,withweakersignalin oxidativedamage.
brain. The pancreas-specific signature S1 was characterized Previouslarge-scaleeffortstodeciphercancer-specificmuta-
byC>Asubstitutions,withC>GandC>Tsubstitutionsatpro- tional signatures in bulk tumor genomes (Alexandrov et al.,
gressivelylowerrates.C>AandC>Gsubstitutionsareattrib- 2013b)discovered21uniquesignaturesbasedonthesubstitu-
utedtooxidationoftheguaninebase,creating8-Oxo-20-deoxy- tion type and the surrounding two bases. We reasoned that
guanosine(8-Oxo)thatmispairswithadenineandcanbefurther our signatures might have been also detected in the tumor
oxidizedtomispairwithguanine(Moriyaetal.,1991;Kinoand dataandcomparedthesignaturesbycollapsingtheirprobabili-
Sugiyama,2005),whereasC>Tsubstitutionsareattributedto ties into single-base substitution probabilities. Signature S3
oxidationofthecytosinebase(KreutzerandEssigmann,1998). foundinthisstudywasverysimilartotumorsignature12from
Consistentwithoxidationofguanosinedrivingthemutational Alexandrov et al. (2013b) (Figure S5D, Pearson correlation
signature of bcells, 8-hydroxyguanosine levels were markedly 0.971),andthecharacteristicT>Csubstitutionsinbraindisplay
elevatedintheDNAofbcellscomparedtonon-isletcells,while a similar degree of strand specificity to tumor signature 12
only modestly elevated in RNA (Figure 5). 8-Oxo substitutions (Figure4B).SignatureS2wasalmostidenticaltoboththeage-
preferentiallyoccurwhentheguanineisonthenon-transcribed dependenttumorsignature1andthemismatch repair-associ-
strand(Parketal.,2012;Alexandrovetal.,2013b),possiblydue atedtumorsignature6(FigureS5D,Pearsoncorrelation 0.975
to transcription-coupled nuclear excision repair of adducts on and 0.987, respectively). The major distinguishing feature
thetranscribedstrand(Banerjeeetal.,2011).Inordertodeter- betweenthetwotumorsignaturesistherateofC>Tsubstitu-
mineiftranscriptionalstrandbiasoccurredinourdata,weanno- tionswithinaGpCcontext.AsshowninFigure4B,thisdistin-
tated the single-base substitutions with whether the mutated guishing feature clearly separates the two tissues in our data,
pyrimidine was on the transcribed ((cid:1)) or untranscribed (+) suggesting that non-clonal substitutions in GP5d mainly stem
strand.Asexpected,C>AandC>Gsubstitutionshadastrong from faulty mismatch repair, whereas somatic substitutions in
326 Cell171,321–330,October5,2017

|     |     |     |     |     | Figure 6. | Transcriptional | Correlates of |
| --- | --- | --- | --- | --- | --------- | --------------- | ------------- |
MutationalSignatures
|     |     |     |     |     | Endocrine  | pancreas cells        | were ordered accord- |
| --- | --- | --- | --- | --- | ---------- | --------------------- | -------------------- |
|     |     |     |     |     | ing to the | fraction of mutations | attributed to        |
SignatureS1.
(A)AverageageishigherincellswithhighS1load
(p=5.95E-23,linearrankregression).Pointsare
runningmean,k=10,andlineisLoessfit,dotted
linesindicate±0.999confidenceinterval.
|     |     |     |     |     | (B) Each | gene was tested | for association with |
| --- | --- | --- | --- | --- | -------- | --------------- | -------------------- |
signatureS1(linearrankregression),shownarethe
|     |     |     |     |     | top genes | by coefficient, | with p < 1E-15 (FDR |
| --- | --- | --- | --- | --- | --------- | --------------- | ------------------- |
corrected).PointsareindividualmRNAmeasure-
ments,lineloessfitasin(A).
(C)Comparisonofthetoptengeneontology(GO)
categoriespositivelycorrelatedwithsignatureS1
|     |     |     |     |     | and transcriptional | noise.  | Categories related to |
| --- | --- | --- | --- | --- | ------------------- | ------- | --------------------- |
|     |     |     |     |     | protein production, | such as | ribosomal proteins,   |
recurinboth.ColorscaleindicatesFDR-adjusted
pvalue,winsorizedat10(cid:1)6.
SeealsoTableS5.
|     |     |     |     |     | S1 showing | the highest | significance |
| --- | --- | --- | --- | --- | ---------- | ----------- | ------------ |
(p=5.95E-23,Figures6AandS5).Signa-
|     |     |     |     |     | ture S2              | showed none | or little effect on |
| --- | --- | --- | --- | --- | -------------------- | ----------- | ------------------- |
|     |     |     |     |     | gene expression—only |             | 45 genes were       |
significantlyaffectedwithfalsediscovery
rate(FDR)<1E-3,noneofwhichwereup-
|     |     |     |     |     | regulated.      | PON2 (a membrane | protein       |
| --- | --- | --- | --- | --- | --------------- | ---------------- | ------------- |
|     |     |     |     |     | with a putative | antioxidant      | activity) and |
EGR1displayedthehighestupregulation
brainarecausedbythesameage-dependentprocessastumor associated with mutational load of the age-dependent S2 (at
signature1. FDR <0.05) (Figure S5; Table S6). Signature S1, on the other
Interestingly,tumorsignature5,whichisofunknownetiology hand,wasassociatedwithaconsiderabletranscriptionaleffect
andisfoundatlowlevelsinalltumortypes,ishighlyreminiscent (1,595genesatFDR<1E-3).Thegenesmosthighlyassociated
ofourfalsepositivesignature(FigureS5D,Pearsoncorrelation withhighS1loadwereinvolvedintranscription(TCEB2),protein
0.990)—suggestingthatitiseitheraproductoffalse-positivecalls synthesis(RPL36),andmodulationofROS(ROMO1)(Figure6B,
inthetumordatasetsorcausedbyamechanismsharedbetween seealsoTableS5foranexpandedlist).
humanreplicationandenzymesusedfornucleicacidamplifica- Genesetenrichmentanalysis(Subramanianetal.,2005)indi-
tion.None of the 21 tumorsignatures found to dateis directly catedthatpathwaysinvolvedinproteinsynthesiswerealteredin
relatedtoendogenousoxidativestress,andtheendocrinesigna- both cells withhighS1 loadand cells withhigh transcriptional
tureS1hasnodirectcounterpartamongthetumorsignatures. noise (Figure 6C). Further, signature S1 correlated with higher
Thestrongestcorrelationwastotumorsignature3(Pearson abundanceofthetumorsuppressorCDKN2A(p16)(FigureS4D,
correlation0.769),whichhasbeenfoundinpancreatic,breast, p=0.024,n=1,425,linearregression),acorrelationthatwasnot
andovariancancers,followedbysignature24(Pearsoncorrela- observed between transcriptional noise and CDKN2A expres-
tion 0.756), which is found in cancers resulting from aflatoxin sion (Figure S4C, p = 0.17, n = 1,425, linear regression) and
exposureviaoxidativestress-inducedDNAdamage.However, thatsuggeststhatevenlowlevelsofmutationalloadmightacti-
signature S1 only bears a passing resemblance to these two, vatethecell’stumorsuppressiveresponse.
andfurtherinvestigationintomutationalsignaturesofhealthytis-
| sueswillbeneededtoelucidatewhethersignatureS1isemblem- |                    |           |                     | DISCUSSION |     |     |     |
| ------------------------------------------------------ | ------------------ | --------- | ------------------- | ---------- | --- | --- | --- |
| atic of mainly                                         | post mitotic cells | with high | rate of metabolism, |            |     |     |     |
whichrarelyformtumors,orifitisspecifictoendocrinepancre- Cellularaginginlong-livedorganismsappearstobeacomplex
aticcells. stochastic process of gradual accumulation of errors (Lo´pez-
|     |     |     |     | Ot´ın et al., 2013). | Using single-cell | data, we | find that aging is |
| --- | --- | --- | --- | -------------------- | ----------------- | -------- | ------------------ |
MutationalLoadofSignatureS1IsHigherinEndocrine accompanied by both increased transcriptional noise and an
CellsfromOlderDonorsandCorrelatewithInductionof accumulationofgeneticerrors.Ithasbeenpreviouslysuggested
ProteinSynthesis-RelatedGenes thatDNAsubstitutionshaveadirectcausativeroleintranscrip-
Rankingofcellsbysignature-specificmutationalloadindicated tional instability (Vijg, 2004). However, as shown in this work
thatsignaturesS1andS2werehighlycorrelatedwithage,with and by others (Lodato et al., 2015), the mutational burden in
|     |     |     |     |     | Cell171,321–330,October5,2017 |     | 327 |
| --- | --- | --- | --- | --- | ----------------------------- | --- | --- |

singlecellsisontheorderofonetoafewthousandsubstitutions theinformationoncellidentityprovided bymRNA-sequencing
genome-wideandisunlikelytoaffecttheexpressionofalarge is lost. Our methods for determining transcriptional noise and
enough number of genes or regulatory elements to have an foridentifyingmutationalsignaturesfromscRNA-seqdatapro-
impact on overall transcriptional noise. If there were a causal vide a meansto study these features in arbitrarily specific cell
linkbetweenmutationalloadandtranscriptionalnoise,wewould populations from primary tissue, irrespective of the replicative
expectthecorrelationbetweenthesetwofeaturestobeconsid- potential of the cells. Such methods applied to much larger
erably stronger than a correlation of either feature with organ- donor cohorts, and different tissue types could be a crucial
ismal age. By contrast, we would expect similar correlations tool for understanding aging and other stochastic processes
betweenallthreeofthesefeaturesifmutationalloadandtran- thatactonsinglecells.
scriptional noise were independently acquired with age. Our
data support the absence of a causal link between mutational STAR+METHODS
load and transcriptional noise. In fact, the correlation of either
transcriptionalnoiseorsignatureS1withagewasslightlystron- Detailedmethodsareprovidedintheonlineversionofthispaper
gerthanthecorrelationbetweenmutationalloadandtranscrip- andincludethefollowing:
tional noise (age–noise: p = 2.94E-11, age–S1: p = 5.29E-16,
noise–S1: p = 4.83E-11. Two-sided Pearson correlation test, d KEYRESOURCESTABLE
n = 1,429). Thus, our single-cell approach seems to suggest d CONTACTFORREAGENTANDRESOURCESHARING
that aging is characterized by a gradual accumulation of both d EXPERIMENTALMODELSANDSUBJECTDETAILS
epigenetic andgenetic errors in astochastic and independent d METHODDETAILS
fashion. B FlowCytometry
Importantly,theaccrualofepigeneticerrorsislikelytocausea B Single-CellRNA-Seq
drift incellfate,assuggestedbyanincreaseinnon-cell-type- B Genomicsequencing
specifichormoneexpressioninendocrinecells.Such‘‘fatedrift’’ B InsituRNAandproteinstaining
could help explain the decrease in fitness and organ function d QUANTIFICATIONANDSTATISTICALANALYSIS
associatedwithaging.Inadditiontoidentifyingage-dependent B Numberofreplicatesused
mutational signatures and transcriptional noise, our findings B Single-cellRNA-seqDataAnalysis
refinedpreviousresultsonage-dependentincreaseinCDKN2A B Somatic mutational signatures in single-cell RNA-
geneexpression.WeidentifiedCDKN2Aexpressioninahigher seqdata
fractionofcellsinpancreatafromolderdonors,ratherthanan B Estimationoftranscriptionalnoise
increaseoftranscriptabundanceineverycell.Suchcellularhet- d DATAANDSOFTWAREAVAILABILITY
erogeneity suggests that the previously observed age-depen-
dent changes in CDKN2A expression (Arda et al., 2016) are SUPPLEMENTALINFORMATION
duetoeventsaffectingasubsetofcellsratherthananintrinsic
SupplementalInformationincludesfivefiguresandeighttablesandcanbe
programdictatingcellularaging.
foundwiththisarticleonlineathttp://dx.doi.org/10.1016/j.cell.2017.09.004.
Age-dependentdeclineinfunctionandregenerativepotential
hasbeenattributedpartiallytotheactivityofreactiveoxygenspe-
AUTHORCONTRIBUTIONS
ciesproducedbycellularmetabolism(Harman1965).Theage-
dependent mutational signature in the endocrine pancreas is M.E.,H.E.A.,S.K.K.,andS.R.Q.designedtheresearch.M.E.,H.E.A.,J.B.,and
characterizedbyahighrateofC>AandC>Gsubstitutions, M.M.performedresearch.R.B.isolatedtheislets.M.E.andS.R.Q.analyzed
which areselectively inducedby reactive oxygen species (Fig- thedata.M.E.,H.E.A.,M.M.,S.K.K.,andS.R.Q.wrotethepaper.
ureS5E)(KinoandSugiyama,2001,2005;Kamiyaetal.,2009).
ACKNOWLEDGMENTS
Pancreatic islet cells are sensitive to reactive oxygen species
due to low expression of antioxidant enzymes such as SOD1
The authors thank Norma Neff and Gary Mantalas for assistance with
(Tiedgeetal.,1997),arelativelyhighrateofATP-dependentpro- sequencingandSpyrosDarmanis,GeoffStanley,andFelixHornsforhelpful
cessessuchasproteinproductionandsecretion,andtherequire- discussions.ThisstudywassupportedbytheCaliforniaInstituteforRegener-
mentsforreducingpowertokeepinsulindisulfidebonded.Our ativeMedicine(GC1R-06673toS.R.Q.),theCenterofExcellenceforStemCell
results thus suggest that the age-specific mutational signature GenomicsandNIH(U01-HL099999andU01-HL099995toS.R.Q.),andbythe
NIH (UC4DK104211, DK10261201, and P30DK116074-01 to S.K.K.), the
observed in the endocrine pancreas is due to ROS-dependent
HelmsleyCharitableTrust(toS.K.K.),theH.L.SnyderFoundation(toS.K.K.),
lesionsonDNA.Interestingly,oxidativedamageispartofthepa-
theElserFoundation(toS.K.K.),andtheJDRF(toS.K.K.).M.E.wassupported
thologyoftypeIIdiabetes,andplasma8-hydroxyguanosineisa
by the Wallenberg Research link at Stanford University (KAW 2013.0391).
goodcorrelatetoendocrinedysfunction(Shinetal.,2001). H.E.A.wassupportedbyapostdoctoralfellowshipfromtheJDRF(3-APF-
Currentmethodsusedtostudysomaticmutationsrelyeither 2016-172-A-N)andanNIDDKtraininggranttotheEndocrinologyDivision,
onsingle-cellgenomicsequencingoronsequencingDNAfrom DepartmentofMedicine,Stanford(5T32DK007217-39).M.M.wassupported
many cells that stem from a clone that has been expanded bytheSwedishResearchCouncil(grant2015-00599).
in vitro (Blokzijl et al.,2016; Lodato etal., 2015; Gawad et al.,
Received:March23,2017
2016). Both families of methods are very costly, precluding
Revised:July2,2017
large-scaleexperimentsonthousandsofcells,andanalysisof Accepted:August30,2017
a specific cell type requires pre-selection of the cells because Published:September28,2017
328 Cell171,321–330,October5,2017

REFERENCES Higuchi,M.,Single,F.N.,Ko¨hler,M.,Sommer,B.,Sprengel,R.,andSeeburg,
P.H.(1993).RNAeditingofAMPAreceptorsubunitGluR-B:abase-paired
Alexander,M.P.,Begins,K.J.,Crall,W.C.,Holmes,M.P.,andLippert,M.J. intron-exonstructuredeterminespositionandefficiency.Cell75,1361–1370.
(2013).HighlevelsoftranscriptionstimulatetransversionsatGCbasepairs Kamiya, H., Suzuki, A., Yamaguchi, Y., Handa, H., and Harashima, H.
inyeast.Environ.Mol.Mutagen.54,44–53. (2009). Incorporation of 8-hydroxyguanosine (8-oxo-7,8-dihydroguanosine)
Alexandrov,L.B.,Nik-Zainal,S.,Wedge,D.C.,Campbell,P.J.,andStratton, 50-triphosphate by bacterial and human RNA polymerases. Free Radic.
M.R.(2013a).Decipheringsignaturesofmutationalprocessesoperativeinhu- Biol.Med.46,1703–1707.
mancancer.CellRep.3,246–259. Kasar,S.,andBrown,J.R.(2016).Mutationallandscapeandunderlyingmuta-
Alexandrov,L.B.,Nik-Zainal,S.,Wedge,D.C.,Aparicio,S.A.,Behjati,S.,Bian- tional processes in chronic lymphocytic leukemia. Mol. Cell. Oncol. 3,
kin,A.V.,Bignell,G.R.,Bolli,N.,Borg,A.,Børresen-Dale,A.L.,etal.;Australian e1157667.
PancreaticCancerGenomeInitiative;ICGCBreastCancerConsortium;ICGC Katsuta,H.,Akashi,T.,Katsuta,R.,Nagaya,M.,Kim,D.,Arinobu,Y.,Hara,M.,
MMML-Seq Consortium;ICGCPedBrain(2013b).Signaturesofmutational Bonner-Weir, S., Sharma, A.J., Akashi, K., and Weir, G.C. (2010). Single
processesinhumancancer.Nature500,415–421. pancreaticbetacellsco-expressmultipleislethormonegenesinmice.Diabe-
Alexandrov,L.B.,Jones,P.H.,Wedge,D.C.,Sale,J.E.,Campbell,P.J.,Nik- tologia53,128–138.
Zainal,S.,andStratton,M.R.(2015).Clock-likemutationalprocessesinhu- Ke,R.,Mignardi,M.,Pacureanu,A.,Svedlund,J.,Botling,J.,Wa¨hlby,C.,and
mansomaticcells.Nat.Genet.47,1402–1407. Nilsson,M.(2013).InsitusequencingforRNAanalysisinpreservedtissueand
Anders,S.,Pyl,P.T.,andHuber,W.(2014).HTSeq–aPythonframeworkto cells.Nat.Methods10,857–860.
workwithhigh-throughputsequencingdata.Bioinformatics31,166–169. Kino,K.,andSugiyama,H.(2001).PossiblecauseofG-C–>C-Gtransversion
Arda,H.E.,Li,L.,Tsai,J.,Torre,E.A.,Rosli,Y.,Peiris,H.,Spitale,R.C.,Dai,C., mutationbyguanineoxidationproduct,imidazolone.Chem.Biol.8,369–378.
Gu,X.,Qu,K.,etal.(2016).Age-dependentpancreaticgeneregulationreveals Kino,K.,andSugiyama,H.(2005).UVR-inducedG-CtoC-Gtransversions
mechanismsgoverninghumanbεcellfunction.CellMetab.23,909–920.
fromoxidativeDNAdamage.Mutat.Res.571,33–42.
Bahar,R.,Hartmann,C.H.,Rodriguez,K.A.,Denny,A.D.,Busuttil,R.A.,Dolle´, Kreutzer,D.A.,andEssigmann,J.M.(1998).Oxidized,deaminatedcytosines
M.E.T.,Calder,R.B.,Chisholm,G.B.,Pollock,B.H.,Klein,C.A.,andVijg,J. are a source of C–> T transitions in vivo. Proc. Natl. Acad. Sci. USA 95,
(2006).Increasedcell-to-cellvariationingeneexpressioninageingmouse 3578–3582.
heart.Nature441,1011–1014.
Li,H.,andDurbin,R.(2010).Fastandaccuratelong-readalignmentwithBur-
Banerjee,D.,Mandal,S.M.,Das,A.,Hegde,M.L.,Das,S.,Bhakat,K.K.,Bol- rows-Wheelertransform.Bioinformatics26,589–595.
dogh,I.,Sarkar,P.S.,Mitra,S.,andHazra,T.K.(2011).Preferentialrepairof
Li,J.,Klughammer,J.,Farlik,M.,Penz,T.,Spittler,A.,Barbieux,C.,Berishvili,
oxidizedbasedamageinthetranscribedgenesofmammaliancells.J.Biol.
E.,Bock,C.,andKubicek,S.(2016).Single-celltranscriptomesrevealcharac-
Chem.286,6006–6016.
teristicfeaturesofhumanpancreaticisletcelltypes.EMBORep.17,178–187.
Blodgett,D.M.,Nowosielska,A.,Afik,S.,Pechhold,S.,Cura,A.J.,Kennedy,
Lodato,M.A.,Woodworth,M.B.,Lee,S.,Evrony,G.D.,Mehta,B.K.,Karger,A.,
N.J.,Kim,S.,Kucukural,A.,Davis,R.J.,Kent,S.C.,etal.(2015).Novelobser-
Lee,S.,Chittenden,T.W.,D’Gama,A.M.,Cai,X.,etal.(2015).Somaticmuta-
vationsfromnext-generationRNAsequencingofhighlypurifiedhumanadult
tioninsinglehumanneuronstracksdevelopmentalandtranscriptionalhistory.
andfetalisletcellsubsets.Diabetes64,3172–3181.
Science350,94–98.
Blokzijl,F.,deLigt,J.,Jager,M.,Sasselli,V.,Roerink,S.,Sasaki,N.,Huch,M.,
Lo´pez-Otı´n, C., Blasco, M.A., Partridge, L., Serrano, M., and Kroemer, G.
Boymans,S.,Kuijk,E.,Prins,P.,etal.(2016).Tissue-specificmutationaccu-
(2013).Thehallmarksofaging.Cell153,1194–1217.
mulationinhumanadultstemcellsduringlife.Nature538,260–264.
Martin, M. (2011). Cutadapt removes adapter sequences from high-
Chang, A.M., and Halter, J.B. (2003). Aging and insulin secretion. Am. J.
throughputsequencingreads.EMBnetj.17,10–12.
Physiol.Endocrinol.Metab.284,E7–E12.
McKenna,A.,Hanna,M.,Banks,E.,Sivachenko,A.,Cibulskis,K.,Kernytsky,
Chen,H.,Gu,X.,Liu,Y.,Wang,J.,Wirt,S.E.,Bottino,R.,Schorle,H.,Sage,J.,
A.,Garimella,K.,Altshuler,D.,Gabriel,S.,Daly,M.,andDePristo,M.A.(2010).
andKim,S.K.(2011).PDGFsignallingcontrolsage-dependentproliferationin
TheGenomeAnalysisToolkit:aMapReduceframeworkforanalyzingnext-
pancreaticb-cells.Nature478,349–355.
generationDNAsequencingdata.GenomeRes.20,1297–1303.
Darmanis,S.,Sloan,S.A.,Zhang,Y.,Enge,M.,Caneda,C.,Shuer,L.M.,Hay-
Mignardi,M.,Mezger,A.,Qian,X.,LaFleur,L.,Botling,J.,Larsson,C.,and
denGephart,M.G.,Barres,B.A.,andQuake,S.R.(2015).Asurveyofhuman
Nilsson, M. (2015). Oligonucleotide gap-fill ligation for mutation detection
braintranscriptomediversityat thesingle celllevel.Proc.Natl.Acad. Sci.
andsequencinginsitu.NucleicAcidsRes.43,e151.
USA112,7285–7290.
Moriya,M.,Ou,C.,Bodepudi,V.,Johnson,F.,Takeshita,M.,andGrollman,
Daugaard,M.,Rohde,M.,andJa¨a¨ttela¨,M.(2007).Theheatshockprotein70
A.P.(1991).Site-specificmutagenesisusingagappedduplexvector:astudy
family:Highlyhomologousproteinswithoverlappinganddistinctfunctions.
oftranslesionsynthesispast8-oxodeoxyguanosineinE.coli.Mutat.Res.254,
FEBSLett.581,3702–3710.
281–288.
DeTata,V.(2014).Age-relatedimpairmentofpancreaticBeta-cellfunction:
Muraro,M.J.,Dharmadhikari,G.,Gru¨n,D.,Groen,N.,Dielen,T.,Jansen,E.,
pathophysiologicalandcellularmechanisms.Front.Endocrinol.(Lausanne)
vanGurp,L.,Engelse,M.A.,Carlotti,F.,deKoning,E.J.,andvanOudenaar-
5,138.
den,A.(2016).Asingle-celltranscriptomeatlasofthehumanpancreas.Cell
Dobin,A.,Davis,C.A.,Schlesinger,F.,Drenkow,J.,Zaleski,C.,Jha,S.,Batut, Syst.3,385–394.e3.
P.,Chaisson,M.,andGingeras,T.R.(2013).STAR:ultrafastuniversalRNA-seq
Nik-Zainal,S.,Wedge,D.C.,Alexandrov,L.B.,Petljak,M.,Butler,A.P.,Bolli,
aligner.Bioinformatics29,15–21.
N.,Davies,H.R.,Knappskog,S.,Martin,S.,Papaemmanuil,E.,etal.(2014).
Gaujoux,R.,andSeoighe,C.(2010).AflexibleRpackagefornonnegativema- Association of a germline copy number polymorphism of APOBEC3A and
trixfactorization.BMCBioinformatics11,367. APOBEC3BwithburdenofputativeAPOBEC-dependentmutationsinbreast
Gawad,C.,Koh,W.,andQuake,S.R.(2016).Single-cellgenomesequencing: cancer.Nat.Genet.46,487–491.
currentstateofthescience.Nat.Rev.Genet.17,175–188. Nik-Zainal,S.,Davies,H.,Staaf,J.,Ramakrishna,M.,Glodzik,D.,Zou,X.,
Gonitel, R., Moffitt, H., Sathasivam, K., Woodman, B., Detloff, P.J., Faull, Martincorena,I.,Alexandrov,L.B.,Martin,S.,Wedge,D.C.,etal.(2016).Land-
R.L.M.,andBates,G.P.(2008).DNAinstabilityinpostmitoticneurons.Proc. scapeofsomaticmutationsin560breastcancerwhole-genomesequences.
Natl.Acad.Sci.USA105,3467–3472. Nature534,47–54.
Harman,D.(1965).Thefreeradicaltheoryofaging:effectofageonserumcop- Paneni,F.,Osto,E.,Costantino,S.,Mateescu,B.,Briand,S.,Coppolino,G.,
perlevels.J.Gerontol.20,151–153. Perna,E.,Mocharla,P.,Akhmedov,A.,Kubant,R.,etal.(2013).Deletionof
Cell171,321–330,October5,2017 329

theactivatedprotein-1transcriptionfactorJunDinducesoxidativestressand Toone,W.M.,Morgan,B.A.,andJones,N.(2001).RedoxcontrolofAP-1-like
acceleratesage-relatedendothelialdysfunction.Circulation127,1229–1240. factorsinyeastandbeyond.Oncogene20,2336–2346.
Park,C.,Qian,W.,andZhang,J.(2012).Genomicevidenceforelevatedmu- VanderAuwera,G.A.,Carneiro,M.O.,Hartl,C.,Poplin,R.,DelAngel,G.,Levy-
tationratesinhighlyexpressedgenes.EMBORep.13,1123–1129. Moonshine,A.,Jordan,T.,Shakir,K.,Roazen,D.,Thibault,J.,etal.(2013).
Picelli, S., Faridani, O.R., Bjo¨rklund, A.K., Winberg, G., Sagasser, S., and FromFastQdatatohighconfidencevariantcalls:theGenomeAnalysisToolkit
Sandberg, R. (2014). Full-length RNA-seq from single cells using Smart- bestpracticespipeline.Curr.Protoc.Bioinformatics43,11.10.1–11.10.33.
seq2.Nat.Protoc.9,171–181.
vanderMaaten,L.,andHinton,G.(2008).VisualizingdatausingT-SNE.JMLR
Segerstolpe,A˚.,Palasantza,A.,Eliasson,P.,Andersson,E.M.,Andre´asson,
9,2579–2605.
A.C.,Sun,X.,Picelli,S.,Sabirsh,A.,Clausen,M.,Bjursell,M.K.,etal.(2016).
Single-celltranscriptomeprofilingofhumanpancreaticisletsinhealthand Vijg,J.(2004).Impactofgenomeinstabilityontranscriptionregulationofaging
type2diabetes.CellMetab.24,593–607. andsenescence.Mech.AgeingDev.125,747–753.
Shin,C.S.,Moon,B.S.,Park,K.S.,Kim,S.Y.,Park,S.J.,Chung,M.H.,andLee, Wang,Y.J.,Schug,J.,Won,K.J.,Liu,C.,Naji,A.,Avrahami,D.,Golson,M.L.,
H.K.(2001).Serum8-hydroxy-guanine levelsareincreasedindiabeticpa- andKaestner,K.H.(2016).Single-celltranscriptomicsofthehumanendocrine
tients.DiabetesCare24,733–737. pancreas.Diabetes65,3028–3038.
Subramanian,S.,andKumar,S.(2003).Neutralsubstitutionsoccuratafaster
Warren,L.A.,Rossi,D.J.,Schiebinger,G.R.,Weissman,I.L.,Kim,S.K.,and
rateinexonsthaninnoncodingDNAinprimategenomes.GenomeRes.13,
Quake,S.R.(2007).Transcriptionalinstabilityisnotauniversalattributeofag-
838–844.
ing.AgingCell6,775–782.
Subramanian,A.,Tamayo,P.,Mootha,V.K.,Mukherjee,S.,Ebert,B.L.,Gil-
lette, M.A., Paulovich, A., Pomeroy, S.L., Golub, T.R., Lander, E.S., and Xin,Y.,Kim,J.,Ni,M.,Wei,Y.,Okamoto,H.,Lee,J.,Adler,C.,Cavino,K.,Mur-
Mesirov, J.P. (2005). Gene set enrichment analysis: a knowledge-based phy,A.J.,Yancopoulos,G.D.,etal.(2016).UseofthefluidigmC1platformfor
approach for interpreting genome-wide expression profiles. Proc. Natl. RNAsequencingofsinglemousepancreaticisletcells.Proc.Natl.Acad.Sci.
Acad.Sci.USA102,15545–15550. USA113,3293–3298.
Tiedge,M.,Lortz,S.,Drinkgern,J.,andLenzen,S.(1997).Relationbetween Yu,Y.,Cai,Z.,Cui,M.,Nie,P.,Sun,Z.,Sun,S.,Chu,S.,Wang,X.,Hu,L.,Yi,J.,
antioxidantenzymegeneexpressionandantioxidativedefensestatusofinsu- etal.(2015).TheorphannuclearreceptorNur77inhibitslowshearstress-
lin-producingcells.Diabetes46,1733–1742. inducedcarotidarteryremodelinginmice.Int.J.Mol.Med.36,1547–1555.
330 Cell171,321–330,October5,2017

STAR+METHODS
KEYRESOURCESTABLE
| REAGENTorRESOURCE | SOURCE | IDENTIFIER |
| ----------------- | ------ | ---------- |
Antibodies
| HPx1-Dylight488        | Novus          | NBP1-18951G |
| ---------------------- | -------------- | ----------- |
| HPi2-Dylight650        | Novus          | NBP1-18946C |
| CD133/1–Biotin         | MiltenyiBiotec | 130-090-664 |
| CD133/2–Biotin         | MiltenyiBiotec | 130-090-852 |
| Streptavidin-eFluor780 | eBioscience    | 47-4317-82  |
| Streptavidin-APC       | eBioscience    | 17-4317-82  |
| antihumanEpCAM-        | Biolegend      | 324208      |
APC,
| AntihumanInsulin  | DAKO        | A0564     |
| ----------------- | ----------- | --------- |
| AntihumanGlucagon | Sigma       | G2654     |
| 8-oxo-dGmouseAb   | MyBioSource | MBS606843 |
BiologicalSamples
| Humanpancreaticsamples | IntegratedIsletDistribution | N/A |
| ---------------------- | --------------------------- | --- |
Network(IIDP),
| Humanpancreaticsamples | UCSFIsletIsolationCore | N/A |
| ---------------------- | ---------------------- | --- |
(SanFrancisco,CAUSA)
| Humanpancreaticsamples | InternationalInstituteforthe | N/A |
| ---------------------- | ---------------------------- | --- |
AdvancementofMedicine(IIAM)
Chemicals,Peptides,andRecombinantProteins
| Antifadegold | Invitrogen   | P36930   |
| ------------ | ------------ | -------- |
| UNG          | ThermoFisher | N8080096 |
CriticalCommercialAssays
| NexteraXT                | Illumina       | FC-131-1096 |
| ------------------------ | -------------- | ----------- |
| KAPAHiFiHotStartReadyMix | KAPABiosystems | KK2601      |
DepositedData
| SinglecellmRNA-seqdata | Thispaper | GEO:GSE81547 |
| ---------------------- | --------- | ------------ |
ExperimentalModels:CellLines
| GP5dcolonadenocarcinomacellline | Sigma-Aldrich | 95090715 |
| ------------------------------- | ------------- | -------- |
Oligonucleotides
| GCGprimerforstaining: | Thispaper | N/A |
| --------------------- | --------- | --- |
G+TC+TC+TC+AA+AT+TC+ATCGTGACGTTT
| INSprimerforstaining: | Thispaper | N/A |
| --------------------- | --------- | --- |
G+CA+CC+AG+GGC+CCC+CGCCCAGCTCCA
| GCGpadlockprobe: | Thispaper | N/A |
| ---------------- | --------- | --- |
Phosp-GAATAACATTGCCAAACGTGTGTCTATTTAG
TGGATCCCGTGCGCCTGGTAGCAATTAGCT
CCACTGTTACTAGATTGGAATACCAAGAGGA
ACAG
| INSpadlockprobe: | Thispaper | N/A |
| ---------------- | --------- | --- |
Phosp-AGGTGGGGCAGGTGGAGCCTCAATGCTGC
TGCTGTACTCTACGATTTTACCAGTTGCCCT
AGATGTTCCGCTATTGTCCGGGAGGCAGAG
GACCTGC
(Continuedonnextpage)
Cell171,321–330.e1–e7,October5,2017 e1

Continued
REAGENTorRESOURCE SOURCE IDENTIFIER
SmartSeq2OligodT: Picellietal.,2014 N/A
50–AAGCAGTGGTATCAACGCAGAGTACT30VN-
30
SmartSeq2TSO: Picellietal.,2014 N/A
50-AAGCAGTGGTATCAACGCAGAGTACATrGrG
+G-30
SmartSeq2ISPCR: Picellietal.,2014 N/A
50-AAGCAGTGGTATCAACGCAGAGT-30
DetectionprobesforinsituRNAstaining–seeTableS8 Thispaper N/A
SoftwareandAlgorithms
GATKpipeline McKennaetal.,2010;Vander https://software.broadinstitute.
Auweraetal.,2013 org/gatk/
HTSeq Andersetal.,2014 https://github.com/simon-
anders/htseq
STAR Dobinetal.,2013 https://github.com/alexdobin/STAR
GSEA Subramanianetal.,2005 software.broadinstitute.org/gsea
Picard McKennaetal.,2010 https://broadinstitute.github.io/picard/
TSNE vanderMaatenandHinton,2008 https://github.com/jdonaldson/rtsne/
CONTACTFORREAGENTANDRESOURCESHARING
FurtherinformationandrequestsforresourcesandreagentsshouldbedirectedtoandwillbefulfilledbytheLeadContact,Stephen
R.Quake(quake@stanford.edu).
EXPERIMENTALMODELSANDSUBJECTDETAILS
AllstudiesinvolvinghumanpancreasorisletswereconductedinaccordancewithStanfordUniversityInstitutionalReviewBoard
guidelines,includinginformedconsentfortissuedonationfromallsubjects.De-identifiedhumanpancreataorisletswereobtained
frompreviouslyhealthy,non-diabeticorgandonorswithBMI<30,lessthan15hrofcoldischemiatime,anddeceasedduetoacute
traumaoranoxia.OrgansandisletswereprocuredthroughIntegratedIsletDistributionNetwork(IIDP),NationalDiabetesResearch
Institute (NDRI),UCSFIsletIsolationCore(SanFrancisco, CAUSA) andInternational InstitutefortheAdvancementofMedicine
(IIAM). For FACS, scRNA-seqstudies islets from threejuvenile (ages1 month-old, 5,6),and five adult donors (ages21, 22, 38,
44,54years)wereused.Forimmunostainingstudiespancreatictissuesectionsfroma31-year-olddonorwereused.
Tissuefrombothmaleandfemaledonorswereused,ananalysisofsystematicinfluenceofsexontheresultsisincludedinFig-
ureS1B.Subjectswerenotinvolvedinpreviousstudies.FurtherdonordetailsareprovidedinTableS1.
VerifiedGP5dcells(colonadenocarcinomafromhumanfemaleCaucasian)wereobtainedfromSigma-Aldrich(95090715),and
onlyfirst-passagecellswereusedinthisstudy.
METHODDETAILS
FlowCytometry
IsolatedhumanisletsweredissociatedintosinglecellsbyenzymaticdigestionusingAccumax(Invitrogen).Priortoantibodystaining,
cellswereincubatedwithblockingsolutioncontainingFACSbuffer(2%v/vfetalbovineseruminPBSandgoatIgG[JacksonLabs],
11.2mgpermillioncells).LIVE/DEADFixableAquaDeadCellDye(LifeTechnologies)wasusedasaviabilitymarker.Cellswerethen
stainedwithappropriateantibodiesat1:100(v/v)finalconcentration.ThefollowingantibodieswereusedforFACSexperiments:
HPx1-Dylight 488 (Novus, NBP1-18951G), HPi2-Dylight 650(Novus, NBP1-18946C), CD133/1 - Biotin (MiltenyiBiotec 130-090-
664), CD133/2 - Biotin (Miltenyi Biotec 130-090-852), streptavidin-eFluor780 (eBioscience, 47-4317-82), streptavidin-APC
(eBioscience,17-4317-82),antihumanEpCAM-APC(Biolegend,324208).Cellsweresortedonaspecialorder5-laserFACSAria
II(BDBiosciences)usinga100mnozzlefollowingdoubletremoval.Sortedsinglecellswerecollecteddirectlyinto96-wellplates
(Bio-Radcat#:HSP9601)containing4mLoflysisbufferwithdNTPs(Picellietal.,2014)fordownstreamsingle-cellRNA-seqassays.
e2 Cell171,321–330.e1–e7,October5,2017

Single-CellRNA-Seq
Single-cellRNA-seqlibrariesweregeneratedasdescribed(Picellietal.,2014).Single-cellscollectedin96-wellplateswerelysed,
followedbyreversetranscriptionwithtemplate-switchusinganLNA-modifiedtemplateswitcholigotogeneratecDNA.After21cy-
clesofpre-amplification,DNAwaspurifiedandanalyzedonanautomatedFragmentAnalyzer(AdvancedAnalytical).Eachcell’s
cDNA fragment profile was individually inspected and only wells with successful amplification products (concentration higher
than0.06ng/ul)andwithnodetectableRNAdegradationwereselectedforfinallibrarypreparation.Tagmentationassaysandbar-
codedsequencinglibrarieswerepreparedusingNexteraXTkit(Illumina)accordingtothemanufacturer’sinstructions.Barcoded
librarieswerepooledandsubjectedto75bppaired-endsequencingontheIlluminaNextSeqinstrument.
Genomicsequencing
GenomicvariantsweredeterminedfromwholegenomesequencingdatafollowingGATKBestPractices(VanderAuweraetal.,
2013).Adaptersandlowqualitybasesweretrimmedusingcutadaptv1.9(VanderAuweraetal.,2013;Martin,2011).Readswere
alignedtohg19usingBWA-MEM0.7.12(LiandDurbin,2010).DuplicateswereremovedusingPicardtoolsv1.119followedbyindel
realignmentandbaserecalibrationusingGATKv3.5(McKennaetal.,2010).Variantswerecalledusinghaplotypecallerandrecali-
brated using VQSR. Default software parameters were used and reference files downloaded from the GATK Resource Bundle
2.8/hg19.
InsituRNAandproteinstaining
MultiplexRNAstainingwasperformedon10mmthick,formalin-fixed,tissuesectionsusingbarcodedtranscript-specificpadlock
probesandrollingcircleamplification(RCA)asdescribedbefore(Keetal.,2013).Theprimersequenceswere
GCG:G+TC+TC+TC+AA+AT+TC+ATCGTGACGTTT
INS:G+CA+CC+AG+GGC+CCC+CGCCCAGCTCCA
Padlockprobes
GCG:Phosp-GAATAACATTGCCAAACGTGTGTCTATTTAGTGGATCCCGTGCG
CCTGGTAGCAATTAGCTCCACTGTTACTAGATTGGAATACCAAGAGGAACAG
INS:Phosp-AGGTGGGGCAGGTGGAGCCTCAATGCTGCTGCTGTACTCTACG
ATTTTACCAGTTGCCCTAGATGTTCCGCTATTGTCCGGGAGGCAGAGGACCTGC
Detectionprobes
DO_1_FITC:AGUCGGAAGUACTACTCUCT_FITC
DO_1_Cy3:CCUCAATGCUGCTGCTGUAC_Cy3
DO_1_Cy5:TGUGTCTATUTAGTGGAUCC_Cy5
DO_2_FITC:CGUGCGCCUGGTAGCAAUTA_FITC
DO_2_Cy3:AGUAGCCGUGACTATCGUCT_Cy3
DO_2_Cy5:TCUACGATUTTACCAGTUGC_Cy5
DO_3_FITC:CCUAGATGTUCCGCTATUGT_FITC
DO_3_Cy3:GCUCCACTGUTACTAGAUTG_Cy3
DO_3_Cy5:CTUGTGCTGUATGATCGUCC_Cy5
The RCA products were stained by sequential hybridization of three uracil-containing fluorescent oligonucleotides following a
modified protocol from Ke 2013 (Ke et al., 2013). The three reported probes were mixed 0.1 mMeach with hybridization buffer
(20%formamidein2xSSC)andincubatedwiththetissueat37(cid:3)Cfor30’.Afterincubation,tissuesectionwaswashedinPBS50
andnucleiwerecounterstainedwithDAPI300nMinPBSatroomtemperaturefor15’.Thetissuewaswashedinethanol70,85
and100%50each,air-driedandmountedinAntifadegold(Invitrogen)beforeimaging.Afterimaging,thefluorescentprobeswere
removed bydigestion with0.02U/ml UNG (Thermo) in UNG buffer and 0.2mg/mlBSA at37(cid:3)C for30’ followed bytwo washes in
65%formamidepre-warmedat55(cid:3)C.ConsecutivestainingoftheRCAproductswereperformed,inthesameway,withdifferent
setoffluorescentprobes.
AfterRNA,immunofluorescentstainingwasdoneonthesametissuesection.ThetissuewaswashedtwiceinPBSwith0.025%
TritonX-100atroomtemperatureandblockedwith1%BSAinPBSfor2hratroomtemperature.AntibodiesagainsthumanInsulin
(DAKO,A0564,guineapig)andglucagon(Sigma,G2654,mouse)werediluted1%inPBScontaining1%BSAandappliedtothe
tissueandincubatedat4(cid:3)Covernight.ThetissuewaswashedtwiceinPBSwith0.025%TritonX-100beforeincubationwith1%
anti-guineapigGFPlabeledandanti-mouseCy5secondaryantibody,1%BSAinhybridizationbufferfor1hratroomtemperature.
Cy3-labeledRCAreporterprobeswerealsoaddedat0.1mMconcentrationtostainalltheRCAproductsandusedtoalignimmu-
nofluorescenceimagestopreviousRNAstaining.Afterincubationinsecondaryantibodythesectionwaswashed3timesin1xPBSat
roomtemperaturebeforemountinginAntifadegoldandimaging.For8-hydroxyguanosinestaining,8-oxo-dGAb(MyBioSource,
MBS606843,mouse)wasused,whichbindstotheoxidizedbasedbothinDNAandRNA.Tomeasurethelevelsofoxidizedgenomic
guanine,cellsweretreatedwithRNaseAbeforestainingaccordingtotheprotocolprovidedbythemanufacturer.Briefly,sections
Cell171,321–330.e1–e7,October5,2017 e3

wereincubatedinPBSbuffercontaining500mg/mlRNaseA(ThermoFisher),150mMNaCland15mMsodiumcitratefor1hrat37(cid:3)C.
AfterwashingthesampletwiceinPBStheDNAwasdenaturedbyincubatingwithHCl2Nfor50atroomtemperatureandthenneutral-
izedbyincubationwithTris-base50 atroomtemperaturefollowedbytwowashesinPBS.Blockingandantibodystainingagainst
humaninsulinand8-Hydroxy-20-deoxyguanosinewasperformedasdescribedbefore(anti8-oxo-dGwasusedat1:250dilution).
MultidimensionalimagingwasdonewithaZeissAxioplanepifluorescencemicroscopeequippedwithfilter-cubesforDAPI,FITC,
Cy3andCy5,aAxiocam506monocamera(Zeiss),automatedfilter-cubewheelandamotorizedstage.Zstacksof15imageswere
acquiredwithaPlan-Apochromat63xobjectiveandcheckobjective)severalfieldofviewofeachregionofinterestwereprojected
(maximumintensityprojection)andautomaticallystitchedusingtheAxiovisionsoftware(Zeiss).
Imageswereexportedassingle-channel16-bitgrayscaleandanalyzedasdescribedbefore(Keetal.,2013).Briefly,singlechan-
nelsimagesfromstainingcycleonewerecombinedandusedasmasktoalignimagesfromsubsequentcyclesbasedonnucleiand
RCAstaining.ImagealignmentwasdoneusingMultiStackRegmoduleofImageJ(version1.50e).Pre-alignedRNAimageswere
analyzedwithCellProfiler2.1.1(rev6c2d896)andintensityandpositionofRCAproductsweremeasuredusingthesamepipeline
asinMignardietal.(2015).ThebarcodedecodingwasobtainedusingthesameMATLABscriptasdescribedbefore(Keetal.,
2013). Lowering the quality threshold to zero (Qt = 0) allowed us to increase sensitivity of detection while the fraction of insulin
andglucagonesignalsdetectedoutsidetheislets(falsepositives)wasstillnegligible(lessthan0.3%ofallGCGandINSsignals).
Object-basedmeasurementofimmunostainingintensitywasdonewithCellProfileronthecorrespondingimagesusingtheidentified
RCAproductsasmask.
QUANTIFICATIONANDSTATISTICALANALYSIS
Numberofreplicatesused
Thenumberofbiologicaland/ortechnicalreplicatesforeachexperimentisstatedinthe‘‘MethodDetails’’sectionandthefigure
legends.
Single-cellRNA-seqDataAnalysis
Sequencingreadsweretrimmed,adaptorsequencesremovedandthereadsalignedtothehg19referenceassemblyusingSTAR
(Dobin etal.,2013)withdefaultparameters.Duplicate reads wereremoved usingpicard(McKennaetal.,2010).Raw transcript
counts were obtained using HT-Seq (Anders et al., 2014) and hg19 UCSC exon/transcript annotations. Transcript counts were
normalizedintologtransformedcountspermillion(CPM),byapplyingtheformulalog2(c *1000000/tc +1,wherec isthetran-
ij j ij
scriptcountsforgeneiincellj,andtc isthetotalnumberoftranscriptcountsforcellj.Singlecellprofileswiththefollowingfeatures
j
weredeemedtobeofpoorqualityandremoved:1)cellswithlessthan100.000totalnumberofvalidcountsonexonicregions.2)cells
withverylowactinCPM.TodetermineacutoffforactinCPM,weusedthenormaldistributionwithempiricalmeanandstandard
deviationfromactin.Thecutoffwassettothe0.01quantile(e.g.,thelower0.01%ofthebellcurve).
Table-SummaryofsequencedcellsSequencingstatisticsaremedianvalues.
PassedQC FailedQC
Cells 2544(94.9%) 136(5.1%)
Sequencingstatistics
alignedreads 932172 962153
transcriptsdetected 3203 1392
%aligned 78.54% 79.94%
%ERCC 8.06% 33.20%
%exonic(non-ERCC) 62.85% 29.03%
%mitochondrial 6.47% 10.53%
Pairwisedistancesbetweencellswereestimatedusingpearsoncorrelationonthe500mosthighlyexpressedgenes(byCPM)in
anyonecell.Dimensionalityreductionofthepairwisecorrelationmatrixwasperformedusingthet-SNEmethod(vanderMaatenand
Hinton,2008).
To determine Gene Ontology categories that were associated with transcriptional noise or signature specific mutational load,
weusedGeneSetEnrichmentAnalysis (GSEA),usingthecoefficients ofassociation tonoise/rank ofsignificantly alteredgenes
(p<1E-5,linearmodel,FDRcorrected).CoefficientswereusedasaprerankedlistintheGSEAsoftwareusingdefaultparameters
withthegenesetdatabase‘‘c5.all.v5.2.symbols.gmt,’’whichincludesallGOcategories.Statisticaloverrepresentationofgenesets
wasperformedusingthePANTHERoverrepresentationtest(pantherdb.org)usingthefullGObiologicalprocesscategorization.
e4 Cell171,321–330.e1–e7,October5,2017

Somaticmutationalsignaturesinsingle-cellRNA-seqdata
Toexploremutationalsignaturesinsinglepostmitoticcells,weanalyzedtherawsequencereadsfrommRNA-seq.Previously,muta-
tionalsignatureshavebeensuccessfullyextractedfromexomesequencing;however,usingsingle-celldataposesanumberofaddi-
tionalchallenges.First,weneedtodealwiththehighererrorrateassociatedwithreversetranscriptionandahighernumberofPCR
cycles.Wedothisintwoways-byincludingpositiveandnegativeinternalcontrolsforeachcell,thatareusedtoderiveameaningful
cutoffwhencallingsubstitutions,andbyperforminganadditionalpost-selectionofsignatures,discardingpotentialfalse-positives.
Second,thesequencespaceinasingle-cellRNA-seqexperimentistypicallyfairlylimited,evencomparedtoexomesequencing.We
mitigatethisissuebysequencinglongreads(75bppaired-end),andbysequencingdeeperthantypicallyneededforscRNA-seq
(approx.1Mmappedreadspercell).Further,wecalculatesubstitutionratesbasedontheactualnumberofsequencedkmersin
eachcell, toaccountfor differencesin basedistribution. Finally, the limitednumberofsubstitutionsineach cellmeansthatthe
sequencecontextcannotbereliablyincludedinallcases,whichiswhywegenerallyrestrictedourselvestoanalyzingsingle-base
substitutions.
RawvariationcallsweremadeusingtheHaplotypeCaller(GATKpipeline)(McKennaetal.,2010;VanderAuweraetal.,2013)
ontheBAMfilesafterapplyingSplitNCigarReadstoremoveoverhangsintointronicregions.Variantswerefilteredtoremoveclusters
(>3SNPswithin35bases),aswellasvariantswithQD<2.0andFS>30.0.Germlinemutationswerecalledusingamergedsetofall
single-cellprofilesfromeachpatient.Subsequently,wefilteredtherawvariationcallsbyapplyingvariantqualityscorerecalibration
usingtheGATKpipeline.Toreliablycallsubstitutionsweneedinternalcontrolsforeachcell,correspondingtoatrue-positiveand
true-negative set. We used known variants (dbSNP release 138) from our germline calls that mapped to transcribed regions of
thegenomeasatruepositiveset(phred-scaledprior:15.0)andvariantsthatmaptoERCCcontrolreadsasafalsepositiveset
(ERCCcontrolsaresyntheticRNAsequencesandthereforedevoidofsystematicvariation).Tofiltersomaticsubstitutions,astrict
cutoff, allowing 10% false negative rate was used. Variants also found in the germline were flagged as germline mutations and
notusedforsomaticsignatures.Inallsubsequentanalysis,onlysingle-nucleotidesubstitutionswereconsidered.
Foreachcell,weextractedthegenomiccontextofeachmutationandcreatedacatalogofthefrequencyofmutationtypes.We
thendividedthesefrequencieswiththekmercountsderivedfromfastqsequencesforthecelltoobtainthefinalsubstitutionrates.
NegativecontrolERCCsequenceswereprocessedinparallel,togiveaccuratesubstitutionratesthatreflectthedifferentsequence
background.SubstitutionratesintheseERCCsampleswere4.8E-7.Assumingthatfalse-positivesubstitutionsstemexclusively
from somatic calls (e.g., that the germline calls are completely devoid of false positives), this result indicates a false discovery
rate of 15.05% for somatic substitutions (excluding transcriptional errors, which are not accounted for by the ERCC controls).
Thus,weestimatethattheupperboundofourfalsediscoveryrateis15%.Tofurthervalidateourmethodweperformed25xwhole
genomesequencing(WGS)ofGP5dandcomparedtheoverlappingsubstitutioncallsfromsingle-cellmRNAseqandbulkgenomic
sequencing.Atotalof151,030genomicpositionsweredeterminedtohavesingle-basesubstitutionsfromthereferencegenome
basedonmRNA-seq.Outofthese151,030substitutioncalls,105,673werealsofoundinWGSand105,543wereidentical(concor-
dant).45357substitutions,or30.0%oftotal,werenotfoundinWGScalls;thesecallsincludesomaticsubstitutions,falsenegative
callsfromWGSandtechnicalerrors.Thesenumbersareinlinewiththepreviouslydeterminedfalse-positiverate(%15%),andso-
maticsubstitutionratesonhighlytranscribedDNA((cid:4)15%,seebelowfordiscussion).
Itwouldbeofinteresttoestimatetheabsolutenumberofsomaticsubstitutionsinthedifferenttissues.Onaverage,wefindthat
73.5%ofourrawsubstitutionscallsarecalledasgerm-linewiththerestconsistingmainlyofsomaticsubstitutions,false-positive
callsandgermlinesubstitutionsthatwereerroneouslycalledsomatic.BasedontheERCCerrorrateandNMFfilterning,weestimate
thenon-germlineerrorratetobe7%–15%,andbasedonWGSsequencingtherateofgermlinesubstitutionserroneouslycalled
somaticis32.6%.Thus,thefinalnumberofsomaticsubstitutionsinourmRNAdataisapproximately15%,which,ifextrapolated
linearly,wouldstillindicateatotalnumberofsomaticsubstitutionssignificantlyhigherthaneventhemutationalburdenofmanytu-
mors.However,wehavetotakeintoaccountthatwecanonlycallsubstitutionsinhighlyexpressedgenes.Codingregionsare
depletedingerm-linemutationsbecauseofnegativeselectionagainstnon-silentmutations.InourGP5dWGSdata,forexample,
weobserve one substitution from the hg19reference genome per 510bpgenome-wide, butonlyone per886 bpin exonic se-
quences.However,thetranscribedgenomegenerallyhasaconsiderablyhighersubstitutionratethanthenon-transcribedgenome
withincreasesofbetween(cid:4)2-foldand50-foldreporteddependingonthecelltypes/speciesandtheleveloftranscriptionalactivity
(SubramanianandKumar,2003;Alexanderetal.,2013).ThisbiasissostrongthatitisdetectableusingmRNA-seqdataalone–the
sensitivitytodetectsomaticsubstitutionsissignificantlymoredependentongeneexpressionlevelsthanthesensitivitytodetect
germlinesubstitutionsis(p<1E-16,linearmodeln=316234),eventhoughthesensitivitytocallbothtypesishighlydependent
onexpressionlevels.Becauseofthisintrinsiclimitationofthemethod,weavoidabsolutequantificationofsubstitutionratesandlimit
ourselves to relative quantification between samples. DNA-sequencing of brainsingle braincellsindicatedthatneurons contain
between1458and1580somaticsinglenucleotidevariants,whichweremostlyacquiredduringactivetranscriptioninpost-mitotic
cells(Lodatoetal.,2015),similarly towhatwefindforendocrine pancreascells. Thesomaticsubstitution ratein ourendocrine
pancreascellswas5.2-foldhigherthantherateinourbraindata(2.74E-6and0.52E-6substitutionsperbase,respectively),which
wouldindicateasomaticmutationalloadofbetween7582and8216substitutionspergenomeinendocrinepancreaticcells,given
thattheassociationwithactivetranscriptionissimilarbetweenthetwomutationalprocesses.
Asdescribedabove,classificationofsubstitutionsaseithergermlineorsomaticisdonebasedonscRNA-seqdatamergedoverall
cellsfromadonor.Becauseofthesparsityofthedata,somegermlinesubstitutionswillappeartobesomatic(e.g.,becalledina
Cell171,321–330.e1–e7,October5,2017 e5

singlecell,butnotinthemergeddata).Todeterminehowwellourmethodidentifiessomaticsubstitutions,weusedgermlinesub-
stitutionscalledfrombulkWGSofGP5dcoloncancercellsasagoldstandard.Thisanalysisindicatedthat32.6%oftheputative
somaticsubstitutionswereactuallygermlineSNPs.
Thus,weestimatetheoverallfalsediscoveryrateforsomaticsubstitutionsinourdata(beforeapplyingnonnegativematrixfactor-
izationandsignatureselection)tobeapproximately40%,whichincludes(cid:4)30%thatrepresentrealvariationstemmingfromgermline
rather than somatic events and (cid:4)10% substitution calls that were erroneously called due to technical errors such as PCR or
sequencingartifacts.Thisshouldbecomparedtoprevioussingle-cellDNA-sequencingapproaches,wheretheerrorrateisaround
20%–30%(Lodatoetal.,2015).
Tofurtherexplorestructurewithinthesomaticsubstitutioncalls,weexaminedtheeffectofsubstitutionsonproteinsequence.
Becauseofthedegeneracyoftheexoncode,afractionofexonicsubstitutionswillgiverisetoaDNAsequencewhichcodesfor
thesameaminoacidsequence.Suchsynonymous(orsilent)substitutionsareenrichedingermlineSNPs,andgiventhatasubset
ofaminoacidsubstitutionswillnegativelyaffectfitnessofthecells,wewouldexpectsomeenrichmentofsynonymoussubstitutions
alsoamongsomaticsubstitutions.Also,wewouldexpectthisenrichmenttobesimilarindifferentcelltypes,irrespectiveofthemuta-
tionalload.Substitutioncallsduetotechnicalerrors,however,willnotbeenrichedinsilentsubstitutions.Weannotatedthesubsti-
tutioncallsbasedongenomicnotation(hg19),andcalculatedthefractionofcallsthatresultinacodonforthesameaminoacid.Asa
comparison,wecalculatedthefractionofsynonymoussubstitutionsbasedonrandomDNAmutation.Theaveragefractionofsyn-
onymoussubstitutionswas40%higherthanexpectedbyrandomchance(0.32inpancreascomparedto0.23expectedbyrandom,
p=3.34E-125,Wilcoxontest.FigureS5H).Importantly,thisnumberdidnotcorrelatewithmutationalload;cellswithhighernumberof
mutationsinfacthadasomewhatincreasedfractionofsynonymoussubstitutions(Slope=3.25E-5,p=0.08,linearregression),and
pancreascellshadalmostidenticalfractionofsilentmutationscomparedtobraineventhoughthesubstitutionratewas5-foldhigher
inpancreas(FigureS5I).Thus,thedifferencesinsubstitutionrateslikely reflectgeneticalterationsinthecells,ratherthantech-
nicalerror.
Todeciphertheunderlyingmutationalsignatures,weappliednon-negativematrixfactorizationusingtheNMFRpackage(Gaujoux
andSeoighe,2010)tothesubstitutionratesofsingle-nucleotidesubstitutions(e.g.,themeanoftheratesforasubstitutiontypeover
allcontexts)foreachcelltypeseparately.Thehighestscoringsolutionoutof10000independentrunsofthealgorithmwasusedfor
thefinalresult.Thenumberofpossiblesignatures(5)waschosentobehigherthanthenumberofuniquesignaturesactuallyfoundby
thealgorithm,andduplicatesignaturesweremergedtogether.Weappliedhierarchicalclusteringonthefullsetofmutationalsigna-
tures(‘‘basismatrices’’)toidentifydistinctmutationalsignatures(FigureS4A).Finally,weselectedsignaturesbasedonfivecriteria
(summarizedbelowandinFigure4A).Tofindthesignaturesthatlikelyrepresentcelltypespecificprocessesthatwereactiveinthe
healthycellduringthedonor’slifetime,wedeterminedcelltypespecificityandagedependenceofeachsignature.Also,becauseof
therelativelyhighlevelofnoiseinthedata,asignaturemightrepresenterrorsthatarosesystematicallyduringreversetranscription.
Thus,toarriveatthefinalthreesignatures(S1-S3),removedmutationalsignatureswithahighdegreeofsimilaritytothesubstitution
ratesofthenegativecontrolRNA,withnocell-typespecificity,positiveagedependence,orwithaverylowsignal.Wealsodeter-
minedthesimilarityofthesignaturestotheCOSMICtumorsignatures(Alexandrovetal.,2013b).Figure4A,bottompanel,summa-
rizestheassociationofsignatureswiththesetraits.Itshouldbenotedthatwecannotformallyruleoutthepossibilitythattheexcluded
signatureswereduetoacell-typespecificprocessactiveduringthelifetimeofthedonor.Furtherinvestigationonmuchlargerpanels
oftissueswillbeneededtodeterminetheoriginofthesesignatures.
Figure4Ashowthegeometricmediansignatureofeachcluster.Mutationalloadofasignatureonacellwasdeterminedasthe
fractionofsomaticsubstitutionsofthatcellattributedtothesignatureinquestion.Toobtainasignatureloadranking,cellswere
orderedaccordingtothefractionofmutationsthatareattributedtoaspecificsignature.Statisticalsignificantassociationwasdeter-
minedusinglinearregression.
Estimationoftranscriptionalnoise
Inordertoascertaintherobustnessofagedependenttranscriptionalnoise,wecomputedthreemeasurementsoftranscriptional
instabilityeachofwhichdisplayedastrongstatisticalsignificanceandpositivecoefficienttoage.Asamainmeasure,weuseda
correlationbasedmethodwherenoiseisexpressedasbiologicalvariationovertechnicalvariation.First,wecalculatedthebiological
variationb =1-cor(x ,u),whereuiisthemeanexpressionvectorincelltypei,patientjandx istheexpressionvectorofcellkin
ijk ijk ij ijk
thatcelltypei,patientj.Next,wecalculatedthecorrespondingtechnicalvariationt =1-cor(xcontr ,ucontr)wherexcontr anducontr
ijk ijk ijk
aretheexpressionvectorandmeanexpressionvectoroftheERCCspike-incontrols.Thefinalmeasurementisb /t -thebiological
ijk ijk
noiseasafractionoftechnicalnoise.Thecellswereorderedbythisdistancewithincelltype,andtheirnormalizedrankingusedfor
linearregression.
Forper-donormeasurementswealsofirstdividedthecellsintocelltypesandcomputedthemeanexpressionvectorforeachcell
type.WethencalculatedtheEuclideandistancebetweeneachcellanditscorrespondingcelltypemeanvector.Theindividualdata-
pointsweresummarizedasboxplots.Finally,asanalternativemethodtoobtainameasureofthetranscriptionalnoiseofasinglecell,
wefirstsubsampledthegenecountlistto100000countspercell.Wethenselectedasetofinvariantgenesevenlyacrosstherange
ofmeanexpression.Firstwebinnedthegenesin10equallysizedbinsbymeanabundance,thenweselectedthe10%ofgeneswith
thelowestCVfromeachbin,omittingthebinsatthehighandlowextremes.WethenusedthesegenestodeterminetheEuclidean
distancefromeachcelltotheaverageprofileacrossallcells.
e6 Cell171,321–330.e1–e7,October5,2017

TodeterminethegeneswhosemRNAabundanceweresignificantlydependentupontranscriptionalinstability,weusedlinearrank
regressionontheCPMvalues.pvalueswereadjustedformultipletestingusingtheFDRprocedureofBenjamini&Hochberg(with
FDR<1E-15assignificancecutoff),andorderedbytheircoefficient.
DATAANDSOFTWAREAVAILABILITY
Theaccessionnumberforthesingle-cellmRNA-seqdatareportedinthispaperisGEO:GSE81547.Allcustomscriptswillbepro-
videduponrequesttotheLeadContact.
Cell171,321–330.e1–e7,October5,2017 e7

Supplemental Figures
FigureS1. Single-CellRNA-SeqofHumanPancreas,RelatedtoFigure1
(A)tSNEplotofcellsfromthemajorendocrinecelltypes.Colorsarebydonor(asspecifiedbyage,toprightpanel).Cellsclusterbydonorsuggestingthatourdata
couldnotfindsupportforsubcelltypesthathaveastrongercellidentitythanindividualvariation,butdoesnotprecludetheexistenceofmoresubtlesub-
celltypes.
(B)Relativecontributionsofcelltype,age,gender,donor,andlibrarypreparationbatch.Errorbarsaremean+-SEM.
(C)Boxplotofpairwiseeuclideandistancesbetween10000randompairsofendocrinecellsfromeachdonorisplottedbyagegroup.Whole-transcriptomecell-
to-cellvariabilitybetweenb-cellsfromadultdonorsishigherthanvariabilitybetweencellsfromjuveniledonors.Boxesindicatethemiddlequartiles,separatedby
medianline.Whiskersindicatelastvalueswithin1.53theinterquartilerangeforthebox.
(D)Celltypecompositionisconstantbetweenendocrinepancreaticcellswithlowandhightranscriptionalnoise.Linesarerunningmean(k=200)offractionalcell
typecontent,byrankoftranscriptionalnoise(lowtohigh).

FigureS2. QuantificationofCell-AtypicalHormoneExpressionInSitu,RelatedtoFigure2
(A)CellswererankedbynumberofINSspotspercell(bluebars),withthenumberofGCGspotsinthesamecellshowninred.Therewasnosignificantde-
pendencybetweenINSexpressionandGCGexpression(p=0.859,linearregression,n=730).
(B–D)ParallelproteinandRNAstaininginsitu.Arepresentativeimageat63xmagnificationofapancreaticisletcontainingcellswithatypicalhormoneexpression.
Scalebaris20mm.(B),proteinstainonly(green:insulin,blue:glucagon);(C),insituRNA-staining(dots)+proteinstain(greendots:INSgenespecific,bluedots:
GCGgenespecific);(D)magnifiedversionof(B).

FigureS3. CharacteristicsofSomaticSubstitutionsinSingle-CellRNA-SeqData,RelatedtoFigure3
(A)Thedistributionofthenumberofoccurrencesofdistinctsomatic(non-germline)substitutions.Asexpected,somaticmutationsthataresharedbetweenmore
thanonecellarerare.
(B)Somaticsubstitutionratesvarybetweencelltypesinthesameorgan(barsaremean+-SEM).
(C)NumbersofsubstitutioncallsinERCCcontrolaresimilarbetweencelltypes.Shownaremeannumbers(±SEM)ofputativesubstitutioncallsinERCCcontrols,
thatwererejected(graybars)oraccepted(redbars)byourvariationcallingmethod.Redbarsconstitutefalse-positivecalls.
(D)Substitutions/cellingenesinGP5dcells,orderedbymeanexpression.Onlygenesthatwereexpressedinatleastonecellareshown.Bothclonalsomaticand
non-clonalsubstitutionsarecounted.Redlineisrunningmean(k=100).
(E)SubstitutionsinERCCcontrolsbyconcentrationofeachspike-inRNA.Redlineisalocalregression(loess)fit.
(legendcontinuedonnextpage)

(F) Somatic substitutions in individual mRNA or ERCC control transcripts in a cell as a function of the number of reads mapped to the transcript/cell.
Substitutionsinhighlyexpressedgenesaremorelikelytobedetected,whereasPCRerrorsarelesslikelytopassQCthresholds.Linesarerunningmean
(k=300).
(G)Allelicimbalanceisnegativelycorrelatedwiththedepthofsequencingusedtocallthesubstitution.

FigureS4. MutationalSignatures,RelatedtoFigure4
(A)Heatmapshowingrawsignaturesfromnon-negativematrixfactorization.Dendrogram(top)indicateshierarchicalclustering,andclustersatthe6thbranch
pointshownascoloredbarbetweendendrogramandheatmap.ThespatialmedianofeachclusterisshowninFigure4A.
(B)AssociationofsignaturesS1-3,SC4-7toage.Cellswereorderedaccordingtothefractionofmutationsattributedtotheindicatedsignature.Dotsarerunning
meanofage,k=10.Lineisloessfit,dottedlinesindicate+-.999confidenceinterval.
(CandD)CDKN2Aexpressionincellsorderedaccordingtotheirleveloftranscriptionalnoise(C)orfractionofmutationsattributedtosignatureS1(D).Tran-
scriptionalnoiseisnotassociatedwithCDKN2Aexpression,whileS1mutationalloadisweaklyassociatedtoit.
(E)CelltypecompositionisconstantbetweencellswithlowandhighsignatureS1mutationalload.Linesarerunningmean(k=200)offractionalcelltypecontent,
byrankofsignatureS1specificmutationalload(lowtohigh).

FigureS5. TranscriptionalCorrelatesofMutationalSignatures,RelatedtoFigure6
BraincellswereorderedaccordingtothefractionofmutationsattributedtoSignatureS2.
(A)AverageageishigherincellswithhighsignatureS2load(p=2.7E-3,n=398.linearrankregression).Lineisloessfit+-.999confidenceinterval.Dotsare
runningmean,k=10.
(legendcontinuedonnextpage)

(B)EachgenewastestedforassociationwithsignatureS2(linearrankregression),shownarethetopgenesbycoefficient,withp<5E-2(FDRcorrected).Lineis
loessfit+-.999confidenceinterval.Dotsareindividualobservations.
(C)SignatureofrawsubstitutionratesinERCCspike-inRNAconstitutesafalse-positivesignature.
(D)TumorsignaturesfromAlexandrovetal.(2013b)collapsedintosubstitutiontypeswithout30/50contextbyaddition.
(E)Empiricalmisincorporationratescausedby8-Hydroxyguanosineinvitro.Barsaremean±SEM.DatafromfromKamiyaetal.(Kamiyaetal.,2009).
(FandG)RatioofhumanmRNAtospikeincontrolincells,orderedbyrankoftranscriptionalnoise(F)orrankofsignatureS1mutationalload(G).
(H)Synonymoussubstitutionsgeneratinganidenticalcodonasthereferencesequenceareenrichedinsomaticvariationfromalltissues.
(I)Thefractionofsynonymoussubstitutionsisnotpositivelycorrelatedwithoverallmutationload.