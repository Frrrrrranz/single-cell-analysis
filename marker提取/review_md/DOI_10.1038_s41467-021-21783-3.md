ARTICLE
|     | https://doi.org/10.1038/s41467-021-21783-3 |     |     |                 |             | OPEN |                |            |             |         |
| --- | ------------------------------------------ | --- | --- | --------------- | ----------- | ---- | -------------- | ---------- | ----------- | ------- |
|     | Time-resolved                              |     |     |                 | single-cell |      |                | analysis   | of          | Brca1   |
|     | associated                                 |     |     | mammary         |             |      | tumourigenesis |            |             | reveals |
|     | aberrant                                   |     |     | differentiation |             |      |                | of luminal | progenitors |         |
Karsten Bach1,2,3,10, Sara Pensa1,3,10, Marija Zarocsinceva 3,4, Katarzyna Kania2, Julie Stockis 2,
|     |         | Pinaud2, |       | Lazarus1,3, |      | Shehata5, |     |                 | 6,    | Greenhalgh6, |
| --- | ------- | -------- | ----- | ----------- | ---- | --------- | --- | --------------- | ----- | ------------ |
|     | Silvain |          | Kyren | A.          | Mona |           |     | Bruno M. Simões | Alice | R.           |
|     |         |          |       | 6,7,        |      | 6,        |     | 2,3,            |       | 2,           |
Sacha J. Howell Robert B. Clarke Carlos Caldas Timotheus Y. F. Halim
| ;,:)(0987654321 |      |                 |     | ✉       |           |     | ✉     |     |     |     |
| --------------- | ---- | --------------- | --- | ------- | --------- | --- | ----- | --- | --- | --- |
|                 | John | C. Marioni2,8,9 |     | & Walid | T. Khaled |     | 1,3,4 |     |     |     |
It is unclear how genetic aberrations impact the state of nascent tumour cells and their
microenvironment. BRCA1 driven triple negative breast cancer (TNBC) has been shown to
arisefromluminalprogenitorsyetlittleisknownabouthowBRCA1loss-of-function(LOF)and
concomitant mutations affect the luminal progenitor cell state. Here we demonstrate how
profiling
time-resolved single-cell of genetically engineered mouse models before tumour
formation can address this challenge. We found that perturbing Brca1/p53 in luminal pro-
genitors induces aberrant alveolar differentiation pre-malignancy accompanied by pro-
tumourigenic changes in the immune compartment. Unlike alveolar differentiation during
gestation, this process is cell autonomous and characterised by the dysregulation of tran-
scriptionfactorsdrivingalveologenesis.BasedonourdataweproposeamodelwhereBrca1/
p53 LOF inadvertently promotes a differentiation program hardwired in luminal progenitors,
highlightingthedeterministicroleofthecell-of-originandofferingapotentialexplanationfor
|     | the | tissue specificity |     | of BRCA1 tumours. |     |     |     |     |     |     |
| --- | --- | ------------------ | --- | ----------------- | --- | --- | --- | --- | --- | --- |
1UniversityofCambridge,DepartmentofPharmacology,Cambridge,UK.2CancerResearchUKCambridgeInstitute,LiKaShingCentre,Universityof
Cambridge,Cambridge,UK.3CancerResearchUK,CambridgeCancerCentre,Cambridge,UK.4Wellcome-MRCCambridgeStemCellInstitute,
Cambridge,UK.5MedicalResearchCouncilCancerUnit,UniversityofCambridge,Cambridge,UK.6ManchesterBreastCentre,OglesbyCancerResearch
Building,UniversityofManchester,Manchester,UK.7DepartmentofMedicalOncology,ChristieNHSFoundationTrust,Manchester,UK.8Wellcome
SangerInstitute,WellcomeGenomeCampus,Hinxton,Cambridge,UK.9EuropeanBioinformaticsInstitute,EuropeanMolecularBiologyLaboratory,
✉
Hinxton,UK.10Theseauthorscontributedequally:KarstenBach,SaraPensa. email:John.Marioni@cruk.cam.ac.uk;wtk22@cam.ac.uk
NATURECOMMUNICATIONS|        (2021) 12:1502 |https://doi.org/10.1038/s41467-021-21783-3|www.nature.com/naturecommunications 1

ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-021-21783-3
O
neofthemajorhurdlesfortheearlydetectionofcanceris Thedatasetcomprises~100,000cellsthatwegroupedinto51cell
our poor understanding of tumour-initiating events. types/states spanning the epithelial, immune and stromal com-
Historically, cancer research has focused on histological partment(Fig.1bandSupplementaryFig.1c).Duetothelackof
andmolecularcharacterisationofestablishedtumours,whichhas an external indicator of the samples’ premalignant stage we
ledtotheidentificationofhundredsofputativedrivermutations. inferredthestagesfromthetranscriptionaldataitself.Forthis,we
It is currently unclear how these genetic aberrations in tumour- pseudo-bulked the samples to derive a single transcriptional
initiating cells impact the cell state of nascent tumour cells and profile per sample and performed principal component analysis
their microenvironment. BRCA1-driven triple-negative breast (PCA) to identify latent factors that drive variation in the data
cancer (TNBC), for example, has been shown to arise from (Fig. 1c). We noted that PC1 appears to capture disease pro-
luminal progenitor cells1,2 yet little is known about how BRCA1 gression from wild-type like (low PC1 values) to fully developed
loss-of-function (LOF) and concomitant mutations affect the tumours (high PC1 values). This was supported by a correlation
luminal progenitor cell state and ultimately lead to transforma- ofPC1withageandwasalsoreflectedinthefactthatgeneswith
tion.Toexplorethisinmoredetail,weusedtheBrca1/p53TNBC high loadings for PC1 were enriched for central processes of
mouse model (Blg-Cre; Brca1f/f;p53 +/− ) that harbours a condi- tumourigenesis (SupplementaryFig.2).Tofacilitatetheanalysis,
tional Brca1 LOF in the luminal progenitor compartment. we divided the samples into four groups along PC1 (Stages 1–4)
as well as one group of tumour samples (Fig. 1c). Despite the
absence of visible tumours, we readily identified a small number
Results oftumourcellsinstages3and4,highlightingthestrengthofthe
We performed single cell RNA sequencing (scRNA-seq) on cells unbiased experimental and analytical approach (Fig. 1d).
isolated from the mammary glands of 15 Brca1/p53 mice span- Thestagingofthepremalignantsamplesallowedustoidentifya
ning various premalignant stages (n=15) and fully developed totalof16celltypesthatchangeinabundanceduringtheearlystages
tumours (n=2) (Fig. 1a and Supplementary Fig. 1a, b). of tumourigenesis (false discovery rate (FDR)<0.1; Fig. 2a, b and
Fig.1Atime-resolvedviewofTNBCdevelopmentintheBlg-Cre;Brca1f/f;p53+/−mousemodelatsingle-celllevel.aSchematicoverviewofthe
experimentaldesign.Mammaryglandsfrom13animalsbetween30and48weeksofageaswellastwofullydevelopedtumourswerepreparedforscRNA
sequencingafterdepletingdeadcells.bUMAPofallsamples,includingwild-typecontrols,cellsarecolouredbycelltypeannotation.Forthecomplete
annotationseeSupplementaryFig.3b.cPrincipalcomponentanalysiscomputedonthepseudo-bulked,normalisedandlog-transformedcountsfromall
samplesoftheBlg-Cre;Brca1f/f;p53+/−animals.Dashedlineshighlighttheboundariesofthefourstagespre-malignancyandthetumourstage.Themean
ageineachstageisnotedatthetopoftheplot(Stage1:36.6w[30–41],Stage2:40w[38–41],Stage342.3w[33–48],Stage4:42w[38–46],Tumour:47w
[46–48]).dUMAPfrombsubsettedbythestagesidentifiedinc.Cellsarecolouredbycellcompartments.Greycellsinthebackgroundrepresentcellsfrom
allsamplesnotpresentatthestageofinterest.BarsunderneaththeUMAPsrepresentthetissuecompositionateachstage.PCprincipalcomponent.
2 NATURECOMMUNICATIONS| (2021) 12:1502 |https://doi.org/10.1038/s41467-021-21783-3|www.nature.com/naturecommunications

ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-021-21783-3
Fig.2LuminalprogenitorcellsaberrantlydifferentiatetowardsanalveolarfateduringBRCA1LOF-dependentTNBCdevelopment.aCelltype
compositionofallBlg-Cre;Brca1f/f;p53+/−samplesgroupedbystages.Keycelltypesarehighlighted,forfullannotationseeSupplementaryFig.3a.
bVolcanoplotshowingtheresultsofthedifferentialabundancetestduringtumourdevelopmentfromstage1to4.ThelogFCrepresentsthecoefficientof
arobustregressionofnormalisedlog-transformedcelltypeabundanceonthe0–1scaledPC1valuesfromFig.1c.Colourschemecorrespondstoaand
SupplementaryFig.3.cGeneexpressionofvariouslineage-markersfortheAvdcluster.Expressionvaluesrepresentnormalised,log-transformedcounts.
Thehorizontallinedepictsthemedianexpression.Expressionvaluesarederivedfromn=15independentanimals.dUMAPcoordinatesfromFig.1,only
showingtheLpandAvdcluster.Thetoprowhighlightsthelocationofthetwoclustersaswellasgeneexpressionofthreemarkergenes.Thebottomrow
isfacettedbystageswithoverlaiddensityestimate.eWholemountsofmammaryglandsfromwild-typeandBlg-Cre;Brca1f/f;p53+/−animals.Weeks
(wks)ofageareshowninthebottomrightcorner.AdditionalexamplesareshowninSupplementaryFig.3c.fImmunofluorescencestainingforCsn2(red),
Cytokeratin-8(K8,green)andDAPI(blue)fromwild-type(toprow)andBlg-Cre;Brca1f/f;p53+/−(bottomrow)mammaryglands.Scalebarsrepresent
100µm.Tenindividualimagesfromthreeindependentanimalswereanalysed.gATAC-sequencingdatafromsortedluminalprogenitorcellsofwild-type
(top)andBlg-Cre;Brca1f/f;p53+/−(bottom)animals.hExpressionofCSN2insortedluminalprogenitorsfromeitherreductionmammoplastiesofhealthy
controlsorprophylacticmastectomiesfromBRCA1carriers.ThetoppanelshowsexpressionineightcontrolsandeightBRCA1carriersofCSN2as
measuredbyqPCR.Thebottompanelshowsexpressioninfourcontrolsvs.fourBRCA1carriersasmeasuredbyRNA-sequencingofsortedluminal
progenitors.FCfoldchange,TFtranscriptionfactor,CPMcountspermillion.SourcedatafortheqPCRisprovidedasasourcedatafile.
NATURECOMMUNICATIONS| (2021) 12:1502 |https://doi.org/10.1038/s41467-021-21783-3|www.nature.com/naturecommunications 3

ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-021-21783-3
Supplementary Fig. 3a, b). We noted a general decrease in various release paracrine signalling factors such as Rankl (also known as
populations of fibroblasts as well as signs of an overt immune Tnfsf11) and Igf2 (Fig. 3e) to orchestrate the development of the
reaction characterised by the expansion of myeloid and lymphoid tissue. In response, the basal compartment up-regulates the
cells. The only epithelial cluster that expanded was a cluster of expression of various collagens and myosins, all of which is
luminal cells with an expression profile of secretory alveolar cells required for the contraction of the ducts upon suckling of the
(Avd)thatwasvirtuallyabsentatStage1andmadeupmorethana infant (Fig. 3e). Finally, we also observe the gradual differentia-
third of the epithelium in Stage 4 (Fig. 2a–c and Supplementary tion of luminal progenitors, which commences at 4.5dG and
Fig. 3a).This cell type alsoappeared to be themostproliferative in reaches near-completion at 14.5dG, marked by expression of
theentiretissue(SupplementaryFig.3e).Underhomoeostasisthese variousmilkproteinsandgenesinvolvedinfatty-acidmetabolism
cellsarerestrictedtogestationalandlactationalstages3andarisefrom (Fig. 3d, e).
hormone-mediated differentiation of luminal progenitors4. In fact, Next, we contrasted this molecular reference of gestation
despite all animals being nulliparous we observed a progressive dif- with the aberrant phenotype of the Brca1/p53 animals. We
ferentiationoftheluminalprogenitor(Lp)compartmenttowardsthe foundthathormone-sensingluminalcellsinBrca1/p53animals
alveolarfate(Avd)withAvdaccountingfor1.8%(SD=1.6%)ofthe lack the transcriptional response observed during pregnancy,
epitheliumatStage1and40.4%(SD=2.3%)atStage4(Fig.2a,d). indicative of an absence of progesterone signalling (Fig. 3f, g).
This was accompanied by the expression of known markers of This is corroborated by the absence of basal differentiation
alveologenesis such as the milk protein beta-casein (Csn2) and the during Brca1-mediated tumourigenesis, indicating that the
transcription factor Elf5 (Fig. 2c, d). At the macroscopic level we gestation-like phenotype is hormone-independent, and a cell-
observed the appearance of what has previously been described as autonomous process restricted to the luminal progenitor
hyper-branching and alveologenesis in a different model of Brca1/ compartment (Fig. 3f, g).
p535(Fig.2eandSupplementaryFig.3c).Wefurtherconfirmedthe To directly compare the alveolar differentiation between
presenceofalveolarcellsbyimmunofluorescence,whichhighlighted gestation and early steps of tumourigenesis we identified genes
theexpressionofCsn2attheproteinlevelaswellasthepresenceof thatdifferintheircorrelationtoCsn2.Thisanalysisrevealed137
alveolar structures (Fig. 2f). Finally, we used assay for transposase- genes with a differential correlation (FDR<0.001 and |Δρ|>0.3,
accessiblechromatinsequencing(ATAC-Seq)toidentifychangesin Fig. 3h). For example, during tumourigenesis we observed no
chromatin accessibility of Lps in Brca1/p53 animals pre-tumour correlation between Csn2 expression and numerous genes
formation (Fig. 2g and Supplementary Fig. 4). We identified involved in fatty-acid metabolism which are normally induced
increased accessibility at several key genes of alveologenesis such as during gestation (Fig. 3i). This suggests that the alveolar cells
Csn2 and Wap with proximal enhancer regions known to be more foundduringearlystagesoftumourigenesisareunlikelytobefully
accessibleduringgestation6(Fig.2g,highlighted).Inaddition,chro- functional, secretory cells. Genes that showed a positive correla-
matin regions with increased accessibility showed significant tionwithCsn2onlyduringtumourigenesisincludedanumberof
enrichment for key transcription factors that drive alveolar differ- factors that are associated with basal-like breast cancer, among
entiation including Cebpb, Elf5, Nfkb1 and Sox10 (Fig. 2g and Sup- them a master regulator of alveologenesis Cebpb8 (Fig. 3j and
plementaryData1).Togetherthissuggeststhatluminalprogenitors SupplementaryFig.5d).Interestingly,multiplestudieshaveshown
intheBrca1/p53mousemodelarepoisedtodifferentiatetowardsthe that Cebpb as well as other regulators of alveologensis such as
alveolar fate and progressively do so during the early stages of Nfkb1canbeinducedinresponsetoDNAdamage9,10.Therefore,
tumourigenesis. this response could unintentionally drive a transcriptional pro-
Next, we sought to find an indication of whether a similar gramofalveolardifferentiationinthissetting,whichissupported
process might occur in the human breast during tumour devel- bytheenrichmentofCebpbandNfkb1bindingsitesinaccessible
opment.Forthis,weperformedqPCRtoassessCSN2expression chromatinof luminal progenitors (Fig. 2g).
in FACS-sorted luminal progenitor cells from BRCA1 carriers The analysis so far suggests that the early stages of TNBC
who had undergone prophylactic mastectomy (n=8) as well as development in the Brca1/p53 model are primarily characterised
healthywomenundergoingreductionmammoplasty(n=8).We by the cell-autonomous differentiation of the luminal progenitor
identified two samples from BRCA1 carriers with noticeably compartment. To further understand how this affects the com-
elevated CSN2 levels and none in the healthy controls (Fig. 2h). position of surrounding cells (Fig. 2a, b), we identified potential
To further validate this, we performed RNA-sequencing on an cell–cell communication pathways using CellPhoneDB11, a
independentsetofluminalprogenitorsfromfourhealthycontrols database of curated ligand receptor pairs associated with a sta-
and four BRCA1 carriers. Again, we found that two out of the tistical framework to test for enrichment of signalling pathways
four carriers show high levels of CSN2 (Fig. 2h). Differential between cell types in scRNA-seq data. When computing the
expression analysis from those two samples against all other difference in the number of potential signalling axes among the
samples showed an enrichment of pathways involved in the variousepithelialandimmunecellsfoundinstage1andstage4,
recruitment of the immune system as well as positive regulation we find an increase in heterotypic signalling, clustering around
of NFKB (Supplementary Fig. 3d). Although these data lack the theluminalprogenitorsandalveolarcells(Fig.4a).Forexample,
cellular and temporal resolution that we have from the mouse we see that later stages show a signalling axis from hormone-
model, it does suggest that aberrant differentiation of luminal sensingcellstodevelopingalveolarcellsviaRankl:RankandIgf2:
progenitors also occurs in humans. Igf2Rbothofwhichareknowntoinducealveologenesis12(Fig.4b
Tofurthercharacterisetheaberrantalveologenesis,wedecided andSupplementaryFig.6a).Thisisinlinewithpreviousdatathat
to compare it to its homoeostatic counterpart. We performed highlighted a dysregulation of RANKL in BRCA1 carriers13. In
scRNA-seq on three gestational time points (4.5dG, 9.5dG and contrast to normal development, however, we find that aberrant
14.5dG)andintegrateditwiththetumourigenesisdata(Fig.3a–c differentiation precedes Rankl expression fromhormone-sensing
andSupplementaryFigs.1aand5).Epithelialmaturationduring cells (Fig. 4c and Supplementary Fig. 6c), suggesting that induc-
gestation is regulated by systemic hormones, including proges- tion of Rankl expression is a means to further potentiate the
terone released by the corpus luteum7. Accordingly, we found aberrant differentiation. We note that there are several potential
transcriptionalresponsesinallepithelialcompartments(Fig.3d,e signalling axes from alveolar cells to hormone-sensing cells
andSupplementaryFig.5c).Hormone-sensingcellsareknownto includingFgf1andLif,bothofwhichhavebeenshowntoinduce
be the direct responders to pregnancy hormones and in turn Rankl expression14 (Supplementary Fig. 6b).
4 NATURECOMMUNICATIONS| (2021) 12:1502 |https://doi.org/10.1038/s41467-021-21783-3|www.nature.com/naturecommunications

ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-021-21783-3
Theanalysisalsorevealedanincreaseinthenumberofpotential checkpoint thus, inducing host tolerance during tumour forma-
signalling axes between the epithelium and some cells of the tion15. Additionally, we find an expansion of Tregs suggesting
immune system (Fig. 4a, d and Supplementary Fig. 6d). For the early establishment of an immuno-suppressive environment
example, we found a potential interaction between osteopontin (Fig.4f,Fig.2b).Comparedtowild-typeanimals,Tregsfromstage
(Spp1) expressed by Avd with Cd44 expressed on immune cells 1showreducedexpressionofKlrg1andIl1rl1,twomarkersoftissue
across all stages (Fig. 4e). Spp1 is up-regulated specifically in Avd resident Tregs, suggesting an early influx of Tregs from the circu-
during tumourigenesis and ultimately alsohighly expressed by the latory system preceding tumourformation (Fig. 4g).
tumour (Fig. 4e and Supplementary Fig. 6e). Previous research Inthe myeloidcompartment weidentifiedthree types oftissue
suggests that the Spp1:Cd44 signalling axis acts as an immune residentmacrophages(Mø1–3)matchingtherecentclassifications
NATURECOMMUNICATIONS| (2021) 12:1502 |https://doi.org/10.1038/s41467-021-21783-3|www.nature.com/naturecommunications 5

ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-021-21783-3
Fig.3Theaberrantdifferentiationofluminalprogenitorsinthecontextofhomoeostaticdifferentiationduringgestation.aSchematicoverviewofthe
experimentalstrategy.Mammaryglandsof12animalsfromfourtimepoints(Nulliparous,4.5dG,9.5dG,14.5dG;threesamplesandaminimumof18,000
cellspertimepoint)weredigestedtopreparesingle-cellsuspensionsforscRNAsequencingafterdepletionofdeadcells.Thedatasetwasintegratedwith
thetumourigenesisdatasetpresentedinFig.1.bSameUMAPasinashowingonlytheepithelialcompartment.cGeneexpressionofmarkergenesforall
epithelialcelltypes.Valuesarescaledfrom0to1perrow.dBinnedUMAPfrombonlyshowingcellscollectedfromthegestationtimepoints,colouredby
thetimepointatwhichthemajorityofthecellsintherespectivebinwerecollected.eGenesignaturesofgestationforeachofthethreemainepithelial
compartmentsdefinedasthetop100up-regulatedgenesbetween14.5dG(BasalandLps)or9.5dG(Hs)andnulliparoussamples.fBinnedUMAPfrom
bcolouredbythepercentageofcellsineachbinderivingfromthetumourigenesisdatasetwithbluerepresenting100%ofcellsderivingfromthegestation
samplesandpurplerepresenting100%ofcellsderivedfromtheBlg-Cre;Brca1f/f;p53+/−animals.Datasetsweredownsampledtothesamenumberof
cells.gSummedexpressionofsignaturesfromeacrossallconditions.hDifferentialcorrelationanalysiswithCsn2duringtumourigenesisandgestation
computedonallLpsandAvds.Thevaluesrepresentthedistancetomediancorrelationinthetwoconditions.Highlighteddotsrepresentgeneswithand
FDR<0.001and|Δρ|>0.3.i,jSomegenesfromharehighlighted.Theleft(blue)panelrepresentsthecorrelationwithCsn2(X-axis)duringgestationand
theright(purple)plotthecorrelationduringtumourigenesis.Geneexpressionvaluesarenormalised,log-transformedcounts.Thelinerepresentsalinear,
least-squareregressionandthedashedlinesa2Ddensityestimate.dGdaygestation.
inthefield16,17.InlinewithDawsonetal.wefoundthealveolar- betweenthedevelopingtumourandotherstromalcompartments.
associated macrophages Mø 3 to be the dominating macrophage In addition, we also show that aberrant differentiation is detect-
phenotype during gestation (Fig. 4h). Interestingly, we find a able in some human BRCA1 carriers. With the advent of spatial
similar expansion of Mø 3 during the premalignant stages of transcriptomics, it will be interesting to investigate the potential
tumourigenesis (Fig. 4h). As this subtype has been shown to be spatialdynamicofthisaberrantdifferentiationprocessinBRCA1
requiredfortissueremodellingitmostlikelyfulfilsasimilarrolein carriers.Futureeffortsshouldinvestigatetheefficacyofdetectable
the context of tumour development, supported by a relative aberrant differentiation and the accompanied changes in the
enrichmentfortheexpressionofgeneswithmetalloendopeptidase microenvironmentinstratifyingwomenathighriskofTNBCin
and collagen binding activity (Supplementary Fig. 7). We further the clinic, thus potentially reducing unnecessary invasive
found two types of tumour-associated macrophages Tam 1 screening and surgical interventions.
(markedbyArg1,Spp1andTrem2)andTam2(markedbyC1qb,
C1qc,LgmnandApoe)(SupplementaryFig.7)18.Theseseemtobe
Methods
recruitedalreadyinstage3and4beforeamacroscopictumouris
Mouseexperiments.Allexperimentalanimalworkwasperformedinaccordance
visible, potentially establishing an immuno-suppressive environ- totheAnimals(ScientificProcedures)Act1986,UKandapprovedbytheEthics
ment early on. CommitteeattheSangerInstitute.TheBlg-Cre;Brca1f/f;p53+/−(JAX012620)19
mousemodelwasusedtostudyTNBCtumourdevelopment.Indetail,tissueswere
collectedfrom13nulliparousmicewithagerangingfrom30to48weeks(Sup-
Discussion plementaryFig.1a).Attimeofcollection,11miceshowednopresenceoftumours,
Oneofthemajorhurdlesfortheearlydetectionofcancerisour while2presentedtumoursinoneoftheglands.Inaddition,wecollectedglands
poor understanding of tumour-initiating events. In humans it is
fromtwoBlg-Cre;Brca1f/f;p53+/+thatwereusedasvalidationfortheorderingof
thesamples(SupplementaryFig.2d).Forthetumour-bearingmice,contralateral
challenging toassess theimmediate impact of genetic alterations
glandsandtumoursclearedofsurroundingmammaryglandtissueweretreatedas
on the cellular dynamics of the tissue. Here we demonstrate the independentsamplesinthedataset.Forthepregnancytimepoints,femaleswere
utility of time-resolved single-cell profiling of genetically engi- matedwithstuds.Tissueswerethenharvestedfromthreeindividualmicepertime
neered mouse models before tumour formation to address this pointatgestationday4.5,9.5,and14.5.Tissuefromnulliparouswild-typefemales
washarvestedat12weeksofageforcomparisontothepregnancytimepoints
challenge. We found that perturbing Brca1/p53 in the putative
(youngnulliparous,n=3),andat53and74weeksofageforcomparisontothe
celloforigin,luminalprogenitors1,2,inducesanaberrantalveolar
premalignantandtumourstages(oldnulliparous).FortheATAC-Seqexperiment,
differentiation pre-malignancy. Unlike the hormonally driven twowild-typeandtwoBlg-Cre;Brca1f/f;p53+/−mice(agedbetween36and
alveolar differentiation that occurs during gestation, this process 40weeks)wereused.Allmicewerehousedinindividuallyventilatedcagesundera
is cell autonomous and characterised by the dysregulation of
12:12hlight–darkcycle,withwaterandfoodavailableadlibitumandeuthanized
byterminalanaesthesia.AlltheprimersusedforgenotypingarelistedinSup-
transcriptionalregulatorsofalveologenesis.Basedonourdatawe
plementaryData2.
propose a model where transcriptional and epigenetic changes
driven by Brca1/p53 inadvertently promote a differentiation
Humantissues.Allprimaryhumanbreasttissuewasderivedfromwomen
program hardwired in luminal progenitors, highlighting the undergoingreductionmammoplastieswithnoknowngenetichistory(n=12)and
deterministic role of the cell of origin and offering a potential prophylacticmastectomiesfromwomenwithgermlineBRCA1mutations(n=12,
explanation for the tissue specificity of BRCA1 tumours. Despite oneofwhichhadatumourinthecontralateralgland)underfullinformedconsent
the dense, longitudinal sampling it remains unclear at which
eitheratAddenbrooke’sHospital,Cambridge,UK,inaccordancewiththeNational
point in the herein described differentiation trajectory the first ResearchEthicsService,Cambridgeshire2ResearchEthicsCommitteeapproval
(08/H0308/178)aspartoftheAdultBreastStemCellStudyorobtainedfromthe
tumourcellsemerge,andatwhichpointtheyshouldbedenoted BreastCancerNowTissuebank,asapprovedbyCambridgeCentralREC(15/EE/
as such. We do note, however, that the tumours in our study as 0192).(SupplementaryData3).
well as human TNBCs express transcriptional regulators of
alveologenesis such as Elf5, Sox10, Foxc1 and Cebpb (Supple- Mammaryglanddissociationintosingle-cellsuspension.Lymphnodedivested
mentary Figs. 5 and 10). Yet, inferring the cellular lineage of the mousemammaryglands(excludingthecervicalpair)weremechanicallydis-
tumour precisely will require advanced lineage tracing studies.
sociatedaftercollection,pooledperanimalandthefinelymincedtissuewas
transferredtoDMEM/F12(Gibco)+10mMHEPES(Gibco)+2mgml−1col-
Our experimental approach has allowed us to further identify lagenase(Roche)+200Uml−1hyaluronidase(Sigma)(CH)+gentamicin(Gibco)
responses in the surrounding cellular compartments during the
at37°Candvortexedevery30min.AfterthelysisofredbloodcellsinNHCl,cells
early steps of tumourigenesis. In particular, we highlight the werebrieflydigestedwithwarm0.05%Trypsin-EDTA(Gibco),5mgml−1 4 dispase
establishment of a potentially immuno-suppressive environment
(Sigma)and1mgml−1DNase(Sigma)andfilteredthroughacellstrainer(BD
Biosciences).
pre-malignancymarkedbytherecruitmentofTregsandtumour-
Frozenvialsofhumanepithelial-enrichedfractionsobtainedfromthe
associatedmacrophages.Finally,thisdatasetcanalsobeusedasa CambridgeBreastCancerUnitanddissociatedasinref.20oroforganoidsfrom
resource for the community to understand the relationship theBreastCancerNowtissuebankweredefrostedanddilutedincoldHBSS1%
6 NATURECOMMUNICATIONS| (2021) 12:1502 |https://doi.org/10.1038/s41467-021-21783-3|www.nature.com/naturecommunications

a b
Rankl : Rank
c
CD8 T cells 2
CD4 T cells 2
● ● ● ● ● ● ● ● ● ● ● ● CTLs
● ILCs
● ●● ● ● ●● ● ● ● ● ● ● ● NK C T D re 4 g T s cells 1
●●●●●●●●●●●● ●●●●●● ●● ● ● ● ●
●
●
●
●
●
●
●
●●●●●● ● ●● ● ●●●●●●
● ●
●● ●●●●
●
● ● ●
●
● ●●
●●
●
● ● ●
●● ●● ●●
●
● ● ●
● ● Cycling T CD8 C T D ce 8 l l T s c 1 ells 3
Mast cells Plasma cells
B cells
Tam 1 Neutrophils
Tam 2
pDC Mø 3
e Mø 1 cDC1 migDC
Spp1 : Cd44 Mø 2 cDC2
Tre c g D s C c 1 DC m 2 igDC Avd B cel B ls as C a D l 4 T cells 1 Md M C d 3 C 2 MdC 1
Neutrophils CD4 T cells 2
NK CD8 T cells 2
Mø 3 CD8 T cells 3 Mø 2 CTLs Mø 1 MdC M 3 dC 2 MdC 1Lp ILCs Hs Cycling T
FCS(HF),furtherdigestedwithwarmTrypsin-EDTA(Gibco),5mgml−1dispase Cd49f-BV421(Biolegend313623,2µgml−1,1:100);Cd49b-AF488(Biolegend,clone
(Sigma)and1mgml−1DNase(Sigma)andfilteredthrougha40μMcellstrainer HMα2,1µgml−1,1:500)andSca1-AF647(Biolegend,cloneD7,1µgml−1,1:500).
(BDBiosciences). CellswerethenstainedwithStreptavidin-PE/Cy7(BDBiosciences,0.4µgml−1,
1:500).ZombieAqua(Biolegend,1:100)wasusedtodetectdeadcells.Human
mammarycellswerestainedwiththefollowingprimaryantibodies:CD45-APC
Celllabellingfollowedbyflowcytometryandsorting.Mouseandhuman (Biolegend,cloneH130,1:100),CD31-APC(Biolegend,cloneWM-59,1:100),
mammarycellswereincubatedinHFmedium(Hank’sbalancedsaltsolution EPCAM-APC/Fire750(Biolegend,clone9C4,1:50),CD49f-PE/Cy7(Biolegend,clone
(Gibco)+1%fetalbovineserum,Gibco)+10%normalratserum(Sigma)for20min GoH3,1µgml−1,1:200).DAPIwasusedtodetectdeadcells.Cellswerefiltered
onicetopre-block.Mousemammarycellswerestainedwiththefollowingprimary throughacellstrainer(Partec)beforesorting.SortingofcellswasdoneusingaFACS
antibodies:Cd31-biotin(eBioscience,clone390,1µgml−1,1:500);Cd45-biotin AriaFusionsorter.Single-stainedcontrolcellswereusedtoperformcompensation
(eBioscience,clone30F11,1µgml−1,1:500);Ter119-biotin(eBioscience,cloneTer119, manually.Unstainedcellswereusedtosetgates.Afterdoublets,deadcellsandcon-
1µgml−1,1:500);EpCAM-APC/Cy7(Biolegend,cloneG8.8,0.5µgml−1,1:500); taminatinghaematopoietic,endothelialandstromalcellsweregatedout,human
4
egatS
d9
sisenegiromuT
noitatseG
Number of potential interactions
[Stage 4 - Stage 1]
Igf2 : Igf2r
cDC c 1 DC m 2 igDC AvdB ce B ll a s sal cDC c 1 DC m 2 igDC Avd B ce B lls asal Tregs CD4 T cells 1 Tregs CD4 T cells 1
Neutrophils CD4 T cells 2 Neutrophils CD4 T cells 2
NK CD8 T cells 2 NK CD8 T cells 2
Mø 3 CD8 T cells 3 Mø 3 CD8 T cells 3
Mø 2 CTLs Mø 2 CTLs Mø 1 Cycling T Mø 1 Cycling T MdC M 3 dC 2 MdC 1LpILCs Hs MdC M 3 dC 2MdC 1Lp ILCs Hs
cDC c 1 DCm2igDC Avd B ce B ll a s sal cDC c 1 DC m 2 igDC Avd B ce B lls asal
Tregs CD4 T cells 1 Tregs CD4 T cells 1
Neutrophils CD4 T cells 2 Neutrophils CD4 T cells 2
NK CD8 T cells 2 NK CD8 T cells 2
Mø 3 CD8 T cells 3 Mø 3 CD8 T cells 3
Mø 2 CTLs Mø 2 CTLs
M M ø d 1 C M 3 dC 2 MdC 1LpILCs Hs Cycling T M M ø d 1 C M 3 dC 2MdC 1 LpILCs Hs Cycling T
d
h f g
100
C C
C
D D
D
4 8
4
T T
T
c c
c
e e
e
l l
l
l l
l
s s
s
2 1
1
1.5 G Il m 1 M r 2 l t 1 1 a ●●●●O●●●● C dc c 1 nd2 S ●● atb1
Gdpd3●●
Thy1●●●●●●Lgals1
0 Ol d 1 2 3 4 C C C C Tr D D T y e c L g 8 8 l s s i n T T g c c T e e l l l l s s 2 3 0 0 1 . . . 0 5 0 K ● lr ● g1 C R i●● e ● s l h ● ● ● ●●●● ● S T ●● ● ● ● ● ● ● ● ● ● ● ● ●●●● ● ●●● ● ● ● ● p ● ● ● ● ● ● ● g ● ● ● ● ●●● ●● ● ● ● ● ● ● ● ●● ● ● ● ● ● ● ● ● ● ●● ●● ● ● ● ● ● ●●● ● ● ● ●● ● ● ● ● ●● ● ● R ●● ● ● ● ●● ● ● ● ● ●● ● ● ●● ● ●● ● ●● ●● ● ●● ● ● ● ●● ● ● ●●● ● ●● ● ● ● ● ●●●● ●● ●●● ● ● ●●●● ●● ●● ●● ● ●● ● ●● ● ●● ●● ● ● ● ● ● ● ● ● t ● ● ●● ● ● ● ● ●●● ●●● ● ●● ● ● ● ● ● ●● ● ● ● f ● ● ●● ● ● ● ●●● ● ●● ● ● ● ● ● ● ● ●● ● ●● ● ●● ●● ● ●● ● ●● ● ● ●●●●●● ● ●●●●● ●●●● ● ● ●●●●● ● ●● ● ● ● ●● ● ●● ●● ● ●●●● ● ● ● ● ●● ● ● ● ● ● ● ●●● ●● ●● ●●●● ● ●●●●● ● ● ●●●●●●●●● ● ●●●●●●● ● ● ●●●●●● ● ● ● y ● ●● ●● ●●● ● ● ●●● ● ● ● ●● ●●●●●●●●●● ● b ●●●●●●●●● ● ● ●●●●●● ●●●●● ●●●● ●●● ● ● ● ●● ●●● ●●●●●●●●● ● ●● ● ●●● ● ●●●● ●●● ●● ● ●●● ● ● ● ●●●●● ●●●●●● ●● ● ●●● ● ● ● ●●●●● ●● ● ●●●●●●●●●●●● ● ● ● ●● ● ● ● ●●●●●●●●● ●●●●●●● ● ●●●●●●● ● ● o ●●●●● ●● ●●●● ●●●●● ● ●●●●●● ●●●● ● ● ●● ● ●●●●●●●●● ● ●●●●●●●●●●●●●●●●●●● ● ● ● ●● ●●●●●●● ●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●● ● ●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●● 2 ●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●● 1 ●●●●●●●●●●●●●●●● ●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●● ● ●●●● ●●●●●●●●●●● ● ●●●● ●●●●●●●● ●●●●●●●●●●●●●●● ● ●●●●●● ● ●●●● ● ● ● ●●●●●●● ●●●● ●●● ● ●●●●●●●●●●●●●● r ● ●●●●●●●● ●●●●●●●●●● ● ●● ● ●●● ●●●●●● ● ●●●●●●●● ●●●●●● ● ● ●●●●●●●●● ● ● ●● ●●●●● ● ●●●●●●●●●● ● ●●●●●●● ●●● ●● ●● ● ●●●●●● ● ●● ●● ● ●●●●● ●● ● ●●●●●● ● ●● ● ●●● ● ●●●●●●● ● ● ●●● ●● ● ● ●●● ● ● ● ● ●● ● ●●● ● ● ●●●● ● ● ●●● ● ● ●● ● ● ●● ● ● ● ●●●●● ● ●●●● ●● ● ● ●●● ● ● ● ● ● ● ●●●● ● ●●● ●●● ● ●●● ● ●●●● ● ● ● ●● ●●● ● ●●●● ● ●●● ● ● ●●●● d ●●●●● ● ● ●● a ● ● ●● ● ●● ●● ● ●● ● ● ● ●● ● ●●●●●● ● ● ● ●●●●●● ●●●●●●● ● ● ● ● ● ●● ● ●●● ● ●●●●●● ● ● ● ●●●●● ● ● ●● ● ● ● ● ● ●●●● ●● ●● ● ● ● ● ● ●● ●● ● ● ● ●● ● ● ● ● ●● ● ● ● ● ● ● ●● ● ● ● ● ● ● ● ●● ●● ●●● ● ●● ● ● ● ● ●● ● ● ● ●● ● ●●● ● ●● ●● ● ● ● ●● ● ●● ● ● ● ● ● ● ● ● ● ● ●● ● ● ●●● ● ● ● ● ● ● ● ● ●● ● ● ● ● ●● ● ●●●●●● ● ●● ● ● ● ●● ● ● 1 ●● ● ● ●● ● ● ● ●● ● ● ● ●● ● ●● ● ●● ● ● ● ● ● ● ● ● ●● ● ●● ● ● ● ● ●● ● ● ●● ●● ● ● ● ●● ●● ● ●● ● ● ● ● ● ● ●● ●● ●●●●● ● ● ● ● ● ● M ● ● ● ●● ●●m ● ● ● ● ●● a ●● t g − ●● o ● N ● h d ● 4 ● l ● ●
T −5 0 5
W logFC
)RDF(01gol−
Lp
Avd CD8 T cells 3 Mø 3 Mø 1 cDC2
cDC1
Cycling T
CTLs
Hs Basal CD8 T cells 2 B cells NK
CD4 T cells 2
CD4 T cells 1
Tregs ILCs
Mø 2
MdC 1
migDC
Neutrophils
MdC 2
MdC 3
Tregs WT Stage 1
3 CdM 2 CdM slihportueN CDgim 1 CdM 2 øM sCLI sgerT 1 sllec
T
4DC
2 sllec
T
4DC
KN sllec
B
2 sllec
T
8DC
lasaB sH sLTC T gnilcyC 1CDc 2CDc 1 øM 3 øM 3 sllec
T
8DC
dvA pL
40 20 0 -10
1
0.5
0
0 5 10 150 20 40 60
Gestation Tumourigenesis
[d] [PC1]
Gene Expressed by
Rankl Wap Hs
Igf2 Csn2 LpAv
noisserpxE
evitaleR
Spp1 Expression
Lm Lp Hsp Hs Bsl G
Bsl 2
Bsl 1 Avd
WT You W ng T O 4 ld .5d 9 G .5d 1 G 4.5d G1234 0 Max 100 Mø 1
Tam1 Mø 2
Mø 3 Tam2 0 WT Young 4.5d G 9.5d G 14.5d G WT Old 1 2 3 4
T
u m o ur sllec T fo %
segahporcaM
fo %
ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-021-21783-3
NATURECOMMUNICATIONS| (2021) 12:1502 |https://doi.org/10.1038/s41467-021-21783-3|www.nature.com/naturecommunications 7

ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-021-21783-3
Fig.4Aberrantdifferentiationofluminalprogenitorcellsisaccompaniedbyanalteredmicroenvironmentwithtumour-promotingcharacteristics.
aNetdifferenceinthenumberofpotentialinteractionsbetweenanyimmuneandepithelialcelltypesbetweenstage4andstage1.Thenumberofpotential
interactionswasestimatedineachstageusingcellphoneDBatanFDRof0.05.bGraphsrepresentingpotentialinteractionsforRankl:RankandIgf2:Igf2r
forStage4oftumourigenesis(toprow)and9dG(bottomrow).Nodesrepresentcelltypesandedgesrepresentsignificantinteractionswiththewidthof
theedgeillustratingthemeanexpressionofligandandreceptor.Thearrowoftheedgesrepresentsthedirectionfromligandexpressingtoreceptor
expressing.cGeneexpressionfortheparacrinesignallingfactorsRanklandIgf2inhormone-sensingcellsandthealveolarmarkersCsn2andWapinluminal
progenitorsandalveolarcells.Expressionisscaledacrossgestationandtumourigenesisto0and1.Inthetumourigenesispanel,theX-axisrepresentsthe
valuesofPC1thatwerescaledby(PC1+min(PC1))/max(PC1−min(PC1))×100dUMAPforallimmunecelltypescapturedinthegestationand
tumourigenesisdataset.eInteractionplotasinbforSpp1:Cd44duringstage1oftumourigenesis.RightpanelshowsmeanlogexpressionofSpp1across
epithelialcelltypesinthemammaryglandacrossvariousconditions.Greyrepresentsconditionswithnocellsofthatparticularcelltype.fBarplotof
relativefrequencyofT-lymphocytesduringtumourigenesis.gDifferentialexpressionanalysisofTregsfromoldwild-typeanimalsandTregsfromstage1.
hDistributionofmacrophagepopulationsduringgestationandtumourigenesisasing.Datainbarplotsrepresentthemeanperstage.Forallpregnancy
timepointsn=3independentanimalswereanalysed;forthetumourigenesisstagesthesamplesizesarespecifiedinSupplementaryFig.1a.FCfold
change,FDRfalsediscoveryrate.
luminalprogenitorsweresortedforRNAprocessingandmouseCD49b+,Sca1− genesaswellasthedetectiontrend(seebelow).Cellswithanumberofgenes
luminalprogenitorsweresortedforATAC-Seqexperiments.Thegatingstrategiesare detectedandtotalnumberofUMIsthatwasgreaterorsmallerthanmedian±3×
reportedinSupplementaryFigs.8and9. MAD(medianabsolutedeviation)orapercentageofmoleculesmappedto
mitochondrialgenesgreaterthanmedian+5×MADwerethenexcludedfromthe
downstreamanalysis.Thedetectiontrendwasdefinedasacubicsplineregression
scRNAsequencingofmousesamples.MACSDeadCellRemovalkitwasusedto
ofgenesdetectedonthenumberofUMIssequencedinlogspace.Cellswitha
excludedeadcellsfromsingle-cellsuspensions.Subsequently,cellswerespundown residualsmallerthanmedian−6×MADwereidentifiedasoutliers,mostofwhich
andresuspendedinHF.Samplesweremanuallycountedusinganimproved
wereredbloodcells(RBCs).Thisresultedinatotalof124,507(102,829)cellsbeing
NeubauerchamberandthecellconcentrationwasnormalisedbyadditionofHF.
consideredforfurtheranalysis.Geneexpressionvalueswerethennormalisedper-
EqualnumbersofcellspersamplewereprocessedforscRNAlibrarypreparation. batchbysizefactorsthatwereestimatedusingthe“computeSumFactors”function
Sampleswereprocessedforfirst-strandcDNAsynthesiswithin6hfromtissue
inscranbeforebeingscaledacrossbatchesusing“muliBatchNorm”23,24.
isolation.Theremainingstepsoflibrarypreparationwerecompletedwithinthe
following7days.
Highlyvariablegenes.Highlyvariablegenes(HVGs)wereidentifiedbyfirst
fittingamean-dependenttrendtothegene-specificvariancestoallgenesassuming
u
W
si
h
n
o
g
le
fo
m
rc
o
e
u
p
n
s
t
o
s
n
.F
a
or
gl
w
as
h
s
o
s
le
lid
m
e
o
a
u
n
n
d
t
i
a
n
n
c
a
u
ly
b
s
a
i
t
s
e
,
d
n.
in
4
C
ab
a
d
rn
om
oy
i
’
n
s
a
fi
l
x
g
a
la
ti
n
v
d
e
s
o
w
ve
e
r
r
n
e
i
s
g
p
h
r
t
e
.
a
T
d
h
o
e
ut thatthistrendisdominatedbytechnicalvariance.Thistrendwasthendefinedas
thetechnicalcomponentofthevariance.Thegeneswithapositiveresidualvar-
slidewasthenplacedincarminealum(Sigma)stainovernight.Theslidewas ianceweredefinedasHVGsorafractionthereofifcomputationalspeedwasa
returnedtoCarnoysandimagedusingaLeicaMZ75dissectingmicroscope.
priority,e.g.fordoubletdetection.FromthelistofHVGsweexcludedallgenes
thatwereannotatedasconstituentsoftheribosome(GO:0003735,GO:0005840,
Immunofluorescence.Fivemicrometersectionsofmammaryglandswere GO:0015935,GO:0015934)orencodedbythemitochondrialgenomeasthesetend
immunostainedwithantibodiesforCsn2(sc-166530,Santacruz,1:50)andK8 tobedrivenbytechnicalvariation.
(TROMA-1,MABT329,Merk-Millipore,1:500).Secondarystaininginvolvedgoat
anti-ratAlexaFluor647,oranti-mouseAlexaFluor594(1:200,Invitrogen).Nuclear Doubletdetectionanddatafiltering.Duetothehighnumberofcellsand
stainwasdetectedusingProLongGoldAntifadeMountantwithDAPI(Thermo-
fisher,P36941). s
c
a
a
m
pt
p
u
l
r
e
e
s
d
,d
in
ro
a
pl
s
e
u
ts
ffi
w
ci
i
e
th
nt
m
n
u
u
l
m
tip
b
l
e
e
r
c
t
e
o
ll
f
s
o
a
rm
re
d
p
i
a
s
r
t
t
i
i
n
c
c
u
t
la
c
r
l
l
u
y
st
p
e
r
r
o
s.
bl
W
em
e
a
t
t
h
ic
er
a
e
s
fo
t
r
h
e
ey
tri
w
ed
ill
t
b
o
e
identifydoubletsbeforeclusteringandannotatingthedata.Weusedrelatively
Confocalmicroscopyandimageanalysis.Immunofluorescenceimageswere liberalthresholdstoavoiderroneouslyremovingcells.Briefly,theprobabilityof
acquiredusingaLeicaTCSSP5invertedconfocalmicroscopeswith×40/1.3HCPL beingadoubletwasestimatedforeachcellpersample(thatisone10×lane)using
APOobjectivelens.Laserpower,lineaveragingandstepincrementwereadjusted the“doubletCells”functioninscran23usingonlyHVGs.Next,weused“clus-
manuallytogiveoptimalfluorescenceintensityforeachfluorophorewithminimal ter_walktrap”25ontheSNN-GraphthatwascomputedonHVGstoformhighly
photobleaching. resolvedclusterspersample.Per-sampleclusterswith>median +1.5×MAD)
doubletscorethatmadeuplessthan5%ofthesampleweretaggedasdoublets.
Thiswasfollowedbyasecondroundofper-datasetclustering,inwhichagaincells
Librarypreparationandsequencing.Librarypreparationofmurinesampleswas
belongingtoclusterswithahighproportion(>2×MADfrommedian)ofcells
performedaccordingtoinstructioninthe10XChromiumsinglecellkitv2(Batch1 previouslylabelledasdoubletswerealsodefinedasdoublets.Atthispointwealso
and2)orv3(Batch3–5).Thesampleswereprocessedinfivebatches(Supple-
excludedclusterswithanon-zeromedianexpressionofhaemoglobinsasthese
mentaryFigs.1aand5a)whereeachbatchrepresentsadayinwhichmultiple representcontaminatingRBCs.Clustersmostlikelyrepresentingstrippednucleias
biologicalsamples(onebiologicalsamplerepresentseitherpooledglandsfromone definedasclusterswithlessthana0.005medianfractionofmitochondrialreads
mouseoratumourfromonemouse)wereprocessedtogether.Thelibrarieswere werealsoexcluded26.Intotal,thisledtothefurtherexclusionof2439(3047)cells.
thenpooledandsequencedonaHiSeq4000(PE26/98)orNovaSeq6000(PE28/91).
Batchcorrection.Toaccountfortechnicaldifferencesbetweenexperimental
ProcessingandqualitycontrolofscRNA-seqdata.Readprocessingwasper- batcheswematchedmutualnearestneighboursacrossbatches27.Thisstepwas
formedusingthe10XGenomicsworkflow.Briefly,theCellRangerSingle-Cell
performedbothwithinthedatasetsbeforeandafterdoubletremovalaswellas
SoftwareSuite(3.10)wasusedfordemultiplexing,barcodeassignmentandUMI
acrossthedatasetstointegratethepregnancyandtumourigenesisdata(Fig.3a).
quantification(http://software.10xgenomics.com/single-cell/overview/welcome).
Forthisweappliedthe“fastMNN”functionfrombatchelorwith“k=20”,“cos.
Thereadswerealignedtothepre-builtmm10referencegenomeprovidedby10x norm.out=FALSE”andd=50onthenormalisedgeneexpressionvaluesofHVGs.
Genomics(https://support.10xgenomics.com/single-cell-gene-expression/software/
ForHVGdetection,thevariancewasdecomposedper-batchasdescribedabove
downloads/latest). andthencombinedusingthe“combineVar”functioninscran;23allgeneswitha
Samplesfromthetumourigenesisdatasetandthepregnancydatasetwere positiveresidualvariancewerethendefinedasHVG.Visualinspectionofthedata
processedindependentlytogeneratetwohigh-quality,filtereddatasetspriorto
afterbatchcorrectionsuggestedthatmostoftheeffectwasremovedandthatthe
merging.Theformerconsistedofthreebatchesandthelatteroftwo.Allsteps
biologicalsignalnowdominatesthestructure(SupplementaryFig.5a).Thebatch-
belowwereperformedindividuallyforthetwodatasets,whenresultsorsettings
correctedprincipalcomponentswereusedfordimensionalityreductionand
arepresentedthevaluesinparenthesesrepresenttheresultsorsettingsforthe
clustering.Alldifferentialexpressiontestswereperformedonnon-corrected,
pregnancydata.
normalisedgene-expressionvalueswithanaddedblockingfactorforbatch.
Barcodesthatcorrespondtodropletswithsuccessfullycapturedcellswere
distinguishedfromemptydropletsusingthe“emptyDrops”functionfrom
DropletUtils22atanFDRof0.01.Wethenusedthefollowingmetricstoflagpoor- Dimensionalityreduction.Alltwo-dimensionalrepresentationsofthescRNA-seq
qualitycellsoroutliers:numberofgenesdetected,totalnumberofunique datawerecomputedusingUMAP(UniformManifoldApproximationandPro-
molecularidentifiers(UMIs),percentageofmoleculesmappedtomitochondrial jectionforDimensionReduction)28.TheUMAPcoordinateswerecomputedbased
8 NATURECOMMUNICATIONS| (2021) 12:1502 |https://doi.org/10.1038/s41467-021-21783-3|www.nature.com/naturecommunications

ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-021-21783-3
onthebatch-correctedprincipalcomponentsusingtheumapfunctionfromthe Cell–cellinteractions.Potentialcell–cellinteractionswereidentifiedusingcell-
umappackagewithdefaultsettingsand“random_state=42”.Foreaseofinter- phoneDB11.Thiswasperformedonallepithelialandimmunecelltypesthatwere
pretation,allUMAPembeddingsrepresentthecoordinatescomputedonthe presentinallconditionsexcludingthetumoursamples.Furtherthebasalclusters
integrateddataset,thatispregnancyandtumourigenesis.InFigs.1and2only Bsl1,Bsl2andBslGweregroupedinto“Basal”becauseBsl2andBslGcontained
samplesofthetumourigenesisdatasetareshown,whereasinFigs.3and4cells onlyasmallnumberofcellsinthetumourigenesisdatasetandHspandHswere
fromallsamplesareshown.ThegeneexpressionplotsinFig.2aswellasthe combinedintoHs.ThemouseENSEMBLIDsweremappedtothehuman
UMAPscolouredbytimepointandcondition(Fig.3)wereproducedbybinning orthologouesasdefinedintheENSEMBLdatabaseaccessedviathebiomaRt
cellsintohexagonalbinsusingtheschexpackage(FreytagS(2020).schex:Hexbin package.Forthevisualisationofspecificinteractionswecomputedadirectedgraph
plotsforsinglecellomicsdata.Rpackageversion1.2.0,https://github.com/ whereeachnoderepresentacelltypeandeachedgeasignificantinteractionwith
SaskiaFreytag/schex). theweightoftheinteractionrepresentingthemeanexpressionofligandand
receptor.Thisisbasedonthevisualisationproposedinthecomunetpackage30.
Clusteringandcelltypeannotation.Thedatawereclusteredfirstindividuallyper
datasetincludingapreliminaryannotation.Thisannotationwasmainlyusedto Differentialexpression.Differentialgeneexpressionanalysiswasperformed
identifyclustersthatrepresentremainingdoubletsordamagedcellswhichallows usingedgeR31.Anegativebinomialgeneralisedlog-linearmodelwasfittedtothe
removalbeforethefinalintegrationstepofthetwodatasets. remaininggeneswiththeclusterassignmentsascovariate(s).The“glmQLFTest”
ClusteringwasperformedusingthewalktrapalgorithmontheGraphfromthe functionwasusedtoidentifygenesthathaveLFCsignificantlydifferentfrom0at
UMAPembeddingusingthecluster_walktrapfunctioninigraphwith“step=7”(6 anFDRof0.1.Themarkergenesusedforcelltypeinferenceswereidentifiedusing
forthetumourigenesisdata,7forpregnancy)25.Beforeannotatingcelltypes,we the“findMarkers”functioninscranwithdefaultsettings.
performedapost-hoctestbyiterativelymergingclusterswith<10differentially
expressedgenes(FDR<0.1andminimumlogfoldchangeof1)using
“findMarkers”fromscran.Ribosomalgenesandmitochondrialgeneswere Geneontologyenrichmentanalysis.Agenesetenrichmentanalysisbasedon
excludedatthisstagefordifferentialexpression(DE)analysis(seeabove).Some geneontology(GO)termswasconductedtocharacterisevariousgenesetsinthe
clustersweremanuallysub-clusterediftherewasstructureapparentbasedongene analysis.Thegenesofinterestwerecomparedtoallgenesthatweretestedusing
expressionofcommonmarkergenesorasobservedintheUMAPembedding.The topGO32.
sub-clusteringwasperformedonanSNN-Graphascomputedonthebatch-
correctedprincipalcomponentsusingeitherlouvainorwalktrapclustering.Finally,
remainingclustersthathad<10DEgenesasdefinedby“findMarkers”were ATAC-Seq.UsingthepreviouslyestablishedATAC-sequencingprotocol33the
mergedtotheirclosestcluster.Theexceptiontothisapproachweretwo tagmentationreactionwasperformedonFACS-sortedluminalprogenitorsisolated
superclustersofT-CellsthatrepresentedknownbiologicalsubtypeswithlittleDE fromnulliparousmiceeitherwild-type(n=2,age40weeks)orBrca1/p53(n=2,
oneconsistingofCD4,TregsandCD8T-CellstheothercontainingCTLs,NKand age36and38weeks).LibrarypreparationwasperformedbytheNGSFacilityat
CD8cells.Inthiscasetheclusterswerekeptseparatedespiteshowinglessthan10 theWellcomeTrustMedicalResearchCouncilStemCellInstituteusingthe
DEgenes. NexteraDNALibraryPrepReferenceGuide.Resultinglibrarieswerepooledacross
allsamplesandsequencedacrossonelaneoftheNovaseq6000.
Resultingreadsweresubjecttoqualityprocessingbytrimmingofftheadapter
Transcriptionalorderingofsamples.Despitetheageoftheanimalsbeinghighly sequencesusingTrimGaloreinpaired-endmodewithdefaulterrorrate,–nextera
correlatedwiththeunderlyingbiologicalprocessoftumourdevelopmentitdoes optionfortransposasesequencefilteringandexcludingreadswithPhredscore
notdirectlyrepresentthestageofdiseasedevelopment.Thisislargelyduetothe below30.Forwardandreversereadsweresubsequentlyalignedtothemm10
stochasticityofthemanyprocessesinvolvedintumourdevelopmentincludingbut genomeusingtheBWA-MEMalgorithm34.Mitochondrialreadswereremoved
notlimitedtotheacquisitionoffurthermutationsuponthelossofBrca1andp53. usingSAMtools.PCRduplicatesweremarkedwithMarkDuplicatesfromPicard
Theapproachthatwasusedinthisstudyisbasedontheassumptionthatthereare tools.Readsshorterthan30bpwerediscardedwithalignmentSievefrom
stereotypicalprocessesinthetranscriptomesofthecapturedcellsthatrepresentthe deepTools35.UsingSAMtoolsview,readswerequalityfilteredleavingonlyunique,
biologicalprocessoftumourformation,including,forexample,aresponseofthe mate-mappedreadsandremovingchimericalignmentandPicardmarkedPCR
immunesystem.Thelatentfactormostlikelyrepresentingbiologicaltimewas duplicates.
identifiedusingPCAcomputedonthepseudo-bulkedandTMMnormalised,log- CoveragetracksweregeneratedfromqualityprocessedBAMfilesusing
transformedcounts.Weinterpretedthefirstprincipalcomponenttorepresent bamCoveragefromdeepToolswiththecountspermillionnormalisationand10-
tumourigenesisbasedonthehighcorrelationwithage(SupplementaryFig.2b),the basepairlongbins.Theresultingbigwigfileswithnormalisedcountswere
separationoftumoursfrommammaryglandsamples(SupplementaryFig.2a),and visualisedusingtheIntegrativeGenomicsViewer(IGV)36.
theenrichmentofgenesinprocessessuchasimmuneresponseandcellcycle Differentiallyaccessiblesitesbetweenwild-typeandBrca1/p53luminal
progression.WedefinedPC1as–1×PC1inordertohaveWTsamplesontheleft progenitorcellswereidentifiedusingthecsawpackage37inR.Afterloadingthe
ofthePCAandtumoursontheright,thisisapurelyaestheticchangeandhasno QC-filteredBAMfile,theENCODEblacklistedregionswerediscardedandreads
otherimpact.Further,weprojectedtwoindependentlycollectedsamplesfrom subsequentlycountedinwindowsoffixedgenomicintervals(20bp).Lowcount
42weekoldBlg-Cre,Brca1f/f;p53+/+animals,whichalsodevelopTNBCalbeitwith windowswerefilteredusingtheglobalenrichmentapproachwith10,000bpbin
muchlongerlatency19,ontothePCAspace(SupplementaryFig.2d).Thesesam- sizeandkeepingwindowsthatarethreefolddifferentfromthebackground
plesreceivedlowPC1valuesandweresubstantiallyolderthanothermiceinthe estimate.Normalisationfactorswerecalculatedfromhighabundancewindows
samebin,supportingthenotionthatPC1representstumourformationandthat toeliminateefficiencybias.Differentiallyaccessiblesiteswereidentifiedusing
thisisdelayedinBlg-Cre,Brca1f/f;p53+/+animals. edgeR31withFDR<0.1.Enrichedmotifsintheresultingdifferentiallyaccessible
genomicregionswerefoundusingthefindMotifsGenome.plscriptfromHOMER38
usingthesize-givenoptiontoincludetheexactsizeofeachdifferentially
Differentialabundancetesting.Toidentifychangesincell-type-specificabun- accessiblesite.
danceduringthepremalignantstagesweregressedthescaledPC1valuesonthe
normalisedlogcountsforeachcelltypeusingrobustregressionasimplementedin
the“rlm”functionoftheMASSpackage21withdefaultsettingsand“max_it=100”. PreparationofRNAforqPCR.Sortedcellswerespundownandresuspendedin
Normalisedlogcountsofclusterabundancewerecomputedusingthe“cpm” RLT,andRNAwasextractedusingtheRNeasyminikit(formousecells)orthe
functioninedgeRaccountingfortotalnumberofcellspersample.Toassess RNeasymicrokit(forhumancells;Qiagen)accordingtomanufacturer’sinstruc-
statisticalsignificanceoftheregressionweemployedarobustF-testasimple- tions.DNAwasdegradedbyadding20URnase-freeDnaseI(Roche)for30minat
mentedinsfsmisc.TheresultingPvalueswerecorrectedformultipletestingusing roomtemperature.DnaseItreatmentwasperformedoncolumns.
theBenjamini–Hochbergmethod.Priortofitting,thePC1valuesofallsamples
werescaledsothatthesamplewiththesmallestPC1valueissetto0andtheone
withthehighestPC1valuea1.Thiswaytheestimatedcoefficient(logFC)is PreparationofcDNAandqPCR.TotalRNAwasdilutedtoafinalvolumeof11µl.
interpretableandrepresentstheestimatedaveragechangeinabundanceofa Twomicrolitersofrandomprimers(Promega)wereaddedafterwhichthemixture
particularcelltypefromthefirsttolastsample.Thiswasperformedonallsamples wasincubatedat65°Cfor5min.AmastermixcontainingTranscriptorReverse
fromstage1to4andclusterswithmorethananaverageof10cellspersample. Transcriptase(Roche),ReverseTranscriptasebuffer,2mMdNTPmixandRNasin
RibonucleaseInhibitors(Promega)wasthenadded.Thismixturewasincubatedat
25°Cfor10min,then42°Cfor40minandfinally70°Cfor10min.Theresulting
Differentialcorrelationanalysis.Inordertoidentifygenesthataredifferentially cDNAwasthendiluted1:2.5inHOforsubsequentuse.qPCRwasperformed
2
regulatedduringgestationandtumourigenesis,wetestedforgenesthataredif- usingaStep-OnePlusReal-TimePCRSystem(ThermofisherScientific).Taqman
ferentiallycorrelatedwithCsn2inthetwoconditionsusingthescHOTapproach29. (ThermoFisherScientific)probeswithGoTaqRealTimeqPCRMasterMix
ThiswasperformedonallcellsbelongingtotheLpandAvdclusterusing (Promega)wereused.TheenrichmentwasnormalisedwithcontrolmRNAlevels
Spearmancorrelationtestingforgeneswithatleast10non-zeroobservationsin ofGAPDHandrelativemRNAlevelswerecalculatedusingtheΔΔCtmethod
bothgroups. comparedtothecontrolgroup.ForthelistofprobesseeSupplementaryData2.
NATURECOMMUNICATIONS| (2021) 12:1502 |https://doi.org/10.1038/s41467-021-21783-3|www.nature.com/naturecommunications 9

ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-021-21783-3
Reportingsummary.FurtherinformationonresearchdesignisavailableintheNature 22. Lun,A.T.L.etal.EmptyDrops:distinguishingcellsfromemptydroplets
ResearchReportingSummarylinkedtothisarticle. indroplet-basedsingle-cellRNAsequencingdata.GenomeBiol.20,63
(2019).
Data availability 23. Lun,A.T.L.,McCarthy,D.J.&Marioni,J.C.Astep-by-stepworkflowfor
low-levelanalysisofsingle-cellRNA-seqdatawithbioconductor.
Theauthorsdeclarethatalldatasupportingthefindingsofthisstudyandunprocessed
F1000Research5,2122(2016).
imagesareavailablewithinthearticleanditssupplementaryinformationfilesorfrom
24. Lun,A.T.,Bach,K.&Marioni,J.C.Poolingacrosscellstonormalize
thecorrespondingauthoruponreasonablerequest.Therawsequencingdataare single-cellRNAsequencingdatawithmanyzerocounts.GenomeBiol.17,75
availableonArrayExpresswiththefollowingaccessionnumbers:E-MTAB-10043
(2016).
(scRNA-Seq),E-MTAB-10046(RNA-Seq)andE-MTAB-10054(ATAC-Seq).Processed
25. Csardi,G.&Nepusz,T.Theigraphsoftwarepackageforcomplexnetwork
datacanalsobeexploredanddownloadedathttp://marionilab.cruk.cam.ac.uk/ research.InterjournalComplexSyst.1695,1–9(2006).
BRCA1Tumourigenesis.AllcomputationalanalyseswereperformedinR(Version3.4.1)
26. Pijuan-Sala,B.etal.Asingle-cellmolecularmapofmousegastrulationand
usingstandardfunctionsunlessotherwiseindicated.Allcodeisavailableonlineat earlyorganogenesis.Nature566,490–495(2019).
https://github.com/MarioniLab/Tumorigenesis2018.Sourcedataareprovidedwith
27. Haghverdi,L.,Lun,A.T.L.,Morgan,M.D.&Marioni,J.C.Batcheffectsin
thispaper.
single-cellRNA-sequencingdataarecorrectedbymatchingmutualnearest
neighbors.Nat.Biotechnol.36,421(2018).
Received: 12November 2020; Accepted: 11February 2021; 28. McInnes,L.,Healy,J.,Saul,N.&Großberger,L.UMAP:UniformManifold
ApproximationandProjection.J.OpenSourceSoftw.3,861(2018).
29. Ghazanfar,S.etal.Investigatinghigher-orderinteractionsinsingle-celldata
withscHOT.Nat.Methods17,799–806(2020).
30. Solovey,M.&Scialdone,A.COMUNET:atooltoexploreandvisualize
intercellularcommunication.Bioinformatics36,4296–4300(2020).
References 31. Robinson,M.D.,McCarthy,D.J.&Smyth,G.K.edgeR:aBioconductor
packagefordifferentialexpressionanalysisofdigitalgeneexpressiondata.
1.
f
L
o
i
r
m
b
,
a
E
s
.
a
e
l
t
tu
al
m
.A
or
be
d
r
e
r
v
a
e
n
l
t
op
lu
m
m
e
i
n
n
t
al
in
pr
B
o
R
g
C
en
A
it
1
or
m
s
u
a
t
s
a
t
t
h
io
e
n
ca
c
n
ar
d
r
i
i
d
e
a
rs
te
.N
ta
a
r
t
g
.
e
M
tp
e
o
d
p
.
u
1
l
5
a
,
tion Bioinformatics26,139–140(2009).
907–913(2009). 32. Alexa,A.&Rahnenfuhrer,J.topGO:EnrichmentAnalysisforGeneOntology.
Rpackageversion2.40.0(Bioconductor,2020).
2. Molyneux,G.etal.BRCA1basal-likebreastcancersoriginatefromluminal
epithelialprogenitorsandnotfrombasalstemcells.CellStemCell7,403–417 33. B
T
u
ra
e
n
n
s
r
p
o
o
st
s
r
i
o
ti
,
o
J
n
.D
of
.,
n
G
at
i
i
r
v
e
e
si
c
,
h
P
r
.
o
G
m
.
a
,
t
Z
in
ab
f
a
o
,
r
L
fa
.
s
C
t
.
a
,
n
C
d
ha
se
n
n
g
s
,
i
H
tiv
.
e
Y
e
.
p
&
ige
G
n
r
o
e
m
en
ic
lea
p
f
r
,
o
W
fili
.
n
J
g
.
(2010).
ofopenchromatin,DNA-bindingproteinsandnucleosomeposition.Nat.
3.
b
B
y
ac
s
h
in
,
g
K
le
.
-
e
c
t
el
a
l
l.
R
D
N
i
A
ffe
s
r
e
e
q
n
u
ti
e
a
n
ti
c
o
i
n
ng
d
.
y
N
n
a
a
t
m
.
i
C
c
o
s
m
of
m
m
un
a
.
m
8
m
,2
ar
1
y
28
ep
(
i
2
t
0
h
1
e
7
li
)
a
.
lcellsrevealed Methods10,1213–1218(2013).
34. Li,H.&Durbin,R.FastandaccurateshortreadalignmentwithBurrows-
4.
a
W
du
at
l
s
t:
on
a
,
jo
C
u
.
r
J
n
.
e
&
yo
K
f
h
m
al
o
ed
rp
,
h
W
og
.
e
T
n
.
e
M
sis
am
an
m
d
a
c
r
o
y
m
d
m
ev
i
e
tm
lop
en
m
t.
en
D
t
e
i
v
n
elo
th
p
e
m
e
e
m
nt
b
1
ry
3
o
5,
and Wheelertransform.Bioinformatics25,1754–1760(2009).
995–1003(2008). 35. R
se
a
q
m
ue
ír
n
e
c
z
i
,
n
F
g
.
d
e
a
t
t
a
a
l.
a
d
n
e
a
e
ly
p
s
T
is
o
.
o
N
ls
u
2
c
:
le
a
ic
ne
A
x
c
t
id
g
s
en
R
e
e
r
s
a
.
t
4
io
4
n
,W
we
1
b
60
s
–
er
W
ve
1
r
6
f
5
or
(2
d
0
e
1
e
6
p
)
-
.
5. m Po i o ce le, by A. a J p . r e o t g a e l s . t P er r o e n ve e n a t n io t n ag o o f n B is r t. ca S 1 c - ie m n e c d e i 3 at 1 e 4 d , m 14 a 6 m 7– m 1 a 4 r 7 y 0 t ( u 2 m 00 o 6 r ) ig . enesisin 36. Robinson,J.T.etal.Integrativegenomicsviewer.Nat.Biotechnol.29,24–26
(2011).
6. Shin,H.Y.etal.HierarchywithinthemammarySTAT5-drivenWapsuper-
enhancer.Nat.Genet.48,904–911(2016). 37. Lun,A.T.L.&Smyth,G.K.csaw:aBioconductorpackagefordifferential
bindinganalysisofChIP-seqdatausingslidingwindows.NucleicAcidsRes.
7.
g
H
la
e
n
n
d
n
.
ig
N
h
a
au
t.
s
R
en
e
,
v.
L
M
.&
ol
R
.C
ob
e
i
ll
ns
B
o
i
n
ol
,
.
G
6
.
,
W
71
.
5
I
–
n
7
f
2
o
5
rm
(2
a
0
ti
0
o
5
n
).
networksinthemammary 44,e45–e45(2016).
38. Heinz,S.etal.Simplecombinationsoflineage-determiningtranscription
8. Robinson,G.W.,Johnson,P.F.,Hennighausen,L.&Sterneck,E.TheC/
factorsprimecis-regulatoryelementsrequiredformacrophageandBcell
E
di
B
ff
P
e
b
re
e
n
ta
tia
tr
t
a
io
n
n
sc
i
r
n
ip
t
t
h
io
e
n
m
fa
a
c
m
to
m
r
a
r
r
e
y
gu
g
l
l
a
a
t
n
e
d
s
.
e
G
pi
e
t
n
h
e
e
s
li
D
al
e
c
v
e
.
l
1
l
2
p
,
ro
1
l
9
if
0
e
7
r
–
a
1
ti
9
o
1
n
6
a
(
n
1
d
998).
identities.Mol.Cell38,576–589(2010).
9. Sau,A.etal.PersistentactivationofNF-κBinBRCA1-deficientmammary
progenitorsdrivesaberrantproliferationandaccumulationofDNAdamage. Acknowledgements
CellStemCell19,52–65(2016).
WewouldliketothankthestaffatSangerInstitute,ResearchServiceFacility(RSF),the
10. Ranjan,R.,Thompson,E.A.,Yoon,K.&Smart,R.C.C/EBPalphaexpression
staffattheCambridgeNIHRBRCCellPhenotypingHub,theGenomicsCoreatthe
ispartiallyregulatedbyC/EBPbetainresponsetoDNAdamageand
C/EBPalpha-deficientfibroblastsdisplayanimpairedG1checkpoint. CRUKCambridgeInstituteandattheWellcome-MRCStemCellInstitute,Cambridge
Oncogene28,3235–3245(2009). fortheirconstantsupportandassistance,thestaffatCambridgeBreastCancerResearch
UnitandattheBreastCancerNowTissueBankforprovidingthehumansamples.J.S.is
11. Efremova,M.,Vento-Tormo,M.,Teichmann,S.A.&Vento-Tormo,R.
CellPhoneDB:inferringcell–cellcommunicationfromcombinedexpression
fundedbytheEuropeanUnion’sHorizon2020researchandinnovationprogramme
ofmulti-subunitligand–receptorcomplexes.Nat.Protoc.15,1484–1506
undertheMarieSkłodowska-Curiegrantagreement(Pan-ILCno.840501)andbythe
Wallonie-BruxellesInternationalGrantofExcellenceWBI.WORLD(SUB/2019/441873).
(2020).
T.Y.F.H.isfundedbyTheRoyalSocietyandWellcomeTrust(204622/Z/16/Z)and
12. Fata,J.E.etal.Theosteoclastdifferentiationfactorosteoprotegerin-ligandis
essentialformammaryglanddevelopment.Cell103,41–50(2000). CancerResearchUK(CRUK)coreaward(A24995).J.C.M.acknowledgescorefunding
fromEMBLandcoresupportfromCancerResearchUK(C9545/A29580).W.T.K.is
13. Nolan,E.etal.RANKligandasapotentialtargetforbreastcancerprevention
inBRCA1-mutationcarriers.Nat.Med.22,933–939(2016). fundedbyaCRUKCareerEstablishmentAward(C47525/A17348),BBSRCprojectgrant
14. O’Brien,C.A.ControlofRANKLgeneexpression.Bone46,911–919(2010). (BB/S006745/1),MRCProjectGrant(MR/S036059/1),BreastCancerNowProjectGrant
(2017MayPR907),UniversityofCambridgeandMagdaleneCollege,Cambridge.
15. Klement,J.D.etal.Anosteopontin/CD44immunecheckpointcontrolsCD8
+Tcellactivationandtumorimmuneevasion.J.Clin.Invest.128,5549–5560
(2018). Author contributions
16. Dawson,C.A.etal.Tissue-residentductalmacrophagessurveythe
K.B.performedandanalysedthescRNA-seqexperiments.S.Pensaperformedand
mammaryepitheliumandfacilitatetissueremodelling.Nat.CellBiol.22,
supervisedallnon-computationalexperiments.M.Z.performedandanalysedtheATAC-
546–558(2020).
Seqexperiment.K.K.performedthelibrarypreparationofthescRNA-seqexperiments.
17. Jäppinen,N.etal.Fetal-derivedmacrophagesdominateinadultmammary
J.S.,S.PinaudandT.Y.F.H.helpedanalysingthescRNA-seqdataoftheimmunecom-
glands.Nat.Commun.10,281(2019). partment.K.A.L.maintainedtheBlg-Cre;Brca1f/f;p53+/−colony.M.S.andC.C.were
18. Katzenelenbogen,Y.etal.CoupledscRNA-Seqandintracellularprotein
involvedincollectingandanalysingthehumansamplesfromCambridge.S.J.H.,B.M.S.,
activityrevealanimmunosuppressiveroleofTREM2incancer.Cell182,
A.R.G.andR.C.wereinvolvedinthecollectionandprocessingofsomeofthehuman
872–885.e19(2020).
samplesfromBCN.J.C.M.co-supervisedK.B.andoversawthescRNA-seqanalysis.K.B.,
19. McCarthy,A.etal.Amousemodelofbasal-likebreastcarcinomawith
S.PensaandW.T.K.wrotethemanuscriptwithinputfromtheotherauthors.W.T.K.
metaplasticelements.J.Pathol.211,389–398(2007).
conceptualisedandsupervisedthestudy.
20. Shehata,M.&Stingl,J.Purificationofdistinctsubsetsofepithelialcellsfrom
normalhumanbreasttissue.MethodsMol.Biol.1501,261–276(2017).
21. Venables,W.N.&RipleyB.D.ModernAppliedStatisticswithS.Statisticsand Competing interests
Computing(Springer,2002). Theauthorsdeclarenocompetinginterests.
10 NATURECOMMUNICATIONS| (2021) 12:1502 |https://doi.org/10.1038/s41467-021-21783-3|www.nature.com/naturecommunications

ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-021-21783-3
Additional information Open Access This article is licensed under a Creative Commons
SupplementaryinformationTheonlineversioncontainssupplementarymaterial Attribution 4.0 International License, which permits use, sharing,
availableathttps://doi.org/10.1038/s41467-021-21783-3. adaptation,distributionandreproductioninanymediumorformat,aslongasyougive
appropriatecredittotheoriginalauthor(s)andthesource,providealinktotheCreative
CorrespondenceandrequestsformaterialsshouldbeaddressedtoJ.C.M.orW.T.K. Commonslicense,andindicateifchangesweremade.Theimagesorotherthirdparty
materialinthisarticleareincludedinthearticle’sCreativeCommonslicense,unless
PeerreviewinformationNatureCommunicationsthankstheanonymousreviewer(s)for
indicatedotherwiseinacreditlinetothematerial.Ifmaterialisnotincludedinthe
theircontributiontothepeerreviewofthiswork. article’sCreativeCommonslicenseandyourintendeduseisnotpermittedbystatutory
regulationorexceedsthepermitteduse,youwillneedtoobtainpermissiondirectlyfrom
Reprintsandpermissioninformationisavailableathttp://www.nature.com/reprints
thecopyrightholder.Toviewacopyofthislicense,visithttp://creativecommons.org/
licenses/by/4.0/.
Publisher’snoteSpringerNatureremainsneutralwithregardtojurisdictionalclaimsin
publishedmapsandinstitutionalaffiliations.
©TheAuthor(s)2021
NATURECOMMUNICATIONS| (2021) 12:1502 |https://doi.org/10.1038/s41467-021-21783-3|www.nature.com/naturecommunications 11