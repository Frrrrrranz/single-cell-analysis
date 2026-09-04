communications biology

Article

https://doi.org/10.1038/s42003-024-07315-x

Cross-species single-cell RNA-seq
analysis reveals disparate and conserved
cardiac and extracardiac inﬂammatory
responses upon heart injury

Check for updates

Eric Cortada 1,2,6, Jun Yao 2,3,6, Yu Xia2,3,6, Friederike Dündar
Alfonso Rubio-Navarro 1,2, Björn Perder2,3, Miaoyan Qiu2,3, Anthony M. Pettinato1, Edwin A. Homan1,2,
Lisa Stoll

4, Paul Zumbo4, Boris Yang1,2,

& James C. Lo 1,2

, Jingli Cao 2,3

1,2, Doron Betel

4,5

;
,
:
)
(

0
9
8
7
6
5
4
3
2
1

;
,
:
)
(

0
9
8
7
6
5
4
3
2
1

The immune system coordinates the response to cardiac injury and controls regenerative and ﬁbrotic
scar outcomes in the heart and subsequent chronic low-grade inﬂammation associated with heart
failure. Adult mice and humans lack the ability to fully recover while adult zebraﬁsh spontaneously
regenerate after heart injury. Here we proﬁle the inﬂammatory response to heart cryoinjury in zebraﬁsh
and coronary artery ligation in mouse using single cell transcriptomics. We interrogate the extracardiac
reaction to cardiomyocyte necrosis to assess the speciﬁc peripheral tissue and immune cell reaction
to chronic stress. Cardiac macrophages play a critical role in determining tissue homeostasis by
healing versus scarring. We identify distinct transcriptional clusters of monocytes/macrophages
(mono/Mϕ) in each species and ﬁnd analogous pairs in zebraﬁsh and mice. However, the reaction to
myocardial injury is largely disparate between mice and zebraﬁsh. The dichotomous response to heart
damage between the murine and zebraﬁsh mono/Mϕ and/or the presence of distinct zebraﬁsh mono/
Mϕ subtypes may underlie the impaired regenerative process in adult mammals and humans. Our
study furnishes a direct cross-species comparison of immune responses between regenerative and
proﬁbrotic myocardial injury models, providing a useful resource to the ﬁelds of regenerative biology
and cardiovascular research.

Cardiovascular disease is the leading cause of death worldwide with
myocardial infarction (MI) and its complications including congestive
heart failure (CHF) accounting for the lion’s share of the burden1,2. It has
long been known that local tissue injury induces distal organ or even
whole-body responses3. Despite the local nature of the cardiac injury, the
adverse effects of MI are not restricted to the cardiovascular system. Sur-
vivors of MI often experience liver and kidney injury, fever, inﬂammation
and have increased risk of certain cancers and ischemic stroke4–6. In
humans and other mammals, MI resulting from an acute disruption in
coronary artery blood ﬂow to the heart leads to cardiomyocyte necrosis.
Due to the incapacity of the adult mammalian heart to regenerate, the heart

is ultimately repaired through a predominantly ﬁbrotic process with many
patients suffering from CHF.

It is well known that MI and heart failure with reduced ejection fraction
are associated with chronic low-grade inﬂammation7. That chronic
inﬂammation after MI can drive adverse cardiovascular events has been
elegantly shown in clinical trials with blockade of some inﬂammatory
pathways8,9. Post-MI inﬂammation may also contribute to the pathogenesis
of breast and lung cancer, and chronic liver and kidney disease10–13. The
dynamic inﬂammatory process post-MI evolves from an acute phase
characterized by the elaboration of proinﬂammatory cytokines and che-
mokines, immune cell inﬁltration to the site of injury, and systemic

1Division of Cardiology, Department of Medicine, Weill Center for Metabolic Health, Weill Cornell Medicine, New York, NY, USA. 2Cardiovascular Research Institute,
Weill Cornell Medicine, New York, NY, USA. 3Department of Cell and Developmental Biology, Weill Cornell Medicine, New York, NY, USA. 4Applied Bioinformatics
Core, Weill Cornell Medicine, New York, NY, USA. 5Institute for Computational Biomedicine, Division of Hematology and Medical, Oncology, Department of
Medicine, Weill Cornell Medicine, New York, NY, USA. 6These authors contributed equally: Eric Cortada, Jun Yao, Yu Xia.
jic4001@med.cornell.edu; jlo@med.cornell.edu

e-mail: dob2014@med.cornell.edu;

Communications Biology |

 (2024) 7:1611

1

https://doi.org/10.1038/s42003-024-07315-x

Article

leukocytosis. This is followed by a resolution or reparative phase punctuated
by a tissue clearing and ﬁbrotic cell and gene program in the heart with
macrophages playing a large role and unresolved systemic inﬂammation in
some patients14–20.

Unlike mammals, adult zebraﬁsh possess a remarkable capacity for
cardiac regeneration with minimal scarring. This is achieved through pro-
liferation of spared cardiomyocytes with cellular and molecular supports
from non-muscle cells including immune cells21,22. Cryoinjury of the zeb-
raﬁsh heart triggers a sequence of dynamic pro- and anti-inﬂammatory
programs that govern successful myocardial regeneration23,24. Swift neu-
trophil inﬁltration to the injury site in the acute inﬂammation stage (within 1
day of injury) is followed by macrophage recruitment that spans the
inﬂammatory and regenerative stages (until 7 days after injury), while
natural killer (NK) or T cells actively participate in the regeneration
stage23,25–28. This process employs various, functionally diverse populations
of macrophages that play vital roles for zebraﬁsh heart regeneration23,27–30.
Early macrophage inﬁltration of the wound is critical for successful regen-
eration and results in transient ﬁbrosis through direct and indirect con-
tributions to the extracellular matrix (ECM)27,31. Subsequently,
the
microenvironment undergoes a transition to an anti-inﬂammatory stage
that involves distinct macrophages in scar resolution23,24. Moreover, mac-
rophages are reported to stimulate cardiomyocyte proliferation during heart
development through activation of the epicardium and promote angio-
genesis during wound healing32,33. This leaves open the possibility that the
different immune responses to cardiac injury may underly the diametrically
opposed cardiac and extra-cardiac outcomes between adult mammals and
zebraﬁsh.

Here we used unbiased single-cell transcriptomics to proﬁle the
dynamic immune response to cardiac injury in the heart, blood, liver, kid-
ney, and pancreatic islets of mice and zebraﬁsh. This allowed us to identify
analogous immune cell subtypes between the two species along with con-
served and disparate responses to cardiac injury within the heart and per-
ipheral organs. We identiﬁed similar cardiac monocyte/macrophage
(mono/Mϕ) subclusters present in both mice and zebraﬁsh, although the
responses of the shared mono/Mϕ subtypes were dramatically different after
myocardial injury. Additionally, there were unique mono/Mϕ subclusters
for each species. This study provides support for both differences in mono/
Mϕ subtypes between species and the largely disparate reactions to heart
injury among these analogous subtypes that may determine healing versus
heart failure with systemic inﬂammation. Furthermore, the datasets and
hypotheses generating analyses supplied here will serve as a resource to the
ﬁeld of regenerative biology to enable follow-up studies.

Results
Single cell transcriptomic dissection of the multiorgan response
to cardiac injury in mice and zebraﬁsh
To interrogate the multiorgan response to heart injury between ﬁbrotic and
regenerative models, we performed single cell RNA-Seq (scRNA-Seq)
analyses on the heart, blood, and peripheral organs of adult mice and zeb-
raﬁsh (Fig. 1a, b). In a model of cardiac scarring, 10–12 week old mice
underwent permanent left anterior descending (LAD) coronary artery
ligation or sham surgery with scRNA-Seq analyses at 1, 7, and 30 days post
injury (dpi) (Fig. 1a). Sham controls were chosen to speciﬁcally assess the
effect of MI rather than acute inﬂammation from open chest surgery34. 1 dpi
is representative of an acute MI with the initial proinﬂammatory phase,
while day 7 is part of the subacute phase when the inﬂammatory response
shifts toward a reparative phase35. Finally, 30 dpi represents chronic MI with
left ventricular (LV) systolic heart failure (HF) with an average left ven-
tricular ejection fraction (LVEF) of 27% (Supplementary Fig. 1a–c)36. For
comparisons between regenerative and non-regenerative models, we chose
the cryoinjury model in adult zebraﬁsh with the hope to enrich for immune
cells in order to detect potential rare subtypes. This is because cryoinjury
leaves necrotic tissues in the heart and causes stronger inﬂammatory
responses with more inﬁltrating immune cells than the wildely-used apex
resection model (e.g., reviewed in ref. 21). We performed scRNA-Seq of

zebraﬁsh cells from the heart, liver, pancreas, and whole kidney marrow
(WKM) at 1 and 7 days post heart cryoinjury (dpci) together with the
uninjured control (Ctrl) (Fig. 1b). These 2 timepoints represent acute
inﬂammatory (1 dpci) and regenerative stages (7 dpci), respectively25.
Because cardiac immune responses upon heart injury in zebraﬁsh are
predominantly enriched in the ﬁrst 2 weeks, we did not include a 30 dpci
sample, which is likely similar to an uninjured sample23. Approximately
196,000 murine and 70,783 zebraﬁsh cells were included in the analyses
(Fig. 1c, d). The zebraﬁsh scRNA-Seq analyses were performed with two
biological replicates, while samples from two tissue donors were pooled for
most of mouse experiments. Cell type labeling was performed using SingleR
(see Methods) and validated by the expression of known marker genes
(Fig. 1c and Supplementary Fig. 1d; Fig. 1d and Supplementary Fig. 2a–d
and Supplementary Data 1)37.

Chronic systemic inﬂammation in mice following MI
Across the mouse tissues analyzed, immune cells represented the majority
(56%) of the cells surveyed by scRNA-Seq. Granulocytes represented the
majority of white blood cells (WBCs) at 1 dpi and were abundant in the heart
of the MI group at 1 dpi (35%) but dropped to almost zero at 7 dpi (Sup-
plementary Fig. 1e). The WBC composition was independently conﬁrmed by
ﬂow cytometry in separate cohorts of mice (Supplementary Fig. 1f, g).
Excluding WBCs, immune cells in peripheral tissues accounted for 18% of the
murine cells sequenced, with elevated numbers of immune cells in tissues
from MI compared to sham (heart 43% vs. 27%; liver 20% vs. 9%), which is
consistent with MI inciting an inﬂammatory response (Supplementary
Fig. 1e). In the heart, the major immune cell type was mono/Mϕ at all
timepoints. Small numbers (<200) of cardiomyocytes were sequenced as we
did not employ single nuclei RNA-Seq (snRNA-Seq) and were excluded from
the analysis since this was not the focus of our study. Beta cells were the
dominant cell type within pancreatic islets and no major changes in islet cell
composition were detected with MI (Supplementary Fig. 1e).

We found that MI induced a strong transcriptional response in all of
the major immune cell types across multiple organs during all phases of MI
(Fig. 1e). Mono/Mϕ cells were the most abundant immune cells in all of the
organs we sequenced at all timepoints. While the ratio of sequenced par-
enchymal cells minimally changed, immune cell ratios and absolute counts
displayed dynamic changes in response to MI (Supplementary Fig. 1e–g).
Blood B and T cells increased dramatically over time in both sham and MI
groups, from close to 0% at 1 and 7 dpi to a majority of the WBCs at 30 dpi,
consistent with previous reports that major surgeries or trauma can cause
transient lymphopenia in blood38 (Supplementary Fig. 1e, g). The frequency
of blood monocytes peaked at 1 dpi in the MI group and at 7 dpi in the sham
group. By day 30, mono/Mϕ remained slightly higher in the MI group
compared to the sham (7 vs 2%). This trend was conﬁrmed by ﬂow cyto-
metry (Supplementary Fig. 1g). In the heart at 1 dpi, the MI group had
increased frequency of granulocytes compared to sham. By day 30, both
sham and MI groups had similar number of mono/Mϕ in the heart (Sup-
plementary Fig. 1e). In contrast, liver mono/Mϕ accounted for similar
proportions of the liver immune cells at 1 and 7 dpi; however, at 30 dpi, the
sham was exclusively composed of Kupffer cells (i.e., resident macrophages)
whereas the MI group consisted of a more diverse set of immune cells such
as mono/Mϕ, T, B, and NK cells, suggesting chronic liver inﬂammation post
MI (Supplementary Fig. 1e). Similarly, in the kidney we observed a trend of
~2-fold increase in the percentage of mono/Mϕ at 30 dpi in the MI com-
pared to sham.

To identify which organs and cells were most strongly perturbed in
each of the two diametrically opposed heart injury models, we assessed the
number of differentially expressed genes (DEGs). In mouse, MI elicited
substantial numbers of DEGs (>700) in the heart, liver, and leukocytes
(Fig. 1e and Supplementary Data 2). By contrast, the pancreatic islets were
largely unaffected by MI with <25 DEGs. In the heart, most of the gene
expression changes with MI in non-immune cells were found at 1 dpi in
ﬁbroblasts and endothelial cells. This transcriptional perturbation decreased
substantially at later timepoints, consistent with resolution of local injury by

Communications Biology |

 (2024) 7:1611

2

https://doi.org/10.1038/s42003-024-07315-x

Article

Fig. 1 | Multiorgan response to cardiac injury in mouse and zebraﬁsh by scRNA-
Seq. Experimental outline for mouse (a) or zebraﬁsh (b) heart injury and sampling
for scRNA-seq analysis. A scRNA-seq analysis was done per sample, for a total of 28
murine samples (5 tissues, 3 timepoints except for the kidney which were analyzed at
7 and 30 dpi, and 2 conditions, sham and MI. Each sample included cells from one or
two biological replicates combined 1:1). 24 zebraﬁsh samples (4 tissues, 3 conditions,
and 2 biological replicates) were included. a was created with BioRender. c UMAPs
(Uniform manifold approximation and projection) of the 194,315 cells (from 41

mice; 22 sham and 19 MI) colored by timepoint (left), tissue of origin (center) and
cell type (right). Dpi, days post infarction. d UMAP of 70,783 zebraﬁsh cells showing
treatments timepoints (left), tissue of origin (center) and cell type (right). Dpci, days
post cardiac injury; WKM, whole kidney marrow; Ctrl, uninjured. Bar plot of DEGs
(MI compared to sham procedure) in mice (e) and zebraﬁsh (f) by tissue and cell
type. Bars are colored by timepoint. Genes with FDR < 0.05 and absolute
log2(FC) > 0.25 were considered differentially expressed.

30 dpi (Fig. 1e). In the liver, hepatocytes showed more transcriptional
perturbation at 1 dpi with MI, while 30 dpi was highest for endothelial cells
(Fig. 1e), indicating major transcriptional responses that vary by cell type in
acute and chronic MI. The DEG count for kidney epithelial cells was similar
at 7 and 30 dpi with MI, suggesting peripheral organ gene dysregulation
with chronic MI. The temporal effects of MI were also dependent on the

speciﬁc immune cell type as granulocytes displayed high DEG counts early
(1 and 7 dpi) whereas T cells were affected later (7 and 30 dpi), which could
reﬂect early activation of the innate immune system with acute injury fol-
lowed by chronic T cell activation. Overall, our results suggest that acute MI
in mice triggered an intense local response that may resolve by day 7 in the
heart but remain activated at day 30 in some extracardiac organs.

Communications Biology |

 (2024) 7:1611

3

https://doi.org/10.1038/s42003-024-07315-x

Article

Cardiac and systemic responses after heart injury in zebraﬁsh
In zebraﬁsh, heart cells had the most signiﬁcant changes in cell type fractions
with cryoinjury (Supplementary Fig. 2e, f). The uninjured sample contained
about 11% cardiomyocytes (myl7+tnnt2a+)39, 7% mono/Mϕ (c1qa+)40, 5%
NK or T cells (zbtb32+il2rb+ or lck+zap70+)41–43, 3% thrombocytes
(itga2b+)44, 2% B cells (cd37+)45, and 1% neutrophils (mpx+)46. The
remaining cell types, including epicardial cells and ﬁbroblasts (tcf21+)47,
endocardial and endothelial cells (kdrl+), and mural cells (pdgfrb+)48, con-
tributed about 14% of all cells, which are labeled as Mixed cluster 5 (Fig. 1d
and Supplementary Fig. 2). The mono/Mϕ and neutrophil populations
sharply expanded to 26% and 6% of all cells at 1 dpci, respectively, indicating
an acute inﬂammatory response. By 7 dpci, when mono/Mϕ were down to
13% and neutrophils to 1%, whereas the number of NK/T cells and B cells
increased to 8% and 3%, respectively (Supplementary Fig. 2e, f). These
observations match previous reports that macrophages and neutrophils
dominate the acute inﬂammatory stage while NK/T cells take on a larger role
during regeneration23,25.

For the liver, cell type fractions were largely unchanged across samples
with hepatocytes constituting ~70% of cells (fabp10+cp+, Supplementary
Fig. 2c, e, f)49. The zebraﬁsh pancreatic islets and exocrine lobules tightly
adhere to intestinal and hepatic tissues and our dissection method may not
be ideal for isolating islet cells (<2% of the total, included in the Mixed
cluster 5). The primary cell type fractions in the Ctrl sample are acinar cells
(prss1+ela2+)50, mono/Mϕ, neutrophils, NK/T cells, and B cells (Supple-
mentary Fig. 2e, f). The mono/Mϕ ratio decreased from 27% in ctrl to 19% at
1 dpci and 17% at 7 dpci. The main WKM cell fractions in the Ctrl consisted
of neutrophils, mono/Mϕ, erythrocytes, hematopoietic stem or progenitor
cells (HPC, runx1t1+meis1b+csf1rb+)51, B cells, and NK/T cells (Supple-
mentary Fig. 2e, f). The neutrophil population transiently expanded from
21% in the Ctrl to 32% at 1 dpci and reduced back to ctrl levels of 23% at
7 dpci. By contrast, the mono/Mϕ fraction shrunk from 20% in the Ctrl to
14–15% at 1 and 7 dpci.

We further analyzed the kinetic response of the 29,432 immune cells
that consisted of 36% mono/Mϕ, 29% neutrophils, 20% NK/T cells, and 15%
B cells (Supplementary Fig. 3a). The number of mono/Mϕ sharply increased
in the heart at 1 dpci, making it the most abundant cells, whereas in other
organs mono/Mϕ decreased synchronously (Supplementary Fig. 3b). By
contrast, the numbers of neutrophils in the heart and WKM increased
concurrently at 1 dpci. Interestingly, minor changes in the abundance of
immune cells in the liver were detected (Supplementary Fig. 3b), suggesting
that the liver likely has minimal immune responses upon heart injury. In
summary, compared to the heart samples, cell fractions in the non-cardiac
organs were relatively stable upon heart injury.

We next assessed the number of DEGs in zebraﬁsh organs by cell type
(Fig. 1f). Similar to the mouse results, the most dramatic changes in zeb-
raﬁsh were detected in hepatocytes and immune cells such as blood and
tissue macrophages and neutrophils. Hepatocytes showed 504 and 371
DEGs at 1 and 7 dpci, respectively. In heart mono/Mϕ, we detected 666 and
253 DEGs at 1 and 7 dpci, respectively (Fig. 1f). Liver, pancreas, and WKM
macrophages and neutrophils showed similar results with generally higher
number of DEGs at 1 dpci but continued transcriptional perturbation at
7 dpci (Fig. 1f and Supplementary Data 2). Thus, we observed systemic
immune cell activation, especially in macrophages, in both the injured heart
and distal organs. While cardiac inﬂammation resolved by 7 dpci, peripheral
inﬂammation was present. Taken together, these results suggest that both
species employ local and peripheral cellular responses to heart injury, and
the extracardiac response continues at 30 dpi
in the scar-forming
mouse model.

Dynamic cardiac and extracardiac mono/Mϕ subcluster
response to myocardial injury in mice
Our data suggest that MI may trigger a dynamic gene program in blood
monocytes from 1 to 30 dpi (Fig. 2a, b and Supplementary Data 3). At 7 dpi
there was enrichment of EIF2 Signaling, mTOR signaling, Fc gamma
receptor-mediated phagocytosis, and integrin signaling pathways with

many showing inhibition (Fig. 2a, b and Supplementary Data 3). While at
30 dpi, the complement, antigen presentation, and alternative activation
signaling pathways were enriched in monocytes with MI. Collectively, this
pattern suggests a potentially transient inhibition of many monocyte acti-
vation pathways in the subacute stage that later transitions to activation with
chronic MI. Intriguingly, some of the inﬂammatory pathways active on day
1 were active a month later in WBCs even after resolution of inﬂammation
in the heart, indicating persistent monocyte activation with chronic MI.
Mono/Mϕ comprise a heterogenous group of cell types, with signiﬁcant
differences and functions depending on their origin and localization52.
Moreover, the simultaneous detection of pro- and anti-inﬂammatory
pathways in monocytes suggests the coexistence of different monocyte
subpopulations that may reﬂect the complex and multifaceted response of
these cells to MI.

To determine if MI could induce different responses in speciﬁc mono/
Mϕ subtypes, we performed a more focused analysis restricted to these cells,
from the different organs, timepoints, and sham/MI experimental groups.
Cells were reclustered to identify six mono/Mϕ subsets. We performed
pathway analyses on the top marker genes for each mono/Mϕ subcluster to
ascertain their function, and assessed the expression of macrophage markers
(Fig. 2c–e Supplementary Fig. 4a and Supplementary Data 3).

Cluster 1 mono/Mϕ were mostly found in the blood and heart at 1 and
7 dpi, expressed the highest levels of Arg1, Spp1, and Ccl2, and were enriched
in glycolysis, gluconeogenesis, cytokine storm, and adhesion and diapedesis
pathways, suggesting a classical proinﬂammatory phenotype (Fig. 2d–f and
Supplementary Fig. 4a, b). Cluster 2 mono/Mϕ increased in numbers in the
blood following 1 dpi in both sham and MI groups, expressed high levels of
MHC class II genes and were highly enriched in antigen presentation, EIF2,
PD-1, and mTOR signaling pathways, suggesting immune modulation and
increased RNA translation and metabolic activity in these cells (Fig. 2d–f
and Supplementary Fig. 4a, b). Cluster 3 cells were present in the blood of
both experimental groups but found at elevated numbers in the heart at
1 dpi and kidneys and liver at 30 dpi in the MI group (Fig. 2f and Supple-
mentary Fig. 4b). The cluster 3 mono/Mϕ expressed the highest levels of
Ly6c2 and were enriched in Fcγ receptor-mediated phagocytosis, produc-
tion of nitric oxide and reactive oxygen species, EIF2, and regulation of EIF4
and p70S6K signaling, and metabolic pathways (oxidative phosphorylation,
mitochondrial dysfunction, and mTOR Signaling) with an activation pat-
tern suggesting high metabolic and phagocytic activity (Fig. 2d–f and
Supplementary Fig. 4a, b).

By contrast, Cluster 4 cells were predominantly found in tissues but not
detected in the blood, consistent with a tissue macrophage phenotype
(Fig. 2c, f and Supplementary Fig. 4b). Supporting this, cluster 4 macro-
phages in the liver had high expression of Clec4f, a Kupffer cell marker
(Supplementary Fig. 4c). Cluster 4 macrophages expressed the highest levels
of Mrc1, Timd4, Lyve1, and Folr2 and were enriched in LXR/RXR
activation, endocytosis, complement, and phagocytic pathways53 (Fig. 2d, e).
Mono/Mϕ cluster 5 was temporarily present in the blood of the MI group
only at 7 dpi. DEGs for Cluster 5 suggested a role for these cells in iron
homeostasis and hypoxia with heme and tetrapyrrole biosynthesis and
hypoxia pathways enriched (Fig. 2e, f and Supplementary Fig. 4a, b). Lastly,
Cluster 6 cells represented over half (57%) of the blood monocytes in the
sham group at 7 dpi and were overrepresented (25%) in the MI group at
30 dpi while these cells were present at trace amounts (4%) in the sham
group (Fig. 2f and Supplementary Fig. 4b). Complement, leukocyte extra-
vasation, antigen presentation, and hepatic ﬁbrosis were among the top
pathways overrepresented in Cluster 6 cells (Fig. 2e). Altogether our data
suggest that MI may regulate both the mono/Mϕ composition and their
activation status in blood and peripheral tissues.

Dynamic cardiac and extracardiac mono/Mϕ subcluster
response to myocardial injury in zebraﬁsh
Zebraﬁsh monocytes and macrophages are highly heterogeneous28,30,54,55.
Our initial clustering result indicated two macrophage subpopulations in
zebraﬁsh (clusters 9 and 15, Supplementary Fig. 2a). To further interrogate

Communications Biology |

 (2024) 7:1611

4

https://doi.org/10.1038/s42003-024-07315-x

Article

Fig. 2 | Dynamic cardiac and extracardiac mono/Mϕ subcluster response to
myocardial injury in mice. a Dot plot depicting enriched pathways in monocytes at
1, 7, and 30 days post infarction (dpi). b Dot plot shows gene expression in blood
monocytes by experimental group (MI or SH) and timepoint. c UMAPs of all
37,215 sequenced mono/Mϕ reclustered, colored by timepoint (left), cluster (center)
and tissue of origin (right). d Dot plot shows normalized gene expression (dot color
intensity) across all analyzed mono/Mϕ clusters, regardless of tissue, timepoint and
sham or MI procedure. Common mono/Mϕ marker genes and MHC-II and TLF
(Timd4, Lyve1 and Folr2) genes are indicated. e Dot plot depicting enriched

pathways in mono/Mϕ cell subclusters, regardless of tissue of origin, timepoint or
sham/MI. f Stacked column plot shows percentage of the 6 murine subclusters (C1-
C6) of total mono/Mϕ by condition, timepoint and tissue. In (a) and (e) Dot size
represents statistical signiﬁcance of enrichment, dot color represents z-score.
Positive z-score predicts activation of the pathway in the MI compared to the sham
group and negative z-score predicts inhibition of the pathway in the MI compared to
the sham group. Gray dots denote undetermined activation status. In (b) and (d):
Color intensity in dot plots represents normalized mean expression, dot size
represents fraction of cells expressing the gene.

Communications Biology |

 (2024) 7:1611

5

https://doi.org/10.1038/s42003-024-07315-x

Article

the heterogeneity and dynamics of zebraﬁsh macrophages after heart injury,
we clustered all the zebraﬁsh macrophages and identiﬁed seven clusters
(Fig. 3a). Clusters 1 and 2 were predominantly derived from the WKM,
constituting 21% and 14% of all macrophages, respectively (Fig. 3b–d).
Cluster 3 (8% of the total) was primarily pancreatic and cluster 4 (9% of the
total) was primarily from the heart (Fig. 3b–d). Cluster 5 was the smallest

mono/Mϕ subpopulation (2%). Cluster 6 (31%) was the most abundant,
constituting 31% of all macrophages and present in all 4 organs. Similarly,
cluster 7 had no organ speciﬁcity and contributed 15% of all macrophages.
Interestingly, four subclusters (1, 3, 6, and 7) were enriched in the uninjured
control, with their numbers synchronously decreasing at 1 dpci before
rebounding at 7 dpci (Fig. 3e). By contrast, the fractions of clusters 4 and 5

Communications Biology |

 (2024) 7:1611

6

https://doi.org/10.1038/s42003-024-07315-x

Article

Fig. 3 | Mono/Mϕ response to cryoinjury in zebraﬁsh. a UMAPs of 10,709
reclustered mono/Mϕ, colored by treatment group (Ctrl, 1 dpci, or 7 dpci; left),
cluster (center) and tissue of origin (right). WKM, whole kidney marrow; Ctrl,
uninjured; dpci, days post heart cryoinjury. b Fractions of each subcluster over total
macrophages and monocytes. Tissue distribution of each mono/Mϕ subcluster
grouped by cluster (c) or tissue and treatment group (d). e Dynamics of subcluster
fractions over total mono/Mϕ in each treatment group (Ctrl, 1 dpci, or 7 dpci) across
three groups. f UMAPs showing expression patterns of selected marker genes.
g Enriched biological process terms (top) and KEGG pathway (bottom) for the
subcluster markers (mean AUC > 0.6). The gene ratio is indicated by the dot size and
the signiﬁcance by the color of the dot (P < 0.05). h, i, Images of heart cryosection
showing HCR staining signals of gda in green and moxd1 in magenta in Ctrl

(uninjured), 1 dpci, and 7 dpci samples. Anti-lcp1 staining is shown in blue. DAPI
staining is shown in white. The framed regions are enlarged to show details on the
right with different channel combinations. Arrowheads and arrows indicate
representative gda+lcp1+ and moxd1+lcp1+ cells, respectively. Scale bar, 100 μm.
j Quantiﬁcation of gda+lcp1+ cells in the wound in Ctrl (uninjured), 1 dpci, and
7 dpci samples. n = 3 (Ctrl), 7 (1 dpci), and 8 (7 dpci). Mean ± S.D. Student’s t-test
versus the control. k Images of heart cryosection showing HCR staining signals of
havcr1 and moxd1 at 1 dpci in green and magenta, respectively. Anti-lcp1 staining is
shown in blue. DAPI staining is shown in white. The framed regions are enlarged to
show details on the right with different channel combinations. Arrowheads and
arrows indicate representative havcr1+lcp1+ and moxd1+lcp1+ cells, respectively.
Scale bar, 100 μm.

(enriched in the heart) drastically increased at 1 dpci, but quickly dropped to
the uninjured level at 7 dpci, indicating the transiently expanded mono/Mϕ
subsets in the heart. Cluster 2 also increased at 1 dpci and stayed high at
7 dpci (Fig. 3e). Thus, the zebraﬁsh mono/Mϕ population was highly het-
erogeneous and dynamic with heart injury.

We next looked for cluster markers to characterize these mono/Mϕ
subsets. The WKM-dominating cluster 1 was enriched for expression of
translation and ribosome biogenesis-associated genes such as eef1g, rpl15,
and eif2s3 (Supplementary Fig. 3c, Fig. 3f, g, and Supplementary Data 4, 5).
This cluster also preferentially expressed the M2 macrophage marker mrc1b
(Cd206 in mice), copper ion binding protein gene moxd1, and calcium ion
binding protein genes icn and s100a10b. Cluster 2 shared most of the cluster
1 marker genes at a relatively lower expression level, in addition to the
enriched expression of histone modiﬁcation and chromatin regulatory
genes such as hmgn2, h2az2b, and mki67 and nucleotide metabolism gene
dut (Fig. 3f and Supplementary Fig. 3c). The pancreatic cluster 3 showed
high expression of antigen component cd7al, glycoprotein gene gpnmb, and
lysosomal activity-related genes such as asah1b, lgmn, and ctsd (Fig. 3f,
Supplementary Fig. 3c, and Supplementary Data 4). Notable enriched GO
terms in this cluster were negative regulation of cell proliferation, leukocyte
activation, and regulation of intrinsic apoptotic signaling pathway (Fig. 3g
and Supplementary Data 5). The heart-dominated cluster 4 had enriched
expression of cd9b, fn1a, lipf, gpc1b, gda, and hsp70.1, which are associated
with cell adhesion, response to oxygen levels, protein or vesicle transport,
protein folding, or endomembrane system organization (Fig. 3f, g, Sup-
plementary Fig. 3c, and Supplementary Data 5). Enriched KEGG pathways
in cluster 4 were phagosome, lysosome, and endocytosis, suggesting active
phagocytosis (Fig. 3g and Supplementary Data 5). Notably, fn1a encodes the
pro-regenerative ECM protein ﬁbronectin56. Cluster 5 had enriched
expression of oxygen transport-associated gene hbaa1, ribosomal genes
such as rpl17, and oxidative stress-responsive gene lgals2a (Fig. 3f, g, and
Supplementary Fig. 3d). Cluster 6 had high expression of standard mac-
rophage markers such as mpeg1.1, cd74a, mhc2a, marco, mfap4, and havcr1.
The top enriched GO terms were mostly regulators of the immune system
process: antigen processing and presentation, leukocyte activations, and
KEGG pathways were lysosome, phagosome, and apoptosis (Fig. 3f, g,
Supplementary Fig. 3c, and Supplementary Data 4, 5). Cluster 7 exhibited
high expression of defense response-related genes lygl1 and cybb and shared
marker genes enriched in translation with cluster 1, such as rpl15 and copper
ion binding protein gene moxd1 (Fig. 3f, g, Supplementary Fig. 3c, and
Supplementary Data 4, 5). Although clusters 6 and 7 were present in all 4
organs, cluster 7 was similar to the WKM clusters 1 and 2, while cluster 6
displayed a pro-inﬂammatory and phagocytic gene program. This suggests
that cluster 6 is the resident macrophage population within each organ, and
cluster 7 consists of circulating mono/Mϕ.

To aid in assessing the identities of these macrophage subtypes, we
analyzed the expression of known zebraﬁsh macrophage subset markers.
mpeg1.1 was widely used as a pan-macrophage marker; however, it does not
label the entire mono/Mϕ population. Broad expression in B cells was also
observed (Supplementary Fig. 3d, e). These observations match recent
reports of mpeg1.1- macrophages and mpeg1.1+ B cells in zebraﬁsh32,57. By
contrast, c1q genes were mostly restricted to the mono/Mϕ population and

expressed in all mono/Mϕ 7 clusters

broadly
(Supplementary
Figs. 2c and 3e), indicating higher speciﬁcity than mpeg1.1. Macrophages are
traditionally classiﬁed as pro-inﬂammatory M1 macrophages and anti-
inﬂammatory M2 populations. Notable zebraﬁsh M1 markers include tnfa,
tnfb, il1b, il6 and cxcl11.154,55. As shown in Supplementary Fig. 3d–f, tnfa,
tnfb and cxcl11.1 were preferentially expressed in clusters 3 and 6, in
addition to having lower expression in small fractions of clusters 4 and 7. il1b
was expressed by <20% of cells in clusters 3, 5, 6, and 7, and il6 was barely
detected in clusters 4, 5, 6, and 7. These expression patterns suggest an M1
identity for clusters 3, 6, and 7. However, zebraﬁsh M2 markers mrc1b and
cxcr4b were broadly expressed in all clusters except cluster 5, overlapping
with the expression of M1 markers (Supplementary Fig. 3d, e)54,55,58. Other
M2 genes tgfb1a and ccr2 were enriched in some cluster 4 cells in addition to
a lower expression in clusters 3 and 654,55. These observations suggest that
cells in clusters 3, 4, and 6 may have both pro- and anti-inﬂammatory
function. Previous studies found that the Tgfβ signaling is required for
zebraﬁsh heart regeneration56,59. This ﬁnding and our results suggest an anti-
inﬂammatory M2 feature of cluster 4.

To better understand the functions of these subclusters in the injured
heart, we performed hybridization chain reaction (HCR) staining for a few
cluster markers on heart cryosections at 1 and 7 dpci, together with antibody
staining against the pan-leukocyte marker L-plastin (i.e., lymphocyte cytosolic
protein 1, lcp1)60,61. As shown in Fig. 3h, expression of the cluster 4 marker gda
was enriched in macrophages in the boundary zone of the wound at 1 dpci but
not detected in the uninjured control. By contrast, the cluster 1, 2, and 7
enriched moxd1 was mostly on the ventricular surface of the wound (Fig. 3h).
By 7 dpci, the number of gda+lcp1+ cells in the wound was largely reduced
(Fig. 3i, j), which match the scRNA-seq analysis result (Fig. 3e). In addition, the
cluster 3, 4, and 6 enriched havcr1 was expressed in mono/Mϕ both in the
boundary zone and ventricular wall at 1 dpci, with some overlap with moxd1
expression on the ventricular surface (Fig. 3k). These expression patterns
suggest that cluster 4 contains boundary zone macrophages while clusters 1, 2,
3, 6, and 7 are mostly on the ventricular surface. In summary, our results
revealed the dynamic heterogeneity of zebraﬁsh mono/Mϕ during heart
regeneration and that the boundary zone, phagocytotic, fn1a+tgfb1a+ cluster 4
macrophages may support regeneration29,56,59.

Interspecies similarities and differences in mono/Mϕ subsets
Given that the immune system plays a critical role in determining the
outcome of the cardiac and systemic reaction to myocardial injury, we
sought to compare and contrast the immune response between mouse and
zebraﬁsh. We focused our analyses on the monocytes and macrophages,
which were amongst the cells with the greatest number of DEGs in response
to heart injury in both species (Fig. 1e, f). Integration of 6 macrophages
subtypes from mice (mm1–mm6) and 7 from zebraﬁsh (dr1–dr7) was
performed by sequence homology analysis to identify the commonly
expressed genes and generate a joint manifold representation using the
SAMap algorithm (Fig. 4a–c). We found 3 macrophage cluster pairs with
high inter-species alignment scores: mm1-dr4, mm4-dr6, and mm6-dr3
(Fig. 4d). mm1-dr4 are injury-responsive mono/Mϕ that are robustly
increased in the heart following myocardial injury. The mm4-dr6 pair
represents tissue resident macrophages that are present in the heart and

Communications Biology |

 (2024) 7:1611

7

https://doi.org/10.1038/s42003-024-07315-x

Article

Fig. 4 | Interspecies similarities and differences in mono/Mϕ subsets. UMAPs of
mono/Mϕ from the mouse (37,215 cells) and zebraﬁsh (10,709 cells) plotted as total
(a), zebraﬁsh (b) and murine (c) clusters. d SAMap alignment of the mouse (mm)
and zebraﬁsh (dr) mono/Mϕ subclusters. Edges with alignment scores less than 0.2
were omitted. The connections between the subclusters are colored by alignment

score. Shared enriched biological process terms (GO-BP) between mm1-dr4 (e),
mm4-dr6 (f), and mm6-dr3 (g) clusters based on subcluster markers for each species
(mean AUC > 0.6). Only terms with an adjusted p < 0.05 in both species were
included.

Communications Biology |

 (2024) 7:1611

8

https://doi.org/10.1038/s42003-024-07315-x

Article

other organs examined while the mm6-dr3 mono/Mϕ pair was mostly
found in the blood in mice and the whole pancreas in zebraﬁsh. Two
zebraﬁsh clusters (dr5 and dr7) did not show signiﬁcant similarity to any
mouse mono/Mϕ cluster while mouse cluster mm5 did not align with
zebraﬁsh. To understand the similarities between these analogous clusters,
we assessed the marker genes for each cluster and performed GO biological
process (BP) enrichment analysis. Leukocyte migration, pyruvate metabo-
lism, vesicle organization, hypoxia, and autophagy were among the top
shared overrepresented pathways for mm1 and dr4 mono/Mϕ subclusters
(Fig. 4e and Supplementary Data 6). The mm4-dr6 pair had the highest
number of top shared overrepresented pathways, which include the com-
plement pathway, humoral
junction disassembly, and
immunity, cell
synapse formation (Fig. 4f). mm6-dr3 had the fewest shared pathways that
contained neutrophil degranulation, immune regulation, and antigen pre-
sentation (Fig. 4g). Collectively, these analyses suggest that there are ana-
logous mono/Mϕ clusters between mouse and zebraﬁsh that may share
similar functions. In addition to the transcriptional differences in the ana-
logous mono/Mϕ clusters, there were mono/Mϕ clusters distinct to each
species.

Differential transcriptional response to cardiac injury in analo-
gous cardiac mono/Mϕ subsets between ﬁbrotic and
regenerative models
To examine shared and divergent species transcriptional responses to
myocardial injury in the mono/Mϕ cluster pairs, we next focused on the
heart where macrophages and inﬁltrating monocytes are abundant and
important in tissue repair as well as the blood, which is an indicator of the
systemic inﬂammatory response and an important source of inﬁltrating
monocytes. We assessed transcriptional changes induced by myocardial
injury (fold change compared to control) in mono/Mϕ pairs in tissues and
timepoints where they are jointly found: mm1-dr4 and mm4-dr6 at days 1
and 7 in the heart (Fig. 5 and Supplementary Fig. 5a, b). Focusing solely on
the ortholog genes between the two species, the number of genes that were
concordantly upregulated or downregulated in the mono/Mϕ cluster pairs
was very small compared to those genes that were discordantly transcribed
in response to myocardial injury (Fig. 5a, c, e, g, and Supplementary Data 7).
In the heart, both mm1-dr4 and mm4-dr6 had >3 times more DEGs at
day 1 compared to 7. GO terms enrichment analysis of DEGs in the heart at
day 1 for mm1-dr4 revealed that genes upregulated in both species were in
the BP of negative regulation of cell adhesion (Supplementary Fig. 5a, b). In
contrast, BP terms overrepresented in zebraﬁsh but not in mouse were
related to plasma membrane homeostasis, lysosome and lipid catabolism,
and cell-matrix adhesion (Fig. 5b and Supplementary Data 8). Gene path-
ways that were overrepresented in mm1 but not in dr4 with injury at day 1
were ribosome biogenesis and ATP/aerobic metabolism. At day 7, the dr4
mono/Mϕ displayed high transcriptional response to stress, wound healing,
and phosphatidylinositol-mediated signaling whereas apoptosis and
response to toxic substances were found upregulated in mm1 cells (Fig. 5d).
Comparing the cells in the mm4-dr6 cluster in the heart, there was a large
discordant transcriptional response induced with injury at day 1 (336 genes
in mouse; 208 genes in zebraﬁsh; 15 genes concordant) that was dramati-
cally reduced by day 7 (35 genes in mouse; 57 genes in zebraﬁsh; 0 genes
concordant) (Fig. 5e, g). At 1 day of injury, the concordant genes signaled BP
involved in ATP metabolism, nucleotide biosynthesis, and regulation of
actin ﬁlament (Supplementary Fig. 5b). The overrepresented BP in mm4 but
not dr6 were categorized by translation, protein localization, and immune
cell cytotoxicity, all of which suggest robust cellular activation (Fig. 5f). In
contrast, dr6 cells were enriched in chromatin modiﬁcation, B cell differ-
entiation, and cellular insulin signaling processes. At day 7, mm4 injury
response genes were enriched in integrin-mediated signaling, protein pro-
cessing, and cytokine processes (Fig. 5h), while dr6 cells showed enrichment
in angiogenesis, type 2 immune response and ﬁbroblast growth factor
production. Our analysis suggests that the initial transcriptional response to
injury in analogous heart macrophages was likely highly discrepant with
minimal conserved pathways between mice and zebraﬁsh.

Cardiac macrophage response to heart injury by mono/Mϕ
clusters in mice and zebraﬁsh
The inter-species differences in the monocyte and macrophage response to
heart injury observed by scRNA-Seq was striking. We sought to use an
orthogonal system for validation that does not require lysing the cells for
analysis and that can be assessed by other labs in their models. In the mouse
mono/Mϕ subclusters, we identiﬁed and plotted marker genes that are
commonly used for ﬂow cytometry analysis to characterize macrophages.
We plotted mono/Mϕ lineage and subtype genes for cardiac macrophages at
1 dpi for the mouse clusters (1–4) present in the heart (Supplementary
Fig. 5c). H2-Aa was highest in mm2 cells while Ly6c2 and Mrc1 were most
abundantly expressed in mm3 and mm4 cells, respectively. Flow cytometry
of digested cardiac cells allowed us to distinguish macrophage subsets based
on cell surface protein expression of these macrophage genes (Supple-
mentary Fig. 5d). Mice with sham and MI at 1 dpi had different proportions
and numbers of cardiac macrophage subsets, corroborating the scRNA-Seq
analyses (Figs. 2f and 6a, Supplementary Figs. 4b and 5e). At 1 dpi, there was
~5-fold increase in the number of cardiac mono/Mϕ in the MI group
compared to controls (Supplementary Fig. 5e). CD206−Ly6chi cells (pre-
dicted to be mm3) and CD206−Ly6clo (predicted mm1) were up >10 and ~8-
fold, respectively with MI (Fig. 6a). CD206+ macrophages (predicted mm4)
were modestly increased two fold with MI compared to sham (Fig. 6a). This
further permitted us to use ﬂuorescent activated cell sorting (FACS) to
enrich for mm1 cells (Supplementary Fig. 5d, f, and Fig. 6a) and assess
transcriptional responses to MI within the different cardiac macrophage
subsets (Fig. 6b, c). In CD206−Ly6clo macrophages, Fth1 was increased >5
fold in the MI group compared to sham (Fig. 6b). However, genes such as
Ahnak, Gda, and Psap that were induced at 1 dpci in the zebraﬁsh dr4
macrophage subset were not changed or downregulated in the case of Psap
with MI in CD206−Ly6clo mouse cardiac macrophages (Fig. 6b, d). Mean-
while, CD206+ heart mono/Mϕ (mm4 cluster) showed threefold upregu-
lation in Ccl2, validating data from scRNA-Seq analyses (Fig. 6c). We
performed HCR staining of cd9b and fn1a on zebraﬁsh heart sections
(Fig. 6e). These two genes were induced in mono/Mϕ around the injury site
at 1 dpci but were not detectable in the absence of heart injury. Similarly, the
zebraﬁsh cluster dr4 speciﬁc gda was also highly induced by injury at 1 dpci
(Fig. 3h). Thus, while cd9b (Cd9 in mice) was likely upregulated in both
species, inductions of gda and fn1a in macrophages were presumably zeb-
raﬁsh speciﬁc. Overall, these results suggest both shared and distinct
immune responses between regenerative and proﬁbrotic myocardial injury
models.

Chronic systemic and peripheral inﬂammation in response to
heart injury in mouse but not zebraﬁsh
Dissecting the long-term inﬂammatory impacts of MI systemically and in
extracardiac organs was a focus of this study. The murine blood mono/
Mϕ response compared to the zebraﬁsh WKM mono/Mϕ response was
strikingly different with heart injury (Fig. 7a and Supplementary Data 9).
In mice, there were some shared GO-BP terms such as leukocyte adhesion
and mono/Mϕ activation that spanned across the timepoints. Carbohy-
drate catabolic process at day 7 was the only shared enriched GO-BP term
across species, revealing largely distinct activation with heart injury in
mice and zebraﬁsh. At 30 dpi in mice, the blood mono/Mϕ continued to
evolve with a transcriptional program depicting immune activation
(migration, antigen processing, and presentation, and lymphocyte
immunity). Similar immune activation patterns were observed in mouse T
and B cells that were distinct from zebraﬁsh (Supplementary Fig. 6a, b and
Supplementary Data 9). Within the mono/Mϕ subpopulations in mice,
there was a larger representation of cluster 2 in blood (23% sham vs 40%
MI), suggesting these cells could be driving the MI-derived persistent
inﬂammation (Fig. 2f). Cluster 2 blood monocytes in the MI group were
enriched in complement, ID1 signaling, neutrophil activation, and mac-
rophage alternative activation pathways compared to sham controls,
suggesting immune activation of this subset with chronic MI (Supple-
mentary Fig. 6c and Supplementary Data 3).

Communications Biology |

 (2024) 7:1611

9

https://doi.org/10.1038/s42003-024-07315-x

Article

Hepatic mono/Mϕ in both mouse and zebraﬁsh likely underwent a
dynamic and drastic transcriptional shift with evolution of heart injury
(Fig. 7b). In mice, metabolic and death pathways were upregulated early
while complement, lipid, and cytokine pathways were enriched at 30 dpi
(Fig. 7b and Supplementary Data 9). In contrast, zebraﬁsh liver mono/Mϕ
cells displayed robust immune cell activation and cardiac differentiation

pathways at 1 dpci before shifting to ERK1/ERK2, cholesterol, and estrogen
pathways at 7 dpci with cardiac injury. The dynamic change in cytokines
from day 1 to 30 in the mouse liver was independently validated by qPCR
(Fig. 7c). The mice with chronic MI also displayed histological signs of liver
damage consistent with chronic heart failure (Fig. 7d) and importantly a >2-
fold increase in the number of macrophages with MI compared to sham,

Communications Biology |

 (2024) 7:1611

10

https://doi.org/10.1038/s42003-024-07315-x

Article

Fig. 5 | Differential transcriptional response to cardiac injury in mono/Mϕ
subsets between species. a Scatterplot of the fold changes in murine and zebraﬁsh
genes with cardiac injury compared to control in mm1 and dr4 cells at 1 dpi
(FDR < 0.10 and |log2FC| > 0.25). b Enriched biological process terms of the dif-
ferentially expressed genes (DEGs) that are discordant between mm1 and dr4 cells in
(a). c Scatterplot of the fold changes in murine and zebraﬁsh genes with cardiac
injury compared to control in mm1 and dr4 cells at 7 dpi (FDR < 0.10 and |
log2FC| > 0.25). d Enriched biological process terms of the DEGs that are discordant
between mm1 and dr4 cells in (c). e Scatterplot of the fold changes in murine and
zebraﬁsh genes with cardiac injury compared to control in mm4 and dr6 cells at 1 dpi

(FDR < 0.10 and |log2FC| >0.25). f Enriched biological process terms of the DEGs
that are discordant between mm1 and dr4 cells in (e). g Scatterplot of the fold
changes in murine and zebraﬁsh genes with cardiac injury compared to control in
mm4 and dr6 cells at 7 dpi (FDR < 0.10 and |log2FC| >0.25). h Enriched biological
process terms of the DEGs discordant between mm1 and dr4 cells in g. In (a), (c), (e),
and (g), concordant genes with FDR < 0.10 and |log2FC| > 0.25 in both species were
colored blue when downregulated and green when upregulated. Discordant genes
with FDR < 0.10 and |log2FC| > 0.25 in one specie were colored red when upregu-
lated in zebraﬁsh and yellow when upregulated in mouse. In (b), (d), (f), and (h),
pathways with a -log10(p-value) >1.3 were considered signiﬁcantly enriched.

Fig. 6 | Cardiac macrophage response to heart injury by mono/Mϕ clusters in
mouse and zebraﬁsh. a Enumeration of LV macrophages expressing CD206 and
Ly6c as determined by ﬂow cytometry in mice undergoing MI or sham at 1 dpi.
n = 14SH/11MI (males), 4SH/4MI (females). b Gene expression analyses of
Ly6cloCD206− FAC-sorted cardiac macrophages from sham or MI at 1 dpi. n = 3SH/
6MI (males), 2SH/1MI (females). c Gene expression analysis of CD206+ FAC-sorted
murine cardiac macrophages from sham or MI at 1 dpi. n = 5SH/6MI (males), 4SH/
2MI (females). a–c Mean ± S.E.M. Two-tailed Student’s t-test. d Violin plots of

indicated genes in zebraﬁsh cluster dr4 across timepoints. e Images of zebraﬁsh heart
cryosection showing HCR staining signals of cd9b and fn1a at 1 dpci in green and
magenta, respectively. No expression was detected in the uninjured sample (Ctrl, left
panel). Anti-lcp1 staining is shown in blue. DAPI staining is shown in white. The
framed region is enlarged to show details on the right with different channel com-
binations. Arrowheads indicate representative cd9b+fn1a+lcp1+ cells. Scale
bar, 100 μm.

validating the scRNA-Seq data (Fig. 7e, f). By contrast, the zebraﬁsh liver
showed comparable number of isolectin B4 (IB4)+ macrophages27,62,63
between the 30 dpci and uninjured samples (Fig. 7g, h). Cluster 3 and 4
mono/Mϕ cells were the predominant mono/Mϕ found in the mouse liver
at 30 dpi with cluster 3 virtually only present in the MI group (Fig. 2f and
Supplementary Fig. 4b). In cluster 4, MI induced a gene expression program
enriched in inﬂammation (acute phase response, production of NO and
ROS, IL-12 signaling, coronavirus pathogenesis and PD-1) while the LXR/
RXR pathway showed inhibition (Supplementary Fig. 7a, b and Supple-
mentary Data 3). Altogether, our data suggest altered liver macrophage
composition and gene expression changes signaling increased inﬂammation

and tissue damage in mice with MI are not observed in zebraﬁsh after
cardiac injury.

Transcriptional perturbations in the liver after cardiac injury in
mice but not zebraﬁsh
Macrophage accumulation in the mouse liver and the high number of DEGs
in hepatocytes after chronic MI suggested hepatic dysfunction. We used
SAMap to delineate the hepatocyte response to cardiac injury between spe-
cies. The mouse hepatocytes that underwent sham surgery at 1 and 7 dpi were
most similar to zebraﬁsh hepatocytes at 1 and 7 dpci while those from mouse
sham at 30 dpi aligned with uninjured zebraﬁsh hepatocytes (Fig. 8a). In

Communications Biology |

 (2024) 7:1611

11

https://doi.org/10.1038/s42003-024-07315-x

Article

Fig. 7 | Chronic systemic and peripheral inﬂammation in response to heart
injury in mouse but not zebraﬁsh. Enriched biological process terms for mouse
blood monocytes and zebraﬁsh WKM (whole kidney marrow) monocytes (a) and
liver macrophages (b) (mean AUC > 0.6, numbers in parenthesis below each col-
umn indicate number of upregulated genes). The gene ratio is indicated by the dot
size and the signiﬁcance by the color of the dot (P < 0.05). mm, mouse; dr, zebraﬁsh.
c qPCR expression of liver samples from mice with MI or sham (SH) at 1 and 30 dpi.
1 dpi: n = 5SH/7MI, 30 dpi: n = 18SH/10MI. Dots represent individual mice.
Mean ± S.E.M. Two-way ANOVA. d Representative liver sections stained by H&E

(n = 3/group). Scale bar is 50 µm. Arrowhead indicates liver damage. e Mac2
immunohistochemistry in the liver (n = 5SH/4MI). Representative pictures are
shown. Scale bar is 50 µm. f Quantiﬁcation of Mac2+ liver macrophages in (e).
n = 5SH/4MI male mice. Dots represent individual mice. Mean ± S.E.M. Two-tailed
Student’s t-test. g Section images of zebraﬁsh liver showing staining against IB4
(green). DAPI staining is shown in blue. Livers were collected at 30 dpci of heart
injury together with the uninjured ﬁsh. Arrowheads indicate IB4+ cells. Scale bar,
100 μm. h Quantiﬁcation of IB4+ macrophages in (g). n = 6 for each group.
Mean ± S.D. Two-tailed Student’s t-test.

contrast, the mouse hepatocytes from MI at 7 dpi weakly corresponded to
zebraﬁsh 1 and 7 dpci (Fig. 8a). At 1 dpi, enriched pathways in murine
hepatocytes with MI included wound healing, fat cell differentiation, and
triglyceride and ribonucleotide metabolism while at 7 dpi ribosome biogen-
esis, ﬁbrinolysis and hemostasis were present (Fig. 8b, Supplementary Fig. 7c,
and Supplementary Data 9). On the other hand, the zebraﬁsh response was
more homogeneous over time, with enriched terms relating to humoral
immune response and cholesterol transport at 1 and 7 dpci (Fig. 8b, Sup-
plementary Fig. 7c and Supplementary Data 9). Between mouse and zebraﬁsh
there were relatively few shared pathways such as ER stress, negative reg-
ulation of hydrolase activity, and humoral immune response (Fig. 8b). Col-
lectively, these data suggest that the hepatic response to heart injury in
zebraﬁsh is a systemic stress response resembling that of the control mice.
To gain further molecular insight into how hepatocytes between the
two species respond to cardiac injury, we assessed the ortholog gene

response and pathways to heart injury (Fig. 8c–f). At 1 and 7 days, there were
293 and 201 genes, respectively that were discordant between mouse and
zebraﬁsh while only 27 and 19 genes were concordant at the corresponding
timepoints (Fig. 8c, e and Supplementary Data 10). At 1 dpci, zebraﬁsh
hepatocytes had preferential enrichment in cholesterol biosynthetic process
whereas murine hepatocytes were enriched in energetic pathways at 1 dpi
(Fig. 8d, Supplementary Fig. 7d, and Supplementary Data 11). At 7 dpci,
zebraﬁsh hepatocytes were largely enriched in fatty acid metabolism and
glycolytic pathways while murine hepatocytes showed upregulation of
antigen processing and presentation and ribosome/translation pathways
(Fig. 8f, Supplementary Fig. 7e, and Supplementary Data 11). With chronic
heart failure in mice at 30 dpi, the hepatocyte response to MI continued to
evolve with none of the top pathways overlapping with prior mice or zeb-
raﬁsh at 1 or 7 dpi. The top terms upregulated in hepatocytes related to tissue
remodeling (wound healing, cell migration, epithelial cell proliferation),

Communications Biology |

 (2024) 7:1611

12

https://doi.org/10.1038/s42003-024-07315-x

Article

Fig. 8 | Hepatic outcomes after cardiac injury in mice and zebraﬁsh. a SAMap
alignment of the mouse (mm) and zebraﬁsh (dr) hepatocyte scRNA-seq samples.
Edges with alignment scores less than 0.2 were omitted. The connections between
the samples are colored by alignment score. b Enriched biological process terms for
mouse and zebraﬁsh hepatocytes (mean AUC > 0.6). The gene ratio is indicated by
the dot size and the signiﬁcance by the color of the dot (p < 0.05). c Scatterplot of the
fold changes in murine and zebraﬁsh genes with cardiac injury compared to control
in hepatocytes at 1 dpi (FDR < 0.10 and |log2FC| > 0.25). d Enriched biological
process terms of the DEGs that are discordant between mouse and zebraﬁsh

hepatocytes in (c). e Scatterplot of the fold changes in murine and zebraﬁsh genes
with cardiac injury compared to control in hepatocytes at 7 dpi (FDR < 0.10 and |
log2FC| > 0.25). f Enriched biological process terms of the DEGs that are discordant
between mouse and zebraﬁsh hepatocytes in (e). In (c) and (e), concordant genes
(FDR < 0.10 and |log2FC| > 0.25) in both species were colored blue when down-
regulated and green when upregulated. Discordant genes (FDR < 0.10 and |
log2FC| > 0.25) between species were colored red when upregulated in zebraﬁsh and
yellow when upregulated in mouse. In (d) and (f), GO terms with a -log10(p-value)
>1.3 were considered signiﬁcantly enriched. mm=mouse; dr=zebraﬁsh.

response to metal ion, and receptor-mediated endocytosis (Fig. 8b and
Supplementary Fig. 7c). Downregulated terms at 30 dpi included metabolic
changes in small molecule, fatty acid, amino acid, and steroid metabolism,
which were orthogonally validated by qPCR in separate cohorts of mice
(Supplementary Fig. 8a–c and Supplementary Data 9). In summary, these
discrepant responses between mouse and zebraﬁsh hepatocytes in metabolic
activities and immune activation are associated with cardiac regenerative
and ﬁbrotic effects on the liver, respectively. Similarly, mouse kidney epi-
thelial cells in the MI group also showed potential signs of organ stress
(Supplementary Fig. 9a and Supplementary Data 3), highlighting the long-
term effects of MI on extracardiac organs.

Discussion
Our study provides a direct cross-species comparison of immune responses
between regenerative and proﬁbrotic myocardial injury models across
several tissues that can serve as a useful resource to the ﬁelds of regenerative

biology and cardiovascular research. We proﬁled immune cells in multiple
extracardiac organs by scRNA-Seq after cardiac necrosis in mice and zeb-
raﬁsh. We observe dramatic plasticity in the dynamic immune response that
was not limited to the heart. Persistent inﬂammatory changes, especially in
macrophages, are noted in extracardiac organs and blood monocytes.
Macrophages are critical for heart repair after injury32,64 and we indeed ﬁnd
multiple subtypes of macrophages in mice and zebraﬁsh. To our surprise,
most of the mono/Mϕ subclusters from zebraﬁsh align to a subcluster in
mouse. This permitted us to study analogous pairs of macrophages across
species. The cross-species comparison is based on sequence homology
between genes with projection of expression proﬁle to a common lower
dimension embedding65. Although functional similarity implied by the
sequence homology is a reasonable assumption, it is possible that not all
functional similarities are captured in this approach; and conversely that the
aligned zebraﬁsh-mouse macrophage subtypes may not function in a
similar way. Notwithstanding these limitations in both species there are

Communications Biology |

 (2024) 7:1611

13

https://doi.org/10.1038/s42003-024-07315-x

Article

noticeable changes in macrophage populations in response to MI. Our
results show that at 1 dpi, the transcriptional response in the analogous
macrophage pairs was dramatically different. The vast majority of DEGs
were discordant and generally <10 were concordant. We also ﬁnd striking
differences in metabolic pathways (ATP, oxidative phosphorylation, gly-
colysis, cholesterol, fatty acids) induced by heart injury between species in
the macrophages. Tian and colleagues previously demonstrated that mac-
rophage loss of mitochondrial complex I results in impaired cardiac
healing66. Our data provides additional context for macrophage metabolism
playing a role in cardiac regeneration versus ﬁbrosis with metabolic path-
ways that will need to be tested67. It is interesting to note that while zebraﬁsh
and mouse share signiﬁcant macrophage signatures,
their disparate
responses to MI may be key to the different ﬁbrotic and healing outcomes
between the species. What fundamentally determines the dichotomous
macrophage responses to cardiac injury remains to be determined but could
include factors extrinsic to the macrophage. Our data also reveal that zeb-
raﬁsh possess a dr7 macrophage subtype not present in mouse, which may
play an important role in regeneration. Currently, it is unknown if the
different reactions to myocardial injury, the presence of unique regenerative
macrophage subclusters in zebraﬁsh or inhibitory macrophage clusters in
mouse, or a combination thereof might be responsible for differences in
cardiac healing. The answers to these questions will require gain and loss of
function studies to speciﬁcally modulate macrophages in vivo and test for
their ability to impact heart regeneration. How the adult mouse and zeb-
raﬁsh macrophage subclusters compare to neonatal mouse macrophages is
another open question fertile for future research.

We identify 6 subsets of murine macrophages in our study across
tissues that are dynamically regulated with MI. mm4 macrophages are tissue
resident macrophages that express Timd4, Lyve1, and Folr2 (TLF+) that
closely resemble the subset previously characterized by Epelman and
colleagues53. Runx1 and Trem2 are 2 macrophage markers that have been
linked to cardiac recovery17,68. Across our 6 mouse macrophage clusters, we
observe similar expression of these 2 factors at the mRNA level without one
or two clear clusters having higher levels of Runx1 or Trem2 in the heart
before or after MI. Cochain and colleagues integrated scRNA-Seq datasets of
cardiac macrophages in experimental murine MI and found increases in
Isg15hi, Trem2hiSpp1hi, and Trem2hiGdf15hi monocytes days after MI69. Our
results also indicate a rise in Isg15, predominantly within clusters 2 and 3
heart macrophages at 7 dpi whereas Spp1 is highly expressed in cluster 1
heart macrophages. We do not detect signiﬁcant expression of Gdf15 within
any of the cardiac macrophage clusters at any timepoint post-MI, which
may reﬂect sensitivity or differences in thresholds for determination. The
ontogeny of cardiac macrophages is known to be different between neonatal
and adult mice at baseline and with injury70. Olson and colleagues identiﬁed
5 subpopulations of cardiac monocytes/macrophages in neonatal mice with
regenerative capacity by scRNA-Seq71. Based on select markers published in
that study, the “M2”, “DC-like”, and “M1 Mo” neonatal subpopulations
most closely resemble our C1, C2, and C3 clusters in adult mice, respectively.
There are limitations to using a few marker genes for comparison and
functional studies would ultimately be needed to ascribe the role of mac-
rophage subsets in cardiac regeneration.

Other groups have previously studied macrophages in non-cardiac
tissues after MI. Nahrendorf and colleagues proﬁled macrophage subtypes
in multiple organs mostly by ﬂow cytometry and targeted gene expression72.
Their general ﬁnding was that tissue macrophages in distal organs were
affected by the primary injury, similar to what we ﬁnd with scRNA-Seq
analyses. The Dimmeler lab used scRNA-Seq to study the effects of post-MI
heart failure on the bone marrow and found increased inﬂammation with
MI73. Similar to our mouse analyses, scRNA-Seq of peripheral blood
mononuclear cells from humans suffering an acute ST-segment–elevated
myocardial infarction (STEMI) reveal large transcriptional perturbations
early on that decrease over time, though blood monocytes have the largest
number of DEGs 6–8 weeks post STEMI74. Of note, human STEMI is similar
to the mouse model of permanent coronary artery ligation we use here.
Likewise, scRNA-Seq of blood monocytes in humans with chronic heart

failure also demonstrate higher counts of monocytes in a small group of
patients with heart failure75. Overall, there is now clear evidence that MI and
CHF perturb mono/Mϕ function that can have deleterious effects on
extracardiac tissues in mammals. This study cannot determine the extent to
which acute heart injury or chronic LV systolic heart failure contributes to
the peripheral inﬂammation seen in mice but not zebraﬁsh15. The datasets
provided here are designed to serve as a resource for the ﬁeld and hypothesis
generating. Future studies to examine how macrophages post-MI might
contribute to chronic liver and kidney injury will be valuable and can inform
of new therapeutic targets for extracardiac complications of MI.

Moreover, speciﬁc macrophage reporters in zebraﬁsh have yet to be
developed, and c1q genes are ideal candidates because of their high speci-
ﬁcity and broad expression in all mono/Mϕ subtypes. Our results suggest
mixed M1 and M2 features in zebraﬁsh mono/Mϕ clusters. It is possible that
there is further heterogeneity within our deﬁned mono/Mϕ clusters that are
associated with pro-inﬂammatory, anti-inﬂammatory, or other functions. It
is also worth noting that macrophages expressing the classic M1 marker tnfa
were reported to be pro-regenerative in zebraﬁsh spinal cord regeneration76.
Thus, the traditional M1/M2 classiﬁcation may not be applicable in deter-
mining regenerative capacity. Here we identiﬁed an acute inﬂammatory
stage (i.e., 1 dpci) enriched macrophage cluster 4 expressing phagocytic and
pro-regenerative genes (e.g., fn1a and tgfb1a), suggesting a pro-regenerative
potential in zebraﬁsh29,56,59. These dr4 cluster macrophages represent a new
source of Tgfb1a and Fn1a, factors reported to contribute to heart
regeneration56,59,77. This further supports the notion that a pro-regenerative
decision is made early in the acute stage upon heart injury. How this
transient macrophage population interacts with other cardiac cell types and
may trigger a potential regenerative program warrants further investigation.
One important limitation of our study is that our mouse scRNA-Seq
samples came from one sample that was mostly pooled from two tissue
donors while our zebraﬁsh scRNA-Seq came from two biological replicates.
The effect this has is to bias towards the mean for the group. There thus may
be heterogeneity in the heart injury response between different mice or
zebraﬁsh that is not captured in the scRNA-Seq analyses. We validated key
ﬁndings
such as monocyte/macrophage ﬁndings using orthogonal
approaches in the heart and liver in separate cohorts of mice. However, this
validation was not possible for all of the different tissues and timepoints
analyzed in our study. Future studies are needed to more precisely deter-
mine the extent of heterogeneity in the immune response to cardiac injury in
certain organs such as the kidney and liver. As this project focused on
inﬂammation, cell isolation and scRNA-Seq protocols were adapted for
immune cells. Many hepatocytes, kidney epithelial cells, and pancreatic islet
cells were sequenced. However, there were relatively few cardiomyocytes
sequenced due to their size. In general, we ﬁnd evidence of peripheral organ
dysfunction in the liver and kidney but not in the pancreatic islets in mice.
Another limitation of our study is that this does not permit robust in silico
assessment of ligand-receptor or cell-cell interactions. Although we observe
many of the mono/Mϕ clusters across different timepoints and organs, we
do not formally know if they represent deﬁnitive ﬁxed cell subtypes or
activation states. It is possible that there is some degree of plasticity observed
within a cell cluster or between clusters. Lineage tracing experiments will be
needed in the future to answer this. Moreover, functional validation of the
shared and distinct mono/Mϕ clusters between species needs to be rigor-
ously performed to demonstrate their potential contributions to regenera-
tion. Future experiments to determine how the macrophage subclusters
respond to injury at later timepoints such as 7 and 30 dpi in mice and
zebraﬁsh will be of considerable interest. In summary, our results provide
new insights into manipulating immunomodulators for cardiac repair.

Materials and methods
Mouse maintenance
Animal procedures were performed according to approved protocols by the
Institutional Animal Care and Use Committee (IACUC) at Weill Cornell
Medical College. We have complied with all relevant ethical regulations for
animal use. C57BL/6J (Stock #000664) male and female mice were

Communications Biology |

 (2024) 7:1611

14

https://doi.org/10.1038/s42003-024-07315-x

Article

purchased from Jackson Laboratories and maintained in Thoren cages
under a 12/12-h light/dark cycle at constant temperature (22 °C) with free
access to water and food. Mice were bred in our animal facility to maintain a
colony.

Mouse LAD ligation procedure
10–12 weeks old male and female C57BL/6J mice were subjected to LAD
ligation or sham surgery78. scRNA-Seq analysis was performed on male
mice with other experimental analyses consisting of mice of both sexes.
Brieﬂy, mice were anesthetized with isoﬂurane and then orally intubated
and connected to a ventilator (Hugo Sachs MiniVent type 845) for
mechanical ventilation. The left pectoralis major muscle was bluntly dis-
sociated until the ribs were exposed. The muscle layers were pulled aside and
ﬁxed with an eyelid-retractor. Left thoracotomy was performed between the
third and fourth ribs to visualize the anterior surface of the heart and left
lung. The pericardium was removed and the proximal segment of the left
coronary artery ligated with a 7-0 Ethilon nylon suture (Ethicon). In sham
surgeries, the suture step was skipped. The rib cage was closed with Vicryl
(Ethicon) stitches on the 3rd and 4th ribs and the skin closed with wound
clips. Postoperative analgesia consisted of meloxicam (2 mg/kg) and
buprenorphine (0.5 mg/kg). The mice were extubated when spontaneous
breathing was observed. The animals were kept in a warm cage until
recovery.

Echocardiography
Cardiac morphology and function were evaluated using an ultrasound
imaging system Vevo 3100 with the MX400 transducer (VisualSonics).
Mice were scanned 7 or 30 dpi under light isoﬂurane (1.5%) anesthesia
within 20–30 min. Mouse body temperature was maintained using a heated
platform. LVEF was measured.

Venipuncture mouse blood collection
For blood cytometry analyses, mouse blood was collected from the tail vein
as follows. A small puncture was introduced into the vein with a scalpel.
Droplets of blood were collected with a lithium heparin Microvette CB300
(Sarstedt).

Mouse tissues single cell isolation
Whole blood was collected by cardiac puncture. Red blood cells were lysed
with ACK (Ammonium–chloride–potassium) lysis buffer and removed by
density centrifugation on a 5% BSA cushion (230 × g for 5 min at 4 °C). Cells
were strained with a 40 µm sieve.

Kidney cells were isolated as described in Barry et al.79 with modiﬁca-
tions: animals were perfused with ice-cold PBS-5mM EDTA through the left
ventricle, then kidneys were collected, decapsulated, and minced with a razor
blade. Tissue fragments were digested in HBBS 0.15 mg/ml Liberase TM
(Sigma) for 25 min at 37 °C with vigorous agitation. Digestion was stopped
with ice-cold FBS. The digestion mix was passed through a 70 µm cell strainer
and spun down for 5 min at 300 g (4 °C). The pellet was spun down on a 7.5%
BSA cushion, for 4 min at 230 g (4 °C) twice to clear debris.

For heart, non-myocyte cells, hearts were perfused by the standard
Langendorff method and cells obtained by enzymatic dissociation, as
described in Cerrone et al.80 with minor changes. Brieﬂy, mice were injected
with 0.1 ml heparin (500 IU/ml i.p.) 20 min. before heart excision, and
anesthetized with ketamine/xylazine (100 mg of ketamine/kg of body
weight and 10 mg of xylazine/kg). Hearts were excised and placed in a
Langendorff column. The digestion buffer consisted of 0.15 mg/ml Liberase
TM (Sigma), ﬂowing at 3 ml/min and 37 °C, for 10 min. Then the LV of
sham-operated animals or the infarcted area of the LV of infarcted hearts
was dissected and triturated with a plastic Pasteur pipette. Myocytes were
then separated by centrifugation at 30 × g for 4 min (4 °C) and discarded.
The supernatant with the rest of the cells was pelleted at 300 × g for 5 min
(4 °C). Cells were then passed through a 70 µm cell strainer and debris
removed by centrifugation over a 7.5% BSA-PBS cushion at 230 × g for
4 min (4 °C) twice.

Liver cells were isolated as described in Kawano et al.81. Brieﬂy, mice
were anesthetized with ketamine/xylazine (100 mg of ketamine/kg of body
weight and 10 mg of xylazine/kg). Livers were perfused in situ with liver
perfusion medium (Invitrogen) and then digested with liver digestion
medium (Invitrogen). Livers were then dissected, placed in ice-cold hepa-
tocyte wash medium (Invitrogen), and the capsule of the liver was then
opened to release the cell suspension. Hepatocytes were separated by cen-
trifugation at 30 × g for 4 min (4 °C). The rest of the cells (supernatant) were
pelleted by centrifugating 5 min at 300 × g (4 °C). Non-hepatocyte liver cells
were passed through a 70 µm cell strainer. Hepatocytes and the rest of the
liver cells were combined 1:1.

Pancreatic islets were isolated as described in Gómez-Banoy et al.82.
Brieﬂy, mouse pancreases were perfused with CiZyme (Vitacyte) through
the common hepatic duct. Pancreases were removed and digested at 37 °C
for 17 min. After two washes with RPMI medium with 3% FBS, islets were
separated into a gradient using RPMI medium and Histopaque-1077
(Sigma). Islets were then hand-picked and dispersed into a single-cell sus-
pension with 0.05% trypsin.

Mouse cardiac macrophages isolation
Mice were injected with 0.1 ml heparin (500 IU/ml i.p.) 20 min. before heart
excision and anesthetized with ketamine/xylazine (100 mg of ketamine/kg
of body weight and 10 mg of xylazine/kg). Hearts were excised and the blood
ﬂushed with ice-cold PBS 5 mM EDTA with a syringe. The LV in sham-
operated animals or the infarcted area in MI-operated animals were dis-
sected and minced with a razor blade. The minced tissue was kept in ice-cold
PBS 5 mM EDTA. Tissue fragments were spun down at 30 × g for 3 min
(4 °C) to further remove blood cells83. Tissue fragments were then digested
in HBBS 0.15 mg/ml Liberase TM (Sigma) for 25 min at 37 °C with vigorous
agitation. Digestion was stopped with FBS. The digestion mix was passed
through a 100 µm sieve and cardiomyocytes were separated by centrifuga-
tion at 30 × g for 4 min (4 °C). The rest of the cells (supernatant) were passed
through a 70 µm cell strainer and pelleted by centrifugating 5 min at 300 × g
(4 °C). The pellet was spun down on a 7.5% BSA cushion, for 4 min at
230 × g to clear debris (4 °C). Cells were then stained for FACS.

Mouse single cell-RNA sequencing
All cell suspensions were stained with trypan blue and counted using a
hemocytometer. Cells from one to two mice were pooled 1:1 per sample
(refer to https://cellxgene.cziscience.com/collections/24e324a1-b42d-4438-
9bb5-cf5233fa90b0 for detailed information). Cell suspensions were diluted
to target a recovery of 10,000 cells per sample at 50,000 reads per cell. The
isolated cells were sent to the Epigenomics Core Facility of Weill Cornell
Medicine for single-cell RNA-seq library preparation using the 10x Geno-
mics Chromium Single Cell 3’ GEM, Library & Gel Bead Kit v3, and
Chromium Single Cell B Chip Kit. The libraries were sequenced on a pair-
end ﬂow cell with a 2 × 50 cycles kit on Illumina NovaSeq6000.

Mouse RNA extraction and qPCR analysis
RNA isolation was performed with RNeasy Micro kits (Qiagen). cDNA was
synthesized through reverse transcription using High-Capacity cDNA
Reverse Transcription Kit (Thermo). cDNA was analyzed by real-time PCR
using speciﬁc gene primers (See Supplementary Table in Supplementary
Information) and PerfeCTa SYBR Green FastMix (Quanta) with a Quan-
taStudio6 Real-Time PCR System (Applied Biosystems). Rps-18 was used as
reference housekeeping gene.

Histology and immunostaining for mouse samples
Freshly collected mouse tissues were ﬁxed with 10% neutral buffered for-
malin (Sigma) overnight at 4 °C. Tissues were then transferred to 70%
ethanol and subsequently embedded in parafﬁn and sectioned at 5 μm
thickness. Tissue sections were sent to Weill Cornell’s Laboratory of
Comparative Pathology for hematoxylin and eosin (H&E) staining.

For immunohistochemistry (IHC) staining,

liver sections were
dewaxed, and antigen retrieval was performed using 10 mM sodium citrate

Communications Biology |

 (2024) 7:1611

15

https://doi.org/10.1038/s42003-024-07315-x

Article

buffer (pH 6.0) at boiling temperature for 14 min. Sections were incubated
overnight at 4 °C with anti-Mac2 antibody (Cedarlane cat. CL8942AP, 1:100
dilution), followed by incubation with a biotinylated secondary antibody
(Invitrogen cat. 31830, 1:500 dilution). All antibodies are commercially
available and are validated by suppliers. The biotinylated 2ary antibody was
detected using the HRP-conjugated avidin–biotin complex reagent VEC-
TASTAIN ABC-HRP Kit, Peroxidase (Standard) (Vector laboratories)
following the manufacturer’s protocol. Slides were developed using DAB
Substrate Kit, Peroxidase (HRP), with Nickel, 3,3′-diaminobenzidine (DAB)
(Vector laboratories) and counterstained with Mayer’s hematoxylin solu-
tion (Sigma). Microphotographs were taken on an optical microscope and
positive cells were counted manually.

White blood cell counts
Whole blood was diluted 1:30 with Türk’s solution (1% crystal violet, 1.5%
glacial acetic acid in distilled water) and stained cells were counted with a
hemocytometer.

Flow cytometry and cell sorting for mouse samples
Single cells were stained in FACS buffer (2% FBS, 0.05% sodium azide in
PBS) at 4 °C with ﬂuorescent antibodies and analyzed and FAC-sorted on a
Sony MA900 cell sorter. The following antibodies were used for WBC
analysis: Anti-CD16/32 (Biolegend cat. 101302, 0.25 μg/M cells) (to block
non-speciﬁc binding of immunoglobulins to Fc receptors), FITC Anti-
CD45R/B220 (Biolegend cat. 103206, 1 μg/M cells), APC anti-CD3 (BD
Pharmigen cat. 553066, 0.4 μg/M cells), Paciﬁc Blue™ anti-CD4 (Biolegend
cat. 100427, 0.2 μg/M cells), PE anti-CD8 (BD Pharmigen cat. 553032,
0.25 μg/M cells), FITC anti-CD11b (Biolegend cat. 101206, 0.25 μg/M cells),
and Paciﬁc Blue™ anti- Ly-6C (Biolegend cat. 128014, 0.2 μg/M cells). The
gating strategy can be found in Supplementary Information. The following
antibodies were used for cardiac macrophages: Anti-CD16/32 (Biolegend
cat. 101302, 0.25 μg/M cells) (to block non-speciﬁc binding of immu-
noglobulins to Fc receptors), FITC anti-CD11b (Biolegend cat. 101206,
0.25 μg/M cells), PE anti-F4/80 (Biolegend cat. 123110, 0.25 μg/M cells),
Paciﬁc Blue™ anti-Ly-6C (Biolegend cat. 128014, 0.2 μg/M cells), and Alexa
Fluor® 647 anti-CD206 (MMR) (Biolegend cat. 141712, 0.5 μg/M cells). All
antibodies are commercially available and are validated by suppliers.

IPA analysis
Ingenuity Pathway Analysis (IPA) version 01-20-04 (Qiagen) was utilized
for mouse pathway analyses. Redundant pathways and pathways sharing
the same genes and p value of enrichment were excluded from the plots.

Zebraﬁsh maintenance
Animal procedures were performed according to approved protocols by the
Institutional Animal Care and Use Committee (IACUC) at Weill Cornell
Medical College. We have complied with all relevant ethical regulations for
animal use. Adult zebraﬁsh of the Ekkwill (EK) strains were maintained at
28 °C under 14 h/10 h light/dark cycles84,85. Adult zebraﬁsh (8-month-old)
of both sexes were used for the experiments. Heart cryosection injury was
done as following a standard protocol86. The Tg(tcf21:nucEGFP)pd41 line47
was used. All reporters were analyzed as hemizygotes.

Zebraﬁsh cell isolation and single cell-RNA sequencing
Two biological replicates were included for all collected samples. Heart
ventricles were collected from adult hearts either with cryoinjury or unin-
jured control ﬁsh. Brieﬂy, ventricles were dissected using scissors and
forceps59,87. Ventricles were placed in the ice-cold PBS buffer with 1% BSA.
After several washes removing blood cells, ventricles were gently cut into
small pieces. Tissues were incubated in digestion buffer (0.5 ml HBSS plus
0.26 μ/ml Liberase DH [Roche]) for 45 min at 37 °C while agitating at
750 rpm on an Eppendorf ThermoMixer. Supernatants were collected every
15 min and neutralized with 10% sheep serum, and cells were completely
disaggregated by gently pipetting up and down. The dissociated cells were
centrifuged at 200 × g for 5 min at 4 °C and re-suspended in HBSS with

0.05% BSA. The cell suspension (2 ml) was then gently added on top of 2 ml
HBSS buffer with 7.5% BSA. After spinning down at 200 × g for 5 min at
4 °C, the pellet was resuspended in 500 ml and ﬁltered through a 35 μm
strainer. Whole kidney marrow cells were isolated using an established
protocol88. Brieﬂy, kidneys were collected on ice and homogenized imme-
diately in PBS plus 0.05% BSA by using a 10 ml syringe with 18.5 G. The
dissociated cells were washed twice in PBS plus 0.05% BSA and spun down
at 300 × g for 5 min at 4 °C. Pellets were re-suspended in PBS plus 0.05%
BSA and ﬁltered through a 35 μm strainer. Livers were collected on ice and
incubated in digestion buffer (0.5 ml HBSS plus 0.13 U/ml Liberase DH
[Roche]) at room temperature. The cell lyses was gently stirred with a
Spinbar® magnetic stirring bar (Bel-Art Products), and the supernatant
were collected every 5 min. The cell lysate was ﬁltered through a 70 μm
strainer and centrifuged at 150 × g for 3 min at 4 °C. Pellet was resuspended
in PBS plus 0.05% BSA and then gently added on top of HBSS buffer with
7.5% BSA. After spinning down at 300 × g for 5 min, pellets were washed
one more time with PBS plus 0.05% BSA. After centrifuging at 300 × g for
5 min, the resuspended cell lyses was ﬁltered through a 35 μm strainer.
Pancreatic cells were isolated using the same protocol as liver cells except for
the initial spinning down at 300 × g for 5 min. All suspended cells were
stained with trypan blue and counted using a hemocytometer. The isolated
cells were sent to the Epigenomics Core Facility of Weill Cornell Medicine
for single-cell RNA-seq library preparation using the 10x Genomics
Chromium Single Cell 3’ GEM, Library & Gel Bead Kit v3, and Chromium
Single Cell B Chip Kit. The libraries were sequenced on a pair-end ﬂow cell
with a 2 × 50 cycles kit on Illumina NovaSeq6000. We sequenced 2 replicates
of all samples (24 total).

scRNA-seq analysis
The raw reads were aligned and processed with the CellRanger pipeline
(v6.0.0) using the mouse (mm10) or zebraﬁsh genomes (GRCz11). Sub-
sequent analyses were performed in R following the recommendations of
Amezquita et al. (https://osca.bioconductor.org/) using numerous functions
provided in the R packages scater89 (v1.24.0) and scran90 (v1.22.1). Brieﬂy,
quality control was carried out for each sample separately with functions
from the scuttle89 package; cells with low gene content and high mito-
chondrial gene content were removed from further analyses. For each
species, count matrices across all samples were scaled for sequencing depth
differences, log-transformed, and integrated using multiBatchNorm and
fastMNN functions from the batchelor91 package (v1.10.0). Dimensionality
reductions were done with scater (runUMAP) using the batch-corrected
values. Cell types were annotated with SingleR37 (v1.8.1) using numerous
datasets and manual inspection of marker genes. For zebraﬁsh annotation
with SingleR, the following datasets were used as references: pancreas
(GSM3509161), WKM (GSE100911)92, and heart (GSE158919)93. For
mouse annotation with SingleR, the following datasets were used as refer-
ences: pancreas (GSE84133)94, kidney (GSM2967051, GSE119531)95, liver
(GSE125688, GSE171904)96,97, and heart (GSM2967050, E-MTAB-6173)98.
The following referecnes were also used for the mouse cell type markers:
cells100, ﬁbroblasts101,
endothelial
lymphocytes102, myeloid cells as a whole, and macrophages, dendritic cells103,
granulocytes104, hepatocytes105, natural killer cells106, pancreatic cells94,107.
References for speciﬁc maker genes are listed in the text. Data was also
explored and annotated with Cellxgene version v0.16.8. scRNA-seq data
UMAPs, SAMaps, dot plots, and violin plots were generated with Cellxgene
VIP (https://doi.org/10.1101/2020.08.28.270652). Cell proportions were
calculated by dividing the number of cells of a speciﬁc type by the total
number of cells in the sample. Gene ontology analysis was performed on
marker genes identiﬁed between clusters of the same cell type.

and pericytes99,

epithelial

cells

Cross-species comparisons
SAMap65 (v1.0.2) was used to determine cell homology between mouse and
zebraﬁsh mono/Mϕ clusters and hepatocytes. Brieﬂy, a reciprocal BLAST
map between mouse and zebraﬁsh transcriptomes was generated using the
map_genes.sh script from SAMap, which ran tblastx (nucleotide-nucleotide

Communications Biology |

 (2024) 7:1611

16

https://doi.org/10.1038/s42003-024-07315-x

Article

BLAST, NCBI) in both directions with respect to Ensembl zebraﬁsh and
mouse transcriptomes (Danio_rerio.GRCz11.cds.all.fa and Mus_muscu-
lus.GRCm38.cds.all.fa). Raw scRNA-seq count matrices of zebraﬁsh and
mouse were extracted from SingleCellExperiment objects with cluster
annotations and converted to h5ad format using the sceasy R package
(v0.0.7). Raw data were then processed and integrated by SAMap. Mapping
scores between the mono/Mϕ clusters and hepatocytes of each species were
calculated with SAMap get_mapping_scores (n top=0) and visualized in R
using ggalluvial; cluster pairs with alignment scores less than 0.2 were
excluded.

For hepatocytes and mono/Mϕ cluster pairs with high inter-species
alignment scores (mm1-dr4, mm4-dr6, and mm6-dr3), marker genes for
each cell population were assessed using scran::scoreMarkers (mean
AUC > 0.6), and over-representation analyses were performed using
clusterProﬁler108 (v4.2.2) with respect to gene ontology terms. Gene ontol-
ogy terms with semantic similarity were reduced using the rrvgo (v1.6.0) R
package (with similarity threshold set to 0.5). Sayols, S (2023). rrvgo: a
Bioconductor package for interpreting lists of Gene Ontology terms.
microPublication Biology. 10.17912/micropub.biology.000811.

To compare the transcriptional response to MI (mouse) or cardiac
cryoinjury (zebraﬁsh) between the hepatocytes and the mono/Mϕ cluster
pairs, differential expression analysis was performed using scran::ﬁnd-
Markers(lfc = 0.25) at days 1 and 7 in the heart and in the liver. Genes were
considered statistically signiﬁcant at an FDR cutoff of 0.10.

Zebraﬁsh histology and microscopy
Freshly collected zebraﬁsh tissues were ﬁxed with 4% paraformaldehyde
(PFA) overnight at 4 C and applied to cryosection at a 10 μm thickness.
Hybridization Chain Reaction (HCR 3.0) staining of whole-mounted hearts
or cryosections was done following the published protocols61. HCR probes
for havcr1, moxd1, cd9b, fn1a, and gda were synthesized by Molecular
Instruments Inc. For immunostaining of whole-mounted hearts or heart
sections109,110, samples were blocked with 2% bovine serum albumin (BSA,
VWR, cat#97061), 1% DMSO, 0.5% goat serum (ThermoFisher, cat#16210)
and 0.5% Triton X-100 in PBS for 1 h at room temperature (RT). Primary
antibodies were diluted in the blocking buffer and incubated with hearts
overnight at 4 C. Hearts were then washed with PBS plus 0.1% Tween 20 and
incubated with the secondary antibody diluted in the blocking buffer for
1.5 h at room temperature. Hearts were stained with DAPI (ThermoFisher,
D3571) to visualize nuclei. The primary antibody used in this study was
rabbit anti-lcp1 (GeneTex GTX124420, 1:200), the secondary antibody used
in this study was Alexa Fluor 488 goat anti-rabbit (ThermoFisher, 1:200).
IB4 (Vector Laboratories, DL-1207, 1:100) staining was perfomed by
standard procedures63. All antibodies are commercially available and are
validated by suppliers. Fluorescent images of tissue sections were captured
used a Zeiss 800 confocal microscope (Zen 2.6 blue edition software).

Statistics and reproducibility
Unless otherwise stated, data are presented as mean ± s.e.m. Data are
derived from multiple experiments, and measurements were taken from
distinct samples (animals) unless stated otherwise. If not mentioned
otherwise in the ﬁgure legend, statistical signiﬁcance is indicated by
*P < 0.05, **P < 0.01 and ***P < 0.001. Statistical analysis was carried out
assuming normal distribution after visualizing the data in histograms and
conﬁrming a normal distribution. Data was plotted in a QQ plot when
histograms were not clear. Non-parametric analyses were used when nor-
mal data distribution could not be assumed. Statistical signiﬁcance was
tested with unpaired, two-tailed t-test, and one-way or two-way ANOVA
with Tukey’s honest signiﬁcant difference (HSD) post hoc test for multiple
comparisons when one or two independent variables, respectively, were
compared. GraphPad Prism 7 was used for statistical analysis.

Data availability
The scRNA-seq datasets generated in this study have been deposited at the
Cellxgene platform (https://cellxgene.cziscience.com/collections/24e324a1-
b42d-4438-9bb5-cf5233fa90b0) as well as the NCBI’s Gene Expression
Omnibus under accession number GSE227191. Numerical data used for
plots can be found in Supplementary Datas 1-12.

Code availability
Scripts and code used for processing and annotating the scRNA-seq are
deposited at Github (https://github.com/abcwcm/CZI_MI_mouseZebraﬁsh)
and Zenodo111.

Received: 12 August 2024; Accepted: 22 November 2024;

References
1.

Collaborators, G. B. D. M. Global, regional, and national age-sex-
speciﬁc mortality and life expectancy, 1950-2017: a systematic
analysis for the Global Burden of Disease Study 2017. Lancet 392,
1684–1735 (2018).
Tsao, C. W. et al. Heart Disease and Stroke Statistics-2022 update: a
report from the American Heart Association. Circulation 145,
e153–e639 (2022).
Sun, F. & Poss, K. D. Inter-organ communication during tissue
regeneration. Development 150 https://doi.org/10.1242/dev.
202166 (2023).
Merkler, A. E. et al. Duration of heightened ischemic stroke risk after
acute myocardial infarction. J. Am. Heart Assoc. 7, e010782 (2018).
Hasin, T. et al. Patients with heart failure have an increased risk of
incident cancer. J. Am. Coll. Cardiol. 62, 881–886 (2013).
Hasin, T. et al. Heart failure after myocardial infarction is associated
with increased risk of cancer. J. Am. Coll. Cardiol. 68, 265–271 (2016).
Adamo, L., Rocha-Resende, C., Prabhu, S. D. & Mann, D. L.
Reappraising the role of inﬂammation in heart failure. Nat. Rev.
Cardiol. 17, 269–285 (2020).
Ridker, P. M. et al. Antiinﬂammatory therapy with canakinumab for
atherosclerotic disease. N. Engl. J. Med 377, 1119–1131 (2017).
Tardif, J. C. et al. Efﬁcacy and safety of low-dose colchicine after
myocardial infarction. N. Engl. J. Med. 381, 2497–2505 (2019).
Koelwyn, G. J. et al. Myocardial infarction accelerates breast cancer
via innate immune reprogramming. Nat. Med. 26, 1452–1458 (2020).
Ridker, P. M. et al. Effect of interleukin-1beta inhibition with
canakinumab on incident lung cancer in patients with
atherosclerosis: exploratory results from a randomised, double-
blind, placebo-controlled trial. Lancet 390, 1833–1842 (2017).
Ridker, P. M., Tuttle, K. R., Perkovic, V., Libby, P. & MacFadyen, J. G.
Inﬂammation drives residual risk in chronic kidney disease: a
CANTOS substudy. Eur. Heart J. 43, 4832–4844 (2022).
Kubo, S. H., Walter, B. A., John, D. H., Clark, M. & Cody, R. J. Liver
function abnormalities in chronic heart failure. Inﬂuence of systemic
hemodynamics. Arch. Intern Med 147, 1227–1230 (1987).
Yap, J. et al. Macrophages in cardiac remodelling after myocardial
infarction. Nat. Rev. Cardiol. https://doi.org/10.1038/s41569-022-
00823-5 (2023).

2.

3.

4.

5.

6.

7.

8.

9.

10.

11.

12.

13.

14.

16.

15. Dick, S. A. & Epelman, S. Chronic heart failure and inﬂammation:
what do we really know? Circ. Res. 119, 159–176 (2016).
Zhuang, L. et al. Global characteristics and dynamics of single
immune cells after myocardial infarction. J. Am. Heart Assoc. 11,
e027228 (2022).
Jung, S. H. et al. Spatiotemporal dynamics of macrophage
heterogeneity and a potential function of Trem2(hi) macrophages in
infarcted hearts. Nat. Commun. 13, 4580 (2022).

17.

Reporting summary
Further information on research design is available in the Nature Portfolio
Reporting Summary linked to this article.

18. Horckmans, M. et al. Neutrophils orchestrate post-myocardial

infarction healing by polarizing macrophages towards a reparative
phenotype. Eur. Heart J. 38, 187–197 (2017).

Communications Biology |

 (2024) 7:1611

17

https://doi.org/10.1038/s42003-024-07315-x

Article

19.

Vagnozzi, R. J. et al. An acute immune response underlies the beneﬁt
of cardiac stem cell therapy. Nature 577, 405–409 (2020).

20. Grune, J. et al. Neutrophils incite and macrophages avert electrical
storm after myocardial infarction. Nat. Cardiovasc. Res. 1, 649–664
(2022).

42.

speciﬁc natural killer cells responding to infection. Nat. Immunol. 15,
546–553 (2014).
Rubin, S. A. et al. Single-cell analyses reveal early thymic progenitors
and pre-B cells in zebraﬁsh. J. Exp. Med. 219 https://doi.org/10.
1084/jem.20220038 (2022).

21. Gonzalez-Rosa, J. M., Burns, C. E. & Burns, C. G. Zebraﬁsh heart

43. Moore, J. C. et al. T cell immune deﬁciency in zap70 mutant

22.

23.

regeneration: 15 years of discoveries. Regeneration 4, 105–123 (2017).
Kikuchi, K. et al. Primary contribution to zebraﬁsh heart regeneration
by gata4(+) cardiomyocytes. Nature 464, 601–605 (2010).
Bevan, L. et al. Speciﬁc macrophage populations promote both
cardiac scar deposition and subsequent resolution in adult zebraﬁsh.
Cardiovasc. Res. https://doi.org/10.1093/cvr/cvz221 (2019).
24. Denans, N. et al. An anti-inﬂammatory activation sequence governs
macrophage transcriptional dynamics during tissue injury in
zebraﬁsh. Nat. Commun. 13, 5356 (2022).
Peterson, E. A., Sun, J. & Wang, J. Leukocyte-mediated cardiac
repair after myocardial infarction in non-regenerative vs.
regenerative systems. J. Cardiovasc. Dev. Dis. 9 https://doi.org/10.
3390/jcdd9020063 (2022).

25.

27.

26. Hui, S. P. et al. Zebraﬁsh regulatory T cells mediate organ-speciﬁc
regenerative programs. Dev. Cell 43, 659–672.e655 (2017).
Lai, S. L. et al. Reciprocal analyses in zebraﬁsh and medaka reveal
that harnessing the immune response promotes cardiac
regeneration. eLife 6 https://doi.org/10.7554/eLife.25605 (2017).
28. Wei, K. H. et al. Comparative single-cell proﬁling reveals distinct
cardiac resident macrophages essential for zebraﬁsh heart
regeneration. eLife 12 https://doi.org/10.7554/eLife.84679 (2023).
de Preux Charles, A. S., Bise, T., Baier, F., Marro, J. & Jazwinska, A.
Distinct effects of inﬂammation on preconditioning and regeneration
of the adult zebraﬁsh heart. Open Biol. 6 https://doi.org/10.1098/
rsob.160102 (2016).

29.

31.

30. Ma, H. et al. Functional coordination of non-myocytes plays a key
role in adult zebraﬁsh heart regeneration. EMBO Rep. 22, e52901
(2021).
Simoes, F. C. et al. Macrophages directly contribute collagen to scar
formation during zebraﬁsh heart regeneration and mouse heart
repair. Nat. Commun. 11, 600 (2020).
Bruton, F. A. et al. Macrophages trigger cardiomyocyte proliferation
by increasing epicardial vegfaa expression during larval zebraﬁsh
heart regeneration. Dev. Cell 57, 1512–1528.e1515 (2022).
33. Gurevich, D. B. et al. Live imaging of wound angiogenesis reveals
macrophage orchestrated vessel sprouting and regression. EMBO
J. 37 https://doi.org/10.15252/embj.201797786 (2018).

32.

34. Nossuli, T. O. et al. A chronic mouse model of myocardial ischemia-
reperfusion: essential in cytokine studies. Am. J. Physiol. Heart Circ.
Physiol. 278, H1049–H1055 (2000).

37.

36.

35. Ong, S. B. et al. Inﬂammation following acute myocardial infarction:
multiple players, dynamic roles, and novel therapeutic opportunities.
Pharm. Ther. 186, 73–87 (2018).
Lindsey, M. L. et al. Guidelines for in vivo mouse models of
myocardial infarction. Am. J. Physiol. Heart Circ. Physiol. 321,
H1056–H1073 (2021).
Aran, D. et al. Reference-based analysis of lung single-cell
sequencing reveals a transitional proﬁbrotic macrophage. Nat.
Immunol. 20, 163–172 (2019).
Andreu-Ballester, J. C. et al. Lymphopenia in hospitalized patients
and its relationship with severity of illness and mortality. PLoS ONE
16, e0256205 (2021).
Tsedeke, A. T. et al. Cardiomyocyte heterogeneity during zebraﬁsh
development and regeneration. Dev. Biol. 476, 259–271 (2021).
Zhou, Q. et al. Cross-organ single-cell transcriptome proﬁling
reveals macrophage and dendritic cell heterogeneity in zebraﬁsh.
Cell Rep. 42, 112793 (2023).
Beaulieu, A. M., Zawislak, C. L., Nakayama, T. & Sun, J. C. The
transcription factor Zbtb32 controls the proliferative burst of virus-

40.

38.

39.

41.

44.

zebraﬁsh. Mol. Cell Biol. 36, 2868–2876 (2016).
Lin, H. F. et al. Analysis of thrombocyte development in CD41-GFP
transgenic zebraﬁsh. Blood 106, 3803–3810 (2005).

46.

45. Hu, C. et al. Single-cell RNA sequencing unveils the hidden powers
of zebraﬁsh kidney for generating both hematopoiesis and adaptive
antiviral immunity. eLife 13 https://doi.org/10.7554/eLife.92424
(2024).
Renshaw, S. A. et al. A transgenic zebraﬁsh model of neutrophilic
inﬂammation. Blood 108, 3976–3978 (2006).
Kikuchi, K. et al. tcf21+ epicardial cells adopt non-myocardial fates
during zebraﬁsh heart development and regeneration. Development
138, 2895–2902 (2011).
Kim, J. et al. PDGF signaling is required for epicardial function and
blood vessel formation in regenerating zebraﬁsh hearts. Proc. Natl
Acad. Sci. USA 107, 17206–17210 (2010).

47.

48.

50.

49. Her, G. M., Yeh, Y. H. & Wu, J. L. 435-bp liver regulatory sequence in
the liver fatty acid binding protein (L-FABP) gene is sufﬁcient to
modulate liver regional expression in transgenic zebraﬁsh. Dev. Dyn.
227, 347–356 (2003).
Singh, S. P. et al. A single-cell atlas of de novo beta-cell regeneration
reveals the contribution of hybrid beta/delta-cells to diabetes
recovery in zebraﬁsh. Development 149 https://doi.org/10.1242/
dev.199853 (2022).
Kobayashi, I. et al. Enrichment of hematopoietic stem/progenitor
cells in the zebraﬁsh kidney. Sci. Rep. 9, 14205 (2019).
Bassler, K., Schulte-Schrepping, J., Warnat-Herresthal, S.,
Aschenbrenner, A. C. & Schultze, J. L. The myeloid cell
compartment-cell by cell. Annu. Rev. Immunol. 37, 269–293 (2019).
53. Dick, S. A. et al. Three tissue resident macrophage subsets coexist
across organs with conserved origins and life cycles. Sci. Immunol.
7, eabf7777 (2022).

52.

51.

54. Nguyen-Chi, M. et al. Identiﬁcation of polarized macrophage

55.

subsets in zebraﬁsh. eLife 4, e07288 (2015).
Rougeot, J. et al. RNAseq proﬁling of leukocyte populations in
zebraﬁsh larvae reveals a cxcl11 chemokine gene as a marker of
macrophage polarization during mycobacterial infection. Front.
Immunol. 10, 832 (2019).

56. Wang, J., Karra, R., Dickson, A. L. & Poss, K. D. Fibronectin is

57.

58.

59.

60.

deposited by injury-activated epicardial cells and is necessary for
zebraﬁsh heart regeneration. Dev. Biol. 382, 427–435 (2013).
Ferrero, G. et al. The macrophage-expressed gene (mpeg) 1
identiﬁes a subpopulation of B cells in the adult zebraﬁsh. J. Leukoc.
Biol. 107, 431–443 (2020).
Jablonski, K. A. et al. Novel markers to delineate murine M1 and M2
macrophages. PLoS ONE 10, e0145342 (2015).
Xia, Y. et al. Activation of a transient progenitor state in the
epicardium is required for zebraﬁsh heart regeneration. Nat.
Commun. 13, 7704 (2022).
Feng, Y., Santoriello, C., Mione, M., Hurlstone, A. & Martin, P. Live
imaging of innate immune cell sensing of transformed cells in
zebraﬁsh larvae: parallels between tumor initiation and wound
inﬂammation. PLoS Biol. 8, e1000562 (2010).

62.

61. Choi, H. M. T. et al. Third-generation in situ hybridization chain
reaction: multiplexed, quantitative, sensitive, versatile, robust.
Development 145 https://doi.org/10.1242/dev.165753 (2018).
Shimizu, Y., Kiyooka, M. & Ohshima, T. Transcriptome analyses
reveal IL6/Stat3 signaling involvement in radial glia proliferation after
stab wound injury in the adult zebraﬁsh optic tectum. Front. Cell Dev.
Biol. 9, 668408 (2021).

Communications Biology |

 (2024) 7:1611

18

https://doi.org/10.1038/s42003-024-07315-x

Article

63.

Sun, J., Peterson, E. A., Chen, X. & Wang, J. ptx3a(+) ﬁbroblast/
epicardial cells provide a transient macrophage niche to promote
heart regeneration. Cell Rep. 43, 114092 (2024).

65.

64. Wong, N. R. et al. Resident cardiac macrophages mediate adaptive
myocardial remodeling. Immunity 54, 2072–2088 e2077 (2021).
Tarashansky, A. J. et al. Mapping single-cell atlases throughout
Metazoa unravels cell type evolution. eLife 10 https://doi.org/10.
7554/eLife.66747 (2021).

67.

68.

66. Cai, S. et al. Mitochondrial dysfunction in macrophages promotes
inﬂammation and suppresses repair after myocardial infarction. J.
Clin. Invest. 133 https://doi.org/10.1172/JCI159498 (2023).
Thorp, E. B. Cardiac macrophages and emerging roles for their
metabolism after myocardial infarction. J. Clin. Invest. 133 https://
doi.org/10.1172/JCI171953 (2023).
Amrute, J. M. et al. Deﬁning cardiac functional recovery in end-stage
heart failure at single-cell resolution. Nat. Cardiovasc. Res. 2,
399–416 (2023).
Rizzo, G. et al. Dynamics of monocyte-derived macrophage
diversity in experimental myocardial infarction. Cardiovasc. Res.
119, 772–785 (2023).
Lavine, K. J. et al. Distinct macrophage lineages contribute to
disparate patterns of cardiac recovery and remodeling in the
neonatal and adult heart. Proc. Natl Acad. Sci. USA 111,
16029–16034 (2014).

69.

70.

71. Wang, Z. et al. Cell-type-speciﬁc gene regulatory networks
underlying murine neonatal heart regeneration at single-cell
resolution. Cell Rep. 33, 108472 (2020).

72. Hoyer, F. F. et al. Tissue-speciﬁc macrophage responses to remote
injury impact the outcome of subsequent local immune challenge.
Immunity 51, 899–914.e897 (2019).

73. Hoffmann, J. et al. Post-myocardial infarction heart failure

74.

75.

dysregulates the bone vascular niche. Nat. Commun. 12, 3964
(2021).
van Blokland, I. V. et al. Single-cell dissection of the immune
response after acute myocardial infarction. Circ. Genom. Precis.
Med. e004374 https://doi.org/10.1161/CIRCGEN.123.004374
(2024).
Abplanalp, W. T. et al. Single-cell RNA-sequencing reveals profound
changes in circulating immune cells in patients with heart failure.
Cardiovasc. Res. 117, 484–494 (2021).

76. Cavone, L. et al. A unique macrophage subpopulation signals

directly to progenitor cells to promote regenerative neurogenesis in
the zebraﬁsh spinal cord. Dev. Cell 56, 1617–1630.e1616 (2021).

77. Chablais, F. & Jazwinska, A. The regenerative capacity of the

79.

78.

zebraﬁsh heart is dependent on TGFbeta signaling. Development
139, 1921–1930 (2012).
Shao, Y., Redfors, B. & Omerovic, E. Modiﬁed technique for coronary
artery ligation in mice. J. Vis. Exp. https://doi.org/10.3791/3093
(2013).
Barry, D. M. et al. Molecular determinants of nephron vascular
specialization in the kidney. Nat. Commun. 10, 5705 (2019).
80. Cerrone, M. et al. Plakophilin-2 is required for transcription of genes
that control calcium cycling and cardiac rhythm. Nat. Commun. 8,
106 (2017).
Kawano, Y. et al. Thioesterase superfamily member 2 (Them2) and
phosphatidylcholine transfer protein (PC-TP) interact to promote
fatty acid oxidation and control glucose utilization. Mol. Cell Biol. 34,
2396–2408 (2014).

81.

84. Wang, J. et al. The regenerative capacity of zebraﬁsh reverses

cardiac failure caused by genetic cardiomyocyte depletion.
Development 138, 3421–3430 (2011).
Poss, K. D., Wilson, L. G. & Keating, M. T. Heart regeneration in
zebraﬁsh. Science 298, 2188–2190 (2002).

85.

86. Chablais, F., Veit, J., Rainer, G. & Jazwinska, A. The zebraﬁsh heart

regenerates after cryoinjury-induced myocardial infarction. BMC
Dev. Biol. 11, 21 (2011).

87. Cao, J. et al. Single epicardial cell transcriptome sequencing
identiﬁes Caveolin 1 as an essential factor in zebraﬁsh heart
regeneration. Development 143, 232–243 (2016).
LeBlanc, J., Bowman, T. V. & Zon, L. Transplantation of whole kidney
marrow in adult zebraﬁsh. J. Vis. Exp. 159 https://doi.org/10.3791/
159 (2007).

88.

89. McCarthy, D. J., Campbell, K. R., Lun, A. T. & Wills, Q. F. Scater: pre-
processing, quality control, normalization and visualization of single-
cell RNA-seq data in R. Bioinformatics 33, 1179–1186 (2017).
Lun, A. T., McCarthy, D. J. & Marioni, J. C. A step-by-step workﬂow
for low-level analysis of single-cell RNA-seq data with Bioconductor.
F1000Res 5, 2122 (2016).

90.

91. Haghverdi, L., Lun, A. T. L., Morgan, M. D. & Marioni, J. C. Batch
effects in single-cell RNA-sequencing data are corrected by
matching mutual nearest neighbors. Nat. Biotechnol. 36, 421–427
(2018).
Tang, Q. et al. Dissecting hematopoietic and renal cell heterogeneity
in adult zebraﬁsh at single-cell resolution using RNA sequencing. J.
Exp. Med. 214, 2875–2887 (2017).

92.

93. Hu, B. et al. Origin and function of activated ﬁbroblast states during

94.

zebraﬁsh heart regeneration. Nat. Genet. 54, 1227–1237 (2022).
Baron, M. et al. A single-cell transcriptomic map of the human and
mouse pancreas reveals inter- and intra-cell population structure.
Cell Syst. 3, 346–360.e344 (2016).

96.

97.

95. Wu, H., Kirita, Y., Donnelly, E. L. & Humphreys, B. D. Advantages of
single-nucleus over single-cell RNA sequencing of adult kidney: rare
cell types and novel cell states revealed in ﬁbrosis. J. Am. Soc.
Nephrol. 30, 23–32 (2019).
Pepe-Mooney, B. J. et al. Single-cell analysis of the liver epithelium
reveals dynamic heterogeneity and an essential role for YAP in
homeostasis and regeneration. Cell Stem Cell 25, 23–38.e28 (2019).
Yang, W. et al. Single-cell transcriptomic analysis reveals a hepatic
stellate cell-activation roadmap and myoﬁbroblast origin during liver
ﬁbrosis in mice. Hepatology 74, 2774–2790 (2021).
Skelly, D. A. et al. Single-cell transcriptional proﬁling reveals cellular
diversity and intercommunication in the mouse heart. Cell Rep. 22,
600–610 (2018).
Kalucka, J. et al. Single-cell transcriptome atlas of murine
endothelial cells. Cell 180, 764–779.e720 (2020).

98.

99.

100. Rajasekaran, S. A. et al. Na,K-ATPase activity is required for

formation of tight junctions, desmosomes, and induction of polarity
in epithelial cells. Mol. Biol. Cell 12, 3717–3732 (2001).

101. Muhl, L. et al. Single-cell analysis uncovers ﬁbroblast heterogeneity

and criteria for ﬁbroblast and mural cell identiﬁcation and
discrimination. Nat. Commun. 11, 3953 (2020).

102. Zhang, Y. et al. A biphenotypic lymphocyte subset displays both T-

and B-cell functionalities. Commun. Biol. 7, 28 (2024).
103. Valente, M. et al. Novel mouse models based on intersectional

genetics to identify and characterize plasmacytoid dendritic cells.
Nat. Immunol. 24, 714–728 (2023).

82. Gomez-Banoy, N. et al. Adipsin preserves beta cells in diabetic mice
and associates with protection from type 2 diabetes in humans. Nat.
Med. 25, 1739–1747 (2019).

83. Covarrubias, R. et al. Optimized protocols for isolation, ﬁxation, and

ﬂow cytometric characterization of leukocytes in ischemic hearts.
Am. J. Physiol. Heart Circ. Physiol. 317, H658–H666 (2019).

104. Shi, Y. et al. Resistin-like molecules: a marker, mediator and

therapeutic target for multiple diseases. Cell Commun. Signal 21, 18
(2023).

105. Hildebrandt, F. et al. Spatial transcriptomics to deﬁne transcriptional
patterns of zonation and structural components in the mouse liver.
Nat. Commun. 12, 7046 (2021).

Communications Biology |

 (2024) 7:1611

19

https://doi.org/10.1038/s42003-024-07315-x

Article

106. Santana-Hernandez, S. et al. NK cell-triggered CCL5/IFNgamma-
CXCL9/10 axis underlies the clinical efﬁcacy of neoadjuvant anti-
HER2 antibodies in breast cancer. J. Exp. Clin. Cancer Res. 43, 10
(2024).

107. Rubio-Navarro, A. et al. A beta cell subset with enhanced insulin
secretion and glucose metabolism is reduced in type 2 diabetes.
Nat. Cell Biol. 25, 565–578 (2023).

108. Yu, G., Wang, L. G., Han, Y. & He, Q. Y. clusterProﬁler: an R package
for comparing biological themes among gene clusters. OMICS 16,
284–287 (2012).

109. Cao, J. et al. Tension creates an endoreplication wavefront that

leads regeneration of epicardial tissue. Dev. Cell 42, 600–615 e604
(2017).

110. Wang, J., Cao, J., Dickson, A. L. & Poss, K. D. Epicardial

regeneration is guided by cardiac outﬂow tract and Hedgehog
signalling. Nature 522, 226–230 (2015).

111. Dündar, F. & Zumbo, P. abcwcm/CZI_MI_mouseZebraﬁsh:

CZI_MI_mouseZebraﬁsh. Zenodo https://doi.org/10.5281/zenodo.
14048063 (2024).

Acknowledgements
We thank Adedeji A. Afolalu, Chaim Shapiro, Soji Hosten, and Chelsea
Quaies for ﬁsh care. We thank the Epigenomics Core of Weill Cornell
Medicine for their technical support. This work was supported by Rudin
Foundation fellowships to Y.X. and J.Y., a predoctoral training grant position
in Stem Cell Biology and Regenerative Medicine from New York State Stem
Cell Science program (NYSTEM) to B.P. The research was supported by
Chan Zuckerberg Initiative grant (DAF2020-217734) to D.B., J.C, and J.C.L.,
Weill Cornell Start-up fund and NIH grants (R01HL155607 and
R01HL166518) to J.C. J.C.L. is supported by NIH grants R01 DK121844,
R01 DK121140, and R01 DK132879. We thank G.S.P. and M.H. for con-
structive feedback on the manuscript.

Author contributions
E.C., J.Y., D.B., J.C., and J.C.L. designed the study and wrote the
manuscript with input from all authors. E.C., J.Y., Y.X., A.R.-N., B.Y., B.P.,
M.Q., E.A.H., L.S., performed and analyzed the animal experiments. P.Z.,
F.D., E.C., and A.M.P. analyzed the scRNA-Seq experiments. J.C.L, J.C.,
and D.B. conceived and supervised the study and acquired funding for
the work.

Competing interests
The authors declare no competing interests.

Additional information
Supplementary information The online version contains
supplementary material available at
https://doi.org/10.1038/s42003-024-07315-x.

Correspondence and requests for materials should be addressed to
Doron Betel, Jingli Cao or James C. Lo.

Peer review information Communications Biology thanks the anonymous
reviewers for their contribution to the peer review of this work. Primary
Handling Editor: Dario Ummarino.

Reprints and permissions information is available at
http://www.nature.com/reprints

Publisher’s note Springer Nature remains neutral with regard to
jurisdictional claims in published maps and institutional afﬁliations.

Open Access This article is licensed under a Creative Commons
Attribution-NonCommercial-NoDerivatives 4.0 International License,
which permits any non-commercial use, sharing, distribution and
reproduction in any medium or format, as long as you give appropriate
credit to the original author(s) and the source, provide a link to the Creative
Commons licence, and indicate if you modiﬁed the licensed material. You
do not have permission under this licence to share adapted material
derived from this article or parts of it. The images or other third party
material in this article are included in the article’s Creative Commons
licence, unless indicated otherwise in a credit line to the material. If material
is not included in the article’s Creative Commons licence and your intended
use is not permitted by statutory regulation or exceeds the permitted use,
you will need to obtain permission directly from the copyright holder. To
view a copy of this licence, visit http://creativecommons.org/licenses/by-
nc-nd/4.0/.

© The Author(s) 2024

Communications Biology |

 (2024) 7:1611

20

