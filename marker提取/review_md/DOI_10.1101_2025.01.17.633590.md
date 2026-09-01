bioRxiv preprint doi: https://doi.org/10.1101/2025.01.17.633590; this version posted January 22, 2025. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under a CC-BY-ND 4.0 International license.
1 Single-cell decoding of human islet cell type-specific alterations in type 2
β
2 diabetes reveals converging genetic- and state-driven -cell gene expression
3 defects
4
5 Khushdeep Bandesh1†, Efthymios Motakis1†, Siddhi Nargund1†, Romy Kursawe1, Vijay Selvam1,
6 Redwan M Bhuiyan1,2, Giray Naim Eryilmaz1, Sai Nivedita Krishnan1,2, Cassandra N.
7 Spracklen3, Duygu Ucar1,2,4 and Michael L. Stitzel1,2,4, *
8
9 1 The Jackson Laboratory for Genomic Medicine, 10 Discovery Drive, Farmington, CT 06032
10 USA
11 2 Department of Genetics and Genome Sciences, UConn Health, Farmington, CT 06032 USA
12 3 Department of Biostatistics and Epidemiology, University of Massachusetts Amherst, Amherst, MA,
13 USA
14 4 Institute for Systems Genomics, UConn, Farmington, CT 06032 USA
15
16 † Co-first authors
17 * Corresponding author: Michael L. Stitzel (michael.stitzel@jax.org)
18
19
20
21
22
1

bioRxiv preprint doi: https://doi.org/10.1101/2025.01.17.633590; this version posted January 22, 2025. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under a CC-BY-ND 4.0 International license.
23 Abstract
24 Pancreatic islets maintain glucose homeostasis through coordinated action of their constituent
25 endocrine and affiliate cell types and are central to type 2 diabetes (T2D) genetics and
26 pathophysiology. Our understanding of robust human islet cell type-specific alterations in T2D
27 remains limited. Here, we report comprehensive single cell transcriptome profiling of 245,878
28 human islet cells from a 48-donor cohort spanning non-diabetic (ND), pre-diabetic (PD), and
29 T2D states, identifying 14 distinct cell types detected in every donor from each glycemic state.
30 Cohort analysis reveals ~25-30% loss of functional beta cell mass in T2D vs. ND or PD donors
31 resulting from (1) reduced total beta cell numbers/proportions and (2) reciprocal loss of ‘high
32 function’ and gain of senescent β-cell subpopulations. We identify in T2D β-cells 511
33 differentially expressed genes (DEGs), including new (66.5%) and validated genes (e.g.,
34 FXYD2, SLC2A2, SYT1), and significant neuronal transmission and vitamin A metabolism
35 pathway alterations. Importantly, we demonstrate newly identified DEG roles in human β-cell
36 viability and/or insulin secretion and link 47 DEGs to diabetes-relevant phenotypes in knockout
37 mice, implicating them as potential causal islet dysfunction genes. Additionally, we nominate as
38 candidate T2D causal genes and therapeutic targets 27 DEGs for which T2D genetic risk
39 variants (GWAS SNPs) and pathophysiology (T2D vs. ND) exert concordant expression effects.
40 We provide this freely accessible atlas for data exploration, analysis, and hypothesis testing.
41 Together, this study provides new genomic resources for and insights into T2D pathophysiology
42 and human islet dysfunction.
43
44
45
46
47
48
2

bioRxiv preprint doi: https://doi.org/10.1101/2025.01.17.633590; this version posted January 22, 2025. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under a CC-BY-ND 4.0 International license.
49 Introduction
50 Pancreatic islets are primary mediators of type 2 diabetes (T2D) genetic risk and
51 pathophysiology, driving insulin secretion defects1,2,3. They comprise multiple cell types,
52 including insulin-secreting beta (β) cells, glucagon-secreting alpha (α) cells, somatostatin-
53 secreting delta (δ) cells, pancreatic polypeptide-secreting gamma (γ) cells and ghrelin-secreting
54 epsilon (ε) cells, that collectively determine islet functional output4. In humans, they are
55 intermingled throughout the islet, ensuring equal access to vasculature to sense and respond to
56 fluctuating glucose levels5. Growing evidence shows that α- and δ-cell signals regulate β-cell
57 function to ensure proper insulin secretion dynamics5. Robust assessment of islet cell type-
58 specific gene expression programs and their regulation in pathologic states is crucial to define
59 and understand pancreatic dysfunction in T2D. However, donor variability, modest sample size,
60 and/or a relatively small number of cells sampled per individual have limited power to detect
61 robust, reproducible differences6–10. To address this challenge, we completed single cell
62 transcriptome profiling and analysis of pancreatic islets obtained from a cohort of 48 non-
63 diabetic (ND), pre-diabetic (PD), and type 2 diabetic (T2D) donors. We identified robust T2D-
64 associated differences in islet cell type composition and gene expression and nominated 92 β-
65 cell differentially expressed genes (DEGs) for putative causal roles in islet dysfunction using
66 complementary experimental, physiologic, and genetic approaches and analyses.
67
68 Results
69 Comprehensive human islet single-cell transcriptome atlas spanning non-diabetic, pre-diabetic,
70 and type 2 diabetic states
71 To build a comprehensive, representative atlas of human islet transcriptomes, we
72 completed single cell RNA sequencing (scRNA-seq) in human pancreatic islets obtained
73 through the Integrated Islet Distribution Program (IIDP) from a diverse cohort of 48 American
74 cadaveric organ donors, representing European, Hispanic, and African American self-reported
75 ancestries and independent from those in the Human Pancreas Analysis Program (HPAP)6,11
76 (Supplementary Table 1). The cohort included 17 diagnosed T2D (mean HbA1c = 7.6%), 14
77 PD (mean HbA1c = 5.9%; designated based on American Diabetes Association (ADA)
≤ ≤
78 prediabetes criteria (5.7% HbA1c 6.4%)12), and 17 ND (mean HbA1c = 5.2%) donors
3

bioRxiv preprint doi: https://doi.org/10.1101/2025.01.17.633590; this version posted January 22, 2025. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under a CC-BY-ND 4.0 International license.
79 (Figure 1a). ND control donor samples were selected to be as similar as possible to the T2D
80 cases with respect to age, sex, BMI, and self-reported ancestry. HbA1c levels differed
81 significantly between groups, but age and BMI were similar (Figure 1b, Games-Howell post-hoc
82 test) and sex and ancestry distributions were comparable (Supplementary Table 1). Donor
83 islets were dissociated into single-cell suspensions, which were captured and sequenced to a
84 median sequencing depth of 13,400 UMIs using droplet-based scRNA-seq (10X Genomics). In
85 total, 245,878 cells passed stringent quality control (see Methods), with an average of 5,122
86 high quality single cells per donor (Supplementary Figures 1a and 1b and Supplementary
87 Table 2). After batch correction (Supplementary Figure 1c), unsupervised clustering based on
88 expression of the 2,000 most variable genes among these single cell transcriptomes identified
89 14 distinct cell types corresponding to endocrine (α, proliferating α, β, δ, γ, and ε), exocrine
90 (acinar and ductal), stellate/activated stellate, endothelial, glial (Schwann), and resident (mast)
91 and infiltrating immune cell types across ND, PD, and T2D donors (Figure 1c and
92 Supplementary Figure 2).
93 We defined robust signature genes—those specific to each islet cell type and detected
94 across donors irrespective of their glycemic status—by aggregating and comparing per-donor
95 single cell transcriptomes of individual cell types. In addition to classic hormone-encoding
96 marker genes such as INS, GCG, SST, PPY, and GHRL, we identified 270 α-, 272 β-, 173 δ-,
97 130 γ-, and 194 ε-cell signature genes exhibiting ≥ 8-fold expression differences at a false
98 discovery rate (FDR) <5% in one-vs-all ANOVA comparisons (Supplementary Figure 2;
99 Supplementary Table 3). Functional processes enriched among these signature genes
100 included G protein-coupled receptor signaling and amino acid transport (α-cells); insulin
101 secretion, regulation of membrane potential, and neuronal transmission (β-cells); gamma-
102 aminobutyric acid signaling/synaptic transmission and synapse assembly (δ-cells); G protein-
103 coupled receptor signaling, neuropeptide signaling and regulation of cation channel activity (γ-
104 cells); and regulation of lipoprotein lipase activity (ε-cells) (Supplementary Table 4). Examining
105 sex differences, we compared gene expression between males and females across all states
106 combined, identifying 112 α-, 64 β-, and 45 δ-cell DEGs by sex, 27 of which were shared across
107 these three cell types (Supplementary Table 5). 26/27 sex-specific DEGs were on X or Y
108 chromosomes (Supplementary Table 5) and were not significantly enriched for any common
109 processes or pathways.
110
4

bioRxiv preprint doi: https://doi.org/10.1101/2025.01.17.633590; this version posted January 22, 2025. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under a CC-BY-ND 4.0 International license.
111
112 Significant β-cell loss in T2D vs. PD, ND donors
113 After establishing the islet cell types and their robust expression signatures, we
114 assessed T2D-associated alterations in islet cell type composition by comparing cell type counts
115 obtained from each islet donor between ND, PD, and T2D states (Supplementary Table 6).
116 The distribution of each endocrine cell type relative to the total number of endocrine cells
117 confirmed substantial inter-donor heterogeneity within each state (Figure 1d)7,8,13. In T2D islets,
β
118 -cell/endocrine proportions were 13-15% lower (mean β-cell %=42.2±11.3) than those in ND
119 (mean β-cell %=55.2±10.7, p=0.006) or PD (mean β-cell %=57.2±12.9, p=0.002, Figure 1e,
120 ANOVA followed by Tukey's honest significance test) donor islets. α-cell proportions were
121 correspondingly higher in T2D islets (48.7±11.2% vs. 35.8±10.5% in ND (p=0.006) or vs.
122 35.7±13.6% in PD (p=0.009)). Relative proportions of δ- and γ-cells were similar between
123 groups.
124 A portion of the islets from 30/48 donors in this single-cell transcriptome cohort were
125 also characterized by the IIDP Human Islet Phenotyping Program (HIPP)
126 (https://iidp.coh.org/Resources-Offered/HIPP), which reported immunofluorescence-based
127 estimates of their islet cell type composition (Supplementary Table 6). Cell proportions
128 calculated from per-donor scRNA-seq profiles and HIPP for these samples were correlated
β
129 (Supplementary Figure 3; r=0.62 for ND, 0.70 for PD, and 0.73 for T2D for -cells, and r=0.65
130 for ND, 0.81 for PD, and 0.74 for T2D for α-cells), suggesting that the scRNA-seq-determined
131 cell proportion differences were not due to cell loss during sample processing or single cell
132 capture. Collective analysis of the full cohort revealed a significant inverse correlation between
β
133 reduced -cell proportions and elevated HbA1c levels (Figure 1f, Spearman’s r=-0.39;
β β
134 p=0.006), consistent with reported inverse associations between HOMA- (an index reflecting -
135 cell function) and HbA1c levels14, while α-cell expansion also correlated with elevated HbA1c
136 (Figure 1g, Spearman’s r=0.38; p=0.007).
137 Cell type-specific gene expression differences in T2D islets
138 Next, we sought to identify robust cell type-specific gene expression differences between
139 ND, PD, and T2D individuals by aggregating each individual’s scRNA-seq profiles per cell type
140 into “pseudobulk” gene expression profiles and comparing them (Methods). Surprisingly, we
5

bioRxiv preprint doi: https://doi.org/10.1101/2025.01.17.633590; this version posted January 22, 2025. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under a CC-BY-ND 4.0 International license.
141 identified only 3 α- (GGT6 and GALNT13 (T2D vs. ND); AC104770.1 (PD vs. ND)), 2 δ-
142 (TMEM190 (T2D vs. ND); CTRB1 (PD vs. ND)), and 6 γ- (MEG3, MEG8, LPO and CA2 (T2D
143 vs. ND); GAL and AKR1C3 (T2D vs. PD) cell-specific DEGs between the 3 glycemic states at
β
144 FDR< 5% (Supplementary Tables 7, 8 and 9). In striking contrast, we discovered 746 -cell
145 DEGs in T2D vs. ND donors at FDR<5% (Figure 2a and Supplementary Table 7),
β
146 approximately 10 times the number reported in recent HPAP cohort-based analyses6. 511 -cell
≥
147 DEGs exhibited a fold change (FC) 50% (i.e. log FC ±0.585), 316 or 195 of which were up- or
2
148 down-regulated, respectively. We replicated 171 T2D DEGs reported in previous whole islet or
149 cell type-specific studies6–9,15–21, including FXYD2, SLC2A2, SCN9A, PAX5, DGKB, IRS1 and
β
150 SYT1. Importantly, two-thirds of detected -cell DEGs were previously unreported (n=340;
151 Supplementary Figure 4a-d and Supplementary Table 10). Because sample sizes were
152 insufficient for meaningful analyses or interpretation, we did not assess sex-specific differences
153 in this cohort.
β
154 In the full cohort, the five T2D -cell protein-coding genes with the most significant FDR
155 were those with neuronal functions22, mediating central nervous system effects of therapeutic
156 agents (PDE4B) or acetyl-choline receptor aggregation in postsynaptic membranes (PHLDB2),
157 catalyzing proline conversion to the major excitatory neurotransmitter glutamate (OPLAH),
158 regulating postsynaptic neural circuit dynamics (ELFN1), or sensing calcium for
159 neurotransmitter release (SYT1). 4/5 DEGs (excluding PHLDB2) were detected in both male
β
160 and female T2D donors when analyzed separately. More broadly, 17.1% of T2D-upregulated -
161 cell genes were enriched for the biological term ‘neurogenesis’ (FDR p value, q = 6.0 ×10-18),
162 followed by ‘cell-cell signaling’ (q = 1.0 ×10-14), ‘cell adhesion’ (q = 5.1 ×10-12), and ‘regulation of
163 membrane potential’ (q = 1.7 ×10-11) (Figure 2b and Supplementary Table 11). More than 15%
β
164 of the newly identified T2D-upregulated -cell genes were associated with the cellular
β
165 component ‘synapse’ (q = 1.1 ×10-7). Conversely, downregulated T2D -cell genes were
166 enriched for the processes ‘regulation of hormone levels’ (q = 1.2 ×10-4), ‘lipid metabolism’ (q =
167 4.3 ×10-4), and ‘cell-cell signaling’ (q = 4.2 ×10-3, Figure 2c). Pathway enrichment analyses
168 (MSigDB, https://www.gsea-msigdb.org/gsea/msigdb) revealed 'neuroactive ligand-receptor
169 interaction' (q = 3.9 ×10-4) and 'vitamin A and carotenoid metabolism' (q = 1.5 ×10-3) as the
170 primary molecular pathways associated with the up- and downregulated DEGs, respectively
171 (Figure 2d and Supplementary Table 11).
6

bioRxiv preprint doi: https://doi.org/10.1101/2025.01.17.633590; this version posted January 22, 2025. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under a CC-BY-ND 4.0 International license.
172 The enriched neuroactive ligand-receptor interaction pathway included genes encoding
173 glutamate (GRIN1, GRIN2A), acetylcholine (CHRNA3, CHRNA5), and norepinephrine (ADRB1)
174 neurotransmitter receptors; neuroendocrine peptides (GRP, GAL); ATP receptors (P2RY1,
175 P2RX5); receptors for hormones with known insulin suppressive effects (GHSR, TSHR); and a
176 ligand-gated ion channel (GLRA3) (Figure 2e and Supplementary Figure 5a). Pancreatic islets
177 are densely innervated by autonomic nerves23, and the preganglionic sympathetic and
178 parasympathetic neurons innervating islets primarily release acetylcholine24. Additionally,
179 postganglionic sympathetic neurons release norepinephrine, glutamate, and galanin (encoded
180 by GAL) while postganglionic parasympathetic neuron fibers release gastric releasing peptide
181 (encoded by GRP)26. Earlier studies in nerve stimulation have demonstrated the ability of neural
182 signals to override the effects of circulating glucose25,26. Individuals with T2D exhibit increased
183 islet innervation, possibly as a compensatory mechanism by which the nervous system tries to
184 preserve or augment islet function under metabolic stress23. Presence of multiple
β
185 neuroreceptors on -cells indicate that they can directly sense and respond to neural signals.
β
186 Altered expression of these neuroreceptors or neuropeptides within -cells from individuals with
187 T2D suggests disrupted neuroendocrine regulation of insulin secretion as a pathophysiologic
188 aspect of pancreatic dysfunction that is not yet fully understood in T2D. In addition, our data
189 highlight underappreciated roles for aberrant purinergic signaling, involving upregulated ATP
190 receptor genes (P2RY1, P2RX5), in islet dysfunction and T2D. Notably, insulin secretory
191 vesicles contain ATP and ADP molecules, which are co-released with insulin during glucose-
192 stimulated exocytosis27. These secreted purine adenosines act as extracellular signaling
β
193 mediators that activate two types of purinergic P2 receptors on the -cell membrane—P2X
194 (ligand-gated cation channels) and P2Y (G-protein coupled channels)—whose autocrine effects
β
195 amplify glucose-induced calcium [Ca2+] responses in -cells28.
196 Downregulation of multiple genes encoding key proteins in vitamin A metabolism—
β
197 retinol dehydrogenases (RDH10, RDH12), -carotene oxygenase (BCO1, which generates the
β
198 vitamin A precursor, -carotene), and cellular retinoic acid binding proteins (CRABP1 and
199 CRABP2) (Supplementary Figure 5b)—was another hallmark of T2D β-cells. Vitamin A
200 metabolites (retinoic acid, RA) regulate gene expression by activating transcription factors (e.g.,
201 HNF4A, retinoid A receptor nuclear receptor (RAR)) that bind to RA-response elements in target
202 genes. Dietary deficiency of vitamin A has been linked with hyperglycemia, mirroring reduced
203 vitamin A levels in the pancreas29. Retinoids are regulators of apoptosis30,31, and vitamin A
β
204 deprivation has been shown to decrease -cell mass29. To test the apoptotic impact of
7

bioRxiv preprint doi: https://doi.org/10.1101/2025.01.17.633590; this version posted January 22, 2025. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under a CC-BY-ND 4.0 International license.
205 compromised vitamin A metabolism in T2D, we investigated the expression of 1,159 genes
206 encoding proteins associated with cell death in the human protein atlas (HPA,
β
207 https://www.proteinatlas.org)32. T2D vs ND -cells exhibited differential expression of several of
208 these genes including induction of FAIM2, NUPR1, GAS6, HGF, and RAMP3 and reduction of
209 ARG2 and NEDD9, none of which were modulated in T2D α-cells (Figure 2f). Many of these
210 genes harbor RA response elements (Supplementary Figure 6) and are anti-apoptotic, which
β
211 suggests a compensatory response to vitamin A deficiency and related increase in -cell
212 apoptosis.
β β
213 T2D -cell DEGs included multiple genes not previously linked to islet -cell dysfunction
214 or T2D. We selected a subset of these new causal candidates for functional validation based
215 on their suspected roles in T2D and informed by their general cellular functions. Specifically, we
216 targeted MPP1, CD82, GLUL, and GOLT1A (4/10 most downregulated genes), STON2 (an
217 adaptor protein involved in recycling synaptic vesicles for neurotransmission22), and FBXO17 (a
218 regulator of Akt signaling pathway22). To evaluate their role in insulin secretion, we completed
219 shRNA knockdown and assessed effects on glucose-stimulated insulin secretion (GSIS) assays
β β
220 in human EndoC- H3 -cells. Compared to non-targeting (NT) shRNA control cells, knockdown
221 of all targets altered basal insulin secretion, GSIS, or both. MPP1 and GLUL knockdown
222 increased basal insulin secretion (Figure 2g and Supplementary Figure 7), a feature
223 associated with islet dysfunction in T2D33. When stimulated with 20mM glucose, MPP1, CD82,
224 STON2, and FBXO17 knockdown cells exhibited blunted insulin secretory responses.
225 Assessment of the stimulation index revealed impaired GSIS for all 6 genes following
226 knockdown (Figure 2h). Furthermore, Annexin V/7-AAD staining indicated that GLUL and
227 FBXO17 knockdown markedly and modestly decreased cell viability, respectively, with
228 consequent increases in early apoptotic, late apoptotic, and necrotic cells relative to shControl
229 cells (Figure 2i). GLUL encodes glutamine synthetase, which catalyzes conversion of glutamate
230 and ammonia to glutamine. Matschinksy and colleagues previously demonstrated roles for
231 glutamine in both amino acid- and GSIS34, but GLUL has not been directly linked to T2D.
232 Elevated plasma glutamate levels and lower plasma glutamine levels associate with increased
233 T2D incidence35, and GLUL uniquely executes their biochemical conversion22. Considering its
234 pivotal role in these metabolic pathways and the evidence from previous studies, investigating
235 GLUL as a potential target in T2D research holds considerable promise.
236 Convergent T2D genetic and pathophysiologic effects on expression nominate T2D causal
237 genes
8

bioRxiv preprint doi: https://doi.org/10.1101/2025.01.17.633590; this version posted January 22, 2025. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under a CC-BY-ND 4.0 International license.
238 In addition to directly testing selected DEG effects on human beta-cell viability and
239 function, we sought to nominate additional DEGs contributing to, rather than a consequence of,
240 T2D physiology based on links to glucose homeostasis and T2D genetics. Interestingly, genes
241 harboring inactivating monogenic diabetes mutations, such as HNF1A, HNF4A, and SLC2A236,
β
242 were significantly downregulated in T2D donor -cells (Figure 2e). Given these concordant
β
243 down-regulation/loss-of-function effects, we sought to identify T2D -cell DEGs for which T2D-
244 associated risk alleles exerted concordant gene expression effects. We compiled a list of 39,972
245 T2D-associated index and linked proxy genetic variants (all-ancestry or ancestry-specific LD
≥
246 r2 0.80 in 1000Genomes Phase 3 data) reported in genome-wide association study (GWAS)
247 meta-analyses from T2DGGI37, DIAMANTE38, MVP39, and AGEN40 (Supplementary Table 12).
248 We queried islet expression QTL association results (p < 0.05) from the TIGER consortium41
249 and identified 461 T2D variants (representing 41 loci) associated with altered islet expression of
β
250 25 upregulated and 16 downregulated genes in T2D -cells. T2D genetic and environmental
251 effects were concordant (i.e., T2D risk allele altered islet gene expression in the same direction
β
252 as T2D vs. ND -cell differential expression) for 27 genes (Figure 3a, red and blue;
253 Supplementary Table 13), including DGKB, ST6GAL1, and STARD10 reported as colocalized
254 T2D genetic and islet eQTL association signals showing directionally consistent impact on gene
255 expression41,42,43.
β
256 For nineteen T2D -cell DEGs, we identified a single T2D GWAS variant for which the
257 T2D risk allele altered expression in the same direction. For example, the T2D risk allele ‘C’ of
258 intergenic variant rs35825770 (OR = 1.02, p = 3.5 ×10-11)37 in the LINC00917–FOXF1 locus is
259 an islet eQTL associated with elevated expression of FOXF1 (Z-score = 2.12, p = 0.03)41 and its
260 neighboring gene FOXC2 (Z-score = 2.01, p = 0.04)41. We identified >20-fold higher FOXF1
β
261 expression in T2D vs. ND -cells (log FC = 4.38, q = 3.5 ×10-8) with no significant difference in
2
262 FOXC2 expression (log FC = -0.72, q = 0.74), supporting a causal and concordant role for
2
263 FOXF1 induction in T2D genetics and pathophysiology. Similarly, rs67897819 T2D risk allele ‘A’
264 (OR = 1.07, p = 1.7 ×10-68)37, upstream of HNF4A, is associated with decreased expression of
265 SGK2, a serum and glucocorticoid inducible kinase gene 800 kb upstream of HNF4A (Z-score =
266 -2.02, p = 0.04)41, but not HNF4A itself (Z-score = -0.46, p = 0.65)41. Consistent with the T2D
β
267 risk allele effects on SGK2 expression, it was also reduced in T2D vs. ND -cells (log FC = -
2
268 1.36, q = 8.5 ×10-4), which was a stronger difference than HNF4A expression (log FC = -1.01, q
2
269 = 0.04). Expression of neighboring genes (±500kb of rs67897819) did not differ significantly
β
270 between T2D and ND -cells (TOX2, OSER1, GDAP1L1, FITM2, TTPAL, SERINC3, PKIG,
9

bioRxiv preprint doi: https://doi.org/10.1101/2025.01.17.633590; this version posted January 22, 2025. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under a CC-BY-ND 4.0 International license.
271 ADA and KCNK15), highlighting SGK2 as a candidate T2D genetic and pathophysiologic
272 causal/effector gene in this region. SGKs, alongside AKT, are activated downstream of
β
273 mTORC2 (a regulator of -cell mass) in response to insulin and phosphorylate bona-fide AKT
274 target FOXO144, which serves as an anti-apoptotic signal45. SGK2 is a pancreas, liver, and
275 kidney-restricted isoform46 that is linked to PD-L1 signaling47 and inhibits ferroptosis48. Thus,
β
276 diminished SGK2 expression in T2D -cells may contribute to aberrant activation of multiple cell
277 death pathways. This approach also nominated RASGRP1 and KCNH6 as candidate causal
278 genes whose reduced expression contribute to T2D genetic risk and/or pathophysiology by
β
279 increasing -cell susceptibility to pathophysiologic stress and/or enhancing apoptosis
β
280 propensity. Apoptosis is elevated in RASGRP1-/- human embryonic stem cell-derived -cells49,
β
281 and Kcnh6-/- mice exhibit increased -cell ER stress, calcium handling defects, and apoptosis
282 that manifests as impaired glucose tolerance50. KCNH6 mutations have been identified in
283 hypoinsulinemic/hyperglycemic patients51, and the KCNH6-targeting compound berberine has
284 been shown to stimulate insulin secretion52. Mere detection of shared or colocalized eQTL- and
285 T2D-associated variants in non-diabetic islets does not confirm the candidate causal/effector
286 gene's involvement in mediating T2D predisposition or its functional role. However, our
β
287 investigation into gene expression differences in T2D -cells provides complementary evidence
288 supporting roles for these putative T2D causal/effector genes in T2D pathophysiology.
289 Moreover, previous studies for some of the genes identified in these analyses, such as KCNH6,
290 support the provocative hypothesis that these genes represent key actors in islet dysfunction
291 with druggable therapeutic potential50,52.
292 Eight DEGs (FXYD2, RPL39L, DLK2, ITGA1, P2RX5, PITPNM2, HNF1A-AS1, and LTA;
293 Figure 3a, blue) were linked to independent T2D association signals with both concordant and
294 discordant expression effects. For example, rs28413626 T2D risk allele ‘A’ (OR = 1.03, p = 2.1
295 ×10-18)37 was associated with higher expression of PITPNM2 (a membrane-associated
296 phosphatidylinositol transfer protein involved in insulin secretion)53 in whole islets (Z-score = 2.1,
297 p = 0.04)41, while rs1260294 T2D risk allele ‘T’ (OR = 1.04, p = 2.2 ×10-15)39, distinct from
298 rs28413626 (LD r2 = 0.28, all ancestries combined)54 was associated with lower islet PITPNM2
β
299 expression (Z-score = -2.18, p = 0.03)41. In T2D -cells, PITPNM2 expression was reduced
β
300 compared to ND -cells (log FC = -0.72, q = 0.004). Such counteracting signals may reside in
2
301 distinct regulatory elements within a gene, such as promoters, enhancers or silencers which
302 modulate its expression in diverse ways and lead to opposing effects on gene expression.
10

bioRxiv preprint doi: https://doi.org/10.1101/2025.01.17.633590; this version posted January 22, 2025. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under a CC-BY-ND 4.0 International license.
303 We also identified 14 genes, including GRP, SIX6, SCN3A, ADRB1, and others, whose
304 altered expression was significantly associated with both T2D genetic and pathophysiologic
305 differences but in opposite directions (Figure 3a, gray). For example, rs1895701 T2D risk allele
306 ‘C’ (OR = 1.03, p = 2.4 ×10-17)37 located between GALNT3 (upstream) and CSRNP3, SCN2A
307 and SCN3A (downstream) was associated with lower whole islet GALNT3 expression (Z-score
308 = -3.62, p = 2.9 ×10-4)41, SCN3A (Z-score = -2.77, p = 0.006)41 and SCN2A (Z-score = -2.46, p =
β
309 0.01)41. However, T2D -cells showed elevated SCN3A expression (a sodium voltage-gated
310 channel22, log FC = 0.96, q = 3.4 ×10-5) and modestly increased SCN2A expression (log FC =
2 2
311 0.49, q = 0.04), but no difference in GALNT3 (log FC = 0.02, q = 0.97) or CSRNP3 (log FC =
2 2
312 0.07, q = 0.83) expression. This suggests that eQTL associations for such genes exhibiting
313 ‘opposite effects in different tissues’ may be dynamic and context-dependent, potentially
314 switching with the onset of T2D. Indeed, similar context-specific eQTL dynamics have been
315 observed during cell differentiation55. Alternatively, this divergent pattern of effects could imply
β
316 that -cells, the primary focus of our analysis, may not be the major or exclusive cell type
317 contributing to these eQTL effects. Given that TIGER eQTL associations were detected in whole
318 islet RNA-seq, which represents composite expression from multiple cell types, these genetic
β
319 variants may exert significant influence in other non- islet cell types. Opposite eQTL effects
320 between closely related tissues are relatively common52. Single-cell dissection of islet cell type-
321 specific regulation (caQTL) and expression (eQTL) should help to resolve these questions and
322 possibilities.
323 In addition to establishing T2D genetic-pathophysiologic links to identify high priority
β
324 candidates, we evaluated protein levels of T2D -cell DEGs from a recent T2D vs. ND human
β
325 islet proteomic study56. We identified 21 genes with concordant differences in both the -cell
326 mRNA and islet protein levels in T2D vs. ND donors (Figure 3b), including a subset with causal
327 links to islet dysfunction and T2D. For example, concordantly T2D-upregulated SEPT9 gene
β
328 (and protein) disrupted insulin secretion when overexpressed in rat INS-1(832/13) -cells57, and
329 Cystic Fibrosis transmembrane conductance regulator (CFTR) regulates glucose-dependent
β
330 electrical activities in -cells58. T2D-downregulated gene/protein ARG2, a manganese
β
331 metalloenzyme, has been linked with polyamine synthesis and regulation of -cell function59,
332 and recent multi-ancestry studies linked rs11114650 T2D risk allele to decreased LIN7A
333 expression60. Finally, these data support concordant genetic-pathophysiologic effects (Figure
β
334 3a) implicating reduced PITPNM2 expression and protein levels in islet -cell dysfunction and
β
335 failure. Furthermore, GRAMD2B, a downregulated T2D -cell gene (q = 7.2 ×10-6), was also
11

bioRxiv preprint doi: https://doi.org/10.1101/2025.01.17.633590; this version posted January 22, 2025. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under a CC-BY-ND 4.0 International license.
336 down-regulated at the protein level in T2D islets. GRAMD family proteins are ER-plasma
337 membrane contact site proteins that regulate intracellular Ca2+ dynamics61. Downregulation of
β β
338 GRAMD2B in T2D -cells likely causes disruption of Ca2+ signaling, compromising -cell
339 function in T2D. Although GRAMD2B has not been directly linked with T2D previously, it was
340 identified as a DEG in T2D islets15.
β
341 To link promising -cell DEGs to (patho)physiologic effects, we explored diabetes-
342 relevant phenotypes from the International Mouse Phenotyping Consortium (IMPC)62, which
343 aims to characterize the function of every protein-coding gene in the mouse genome through
344 whole body gene knock out (KO) mouse lines. 198/511 DEGs identified were tested by IMPC.
345 Homozygous KO of 35 DEGs in mice caused prenatal lethality (n=22) or sub-lethal fitness
346 phenotypes (n=13), highlighting their roles in essential cell survival processes (Supplementary
347 Table 14). Importantly, germline deletion of 13 additional DEGs resulted in glycemic defects
348 characteristic of T2D etiology (Figure 3c, Supplementary Table 14). To evaluate the
349 effectiveness of mouse KO models in assessing the functional significance of T2D DEGs, we
350 investigated the loss of well-established T2D genes, Abcc8 and Kcnj11, which showed
351 significant glucose tolerance impairment (Figure 3d). Among the identified DEGs, BNIP3, a
352 mitochondrial protein originally characterized as an apoptosis inducer63, was downregulated in
β
353 T2D -cells (q = 0.004, a newly identified DEGs) and Bnip3-/- mice exhibit impaired glucose
354 tolerance (p = 4 ×10-9, Figure 3d)62 and increased circulating insulin levels (p = 2 ×10-7)62
355 compared to wild-type mice. BNIP3 has a dual role in cell fate regulation, balancing between
356 cell death and survival. Notably, during cellular stress (e.g., hypoxia), BNIP3 preserves
357 mitochondrial functional integrity by removing damaged mitochondria via autophagy/mitophagy,
358 thereby protecting cells from death64. Loss of BNIP3 expression in T2D implies that disruption of
359 BNIP3’s stress-responsive adaptation may impair cellular homeostasis. KO of SLITRK1,
β
360 another newly identified T2D upregulated -cell DEG (q = 0.006) improved glucose tolerance in
361 mice (p = 2.2 ×10-6, Figure 3d)62. SLITRK1 is a neuronal transmembrane protein linked to
362 neurological diseases such as schizophrenia65 and Tourette’s syndrome66 and promotes
363 excitatory synapse formation when overexpressed in cultured rat hippocampal neurons67. Its
β
364 upregulation in T2D connects -cell dysfunction to an altered islet-nerve communication which
365 is critical in fine-tuning insulin secretion in response to circulating glucose levels. GRAMD2B, a
β
366 downregulated mRNA/protein in human T2D -cells/islets is crucial for glucose hemostasis, as
367 Gramd2b-/- mice exhibit impaired glucose tolerance (p = 2.3 ×10-5, Figure 3d)62. Thus, our
368 integration of mouse physiologic data provided insights into in vivo gene functions and systemic
12

bioRxiv preprint doi: https://doi.org/10.1101/2025.01.17.633590; this version posted January 22, 2025. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under a CC-BY-ND 4.0 International license.
369 (patho)physiologic effects of identified DEGs, enabling identification of previously unrecognized
370 genes with crucial roles in T2D physiology as promising therapeutic targets.
β
371 T2D-associated differences in putative islet -cell subpopulations
372 Single-cell and targeted islet analyses have reinvigorated the interests in and debates
373 around models in which (patho)physiologic states such as T2D are characterized by molecularly
374 and functionally distinct endocrine cell subpopulations or states with variable maturity, stress,
375 hormone secretion and glucose responsiveness68,69,70,71,72. Thus, we sought to identify robust,
376 reproducible endocrine cell subpopulations present in our 48-donor cohort and assess if they
β
377 are significantly altered in T2D, PD, or ND states. We analyzed 74,812 α-, 99,029 -, and
378 10,770 δ- cells from T2D, PD and ND islets and identified seven putative α- and δ-cell
β
379 subpopulations and eight -cell subpopulations (Supplementary Table 15 and Figure 4a,
β
380 Supplementary Figures 8a-d and 9a-d). All -cell subpopulations expressed INS at
β
381 comparable levels confirming their -cell identity, with no variation in clustering between sexes,
382 ancestries or sequencing chemistries (Supplementary Figure 10a-c). Each cell type
383 subpopulation was detected in every donor across the three glycemic states (Figure 4b and
384 Supplementary Table 15). Within each pancreatic islet endocrine cell type, we observed
385 subpopulations with endoplasmic reticulum (ER) stress and/or hypoxia (a critical ER stressor)
β
386 response gene expression signatures: clusters 7 and 2 (α), clusters 6 and 2 ( ) and, cluster 4
387 (δ) (Supplementary Table 15, Figure 4c, Supplementary Figures 8e and 9e), implying a
β
388 broad role of ER homeostasis perturbations or cycles in multiple islet cell types73, not just -
β
389 cells. Indeed, ER stressed -cells with elevated DDIT3, HSPA5, HERPUD1, and TRIB3
390 expression have been previously documented (Supplementary Figure 10d)74,75,76. Additionally,
β
391 we detected a putative -cell subpopulation with high functional capacity and/or output
392 exhibiting elevated expression of genes enriched in the ‘insulin secretion’ pathway that harbor a
393 spectrum of diabetes-associated sequence variation – ABCC8, G6PC2, PDX1, SLC30A8, RBP4
β
394 (cluster 1). We also identified -cell clusters with expression signatures associated with
395 translation initiation (cluster 3); heat shock proteins (cluster 4, proliferative vs. mature cells with
396 elevated CFAP126 (Fltp in mice) expression77); regulation of signaling receptor activity (cluster
397 5, CD63hi cells with enhanced glucose-stimulated insulin secretion78); cellular senescence (e.g.,
398 CDKN2A, CDKN2B, PLK2, B2M expression, cluster 7); and cellular transport (cluster 8, also
399 found in α and δ cells) (Supplementary Table 15).
13

bioRxiv preprint doi: https://doi.org/10.1101/2025.01.17.633590; this version posted January 22, 2025. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under a CC-BY-ND 4.0 International license.
400 α- and δ-cell sub-clusters showed no significant difference between T2D, PD, or ND
β
401 donors (Supplementary Figures 8f and 9f). Although no -cell subpopulations were uniquely
402 present or absent in T2D donor islets, two exhibited significant reciprocal quantitative
403 differences in their relative abundance between T2D vs. ND or PD donors (Figure 4d and 4e).
404 The putative high-functioning, ‘insulin-secreting’ cluster 1 population proportions were reduced
β
405 an average of 10.5% in T2D vs. ND -cells (p = 0.001), underscoring the potential importance of
406 this sub-population for proper islet function and/or its enhanced sensitivity to pathophysiologic
407 changes. In contrast, the proportion of ‘cellular senescence’ cluster 7 cells increased by an
β
408 average of 12.3% in T2D vs ND -cells (p = 0.009); this significant increase was also observed
β
409 in T2D vs. PD -cells (p = 0.02, average increase = 9.7%). These unsupervised subpopulation
β
410 analyses thus support emerging reports of increased -cell senescence in T2D79,80,81. Together,
β
411 these subpopulation shifts combine with 10-15% overall reductions in T2D donor -cell
β
412 numbers/proportions in this cohort (Figure 1e) to result in ~25-30% reduction of functional -cell
413 mass.
414 Discussion
415 Here, we report comprehensive profiling and comparative analyses of approximately a
416 quarter million human islet single-cell transcriptomes from a unique, HPAP-independent 48-
417 donor cohort representing ND, PD, and T2D states. These studies revealed significant T2D-
β
418 associated changes in -cell (sub)populations that collectively manifest as ~25-30% reductions
β
419 in functional -cell mass compared to ND or PD islet donors. Moreover, we identify 511 genes
β
420 whose expression is perturbed in T2D -cells. T2D genetic and pathophysiologic factors exert
β
421 convergent and concordant effects on their expression for 58 of these T2D -cell DEGs,
422 nominating them as high priority candidate causal and putative interventional target genes. We
423 provide these human islet single cell transcriptomic data as an accessible resource to the islet
424 biology and diabetes research communities in two formats – the free-to-use CellxGene
425 (https://cellxgene.cziscience.com/collections/58e85c2f-d52e-4c19-8393-b854b84d516e)
426 platform for investigating and retrieving gene expression signatures across various islet cell
427 types in the context of T2D and the Transcriptome Atlas of Pancreatic Islet Cells (TAPIC;
428 https://thejacksonlaboratory.shinyapps.io/TAPIC_Stitzel_Lab/) R shiny app we created for data
429 visualization – to enhance exploration and integration of this comprehensive and disease-
430 relevant islet transcriptome atlas.
14

bioRxiv preprint doi: https://doi.org/10.1101/2025.01.17.633590; this version posted January 22, 2025. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under a CC-BY-ND 4.0 International license.
431 This study significantly advances ongoing efforts aimed at important and widely
432 editorialized gaps in our collective ability to identify reproducible “T2D genes” in human islets.
β
433 We applied a pseudobulk analysis approach to identify 746 T2D -cell DEGs at FDR<5%, 511
434 of which differed >1.5-fold in expression. One-third of these 511 robust T2D DEGs have been
435 reported in previous studies, including those such as DGKB, ASCL2, GOLT1A, ARG2,
β
436 PPP1R1A, and others reported as islet and/or -cell T2D DEGs in HPAP and independent
437 cohort studies. Thus, continued efforts and increasing sample sizes are homing in on an ever-
438 increasing set of high-confidence T2D-associated DEGs as anticipated. Systematic efforts to
439 collect and uniformly process, QC, and analyze all human islet single cell profiles, such as those
440 of the newly established Pancreas Knowledgebase (PanKBase), should build on this
441 momentum and enhance our multi-omic understanding of islet cell type-specific (dys)function.
442 Neuroreceptor signaling and vitamin A metabolism emerged among the most significant
443 up- and down-regulated pathways/processes among DEGs, suggesting substantive alterations
β
444 in both neuroactive ligand receptor signaling and metabolism in T2D -cells. Although both have
445 been linked to islet development and function by targeted studies in model systems, the gene-
446 based enrichments detected here uniquely highlight their empiric links to human islet pathology
447 and T2D. Cnop and Pipeleers noted two decades ago the protective effects of vitamin A vs.
β
448 LDL-induced toxicity in rat islet -cells82. Chemical screens and mechanistic studies in zebrafish
449 added retinoic acid biosynthesis and signaling alongside Notch as important contributors to islet
β
450 differentiation and -cell regeneration83–85. Subsequent rodent studies demonstrated that vitamin
β
451 A deficiency increased -cell apoptosis, increased α−cell mass and hyperglucagonemia86, while
452 dominant negative-negative RAR-α inhibition led to age-dependent decreases in plasma insulin
β β
453 resulting from impaired GSIS, decreased -cell mass and per- -cell insulin content87.
454 Expression of genes encoding several neurotransmitter receptors - adrenergic (ADRB1),
455 glutaminergic (GRIN1, GRIN2A), cholinergic (CHRNA3, CHRNA5), purinergic (P2RY1, P2RX5),
456 serotonin (SSTR1), GABAergic (GABRA2), and glycine (GLRA1, GLRA3) - were altered in T2D
β β
457 -cells. -cell function is tightly controlled by the autonomic nervous system88,89 and
458 neurotransmitters, whether synthesized locally within the islet or released by the neurons, are
459 crucial for regulating insulin secretion. Glutamate, for instance, is an excitatory neurotransmitter
460 that signals through N-methyl-D-aspartate receptors (NMDARs), which are ligand-gated cation
β
461 channels with high calcium permeability encoded by GRIN genes22. -cell-specific deletion of
462 Grin1 reveal enhanced GSIS and improved glucose tolerance in mutant mice90. In humans,
463 treatment with the NMDAR antagonist dextromethorphan (DXM) increases serum insulin levels
15

bioRxiv preprint doi: https://doi.org/10.1101/2025.01.17.633590; this version posted January 22, 2025. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under a CC-BY-ND 4.0 International license.
464 and improves glucose tolerance in individuals with T2D90; pancreatic NMDARs are therefore
465 being evaluated as promising therapeutic targets for diabetes management. Furthermore,
β
466 gamma-aminobutyric acid (GABA) is simultaneously released with insulin by -cells and binds
β
467 -cells GABAA receptors to inhibit insulin secretion as an autocrine signal91. GABRA2 encodes
β
468 the exclusive GABAA receptor of human -cells92 and has been reported to feature relatively
469 closed chromatin conformation in T2D islets compared to non-diabetic islets93. Neurotransmitter
470 receptor dysfunction in T2D islets has been discussed before94. Given their critical involvement
β
471 in -cell signaling and insulin secretion, these neuroreceptor genes, which are currently under-
472 studied in the context of diabetes, warrant further exploration.
473 Using a combination of genetic and comparative analyses along with experimental
β
474 approaches, we nominated 92 T2D -cell DEGs as prioritized candidate causal T2D genes (44
475 reported and 48 newly identified). This prioritized list includes genes with long-standing gain- vs.
476 loss-of-function T2D GWAS variant effects on islet gene expression (DGKB, ST6GAL1 vs.
477 STARD10) and exciting new candidates that span the variant-to-function gamut like KCNH6 and
β
478 capture concordant multi-study, multi-modal effects, such as GRAMD2B. Several T2D -cell
479 DEGs exhibit diabetes-relevant glucose homeostasis phenotypes in knockout mice that are
480 directionally consistent with their dysregulation in T2D vs. ND islets, such that germline
481 knockout of up- or down-regulated genes improve (e.g. SLITRK1, IRF8) or impair (e.g.,
482 GRAMD2B, BNIP3) glucose homeostasis, respectively. Systematic and targeted mechanistic
β
483 studies of these prioritized genes in primary human islets and using -cell-specific knockouts
484 are warranted and will firmly establish their causal roles in islet dysfunction and T2D.
β
485 Although we identified robust and extensive gene expression changes in T2D -cells, we
486 detected surprisingly minimal-to-negligible alterations in T2D islet α− or δ-cells. Our comparative
β
487 analyses and experimental validation support these T2D -cell DEGs as compelling causal
488 candidates. Although the biological vs. potential technical basis for the surprising lack of
489 differences in the other cell types is unclear, it is noteworthy that this apparent conundrum was
490 also observed in recent independent, HPAP cohort-based analyses6. All donor islets in this
491 study were handled and processed using standardized protocols after overnight recovery from
492 shipping and islet cell types were captured in parallel with comparable sequencing depth, so it is
493 unlikely this discrepancy results from capture or sequencing bias in the platform. Despite best
494 efforts to match donor characteristics, these experiments and analyses involve ex vivo islets
495 from donors with inherently variable lifestyles and environments. It is possible that 5.5 mM
496 glucose concentrations in standard culture conditions may provide stimulation or stress that
16

bioRxiv preprint doi: https://doi.org/10.1101/2025.01.17.633590; this version posted January 22, 2025. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under a CC-BY-ND 4.0 International license.
β
497 “unmasks” the -cell differences and deficiencies observed but not those in other cell types. For
498 example, α-cells respond to low (0mM) glucose and amino acids, so islets may need to be
499 cultured in these conditions to “unmask” α-cell deficiencies in T2D islets. Future studies
500 comparing T2D vs. ND islet cell differences with cell type-specific stimuli/stressors will be
β
501 important to test this hypothesis and could enhance our understanding of non- -cell
502 contributions to islet dysfunction in T2D.
503 Unsupervised analyses of single cell transcriptomes for each islet cell type identified
β
504 multiple putative -cell subpopulations, present in every donor of this cohort, including several
505 previously described72,74–78,95,96. We confirm and extend to α− or δ-cells the widely reported ER
β
506 stress signature -cell sub-populations described in multiple reports97–99, perhaps reflecting
507 more generalizable cycles of hormone production and secretion, and identify reported
508 subpopulations with elevated CD6378 and CFAP126 (the human Fltp orthologue)77 expression.
509 However, the abundance/proportions of these subpopulations did not differ between T2D and
510 ND or PD individuals, suggesting that they may contribute to physiologic rather than pathologic
β β
511 -cell heterogeneity. In contrast, we detected significant T2D-associated increases in -cells
512 exhibiting an elevated senescence signature gene expression signature. Senescence has been
β
513 recently implicated as a (mal)adaptive -cell process in both type 1100 and type 2 diabetes101,102;
514 changes in this putative subpopulation may underlie reported intra-individual heterogeneity in
β
515 CDKN2A expression and nearby chromatin accessibility in T2D -cells from recent trajectory-
β
516 based analyses of a smaller cohort8. Mechanistic studies of this putative T2D-associated -cell
517 subpopulation and the effects of senolytic vs. senomorphic agents on T2D islet function are
518 warranted to determine and discern their helpful vs. harmful role(s). More broadly, spatial, in
519 situ-based approaches will be critical to assess and compare within- vs. between-islet
520 organization of these putative subpopulations, and their effects on islet function, in distinct
521 regions of the pancreas (e.g., head, neck, body, tail) or healthy vs. diabetic individuals.
522 Funding
523 This study was made possible by generous funding from the American Diabetes Association
524 Pathway to Stop Diabetes Accelerator Award (1-18-ACE-015) and National Institutes of Health
525 (NIH) award number R01DK118011 (to M.L.S) as well as Department of Defense
526 Congressionally Directed Medical Research Program (CDMRP) award number W81XWH-18-
527 0401 (to M.L.S. and D.U.). C.N.S. was also supported by American Diabetes Association grant
528 11-22-JDFPM-06. Opinions, interpretations, conclusions, and recommendations are solely the
529 responsibility of the authors and do not necessarily represent the official views of ADA, NIH, or
17

bioRxiv preprint doi: https://doi.org/10.1101/2025.01.17.633590; this version posted January 22, 2025. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under a CC-BY-ND 4.0 International license.
530 DOD. We gratefully acknowledge contributions of JAX Single Cell Biology and Genome
531 Technologies services and Research Cyberinfrastructure computational resources at The
532 Jackson Laboratory for expert assistance with the work described in this publication. We are
533 indebted to the anonymous islet organ donors and their family, which were provided by the
534 NIDDK-funded Integrated Islet Distribution Program (IIDP) (RRID:SCR_014387) at City of Hope
535 (2UC4DK098085). Special thanks to Dr. Raphael Scharfmann at Institute Cochin for help
β
536 optimizing EndoC- H3 culture. We thank Ucar and Stitzel lab members for critical feedback
537 throughout this study.
538
539 Data and Code Availability:
540 All human islet sample and single cell RNA-seq datasets have been deposited in the BioProject
541 and Gene Expression Omnibus databases under accession numbers PRJNA913127 and
542 GSE221156. The data have been processed in the R statistical package and the analytical
543 pipeline including the detailed methodology, the code and the associated plots/tables are
544 available at Zenodo under https://zenodo.org/records/14656366. The reader can use our code
545 outlined in the Pipeline_html.Rmd and Pipeline_html.html files to replicate the results and to
546 explore other aspects of our data discussed in detail in the manuscript.
547
548 At the single-cell level, the processed data are available for interactive visualization
549 by cellxgene at https://cellxgene.cziscience.com/collections/58e85c2f-d52e-4c19-8393-
550 b854b84d516e. The dataset is divided into four instances, one referring to the data of all
551 annotated cells and one for each of the major identified cell types, namely Beta, Alpha and Delta
552 cells. At the pseudobulk level, processed data are available for interactive visualization by the
553 TAPIC Rshiny applet at https://thejacksonlaboratory.shinyapps.io/TAPIC_Stitzel_Lab/.
554
555 Conflict of interests
556 The authors declare no competing interests.
557
558 Methods
559 Single cell library preparation and sequencing
18

bioRxiv preprint doi: https://doi.org/10.1101/2025.01.17.633590; this version posted January 22, 2025. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under a CC-BY-ND 4.0 International license.
560 Pancreatic islets from 48 individuals consisting of 17 ND, 17 T2D and 14 PD donors were
561 cultured using CMRL, supplemented with 10% FBS, 1% Glutamax,1% Pen/Strep for 14 days.
562 Islet-derived fibroblasts were harvested and gDNA extracted using the Blood & Tissue kit
563 (Qiagen). The RNAse A (Qiagen) treated genomic DNA samples were genotyped using the
564 Infinium Global Diversity Array-8 v1.0 Kit (Illumina). Single cell capture, barcoding, and library
565 preparation were performed using the 10X Chromium platform (https://www.10xgenomics.com)
566 according to the manufacturer’s protocol for chemistries v2 (#CG00052) and v3 (#CG000183).
567 Illumina base call files for all libraries were converted to FASTQs using CellRanger-6.1.2
568 demultiplexing and count pipelines (https://www.10xgenomics.com). Initially, we used
569 cellranger’s mkfastq to demultiplex the raw base call (BCL) files generated by Illumina
570 sequencers, perform adapter trimming, and retrieve the 10-bp length UMI bases to be included
571 into the generated FASTQ files for downstream processing. We processed that raw FASTQs
572 with STARsolo103 using STAR 2.7.9a
573 (https://github.com/alexdobin/STAR/blob/master/docs/STARsolo.md). The barcode
574 demultiplexing was done with the default V2 / V3 whitelists coming from the CellRanger v.6
575 installation (https://kb.10xgenomics.com/hc/en-us/articles/115004506263-What-is-a-barcode-
576 whitelist-). For each of the Gel bead-in Emulsions (GEMs), we aligned the reads to the full
577 Ensembl human genome GRCh38 (https://uswest.ensembl.org/Homo_sapiens/Info/Index) and
578 used the standard STAR spliced read alignment algorithm to assigned them into the exonic,
579 intronic and intergenic groups. We performed error-correction and deduplication of the Unique
580 Molecular Identifiers (UMIs) and quantified the per-cell gene expression to generate the raw
581 UMI data for each library. To filter out the empty droplets we employed the
582 EmptyDrops_CR background model104 that g(cid:0)enerated the filtered UMI data of G = 36,601 genes
(cid:0)
583 (both protein-coding and non-coding) and = 414,082 cells across the J = 54 libraries for
584 downstream processing. The median number of cells across libraries was 7,748 with a 25%-
585 75% Inter-Quantile Range (IQR) of 5,891-9,133. Our data exhibited the typical high-quality
586 features suggested by the 10x’s guidelines (CG000329-Rev A, Technical Note): fraction of
587 r(cid:2)e ads with valid barcodes (ideal: >0.75; our median: 0.98), fraction of UMI bases with Q-score
588 30 (ideal: > 0.65; our median: 0.96) and fraction of unique reads in cells (ideal: > 0.70; our
589 median: 0.81).
590 Experimental design and meta data information
19

bioRxiv preprint doi: https://doi.org/10.1101/2025.01.17.633590; this version posted January 22, 2025. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under a CC-BY-ND 4.0 International license.
591  The similarity of the three glycemic states was assessed in terms of the Euclidian dot product
| (cid:4)(cid:5)(cid:6),(cid:8)(cid:9) (cid:10)(cid:11)∑ | (cid:6) (cid:8) (cid:13)(cid:18)(cid:14)(cid:15)∑ | (cid:6) (cid:16)(cid:15)∑     | (cid:8) (cid:17)              | (cid:6) (cid:8)                              |     |     |
| ------------------------------------------------------ | ------------------------------------------------- | ----------------------------- | ----------------------------- | -------------------------------------------- | --- | --- |
|                                                        | (cid:3)                                           | (cid:3) (cid:6)               | (cid:3) (cid:6)               |                                              |     |     |
|                                                        | (cid:2)(cid:4)(cid:5) (cid:2) (cid:2)             | (cid:2)(cid:4)(cid:5) (cid:2) | (cid:2)(cid:4)(cid:5) (cid:2) |                                              |     |     |
| 592                                                    |                                                   |                               | , where                       | ,   are the z-dimensional attribute vectors  |     |     |
(cid:6) (cid:8)
(cid:2) (cid:2)
593  of a glycemic state pair under comparison (z = 4) and   ,   are the ith components of these
594
vectors (one of sex, ancestry, age and BMI). We generated J = 54 10X libraries containing the
595  data of either single or multiplexed islets. The first 12 islets (in processing date), coming from 4
596  ND, 1 PD and 7 T2D donors, were generated with the V2 chemistry. Cells from 12 islets of V3
597  chemistry had their RNA sequenced across multiple islet-specific or genetically multiplexed islet
libraries105.
598
599  Ambient RNA Decontamination by SoupX
600  Ambient  RNA  is  the  pool  of  mRNA  molecules  released  in  the cell suspension  likely  from
601
stressed or apoptotic cells. It is incorporated into the droplets resulting in cross-contamination of
602  transcripts between different cell populations. We estimated and removed contamination in
603  individual cells by the (cid:19)S(cid:10)ou1p,X… ,m54odel106 using the soupX-1.6.2 R package from CRAN. We
604  processed each library   separately. First, we converted STARsolo’s raw and filtered
UMI data into respective Seurat v.4 objects107 (STAR-Methods) that were subsequently merged
605
606
into a single SoupX object. Seurat’s filtered data were normalized, scaled and clustered with
607  Leuven on the UMAP reduced representation (see “Seurat clustering by library”). The clustering
608  was fed into the SoupX object for ambient RNA contamination estimation and adjustment.
609  For decontamination, we considered as empty the droplets with less than 10 U(cid:19)M(cid:10)Is11,0…6 a,5n4d
610  estimated the fraction of backgroun (cid:8) d e (cid:10) xp∑ressi (cid:24) on f (cid:18) r(cid:25)o∑m ea∑ch g (cid:24) ene(cid:26) g of libra (cid:24) ry j ( )
|     |     |     | (cid:8)(cid:9)(cid:10)         | (cid:8)(cid:9)(cid:10)                  | (cid:8)(cid:9)(cid:10)                 |                  |
| --- | --- | --- | ------------------------------ | --------------------------------------- | -------------------------------------- | ---------------- |
|     |     |     | (cid:13)                       | (cid:13)                                | (cid:14)                               |                  |
|     |     |     | (cid:7) (cid:12)(cid:4)(cid:5) | (cid:7),(cid:12) (cid:12)(cid:4)(cid:5) | (cid:7)(cid:4)(cid:5) (cid:7),(cid:12) | (cid:7),(cid:12) |
611  across  all  empty  droplets  E  as    where    denotes  the
612  observed counts for gene g in the empty dro(cid:27)plet(cid:10) e(cid:25).∑ We (cid:24)use(cid:18)d∑ the (cid:24)bac·k∑groun(cid:8)d (cid:26)to estimate
|     |     |     |     | (cid:8)(cid:9)(cid:10) | (cid:8)(cid:9)(cid:10) (cid:8)(cid:9)(cid:10)                                 | (cid:8)(cid:9)(cid:10)        |
| --- | --- | --- | --- | ---------------------- | ----------------------------------------------------------------------------- | ----------------------------- |
|     |     |     |     |                        | (cid:14) (cid:14)                                                             | (cid:14)                      |
|     |     |     |     | (cid:15)               | (cid:7)(cid:4)(cid:5) (cid:7),(cid:15) (cid:7)(cid:4)(cid:5) (cid:7),(cid:15) | (cid:7)(cid:4)(cid:5) (cid:7) |
613  likewise each cell’s c contamination fraction as   where the
614  sums are taken across all genes G in each cell c of library j (SoupX(cid:24)(cid:29)’s a(cid:10)ut(cid:24)oEs∑tCont(cid:24) me·th(cid:27)od).·
(cid:8)(cid:9)(cid:10) (cid:8)(cid:9)(cid:10) (cid:8)(cid:9)(cid:10) (cid:8)(cid:9)(cid:10)
(cid:14)
(cid:7),(cid:15) (cid:7),(cid:15) (cid:7)(cid:4)(cid:5) (cid:7),(cid:15) (cid:15)
615  Finally, the endogenous (decontaminated) counts were retrieved as  -
(cid:8)
(cid:8)(cid:9)(cid:10)
(cid:7)
616  . The decontaminated counts of all genes G in cells of library j were stored in Seurat objects
617  and w(cid:0)ere used for the downstream a(cid:30)nal(cid:30)ys(cid:10)is.1 ,T…o ,3a6s,s6e0s1s the degre(cid:19)e(cid:19) o(cid:10)f c1o,…nt,a5m4ination across all
(cid:0)
618  cells  , we estimated for each gene  ,   in library  ,  , the difference in
#$
" (cid:10) ∑(cid:3)(cid:4)(cid:5)(cid:6)(cid:17)(cid:18)(cid:19)(cid:2)(cid:20)(cid:21)(cid:22)(cid:2)(cid:23)
(cid:9)
|      |     |     |     | (cid:7) | (cid:2)(cid:4)(cid:7) (cid:0) (cid:0) |         |
| ---- | --- | --- | --- | ------- | ------------------------------------- | ------- |
| 619  |     |     |     |         | (cid:24)(cid:25)                      | (cid:7) |
UMI counts before and after decontamination as  %& , where   was the average
|     |     | (cid:30) |     | (cid:19) |     |     |
| --- | --- | -------- | --- | -------- | --- | --- |
(cid:9)
| 620  |     |     |     |     | (cid:7) |     |
| ---- | --- | --- | --- | --- | ------- | --- |
uncorrected UMI of gene   across all cells of library   and   was the average corrected UMI of
|     |     |     |     | 20  |     |     |
| --- | --- | --- | --- | --- | --- | --- |

bioRxiv preprint doi: https://doi.org/10.1101/2025.01.17.633590; this version posted January 22, 2025. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under a CC-BY-ND 4.0 International license.
(cid:30) (cid:19) "
(cid:7)
621 gene across all cells of library . The levels were examined as a function of the average
’ (cid:10) ∑(cid:3)(cid:4)(cid:5)(cid:6)(cid:17)(cid:18)(cid:19)(cid:2)(cid:26)(cid:21)(cid:22)(cid:2)(cid:23) ’
(cid:7) (cid:2)(cid:4)(cid:7) (cid:0) (cid:0) (cid:7)
622 expression quantity (cid:24)(cid:25) by a classical MA plot that indicated at each level the
(cid:30)
623 degree of average decontamination for gene across all libraries. In addition, we estimated the
(cid:30) ( (cid:10) ∑(cid:3)(cid:4)(cid:5)(cid:6)(cid:27)(cid:28)(cid:29)(cid:30)(cid:8)(cid:31)(cid:2)(cid:10) "
(cid:9)
(cid:10) #$
(cid:9)
)%&
(cid:9)
624 average contamination ranking for each as (cid:7) (cid:2)(cid:4)(cid:7) (cid:24)(cid:25) (cid:0) , where (cid:7) (cid:7) (cid:7) .
625 Combining the information, our data separated three broad clusters of contaminants, the most
626 prominent of which included famous endocrine and exocrine markers such as Insulin (INS),
627 Glucagon (GCG), Somatostatin (SST), Pancreatic Polypeptide (PPY), Regenerating Family
628 Member 1 Alpha (REG1A), Serine Protease 2 (PRSS2) and other genes such as Transthyretin
629 (TTR) and Islet Amyloid Polypeptide (IAPP). The genes of this cluster were ranked on average
630 across all cells among the top 10 contaminants. A second cluster consisted of several
631 mitochondrial and ribosomal genes ranked on average among the top 20 to 100 contaminants.
632 Sample deconvolution by Demuxlet
633 We utilized modern barcoding technology to improve the throughput of detected cells and genes
634 via genetic multiplexing (see “Genetic multiplexing”) for a limited set of 12 libraries generated
635 under the V3 chemistry. Each library consisted of multiplexed barcoded cells from two islets of
636 donors with different clinical and demographic background and processed with Demuxlet108.
637 Demuxlet considered the islet’s genetic variation to determine the genetic identity of each
638 droplet through a set of single nucleotide polymorphisms (SNPs). The islet SNPs were identified
639 from the islet genotypes after extended quality control. The sample IDs of the processed
640 genotypes were validated by comparing them to paired bulk ATAC-seq data using verifyBamID
641 (https://github.com/statgen/verifyBamID/releases). To obtain the SNPs, we used plink v1.90109
642 and generated the Extended variant information files (.bim) accompanying the binary genotype
643 information for each chromosome of the GRCh37 human genome. We performed error-
644 correction for each file with HRC-1000G-check-bim (https://www.well.ox.ac.uk/~wrayner/tools/)
645 (STAR-Methods) to remove duplicate variants, mismatched variants, palindromic variants with
646 frequency > 0.4 and to correct strand flips using the reference file PASS.Variantsbravo-dbsnp-
647 all.tab containing 170M variants on ~15k individuals from the dbSNP database110. We joined
648 and sorted the error-free data of all chromosomes with bcftools-1.11
649 (https://samtools.github.io/bcftools/bcftools.html) and, at the last step, we used liftOver to
650 convert the genotype coordinates in the .vcf file to GRCh38 and obtained the barcode-to-islet
651 associations.
21

bioRxiv preprint doi: https://doi.org/10.1101/2025.01.17.633590; this version posted January 22, 2025. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under a CC-BY-ND 4.0 International license.
* +
(cid:8)(cid:9)(cid:10)
(cid:5)
652 D+emuxlet quantified the likelihood that the -th droplet of libra(cid:5)1ry) j o(cid:6)r(cid:9)i:g(cid:6)inated from the or the
(cid:6)
653 islets that have been multiplexed with mixing proportions . The likelihood had the
654 f-orm+: ,+ ,(cid:6) (cid:10) ∏ /∑ (cid:25)∏ 0∑ (cid:5)1)(cid:6)(cid:9)12(cid:8) 3(cid:30) ,456(cid:6)12(cid:8) 3(cid:30) ,4571 1 (cid:26)8
% $ (cid:5) (cid:8)(cid:7)(cid:5)(cid:10) (cid:8)(cid:7)(cid:6)(cid:10)
655 (
(cid:5) (cid:6)
)
"(cid:4)(cid:5) (cid:7)
(cid:7)
,(cid:7)
(cid:10)
(cid:2)(cid:4)(cid:11)(cid:8)
(cid:5)
(cid:2)(cid:9)(cid:12)
(cid:12)(cid:4)!
%
(cid:15)(cid:8)(cid:2)(cid:9)"(cid:2) (cid:5) (cid:15)(cid:8)(cid:2)(cid:9)"(cid:2) (cid:6) #
(cid:7)
" #
(cid:10)
"
.
(cid:8)(cid:9)(cid:10)
656 The above expression considers+ the rea+ds from barcoded cell-containing droplets of library
(cid:5) (cid:6)
657 j multiplex9ed across two islets and . The islet genotypes :are available acros*s V exonic
&’ (cid:8)(cid:9)(cid:10)
658 v(cid:8)ariants,
(cid:15)(cid:8)(cid:2)(cid:9)"
is the number of unique reads ove;rlapping the ; (cid:10)va1ri,a…nt, 9of the droplet,
&’
659
(cid:15)(cid:8)(cid:2)(cid:9)"(cid:2)
is the variant overlapping base call from the unique read,
(cid:15)(cid:8)(cid:2)(cid:9)"
representaing
660 reference (R), alternative (A) and other (O) alleles and l is a latent variable indicating whether
661 the base call is correct (0) or not (1). *
(cid:8)(cid:9)(cid:10)
662 We used directly Demuxlet’s .best output files th+at summ+arized the best assignment of the -
(cid:5) (cid:6)
663 th droplet of j bet*ween two multiplexed islets and . The provided information explicitly
(cid:8)(cid:9)(cid:10)
664 associating each either to a single islet (singlets) or to both (Demuxlet doublet) with high
665 probability. We integrated this information of each library with the Seurat soupX corrected
666 objects and filtered out the Demuxlet doublets from further analysis. Across the 12 libraries, we
667 removed on average 1,065 doublets (25%-75% IQR: 650-1319). We found that the number of
668 D(<e=m(cid:10)ux)le0t. 5d7oublets was weakly anti-correlated to the library processing date (Pearson’s
669 , p-value( <== 0(cid:10).005.36)1 1and also correlated to the number of STARsolo cell-containing
670 droplets(cid:19) (P(cid:10)e1a,r…so,n6’6s , p-value = 0.035). We kept 401,305 cells for further analysis
(cid:0)
671 across libraries holding the demultiplexed data of D = 48 islets (some islets are
672 represented more than once).
673 Quality control by library
674 The qua(cid:19)lity(cid:10) c1o,n…tr,o6l6 (QC) analysis was performed iteratively on the decontaminated raw counts
(cid:0)
675 of each demultiplexed library. It consisted of the fo(cid:24)ll@oAw’inBg s5t0e0ps: (cid:24)#"C B 1000
676 1. DP"reElim(cid:2)in5a0r%y filtering: We filtered out all cells with or or
677 as a first-pass data cleaning for the subsequent pre-processing steps(cid:24).@ TAh’e
678 i(cid:24)d#e"ntCificatioDn" oEf high-quality cells combined multi-step doublet estimation, stricter ,
679 , and cutoffs and statistical testing as shown below.
680 2. Doublet estimation: (cid:19)We used Scrublet111 and DoubletFinder 112 to estimate the neotypic
(cid:0)
681 doublets from each library. Scrublet was run in Python 3.6.15 on the Seurat-to-10x
682 formatted data (function write10xCounts of DropletUtils R package) with an expected
683 10% doublet ratio. We visualized the doublet scores of the observed and simulated
22

bioRxiv preprint doi: https://doi.org/10.1101/2025.01.17.633590; this version posted January 22, 2025. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under a CC-BY-ND 4.0 International license.
684 doublets in a histogram and inspected their bimodal distributions to set an appropriate
685 cutoff that separates the doublets from the singl(cid:19)ets. DoubletFinder operated on the
(cid:0)
686 normalized and clustered Seurat data of each D. Similar to Scrublet, it simulated
(
687 doublets wDith a set of user-defined parameters: (proportion of generated artificial
)
688 doublets), (the PC neighborDhood si(cid:24)z1e% to compute each cell's proportion of artificial k
*((
689 neare(cid:24)sAtG nDeighbors on a PCA, ), (the number of principal components (PCs))
690 and (a threshold to make the singlet / doublet prediction, similar to the expected
691 doublet ratio).
692 3. Clustering: We followed Seurat’s v4.0 standard pre-processing workflow108 from data
693 normalization to cell clustering (see “Seurat Clustering by library”) to filter ou(cid:24)t @loAw’ q(cid:24)u#a"lityC
694 cellsD b"eEfore the main data integration steGp. W(cid:19)e visualized the distribution of ,
(cid:0)
695 and of all cells across each cluster of to determine the appropriate cutoffs.
696 4. Marker analysis: To avoid over-filtering, we utilized marker expression analysis and pre-
697 annotated the clusters with kn(cid:24)o@wAn’ e(cid:24)n#d"ocCrine aDn"d Eexocrine marker genes (see “Cell
698 Annotation”), considering that , and may vary substantially across the
699 vDa"riEous cell types.
700 5. comparisons: We examined whether certaiDn" cEell types and, more importantly,
701 glycemic states (ND, PD, T2D) exhibited higher rates than others to adjust the
702 cutoffs. The comparisons were performed across annotated clusters within each state
703 and across states within each cell type using ANOVA and Tukey’s Honestly Significant
704 Differences (HSD) pairwise tests with Bonferroni corrected p-values.
705
706 Scrublet set an automatic threshold at the point between the two modes of the simulate scores.
707 We visually determined that the optimal doublet threshold was at 0.25 in all libraries. For
708 DoubletFinder, we normalized and clustered the Seurat data (10 PCs, Leuven clusteDrin(cid:10)g 0w.2ith5
(
709 resolution D= 0(cid:10).50 o.0n9 the UMAP) and(cid:24) AinGsDtr(cid:10)uc0te.1d the a(cid:24)lg1o%rit(cid:10)hm10 to simulate doublets using
)
710 (default), (estimated), and (default). Marker analysis sh1o1wJed
(cid:26)
711 t1hAa%t,’ "in 1contras%t Kt-o1 ’S1crublet, DoubletFinder often assigned higher doublet rates in ,
(cid:26) (cid:26)
712 and cell clusters. To avoid over-filtering, we removed only the common
713 Scrublet-DoubletFinder doublets leaving a total of 336,692 cells for further processing (median
714 = 6,663; 25%-75% IQR = 4,965 –8,288).
715 Seurat clustering by library
23

bioRxiv preprint doi: https://doi.org/10.1101/2025.01.17.633590; this version posted January 22, 2025. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under a CC-BY-ND 4.0 International license.
716 The raw counts of each library were normalizedL *w(cid:6)i4tMh. Nth(cid:6)e* OL=o(g(cid:10)No1r0m,0a0li0ze model that employed a
717 global-scaling (library size) normalization with and log-transformed the
718 result. The top 2,000 variable features, exhibiting the highest cell-to-cell variation, were
719 extracted and their normalized counts were scaled to fit on a Principal Components Analysis
720 (PCA) model for linear dimensionality reduction. We used standard quality control on the PC
721 loadings to empirically determine the optimal number of PCs accounting for the data variability.
722 For each library, we visualized the PC loadings and the associated heatmaps of gene
723 expression and kept the first 100 PCs for the UMAP representation. We constructed a shared
724 nearest neighbor graph by calculating the neighborhood overlap (Jaccard index) between every
725 cell and its 20 nearest neighbors obtained from the cell Euclidean distances. We clustered the
726 data with Leuve(cid:24)n@ aAn’d cluDs"teEring res(cid:24)o#l"utiCon pDa"raEmeter equal to 1. We inspected separate violin
727 and 2d plots of (cid:24)v@s A’ P 1a4n0d0 vs . Based on the spatial 1d and 2d patterns, we
728 flagged all cells with unless, at these cutoffs, the flagged cells enriched for an
729 annotated cluster (high-quality (cid:24)e@xoAc’rinPe1 c0e0l0l types had relatively low number of features) in
730 which case, we determined that was the most appropriate cutoff.
D"E D"E
731 To set the cutoff, we compared various quantiles of the distribution across annotated
732 cell types (derived by merging the cells of the above annotated clusters) and glycemD"icE states
733 (ND, PD, T2D). We used ANOVA and Tukey HSD pairwise tests to find whether the rates
734 differed significantlDy "aEcross the cell types. The analysis showed that α- and β-cells exhibited
735 statistically higher medians, 70-th quantiles and 90-th quantiles compared to other types
736 (see “Quality control by library”) at Bonferroni adjusted pD-"vaElue 5%. On the other hand, none of
737 the cell types showed significant differences among the s of ND vs PD vs T2DD" aEt QBo4n0f%erroni
738 adjusted p-value 5%. Based on these plots and results, we flagged all cells ∑with L (cid:10) 257,.0 A70ll
++ (cid:8)(cid:9)(cid:13)(cid:10)
(cid:9) (cid:4)(cid:5)
739 flagged cells were removed from further analysis reducing the dataset to (cid:13)
740 cells (median: 5,135; 25%-75% IQR: 4,063-6,014).
741 Data Integration and final cell filtering (cid:19) (cid:10) 1,…,66
(cid:0)
742 We used Harmony *v3.8113 within the Seurat v4.0 workflow to integrate the libraries
(cid:9)(cid:13)
743 each consisting of cells (after quality control by library). Harmony exhibits excellent scaling
744 properties for large populations and accommodates complex experimental designs allowing the
745 user to explicitly specify the6 6model parameters (factors) to be integrated. First, we merged the
746 normalized data across all libraries (see “Seurat Clustering by library”) and extracted the top
747 2,000 variable features for scaling. The cells were embedded in a 100-dimensional PCA space
24

bioRxiv preprint doi: https://doi.org/10.1101/2025.01.17.633590; this version posted January 22, 2025. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under a CC-BY-ND 4.0 International license.
748 and Harmony adjusted iteratively for sex, chemistry, and ancestry until convergence (10
749 iterations). At each iteration, the method used fuzzy clusRte(cid:5)r.i(cid:9)ng to assign each cell to multiple
750 clusters while preserving the data diversity via the term that penalized statistical
751 dependence between batch identity and cluster assignment. The estimated cluster and batch
752 centroids were used to derive a batch correction factor and a cell-specific correction factor
753 which were iteratively updated until convergence to a stable clustering representation. The
754 procedure generated 36 cell clusters. The median ratio of females across the 36 clusters was
755 0.36 (25%-75% IQR: 0.3 – 0.41) which was close to the overall female: male ratio of 0.37:0.63.
756 Similarly, the median values were 0.81 for V3 chemistry (overall: 0.79), 0.49 for the European
757 ancestry group (overall: 0.47), and 0.34 for the Hispanic ancestry group (median: 0.37).
758 Doublet enrichment
759 We estimated which of the Harmony integraGted Gclu(cid:10)st0e,r1s, …we,3r5e enriched in Scrublet doublets by
(cid:0) (cid:0)
760 the Fisher test. For each integrated cluster , , we calculated the doublet ratios
ST (cid:10) ST (cid:10)
# /0 /$12(cid:12)&3 (cid:2)(cid:29) ,(cid:13) 3$# /0 /$12(cid:12)&3 (cid:29)/& (cid:2)(cid:29) ,(cid:13)
761
,(cid:13)
# /0 3(cid:2)(cid:29)(cid:7)2(cid:12)&3 (cid:2)(cid:29) , (cid:13) and
(cid:20),(cid:13)
3$# /0 3(cid:2)(cid:29)(cid:7)2(cid:12)&3 (cid:29)/& (cid:2)(cid:29) , (cid:13). The enrichment test was performed
2 G 2
762 on the confusion matrix with cKolTum(cid:10)nS eTntri:eSsT the nQum2 erator and deno@mSinTaBtor1 o%f each of the
763 above quantities. The clusters with ,(cid:13) S (cid:20), T(cid:13) (cid:10) 1a.n2d4 8Fisher test ST (cid:10) 0w.3e0re7 those
(cid:6)4 (cid:6)!
764 labeled as significantly enriched. Clusters 29 with and 20 with stood
765 out with relatively high ratios. The Fisher enrichment tesKtT shQo2wed that clusters 29, 20, 15, and
766 23 were significantly enriched in doublets (odds ratio, ; Fisher test FDR<1%). We ran
767 differential expression analysis at the single-cell level wGith Seurat’s logistic regression model
(cid:0)
768 comparing the average expression of gene g in cluster again4s=t (cid:30)it@s% a(cid:2)ve0ra.2g5e expre@sSsTioBn i1n% all
769 other clusters after adjusting for sex, chemistry and ancestry ( and ).
770 Combined with evidence from marker expression analysis, we found that cluster 29 expressed
771 highly both INS and SST while cluster 20 expressed both GCG and SST. None of the other
772 clusters showed such evidence. We labeled all cells of 20 and 29 as doublets and filtered them
773 out along with all other Scrublet doublets, ending up with the final set of N = 245,878 high-
774 quality cells for downstream processing. We summarized the number of cells after each filtering
775 step by islet and examined whether our strategy and cutoffs led to differences in cell
776 percentages of each steVp a:Lc&ros(cid:10)s Lth& e (cid:10)glyLc& emic states. We used ANOVA and Tukey’s HSD tLo&
(cid:2) (cid:2) (cid:2) (cid:2)
! (5 65 7(cid:6)5
777 test the null hypLo& theLs&is L& versus the alternative that at least one of the
(cid:2) (cid:2) (cid:2)
(5 65 7(cid:6)5
778 differed, where , and were the a;verage percentage of cells across the ND, PD and
779 T2D islets, respectively, after filtering step . We did not detect any statistically differences at
780 Bonferroni adjusted p-value = 5%.
25

bioRxiv preprint doi: https://doi.org/10.1101/2025.01.17.633590; this version posted January 22, 2025. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under a CC-BY-ND 4.0 International license.
781 Doublet estimation
782 We estimated three types of doublets from our data. First, for the genetically multiplexed
783 libraries, we found Demuxlet doublets consisting of cells from different donors (see “Sample
784 deconvolution by Demuxlet”). Second, within each library, we utilized Scrublet and
785 DoubletFinder that simulated doublets from the raw UMI counts (after Demuxlet when
786 applicable) and, via nearest neighboring clustering, calculated the likelihood for an observed cell
787 to be a doublet (“Quality control by library”). Third, after data integration, we identified clusters
788 enriched in Scrublet doublets and expressing highly more than one of the known endocrine and
789 exocrine markers. All cells of such clusters were potential doublets (“Doublet enrichment”).
790 Cell Annotation
791 We annotated the integrated UMAP clusters of high-quality cells with a large list of known
792 endocrine and exocrine marker genes obtained from the literature and by differential expression
793 analysis. The latter was cGonducted by Seurat’s logistic regression model that compared gene’s
(cid:0)
794 g average expression in against its average expression al4l =o(cid:30)th2e@r% c(cid:2)lus0t.e2r5s afte@r SaTdjuBst1in%g for
795 sex, chemistry and ancestry. We reported significant genes at and .
796 The estimated cell types (and indicative markers) were beta (INS), alpha (GCG), delta (SST),
797 gamma (PPY), epsilon (GHRL), ductal (KRT19), acinar (REG1B), stellate (COL1A1), activated
798 stellate (FABP4), endothelial (PLVAP), Schwann (NGFR), immune (C1QC), mast (TPSB2) and
799 proliferating cells (TOP2A). For each islet, we calculated the number of cells across the
800 glycemic states of each cell type. We tested whether the absolute frequencies and/or the cell
801 percentages differed significantly in ND vs PD vs T2D by ANOVA and Tukey’s HSD pairwise
802 tests with Bonferroni correction.
803 Conversion to pseudo-bulk
804 We considered that the single cells within an islet are not independent of each other and
805 estimated the transcriptomic differences across cell types and glycemic states at the pseudo-
806 bulk level where the islets served as the biological replicates. We aggregated the single-cell rawW
807 counts anDd Dm(cid:10)et1a, …da,t1a (clinical and demographic information) associated with each cell type
808 aXn(cid:16)d 1islet , 1 , and generated Z = 14 pseudobulk RNA-seq count matrices of dimension
(cid:3) (cid:3)
809 , where might differ across the cell types. The aggregated data were obtained by the
810 aggregate.Matrix function of the Matrix.util v0.9.8 R pac(cid:24)k#a"geC. The quality control of the
811 pseudob(cid:24)u@lAk ’data was done in terms of the islet library sizes ( ), thDe" isElet number of detected
812 genes ( ), the percentage of reads mapped to the MT genome ( ) and the Counts-per-
813 Million (CPM) normalized log2-expression profiles of the top 50 most expressed genes. We
26

bioRxiv preprint doi: https://doi.org/10.1101/2025.01.17.633590; this version posted January 22, 2025. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under a CC-BY-ND 4.0 International license.
814 employed 2d Multidimensional Scaling (MDS) in edgeR v3.34.1114 to detect the major sources of
815 variability within each cell type.
816 Differential Expression Analysis with edgeR
817 We quantified the transcriptomic differences of the cell types and the glycemic states of each
818 endocrine cell type by edgeR on the pseudobulk level. Each model adjusted for sex, race,
819 chemistry, and BMI. Cell type comparisons were d4o=n(cid:30)e2 @in% t(cid:2)he0 f.5o8rm5 of (1)@ cSeTll Btyp5e% z vs all other
820 cell types to capture the global differences at and and (2) all
821 pairwise compariso|n4=s(cid:30) 2a@m%o|n(cid:2)g 1the en@dSoTcrBine5 %cell types to detect genes that were uniquely
822 upregulated in z at and . For glycemic|4 =st(cid:30)a2te@s%,| w(cid:2)e 0e.5s8tim5ated @alSl TpaBirw5i%se
823 comparisons and reported differentially expressed genes at and .
824 The functional characterization of the significant genes was done in clusterProfiler v4.0115 using
825 the enrichGO function with backgroZu1n0d,5 0a0l[l genes of the GRCh38 genome. The enriched
826 biological processes with set sizes in were reported at FDR=5%.
827 Differential Expression Analysis with a continuous covariate
828 We developed a Negative Binomial generalized linear model to identify genes whose
829 expression levels varied as a function of a continuous covariate X such as Age and BMI. The
830 significant genes wereA de(cid:10)tecJte6d% w<Mit+h ;tLhOe( \L6ike(cid:4)lMihGo6od’ R(cid:24)*aMtLioO ((\LR) test. AFor each gene g, the null
(cid:7) (cid:7)
831 model had the form: where denAote(cid:10)s Lg+e.n(cid:24)eL’s(cid:5)] g,^ Nra(cid:10)w
(cid:7)
832 c2o(cid:9)u6nJts 6(p%s<eMu+d;oLbOu(\lk)6 a(cid:4)cMrGos6s Tis(cid:6)l*eMts of interLe+s.t.(cid:24) LThe alternative model was
833 where generated a basis matrix for natural cubic
834 splines with 2 degrees of freedom, quantifying the smooth differences in mean expression as a
835 function of the factor of interest X. Variable Y is any other factor to be adjusted and it was added
836 here for convenience. For example, when looking for the genes whose expression differed
837 across age (X factor), Y represented the BMI and reverse. The LR test assesse_d th(cid:10)e )g2o(cid:5)o4dnes)s
89 (cid:29)$22
838 o4f f(cid:9)i~t aof the two 4competing4 models based on the ratio of their likelihoods
(cid:6)
(cid:28)2& (cid:5) (cid:29)$22 (cid:28)2&
839 where _ and are the log-likelihoods of the null and alternative models,
89
840 respectively and is distributed as a chi-square with one degree of freedom. Rejection of the
α
841 null model at significance level was associated with a potentially significant finding. In practice,
842 to minimize the chance of detecting genes with low p-values driven by a few outliers (o(v<e=r-
(cid:7)
843 smoothing due to the small sample size), we also estimate the Pearson correlation
844 between gene’s g CPM-nor_malized and log2-transformed d(a<t=a a(cid:2)n0d. 4X. The significant genes
89 (cid:7)
845 were detected at FDR=5% ( test) and the empirical cutoff .
27

bioRxiv preprint doi: https://doi.org/10.1101/2025.01.17.633590; this version posted January 22, 2025. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under a CC-BY-ND 4.0 International license.
846 Cell Type Subclustering
847 The single-cell RNA-seq gene expression profiles of Alpha, Beta and Delta cell types were
848 extracted and individually re-integrated as previously (see paragraph “Data Integration”). The
849 UMAP was estimated from the first 20 PCs and the clustering was performed with the Leuven
850 method and resolution paramGeter equal to 0.8. For each cell type, we compared gene’s g
(cid:3)
851 average expression in cluster vs all other clusters by Seurat’s Negative Binomial (negbinom)
852 m4=o(cid:30)d2e@l%, (cid:2)ad0ju.2s5ting fo@rS cTheBm1is%try, sex, age and ancestry. We labeled genes as significant if
853 and .
854 Cell culture
β
855 EndoC- H3 cells were cultured in Advanced DMEM F-12 media (Invitrogen) containing BSA
856 (SIGMA), Glutamax (Gibco), 2-beta mercaptoethanol (SIGMA), nicotinamide (SIGMA), sodium
857 selenite (SIGMA), Penicillin/Streptomycin (Gibco) and Puromycin (Calbiochem) on ECM
858 (SIGMA) and Fibronectin (SIGMA) coated flasks.
859 Lentivirus production & transduction of cells
860 Plasmid pLKO-puro shRNA clones (Mission shRNA) were purchased from SIGMA. Lentivirus
861 was produced in HEK293T cells co-expressing the shRNA plasmid together with psPAX2
862 packaging plasmid and pVSVG envelope plasmid. Virus was concentrated using Lenti-X
863 Concentrator (Takara) and virus titer was quantified using p24 ELISA antigen assay (Takara).
β
864 A MOI titer of 5 was used to transduce EndoC- H3 cells at 1 ×106 cells in culture media without
865 puromycin. Media change to puromycin complete media was done 18hrs post transduction.
866 RNA isolation
867 Total RNA was isolated from 3.5 ×105 cells/sample 96hrs post transduction. Cells were collected
868 for RNA extraction using TRIZOL (Invitrogen), phase separation was achieved using chloroform.
869 Isopropanol was used for RNA precipitation using glycogen as a carrier, the pellets were
870 washed using 75% ethanol, air-dried, and resuspended in DEPC water. RNA was measured
871 using Nanodrop. Total RNA was used to perform qPCR using RNA to CT kit (Invitrogen) and
872 FAM-Taqman probes (Invitrogen) and analyzed on QuantStudio 7 (Applied Biosystems)
873 normalized to ACTNB Taqman probe.
874 Insulin secretion assay
β
875 EndoC- H3 cells infected with the lentivirus were seeded onto coated 24 well plates at 1.75
876 ×105 cells/well. 72 hrs post transduction the cells were incubated overnight in Starvation media
28

bioRxiv preprint doi: https://doi.org/10.1101/2025.01.17.633590; this version posted January 22, 2025. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under a CC-BY-ND 4.0 International license.
877 [DMEM no glucose, containing BSA (SIGMA), human Transferrin (SIGMA), Glutamax (Gibco),
878 2-beta mercaptoethanol (SIGMA), nicotinamide (SIGMA), sodium selenite (SIGMA)]. After 18h
879 cells were equilibrated in KRBH buffer containing no glucose for 1 hour, before stimulated
880 insulin secretion was measured by static incubation of KRBH buffer containing 0mM and 20mM
881 Glucose for 1 hour. The supernatant was collected and stored at -20°C until human insulin
882 ELISA (Mercodia). After glucose stimulation, KRBH buffer was collected and the cells were
883 lysed with TETG solution [1M Tris pH 8.0, Triton X-100, Glycerol, 5M NaCl, 0.2M EGTA, and
884 distilled water along with 1X cOmplete, protease inhibitor cocktail (Roche)]. The lysate was
885 centrifuged at 3,000 rpm for 5 minutes and stored at -20°C until human insulin ELISA
886 (Mercodia) according to manufacturer’s instruction. Total protein was measured using BCA kit
887 (Thermo Fisher) and insulin secretion and content normalized to total protein content per
888 sample.
889 Flow cytometry
β
890 EndoC- H3 cells infected with the lentivirus were seeded onto coated 24 well plates at 1.75
891 ×105 cells/well. 90 hrs post transduction cells were collected from the plate using Trypsin
892 (Gibco) and stained using FITC Annexin V Apoptosis Detection Kit with 7-AAD (BioLegend)
893 according to Manufacturer’s instruction. The samples were run on Fortessa (BD Sciences), and
894 data was analyzed via FlowJo Software (BD Sciences).
895 Functional annotation of DEGs
896 We obtained the summary statistics of all genetic variants significantly associated with T2D at
(cid:5) (cid:5) (cid:5)
897 genome-wide significance P < 5 ×10−8 from multiple ancestry metanalyses - T2DGGI37,
898 DIAMANTE38, MVP39 and AGEN40. For each T2D associated variant, we identified proxy
≥
899 variants linked at r2 0.80 across all ancestries based on 1000Genomes Phase 3 data. To
900 determine if these T2D variants serve as eQTLs for our identified DEGs, we downloaded
901 summary statistics data of cis-eQTL associations from TIGER41 atlas (https://tiger.bsc.es/),
902 which includes 404 human pancreatic islet samples of European descent and reports >1.11
903 million significant eQTLs in >21,115 eGenes at 5% FDR. We retrieved all variants reported as
904 eQTLs for our identified DEGs at p-value < 0.05, with a consistent direction of association
905 across all four independent cohorts (++++ or ----) in the TIGER dataset. We then cross-
906 referenced the T2D genetic variant list and the eQTL list and identified eQTL variants for 41/511
907 DEGs that were also associated with T2D genetic risk.
29

bioRxiv preprint doi: https://doi.org/10.1101/2025.01.17.633590; this version posted January 22, 2025. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under a CC-BY-ND 4.0 International license.
908 Protein-level association data in T2D vs. ND whole islets was downloaded from the
909 HumanIslets56 consortium (https://www.humanislets.com/#/) that reports mass spectrometry
910 (MS)-based bulk protein expression data in 300 hand-picked islets per sample. P values were
911 calculated by multiple linear regression and adjusted for multiple testing with FDR.
912 Phenotypic data from whole gene knockout mouse lines was obtained from the
913 International Mouse Phenotyping Consortium62 web portal (https://www.mousephenotype.org/).
914 The latest data release (Nov 2024) reports 9,073 phenotyped genes, with knockout mice
915 produced and characterized by various institutional members of IMPC. All mice used in IMPC
916 studies have a C57BL/6N genetic background, with supporting mice derived from C57BL/6NJ,
917 C57BL/6NTac or C57BL/6NCrl strains. Glucose tolerance was assessed by initial response to
918 glucose challenge and/or calculating the area under the glucose response curve from an
919 intraperitoneal glucose tolerance test (IPGTT).
920
921 References
922 1. Thurner, M. et al. Integration of human pancreatic islet genomic data refines regulatory
923 mechanisms at Type 2 Diabetes susceptibility loci. eLife 7, e31977 (2018).
924 2. Stitzel, M. L. et al. Global Epigenomic Analysis of Primary Human Pancreatic Islets Provides
925 Insights into Type 2 Diabetes Susceptibility Loci. Cell Metabolism 12, 443–455 (2010).
926 3. Varshney, A. et al. Genetic regulatory signatures underlying islet gene expression and type 2
927 diabetes. Proceedings of the National Academy of Sciences 114, 2301–2306 (2017).
928 4. Cabrera, O. et al. The unique cytoarchitecture of human pancreatic islets has implications for
929 islet cell function. Proceedings of the National Academy of Sciences 103, 2334–2339 (2006).
930 5. Noguchi, G. M. & Huising, M. O. Integrating the inputs that shape pancreatic islet hormone
931 release. Nat Metab 1, 1189–1201 (2019).
932 6. Elgamal, R. M. et al. An Integrated Map of Cell Type-Specific Gene Expression in Pancreatic
933 Islets. Diabetes 72, 1719–1728 (2023).
30

bioRxiv preprint doi: https://doi.org/10.1101/2025.01.17.633590; this version posted January 22, 2025. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under a CC-BY-ND 4.0 International license.
β
934 7. Fang, Z. et al. Single-Cell Heterogeneity Analysis and CRISPR Screen Identify Key -Cell-
935 Specific Disease Genes. Cell Reports 26, 3132-3144.e7 (2019).
β
936 8. Weng, C. et al. Single cell multiomic analysis reveals diabetes-associated -cell heterogeneity
937 driven by HNF1A. Nat Commun 14, 5400 (2023).
938 9. Segerstolpe, Å. et al. Single-Cell Transcriptome Profiling of Human Pancreatic Islets in
939 Health and Type 2 Diabetes. Cell Metab 24, 593–607 (2016).
940 10. Lawlor, N. et al. Single-cell transcriptomes identify human islet cell signatures and reveal
941 cell-type–specific expression changes in type 2 diabetes. Genome Res. 27, 208–222 (2017).
942 11. Patil, A. R. et al. Single-cell expression profiling of islets generated by the Human
943 Pancreas Analysis Program. Nat Metab 5, 713–715 (2023).
944 12. American Diabetes Association Professional Practice Committee. 2. Classification and
945 Diagnosis of Diabetes: Standards of Medical Care in Diabetes—2022. Diabetes Care 45,
946 S17–S38 (2021).
947 13. Wang, G. et al. Integrating genetics with single-cell multiomic measurements across
948 disease states identifies mechanisms of beta cell dysfunction in type 2 diabetes. Nat Genet 55,
949 984–994 (2023).
β
950 14. Hou, X. et al. Relationship of Hemoglobin A1c with Cell Function and Insulin
951 Resistance in Newly Diagnosed and Drug Naive Type 2 Diabetes Patients. J Diabetes Res
952 2016, 8797316 (2016).
953 15. Bacos, K. et al. Type 2 diabetes candidate genes, including PAX5, cause impaired insulin
954 secretion in human pancreatic islets. J Clin Invest 133, e163612 (2023).
955 16. Bosi, E. et al. Integration of single-cell datasets reveals novel transcriptomic signatures of
β
956 -cells in human type 2 diabetes. NAR Genom Bioinform 2, lqaa097 (2020).
31

bioRxiv preprint doi: https://doi.org/10.1101/2025.01.17.633590; this version posted January 22, 2025. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under a CC-BY-ND 4.0 International license.
957 17. Wang, Y. J. et al. Single-Cell Transcriptomics of the Human Endocrine Pancreas.
958 Diabetes 65, 3028–3038 (2016).
959 18. Fadista, J. et al. Global genomic and transcriptomic analysis of human pancreatic islets
960 reveals novel genes influencing glucose metabolism. Proc Natl Acad Sci U S A 111, 13924–
961 13929 (2014).
β
962 19. Marselli, L. et al. Persistent or Transient Human Cell Dysfunction Induced by
963 Metabolic Stress: Specific Signatures and Shared Gene Expression with Type 2 Diabetes. Cell
964 Rep 33, 108466 (2020).
965 20. Solimena, M. et al. Systems biology of the IMIDIA biobank from organ donors and
966 pancreatectomised patients defines a novel transcriptomic signature of islets from individuals
967 with type 2 diabetes. Diabetologia 61, 641–657 (2018).
968 21. Xin, Y. et al. RNA Sequencing of Single Human Islet Cells Reveals Type 2 Diabetes
969 Genes. Cell Metab 24, 608–615 (2016).
970 22. The UniProt Consortium. UniProt: the Universal Protein Knowledgebase in 2023.
971 Nucleic Acids Research 51, D523–D531 (2023).
972 23. Alvarsson, A. et al. A 3D atlas of the dynamic and regional variation of pancreatic
973 innervation in diabetes. Science Advances 6, eaaz9124 (2020).
974 24. Hampton, R. F., Jimenez-Gonzalez, M. & Stanley, S. A. Unravelling innervation of
975 pancreatic islets. Diabetologia 65, 1069–1084 (2022).
976 25. Meyers, E. E., Kronemberger, A., Lira, V., Rahmouni, K. & Stauss, H. M. Contrasting
977 effects of afferent and efferent vagal nerve stimulation on insulin secretion and blood glucose
978 regulation. Physiol Rep 4, e12718 (2016).
32

bioRxiv preprint doi: https://doi.org/10.1101/2025.01.17.633590; this version posted January 22, 2025. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under a CC-BY-ND 4.0 International license.
979 26. Stanley, S. A. et al. Bidirectional electromagnetic control of the hypothalamus regulates
980 feeding and metabolism. Nature 531, 647–650 (2016).
981 27. Obermüller, S. et al. Selective nucleotide-release from dense-core granules in insulin-
982 secreting cells. Journal of Cell Science 118, 4271–4282 (2005).
983 28. Khan, S. et al. Autocrine activation of P2Y1 receptors couples Ca2+ influx to Ca2+
984 release in human pancreatic beta cells. Diabetologia 57, 2535–2545 (2014).
985 29. Trasino, S. E., Benoit, Y. D. & Gudas, L. J. Vitamin A Deficiency Causes
β
986 Hyperglycemia and Loss of Pancreatic -Cell Mass. J Biol Chem 290, 1456–1473 (2015).
987 30. Noy, N. Between death and survival: retinoic acid in regulation of apoptosis. Annu Rev
988 Nutr 30, 201–217 (2010).
989 31. Lavudi, K. et al. Targeting the retinoic acid signaling pathway as a modern precision
990 therapy against cancers. Front. Cell Dev. Biol. 11, (2023).
991 32. Uhlen, M. et al. Towards a knowledge-based Human Protein Atlas. Nat Biotechnol 28,
992 1248–1250 (2010).
993 33. Taddeo, E. P. et al. Mitochondrial Proton Leak Regulated by Cyclophilin D Elevates
994 Insulin Secretion in Islets at Nonstimulatory Glucose Levels. Diabetes 69, 131–145 (2019).
995 34. Li, C. et al. A Signaling Role of Glutamine in Insulin Secretion*. Journal of Biological
996 Chemistry 279, 13393–13401 (2004).
997 35. Liu, X. et al. High plasma glutamate and low glutamine-to-glutamate ratio are associated
998 with type 2 diabetes: Case-cohort study within the PREDIMED trial. Nutr Metab Cardiovasc
999 Dis 29, 1040–1049 (2019).
1000 36. Zhang, H., Colclough, K., Gloyn, A. L. & Pollin, T. I. Monogenic diabetes: a gateway to
1001 precision medicine in diabetes. J Clin Invest 131, e142244.
33

bioRxiv preprint doi: https://doi.org/10.1101/2025.01.17.633590; this version posted January 22, 2025. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under a CC-BY-ND 4.0 International license.
1002 37. Suzuki, K. et al. Genetic drivers of heterogeneity in type 2 diabetes pathophysiology.
1003 Nature 627, 347–357 (2024).
1004 38. Mahajan, A. et al. Multi-ancestry genetic study of type 2 diabetes highlights the power of
1005 diverse populations for discovery and translation. Nat Genet 54, 560–572 (2022).
1006 39. Vujkovic, M. et al. Discovery of 318 new risk loci for type 2 diabetes and related
1007 vascular outcomes among 1.4 million participants in a multi-ancestry meta-analysis. Nat
1008 Genet 52, 680–691 (2020).
1009 40. Spracklen, C. N. et al. Identification of type 2 diabetes loci in 433,540 East Asian
1010 individuals. Nature 582, 240–245 (2020).
1011 41. Alonso, L. et al. TIGER: The gene expression regulatory variation landscape of human
1012 pancreatic islets. Cell Rep 37, 109807 (2021).
1013 42. Viñuela, A. et al. Genetic variant effects on gene expression in human pancreatic islets
1014 and their implications for T2D. Nat Commun 11, 4912 (2020).
1015 43. Bunt, M. van de et al. Transcript Expression Data from Human Islets Links Regulatory
1016 Signals from Genome-Wide Association Studies for Type 2 Diabetes and Glycemic Traits to
1017 Their Downstream Effectors. PLOS Genetics 11, e1005694 (2015).
1018 44. Zhou, B. et al. Serum- and glucocorticoid-induced kinase drives hepatic insulin resistance
1019 by directly inhibiting AMP-activated protein kinase. Cell Rep 37, 109785 (2021).
1020 45. Kaiser, G. et al. Regulation of forkhead box O1 (FOXO1) by protein kinase B and
1021 glucocorticoids: different mechanisms of induction of beta cell death in vitro. Diabetologia
1022 56, 1587–1595 (2013).
34

bioRxiv preprint doi: https://doi.org/10.1101/2025.01.17.633590; this version posted January 22, 2025. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under a CC-BY-ND 4.0 International license.
1023 46. Kobayashi, T., Deak, M., Morrice, N. & Cohen, P. Characterization of the structure and
1024 regulation of two novel isoforms of serum- and glucocorticoid-induced protein kinase.
1025 Biochem J 344, 189–197 (1999).
1026 47. Programmed death ligand 1 regulates epithelial–mesenchymal transition and cancer stem
1027 cell phenotypes in hepatocellular carcinoma through the serum and glucocorticoid kinase
β(cid:2)
1028 2/ catenin signaling pathway - Kong - 2023 - Cancer Science - Wiley Online Library.
1029 https://onlinelibrary.wiley.com/doi/10.1111/cas.15753.
1030 48. Cheng, L. et al. SGK2 promotes prostate cancer metastasis by inhibiting ferroptosis via
1031 upregulating GPX4. Cell Death Dis 14, 1–14 (2023).
1032 49. Zhao, Z. et al. An integrative single-cell multi-omics profiling of human pancreatic islets
1033 identifies T1D associated genes and regulatory signals. Res Sq rs.3.rs-3343318 (2023)
1034 doi:10.21203/rs.3.rs-3343318/v1.
β
1035 50. Lu, J. et al. KCNH6 protects pancreatic -cells from endoplasmic reticulum stress and
1036 apoptosis. The FASEB Journal 34, 15015–15028 (2020).
1037 51. Hyltén-Cavallius, L. et al. Patients With Long-QT Syndrome Caused by Impaired hERG-
1038 Encoded Kv11.1 Potassium Channel Have Exaggerated Endocrine Pancreatic and Incretin
1039 Function Associated With Reactive Hypoglycemia. Circulation 135, 1705–1719 (2017).
1040 52. Zhao, M.-M. et al. Berberine is an insulin secretagogue targeting the KCNH6 potassium
1041 channel. Nat Commun 12, 5616 (2021).
1042 53. Waselle, L. et al. Role of phosphoinositide signaling in the control of insulin exocytosis.
1043 Mol Endocrinol 19, 3097–3106 (2005).
35

bioRxiv preprint doi: https://doi.org/10.1101/2025.01.17.633590; this version posted January 22, 2025. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under a CC-BY-ND 4.0 International license.
1044 54. Myers, T. A., Chanock, S. J. & Machiela, M. J. LDlinkR: An R Package for Rapidly
1045 Calculating Linkage Disequilibrium Statistics in Diverse Populations. Front. Genet. 11,
1046 (2020).
1047 55. Strober, B. J. et al. Dynamic genetic regulation of gene expression during cellular
1048 differentiation. Science 364, 1287–1290 (2019).
1049 56. Ewald, J. D. et al. HumanIslets.com: Improving accessibility, integration, and usability of
1050 human research islet data. Cell Metabolism 0, (2024).
1051 57. Dayeh, T. et al. Genome-Wide DNA Methylation Analysis of Human Pancreatic Islets
1052 from Type 2 Diabetic and Non-Diabetic Donors Identifies Candidate Genes That Influence
1053 Insulin Secretion. PLOS Genetics 10, e1004160 (2014).
1054 58. Guo, J. H. et al. Glucose-induced electrical activities and insulin secretion in pancreatic
β
1055 islet -cells are modulated by CFTR. Nat Commun 5, 4420 (2014).
1056 59. Marselli, L. et al. Arginase 2 and Polyamines in Human Pancreatic Beta Cells: Possible
1057 Role in the Pathogenesis of Type 2 Diabetes. International Journal of Molecular Sciences 22,
1058 12099 (2021).
1059 60. Mandla, R. et al. Multi-omics characterization of type 2 diabetes associated genetic
1060 variation. 2024.07.15.24310282 Preprint at https://doi.org/10.1101/2024.07.15.24310282
1061 (2024).
1062 61. Besprozvannaya, M. et al. GRAM domain proteins specialize functionally distinct ER-
1063 PM contact sites in human cells. eLife 7, e31019 (2018).
1064 62. Groza, T. et al. The International Mouse Phenotyping Consortium: comprehensive
1065 knockout phenotyping underpinning the study of human disease. Nucleic Acids Research 51,
1066 D1038–D1045 (2023).
36

bioRxiv preprint doi: https://doi.org/10.1101/2025.01.17.633590; this version posted January 22, 2025. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under a CC-BY-ND 4.0 International license.
1067 63. Vande Velde, C. et al. BNIP3 and Genetic Control of Necrosis-Like Cell Death through
1068 the Mitochondrial Permeability Transition Pore. Molecular and Cellular Biology 20, 5454–
1069 5468 (2000).
1070 64. Burton, T. R. & Gibson, S. B. The role of Bcl-2 family member BNIP3 in cell death and
1071 disease: NIPping at the heels of cell death. Cell Death Differ 16, 515–523 (2009).
1072 65. Bansal, V. et al. Genome-wide association study results for educational attainment aid in
1073 identifying genetic heterogeneity of schizophrenia. Nat Commun 9, 3078 (2018).
1074 66. Abelson, J. F. et al. Sequence Variants in SLITRK1 Are Associated with Tourette’s
1075 Syndrome. Science 310, 317–320 (2005).
1076 67. Yim, Y. S. et al. Slitrks control excitatory and inhibitory synapse formation with LAR
1077 receptor protein tyrosine phosphatases. Proceedings of the National Academy of Sciences 110,
1078 4057–4062 (2013).
1079 68. Campbell, S. A. et al. Human islets contain a subpopulation of glucagon-like peptide-1
α
1080 secreting cells that is increased in type 2 diabetes. Molecular Metabolism 39, 101014
1081 (2020).
δ β
1082 69. Carril Pardo, C. A. et al. A -cell subpopulation with a pro- -cell identity contributes to
1083 efficient age-independent recovery in a zebrafish model of diabetes. eLife 11, e67576 (2022).
1084 70. Wang, J. et al. Regulation of endocrine cell alternative splicing revealed by single-cell
1085 RNA sequencing in type 2 diabetes pathogenesis. Commun Biol 7, 1–15 (2024).
1086 71. Fu, Q. et al. Single-cell RNA sequencing combined with single-cell proteomics identifies
1087 the metabolic adaptation of islet cell subpopulations to high-fat diet in mice. Diabetologia 66,
1088 724–740 (2023).
37

bioRxiv preprint doi: https://doi.org/10.1101/2025.01.17.633590; this version posted January 22, 2025. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under a CC-BY-ND 4.0 International license.
β
1089 72. Dorrell, C. et al. Human islets contain four distinct subtypes of cells. Nat Commun 7,
1090 11756 (2016).
1091 73. Maestas, M. M. et al. Identification of unique cell type responses in pancreatic islets to
1092 stress. Nat Commun 15, 5567 (2024).
β
1093 74. Sharma, R. B. et al. Insulin demand regulates cell number via the unfolded protein
1094 response. J Clin Invest 125, 3831–3846 (2015).
1095 75. Baron, M. et al. A Single-Cell Transcriptomic Map of the Human and Mouse Pancreas
1096 Reveals Inter- and Intra-cell Population Structure. cels 3, 346-360.e4 (2016).
β
1097 76. Dominguez-Gutierrez, G., Xin, Y. & Gromada, J. Heterogeneity of human pancreatic -
1098 cells. Molecular Metabolism 27, S7–S14 (2019).
β
1099 77. Bader, E. et al. Identification of proliferative and mature -cells in the islets of
1100 Langerhans. Nature 535, 430–434 (2016).
1101 78. Rubio-Navarro, A. et al. A beta cell subset with enhanced insulin secretion and glucose
1102 metabolism is reduced in type 2 diabetes. Nat Cell Biol 25, 565–578 (2023).
β
1103 79. Aguayo-Mazzucato, C. et al. Acceleration of Cell Aging Determines Diabetes and
1104 Senolysis Improves Disease Outcomes. Cell Metabolism 30, 129-142.e4 (2019).
β
1105 80. Cha, J., Aguayo-Mazzucato, C. & Thompson, P. J. Pancreatic -cell senescence in
1106 diabetes: mechanisms, markers and therapies. Front Endocrinol (Lausanne) 14, 1212716
1107 (2023).
1108 81. Sone, H. & Kagawa, Y. Pancreatic beta cell senescence contributes to the pathogenesis of
1109 type 2 diabetes in high-fat diet-induced diabetic mice. Diabetologia 48, 58–67 (2005).
38

bioRxiv preprint doi: https://doi.org/10.1101/2025.01.17.633590; this version posted January 22, 2025. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under a CC-BY-ND 4.0 International license.
1110 82. Cnop, M., Hannaert, J. C., Grupping, A. Y. & Pipeleers, D. G. Low Density Lipoprotein
β
1111 Can Cause Death of Islet -Cells by Its Cellular Uptake and Oxidative Modification.
1112 Endocrinology 143, 3449–3453 (2002).
1113 83. Rovira, M. et al. Chemical screen identifies FDA-approved drugs and target pathways
1114 that induce precocious pancreatic endocrine differentiation. Proceedings of the National
1115 Academy of Sciences 108, 19264–19269 (2011).
1116 84. Huang, W. et al. Retinoic acid plays an evolutionarily conserved and biphasic role in
1117 pancreas development. Developmental Biology 394, 83–93 (2014).
1118 85. Huang, W. et al. Sox9b is a mediator of retinoic acid signaling restricting endocrine
1119 progenitor differentiation. Developmental Biology 418, 28–39 (2016).
1120 86. Trasino, S. E., Benoit, Y. D. & Gudas, L. J. Vitamin A Deficiency Causes
β
1121 Hyperglycemia and Loss of Pancreatic -Cell Mass*. Journal of Biological Chemistry 290,
1122 1456–1473 (2015).
1123 87. Brun, P.-J. et al. Retinoic acid receptor signaling is required to maintain glucose-
β
1124 stimulated insulin secretion and -cell mass. FASEB J 29, 671–683 (2015).
β
1125 88. Papazoglou, I. et al. A distinct hypothalamus-to- cell circuit modulates insulin secretion.
1126 Cell Metabolism 34, 285-298.e7 (2022).
β
1127 89. Makhmutova, M. et al. Pancreatic -Cells Communicate With Vagal Sensory Neurons.
1128 Gastroenterology 160, 875-888.e11 (2021).
1129 90. Marquard, J. et al. Characterization of pancreatic NMDA receptors as possible drug
1130 targets for diabetes treatment. Nat Med 21, 363–372 (2015).
γ
1131 91. Braun, M. et al. -Aminobutyric Acid (GABA) Is an Autocrine Excitatory Transmitter in
β
1132 Human Pancreatic -Cells. Diabetes 59, 1694–1701 (2010).
39

bioRxiv preprint doi: https://doi.org/10.1101/2025.01.17.633590; this version posted January 22, 2025. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under a CC-BY-ND 4.0 International license.
β
1133 92. Rorsman, P. & Ashcroft, F. M. Pancreatic -Cell Electrical Activity and Insulin
1134 Secretion: Of Mice and Men. Physiol Rev 98, 117–214 (2018).
1135 93. Bysani, M. et al. ATAC-seq reveals alterations in open chromatin in pancreatic islets
1136 from subjects with type 2 diabetes. Sci Rep 9, 7785 (2019).
1137 94. Pan, X., Tao, S. & Tong, N. Potential Therapeutic Targeting Neurotransmitter Receptors
1138 in Diabetes. Front. Endocrinol. 13, (2022).
β
1139 95. Talchai, C., Xuan, S., Lin, H. V., Sussel, L. & Accili, D. Pancreatic Cell
β
1140 Dedifferentiation as a Mechanism of Diabetic Cell Failure. Cell 150, 1223–1234 (2012).
1141 96. Grün, D. et al. De Novo Prediction of Stem Cell Identity using Single-Cell Transcriptome
1142 Data. Cell Stem Cell 19, 266–277 (2016).
1143 97. Muraro, M. J. et al. A Single-Cell Transcriptome Atlas of the Human Pancreas. Cell
1144 Systems 3, 385-394.e3 (2016).
β
1145 98. Fonseca, S. G., Gromada, J. & Urano, F. Endoplasmic reticulum stress and pancreatic -
1146 cell death. Trends in Endocrinology & Metabolism 22, 266–274 (2011).
β
1147 99. Xin, Y. et al. Pseudotime Ordering of Single Human -Cells Reveals States of Insulin
1148 Production and Unfolded Protein Response. Diabetes 67, 1783–1794 (2018).
β
1149 100. Lee, H. et al. Stress-induced cell early senescence confers protection against type 1
1150 diabetes. Cell Metabolism 35, 2200-2215.e9 (2023).
1151 101. Carapeto, P. et al. Exercise activates AMPK in mouse and human pancreatic islets to
1152 decrease senescence. Nat Metab 6, 1976–1990 (2024).
β
1153 102. Cha, J., Aguayo-Mazzucato, C. & Thompson, P. J. Pancreatic -cell senescence in
1154 diabetes: mechanisms, markers and therapies. Front. Endocrinol. 14, (2023).
40

bioRxiv preprint doi: https://doi.org/10.1101/2025.01.17.633590; this version posted January 22, 2025. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under a CC-BY-ND 4.0 International license.
1155 103. Kaminow, B., Yunusov, D. & Dobin, A. STARsolo: accurate, fast and versatile
1156 mapping/quantification of single-cell and single-nucleus RNA-seq dat. Preprint at
1157 https://doi.org/10.1101/2021.05.05.442755 (2021).
1158 104. Lun, A. T. L. et al. EmptyDrops: distinguishing cells from empty droplets in droplet-
1159 based single-cell RNA sequencing data. Genome Biol 20, 63 (2019).
1160 105. Macosko, E. Z. et al. Highly parallel genome-wide expression profiling of individual
1161 cells using nanoliter droplets. Cell 161, 1202–1214 (2015).
1162 106. Young, M. D. & Behjati, S. SoupX removes ambient RNA contamination from droplet-
1163 based single-cell RNA sequencing data. Gigascience 9, giaa151 (2020).
1164 107. Hao, Y. et al. Integrated analysis of multimodal single-cell data. Cell 184, 3573-3587.e29
1165 (2021).
1166 108. Kang, H. M. et al. Multiplexed droplet single-cell RNA-sequencing using natural genetic
1167 variation. Nat Biotechnol 36, 89–94 (2018).
1168 109. Purcell, S. et al. PLINK: A Tool Set for Whole-Genome Association and Population-
1169 Based Linkage Analyses. Am J Hum Genet 81, 559–575 (2007).
1170 110. Sherry, S. T., Ward, M. & Sirotkin, K. dbSNP-database for single nucleotide
1171 polymorphisms and other classes of minor genetic variation. Genome Res 9, 677–679 (1999).
1172 111. Wolock, S. L., Lopez, R. & Klein, A. M. Scrublet: Computational Identification of Cell
1173 Doublets in Single-Cell Transcriptomic Data. Cell Syst 8, 281-291.e9 (2019).
1174 112. McGinnis, C. S., Murrow, L. M. & Gartner, Z. J. DoubletFinder: Doublet Detection in
1175 Single-Cell RNA Sequencing Data Using Artificial Nearest Neighbors. Cell Syst 8, 329-
1176 337.e4 (2019).
41

bioRxiv preprint doi: https://doi.org/10.1101/2025.01.17.633590; this version posted January 22, 2025. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under a CC-BY-ND 4.0 International license.
1177 113. Korsunsky, I. et al. Fast, sensitive and accurate integration of single-cell data with
1178 Harmony. Nat Methods 16, 1289–1296 (2019).
1179 114. Robinson, M. D., McCarthy, D. J. & Smyth, G. K. edgeR: a Bioconductor package for
1180 differential expression analysis of digital gene expression data. Bioinformatics 26, 139–140
1181 (2010).
1182 115. Yu, G., Wang, L.-G., Han, Y. & He, Q.-Y. clusterProfiler: an R Package for Comparing
1183 Biological Themes Among Gene Clusters. OMICS 16, 284–287 (2012).
1184
1185
42

bioRxiv preprint doi: https://doi.org/10.1101/2025.01.17.633590; this version posted January 22, 2025. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under a CC-BY-ND 4.0 International license.
1186 Figure Legends
1187 Figure 1: Human pancreatic islet single-cell transcriptomes from 48-donor cohort reveal
1188 cell type proportion variability in T2D donors.
1189 (a) Human pancreatic islets from 48 cadaveric donors -- 17 with diagnosed type 2 diabetes
1190 (T2D), 14 with HbA1c-based prediabetes (PD; HbA1c 5.7%-6.4%), and 17 without diabetes
1191 (ND) -- were dissociated into single cells and profiled using droplet-based scRNA-seq to obtain
1192 245,878 high quality islet single cell transcriptomes. (b) Comparison of age, body mass index
1193 (BMI, a measure of obesity), and glycated hemoglobin (HbA1c) between T2D, PD, and ND
1194 individuals in the cohort. Each dot represents an individual donor. The black line and error bars
1195 represent the mean ± standard error of the mean. Significant differences (p<0.05, Games-
1196 Howell post-hoc test) are reported. (c) Uniform Manifold Approximation and Projection (UMAP)
1197 plots displaying unsupervised clustering of 245,878 cells in ND (left), PD (middle), and T2D
1198 (right) donors reveals 14 distinct cell types based on the expression of the 2000 most variable
1199 genes across the cells. n=number of single cell transcriptomes obtained for each cell type. (d)
1200 Relative percentages of various endocrine cell types, shown in per-donor stacked bar plots
1201 across the glycemic states, indicate remarkably fewer β-cells in islets from T2D (bottom) vs. PD
1202 (middle) or ND (top) donors. (e) Relative abundance of α-, β-, δ-, and γ-cells in ND, PD, or T2D
1203 donors. Dots represent percentage of endocrine cells detected for each donor. Epsilon (ε) cells
1204 were rare (0.09%) in all donors and omitted from comparison. The black line and error bars
1205 represent the mean ± standard error of the mean. P-values were calculated using Tukey's
1206 honest significance test. Significant differences (p<0.05) are indicated. (f, g) Spearman
β
1207 correlations between HbA1c levels (y-axis) and relative -cell (f, x-axis) or α-cell (g, x-axis)
1208 abundance for all cohort donors (n=48). Bands enclosing the linear regression line represent
1209 99% confidence intervals. Dots represent individual donors colored as in panel (a) based on
1210 their glycemic status.
1211
β
1212 Figure 2: Differentially expressed genes in T2D vs. ND -cells.
β
1213 (a) Volcano plot of differentially expressed genes in T2D vs. ND -cells. Each dot denotes a
1214 gene. 511 genes with significant differences in expression at false discovery rate (FDR) < 5%
≥
1215 and fold change 50% are colored blue (T2D-downregulated) or purple (T2D-upregulated);
β
1216 gray dots denote those with comparable expression in T2D and ND -cells. (b,c) Gene set
1217 enrichment analysis (GSEA) for differentially expressed genes using the molecular signatures
1218 database (MSigDB, BROAD Institute). Enriched non-redundant processes with FDR q<0.05 are
43

bioRxiv preprint doi: https://doi.org/10.1101/2025.01.17.633590; this version posted January 22, 2025. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under a CC-BY-ND 4.0 International license.
1219 shown for upregulated (b) and downregulated (c) gene sets. Number of genes in each
1220 functional term is provided as a gene ratio relative to total number of tested upregulated (n=316)
β
1221 or downregulated (n=195) T2D -cell genes. (d) KEGG- and Wiki- pathways enriched in up- vs.
1222 downregulated genes. (e) Heatmap of scaled expression of genes comprising primary enriched
1223 molecular pathways identified (d) in T2D vs. ND donors. (f) Volcano plots showing differentially
β
1224 expressed cell death genes in - (left) or α- (right) cells from T2D vs. ND donor islets. (g) Basal
1225 (gray; 0mM glucose) or glucose-stimulated (red; 20 mM glucose) insulin secretion in human
β
1226 EndoC- H3 cells following shRNA-mediated knockdown of selected target genes or a non-
1227 targeting control sequence (NT). Data represent mean ± standard error of the means (s.e.m.)
1228 from 5 independent experiments, each represented by dots. Significance was calculated relative
1229 to corresponding conditions for NT control cells using unpaired Student’s t-test where *p < 0.05
1230 and **p < 0.01. (h) Stimulation Index (SI) for shRNA gene knockdowns, calculated from high vs.
β
1231 low glucose insulin secretion measured in panel (g). (i) EndoC- H3 cell viability (assessed via
1232 Annexin V and 7-AAD staining) showing relative percentages of viable, early- or late-apoptotic,
1233 or necrotic cells after shRNA knockdown of selected genes or NT control. Data represent mean
1234 ± s.e.m. from 5 independent flow cytometry experiments, each represented by dots.
1235 Significance was assessed relative to corresponding measures in NT cells; *p < 0.05 and **p <
1236 0.01; Student’s t-test.
1237
β
1238 Figure 3: Integrated multimodal analyses prioritize T2D -cell differentially expressed
1239 genes as candidate causal/driver genes.
1240 (a) Comparison of islet eQTL effect sizes from TIGER consortium41 (y-axis) vs. fold-change in
β
1241 gene expression for T2D -cell differentially expressed genes (DEGs, x-axis) from this study.
1242 Red denotes genes with consistent T2D genetic and disease state effects on expression. Upper
1243 right quadrant genes are concordantly upregulated; lower left quadrant genes are concordantly
β
1244 downregulated. Gray denotes genes with opposite islet eQTL vs. T2D -cell differential
1245 expression effects. Blue denotes genes with multiple T2D genetic association signals exhibiting
1246 concordant and discordant islet eQTL effects. (b) Comparison of T2D differentially abundant
β
1247 proteins in Humanislets56 database (y-axis) and T2D -cell DEGs (x-axis). Red and gray denote
β
1248 genes with concordant or discordant -cell RNA and islet protein level differences in T2D vs. ND
β
1249 individuals, respectively. (c) T2D -cell DEGs significantly associated with various glycemic
1250 phenotypes in whole-body knockout (KO) mice from the IMPC62 consortium data. Log fold
2
β
1251 change (FC) gene expression in T2D vs. ND -cells (x-axis) compared to Log fold change in
2
44

bioRxiv preprint doi: https://doi.org/10.1101/2025.01.17.633590; this version posted January 22, 2025. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under a CC-BY-ND 4.0 International license.
1252 trait measure in KO mice vs. wild-type mice (y-axis). Circles or diamonds distinguish glucose
1253 tolerance (area under glucose response curve and initial response to glucose challenge) vs.
1254 fasting glucose phenotypes, respectively. Red denotes genes with KO glycemic phenotypes
1255 consistent with T2D physiology while gray genes indicate a T2D-misaligned defect. (d) IMPC
β
1256 glucose homeostasis phenotypes of known diabetes gene (Abcc8 and Kcnj11) and T2D -cell DEG
1257 KO mice compared to wildtype controls. Glucose tolerance measured by initial response to glucose
1258 challenge and/or area under the glucose response curve from an intraperitoneal glucose tolerance
1259 test (IPGTT). See Supplementary Table 14 for individual measures.
1260
β
1261 Figure 4: -cell subpopulation differences in T2D vs. ND and PD islets.
β
1262 (a) Sub-clustering analysis of 99,029 -cell transcriptomes reveals eight putative
β
1263 subpopulations. n=number of cells in each sub-population. (b) Dot-and-box plots showing -cell
1264 sub-population distributions in ND, PD, and T2D samples. (c) Heatmap of scaled marker gene
β
1265 expression (rows; y-axis) for each -subcluster (x-axis) aggregated by donors (columns). For
1266 each subpopulation, donor profiles are grouped into ND (light gray), PD (dark gray), and T2D
1267 (black) states, and then sorted based on ascending HbA1c levels. Enriched biological
1268 processes (left) associated with representative differentially expressed genes (right) are shown
β
1269 for each subpopulation. (d) Dot-and-box plots comparing per-donor percentages of each -cell
1270 subpopulation in ND, PD, or T2D individuals. Each dot represents a donor. Bonferroni-adjusted
1271 p values from Tukey's honestly significant difference test are reported for significant differences;
1272 ns=not significant. (e) UMAP plots illustrating inversely correlated changes in cluster 1
β
1273 (decreasing) and cluster 7 (increasing) cells within the bulk -cell cluster from ND to PD to T2D
1274 states.
1275
1276
1277
45

bioRxiv preprint doi: https://doi.org/10.1101/2025.01.17.633590; this version posted January 22, 2025. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under a CC-BY-ND 4.0 International license.
Figure 1
| a   |     | b   |                   |     |
| --- | --- | --- | ----------------- | --- |
| c   |     |     | Total cell count  |     |
245,878
|     | ND donors      |     | PD donors      | T2D donors      |
| --- | -------------- | --- | -------------- | --------------- |
|     | (88,521 cells) |     | (79,575 cells) |  (77,782 cells) |
d
e f
Copy of Data 1.tiff
2_PAMU
UMAP_1
| d   |     |     | e   |     |
| --- | --- | --- | --- | --- |
beta
)71( sronod DN alpha
delta
gamma
)41( sronod DP
|     |     | f   | g   |     |
| --- | --- | --- | --- | --- |
)71( sronod D2T
| 0 20 | 40 60 | 80 100 |     |     |
| ---- | ----- | ------ | --- | --- |
% of endocrine cells

a
d
Gene-set Enriched Pathway FDR q value
Neuroactive ligand-receptor interaction 3.9 ✕10-4
Upregulated g
genes
ECM-receptor interaction 9.2 ✕10-4
Vitamin A and carotenoid metabolism 1.5 ✕10-3
Downregulated
genes Copy of Data 1.tiff
Maturity onset diabetes of the young (MODY) 2.1 ✕10-3
e
ND donors T2D donors
Neuroactive
ligand-
receptor
interaction
ECM-receptor
interaction
Vitamin A
and
carotenoid
metabolism g
MODY
Row
Z-score -2 0 2
f
log2 (Fold change) log2 (Fold change)
)eulav
P
detsujda-RDF(01gol-
1.3
-0.5 0.5
)eulav
P
detsujda-RDF(01gol-
b
log2 (Fold change)
h
i
β-cells ⍺-cells
)eulav
q
RDF(01gol-
bioRxiv preprint doi: https://doi.org/10.1101/2025.01.17.633590; this version posted January 22, 2025. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under a CC-BY-ND 4.0 International license.
Figure 2
c
316 ↑
195 ↓
-0.59 0.59

3
erugiF
bioRxiv preprint doi: https://doi.org/10.1101/2025.01.17.633590; this version posted January 22, 2025. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under a CC-BY-ND 4.0 International license.

bioRxiv preprint doi: https://doi.org/10.1101/2025.01.17.633590; this version posted January 22, 2025. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under a CC-BY-ND 4.0 International license.
Figure 4
a b
| Total β-cell counts  | ND             |     |                | PD  | T2D            |
| -------------------- | -------------- | --- | -------------- | --- | -------------- |
| 99,029               | (39,484 cells) |     | (35,679 cells) |     | (23,866 cells) |
2_PAMU
UMAP_1
2_PAMU
d
UMAP_1
c
e
Cluster 1
|     |     | ND            |     | PD            | T2D           |
| --- | --- | ------------- | --- | ------------- | ------------- |
|     |     | (9,904 cells) |     | (7,576 cells) | (3,409 cells) |
2_PAMU
UMAP_1
Cluster 7
|     |     |               | ND  | PD            | T2D           |
| --- | --- | ------------- | --- | ------------- | ------------- |
|     |     | (2,540 cells) |     | (2,690 cells) | (4,122 cells) |
2_PAMU
UMAP_1

bioRxiv preprint doi: https://doi.org/10.1101/2025.01.17.633590; this version posted January 22, 2025. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under a CC-BY-ND 4.0 International license.
a c
b
Supplementary Figure 1: Quality control measures of single cell transcriptomes from each
donor. (a) Percent of cells retained (y-axis) for non-diabetic (ND), prediabetic (PD) or type 2
diabetic (T2D) donors after each filtering step (x-axis); each dot represents a donor. Bonferroni-
adjusted p-values from Tukey's honest significance test are shown. (b) Stacked bar plot
indicating number of cells retained (y-axis) per donor (x-axis) after each QC filtering step.
Samples with multiplexed runs are typed in bold; 10X sequencing v2 chemistry runs are
italicized. (c) UMAPs of single cell transcriptomes after preliminary filtering before and after
batch correction for sequencing chemistry, sex, and ancestry.

Columns
Supplementary Figure 2: Heatmap of aggregated (pseudobulk) marker gene expression (left;
rows) representing enriched GO terms (right) for each islet cell type (columns). Individual islet
donors are grouped by glycemic status (grayscale) and sorted from lowest to highest reported
HbA1c levels (yellow-blue gradient) for each cell type and glycemic status shown . ND: Non-
diabetic, PD: prediabetic, T2D: Type 2 diabetic. Full set of enriched marker genes and GO terms
for each cell type are provided in Supplementary Table 3 and 4.
swoR
bioRxiv preprint doi: https://doi.org/10.1101/2025.01.17.633590; this version posted January 22, 2025. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under a CC-BY-ND 4.0 International license.

bioRxiv preprint doi: https://doi.org/10.1101/2025.01.17.633590; this version posted January 22, 2025. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under a CC-BY-ND 4.0 International license.
| Alpha cells         | Beta cells          | Delta cells |     |
| ------------------- | ------------------- | ----------- | --- |
| r = 0.65; p = 0.067 | r = 0.74; p = 0.022 |             |     |
r = 0.62; p = 0.098
ND (9 donors)
)detroper-PPIH( sllec enircodne fo %
r = 0.43; p = 0.14
| r = 0.81; p = 0.0012 | r = 0.7; p = 0.007 |     | PD (13 donors) |
| -------------------- | ------------------ | --- | -------------- |
r = 0.82; p = 0.012
r = 0.74; p = 0.046
|     | r = 0.73; p = 0.04 |     | T2D (8 donors) |
| --- | ------------------ | --- | -------------- |
% of endocrine cells (our study)
Supplementary Figure 3: Scatter plots of spearman correlation (r) between alpha, beta, and
delta cell endocrine proportions reported by the the Human Islet Phenotyping Program (HIPP, y-
axis) for 9 Non-diabetic (ND), 13 prediabetic (PD), and 8 type 2 diabetic donors and as detected
by our scRNA-seq counts (x-axis) from the corresponding donors. The identity line (dashed) and
the line of fitted linear regression model (solid blue) are shown.

bioRxiv preprint doi: https://doi.org/10.1101/2025.01.17.633590; this version posted January 22, 2025. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under a CC-BY-ND 4.0 International license.
a
| b   | d   |     |
| --- | --- | --- |
T2D- DEGs
|     | Reported in      | Identified in  |
| --- | ---------------- | -------------- |
|     | previous studies | current study  |
|     | 3628 171         | 340            |
|     | Reported studies | PubMed IDs     |
| c   | Bacos_2023       | 36656641       |
|     | Bosi_2020        | 33575641       |
|     | Elgamal_2023     | 37582230       |
|     | Fadista_2014     | 25201977       |
|     | Fang_2019        | 30865899       |
|     | Lawlor_2017      | 27864352       |
|     | Marselli_2020    | 33264613       |
|     | Segerstolpe_2016 | 27667667       |
|     | Solimena_2018    | 29185012       |
|     | Taneera_2015     | 25489054       |
|     | Wang_2016        | 27364731       |
|     | Weng_2023        | 37669939       |
|     | Xin_2016         | 27667665       |
Supplementary Figure 4: UpSet plots showing overlap between the identified T2D vs ND β-cell
differentially expressed genes (DEGs) with previously reported DEGs –  β-cell scRNA-seq (a),
islet RNA-seq (b), and sorted β-cell RNA-seq (c). Overlaps containing at least 2 common genes
are shown. (d) Venn diagram showing our replication of 171 previously reported genes and
identification of 340 novel T2D-DEGs in current study.

bioRxiv preprint doi: https://doi.org/10.1101/2025.01.17.633590; this version posted January 22, 2025. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under a CC-BY-ND 4.0 International license.
a
*
*
*
*
*
*
*
*
*
*
Supplementary Figure 5: Primary pathways associated with T2D β-cell differentially expressed
genes (DEGs). (a) ‘Neuroactive ligand receptor interaction’ enrichment in upregulated genes.
* marks identified T2D β-cell DEGs in the pathways. Image sources: KEGG and Wikipathways.

bioRxiv preprint doi: https://doi.org/10.1101/2025.01.17.633590; this version posted January 22, 2025. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under a CC-BY-ND 4.0 International license.
b
*
* *
*
*
*
*
*
Supplementary Figure 5(b) ‘Vitamin A and carotenoid metabolism’ in downregulated genes.
* marks identified T2D β-cell DEGs in the pathways. Image sources: KEGG and Wikipathways.

bioRxiv preprint doi: https://doi.org/10.1101/2025.01.17.633590; this version posted January 22, 2025. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under a CC-BY-ND 4.0 International license.
Supplementary Figure 6: Genomic locus snapshots of β-cell death-related DEGs, highlighting
the presence of retinoic acid (RA) response elements and RA receptor (RXRA) binding. These
elements regulate the expression of RA target genes. Data source: ENCODE TF ChIp-seq,
UCSC Genome Browser.

bioRxiv preprint doi: https://doi.org/10.1101/2025.01.17.633590; this version posted January 22, 2025. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under a CC-BY-ND 4.0 International license.
Supplementary Figure 7: shRNA mediated knockdown of selected T2D-downregulated β-cell
genes in human EndoC-βH3 cells. Gene expression is shown relative to that in non-targeting
(NT) shRNA transduced cells. INS was tested as a positive control. Whiskers represent
minimum and maximum knockdown efficiencies from 5 independent experiments.

bioRxiv preprint doi: https://doi.org/10.1101/2025.01.17.633590; this version posted January 22, 2025. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under a CC-BY-ND 4.0 International license.
a b c
d
American
e f
Supplementary Figure 8: UMAPs of alpha-cell subpopulations shown for each glycemic status
(a), sex (b), scRNA sequencing chemistry (c; v2 or v3), and self-reported ancestry (d;
European, African American and Hispanic). Number of cells per cluster (n) is indicated in
parentheses. (e) Heatmap of normalized marker gene expression in alpha-cell subpopulations.
(f) Putative ⍺-cell subpopulation proportions in non-diabetic (ND; n = 17), prediabetic (PD; n =
14) and type 2 diabetic (T2D; n = 17) donors. Individual dots display per-donor proportions in
each group. P-values between groups are calculated from Tukey's honestly significance test,
adjusting for Bonferroni correction.

bioRxiv preprint doi: https://doi.org/10.1101/2025.01.17.633590; this version posted January 22, 2025. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under a CC-BY-ND 4.0 International license.
a b c
d
American
d
e f
Supplementary Figure 9: UMAPs of delta-cell subpopulations shown for each glycemic status
(a), sex (b), scRNA sequencing chemistry (c; v2 or v3), and self-reported ancestry (d;
European, African American and Hispanic). Number of cells per cluster (n) is indicated in
parentheses. (e) Heatmap of normalized marker gene expression in delta-cell subpopulations.
(f) Putative 𝝳-cell subpopulation proportions in non-diabetic (ND; n = 17), prediabetic (PD; n =
14) and type 2 diabetic (T2D; n = 17) donors. Individual dots display per-donor proportions in
each group. P-values between groups are calculated from Tukey's honestly significance test,
adjusting for Bonferroni correction.

bioRxiv preprint doi: https://doi.org/10.1101/2025.01.17.633590; this version posted January 22, 2025. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under a CC-BY-ND 4.0 International license.
a b
c
American
d
Supplementary Figure 10: a) UMAPs of putative beta-cell subpopulations shown for each sex
(a), scRNA sequencing chemistry (b; v2 and v3), and self-reported ancestry (c; European,
African American and Hispanic). d) Heatmap of scaled expression of previously reported beta-
cell subpopulation marker genes72,74-78,95,96 in this study.