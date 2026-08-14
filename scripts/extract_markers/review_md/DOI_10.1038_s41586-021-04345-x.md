1 Local and systemic responses to SARS-CoV-2 infection in children and adults
2
3 Masahiro Yoshida*1,7, Kaylee B. Worlock*1, Ni Huang*2, Rik G.H. Lindeboom*2, Colin R.
4 Butler5, Natsuhiko Kumasaka2, Cecilia Dominguez Conde2, Lira Mamanova2, Liam Bolt2,
5 Laura Richardson2, Krzysztof Polanski2, Elo Madissoon2,10, Josephine L. Barnes1, Jessica Allen-
6 Hyttinen1, Eliz Kilich3, Brendan C. Jones5, Angus de Wilton3, Anna Wilbrey-Clark2,
7 Waradon Sungnak2, J. Patrick Pett2, Juliane Weller2, Elena Prigmore2, Henry Yung1,3,
8 Puja Mehta1,3, Aarash Saleh4, Anita Saigal4, Vivian Chu4, Jonathan M. Cohen3, Clare Cane4,
9 Aikaterini Iordanidou4, Soichi Shibuya5, Ann-Kathrin Reuschl6, Iván T. Herczeg1, A. Christine
10 Argento8, Richard G. Wunderink8, Sean B. Smith8, Taylor A. Poor8, Catherine A. Gao8,
11 Jane E. Dematte8, NU SCRIPT Study Investigators8, Gary Reynolds13, Muzlifah Haniffa2,13,
12 Georgina S. Bowyer11, Matthew Coates11,12, Menna R. Clatworthy2,11, Fernando J. Calero-
13
Nieto9,
14 Berthold Göttgens9, Christopher O’Callaghan5, Neil J. Sebire5, Clare Jolly6, Paolo de Coppi5,
15 Claire M. Smith5, Alexander V. Misharin8, Sam M. Janes1,3, Sarah A. Teichmann2,14,
16 Marko Z. Nikolić 1,3 † & Kerstin B. Meyer2†
17
18 * These authors contributed equally, † These authors jointly supervised this work
19 Correspondence to: m.nikolic@ucl.ac.uk, km16@sanger.ac.uk
20
21 Affiliations
22 1UCL Respiratory, Division of Medicine, University College London, London, UK
23 2Wellcome Sanger Institute, Cambridge, UK
24 3University College London Hospitals NHS Foundation Trust, London, UK
25 4Royal Free Hospital NHS Foundation Trust, London, UK
26 5NIHR Great Ormond Street BRC and UCL Institute of Child Health, London, UK
27 6UCL Division of Infection and Immunity, University College London, London, UK
28 7Division of Respiratory Diseases, Department of Internal Medicine, Jikei University School of
29 Medicine, Tokyo, Japan
30 8Division of Pulmonary and Critical Care Medicine, Northwestern University Feinberg School of
31 Medicine, Chicago, USA
32 9Wellcome - MRC Cambridge Stem Cell Institute, University of Cambridge, Cambridge, UK
33 10European Molecular Biology Laboratory - European Bioinformatics Institute, Cambridge, UK
34 11Department of Medicine, University of Cambridge, Cambridge Biomedical Campus, UK
35 12Cambridge University Hospitals NHS Foundation Trust, Cambridge, UK
36 13Biosciences Institute, Newcastle University, Newcastle upon Tyne, UK
37 14Dept Physics/Cavendish Laboratory, University of Cambridge, JJ Thomson Ave, Cambridge
38 CB3 0HE, UK
39
1

40
41 Abstract
42 It is not fully understood why COVID-19 is typically milder in children1-3. To examine
43 differences in response to SARS-CoV-2 infection in children and adults, we analysed paediatric
44 and adult COVID-19 patients and healthy controls (total n=93) using single-cell multi-omic
45 profiling of matched nasal, tracheal, bronchial and blood samples. In healthy paediatric airways,
46 we observed cells already in an interferon-activated state, that upon SARS-CoV-2 infection was
47 further induced especially in airway immune cells. We postulate that higher paediatric innate
48 interferon-responses restrict viral replication and disease progression. The systemic response in
49 children was characterised by increases in naive lymphocytes and a depletion of natural killer
50 cells, while in adults cytotoxic T cells and interferon-stimulated subpopulations were
51 significantly increased. We provide evidence that dendritic cells initiate interferon signaling in
52 early infection, and identify novel epithelial cell states that associate with COVID-19 and age.
53 Our matching nasal and blood data showed a strong interferon response in the airways with the
54 induction of systemic interferon-stimulated populations, which were massively reduced in
55 paediatric patients. Together, we provide several mechanisms that explain the milder clinical
56 syndrome observed in children.
57
58
59 Introduction
60 Severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2) infections in children present
61 with milder disease severity compared to adults1,2. The overall risk of severe coronavirus disease
62 2019 (COVID-19) in children is even lower than originally believed, with around 2 deaths per
63 million3. The molecular basis of the differences in disease progression between children and
64 adults is not understood and may hold clues for better treatment of severe SARS-CoV-2
65 infection.
66
67 SARS-CoV-2 employs a host cell surface protein, angiotensin-converting enzyme (ACE) 2, as a
68 receptor for cellular entry4. Studies suggested that ACE2 expression is both tissue and age-
69 dependent5,6, with the highest expression found in nasal epithelium of healthy adults7 and
70 comparatively lower expression in paediatric upper8 and lower airways6,9. These differences
2

71 were proposed to contribute to reduced disease severity in children although recent studies have
72 found no correlation with age or infection10,11.
73
74 During the initial antiviral immune response, interferon (IFN) is important in inhibiting viral
75 replication, contributing to both innate and cell-intrinsic immunity12,13. Severe COVID-19 in
76 adults has been linked to an impaired antiviral response in nasal epithelium and blood14–16,
77 whereas several other studies highlight the contribution of the IFN response to the
78
pathogenesis17,18.
79
80 As the virus spreads, 14% of symptomatic, unvaccinated adults develop progressive respiratory
81 failure displaying a strong inflammatory immune response19. Single cell analysis of this response
82 in adults demonstrated the involvement of various immune cell types, including proinflammatory
83 monocytes/macrophages20, clonally expanded cytotoxic T cells21–23 and neutrophils21. However,
84 the cell-specific immune responses in children have not been comprehensively characterised.
85 Studies comparing bulk RNA sequencing and cytokine profiles between children and adults
86 suggest a more robust immune response, such as increased levels of IFN-γ and interleukin-17
87 (IL-17A) in plasma24, and a reduced antibody response and neutralising activity against SARS-
88 CoV-2 in children25. The most recent single-cell transcriptional study analysing upper airways of
89 mild COVID-19 children revealed that higher expression of pattern recognition receptor
90 pathways was related to a stronger innate immune response11. However, differences in the
91 coordination of local and systemic immune responses to SARS-CoV-2 between children and
92 adults including severe patients remains to be elucidated.
93
94 To address these questions and identify paediatric-specific responses in COVID-19, we collected
95 matched nasal, tracheal, bronchial and blood samples from healthy and COVID-19 patients from
96 infancy to adulthood and analysed them with single cell transcriptomics combined with protein
97 profiling.
98
99 Results
100
101 Study cohort and experimental overview
3

102 Using single cell RNA sequencing and CITE-seq we examined the effects of COVID-19 in
103 children versus adults, comparing the airway and systemic responses. We recruited 19 paediatric
104 and 18 adult COVID-19 patients, ranging from asymptomatic to severe, and 41 healthy children
105 and adults, to profile the cellular landscape in airways (nasal, tracheal and bronchial brushings)
106 and in matching peripheral blood mononuclear cells (PBMCs) (Fig. 1a, Extended Data Fig.
107 1a,b). For 6 COVID-19 patients blood was also taken at hospital discharge and 15 post-COVID-
108 19 patients (3 months post-severe disease) contributed nasal and/or blood samples. Patient
109 characteristics and metadata are summarised in Extended Data Table 1.
110
111 In total, we generated a dataset of 659,217 cells (see https://www.covid19cellatlas.org/ for easy
112 interactive analysis). We characterised the epithelial and immune cell compartments at great
113 granularity, identifying 59 different, including novel, cell types and states in airways (Fig. 1b,c,
114 Extended Data Fig. 2a,b) and 34 cell types in blood, mostly based on established markers23,26.
115
116 Novel cell subtypes in airway epithelia
117 The detailed cell type annotation is described in Supplementary Note, with marker genes and
118 comparison to existing data sets in Extended Data Fig. 2c and 3a-d. Multiple basal, goblet,
119 ciliated and transit epithelial 1 and 2 (secretory to ciliated) cell types reflect the plasticity of the
120 airway compartment26–28, with the main differentiation pathways visualised in Fig. 1d. Notably,
121 transit epithelial 1 cells occur mostly in COVID-19 patients, but also in healthy children
122 (Extended Data Fig. 2a) suggesting a function in development and tissue regeneration.
123 Compared to published adult nasal datasets sets14,28, we annotate cell types with greater
124 granularity, especially for B and T lymphocytes, and we identify three Hillock-like
125 populations14,26,27. The latter are all marked by KRT14, KRT6A and KRT13, which form a distinct
126 differentiation trajectory (Fig. 1d) similar to the one reported in mouse27. Additionally,
127 monocytes fall into clearly distinct clusters, annotated by their highly expressed markers as mono
128 IL-6+, mono GPBAR1+ and mono CXCL10+, and mostly derived from COVID-19 neonates
129 (Fig. 1c, Extended Data Fig. 2a, 3a).
130
131 SARS-CoV-2 reads in airway epithelium
4

132 (cid:890)(cid:927)(cid:849)(cid:884)(cid:896)(cid:903)(cid:890)(cid:885)(cid:862)(cid:866)(cid:874)(cid:849)(cid:929)(cid:928)(cid:932)(cid:922)(cid:933)(cid:922)(cid:935)(cid:918)(cid:849)(cid:927)(cid:914)(cid:932)(cid:914)(cid:925)(cid:849)(cid:932)(cid:914)(cid:926)(cid:929)(cid:925)(cid:918)(cid:932)(cid:861)(cid:849)(cid:936)(cid:918)(cid:849)(cid:917)(cid:918)(cid:933)(cid:918)(cid:916)(cid:933)(cid:918)(cid:917)(cid:849)(cid:935)(cid:922)(cid:931)(cid:914)(cid:925)(cid:849)(cid:931)(cid:918)(cid:914)(cid:917)(cid:932)(cid:849)(cid:857)(cid:927)(cid:1541)(cid:866)(cid:865)(cid:858)(cid:849)(cid:922)(cid:927)(cid:849)
133 (cid:866)(cid:865)(cid:864)(cid:867)(cid:873)(cid:849) (cid:929)(cid:914)(cid:933)(cid:922)(cid:918)(cid:927)(cid:933)(cid:932)(cid:861)(cid:849) (cid:936)(cid:922)(cid:933)(cid:921)(cid:849) (cid:933)(cid:921)(cid:918)(cid:849) (cid:921)(cid:922)(cid:920)(cid:921)(cid:918)(cid:932)(cid:933)(cid:849) (cid:925)(cid:918)(cid:935)(cid:918)(cid:925)(cid:932)(cid:849) (cid:919)(cid:928)(cid:934)(cid:927)(cid:917)(cid:849) (cid:922)(cid:927)(cid:849) (cid:929)(cid:914)(cid:933)(cid:922)(cid:918)(cid:927)(cid:933)(cid:932)(cid:849) (cid:932)(cid:914)(cid:926)(cid:929)(cid:925)(cid:918)(cid:917)(cid:849)
134 (cid:916)(cid:925)(cid:928)(cid:932)(cid:918)(cid:932)(cid:933)(cid:849)(cid:933)(cid:928)(cid:849)(cid:918)(cid:932)(cid:933)(cid:922)(cid:926)(cid:914)(cid:933)(cid:918)(cid:917)(cid:849)(cid:928)(cid:927)(cid:932)(cid:918)(cid:933)(cid:849)(cid:928)(cid:919)(cid:849)(cid:922)(cid:927)(cid:919)(cid:918)(cid:916)(cid:933)(cid:922)(cid:928)(cid:927)(cid:849)(cid:857)Fig. 1e). After filtering ambient RNA,
135 cell types with the highest proportion of viral reads were goblet 2 inflammatory cells, followed
136 by cycling basal, transit epithelial and ciliated cells (Fig. 1f), largely mirroring ACE2 expression
137 (Extended Data Fig. 4). Viral reads were also detected in lymphocytes and myeloid cells
138 (mostly macrophages), either reflecting active infection in macrophages29 or merely uptake of
139 virions or infected cells. The expression of SARS-CoV-2 viral entry and associated factors,
140 including ACE2 was similar between children and adults, with few genes correlating with active
141 viral infection (Extended Data Fig. 4a,b). In adults, ACE2 expression is induced by IFN30 and
142 in response to infection28, but we observe no significant increase of ACE2 expression in children
143 with COVID-19 (Extended Data Fig. 4c), consistent with recent bulk RNAseq comparisons10.
144 As reported31,32, no SARS-CoV-2 viral reads were detected in peripheral blood.
145
146 Airway cell type proportions in COVID-19
147 We next examined changes in cell type proportions for location, age group and COVID-19 status
148 in all airway cell populations (Fig. 2a, Extended Data Fig. 5a,b). To test significance, we used a
149 Poisson linear mixed model (see Methods) allowing us to test the whole cohort in a single
150 analysis while taking into account clinical metadata and technical factors (Extended Data Fig.
151 5b). Airway epithelial cell type composition showed trends of decreasing basal 1 and increasing
152 secretory and goblet cells with age (Extended Data Fig. 3e), reflecting developmental
153 trajectories from progenitors to differentiated cells (Fig. 1d). Notably, there were significant
154 changes with location, as previously reported33.
155
156 Contrasting epithelial cells in COVID-19 versus healthy adults, the most highly enriched cell
157 types are transit epithelial 1 and goblet 2 inflammatory cells (Fig. 2a, for all cell types see
158 Extended Data Fig. 5a). We hypothesise that increased transit epithelial cell numbers reflect a
159 compensatory replacement of dying ciliated cells14,34 by their precursors, to maintain
160 homeostasis upon infection as seen in lower airways35,36, and consistent with trajectory analysis
161 (Fig. 1d). This is further supported by the return to healthy cell population levels in the post-
5

162 COVID-19 patients (Fig. 2a). In adults, proportions of nasal immune cells were not significantly
163 changed in COVID-19.
164
165 In children epithelial cell proportions did not change, but in the immune compartment IL6+
166 monocytes were significantly enriched in COVID-19, with a trend towards higher mono
167 CXCL10+ cells and neutrophils. We also observed changes in immune cell populations over
168 healthy childhood (Fig. 2a), such as high monocytes and low CD8 T cell levels in infants, and
169 expansion of B cell populations in young children, reflecting a switch from innate to adaptive
170
immunity37.
171
172 Distinct changes in children and adults
173 We next examined gene expression changes in children versus adults, in healthy, COVID-19 and
174 post-COVID-19 patients. In nasal epithelial cells, the biggest changes were observed for gene
175 expression signatures associated with IFN-α signalling (Fig. 2b). Healthy adults had the lowest
176 IFN-α response that was strongly induced in COVID-19 and returned to pre-infection levels in
177 post-COVID-19 patients. In children, this gene signature was already activated and only
178 increased slightly upon infection. These patterns were repeated for signatures of IFN-γ response,
179 TNF-α signalling and neutrophil migration, albeit with smaller fold-changes. For nasal immune
180 cells, the induction of the IFN-α response signature was higher in children than adults. The other
181 signatures examined also showed greater induction in children than in adults.
182
183 Examining these responses by cell types in healthy children versus adults, the IFN response
184 signatures were already activated in children across several epithelial cell types, with highest
185 levels in goblet inflammatory cells, Hillock precursors and rare melanocytes (Fig. 2c; Extended
186 Data Fig. 5c for absolute values per cell type). However, SARS-CoV-2 induced IFN responses
187 were higher in adults across many epithelial cell types. For the immune cells in healthy children
188 many cell types had elevated IFN response signatures compared to adults, particularly NK CD56
189 lo, NKT cells, neutrophils, mono CXCL10+ and some CD8+ T cell subsets for IFN-α, and a
190 wider range for IFN-γ (Fig. 2d). Upon infection we saw greater induction of these responses in
191 immune cells in children, most prominently in monocytes, including in the already expanded
192 IL6+ monocytes, CD4 CCR4+ T cells and Tfh cells.
6

193
194 In adults with COVID-19, a higher systemic IFN response has been reported for non-severe
195 disease14,38,39. We confirmed this across disease severity in our adult cohort for the local
196 response, finding a higher IFN-α response in asymptomatic/mild versus moderate/severe disease
197 in both epithelial and immune cells (Fig. 2e). In children this phenomenon was much stronger in
198 immune versus epithelial cells. These data suggest that in both children and adults a strong local
199 IFN response is associated with milder disease severity, presumably because interferons inhibit
200 viral replication13. However, in children this local response is pre-activated in epithelial cells and
201 stronger in immune cells, providing better protection against the virus.
202
203 We next examined differential gene expression patterns in healthy versus COVID-19 samples,
204 followed by GO term enrichment, in cell types particularly associated with disease: transit
205 epithelial 1 and goblet 2 inflammatory cells upregulated in adult COVID-19, and IL-6 monocytes
206 upregulated in children, as strong IFN-α responders (Fig. 2f). For transit epithelial cells, this
207 highlighted the IFN type I and II response as well as neutrophil chemotaxis, a striking finding
208 given that neutrophil infiltration is linked to COVID-19 severity40. The neutrophil recruitment
209 signature was driven by S100A8 and S100A9 expression (calprotectin) (Extended Data Fig. 5d),
210 also a key correlate of disease severity41. For goblet 2 inflammatory cells and mono IL-6+, the
211 top two terms were type I IFN signalling and negative viral replication. Enrichment of motile
212 cilium assembly is in line with our observation that in disease there appears to be higher cell
213 turnover with precursors such as secretory cells differentiating to replace dying ciliated cells.
214
215 As calprotectin expression has primarily been associated with myeloid cells, we validated
216 expression at the protein level in epithelial cells. Fig. 2g depicts double positive cells, staining
217 for both calprotectin subunit S100A9 and the epithelial marker EPCAM in a posterior nasal
218 space biopsy of an adult COVID-19 patient. At the RNA level, calprotectin is expressed across
219 different secretory cell types (Extended Data Fig. 3b).
220
221 Multi-omic blood immune landscape
222 Using CITE-seq and single cell profiling of blood from paediatric and adult COVID-19 patients,
223 we annotated 422,220 high-quality single cell transcriptomes from healthy, diseased and
7

224 recovered donors, into 34 blood cell types (Fig. 3a, marker expression and annotation validation
225 in Extended Data Fig. 6a-c). To investigate how the immune system responds to SARS-CoV-2,
226 and how age is affecting this response, we calculated fold-changes in cell type proportions that
227 can be attributed to disease state and age (Fig. 3b, Extended Data Fig. 6d-g). Importantly, our
228 Poisson linear mixed model enabled us to distinguish the immune dynamics that can be
229 attributed to technical effects, ageing and COVID-19. Furthermore, we included an interaction
230 between adulthood and disease status to uncover paediatric-specific immune responses to
231 COVID-19 (Fig. 3b). We observed higher plasma cell and plasmablast proportions, and a
232 reduction in the monocyte and dendritic cell compartment in the blood of both adult and
233 paediatric COVID-19 patients, as previously reported in adults21,23.
234
235 Reduced cytotoxic response in children
236 In contrast to the aforementioned cell types that change consistently in adults and children in
237 response to COVID-19, we observe opposing changes in the abundance of many other immune
238 cell types (Fig. 3b). The circulating immune system of adult COVID-19 patients is characterised
239 by an increased cytotoxic compartment, where CD8+ cytotoxic T lymphocytes (CTLs) and
240 effector memory cells re-expressing CD45RA are significantly more abundant in adults.
241 Strikingly, the latter populations, natural killer cells and CD4+ CTLs are reduced in paediatric
242 COVID-19 patients. Together, this could reflect a more systemic infection and inflammation in
243 adults, while the infection in paediatric patients remains more restricted to airways.
244
245 Naive T cells in children with COVID-19
246 In addition to a reduced cytotoxic cellular composition, we observe a striking increase of naive
247 lymphocytes in the blood of paediatric COVID-19 patients (Fig. 3b). High numbers of naive
248 cells may be attributed to increased release of immature B and T lymphocytes from the bone
249 marrow and thymus respectively, or due to migration of more mature cells to the site of
250 infection. With our statistical model and large healthy cohort, the strong effects of age on the
251 immune landscape were deconvoluted from the COVID-19 effects into independent age effects
252 and quantified in Fig. 3b. Interestingly, the strong maturation patterns and shift from innate to
253 adaptive immunity observed over healthy childhood amplifies some of the paediatric specific
254 COVID-19 responses, i.e. not only do children have a more naive and reduced cytotoxic
8

255 response to COVID-19, they also start off with an immune state that is already skewed towards
256 this response.
257
258 Diverse immune repertoire in children
259 As we detected more naive immune cells in children, we hypothesised that this could affect the
260 amount of unique T and B cell receptors (TCRs and BCRs) available to detect new pathogens.
261 Indeed, we observed that the pool of detected TCRs becomes increasingly dominated by
262 expanded clones over age (Fig. 3c, Extended Data Fig. 7a), reducing the amount of unique
263 TCRs available to detect unseen pathogens. It is therefore conceivable that higher TCR repertoire
264 diversity in children could contribute to a faster, more efficient adaptive immune response to
265 SARS-CoV-2.
266
267 IFN-stimulated cell subtypes in blood
268 When annotating our PBMC dataset, we noticed further cell type heterogeneity that generated
269 distinct clusters within all major immune cell types due to high expression of IFN-stimulated
270 genes (Fig. 3d, Extended Data Fig. 7b). Activation of IFN signaling is a key hallmark of
271 COVID-19, acting both as an important protective pathway that can equally be associated with
272 severe COVID-1942,15,43. While we and others reported an association between global changes in
273 IFN related gene expression and COVID-1923, our increased granularity allowed us to
274 distinguish multiple distinct stimulated and unstimulated populations alongside each other within
275 donors. Importantly, this shows that IFN stimulation of PBMCs does not lead to a global
276 activation of gene expression, but is restricted to a subset of circulating cells.
277
278 IFN response in early COVID-19
279 When investigating the COVID-19 IFN response, we found that IFN-stimulated NK, B, T and
280 HPC subpopulations are much more abundant in adult than in paediatric COVID-19 patients
281 (Fig. 3e,f). In adults, the amount of IFN-stimulated PBMCs strongly correlated with sampling
282 time since onset of symptoms (Fig. 3e). This suggests that IFN-stimulated PBMCs are a
283 characteristic of the acute phase of infection, when the innate immune response is trying to
284 control the viral infection. In children the correlation with onset of symptoms is completely
285 absent (Fig. 3e) but IFN-stimulated cells were abundant in some asymptomatic children
9

286 (Extended Data Fig. 7c), suggesting a much faster induction and clearance of IFN-stimulated
287 cells. Together, these observations support our hypothesis that COVID-19 induced inflammation
288 and cytotoxicity in blood is more abundant in adults than in children.
289
290 Dendritic cells initiate IFN response
291 To investigate the connection between the local and systemic immune response to SARS-CoV-2
292 we compared cell type proportions in blood and nose for multi-tissue donors and observed strong
293 correlations (Fig. 3g, all comparisons in Extended Data Fig. 7d-e). Particularly SARS-CoV-2-
294 infected and inflammatory nasal epithelial cells, and nasal plasmacytoid and conventional
295 dendritic cells (pDCs and cDCs) correlated with IFN stimulation in blood. This is interesting as
296 DCs are known for their viral sensing and IFN production capacities44, but this has not been
297 directly observed in COVID-19. While DCs protect against severe disease45, most COVID-19
298 studies that analyse blood reported a depletion of DCs46. However, here we provide evidence that
299 at the earliest stages of infection, type I and type III IFNs are detectable (Fig. 3h) and produced
300 by pDCs and cDCs, but not other immune or epithelial cells (Extended Data Fig. 8b and
301 Supplementary Note).
302
303
304 Discussion
305
306 We focused on why children are generally protected from severe COVID-19 and propose
307 multiple mechanisms (Fig. 4). First, we show that the airway epithelium has a higher steady-state
308 expression of IFN response genes in children. SARS-CoV-2 has been reported to be highly
309 sensitive to pre-stimulation with interferons47 and pre-activation may restrict viral spread in
310 children. Secondly, the systemic immune response in blood is characterised by a more naive
311 state. In contrast, adults display a highly cytotoxic immune compartment in blood, likely because
312 of failure to restrict viral spreading. This elevated systemic response in adults can lead to
313 widespread immune-related organ damage48. A third feature we observe is the higher TCR
314 repertoire diversity in children versus adults. The acquisition of memory T and B cells during
315 child- and adulthood, combined with reduced thymic output, shifts the adaptive immune system
316 into a more memory-based compartment in aged individuals49. This reduces the pool of unique
10

317 immune receptors within naive lymphocytes50, which makes it less probable that a high-affinity
318 immune receptor is directly available against SARS-CoV-2 antigens. Lastly, we uncovered novel
319 IFN-stimulated cell states in multiple blood cell lineages that are highly abundant in early disease
320 in adults. This presents an added inflammatory feature of the already cytotoxic immune
321 compartment in adult COVID-19 patients, and possibly amplifies any pathological effects of the
322 systemic immune response. The identification of both IFN stimulated and unstimulated blood
323 cells within donors underscores that activation is cell-specific rather than, as noted by others,
324 systemic, possibly caused by either close proximity to the site of infection or an associated
325 secondary lymphoid organ, or cell-to-cell variability in responsiveness as we have shown in
326 fibroblasts and phagocytes51.
327
328 SARS-CoV-2 infection frequently starts in the upper airways, where we found the highest total
329 viral load in surface epithelial goblet, ciliated and differentiating cells. Viral infections are
330 cleared by cell death and removal of infected cells52, which led to a highly dynamic re-
331 structuring of the airway epithelium with a marked increase in developmental intermediates,
332 most notably the transit epithelial populations, that are re-balanced post-infection. We also see a
333 strong neutrophil recruiting signature, driven by expression of calprotectin in epithelial cell
334 types, highlighting the key role of epithelial cells in initiating an innate immune response.
335
336 Overall, our study demonstrates multiple novel insights from paired multi-omics profiling of
337 both airway epithelium and peripheral blood to fill the gap in our understanding of paediatric
338 epithelial and immune responses to COVID-19, while also identifying novel cell states in both
339 airway epithelium and blood. These insights could contribute to pinpointing the triggers of
340 severe disease in adults with a view towards risk stratification and therapeutic intervention.
341
342
343 Acknowledgments
344
345 We acknowledge assistance from Lucy Thorne, Pei Shi Chia, Robert Hynds, Jana Eliasova,
346 Douglas King, Melanie Heightmann, Michael Marks, Malcolm Avari, Talisa Mistry, Marianne
347 Shaw-Taylor, Ruchira Pereira, Joseph Machta, Julian Lim, Ruth Prendecki, Claire Frauenfelder,
11

348 James Rudd, Andrew Hall and the Sanger Institute Core Sequencing facility. We thank Richard
349 Jenner and the UCLH/UCL Biomedical Research Centre for the use of their 10X Chromium
350 controller.
351
352 We acknowledge funding from Wellcome (WT211276/Z/18/Z and Sanger core grant
353 WT206194). M.Z.N, S.M.J and K.B.M have been funded by the Rosetrees Trust (M944, M35-
354 F2) and from Action Medical Research (GN2911). This project has been made possible in part
355 by grants 2017-174169 and 2019-202654 from the Chan Zuckerberg Foundation and has
356 received funding from the European Union’s Horizon 2020 research and innovation programme
357 under grant agreement No 874656. M.Z.N. acknowledges funding from the Rutherford Fund
358 Fellowship allocated by the MRC, and M.Z.N. and S.M.J. from the UK Regenerative Medicine
359 Platform 2 (MR/5005579/1), the Longfonds BREATH consortium and University College
360 London Hospitals Biomedical Research Centre. M.Y. is funded by The Jikei University School
361 of Medicine. KBW acknowledges funding from University College London, Birkbeck MRC
362 Doctoral Training Programme. C.M.S and M.Z.N. acknowledge support from BBSRC
363 (BB/V006738/1). S.S. was supported by a Japan Society for the Promotion of Science Overseas
364 Fellowship (310072). R.G.W. was supported by NIH grant U19AI135964 and a
365 GlaxoSmithKline Distinguished Scholar in Respiratory Health grant from the CHEST
366 Foundation. A.V.M. was supported by NIH grant U19AI135964.
367
368 This publication is part of the Human Cell Atlas - www.humancellatlas.org/publications/. For the
369 purpose of Open Access, the authors have applied a CC BY public copyright licence to any
370 Author Accepted Manuscript version arising from this submission.
371
372
373 Author contributions
374
375 M.Z.N. and K.B.M. conceived, set up and directed the study. C.B., E.K., A.W., B.J., A.Sai.,
376 H.Y., S.M.J., S.S., P.M., N.S., P.d.C., V.C., J.C., C.C., A.I., M.Z.N. recruited patients, collected
377 samples (where applicable also through bronchoscopies) and clinical metadata. K.B.W. and
378 M.Y. assisted with sample and meta-data collection, isolated PBMCs and performed single cell
12

379 isolation of nasal, tracheal and bronchial brushings. K.B.W. and M.Y. performed 10X and CITE-
380 seq, isolated DNA for genotyping. J.A.H. collected samples, performed single cell isolation and
381 10X (including CITE-seq) on post-COVID-19 samples. J.L.B. and I.T.H. helped with study set
382 up, CITE-seq and isolated DNA for genotyping. L.M., L.B., L.R. prepared sequencing libraries
383 and conducted the sequencing. E.P. co-ordinated sample shipment and meta-data collection.
384 N.H., R.G.H.L., N.K., C.D.C., E.M., K.P., P.J.P. and J.W. performed bioinformatic analysis.
385 M.Z.N., K.B.M., K.B.W., M.Y., R.G.H.L., N.H., N.K., C.D.C., E.M., W.S. interpreted the data.
386 K.P. facilitated online data hosting. G.R., M.H. provided help with PBMC annotation. N.J.S.,
387 B.J., S.S. provided stored healthy paediatric control nasal tissue blocks. M.C., G.B and M.C
388 carried out experiments to collect and stain post-nasal biopsies. F.J.C.N. and B.G. designed the
389 CITE-seq panel and advised on CITE-seq experimental design. K.B.M., M.Z.N., K.B.W., M.Y.,
390 R.G.H.L., N.H. wrote the manuscript. E.M., S.A.T., B.G., W.S., S.M.J., P.J.P., L.M. edited the
391 manuscript. C.S., C.O., P.d.C., S.M.J., C.B. provided support through ethics and patient
392 recruitment. C.J. and A.K.R. provided support in setting up and training for all CL3 work.
393 Northwestern (bronchial samples): A.C.A., C.A.G., G.R.S.B., J.E.D., R.G.W., S.B.S. and T.A.P.
394 performed bronchoscopies, collection of bronchial brushings and curation of clinical metadata.
395 A.V.M. performed sample processing and analysis. H.K.D obtained informed consent and
396 coordinated sample collection. N.S.M. performed analysis. Z.L. performed sample processing
397 and library construction.
398
399 These authors contributed equally: Masahiro Yoshida, Kaylee B. Worlock, Ni Huang, Rik G.H.
400 Lindeboom
401 These authors jointly supervised this work: Marko Z. Nikolić, Kerstin B. Meyer
402
403
404 Data availability
405
406 The data set from our study can be explored interactively through a web portal:
407 https://covid19cellatlas.org. Quality control metrics for our single cell data can be found at the
408 web portal page. The data object, as a h5ad file, can also be downloaded from the portal page.
409 The UK data set is available under accession number EGAD00001007718. Counts matrices from
13

410 bronchial brushings obtained from patients at Northwestern Memorial Hospital, Chicago, are
411 available at GEO, accession number GSE168215. As data is from living patients, these data will
412 be available under managed data access.
413
414
415 Code Availability
416
417 All data analysis scripts are available on https://github.com/Teichlab/COVID-19paed.
418
419
420 Competing interest statement
421
422 In the past three years, S.A.T has worked as a consultant for Genentech, Roche and Transition
423 Bio, and is a remunerated member of the Scientific Advisory Boards of Qiagen,
424 GlaxoSmithKline and Foresite Labs and an equity holder of Transition Bio. P.M. is a Medical
425 Research Council-GlaxoSmithKline (MRC-GSK) Experimental Medicine Initiative to Explore
426 New Therapies (EMINENT) clinical training fellow with project funding, has served on an
427 advisory board for SOBI, outside the submitted work, and receives co-funding by the National
428 Institute for Health Research (NIHR) University College London Hospitals Biomedical Research
429 Centre (UCLH BRC).
430
431
432
433 References
434 1. Swann, O. V. et al. Clinical characteristics of children and young people admitted to
435 hospital with covid-19 in United Kingdom: prospective multicentre observational cohort
436 study. BMJ 370, m3249 (2020).
437 2. Castagnoli, R. et al. Severe Acute Respiratory Syndrome Coronavirus 2 (SARS-CoV-2)
438 Infection in Children and Adolescents: A Systematic Review. JAMA Pediatr. 174, 882–889
14

439 (2020).
440 3. Ledford, H. Deaths from COVID ‘incredibly rare’ among children. Nature 595, 639–639
441 (2021).
442 4. Hoffmann, M. et al. SARS-CoV-2 Cell Entry Depends on ACE2 and TMPRSS2 and Is
443 Blocked by a Clinically Proven Protease Inhibitor. Cell 181, 271–280.e8 (2020).
444 5. Pang, L. et al. Influence of aging on deterioration of patients with COVID-19. Aging 12,
445 26248–26262 (2020).
446 6. Muus, C. et al. Single-cell meta-analysis of SARS-CoV-2 entry genes across tissues and
447 demographics. Nat. Med. 27, 546–559 (2021).
448 7. Sungnak, W. et al. SARS-CoV-2 entry factors are highly expressed in nasal epithelial cells
449 together with innate immune genes. Nat. Med. 26, 681-687 (2020).
450 8. Bunyavanich, S., Do, A. & Vicencio, A. Nasal Gene Expression of Angiotensin-Converting
451 Enzyme 2 in Children and Adults. JAMA 323, 2427–2429 (2020).
452 9. Saheb Sharif-Askari, N. et al. Airways Expression of SARS-CoV-2 Receptor, ACE2, and
453 TMPRSS2 Is Lower in Children Than Adults and Increases with Smoking and COPD. Mol
454 Ther Methods Clin Dev 18, 1–6 (2020).
455 10. Koch, C. M. et al. Age-related Differences in the Nasal Mucosal Immune Response to
456 SARS-CoV-2. Am. J. Respir. Cell Mol. Biol. (2021). doi:10.1165/rcmb.2021-0292OC.
457 11. Loske, J. et al. Pre-activated antiviral innate immunity in the upper airways controls early
458 SARS-CoV-2 infection in children. Nat. Biotechnol. (2021).
459 https://doi.org/10.1038/s41587-021-01037-9
460 12. Schultze, J. L. & Aschenbrenner, A. C. COVID-19 and the human innate immune system.
461 Cell 184, 1671–1692 (2021).
15

462 13. Schoggins, J. W. Interferon-Stimulated Genes: What Do They All Do? Annu Rev Virol 6,
463 567–584 (2019).
464 14. Ziegler, C. G. K. et al. Impaired local intrinsic immunity to SARS-CoV-2 infection in
465 severe COVID-19. Cell 184, 4713-4733.e22 (2021).
466 15. Hadjadj, J. et al. Impaired type I interferon activity and inflammatory responses in severe
467 COVID-19 patients. Science 369, 718–724 (2020).
468 16. Wang, E. Y. et al. Diverse functional autoantibodies in patients with COVID-19. Nature
469 595, 283–288 (2021).
470 17. Major, J. et al. Type I and III interferons disrupt lung epithelial repair during recovery from
471 viral infection. Science 369, 712–717 (2020).
472 18. Broggi, A. et al. Type III interferons disrupt the lung epithelial barrier upon viral
473 recognition. Science 369, 706–712 (2020).
474 19. Berlin, D. A., Gulick, R. M. & Martinez, F. J. Severe Covid-19. N. Engl. J. Med. 383,
475 2451–2460 (2020).
476 20. Liao, M. et al. Single-cell landscape of bronchoalveolar immune cells in patients with
477 COVID-19. Nat. Med. 26, 842–844 (2020).
478 21. Wilk, A. J. et al. A single-cell atlas of the peripheral immune response in patients with
479 severe COVID-19. Nat. Med. 26, 1070–1076 (2020).
480 22. Zhang, J.-Y. et al. Single-cell landscape of immunological responses in patients with
481 COVID-19. Nat. Immunol. 21, 1107–1118 (2020).
482 23. Stephenson, E. et al. Single-cell multi-omics analysis of the immune response in COVID-
483 19. Nat. Med. 27, 904–916 (2021).
484 24. Pierce, C. A. et al. Immune responses to SARS-CoV-2 infection in hospitalized pediatric
16

485 and adult patients. Sci. Transl. Med. 12, eabd5487 (2020).
486 25. Weisberg, S. P. et al. Distinct antibody responses to SARS-CoV-2 in children and adults
487 across the COVID-19 clinical spectrum. Nat. Immunol. 22, 25–31 (2021).
488 26. Deprez, M. et al. A Single-cell Atlas of the Human Healthy Airways. Am. J. Respir. Crit.
489 Care Med. 202, 1636–1645 (2020).
490 27. Montoro, D. T. et al. A revised airway epithelial hierarchy includes CFTR-expressing
491 ionocytes. Nature 560, 319–324 (2018).
492 28. Chua, R. L. et al. COVID-19 severity correlates with airway epithelium-immune cell
493 interactions identified by single-cell analysis. Nat. Biotechnol. 38, 970-979 (2020).
494 29. Grant, R. A. et al. Circuits between infected macrophages and T cells in SARS-CoV-2
495 pneumonia. Nature 590, 635–641 (2021).
496 30. Ziegler, C. G. K. et al. SARS-CoV-2 Receptor ACE2 Is an Interferon-Stimulated Gene in
497 Human Airway Epithelial Cells and Is Detected in Specific Cell Subsets across Tissues.
498 Cell 181, 1016–1035.e19 (2020).
499 31. Wang, W. et al. Detection of SARS-CoV-2 in Different Types of Clinical Specimens.
500 JAMA 323, 1843–1844 (2020).
501 32. Yu, F. et al. Quantitative Detection and Viral Load Analysis of SARS-CoV-2 in Infected
502 Patients. Clin. Infect. Dis. 71, 793–798 (2020).
503 33. Vieira Braga, F. A. et al. A cellular census of human lungs identifies novel cell states in
504 health and in asthma. Nat. Med. 25, 1153–1163 (2019).
505 34. Zhu, N. et al. Morphogenesis and cytopathic effect of SARS-CoV-2 infection in human
506 airway epithelial cells. Nat. Commun. 11, 3910 (2020).
507 35. Fang, Y. et al. Distinct stem/progenitor cells proliferate to regenerate the trachea,
17

508 intrapulmonary airways and alveoli in COVID-19 patients. Cell Res. 30, 705–707 (2020).
509 36. Ruiz García, S. et al. Novel dynamics of human mucociliary differentiation revealed by
510 single-cell RNA sequencing of nasal epithelial cultures. Development 146, dev177428
511 (2019).
512 37. Ygberg, S. & Nilsson, A. The developing immune system - from foetus to toddler. Acta
513 Paediatr. 101, 120–127 (2012).
514 38. Blanco-Melo, D. et al. Imbalanced Host Response to SARS-CoV-2 Drives Development of
515 COVID-19. Cell 181, 1036–1045.e9 (2020).
516 39. Chen, G. et al. Clinical and immunological features of severe and moderate coronavirus
517 disease 2019. J. Clin. Invest. 130, 2620–2629 (2020).
518 40. Aschenbrenner, A. C. et al. Disease severity-specific neutrophil signatures in blood
519 transcriptomes stratify COVID-19 patients. Genome Med. 13, 7 (2021).
520 41. Silvin, A. et al. Elevated Calprotectin and Abnormal Myeloid Cell Subsets Discriminate
521 Severe from Mild COVID-19. Cell 182, 1401–1418.e18 (2020).
522 42. Galani, I.-E. et al. Untuned antiviral immunity in COVID-19 revealed by temporal type I/III
523 interferon patterns and flu comparison. Nat. Immunol. 22, 32–40 (2021).
524 43. Lee, J. S. et al. Immunophenotyping of COVID-19 and influenza highlights the role of type
525 I interferons in development of severe COVID-19. Sci Immunol 5, eabd1554 (2020).
526 44. Diebold, S. S. et al. Viral infection switches non-plasmacytoid dendritic cells into high
527 interferon producers. Nature 424, 324–328 (2003).
528 45. Saichi, M. et al. Single-cell RNA sequencing of blood antigen-presenting cells in severe
529 COVID-19 reveals multi-process defects in antiviral immunity. Nat. Cell Biol. 23, 538–551
530 (2021).
18

531 46. Zhou, R. et al. Acute SARS-CoV-2 Infection Impairs Dendritic Cell and T Cell Responses.
532 Immunity 53, 864–877.e5 (2020).
533 47. Lokugamage, K. G. et al. Type I Interferon Susceptibility Distinguishes SARS-CoV-2 from
534 SARS-CoV. J. Virol. 94, (2020).
535 48. Schurink, B. et al. Viral presence and immunopathology in patients with lethal COVID-19:
536 a prospective autopsy cohort study. Lancet Microbe 1, e290–e299 (2020).
537 49. Kumar, B. V., Connors, T. J. & Farber, D. L. Human T Cell Development, Localization,
538 and Function throughout Life. Immunity 48, 202–213 (2018).
539 50. Naylor, K. et al. The influence of age on T cell generation and TCR diversity. J. Immunol.
540 174, 7446–7452 (2005).
541 51. Hagai, T. et al. Gene expression variability across cells and species shapes innate immunity.
542 Nature 563, 197–202 (2018).
543 52. Li, S. et al. SARS-CoV-2 triggers inflammatory responses and cell death through caspase-8
544 activation. Signal Transduct Target Ther 5, 235 (2020).
545
546
547 Figure Legends
548 Fig. 1: Experimental outline and overview of results. (a) Visual overview of the experimental
549 design, numbers of patients, samples taken and single cells sequenced. (b) UMAP visualisation
550 of annotated airway epithelial cells, (c) and immune cells, with cell numbers per cell type in
551 parentheses. Full list of abbreviations in Supplementary Information. (d) Airway epithelial
552 cells in the same UMAP as (a) with RNA velocity of major epithelial cell types. (e) Barplot
553 showing fraction of SARS-CoV-2 viral UMI (where >=10 were detected per donor) relative to
554 total UMI per donor, prior to filtering out of ambient RNA, in descending order coloured by
555 infection collection interval (days). This was calculated as the days between sample collection
19

556 and estimated onset of infection, based upon the first symptom onset or a positive SARS-CoV-2
557 RT-qPCR test, whichever was reported first for symptomatic patients, and the latter for
558 asymptomatic patients (f)(cid:849)(cid:887)(cid:931)(cid:914)(cid:916)(cid:933)(cid:922)(cid:928)(cid:927)(cid:849)(cid:928)(cid:919)(cid:849)(cid:914)(cid:922)(cid:931)(cid:936)(cid:914)(cid:938)(cid:849)(cid:916)(cid:918)(cid:925)(cid:925)(cid:932)(cid:849)(cid:936)(cid:922)(cid:933)(cid:921)(cid:849)(cid:917)(cid:918)(cid:933)(cid:918)(cid:916)(cid:933)(cid:918)(cid:917)(cid:849)(cid:900)(cid:882)(cid:899)(cid:900)(cid:862)(cid:884)(cid:928)(cid:903)(cid:867)(cid:849)
559 (cid:926)(cid:899)(cid:895)(cid:882)(cid:849)(cid:922)(cid:927)(cid:849)(cid:918)(cid:914)(cid:916)(cid:921)(cid:849)(cid:916)(cid:918)(cid:925)(cid:925)(cid:849)(cid:933)(cid:938)(cid:929)(cid:918)(cid:849)(cid:857)(cid:936)(cid:922)(cid:933)(cid:921)(cid:849)(cid:922)(cid:926)(cid:926)(cid:934)(cid:927)(cid:918)(cid:849)(cid:916)(cid:918)(cid:925)(cid:925)(cid:932)(cid:849)(cid:922)(cid:927)(cid:849)(cid:915)(cid:931)(cid:928)(cid:914)(cid:917)(cid:849)(cid:916)(cid:914)(cid:933)(cid:918)(cid:920)(cid:928)(cid:931)(cid:922)(cid:918)(cid:932)(cid:858)(cid:849)(cid:922)(cid:927)(cid:849)
560 (cid:884)(cid:896)(cid:903)(cid:890)(cid:885)(cid:862)(cid:866)(cid:874)(cid:849)(cid:929)(cid:914)(cid:933)(cid:922)(cid:918)(cid:927)(cid:933)(cid:932)(cid:849)(cid:936)(cid:922)(cid:933)(cid:921)(cid:849)(cid:917)(cid:918)(cid:933)(cid:918)(cid:916)(cid:933)(cid:918)(cid:917)(cid:849)(cid:935)(cid:922)(cid:931)(cid:914)(cid:925)(cid:849)(cid:899)(cid:895)(cid:882)(cid:849)(cid:857)(cid:1541)(cid:849)(cid:870)(cid:849)(cid:935)(cid:922)(cid:931)(cid:914)(cid:925)(cid:849)(cid:902)(cid:894)(cid:890)(cid:849)(cid:929)(cid:918)(cid:931)(cid:849)(cid:917)(cid:928)(cid:927)(cid:928)(cid:931)(cid:849)
561 (cid:919)(cid:928)(cid:925)(cid:925)(cid:928)(cid:936)(cid:922)(cid:927)(cid:920)(cid:849)(cid:919)(cid:922)(cid:925)(cid:933)(cid:918)(cid:931)(cid:922)(cid:927)(cid:920)(cid:849)(cid:928)(cid:934)(cid:933)(cid:849)(cid:914)(cid:926)(cid:915)(cid:922)(cid:918)(cid:927)(cid:933)(cid:849)(cid:899)(cid:895)(cid:882)(cid:858)(cid:849)(cid:857)(cid:927)(cid:878)(cid:874)(cid:858)(cid:863)
562
563 Fig. 2: Differences in airway epithelial and immune cells between paediatric and adult
564 COVID-19 (a) Dot plot showing fold change and statistical significance of major airway cell
565 type proportions across location of sampling, age group and COVID-19 status, respectively,
566 estimated by fitting Poisson generalised linear mixed models taking into account other technical
567 and biological variables (see Methods). Red circles indicate LTSR> 0.95. (b) Comparing
568 expression signature of cellular response to IFN-α, IFN-γ, TNF-α signalling and neutrophil
569 migration signalling across COVID-19 status and age groups. (c) Heatmaps comparing these
570 expression signatures in healthy paediatric versus adult individuals, and in COVID-19 paediatric
571 versus adult patients in epithelial cells, colours indicate subtraction of scoring, (d) and in
572 immune cells. (e) Comparing expression signatures across COVID-19 severity and age groups.
573 (f) Representative 5 enriched GO terms in genes up-regulated in COVID-19 samples in transit
574 epithelial 1 cells, goblet 2 inflammatory cells, and IL-6+ monocytes. (g) IHC confocal
575 microscopy image illustrating expression of S100A9 (green) by epithelial cells (EPCAM,
576 magenta) in the nasal epithelium. Nuclei stained with DAPI (blue). Scale bar, 20μm. 1
577 representative section out of 4 replicates is shown. Two-sided Wilcoxon rank-sum tests were
578 used for pairwise comparisons in b and e where stars indicate statistical significance (ns: p>0.05,
579 ****: p<2.2e-16).
580
581 Fig. 3: Differences in immune response between paediatric and adult COVID-19 patients.
582 (a) UMAP of 422,220 PBMCs incorporating both protein and RNA expression data. (b) Fold
583 changes of immune cell type proportions across age group and disease status, taking into account
584 confounders (see Methods). Only cell types that change with a local true sign rate of >0.90 in the
585 disease status groups are shown (all cell types shown in Extended Data Fig. 6d-e). Analysis
586 does not include cells analysed in f. (c) Fraction of unique TCR sequences over age. (d) Cell
20

587 type marker expression alongside IFN-stimulated genes. The colour is scaled to all other cell
588 types (see Extended Data Fig. 6a). (e) Boxplot showing the percentage of PBMCs that are IFN-
589 stimulated of each symptomatic COVID-19 patient, grouped by the weeks since the onset of
590 symptoms. (f) Dot plot as in b, showing the IFN-stimulated subpopulations (IFN-stim) across
591 age and disease status. (g) Correlation analysis comparing the blood and nose, using a Spearman
592 rank-order correlation coefficient between relative proportion of PBMC subtypes (y-axis) and
593 nasal cell types (x-axis) (also see Extended Data Fig. 7d-e.) (h) IFN-stimulation in PBMCs and
594 nasal cells, and nasal IFN production in individuals with matched nasal and PBMC data (detailed
595 gene expression dynamics in Extended Data Fig. 8). Dots in c and e represent independent
596 patient samples. Box plots were drawn with the centre line as the median, the hinges as the first
597 and third quartiles, and with the whiskers extending to the lowest and highest values that were
598 within 1.5 × interquartile range. All cell type abbreviations are in Supplemental Information.
599
600 Fig. 4: The local and systemic response to SARS-CoV-2 infection in children and adults.
601 Schematic summary of the difference of the airway and systemic immune response to SARS-
602 CoV-2 infection between children and adults, reflecting the maturation of the immune landscape
603 throughout childhood to adulthood. Key points are: (1) Immune cell proportions display strong
604 maturation patterns throughout healthy child- and adulthood, with a notable innate to adaptive
605 immunity switch. (2) In airways, the local innate IFN response to SARS-CoV-2 is stronger in
606 paediatric airway immune cells compared to adult ones. (3) In blood, the systemic innate IFN
607 response to SARS-CoV-2 is stronger in adults, with a notable increase in IFN-stimulated
608 subpopulations, whereas the adaptive immune response is characterised by expanded cytotoxic
609 populations in adults compared to naïve populations in children. (4) Novel epithelial cells with
610 an inflammatory gene expression (S100A8/A9) are found enriched in COVID-19 patients. (5)
611 Clonotype diversity decreases with age. Created with BioRender.com.
612
613
614
615 Methods
616
617 Study Participants and Design
21

618 The UK cohort: Subjects were included from five large hospital sites in London, United
619 Kingdom, namely Great Ormond Street Hospital NHS Foundation Trust, University College
620 London Hospitals NHS Foundation Trust, Royal Free London NHS Foundation Trust (Royal
621 Free Hospital and Barnet Hospital) and Whittington Health NHS Trust from March 2020-Feb
622 2021. Ethical approval was given through the Living Airway Biobank, administered through
623 UCL Great Ormond Street Institute of Child Health (REC reference: 19/NW/0171, IRAS project
624 ID 261511, North West - Liverpool East Research Ethics Committee), REC reference
625 18/SC/0514 (IRAS project 245471, South Central - Hampshire B Research Ethics Committee)
626 administered through University College London Hospitals NHS Foundation Trust and REC
627 reference 18/EE/0150 (IRAS project ID 236570, East of England - Cambridge Central Research
628 Ethics Committee) administered through Great Ormond Street Hospital NHS Foundation Trust,
629 REC reference 08/H0308/267 administered through Cambridge University Hospitals NHS
630 Foundation Trust, as well as by the local R&D departments at all hospitals. All study participants
631 or their surrogates provided informed consent. At daily virtual COVID-19 co-ordination
632 meetings suitable patients were chosen from a list of newly diagnosed patients admitted within
633 the preceding 24 hours. Only COVID-19 patients who tested positive for SARS-CoV-2 by a RT-
634 qPCR nasopharyngeal test were enrolled in the study, with symptom onset relative to RT-qPCR
635 testing and sampling summarised in Extended Data Fig. 1b. Patients with typical clinical and
636 radiological COVID-19 features but with a negative screening test for SARS-CoV-2 were
637 excluded. Other excluding criteria included active haematological malignancy or cancer, known
638 immunodeficiencies, sepsis from any cause and blood transfusion within 4 weeks. Two cases of
639 paediatric multisystem inflammatory syndrome (PIMS-TS, named by the Royal College of
640 Paediatrics and Child Health) were included (airway samples only), which is also referred to as
641 multisystem inflammatory syndrome in children (MIS-C) by the World Health Organisation,
642 with little to no MIS-C specific difference detected upon analysis in the nasal mucosa when
643 compared to equivalent samples from paediatric patients with COVID-1953. Maximal severity of
644 COVID-19 was determined retrospectively by determining the presence of symptoms, the need
645 for oxygen supplementation and the level of respiratory support (mild - symptomatic without
646 oxygen requirement or respiratory support, moderate - requiring oxygen without respiratory
647 support, severe - requiring non-invasive or invasive ventilation). Brushings and peripheral blood
648 sampling were performed by trained clinicians prior to inclusion in any pharmacological
22

649 interventional trials, with the exception of 3 paediatric COVID-19 patients (noted in Extended
650 Data Table 1) and ideally within 48 hours of a positive SARS-CoV-2 test. All participants for
651 our paediatric healthy cohort were recruited from Great Ormond Street Hospital NHS
652 Foundation Trust and were eligible for inclusion if they were <18 years old and asymptomatic
653 for respiratory viral infections at time of sampling. At the start of the study, initiated in March
654 2020 it was not standard practice for hospitals to test healthy asymptomatic patients. Therefore 8
655 (out of 30) of the earliest recruited subjects were un-tested and assumed negative. In order to
656 confirm this assumption and to look for any other undetected asymptomatic infections
657 metagenomic analysis on the entire dataset was performed (see Methods below and Extended
658 Data Fig. 9). Participants for our adult healthy cohort were recruited from University College
659 London Hospitals and associated research laboratories at University College London and were
660 eligible for inclusion if > 18 years and asymptomatic with a current negative SARS-CoV-2 test
661 (RT-qPCR or rapid-antigen testing). Exclusion criteria for the cohort included active
662 haematological malignancies or cancer, known immunodeficiencies, sepsis from any cause and
663 blood transfusions within 4 weeks, known bronchial asthma, hayfever, diabetes and other known
664 chronic respiratory diseases such as cystic fibrosis, interstitial lung disease and chronic
665 obstructive pulmonary disease. There were three exceptions to these criteria in our paediatric
666 cohort; NP28 who was later discovered to have asthma and NP10 who was reported to have a
667 immunocompromised status in underlying comorbidities, but for whom only nasal brushes were
668 included, and NP27 who did not have any respiratory problem but was subsequently diagnosed
669 with endocarditis. Exclusion of these individuals did not alter any of our conclusions. For some
670 patients included in our COVID-19 cohort matched convalescent blood was taken on the day of
671 hospital discharge and analysed separately in our post-COVID-19 cohort alongside symptomatic
672 patients recruited from University College London Hospitals outpatient COVID-19 follow-up
673 clinic, who were recalled ~3 months after recovering from severe COVID-19 using the exclusion
674 criteria as stated for our COVID-19 cohort. Participants were further divided into subgroups in
675 order to be able to look at age-specific effects. These were classified based on World Health
676 Organisation; neonates (0-30 days), infants (1-24 months), young children (2-6 years), children
677 (6-12 years), adolescents (12-18 years) and adults (18+ years), which were further broken down
678 into adults (18-65 years) and elderly (65+ years).
679
23

680 Chicago Cohort (adult bronchial samples): Ethical approval for sample collection from
681 patients with severe pneumonia was given by Northwestern Institutional Review Board, study
682 STU00204868 (PI Richard Wunderink). Samples from patients with COVID-19, viral
683 pneumonia and other pneumonia, and non-pneumonia controls were collected from participants
684 enrolled in the Successful Clinical Response in Pneumonia Therapy (SCRIPT) study
685 STU00204868 and admitted to the ICU at Northwestern Memorial Hospital, Chicago. All study
686 participants or their surrogates provided informed consent. Individuals of at least 18 years of age
687 with suspicion of pneumonia based on clinical criteria (including but not limited to fever,
688 radiographic infiltrate and respiratory secretions) were screened for enrolment into the SCRIPT
689 study. Inability to safely perform bronchoalveolar lavage or non-bronchoscopic bronchoalveolar
690 lavage were considered exclusion criteria. In our center, patients with respiratory failure are
691 intubated on the basis of the judgement of bedside clinicians for worsening hypoxaemia,
692 hypercapnia or work of breathing refractory to high-flow oxygen or non-invasive ventilation
693 modes. Bronchial brushings were performed during diagnostic bronchoalveolar lavage procedure
694 and samples were collected from representative sites at the lobar bronchi.
695
696 Sample Collection
697 The UK Cohort: Samples were collected and transferred to a Category Level 3 facility at
698 University College London and processed within 2 hours of sample collection. Nasal, tracheal
699 and bronchial brushings were enzymatically digested to a single cell suspension and processed
700 further immediately. Peripheral blood was centrifuged after adding Ficoll Paque Plus and
701 PBMCs, serum and neutrophils separated, collected and frozen for later processing. A local
702 anaesthetic endoscopically guided biopsy of the postnasal space mucosa was collected from a 19
703 year old female subject three weeks after onset of mild COVID-19 symptoms (REC:
704 08/H0308/267). SARS-CoV-2 virus was confirmed by RT-PCR testing at the time of symptom
705 onset.
706 Chicago Cohort (adult bronchial samples): Samples were collected in the ICU at
707 Northwestern Memorial Hospital, transferred to a research laboratory in the Simpson Querrey
708 Biomedical Research Center, Feinberg School of Medicine, Northwestern University, and
709 processed within 1 hour of sample collection in biological safety level 2 facility using biological
24

710 safety level 3 practices. Upon collection bronchial brushings were stored in Hypothermosol
711 (Stem Cell Technologies, 07935) at 4 °C.
712
713 Nasal and tracheal brushing tissue dissociation
714 The UK Cohort: Nasal brushing was performed on the inferior nasal concha zone with a
715 cytological brush (Scientific Laboratory Supplies, CYT1050). All samples were processed fresh
716 based on protocol from Deprez, Zaragosi et al26 with minor modifications
717 (dx.doi.org/10.17504/protocols.io.btpunmnw)54. The brushes were immediately placed in a 15
718 mL sterile Falcon tube containing 4mL of transport media on ice. Transport media; αMEM
719 supplemented with 1X penicillin/streptomycin (Gibco; 15070), 10 ng/mL Gentamicin (Gibco;
720 15710) and 250 ng/ml amphotericin B (Fisher Scientific; 10746254). Once in the Category Level
721 3 facility, the tube was shaken vigorously to collect cells in suspension. The brushes were then
722 carefully transferred into a new Falcon tube containing HBSS and shaken to remove residual
723 cells from the brush. This was repeated until all cells looked like they had been collected from
724 the brush. All Falcon tubes were centrifuged at 400 g for 5 min at 4 °C. The cell pellet was
725 collected from each tube and then put in a dissociation buffer consisting of 10 mg/mL protease
726 from Bacillus Licheniformis (Sigma-Aldrich, P5380) and 0.5 mM EDTA in HypoThermosol
727 (Stem Cell Technologies, 07935) for dissociation on ice for 30 min. Every 5 min, cells were
728 gently triturated using a 21 G and 23 G needle. After incubation, protease was inactivated by
729 adding 200 μL of inactivation buffer (HBSS containing 2% BSA). The suspension was
730 centrifuged at 400 g for 5 min at 4 °C and the supernatant was discarded. Cells were
731 resuspended in 1 mL wash buffer (HBSS containing 1% BSA) and centrifuged again. Red blood
732 cell lysis was performed if needed, followed by an additional wash. The single-cell suspension
733 was forced through a 40 μm Flowmi Cell Strainer. Finally, cells were centrifuged and
734 resuspended in 30 μL of resuspension buffer (HBSS containing 0.05% BSA). Using Trypan
735 Blue, total cell counts and viability were assessed. The cell concentration was adjusted for 5000
736 targeted cell recovery according to the 10X Chromium manual before loading on 10X chip
737 (between 700-1000 cells/ μL) and processing immediately for 10X 5’ single cell capture using
738 either the Chromium Single Cell V(D)J Reagent Kits V1.0 (Rev J Guide) or the newer chromium
739 Next GEM Single Cell V(D)J Reagent Kit v1.1 (Rev E Guide) or chromium Next GEM Single
740 Cell 5’ V2 (Dual index) kit (Rev A guide).
25

741
742 For a small subset of nasal samples (PP5_NB_2, PP6_NB_2, AP11_NB, AP12_NB, AP13_NB
743 and AP14_NB_2) 1uL Viral RT oligo (at 5μM, PAGE) was spiked into the master mix (at step
744 1.2.b in the 10X guide; giving a final volume of 75 μL) to aid with the detection of SARS-CoV-2
745 viral reads. The samples were then processed as per manufacturer's instructions, with the viral
746 cDNA separated from the GEX by size selection during step 3.2. Here the supernatant was
747 collected (159 μL) and transferred to a new PCR tube and incubated with 70 μL of SPRI beads
748 (0.6x selection) at RT for 5 mins. The SPRI beads were then washed as per guide and the viral
749 cDNA eluted using 30 μL of EB buffer. No changes to the transcriptome were observed between
750 samples which were run both with and without the viral oligo and only a small increase in the
751 overall number of SARS-CoV-2 reads detected.
752
753 RT oligo sequence: 5’- AAGCAGTGGTATCAACGCAGAGTACTTACTCGTGTCCTGTCAACG - 3’
754
755 Chicago Cohort (adult bronchial samples): Samples were processed using the protocol from
756 Deprez, Zaragosi et al26 with minimal modifications. Specifically, dissociation was performed
757 without EDTA and trituration was performed by pipetting using a regular b ore 1000 μL tip
758 every 5 minutes. Dissociation was visually confirmed by inspecting an aliquot of the single cell
759 suspension using phase contrast on an inverted microscope. Cell count was performed using
760 AO/PI reagent on K2 Cellometer (Nexcelom). Approximately 300,000-500,000 cells were
761 obtained per brush with viability of 97% and above. Cells were captured on a 10X Chromium
762 Single Cell Controller using Chromium Single Cell V(D)J Reagent Kits V1.0 (Rev J Guide).
763
764 PBMC isolation from peripheral blood
765 Peripheral blood was collected in EDTA immediately after the nasal brushing procedure. The
766 blood was diluted with 5 mL of PBS containing 2 mM EDTA (Invitrogen, 1555785-038). 10 to
767 20 mL of diluted blood was carefully layered onto 15 mL of Ficoll-Paque Plus (GE healthcare,
768 17144002). If the sample volume was less than 5 mL, blood was diluted with an equal volume of
769 PBS-EDTA and layered onto 3 mL Ficoll. The sample was centrifuged at 800 g for 20 min at
770 room temperature. The plasma layer was carefully removed and the peripheral blood
771 mononuclear cell (PBMC) layer was collected using a sterile Pasteur pipette. The PBMC layer
26

772 was washed with 3 volumes of PBS containing EDTA by centrifugation at 500 g for 10 min. The
773 pellet was suspended in PBS-EDTA and centrifuged again at 300 g for 5 min. The PBMC pellet
774 was collected followed by both cell number and viability being assessed using Trypan Blue. Cell
775 freezing medium (90% FBS, 10% DMSO) was added dropwise to PBMCs slowly on ice and
776 then the mixture was cryopreserved at -80 °C until further full sample processing.
777
778 CITE-Seq staining for single-cell proteogenomics
779 Frozen PBMC samples were thawed quickly at 37 °C in a water bath. 20-30 mL of warm
780 RPMI1640 medium containing 10% FBS was added slowly to the cells before centrifuging at
781 300 g for 5 min. This was followed by a wash in 5 mL RPMI1640-FBS. The PBMC pellet was
782 collected, and cell number and viability were determined using Trypan Blue. PBMCs from four
783 different donors were then pooled together at equal numbers - 1.25x105 PBMCs from each donor
784 were combined with the other PBMCs to make up 5.0x105 cells in total. The remaining cells
785 were used for DNA extraction (Qiagen, 69504). The pooled PBMCs were resuspended in 25 μL
786 of cell staining buffer (Biolegend, 420201) and blocked via a 10 minute incubation on ice with
787 2.5 μL Human TruStain FcX block (Biolegend, 422301). The PBMCs pool was then stained with
788 TotalSeq-C antibodies (Biolegend, cat. No. 99814) according to manufacturer’s instructions. For
789 full list of TotalSeq-C antibodies refer to Stephenson et al 202123. After incubating with 0.5 vial
790 of TotalSeq-C for 30 min at 4 °C, PBMCs were washed three times by centrifugation at 500 g for
791 5 min at 4 °C. PBMCs were counted again and processed immediately for 10X 5’ single cell
792 capture (Chromium Next GEM Single Cell V(D)J Reagent Kit v1.1 with Feature Barcoding
793 technology for cell Surface Protein-Rev D protocol). Two lanes of 25,000 cells were loaded per
794 pool on a 10X chip.
795
796 Library Generation and Sequencing
797 Either Chromium Single Cell 5’ V(D)J Reagent Kit (V1.0 chemistry), Chromium Next GEM
798 Single Cell 5’ V(D)J Reagent Kit (V1.1 chemistry) or Chromium Next GEM Single Cell 5’ v2
799 kit (V2.0 chemistry) was used for scRNAseq library construction for all airway samples, with
800 Chromium Next GEM Single Cell V(D)J Reagent Kit v1.1 with Feature Barcoding technology
801 for cell surface proteins used for PBMCs. Gene expression libraries (GEX) and V(D)J libraries
802 were prepared according to the manufacturer’s protocol (10X Genomics) using individual
27

803 Chromium i7 Sample Indices. The cell surface protein libraries were created according to the
804 manufacturer’s protocol with slight modification that included doubling the SI primer amount
805 per reaction and reducing the number of amplification cycles to 7 during the index PCR to avoid
806 the daisy chains effect. GEX, V(D)J and cell surface protein indexed libraries were pooled in
807 1:0.1:0.4 ratio respectively and sequenced on a NovaSeq 6000 S4 Flowcell (paired-end (PE),
808 150-bp reads) aiming for a minimum of 50,000 PE reads per cell for GEX libraries and 5,000 PE
809 reads per cell for V(D)J and cell surface protein libraries.
810
811 Single Cell RNA-seq Computational Pipelines, Processing and Analysis
812 (cid:901)(cid:921)(cid:918)(cid:849) (cid:932)(cid:922)(cid:927)(cid:920)(cid:925)(cid:918)(cid:849) (cid:916)(cid:918)(cid:925)(cid:925)(cid:849) (cid:917)(cid:914)(cid:933)(cid:914)(cid:849) (cid:936)(cid:914)(cid:932)(cid:849) (cid:926)(cid:914)(cid:929)(cid:929)(cid:918)(cid:917)(cid:849) (cid:933)(cid:928)(cid:849) (cid:914)(cid:849) (cid:888)(cid:899)(cid:884)(cid:921)(cid:868)(cid:873)(cid:849) (cid:886)(cid:895)(cid:900)(cid:886)(cid:894)(cid:883)(cid:893)(cid:849) (cid:874)(cid:868)(cid:849) (cid:917)(cid:918)(cid:931)(cid:922)(cid:935)(cid:918)(cid:917)(cid:849)
813 (cid:931)(cid:918)(cid:919)(cid:918)(cid:931)(cid:918)(cid:927)(cid:916)(cid:918)(cid:861)(cid:849)(cid:916)(cid:928)(cid:927)(cid:916)(cid:914)(cid:933)(cid:918)(cid:927)(cid:914)(cid:933)(cid:918)(cid:917)(cid:849)(cid:936)(cid:922)(cid:933)(cid:921)(cid:849)(cid:867)(cid:866)(cid:849)(cid:935)(cid:922)(cid:931)(cid:914)(cid:925)(cid:849)(cid:920)(cid:918)(cid:927)(cid:928)(cid:926)(cid:918)(cid:932)(cid:849)(cid:857)(cid:919)(cid:918)(cid:914)(cid:933)(cid:934)(cid:931)(cid:922)(cid:927)(cid:920)(cid:849)(cid:900)(cid:882)(cid:899)(cid:900)(cid:862)(cid:884)(cid:928)(cid:903)(cid:862)
814 (cid:867)(cid:858)(cid:861)(cid:849) (cid:936)(cid:921)(cid:928)(cid:932)(cid:918)(cid:849) (cid:895)(cid:884)(cid:883)(cid:890)(cid:849) (cid:899)(cid:918)(cid:919)(cid:918)(cid:931)(cid:918)(cid:927)(cid:916)(cid:918)(cid:849) (cid:900)(cid:918)(cid:930)(cid:934)(cid:918)(cid:927)(cid:916)(cid:918)(cid:849) (cid:890)(cid:885)(cid:932)(cid:849) (cid:914)(cid:931)(cid:918)(cid:875)(cid:849) (cid:895)(cid:884)(cid:912)(cid:865)(cid:865)(cid:872)(cid:871)(cid:865)(cid:870)(cid:863)(cid:866)(cid:849) (cid:857)(cid:886)(cid:883)(cid:903)(cid:866)(cid:858)(cid:861)(cid:849)
815 (cid:895)(cid:884)(cid:912)(cid:865)(cid:865)(cid:874)(cid:868)(cid:868)(cid:869)(cid:863)(cid:866)(cid:849) (cid:857)(cid:886)(cid:883)(cid:903)(cid:867)(cid:858)(cid:861)(cid:849) (cid:882)(cid:887)(cid:866)(cid:870)(cid:871)(cid:874)(cid:871)(cid:868)(cid:849) (cid:857)(cid:886)(cid:899)(cid:903)(cid:904)(cid:886)(cid:866)(cid:858)(cid:861)(cid:849) (cid:882)(cid:906)(cid:866)(cid:865)(cid:866)(cid:870)(cid:873)(cid:867)(cid:849) (cid:857)(cid:886)(cid:899)(cid:903)(cid:904)(cid:886)(cid:866)(cid:858)(cid:861)(cid:849) (cid:882)(cid:906)(cid:866)(cid:865)(cid:866)(cid:870)(cid:873)(cid:868)(cid:849)
816 (cid:857)(cid:886)(cid:899)(cid:903)(cid:904)(cid:886)(cid:866)(cid:858)(cid:861)(cid:849)(cid:882)(cid:906)(cid:866)(cid:865)(cid:866)(cid:870)(cid:873)(cid:869)(cid:849)(cid:857)(cid:886)(cid:899)(cid:903)(cid:904)(cid:886)(cid:866)(cid:858)(cid:861)(cid:849)(cid:882)(cid:906)(cid:866)(cid:865)(cid:866)(cid:870)(cid:873)(cid:870)(cid:849)(cid:857)(cid:886)(cid:899)(cid:903)(cid:904)(cid:886)(cid:866)(cid:858)(cid:861)(cid:849)(cid:882)(cid:887)(cid:865)(cid:872)(cid:867)(cid:869)(cid:874)(cid:873)(cid:849)(cid:857)(cid:889)(cid:886)(cid:899)(cid:903)(cid:862)(cid:904)(cid:858)(cid:861)(cid:849)
817 (cid:882)(cid:887)(cid:866)(cid:867)(cid:872)(cid:867)(cid:867)(cid:873)(cid:849) (cid:857)(cid:889)(cid:886)(cid:899)(cid:903)(cid:862)(cid:904)(cid:858)(cid:861)(cid:849) (cid:882)(cid:887)(cid:866)(cid:867)(cid:872)(cid:867)(cid:867)(cid:874)(cid:849) (cid:857)(cid:889)(cid:886)(cid:899)(cid:903)(cid:862)(cid:904)(cid:858)(cid:861)(cid:849) (cid:882)(cid:887)(cid:868)(cid:868)(cid:866)(cid:870)(cid:865)(cid:865)(cid:849) (cid:857)(cid:889)(cid:886)(cid:899)(cid:903)(cid:862)(cid:904)(cid:858)(cid:861)(cid:849)
818 (cid:895)(cid:884)(cid:912)(cid:865)(cid:865)(cid:866)(cid:871)(cid:871)(cid:869)(cid:863)(cid:869)(cid:849) (cid:857)(cid:889)(cid:889)(cid:903)(cid:862)(cid:871)(cid:882)(cid:858)(cid:861)(cid:849) (cid:895)(cid:884)(cid:912)(cid:865)(cid:865)(cid:865)(cid:873)(cid:874)(cid:873)(cid:863)(cid:866)(cid:849) (cid:857)(cid:889)(cid:889)(cid:903)(cid:862)(cid:871)(cid:883)(cid:858)(cid:861)(cid:849) (cid:895)(cid:884)(cid:912)(cid:865)(cid:865)(cid:866)(cid:873)(cid:865)(cid:871)(cid:863)(cid:867)(cid:849) (cid:857)(cid:889)(cid:918)(cid:931)(cid:929)(cid:918)(cid:932)(cid:849)
819 (cid:900)(cid:922)(cid:926)(cid:929)(cid:925)(cid:918)(cid:937)(cid:849) (cid:903)(cid:922)(cid:931)(cid:934)(cid:932)(cid:849) (cid:866)(cid:858)(cid:861)(cid:849) (cid:895)(cid:884)(cid:912)(cid:865)(cid:865)(cid:866)(cid:872)(cid:874)(cid:873)(cid:863)(cid:867)(cid:849) (cid:857)(cid:889)(cid:918)(cid:931)(cid:929)(cid:918)(cid:932)(cid:849) (cid:900)(cid:922)(cid:926)(cid:929)(cid:925)(cid:918)(cid:937)(cid:849) (cid:903)(cid:922)(cid:931)(cid:934)(cid:932)(cid:849) (cid:867)(cid:858)(cid:861)(cid:849) (cid:895)(cid:884)(cid:912)(cid:865)(cid:865)(cid:866)(cid:869)(cid:874)(cid:873)(cid:863)(cid:866)(cid:849)
820 (cid:857)(cid:894)(cid:918)(cid:914)(cid:932)(cid:925)(cid:918)(cid:932)(cid:849)(cid:926)(cid:928)(cid:931)(cid:915)(cid:922)(cid:925)(cid:925)(cid:922)(cid:935)(cid:922)(cid:931)(cid:934)(cid:932)(cid:858)(cid:861)(cid:849)(cid:895)(cid:884)(cid:912)(cid:865)(cid:865)(cid:867)(cid:867)(cid:865)(cid:865)(cid:863)(cid:866)(cid:849)(cid:857)(cid:894)(cid:934)(cid:926)(cid:929)(cid:932)(cid:849)(cid:931)(cid:934)(cid:915)(cid:934)(cid:925)(cid:914)(cid:935)(cid:922)(cid:931)(cid:934)(cid:932)(cid:858)(cid:861)(cid:849)(cid:895)(cid:884)(cid:912)(cid:865)(cid:865)(cid:866)(cid:870)(cid:869)(cid:870)(cid:863)(cid:867)(cid:849)
821 (cid:857)(cid:899)(cid:934)(cid:915)(cid:918)(cid:925)(cid:925)(cid:914)(cid:858)(cid:861)(cid:849) (cid:895)(cid:884)(cid:912)(cid:865)(cid:865)(cid:866)(cid:868)(cid:869)(cid:873)(cid:863)(cid:866)(cid:849) (cid:857)(cid:903)(cid:914)(cid:931)(cid:922)(cid:916)(cid:918)(cid:925)(cid:925)(cid:914)(cid:849) (cid:907)(cid:928)(cid:932)(cid:933)(cid:918)(cid:931)(cid:849) (cid:903)(cid:922)(cid:931)(cid:934)(cid:932)(cid:858)(cid:861)(cid:849) (cid:895)(cid:884)(cid:912)(cid:865)(cid:865)(cid:871)(cid:867)(cid:872)(cid:868)(cid:863)(cid:867)(cid:849)
822 (cid:857)(cid:884)(cid:938)(cid:933)(cid:928)(cid:926)(cid:918)(cid:920)(cid:914)(cid:925)(cid:928)(cid:935)(cid:922)(cid:918)(cid:934)(cid:932)(cid:858)(cid:861)(cid:849) (cid:895)(cid:884)(cid:912)(cid:865)(cid:869)(cid:870)(cid:870)(cid:866)(cid:867)(cid:863)(cid:867)(cid:849) (cid:857)(cid:900)(cid:882)(cid:899)(cid:900)(cid:862)(cid:884)(cid:928)(cid:903)(cid:862)(cid:867)(cid:858)(cid:863)(cid:849) (cid:904)(cid:921)(cid:918)(cid:927)(cid:849) (cid:918)(cid:937)(cid:914)(cid:926)(cid:922)(cid:927)(cid:922)(cid:927)(cid:920)(cid:849) (cid:935)(cid:922)(cid:931)(cid:914)(cid:925)(cid:849)
823 (cid:925)(cid:928)(cid:914)(cid:917)(cid:849)(cid:929)(cid:918)(cid:931)(cid:849)(cid:916)(cid:918)(cid:925)(cid:925)(cid:849)(cid:933)(cid:938)(cid:929)(cid:918)(cid:861)(cid:849)(cid:936)(cid:918)(cid:849)(cid:919)(cid:922)(cid:931)(cid:932)(cid:933)(cid:849)(cid:931)(cid:918)(cid:926)(cid:928)(cid:935)(cid:918)(cid:917)(cid:849)(cid:914)(cid:926)(cid:915)(cid:922)(cid:918)(cid:927)(cid:933)(cid:849)(cid:899)(cid:895)(cid:882)(cid:849)(cid:915)(cid:938)(cid:849)(cid:900)(cid:928)(cid:934)(cid:929)(cid:905)(cid:849)(cid:914)(cid:927)(cid:917)(cid:849)(cid:928)(cid:927)(cid:925)(cid:938)(cid:849)
824 (cid:922)(cid:927)(cid:916)(cid:925)(cid:934)(cid:917)(cid:918)(cid:917)(cid:849) (cid:900)(cid:882)(cid:899)(cid:900)(cid:862)(cid:884)(cid:928)(cid:903)(cid:862)(cid:867)(cid:860)(cid:849) (cid:917)(cid:928)(cid:927)(cid:928)(cid:931)(cid:932)(cid:849) (cid:936)(cid:921)(cid:918)(cid:931)(cid:918)(cid:849) (cid:1541)(cid:870)(cid:849) (cid:935)(cid:922)(cid:931)(cid:914)(cid:925)(cid:849) (cid:931)(cid:918)(cid:914)(cid:917)(cid:932)(cid:849) (cid:936)(cid:918)(cid:931)(cid:918)(cid:849) (cid:932)(cid:933)(cid:922)(cid:925)(cid:925)(cid:849)
825 (cid:917)(cid:918)(cid:933)(cid:918)(cid:916)(cid:933)(cid:918)(cid:917)(cid:863)(cid:849) (cid:882)(cid:927)(cid:933)(cid:922)(cid:915)(cid:928)(cid:917)(cid:938)(cid:862)(cid:917)(cid:918)(cid:931)(cid:922)(cid:935)(cid:918)(cid:917)(cid:849) (cid:933)(cid:914)(cid:920)(cid:849) (cid:916)(cid:928)(cid:934)(cid:927)(cid:933)(cid:932)(cid:849) (cid:857)(cid:882)(cid:885)(cid:901)(cid:858)(cid:849) (cid:914)(cid:927)(cid:917)(cid:849) (cid:920)(cid:918)(cid:927)(cid:918)(cid:849) (cid:918)(cid:937)(cid:929)(cid:931)(cid:918)(cid:932)(cid:932)(cid:922)(cid:928)(cid:927)(cid:849)
826 (cid:916)(cid:928)(cid:934)(cid:927)(cid:933)(cid:932)(cid:849) (cid:922)(cid:927)(cid:849) (cid:884)(cid:890)(cid:901)(cid:886)(cid:862)(cid:932)(cid:918)(cid:930)(cid:849) (cid:917)(cid:914)(cid:933)(cid:914)(cid:849) (cid:936)(cid:918)(cid:931)(cid:918)(cid:849) (cid:923)(cid:928)(cid:922)(cid:927)(cid:933)(cid:925)(cid:938)(cid:849) (cid:930)(cid:934)(cid:914)(cid:927)(cid:933)(cid:922)(cid:919)(cid:922)(cid:918)(cid:917)(cid:849) (cid:934)(cid:932)(cid:922)(cid:927)(cid:920)(cid:849) (cid:884)(cid:918)(cid:925)(cid:925)(cid:931)(cid:914)(cid:927)(cid:920)(cid:918)(cid:931)(cid:849)
827 (cid:868)(cid:863)(cid:865)(cid:863)(cid:867)(cid:863)(cid:849)(cid:901)(cid:921)(cid:918)(cid:849)(cid:914)(cid:925)(cid:922)(cid:920)(cid:927)(cid:926)(cid:918)(cid:927)(cid:933)(cid:861)(cid:849)(cid:930)(cid:934)(cid:914)(cid:927)(cid:933)(cid:922)(cid:919)(cid:922)(cid:916)(cid:914)(cid:933)(cid:922)(cid:928)(cid:927)(cid:849)(cid:914)(cid:927)(cid:917)(cid:849)(cid:929)(cid:931)(cid:918)(cid:925)(cid:922)(cid:926)(cid:922)(cid:927)(cid:914)(cid:931)(cid:938)(cid:849)(cid:916)(cid:918)(cid:925)(cid:925)(cid:849)(cid:916)(cid:914)(cid:925)(cid:925)(cid:922)(cid:927)(cid:920)(cid:849)(cid:928)(cid:919)(cid:849)
828 (cid:914)(cid:922)(cid:931)(cid:936)(cid:914)(cid:938)(cid:849)(cid:932)(cid:914)(cid:926)(cid:929)(cid:925)(cid:918)(cid:932)(cid:849)(cid:936)(cid:918)(cid:931)(cid:918)(cid:849)(cid:916)(cid:914)(cid:931)(cid:931)(cid:922)(cid:918)(cid:917)(cid:849)(cid:928)(cid:934)(cid:933)(cid:849)(cid:935)(cid:922)(cid:914)(cid:849)(cid:933)(cid:921)(cid:918)(cid:849)(cid:900)(cid:901)(cid:882)(cid:899)(cid:932)(cid:928)(cid:925)(cid:928)(cid:849)(cid:919)(cid:934)(cid:927)(cid:916)(cid:933)(cid:922)(cid:928)(cid:927)(cid:914)(cid:925)(cid:922)(cid:933)(cid:938)(cid:849)(cid:928)(cid:919)(cid:849)
829 (cid:900)(cid:901)(cid:882)(cid:899)(cid:849) (cid:867)(cid:863)(cid:872)(cid:863)(cid:868)(cid:914)(cid:861)(cid:849) (cid:936)(cid:922)(cid:933)(cid:921)(cid:849) (cid:933)(cid:921)(cid:918)(cid:849) (cid:916)(cid:918)(cid:925)(cid:925)(cid:849) (cid:916)(cid:914)(cid:925)(cid:925)(cid:922)(cid:927)(cid:920)(cid:849) (cid:932)(cid:934)(cid:915)(cid:932)(cid:918)(cid:930)(cid:934)(cid:918)(cid:927)(cid:933)(cid:925)(cid:938)(cid:849) (cid:931)(cid:918)(cid:919)(cid:922)(cid:927)(cid:918)(cid:917)(cid:849) (cid:936)(cid:922)(cid:933)(cid:921)(cid:849) (cid:884)(cid:918)(cid:925)(cid:925)(cid:849)
830 (cid:899)(cid:914)(cid:927)(cid:920)(cid:918)(cid:931)(cid:849)(cid:868)(cid:863)(cid:865)(cid:863)(cid:867)(cid:856)(cid:932)(cid:849)(cid:935)(cid:918)(cid:931)(cid:932)(cid:922)(cid:928)(cid:927)(cid:849)(cid:928)(cid:919)(cid:849)(cid:886)(cid:926)(cid:929)(cid:933)(cid:938)(cid:885)(cid:931)(cid:928)(cid:929)(cid:932)55. This algorithm has been made available as
831 emptydrops on PyPi. Initial doublets were called on a per-sample basis by computing Scrublet56
28

832 scores for each cell, propagating them through an over-clustered manifold by replacing
833 individual scores with per-cluster medians, and identifying statistically significant values from
834 the resulting distribution, replicating the approach of Pijuan-Sala et al, 201957 and Popescu et al,
835 201958. The clustering was performed with the Leiden59 algorithm on a KNN graph of a PCA
836 space derived from a log(CPM/100 + 1) representation of highly variable genes, following
837 SCANPY protocol60, and overclustering was achieved by performing an additional clustering of
838 each resulting cluster. The primary clustering also served as input for ambient RNA removal via
839
SoupX61.
840
841 Metagenomic analysis
842 To ensure that patients in our cohort did not carry undiagnosed infections, we carried out a
843 metagenomic analysis that was performed with mg2sc (https://github.com/julianeweller/mg2sc).
844 The metagenomic tool Kraken 262 (D. E. Wood, Lu, and Langmead 2019) was installed
845 following standard instructions on GitHub63,64. The pre-built standard Kraken 2 database was
846 downloaded from https://benlangmead.github.io/aws-indexes/k2 (Standard from 12/2/2020,
847 36GB). Only reads that were not aligned to Homo Sapiens with STARsolo65 were extracted from
848 the STARsolo and converted into FASTQ using bedtools v.2.3066,67 for subsequent metagenomic
849 analysis. This was performed using python scripts available on Github
850 (https://github.com/julianeweller/mg2sc) and the command “scMeG-kraken.py --input [bamfile,
851 e.g. starsolo/Aligned.sortedByCoord.out.bam] --outdir [output directory] / --DBpath [path to
852 kraken database] --threads [#, e.g. 8] --prefix [prefered file prefix] --verbosity
853 [error/warning/info/debug]” resulting in a matrix of cell barcodes with assigned taxonomy
854 transcript counts. Organisms shown are highly variable between samples with min_mean=0.08,
855 max_mean=10, and min_disp=0.05. Results are shown in Extended Data Fig. 9.
856
857 Confocal microscopy method
858 Nasal epithelial biopsies were placed in Antigenfix (Microm Microtech) for 1-2 h at 4°C, then
859 30% sucrose in PBS for 12-24 h at 4°C, before cryopreservation in OCT (Cell Path). 30μm
860 sections were permeabilised and blocked in PBS containing 0.3% Triton (Sigma), 1% normal
861 goat serum, 1% normal donkey serum, and 1% BSA (R&D) for 1-2 h at room temperature (RT).
862 Samples were stained with a 1 in 50 dilution of anti-human S100A9 conjugated to FITC (clone:
29

863 MRP 1H9, Biolegend) and a 1 in 50 dilution of anti-human EpCam conjugated to APC (clone:
864 MRP14, Biolegend cat. # 350703) in blocking buffer overnight and washed for 3 x 10 minutes in
865 PBS before mounting with Fluoromount-G containing DAPI (Invitrogen). Images were acquired
866 using a Leica SP8 confocal microscope. Raw imaging data were processed using Imaris
867 (Bitplane).
868
869 Airway single cell RNA-seq data processing
870
871 Quality control, normalization and clustering
872 To account for large quality variance across different samples, quality control was done on
873 SoupX-cleaned expression matrix for each sample separately. QC thresholds were automatically
874 established by fitting a 10-component Gaussian mixture model to log-transformed UMI count
875 per cell and to percentage of mitochondrial gene expression and finding the lower or higher
876 bounds where probability density falls under 0.05. We also excluded cells with hemoglobin
877 expression >0.1% of total expression and genes expressed in fewer than 3 cells. Expression
878 values were then normalised to a sum of 1e4 per cell and log transformed with an added pseudo-
879 counting of 1. Highly variable genes were selected within each sample and then merged with the
880 top 3000 most commonly found genes chosen using Scanpy60 function
881 “scanpy.pp.highly_variable_genes()”. After removing mitochondrial and ribosomal genes from
882 the list of highly variable genes, principle component analysis was performed and top 30
883 principle components were selected as input for BBKNN68 to correct batch effects between
884 donors and compute a batch-corrected KNN graph. Leiden clustering was performed on this
885 graph with a resolution of 0.2 to separate broad cell types (epithelial cells, B/plasma cells,
886 T/NK/ILC cells and myeloid cells). Then for each broad cell type, clustering was repeated
887 starting from highly variable gene discovery to achieve higher resolution and more accurate
888 separation of refined cell types. Sub-clusters were manually examined and further re-clustered
889 when necessary.
890
891 Quantifying SARS-CoV-2 viral expression
30

892 For donor-level quantification, we took the data before ambient RNA removal by SoupX as
893 ambient viral RNA still reflects totally viral load. For cell type level quantification, we used the
894 data after ambient RNA removal as ambient viral RNA cannot be assigned to specific cells.
895
896 Developmental trajectory inference
897 RNA velocity analysis was performed to infer developmental trajectory for the major epithelial
898 cell types (excluding melanocytes, ionocytes, brush cells and neuroendocrine cells). Spliced and
899 unspliced UMI counts were generated via the STARsolo functionality of STAR 2.7.3a. scvelo
900 was used to fit a dynamical model as previously described69, based on top 2,000 highly variable
901 genes with at least 20 UMI for both spliced and unspliced transcripts across all cells.
902
903 Expression signature analysis
904 Gene sets “GOBP_response_to_interferon_alpha”, “GOBP_response_to_interferon_gamma”,
905 “GOBP_response_to_tumor_necrosis_factor” and “GOBP_neutrophil_migration” were retrieved
906 from Molecular Signature Database (gsea-msigdb.org)70 and Scanpy function
907 “scanpy.tl.score_genes()” was used to score signature for each cell.
908
909 CITE-seq data processing
910
911 Demultiplexing and doublet removal of PBMC samples
912 For pooled donor CITE-seq samples, the donor ID of each cell was determined by genotype-
913 based demultiplexing using souporcell version 271. Souporcell analyses were performed with
914 ‘skip_remap’ enabled and a set of known donor genotypes given under the ‘common_variants’
915 parameter. The donor ID of each souporcell genotype cluster was annotated by comparing each
916 souporcell genotype to the set of known genotypes. Droplets that contained more than one
917 genotype according to souporcell were flagged as ‘ground-truth’ doublets for heterotypic doublet
918 identification. Ground-truth doublets were used by DoubletFinder 2.0.372 to empirically
919 determine an optimal ‘pK’ value for doublet detection. DoubletFinder analysis was performed on
920 each sample separately using 10 principal components, a ‘pN’ value of 0.25, and the ‘nExp’
921 parameter estimated from the fraction of ground-truth doublets and the number of pooled donors.
922
31

923 CITE-seq background and ambient RNA subtraction
924 Background and non-specific staining by the antibodies used in CITE-seq was estimated using
925 SoupX version 1.4.861, which models the background signal on near-empty droplets. The
926 ‘soupQuantile’ and ‘tfidfMin’ parameters were set to 0.25 and 0.2, respectively, and lowered by
927 decrements of 0.05 until the contamination fraction was calculated using the ‘autoEstCont’
928 function. Gene expression data was also corrected with SoupX to remove cell free mRNA
929 contamination using default SoupX parameters.
930
931 CITE-seq quality control and normalization
932 CITE-seq data was filtered by removing droplets with fewer than 200 genes expressed or with
933 more than 10% of the counts originating from mitochondrial genes. Gene expression data was
934 normalized with a log + 1 transformation (log1p), and 2000 hyper variable genes were selected
935 with the vst algorithm in Seurat version 3.9.9.902473. Antibody derived tag counts were
936 normalized with the centered log-ratio (CLR) transformation.
937
938 Integrated embedding and clustering of CITE-seq data
939 Principal component analysis was run separately on gene expression and antibody derived tag
940 count data, followed by batch correction using harmony74 on the sequencing library identifier.
941 Nearest neighbor graphs and uniform manifold approximation and projections (UMAP) were
942 generated based on the first 30 harmony-adjusted principal components. The first 30 harmony-
943 adjusted principal components of both gene expression and antibody derived tag count data were
944 used to compute a weighted nearest neighbor (WNN) graph
945 [https://doi.org/10.1101/2020.10.12.335331] with Seurat and embedded using UMAP. Cells
946 were clustered with the Leiden algorithm using the igraph R package, with a resolution of 4.
947 After initial clustering of all PBMCs, subsets of all T and NK cells, all B and plasma cells, and
948 all monocytes and DCs were reclustered after hypervariable gene selection within each subset.
949 Cells in WNN-based clusters with less than 100 members were reassigned based on the closest
950 multimodal neighbour.
951
952 Comparison PBMCs and Azimuth
32

953 The manual blood cell-type annotation was validated using the Azimuth tool
954 (https://azimuth.hubmapconsortium.org). A randomly sampled subset of 100,000 PBMCs were
955 uploaded to predict their cell type identity.
956
957 Differential expression analysis in airway data
958 In addition to the differential expression analysis, correcting for various metadata, that was
959 performed on the whole airway and PBMC data sets as described below, results shown for
960 subsets of the data were obtained with a simpler method. After subsetting cell types and/or age
961 groups, a Wilcoxon rank-sum test (implemented in Scanpy60) was performed to compare gene
962 groups. The sets of differentially expressed genes were further analysed with the g:Profiler
963 toolkit75 (g:Profiler version e102_eg49_p15_7a9b4d6, database updated on 15/12/2020) for
964 functional enrichment analysis. The expression of SARS-CoV-2 viral entry factors, including
965 ACE2 and secondary entry receptors (NRP176,77, BSG78, TFRC79), along with other viral entry-
966 associated factors, were analysed in each cell type (Extended Data Fig. 4a).
967
968 Defining the interferon-stimulated signature in blood
969 The genes that make up the interferon-stimulated signature in blood were defined by performing
970 Wilcoxon rank-sum test in Seurat between each interferon-stimulated subpopulation and its
971 matched unstimulated population. The genes that were most significant (FDR not distinguishable
972 from 0) in all comparisons were included in the interferon-stimulated signature shown in Fig. 3.
973 This list includes BST2, CMPK2, EIF2AK2, EPSTI1, HERC5, IFI35, IFI44L, IFI6, IFIT3,
974 ISG15, LY6E, MX1, MX2, OAS1, OAS2, PARP9, PLSCR1, SAMD9, SAMD9L, SP110,
975 STAT1, TRIM22, UBE2L6, XAF1 and IRF7.
976
977 Inference of ethnicity from single cell RNA-seq data
978 The latest biallelic SNP genotype data (GRCh38) was obtained from 1000 Genomes Project (see
979 URL:
980 ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/data_collections/1000_genomes_project/release/201812
981 03_biallelic_SNV/). Allele specific counts of RNA-seq reads at the SNP location in 1000
982 Genomes Project data were generated for each airway sample. Because the read coverage from
983 the scRNA-seq data was strongly enriched around the 5' end of a gene, SNP loci covered at least
33

984 20 reads for more than 90% of samples that were used (19,733 genome-wide SNP loci in total).
985 The SNP genotype from allele specific expression was determined as a maximum posterior
986 genotype after fitting a beta-binomial mixture distribution with underlying probabilities of 0.01,
987 0.5 and 0.99 for reference homozygote, heterozygote and alternative homozygote, respectively.
988 The overdispersion parameter of the beta-binomial distribution was estimated for each sample
989 independently shared across all SNPs. The genotype data from 1000 Genomes samples were
990 combined with the genotype data for our samples, and principal component analysis was
991 performed on the scaled genotype data (mean 0 and standard deviation equal to 1 for each SNP
992 locus). The ethnicity of each sample was determined by the Mahalanobis distance to the four
993 major ethnic groups in the 1000 Genomes Project (African, East Asian, European and South
994 Asian). The first three principal components were used to compute the cluster centre and the
995 covariance matrix for each ethnic group.
996
997 Cell type composition analysis
998 The number of cells for each sample and cell type combination was modelled with a generalised
999 linear mixed model with a Poisson outcome. The five clinical factors (age, sex, inferred
1000 ethnicity, tissue and the interaction of COVID-19 status and broad age group) and three technical
1001 factors (donor, 10X kit, sequencing batch and sample) were fitted as random effects to overcome
1002 the colinearity among the factors. The effect of each clinical/technical factor on cell type
1003 composition was estimated by the interaction term with the cell type. The ‘glmer’ function in the
1004 lme4 package implemented on R was used to fit the model. The standard error of the variance
1005 parameter for each factor was estimated using the numDeriv package. The conditional
1006 distribution of the fold change estimate of a level of each factor was obtained by the ‘ranef’
1007 function in the lme4 package. The log fold change is relative to the grand mean and adjusted so
1008 that it becomes 0 when there is no effect. The statistical significance of the fold change estimate
1009 was measured by the local true sign rate (LTSR) which is the probability that the estimated
1010 direction of the effect is true, i.e. the probability that the true log fold change is greater than 0 if
1011 the estimated mean is positive (or less than 0 if the estimated mean is negative). It is calculated
1012 based on the estimated mean and standard deviation of the distribution of the effect (log fold
1013 change), which is to an extent similar to performing a (one-sided) one-sample Z-test and
1014 showing (1 - p_value).
34

1015
1016 Differential expression analysis using metadata
1017 We performed differential gene expression analysis for both airway and PBMC data. We used
1018 the 7 clinical (Donor, Age group, Sex, Ethnicity, Tissue, Smoking status and COVID-19 status)
1019 and the 4 technical factors (Batch, 10X kit version, the number of expressed genes and the
1020 number of mapped fragments) to adjust confounding effects. For PBMC data, the tissue and 10X
1021 kit were identical across samples and not included in the model. We utilised the linear mixed
1022 model proposed in Young et al80 to adjust for the 11 confounding factor effects and the effect of
1023 cell type as a random effect in differential expression analysis. We fit the model on a gene-by-
1024 gene basis using the estimated variance parameters to test each factor k explaining a significant
1025 amount of transcription variation. If the focal factor k is a categorical variable with L levels (e.g.,
1026 COVID-19 status with 3 levels), we partitioned the levels into one of two groups. There are 2L-1
1027 contrasts which were tested against the null model (removing the focal factor k in the model) to
1028 compute Bayes factors. Then, those Bayes factors were used for fitting a finite mixture model to
1029 compute the posterior probability as well as the local true sign rate (ltsr) (See Supplementary
1030 Note of Young et al80 Section 1.3 for more details). We used g:Profiler 2 implemented in R
1031 (version 2.0.1.5) to identify which pathways are enriched for differentially expressed genes for
1032 each contrast. We used genes whose ltsr is greater than 0.5 to perform the analysis (both
1033 upregulated and downregulated genes separately).
1034
1035 Single-cell VDJ-sequencing data analysis
1036 TCR and BCR sequencing data was processed using the Cellranger software and downstream
1037 analysis was performed using the scirpy package (version 0.6.1)81. Briefly, we integrated TCR
1038 and BCR data with gene expression from T cell and B cell subsets, respectively. After
1039 categorizing cells based on the detection of productive antigen receptor chains, we selected cells
1040 with a single pair of productive chains for further analysis. T cell clonotypes were defined at the
1041 amino acid level, considering both receptor chains. B cell clonotypes were defined at the amino
1042 acid level while allowing for a Hamming distance of up to 10% of the sequence, considering
1043 both receptor chains.
1044
35

1045
1046 References
1047 53. Lee, P. Y. et al. Distinct clinical and immunological features of SARS-CoV-2-induced
1048 multisystem inflammatory syndrome in children. J. Clin. Invest. 130, 5942–5950 (2020).
1049 54. Worlock, K. B. Cell dissociation from nasal, bronchial and tracheal brushings with cold-
1050 active protease for single-cell RNA-seq. (2021) doi:10.17504/protocols.io.btpunmnw.
1051 55. Lun, A. T. L. et al. EmptyDrops: distinguishing cells from empty droplets in droplet-based
1052 single-cell RNA sequencing data. Genome Biol. 20, 63 (2019).
1053 56. Wolock, S. L., Lopez, R. & Klein, A. M. Scrublet: Computational Identification of Cell
1054 Doublets in Single-Cell Transcriptomic Data. Cell Syst 8, 281–291.e9 (2019).
1055 57. Pijuan-Sala, B. et al. A single-cell molecular map of mouse gastrulation and early
1056 organogenesis. Nature 566, 490–495 (2019).
1057 58. Popescu, D.-M. et al. Decoding human fetal liver haematopoiesis. Nature 574, 365–371
1058 (2019).
1059 59. Traag, V. A., Waltman, L. & van Eck, N. J. From Louvain to Leiden: guaranteeing well-
1060 connected communities. Sci. Rep. 9, 5233 (2019).
1061 60. Wolf, F. A., Angerer, P. & Theis, F. J. SCANPY: large-scale single-cell gene expression
1062 data analysis. Genome Biol. 19, 15 (2018).
1063 61. Young, M. D. & Behjati, S. SoupX removes ambient RNA contamination from droplet-
1064 based single-cell RNA sequencing data. Gigascience 9, (2020).
1065 62. Wood, D. E., Lu, J. & Langmead, B. Improved metagenomic analysis with Kraken 2.
1066 Genome Biol. 20, 257 (2019).
1067 63. Wood, D. kraken2. https://github.com/DerrickWood/kraken2, (2018).
1068 64. Bost, P. Viral-Track. https://github.com/PierreBSC/Viral-Track, (2020).
36

1069 65. Dobin, A. et al. STAR: ultrafast universal RNA-seq aligner. Bioinformatics 29, 15–21
1070 (2013).
1071 66. Quinlan, A. R. & Hall, I. M. BEDTools: a flexible suite of utilities for comparing genomic
1072 features. Bioinformatics 26, 841–842 (2010).
1073 67. Quinlan, A. bedtools2. https://github.com/arq5x/bedtools2, (2021).
1074 68. Polański, K. et al. BBKNN: fast batch alignment of single cell transcriptomes.
1075 Bioinformatics 36, 964–965 (2020).
1076 69. Bergen, V., Lange, M., Peidli, S., Wolf, F. A. & Theis, F. J. Generalizing RNA velocity to
1077 transient cell states through dynamical modeling. Nat. Biotechnol. 38, 1408–1414 (2020).
1078 70. Subramanian, A. et al. Gene set enrichment analysis: a knowledge-based approach for
1079 interpreting genome-wide expression profiles. Proc. Natl. Acad. Sci. U. S. A. 102, 15545–
1080 15550 (2005).
1081 71. Heaton, H. et al. Souporcell: robust clustering of single-cell RNA-seq data by genotype
1082 without reference genotypes. Nat. Methods 17, 615–620 (2020).
1083 72. McGinnis, C. S., Murrow, L. M. & Gartner, Z. J. DoubletFinder: Doublet Detection in
1084 Single-Cell RNA Sequencing Data Using Artificial Nearest Neighbors. Cell Syst 8, 329–
1085 337.e4 (2019).
1086 73. Stuart, T. et al. Comprehensive Integration of Single-Cell Data. Cell 177 1888–1902.e21
1087 (2019).
1088 74. Korsunsky, I. et al. Fast, sensitive and accurate integration of single-cell data with
1089 Harmony. Nat. Methods 16, 1289–1296 (2019).
1090 75. Reimand, J. et al. g:Profiler-a web server for functional interpretation of gene lists (2016
1091 update). Nucleic Acids Res. 44, W83–9 (2016).
37

1092 76. Cantuti-Castelvetri, L. et al. Neuropilin-1 facilitates SARS-CoV-2 cell entry and infectivity.
1093 Science 370, 856–860 (2020).
1094 77. Daly, J. L. et al. Neuropilin-1 is a host factor for SARS-CoV-2 infection. Science 370, 861–
1095 865 (2020).
1096 78. Wang, K. et al. CD147-spike protein is a novel route for SARS-CoV-2 infection to host
1097 cells. Signal Transduction and Targeted Therapy 5, 1–10 (2020).
1098 79. Tang, X. et al. Transferrin receptor is another receptor for SARS-CoV-2 entry. bioRxiv
1099 2020.10.23.350348 (2020) doi:10.1101/2020.10.23.350348.
1100 80. Young, A. M. H. et al. A map of transcriptional heterogeneity and regulatory variation in
1101 human microglia. Nat. Genet. 53, 861–868 (2021).
1102 81. Sturm, G. et al. Scirpy: a Scanpy extension for analyzing single-cell T-cell receptor-
1103 sequencing data. Bioinformatics 36, 4817–4818 (2020).
1104
1105
1106 Supplemental Data
1107
1108 Extended Data Fig. 1: Overview of patient cohort.
1109 (a) Overview of samples taken in our healthy, COVID-19 and post-COVID-19 cohorts. COVID-
1110 19 severity was classified as asymptomatic, mild (symptomatic without oxygen requirement or
1111 respiratory support), moderate (requiring oxygen without respiratory support) or severe
1112 (requiring non-invasive or invasive ventilation). Post-COVID-19 patients were sampled 3
1113 months after recovering from severe COVID-19. (b) Timeline of sample collections from
1114 COVID-19 positive (18 adults and 19 paediatric) and post-COVID-19 (13 adults and 2
1115 paediatric) patients enrolled in our study. Sample collections are shown relative to symptom
1116 onset and a SARS-CoV-2 positive RT-qPCR test, to which all patients are aligned.
1117
1118 Extended Data Fig. 2: Airway single cell metadata, proportions and cell type markers.
38

1119 (a) UMAP visualisation of annotated airway scRNA-seq dataset from Fig. 1b coloured by
1120 COVID-19 status and age groups. (b) Bar plot comparing nasal epithelial cell type compositions
1121 across COVID-19 status and age groups. (c) Dot plots showing marker genes for annotated
1122 airway epithelial and immune cell types, with fraction of expressing cells and average expression
1123 within each cell type indicated by dot size and colour, respectively.
1124
1125 Extended Data Fig. 3: Supplementary information for airway cell type annotation.
1126 (a) Detailed marker genes for distinct airway myeloid populations in our data set listing marker
1127 genes that are unique to each of the defined populations, whilst markers that are common to
1128 closely related myeloid cell types are shown on the right side of the panel. (b) Comparison of
1129 annotated cell types to published data sets. Marker genes for the three populations identified as
1130 differentiating to ciliated cells28 and markers of transit epithelial cells (Transit epi 1 and 2). Deu;
1131 deuterosomal, Ba-d; basal differentiating, IRC; interferon responsive cell. (c,d) Logistic
1132 regression based label transfer for the data sets in (c) Chua et al28 and (d) Ziegler et al14. (e) Bar
1133 chart showing changes in nasal epithelial cell type proportions observed across age within our
1134 paediatric and adult healthy cohorts. Error bars indicate two times standard error of the mean.
1135
1136 Extended Data Fig. 4: Expression of viral entry-associated genes in the airways.
1137 (a) Dot plots showing cell type expression of viral entry-associated genes within the upper
1138 airways of healthy adults (n=7), healthy children (n=30), COVID-19 adults (n=10) and COVID-
1139 19 children (n=18) respectively, included genes linked to SARS-CoV-2, SARS-CoV, MERS-
1140 CoV, Rhinovirus-C and Influenza A infections. The fraction of expressing cells and average
1141 expression within each cell type is indicated by dot size and colour, respectively. (b) Spearman
1142 correlation between the fraction of cells with detected viral RNA and the average expression of
1143 entry factors, as in (a), across cell types within the airways of COVID-19 patients samples (with
1144 viral reads (cid:1541)(cid:849)5) within 5 days of a positive SARS-CoV-2 qPCR test (Early) and those sampled
1145 longer than 5 days prior to onset of symptoms or positive SARS-CoV-2 qPCR test, whichever
1146 was longer (Late). Dots in blue indicate p < 0.05. (c) Expression of ACE2 in paediatric airway
1147 cells in each cell type averaged by donor (upper) and in each donor (lower) and coloured by
1148 COVID-19 status. Error bars indicate two times standard error of the mean across donors.
1149 Numbers in brackets indicate numbers of COVID-19 donors/healthy donors.
39

1150
1151 Extended Data Fig. 5: Airway cell type proportion analysis, interferon responses and
1152 differential gene expression.
1153 (a) Dot plot showing fold change and statistical significance of all airway cell type proportions
1154 across location of sampling, age group and COVID-19 status, respectively, estimated by fitting
1155 Poisson generalised linear mixed models taking into account other technical and biological
1156 variables (see Methods). (b) Feature importance plot depicting the variance accounted for by
1157 each of the clinical and technical factors in our statistical analysis of cell type proportions within
1158 our airway scRNA-seq dataset. Factors were donor (patient), patients age (Age_bin), sample
1159 location (nasal, tracheal, bronchial), COVID-19 status group (COVID-19 positive, negative or
1160 post-COVID-19), dataset (UK cohort or Chicago Cohort) sex, 10X chromium 5’ single cell
1161 sequencing kit version (kit_version) smoking status (non-smoker, ex-smoke or current), date and
1162 other factors (residual). Note: Error bars were not able to be generated for sex, Kit_version and
1163 smoker. 97 samples contributed to the estimation of variances and their standard errors. (c)
1164 Response to interferon by airway cell type. Scores of GO term gene signatures for the terms:
1165 response to type 1 interferon (GO:0035455 or GO:0034340) and interferon-gamma
1166 (GO:0034341) across cell types. Scores were calculated with Scanpy as the average expression
1167 of the signature genes subtracted with the average expression of randomly selected genes from
1168 bins of corresponding expression values. (d) Differential gene expression contrasting COVID-19
1169 and non-COVID-19 samples in transit epithelial 1 cells, inflammatory goblet 2 cells, and mono
1170 IL-6 cells.
1171
1172 Extended Data Fig. 6: Expression of cell type markers and immune compartment
1173 dynamics.
1174 (a) Expanded dot plot from Fig. 3d showing the RNA expression of cell type marker genes and
1175 interferon-stimulated genes. (b) Dotplot showing the cell surface protein expression of cell type
1176 marker proteins. In both a and b the size of the dot is scaled to the percentage of cells that have
1177 at least one count for each gene or protein, and the color is scaled to the z-score normalized
1178 expression of each gene or protein. (c) Comparison of our manual cell type PBMC annotation vs
1179 an automated annotation performed by Azimuth. (d) Fold changes of immune cell type
1180 proportions across age group and disease status. Age and disease specific changes were
40

1181 deconvoluted by fitting Poisson generalised linear mixed models taking into account other
1182 confounders such as sex and ethnicity. (e) Feature importance plot showing the variance that can
1183 be explained by the different features that were included in the Poisson linear mixed model that
1184 was fitted on the cell type proportions in the PBMC data. 80 samples contributed to the
1185 estimation of variances and their standard errors. (f) Bar plots showing the average immune cell
1186 proportions in PBMC samples. Cell types are colour coded and grouped based on their age group
1187 and disease status. N denotes the amount of samples in each group, while K denotes the amount
1188 of cells per group. (g) UMAPs as in Fig. 3a in which the COVID-19 status (left panel) and the
1189 age group (right panel) is visualised for each cell.
1190
1191 Extended Data Fig. 7: Immune cell population dynamics.
1192 (a) Fractions of unique BCR sequences show the differences in immune repertoire diversity over
1193 age and disease. (b) UMAP visualisation as in Fig. 3a showing the annotated interferon-
1194 stimulated subpopulations in clusters 35 - 42. (c) Boxplot showing the percentage of PBMCs that
1195 are interferon-stimulated in asymptomatic or symptomatic COVID-19 patients, grouped by the
1196 weeks since the onset of symptoms, and separated for adults (left) and children (right). (d)
1197 Dotplot of Spearman correlations between nasal and blood cell type proportions in paediatric
1198 COVID-19 patients and (e) in adult COVID-19 patients. In both d and e, cell type proportions in
1199 the nose (x-axis) are compared to the blood (y-axis). Correlations shown in Fig. 3g present a
1200 zoom in of the adult panel. Rows and columns in both dotplots are clustered by hierarchical
1201 clustering on the combined matrices. The size of the dots is scaled by the significance of each
1202 correlation. Colour is scaled by the Spearman rank-correlation coefficient. If a blood - nose cell
1203 type combination shows a positive correlation, this is indicative that if the blood cell type
1204 changes in proportion, the nasal cell type changes accordingly, and vice versa. Dots in a and c
1205 represent independent patient samples. Box plots were drawn with the centre line as the median
1206 of the data distribution, the hinges as the first and third quartiles, and with the whiskers
1207 extending to the lowest and highest values that were within 1.5 × interquartile range of the upper
1208 or the lower hinge.
1209
1210 Extended Data Fig. 8: Interferon expression in COVID-19 patient with highest amount of
1211 interferon-stimulated blood cells.
41

1212 (a) Ranked barplot and matched dotplots as in Fig. 3h, but showing the expression of all genes
1213 that make up the interferon-stimulated gene signature (middle) and the expression of all
1214 interferons (right) in all cells, instead of averaged signatures gene expression signatures in
1215 specific cell types. (b) Dotplot related to Fig. 3h showing the expression of all interferons in all
1216 nasal resident (top) and circulating (bottom) cell types that were present in this individual. The
1217 size of the dot is scaled to the percentage of cells that have at least one count for each gene or
1218 protein, and the color is scaled to the z-score normalized expression of each gene or protein.
1219
1220 Extended Data Fig. 9: Metagenomic analysis of patient sample reads that were not mapped
1221 to the human genome.
1222 (a) Dotplot showing the amount of cells that harbor reads aligned to archaea, bacteria, eukaryota
1223 (including human reads that initially did not align to the human transcriptome by STARsolo) and
1224 viruses. (b) Dotplot showing the amount of cells that harbor reads to a selection of disease-
1225 relevant bacteria and viruses. Apart from SARS-CoV-2 and non-specific signal found in most
1226 samples, we did not detect any pathogens that were highly abundant in samples of interest.
1227
1228 Extended Data Table 1: Summary of patient metadata.
1229 Patients were divided into columns according to COVID-19 status. Metadata on median age, sex,
1230 ethnicity, peripheral blood counts at the time of sampling, reported symptoms, respiratory
1231 support, COVID-19 severity, diagnosis of multisystem inflammatory syndrome in children
1232 (MIS-C), detected co-infection and specific anti-COVID-19 treatment prior to sampling, are
1233 shown. Abbreviations: HFNC = high flow nasal cannula, NIPPV = non-invasive positive
1234 pressure ventilation, IMV = invasive mechanical ventilation, NA = not assessed.
1235
1236 Consortia information
1237
1238 NU SCRIPT Study Investigators authors list:
1239 A Christine Argento8 *, Catherine A Gao8 *, Alexander V Misharin8 *, GR Scott Budinger8, Jane
1240 E Dematte8 *, Helen K Donnelly8, Nikolay S Markov8, Richard G. Wunderink8 *, Sean B Smith8
1241 *, Taylor A Poor8 *, Ziyan Lu8.
42

1242
1243 *already included as named co-author
1244 Affiliations
1245 8Division of Pulmonary and Critical Care Medicine, Northwestern University Feinberg School of
1246 Medicine, Chicago, USA
1247
1248
43

bb
a
12
91
)24082=n( +2AFIPB 2 telboG
31
)5997=n( 1 lasaB 0
)15631
) = 0 n 4 ( 3 ) y 9 2 r = o 5 n t 7 a ( 7 m + = m U n( A a 1 l L f n P ip i e 2 2 t t t i e e s l l n b b a o o r G G T
4 5 6 1 1 1
)078= ) n 5 ( 1 + 7 2 2 )1 S = 0 B n 1 ( R 1 l D a 2 s = H a n K b ( 1 2 g n l l a a il s s c a a yC B B 1 2 3
81 32 71 7 02
)3914=n( 2 ipe tisnarT
71
)034=n( rosrucerp kcolliH 4 35
61
)2942=n( lamosoretueD
81
)453=n( kcollih gnilcyC 5
6
41
)66423=n( 1 detailiC
91
)0752=n( kcolliH 6
51
)5 )9 4 8 0 2 5 2 = ) = 1 n n 6 ( ( = 2 n e d t ( y e h c t s o a u n il r i o C B I
2 0 1 2 2 2
)4807=n(
) + 9 ) 4 2 5 T 6 5 N 2 8 2 L = = A n n ( G ( s u y y r r o o o m t t e e a r r u c c q e e S S S 7 8 9 0 42 4
2
228
21 31
)46=n( enircodneorueN
32
)4341=n( tcuD 01
01
)48=n( etyconaleM
42
)1819=n( bulC 11 1 )80771=n( 1 telboG 21
9 11
)2352=n( caM
0
c
)8
) 6 7 6 5 1 2 = 3 n = ) ) ( n 2 8 ) d ( 7 2 9 ) e ) d 3 0 1 1 0 t e = 8 = 4 s 7 t 1 n 0 n u a 5 = ( 3 ( a v 2 n K = h L i = t ( n x c g g n e a g ( I I ( n e a a m m m i v m m lc e e e ia s s y m m m n c a a l l B P P B B B B 0 1 2 3 4 5 6
4
5 0 3 1 2 )04 ) 3 0 ) = 0 3 n 0 8 ( ) ) 1 3 9 5 d = = 8 4 e n n 8 4 t ( ( s = = 2 3 u n n ) ) 7 2 a ( ( m m 1 8 h i o h 3 1 e e x l 6 6 = = e m m 5 5 n n 8 d d ( ( 8 8 D c c D D d T C g K K K C C
N N N T T T T
1 2 0 3 4 8 9 1 1 1 1 1
) ) 9 1 7 8 1 = ) 1 n ) 6 2 = ( 0 3 n + 3 4 ) ) ( 4 2 6 = 1 ) m R 5 8 8 n = 3 2 C 2 ( e n = = 1 m g ( C n n = n e ( ( n 4 4 i v lc T ( g D D i a y e I h C C A n c r f M T T T T T T
0 1 2 3 4 5 6
4
2
1 5 0
3 7
9 6 01 51 11 21
41
31
) ) 7 0 4 ) 2 0 9 ) 8 2 7 1 = 9 ) 2 = 3 n 2 1 n 8 ( = = ( 3 + n n + 4 1 ( ( 0 = R d d 1 n ) e e A 2 L ( t t ) 8 B C a a + 4 7 v P v 6 X 1 = i i L 5 G t C t n c c I = a ( a o o o n t n n n C ( c u o o a o e C D M M M M N L c
1 2 3 4 5 6 7
0 4
1 3
2 5 7 0 8 1
6 )211=n( CLI
51
)3592=n( 1 mem 8DC T
7
8
)894=n( CDp
8
6
)94=n( CDf
9
9
41.0
)291=n( tsaM
01
21.0 01.0 f
e
d
80.0 60.0 40.0 20.0 00.0
dioleyM amsalP/B CLI/KN/T etyconaleM enircodneorueN hsurB etyconoI 2 detailiC 1 detailiC lamosoretueD 2 ipe tisnarT 1 ipe tisnarT yrotammalfni 2 telboG
+UALP 2 telboG +2AFIPB 2 telboG
1 telboG
bulC tcuD +4TNLAG yroterceS yroterceS suomauqS kcolliH kcollih gnilcyC rosrucerp kcolliH lasab gnilcyC 2 lasaB +2SBRDHK 1 lasaB 1 lasaB sllec +2-VoC-SRAS fo noitcarF
4PA
8PP 81PP
7PP 5PP 1PP 7PA 5PA 3PP 4PP 9PA 1PA 31PP 2PP 11PP
51PP 91PP 21PA
21PP
6PP
61PP
01PP
71PP 41PA 11PA 01PA
8PA
9PP
lavretni noitcelloc
noitcefnI
noitcarf IMU 2-VoC-SRAS
hserf
eson
x01’5
aehcart
RCT
ihcnorb
RCB
/nezorf
doolb
dewaht
x01’5
qes-ETIC
sCMBP
RCT
elpmaS
RCB
stneitaP
doolB
ihcnorb/aehcarT
esoN
42
71 03
03
yhtlaeH
cirtaideaP
31
2 81
91
91-DIVOC
cirtaideaP
11
0 7
11
yhtlaeH
tludA
21
4 01
81
91-DIVOC
tludA
022,224
799,632
rebmun
llec
latoT
2-01
)291=n( tsaM
000111
3-01
e
4-01 5-01 6-01
52 02 51
01
5

b
a
noitargim
tueN
(cid:302)(cid:16)(cid:41)(cid:49)(cid:55)
(cid:534)(cid:16)(cid:49)(cid:41)(cid:44)
(cid:302)(cid:16)(cid:49)(cid:41)(cid:44)
yhtlaeH,tludA
91-DIVOC,tludA
91-DIVO(cid:38)(cid:237)(cid:87)(cid:86)(cid:82)P,tludA
yhtlaeH,deaP
91-DIVOC,deaP
91-DIVO(cid:38)(cid:237)(cid:87)(cid:86)(cid:82)P,deaP
gnirocs naem ,tludA sv deaP ,yhtlaeH ,ipE 2 ipe tisnarT 1 ipe tisnarT suomauqS +4TNLAG yroterceS yroterceS enircodneorueN etyconaleM etyconoI rosrucerp kcolliH kcolliH yrotammalfni 2telboG +UALP 2 telboG +2AFIPB 2 telboG 1 telboG tcuD lamosoretueD kcollih gnilcyC lasab gnilcyC bulC 2 detailiC 1 detailiC hsurB 2 lasaB +2SBRDHK 1 lasaB 1 lasaB
e
d
c
noitargim
tueN
gnirocs naem ,tludA sv deaP ,91-DIVOC ,ipE
g
9A001S
mu02
MACPE
9A001S
MACPE
IPAD
CDp
CDf detavitca CDc ger T evian T dg T hf T gnilcyc T
3 mem 8DC T
2 mem 8DC T
1 mem 8DC T detsuahxe 8DC T mem 4DC T
+4RCC 4DC T LgI amsalP KgI amsalP tueN TKN ol65dc KN ih65dc KN +6LI onoM +1RABPG onoM +01LCXC onoM tsaM detavitca caM caM TIAM CL CLI evian B detsuahxe mem B detavitca mem B mem B gnilcyc B
gnirocs naem
,tludA
sv deaP ,yhtlaeH ,enummI
gnirocs naem
,tludA
sv deaP ,91-DIVOC ,enummI
ecnereffiD (cid:19)(cid:24)(cid:17)(cid:19) (cid:24)(cid:21)(cid:17)(cid:19)
0
(cid:24)(cid:21)(cid:17)(cid:19)(cid:237) (cid:19)(cid:24)(cid:17)(cid:19)(cid:237)
f
yawhtap gnilangis NFI I epyt
noitacilper
emoneg lariv fo noitaluger evitagen ylbmessa muilic elitom (cid:534)(cid:16)(cid:49)(cid:41)(cid:44)(cid:3)(cid:82)(cid:87)(cid:3)(cid:72)(cid:86)(cid:81)(cid:82)(cid:83)(cid:86)(cid:72)(cid:85) yawhtap gnilangis detaidem-72-LI
log10(adjusted p value)
(cid:404) (cid:404)(cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404)(cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404)(cid:404) (cid:404) (cid:404) (cid:404)(cid:404) (cid:404)(cid:404) (cid:404) (cid:404) (cid:404)(cid:404) (cid:404)(cid:404) (cid:404) (cid:404) (cid:404)(cid:404) (cid:404)(cid:404) (cid:404)(cid:404) (cid:404)(cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404)(cid:404) (cid:404)(cid:404) (cid:404) (cid:404) (cid:404)(cid:404) (cid:404) (cid:404) (cid:404)(cid:404) (cid:404)(cid:404) (cid:404) (cid:404)(cid:404)(cid:404)(cid:404)(cid:404)(cid:404)(cid:404)(cid:404)(cid:404)(cid:404)(cid:404)(cid:404)(cid:404)(cid:404)(cid:404)(cid:404)(cid:404)(cid:404)(cid:404)(cid:404)(cid:404)(cid:404)(cid:404)(cid:404)(cid:404)(cid:404)(cid:404)(cid:404)(cid:404)(cid:404)(cid:404)(cid:404)(cid:404)(cid:404)(cid:404)(cid:404)(cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404)(cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404)(cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404)(cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404)(cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404)(cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404)(cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404)(cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404)(cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404)(cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404)(cid:404) (cid:404) (cid:404) (cid:404)(cid:404) (cid:404)(cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404)(cid:404) (cid:404)(cid:404) (cid:404)(cid:404) (cid:404) (cid:404) (cid:404)(cid:404) (cid:404) (cid:404) (cid:404)(cid:404) (cid:404)(cid:404) (cid:404) (cid:404) (cid:404)(cid:404) (cid:404)(cid:404) (cid:404) (cid:404) (cid:404)(cid:404) (cid:404) (cid:404)(cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404)(cid:404) (cid:404)(cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404)(cid:404) (cid:404)(cid:404) (cid:404)(cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404)(cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404)(cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404)(cid:404) (cid:404) (cid:404)(cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404)(cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404)(cid:404) (cid:404) (cid:404)(cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404)(cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404)(cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404)(cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404)(cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404)(cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404) (cid:404)(cid:404)(cid:404)(cid:404)(cid:404)(cid:404)(cid:404)(cid:404)(cid:404)(cid:404)(cid:404)(cid:404)(cid:404)(cid:404)(cid:404)(cid:404)(cid:404)(cid:404)(cid:404)(cid:404)(cid:404)(cid:404)(cid:404)(cid:404)(cid:404)(cid:404)(cid:404)(cid:404)(cid:404)(cid:404)(cid:404)(cid:404)(cid:404)(cid:404)(cid:404)(cid:404)(cid:404)
51
etyconom
+6-LI
yrotammalfni 2 telboG 1 ipe tisnarT
yawhtap
gnilangis
NFI I epyt
01
noitcudorp
NFI
I epyt
fo noitaluger
(cid:534)(cid:16)(cid:49)(cid:41)(cid:44)(cid:3)(cid:82)(cid:87)(cid:3)(cid:72)(cid:86)(cid:81)(cid:82)(cid:83)(cid:86)(cid:72)(cid:85)
5
yawhtap
gnilangis
detaidem-72-LI
0
noitcudorp
01-PI fo
noitaluger
evitagen
tsaM detavitca CDc tueN +6LI onoM +1RABPG onoM +01LCXC onoM caM LgI amsalP KgI amsalP gnilcyc B detavitca mem B detsuahxe mem B mem B evian B ol65dc KN TKN 3 mem 8DC T 2 mem 8DC T 1 mem 8DC T mem 4DC T evian T enircodneorueN etyconoI 1 detailiC 2 ipe tisnarT 1 ipe tisnarT yrotammalfni 2 telboG +UALP 2 telboG +2AFIPB 2 telboG 1 telboG bulC tcuD yroterceS suomauqS kcollih gnilcyC rosrucerp kcolliH +2SBRDHK 1 lasaB
CF2goL 1 0
esoN aehcarT
(cid:20)(cid:237)
ihcnorB etanoeN tnafnI
RSTL
d d l li i h h C c gnuoY
(cid:24)(cid:17)(cid:19)
tnecselodA
(cid:28)(cid:17)(cid:19)
y tl l u re d d A lE
(cid:28)(cid:28)(cid:17)(cid:19)
tludA,yhtlaeH
(cid:28)(cid:28)(cid:28)(cid:17)(cid:19)
t t l l u u d d A A , , 9 9 1 1 - - D D IV IV O O (cid:38) C (cid:237)(cid:87)(cid:86)(cid:82)P deaP,yhtlaeH deaP,91-DIVOC
(cid:302)(cid:16)(cid:41)(cid:49)(cid:55)
(cid:302)(cid:16)(cid:49)(cid:41)(cid:44)
deaP,91-DIVO(cid:38)(cid:237)(cid:87)(cid:86)(cid:82)P
2
****
1 0 2 1 0
Epi Immune
2
****
1 0 2 1 0
****
****
****
****
********
****
yhtlaeH,tludA
dliM/citamotpmysA,tludA
ereveS/etaredoM,tludA
yhtlaeH,deaP
dliM/citamotpmysA,deaP
ereveS/etaredoM,deaP
Epi Immune
****
****
**** ****
****
****
****
****
**** ****
****
****
************
****
****
**** ****
****
****
sn
****
**** ****
sn
****
************
****
noitargim
tueN
****
****
**** ****
****
****
****
****
****
****
**** ****
****
****
****
****
****
****
****
****
********
**** ****
noitargim
tueN
erocS erocS
(cid:534)(cid:16)(cid:49)(cid:41)(cid:44)
(cid:302)(cid:16)(cid:41)(cid:49)(cid:55) (cid:534)(cid:16)(cid:49)(cid:41)(cid:44) (cid:302)(cid:16)(cid:49)(cid:41)(cid:44) (cid:302)(cid:16)(cid:41)(cid:49)(cid:55) (cid:534)(cid:16)(cid:49)(cid:41)(cid:44) (cid:302)(cid:16)(cid:49)(cid:41)(cid:44) yawhtap gnilangis
NFI
I epyt
esnopser enummi
etanni
(cid:3)(cid:12)(cid:534)(cid:16)(cid:49)(cid:41)(cid:44)(cid:11)(cid:3)(cid:74)(cid:81)(cid:76)(cid:79)(cid:79)(cid:68)(cid:81)(cid:74)(cid:76)(cid:86)(cid:3)(cid:49)(cid:41)(cid:44)(cid:3)(cid:44)(cid:44)(cid:3)epyt remartetoreteh nitcetorplaC sixatomehc
lihportuen

)243,8=N( 61DC onoM81
)934,77=N( evian 4DC T1
)371,1=N( 1C+61DC onoM91)229,73=N(
repleh 4DC T2 3222
9 e 9 e u 9 9 t r a t 9 9 r l . 9 a 0 n . c > 0 g o i L s
) ) 5 9 4 ) 5 1 2 = 6 ,1 N = = N ( N ( C ( 1 D C C -S D D A p c
0 1 2 2 2 2
)0 ) 9 ) 0 4 5 3 9 ,3 8 2 3 , , 2 5 = 1 = N = N ( N ( e ( L v M i T a C C n 4 8 8 D D D C C C T T T 3 4 5 6171 91
81
12 02
9 9 9 . . 0 0
)39 ) 1 3 ,0 6 4 9 = ,2 N = ( N e ( v 2 ia C n D B c3
4 2 2
)34 ) 4 6 , 8 6 4 = , N 2 ( = A N R ( M M E E 8 8 D D C C T T 6 7
43 82 0313
5.0
)4 ) 7 0 5 6 ,5 0 = ,4 N = ( N m ( e m m e m w s w -n s B B
5 6 2 2
)712,63 ) = 4 N 4 ( 1 L ,5 T = C N ( 8 D d/ C g T T 8 9 7 21 31
41
51
92 62 52
)449,1=N( ravni B72
)765,8=N( ger T01 3 8
9
72
)755,1=N( sllec amsalP82
)169,3=N( TIAM11
42
)802=N( ) s 8 ts 3 a 9 l = b N am ( C sa P l H P9
0 2 3
)0 ) 3 7 6 8 ,3 6 4 = = N N ( ( T K K N N 2 3 1 1 23 331 6 1 5
4
)52=N( soE/osaB13
)327,4=N( 65DC KN41 2
)395,3=N( gnilcyC23
)504=N( CLI51 01
1
)487,1=N( steletalP33
)025,74=N( 41DC onoM61
)583=N( CBR43
)867=N( 6LI 41DC onoM71
sllec amsalP
stsalbamsalP
2CDc
CDp
1CDc
61DC onoM
steletalP
KN
gnilcyC
6LI 41DC onoM
CBR
evian 4DC T
evian 8DC T
evian B
mem ws-n B
TIAM
ravni B
ARME 8DC T
LTC 8DC T
ME 8DC T
LTC 4DC T
c
b
a
yhtlaeH:cirtaideaP 91-DIVOC:cirtaideaP 91-DIVOC-tsoP:cirtaideaP yhtlaeH:tludA 91-DIVOC:tludA 91-DIVOC-tsoP:tludA etanoeN tnafnI dlihc gnuoY
dloF
dlihC
egnahc
tnecselodA
3>
tludA ylredlE
1 3/1< g
f
d h
2SAO 1SAO 2XM 1XM
51GSI 7FRI
3TIFI 6IFI L44IFI 53IFI 2KNIPS 43DC DHGI 2RECF A3RGCF 41DC G1RECF YLNG 1FRP HMZG R7LI 1RC3XC LLES 72DC 7RCC
A8DC
4DC
D3DC
seneg detalumits
norefretnI srekram epyt lleC
mits NFI evian 4DC
T
mits NFI LTC 8DC
T
mits NFI KN mits NFI 41DC onoM mits NFI 61DC onoM mits NFI evian B mits NFI mem ws-n
B
mits NFI CPH tnecreP
noisserpxe
evitaleR dess % er 0 pxe %05
0.2
0.1
0.0 %001
mits NFI 41DC onoM
mits NFI 61DC onoM
mits NFI evian 4DC T
mits NFI LTC 8DC T
mits NFI CPH
mits NFI KN
mits NFI evian B
mits NFI mem ws-n B
0.1 57. 05. 52. 00.
yhtlaeH:cirtaideaP 91-DIVOC:cirtaideaP
eurt lacoL
91-DIVOC-tsoP:cirtaideaP
etar ngis
yhtlaeH:tludA
9999.0>
91-DIVOC:tludA
999.0
91-DIVOC-tsoP:tludA
99.0 9.0
etanoeN
5.0
tnafnI dlihc
gnuoY
dloF
dlihC
egnahc
tnecselodA
3>
tludA ylredlE
1 3/1<
ylredlE
tludA
tnecselodA
dlihC
dlihc gnuoY
tnafnI etanoeN
secneuqes RCT deifitnedi lla / secneuqes RCT euqinu #
yhtlaeH 91-DIVOC 91-DIVOC-tsoP
e
mits
NFI
mem ws-n
B:CMBP
mits
NFI
KN:CMBP
mits
NFI
evian 4DC
T:CMBP
mits
NFI
evian B:CMBP
mits
NFI
LTC 8DC
T:CMBP
llec lailehtipe +2-VoC-SRAS:lasaN
yrotammalfni 2 telboG:lasaN
+01LCXC etyconoM:lasaN
llec enummi +2-VoC-SRAS:lasaN
CDp:lasaN
detavitca CDc:lasaN
gnilcyc T:lasaN
3 mem 8DC T:lasaN
knar
s’namraepS noitalerroc tneiciffeoc
1
0
1-
fo eulav
P
noitalerroc 100.0< 1 5 1 0 . . . 0 0 0
er
s u ll t e a c N n g l F a i I s s g a d n n e i s t t % a n s l e e 5 u c r 2 m p re x it P e s
91-
y D h 9 I t V l 1 a O - e y D h C H I t V l c c a O i i e r r t t H C a a i i d d t t l l u u e e d d a a P A P A
% % % 0 5 0 2 5 - e d N g e F t a a I t l n u s e C m c M i r t e s B P P
%57
91-DIVOC-tsoP
cirtaideaP
noitalumits NFI eson ni erutangis
noisserpxe egarevA
I epyT NFI
)erocs-z wor(
ni noisserpxe tnediser lasan
0.2 0.1 0.0
sllec citirdned
93PN 14PN
23PN 61PN
5PP 73PN 53PN 44PN 31PN 1PP 9NA 2PP 63PN 61PP 11CP 83PN 81PN 31PP 3PP 42PN 8PP 11NA 82PN 91PN 03PN 11PA
02PN
01PA
9PP
cirtaideaP
tludA
%05 %52 %0
citirdned
lasan tnecreP gnisserpxe sllec selucelom NFI
III epyT
%01 %03
detalumits NFI era taht sCMBP fo egatnecreP
3> 2 1 0
3>
2
1 0
smotpmys fo tesno
ecnis
skeeW

noitalupop
c n
| eviaN |     | ix o o it |
| ----- | --- | --------- |
t o a lu
ty p o
C p
| epytonolC ytisrevid |     | de cixototyc dehcirnE |
| ------------------- | --- | --------------------- |
am lle e c
s alP c v i a u d noitalupop
n   B n i - NFI
|     | evian B llec amsalP noisnapxe lanolC |     |
| --- | ------------------------------------ | --- |
T
llec B 8 d e
| enummi evitpadA |              | D C c ud                                |
| --------------- | ------------ | --------------------------------------- |
|                 | evian T 8DC  |  /  T n                                 |
| esnopser        | yrotammalfnI | LT m e   4D i- N                        |
| evian dehcirnE  | llec telbog  | C   T  8 C F I sllec enummi decudni-NFI |
| noitalupop      |              | 8 D D cimetsys desaercnI                |
C C decud
lihportueN K
N i-NFId n
lihportueN
|               | llec lailehtipe | e t e c            |
| ------------- | --------------- | ------------------ |
|               | tisnarT         | y c o u d          |
| cirtaideaP    |                 | tl d n o n i -N    |
| doolb         |                 | u d o o M FI       |
|               | etyc htaed      | A l b              |
|               | + 6 o lleC      | cimetsyS d e c n o |
| enummi etannI | L I n o         | u d it a NFI       |
| esnopser      | m               | n i- lu p          |
N o p
FI
| NFI lacol regnortS | la c N | 9A/8A001S |
| ------------------ | ------ | --------- |
detavitcA e g o L F I etyconoM
| noitcudorp | ahporc                |      |
| ---------- | --------------------- | ---- |
| 2VoC-SRAS  | a K N                 |      |
| noitcefni  | m                     |      |
|            | ci llec citirdneD     | 2ECA |
|            | rt a y a tludA yawria |      |
id w r
|                 | e aP ia | 2VoC-SRAS   |
| --------------- | ------- | ----------- |
| sisatsoemoH     |         | e y t       |
| etannI ytinummi |         | v it p in u |
ad m
A m
i

1 Supplementary information
2
3
4
5
6
7 Local and systemic responses to SARS-CoV-2 infection in children and adults
8
9
10 Masahiro Yoshida, Kaylee B. Worlock, Ni Huang, Rik G.H. Lindeboom et al.
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33

34 Supplementary Information
35
36 Detailed Cell Type Annotation
37 The epithelial cell populations fall into two broad domains, one comprising ciliated cells and
38 a second covering the basal to secretory cell differentiation pathway, as visualised using
39 Velocyto (Fig. 1d). These include basal, cycling basal, secretory, goblet and squamous cells
40 (markers in Extended Data Fig. 2c). In addition, KHDRBS2 marked a distinct basal 1
41 population, whereas basal 2 cells are high in DAPL1 and NOTCH1. Secretory cells express
42 secretory proteins such as mucins and antimicrobial peptides and may be differentiation
43 intermediates giving rise to more differentiated club cells (SCGB1A1, SCGB3A1). GALNT4
44 marks a distinct secretory subtype. Goblet cells have high MUC5AC expression and were
45 subdivided into TFF1-hi goblet 1 and three distinct goblet 2 populations (BPIFA2, PLAU,
46 and goblet 2 inflammatory cells). Furthermore, we detect squamous cells (SPRR3, KRT78)
47 and identify three Hillock-like populations14,26,27, all marked by KRT14, KRT6A and KRT13
48 expression and referred to as Hillock, cycling Hillock and Hillock precursor cells, which
49 form a distinct differentiation trajectory (Fig. 1d) similar to the one reported in mouse27.
50 Within the ciliated cell domain, the differentiation trajectory points from ciliated 1 (PIFO,
51 OMG) to ciliated 2 (CFAP54, DZIP1L) cells. Between secretory and ciliated clusters, we
52 observe deuterosomal cells as intermediates marked by CDC20 and FOXN426,33 (Fig. 1b, d).
53 Additionally, we detect two novel cell populations that form a second bridge between the
54 secretory and ciliated clusters, which we named Transit epi 1 and 2. They co-express ciliated
55 cell markers (PIFO) and secretory genes (MUC2), but are FOXJ1 low. Distinguishing
56 markers for these two clusters are two long non-coding RNAs, FP671120.4 and FP236383.2
57 for both and HIST1H1E for Transit epi 2. Compared to previously described differentiation
58 intermediates from the nasopharynx14,28, transit epithelial cells express described marker
59 genes at relatively low levels, but do show similarities to IRC28, secretory-diff cells28 and
60 SERPINB11-hi secretory cell types14 (Extended Data Fig. 3b-d), although exact gene
61 expression signatures will depend on sampling method, location and clinical covariates. We
62 detect Transit epi 1 mostly in COVID-19 patients, but also in healthy children (Extended
63 Data Fig. 2a), suggesting a function in development and tissue regeneration (see below). We
64 also detect rare cell types such as ionocytes, brush cells, neuroendocrine cells, and
65 melanocytes, each expressing their canonical markers26,33,82,83.
66
67 Cell type abbreviations for airway and blood immune cells
68 Airway immune: Mac: macrophages, LC: Langerhans cells, Mono: monocytes, Neut:
69 neutrophils, DC: dendritic cells, cDC: conventional DC, pDC plasmacytoid DC, fDC:
70 follicular DC, T reg: T regulatory, T fh: follicular helper T cells, mem: memory, MAIT:
71 mucosal-associated invariant T cells, T gd: gamma-delta T cells, NK: natural killer cells,
72 ILC: innate lymphoid cells. B mem: memory B cells, IgK: immunoglobulin kappa, IgL:
73 immunoglobulin lambda.
74 Blood Immune: CTL: cytotoxic T lymphocyte, CM: central memory, EM: effector memory,
75 EMRA: effector memory re-expressing CD45RA, g/d: gamma-delta, reg: regulatory, MAIT:
76 mucosal-associated invariant T cells, NK: natural killer, NKT: natural killer T, ILC: innate
77 lymphoid cells, Mono: monocyte, pDC: plasmacytoid dendritic cells, cDC: conventional

78 dendritic cells, AS-DC: AXL+ SIGLEC6+ dendritic cells, n-sw mem: non-switched memory,
79 sw mem: switched memory, invar: invariant, HPC: haematopoietic progenitor cell, Baso/Eos:
80 basophil / eosinophil, RBC: red blood cell, IFN stim: interferon stimulated, Tem; T effector
81 memory.
82
83 IFN production in dendritic cells
84 To identify IFN producing cells that initiate the local and systemic immune response against
85 COVID-19, we ranked all donors by the percentage of IFN-stimulated cells in blood and
86 visualised their global IFN activation and IFN production signatures in nasal resident DCs
87 (Fig. 3h, expression of individual genes in all cell types in Extended Data Fig. 8a). We
88 observed that individuals with high numbers of IFN-stimulated cells in blood also had high
89 expression of IFN responsive genes in the nose, suggesting that this is where IFN production
90 first occurs. Strikingly, in nasal resident DCs of the highest ranked patient, we observed
91 strong IFN type I and type III production. Examining all cell types of this individual revealed
92 that both pDCs and cDCs, but not any of the other immune or epithelial cells, are producing
93 high amounts of multiple type I and type III molecules (Extended Data Fig. 8b). Notably,
94 this asymptomatic individual initially tested negative for SARS-CoV-2 by PCR, followed by
95 a positive test and subsequent sampling within four days, which was validated by the high
96 amount of SARS-CoV-2 reads (Fig. 1e). Therefore, sampling occurred at a very early stage
97 of infection, several days before most COVID-19 patients develop symptoms84. It is thus
98 likely that we captured the initiation of the immune response via IFN type I and type III
99 signaling at the site of infection. Together, this suggests a key role for nasal DCs as initiators
100 of the immune response against SARS-CoV-2 infection via IFN signaling, and underscores
101 the importance of temporal resolution when studying COVID-19.
102
103
104 Supplemental Note References:
105 82. Zak, F. G. & Lawson, W. The presence of melanocytes in the nasal cavity. Ann. Otol.
106 Rhinol. Laryngol. 83, 515–519 (1974).
107 83. Ewing, E. Malignant Melanoma Arising in Association with Sinonasal Melanosis: A
108 Case Report and Review of the Literature. Int J Pathol Clin Res 3, 058 (2017).
109 84. Tindale, L. C. et al. Evidence for transmission of COVID-19 prior to symptom onset.
110 Elife 9, (2020).
111

Total number of
cells in group 8220 Mean expression 6570 in group 4930 3290 1640 0 2
PP19-NB
PP18-NB
PP17-NB
PP16-NB
PP15-NB
PP13-NB
PP12-NB
PP11-NB v2.0
PP10-NB
PP9-NB
PP8-TB
PP8-NB
PP7-NB_v1.1
PP6-NB_2
PP6-NB_1
PP5-NB_2
PP5-NB_1
PC12-NB
PC11-NB
PC9-NB
PC6-NB
PC2-NB
NP47-NB
NP44-TB
NP44-NB_v1.1
NP44-NB_v1.0
NP43-NB
NP41-NB
NP39-TB
NP39-NB
NP38-TB
NP38-NB
NP37-TB
NP37-NB
NP36-TB
NP36-NB
NP35-TB
NP35-NB
NP32-NB
NP31-TB
NP31-NB
NP15-NB
NP14-TB
NP14-NB
NP13-NB
NP13-BB
NP12-NB
NP11-NB
NP10-NB
PP4-NB
AP4-NB
NP30-NB
PP3-NB
NP28-TB
NP28-NB
NP27-TB
NP27-NB
NP26-TB
NP26-NB
AP1-NB
PP2-NB
PP1-TB
PP1-NB
NP24-NB
NP23-TB
NP23-NB
NP22-TB
NP22-NB
NP21-TB
NP21-NB
NP20-TB
NP20-NB
NP19-NB
NP18-TB
NP18-NB
NP17-NB
NP16-NB
AP14-NB_2
AP14-NB_1
AP12-NB
AP11-NB
AP10-NB
AP9-NB
AP8-NB
AP7-NB
AP5-NB
AN14-NB
AN13-NB
AN12-NB
AN11-NB
AN9-NB
AN6-NB
AN5-NB
surivanoroc
detaler-SRAS
sucitylomeaharap
sulihpomeaH
sisneigniruht
sullicaB
sulihporeayrc
retcabocrA
asonigurea
sanomoduesP
01
surivamollipapahplA
ealeuzenev
secymotpertS
inujej
alletoverP
musotnemges
muiretcabenyroC
airotacisevue
sanomohtnaX
silatneiro
sanomoduesP
susicnoc
retcabolypmaC
snadivil
secymotpertS
snarovidixobrac
muidirtsolC
snegnirfrep
muidirtsolC
acotyxo
alleisbelK
iloc
aihcirehcsE
alocidihpa
arenhcuB
esnenitnegra
muidirtsolC
iisaalot
sanomoduesP
suerua
succocolyhpatS
suerec
sullicaB
3A97sI
.ps sanomosortiN
eaeadarah
ainiwrE
sutadidnaC
eliciffid
sedioidirtsolC
nahafsI
suriv suetorP
sisneolso
allexaroM
aidemretni
alletoverP
silaceaf
succocoretnE
iismreh
ailerroB
muiretagem
sullicaB
itoneuc
muiretcabattalB
murgip
mulunargisoloD
eainomuenp
alleisbelK
iinnamuab
retcabotenicA
iyvon
muidirtsolC
alocirecsiv
alleisenraB
musomar
muidirtsolcotalepisyrE
irolyp
retcabocileH
munilutob
muidirtsolC
mutaelcun
muiretcabosuF
sunaitenev
retcabotenicA
munairuetsap
muidirtsolC
silahrratac
allexaroM
Total number of Total number of SARS-CoV-2 Pediatric Healthy
cells in group expressing cells in group Adult Healthy 12620 7 1 6 0 2 1 0 20 Mean in e g x r p o r u e p ssion 2 3 6 6 5 5 0 0 e M x e p a re n s S s A io R n S in -C g o ro V u -2 p 1 2 5 2 6 1 0 2 2 0 0 0 5 6 1 5 6 0 50 0 2.5
PP19-NB
PP18-NB
PP17-NB
PP16-NB
PP15-NB
PP13-NB
PP12-NB
PP11-NB v2.0
PP10-NB
PP9-NB
PP8-TB
PP8-NB
PP7-NB_v1.1
PP6-NB_2
PP6-NB_1
PP5-NB_2
PP5-NB_1
PC12-NB
PC11-NB
PC9-NB
PC6-NB
PC2-NB
NP47-NB
NP44-TB
NP44-NB_v1.1
NP44-NB_v1.0
NP43-NB
NP41-NB
NP39-TB
NP39-NB
NP38-TB
NP38-NB
NP37-TB
NP37-NB
NP36-TB
NP36-NB
NP35-TB
NP35-NB
NP32-NB
NP31-TB
NP31-NB
NP15-NB
NP14-TB
NP14-NB
NP13-NB
NP13-BB
NP12-NB
NP11-NB
NP10-NB
PP4-NB
AP4-NB
NP30-NB
PP3-NB
NP28-TB
NP28-NB
NP27-TB
NP27-NB
NP26-TB
NP26-NB
AP1-NB
PP2-NB
PP1-TB
PP1-NB
NP24-NB
NP23-TB
NP23-NB
NP22-TB
NP22-NB
NP21-TB
NP21-NB
NP20-TB
NP20-NB
NP19-NB
NP18-TB
NP18-NB
NP17-NB
NP16-NB
AP14-NB_2
AP14-NB_1
AP12-NB
AP11-NB
AP10-NB
AP9-NB
AP8-NB
AP7-NB
AP5-NB
AN14-NB
AN13-NB
AN12-NB
AN11-NB
AN9-NB
AN6-NB
AN5-NB
aeahcrA airetcaB atoyrakuE sesuriV
a b
Pediatric COVID-19 Adult COVID-19 Pediatric Post-COVID-19 Adult Post-COVID-19
Extended Data Figure 9

| a   |              |              |              |                                                                           |                                                     |           | Type I                                                                 | Type III                                                  |
| --- | ------------ | ------------ | ------------ | ------------------------------------------------------------------------- | --------------------------------------------------- | --------- | ---------------------------------------------------------------------- | --------------------------------------------------------- |
|     | PP9          |              | PP9          |                                                                           |                                                     | PP9       |                                                                        |                                                           |
|     | AP10         |              | AP10         |                                                                           |                                                     | AP10      |                                                                        |                                                           |
|     | NP20         |              | NP20         |                                                                           |                                                     | NP20      |                                                                        |                                                           |
|     | AP11         |              | AP11         |                                                                           |                                                     | AP11      |                                                                        |                                                           |
|     | NP30 NP21    |              | NP30 NP21    |                                                                           |                                                     | NP30 NP21 |                                                                        |                                                           |
|     | AP8          |              | AP8          |                                                                           |                                                     | AP8       |                                                                        |                                                           |
|     | PP6          |              | PP6          |                                                                           |                                                     | PP6       |                                                                        |                                                           |
|     | NP19         |              | NP19         |                                                                           |                                                     | NP19      |                                                                        |                                                           |
|     | NP28         |              | NP28         |                                                                           |                                                     | NP28      |                                                                        |                                                           |
|     | AN11         |              | AN11         |                                                                           |                                                     | AN11      |                                                                        |                                                           |
|     | NP17         |              | NP17         |                                                                           |                                                     | NP17      |                                                                        |                                                           |
|     | PP15         |              | PP15         |                                                                           |                                                     | PP15      |                                                                        |                                                           |
|     | AP9          |              | AP9 PP8      |                                                                           |                                                     | PP8 AP9   |                                                                        |                                                           |
|     | NP24 PP8     |              | NP24         |                                                                           |                                                     | NP24      |                                                                        |                                                           |
|     | AN12         |              | AN12         |                                                                           |                                                     | AN12      |                                                                        |                                                           |
|     | AP12         |              | AP12         |                                                                           |                                                     | AP12      |                                                                        |                                                           |
|     | A N 6        |              | A N 6        |                                                                           |                                                     | AN6       |                                                                        |                                                           |
|     | P P 3        | Paediatric   | P P3         |                                                                           |                                                     | PP3       |                                                                        |                                                           |
|     | AN14         | Healthy      | AN14         |                                                                           |                                                     | AN14      |                                                                        |                                                           |
|     | PP13         |              | PP13         |                                                                           |                                                     | PP13      |                                                                        |                                                           |
|     | N P 1 8      | Adult        | N P 1 8      |                                                                           |                                                     | NP18      |                                                                        |                                                           |
|     | N PC11 P 3 8 | Healthy      | N PC11 P 3 8 |                                                                           |                                                     | NP38 PC11 |                                                                        |                                                           |
|     | PP16         |              | PP16         |                                                                           |                                                     | PP16      |                                                                        |                                                           |
|     | NP22         |              | NP22         |                                                                           |                                                     | NP22      |                                                                        |                                                           |
|     | N P 31       | Paediatric   | N P 31       |                                                                           |                                                     | NP31      |                                                                        |                                                           |
|     | P C 9        | COVID-19     | P C 9        |                                                                           |                                                     | PC9       |                                                                        |                                                           |
|     | NP36         |              | NP36         |                                                                           |                                                     | NP36      |                                                                        |                                                           |
|     | PC6          | Adult        | PC6          |                                                                           |                                                     | PC6       |                                                                        |                                                           |
|     | P P 2        | COVID-19     | P P 2        |                                                                           |                                                     | PP2       |                                                                        |                                                           |
|     | A P 5        |              | A P 5        |                                                                           |                                                     | AP5       |                                                                        |                                                           |
|     | PC2 AN9      |              | PC2 AN9      |                                                                           |                                                     | PC2 AN9   |                                                                        |                                                           |
|     | A N 5        | Paediatric   | A N 5        |                                                                           |                                                     | AN5       |                                                                        |                                                           |
|     | N P 23       | Convalescent | N P 23       |                                                                           |                                                     | NP23      |                                                                        |                                                           |
|     | PP1          |              | PP1          |                                                                           |                                                     | PP1       |                                                                        |                                                           |
|     | PP11         | Adult        | PP11         |                                                                           |                                                     | PP11      |                                                                        |                                                           |
|     | N P 2 6      | Convalescent | N P 2 6      |                                                                           |                                                     | NP26      |                                                                        |                                                           |
|     | N P 1 3      |              | N P 1 3      |                                                                           |                                                     | NP13      |                                                                        |                                                           |
|     | AP4          |              | AP4          |                                                                           |                                                     | AP4       |                                                                        |                                                           |
|     | NP27         |              | NP27 NP44    |                                                                           |                                                     | NP27 NP44 |                                                                        |                                                           |
|     | NP44 NP35    |              | NP35         |                                                                           |                                                     | NP35      |                                                                        |                                                           |
|     | NP37         |              | NP37         |                                                                           |                                                     | NP37      |                                                                        |                                                           |
|     | PP5          |              | PP5          |                                                                           |                                                     | PP5       |                                                                        |                                                           |
|     | NP16         |              | NP16         |                                                                           |                                                     | NP16      |                                                                        |                                                           |
|     | NP32         |              | NP32         |                                                                           |                                                     | NP32      |                                                                        |                                                           |
|     | NP41         |              | NP41         |                                                                           |                                                     | NP41      |                                                                        |                                                           |
|     | AP1          |              | AP1          |                                                                           |                                                     | AP1       |                                                                        |                                                           |
|     | AN13         |              | AN13         |                                                                           |                                                     | AN13      |                                                                        |                                                           |
|     | NP39 PP4     |              | NP39 PP4     |                                                                           |                                                     | NP39 PP4  |                                                                        |                                                           |
|     | NP15         |              | NP15         |                                                                           |                                                     | NP15      |                                                                        |                                                           |
|     | 0 10 20      | 30 40 50     | 2TSB 2KPMC   | 2KA2FIE 1ITSPE 5CREH 53IFI L44IFI 6IFI 3TIFI 51GSI E6YL 1XM 2XM 1SAO 2SAO | 9PRAP 1RCSLP 9DMAS L9DMAS 011PS 1TATS 22MIRT 6L2EBU | 1FAX 7FRI | 1BNFI 1WNFI 12ANFI 4ANFI 7ANFI 01ANFI 61ANFI 71ANFI 41ANFI 5ANFI 6ANFI | 31ANFI 2ANFI 8ANFI 1ANFI ENFI KNFI GNFI 3LNFI 2LNFI 1LNFI |
Percentage of PBMCs
that are IFN stimulated
|     |     |     |     | Interferon stimulated genes |     |     | Interferons |                    |
| --- | --- | --- | --- | --------------------------- | --- | --- | ----------- | ------------------ |
|     |     |     |     | Percent Average expression  |     |     | Percent     | Average expression |
|     |     |     |     | expressed in nasal cells    |     |     | expressed   | in nasal cells     |
|     |     |     |     | 0 (column  z-score)         |     |     | 0.0         | (column  z-score)  |
|     |     |     |     | 25                          |     |     | 0.5         |                    |
|     |     |     |     | 50 -1 0                     | 1 2 |     | 1.0         | -1 0 1 2           |
|     |     |     |     | 75                          |     |     | 1.5         |                    |
b
|     |     |     |     | Type I | Type II Type III |     |     |     |
| --- | --- | --- | --- | ------ | ---------------- | --- | --- | --- |
Basal 1 KHDRBS2+ (N=1)
T CD4 CCR4+ (N=1)
Melanocyte (N=2)
Transit epi 2 (N=3)
B naive (N=8)
Neuroendocrine (N=11)
B mem exhausted (N=2)
Goblet 2 BPIFA2+ (N=2)
Squamous (N=3)
Ciliated 2 (N=7)
ILC (N=2)
doolb ni sllec detalumits NFI fo noitroporp Hillock precursor (N=1)
| tsehgih htiw laudividni fo sllec lasaN |     | T gd (N=3) |     |     |     |     |     |     |
| -------------------------------------- | --- | ---------- | --- | --- | --- | --- | --- | --- |
Basal 1 (N=7)
Duct (N=2)
|     |                      | B a s a l  2   ( N = 3 1                | )   |     |     | A v e r a g      | e     |     |
| --- | -------------------- | --------------------------------------- | --- | --- | --- | ---------------- | ----- | --- |
|     |                      | H i ll o M c k a   c (   N (N = = 1 1 8 | ) ) |     |     | ex p r e s       | s ion |     |
|     | cDC activated (N=29) |                                         |     |     |     | (column z-score) |       |     |
|     | Cycling basal (N=47) |                                         |     |     |     | 2.5              |       |     |
T cycling (N=20)
|     |     | T naive (N=7) |     |     |     | 2.0 |     |     |
| --- | --- | ------------- | --- | --- | --- | --- | --- | --- |
Goblet 1 (N=20)
|     |                  | LC (N=14)                    |     |     |     | 1.5 |     |     |
| --- | ---------------- | ---------------------------- | --- | --- | --- | --- | --- | --- |
|     | T CD             | 8   m e m   3   ( N = 4 4    | )   |     |     |     |     |     |
|     |                  | C i l iat e d  1   ( N = 9 6 | )   |     |     | 1.0 |     |     |
|     | Goblet 2         |  P L A U +   ( N = 1 2 2     | )   |     |     | 0.5 |     |     |
|     |                  | S e cr e to r y   (N = 3 4   | )   |     |     |     |     |     |
|     | NK cd56lo (N=44) |                              |     |     |     | 0.0 |     |     |
Neut (N=43)
Secretory GALNT4+ (N=29)
Cycling hillock (N=27)
|     | NK cd56hi (N=300)   |             |     |     |     | Percent   |     |     |
| --- | ------------------- | ----------- | --- | --- | --- | --------- | --- | --- |
|     | Deuterosomal (N=31) | pDC (N=119) |     |     |     | expressed |     |     |
T reg (N=35)
|     | Mono CXCL10+ (N=1056) |                             |     |     |     |     | 0   |     |
| --- | --------------------- | --------------------------- | --- | --- | --- | --- | --- | --- |
|     | M a c  a              | c tiv a t e d   ( N = 1 2 8 | )   |     |     |     |     |     |
|     | Goblet 2  in f la m   | m a t o r y   ( N = 8 5 6   | )   |     |     |     | 10  |     |
|     | M o                   | n o  I L 6 +   ( N = 1 5 9  | )   |     |     |     |     |     |
|     | Mono  G P             | B A R 1 +   ( N = 1 7 0     | )   |     |     |     | 20  |     |
Ionocyte (N=130)
30
40
HPC (N=1)
| doolb ni sllec detalumits NFI fo noitroporp | T CD8 EMRA (N=1) | Platelets (N=1) |     |     |     |     | 50  |     |
| ------------------------------------------- | ---------------- | --------------- | --- | --- | --- | --- | --- | --- |
T CD8 CTL IFN stim (N=1)
| tsehgih htiw laudividni fo sCMBP |     | ILC (N=3) |     |     |     |     |     |     |
| -------------------------------- | --- | --------- | --- | --- | --- | --- | --- | --- |
pDC (N=2)
B n-sw mem (N=3)
T reg (N=19)
Monocyte CD14 IFN stim (N=12)
NK CD56 (N=23)
B naive IFN stim (N=31)
T CD8 CTL (N=6)
T CD8 naive (N=106)
B naive (N=12)
NK IFN stim (N=27)
T CD4 naive (N=139)
B n-sw mem IFN stim (N=3)
NK (N=31)
T CD8 CM (N=33)
T CD4 naive IFN stim (N=425) T CD4 helper (N=49)
Cycling (N=89)
|     |     |     | 1BNFI 1WNFI 12ANFI 4ANFI | 7ANFI 01ANFI 61ANFI 71ANFI 41ANFI 5ANFI 6ANFI 31ANFI 2ANFI 8ANFI 1ANFI ENFI KNFI | GNFI 3LNFI 2LNFI | 1LNFI |     |     |
| --- | --- | --- | ------------------------ | -------------------------------------------------------------------------------- | ---------------- | ----- | --- | --- |
Extended Data Figure 8

| a   | b   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
secneuqes RCB deifitnedi lla 1.0
/ secneuqes RCB euqinu # 222222222333333 1T CD4 naive (N=77,439) 1155ILC (N=405) 2299Plasmablasts (N=208)
38
.75 39111111111199999999999999999999999999999999999999 2T CD4 helper (N=37,922) 1166Mono CD14 (N=47,520) 3300HPC (N=938)
|     |     |     | 21  | 1111111118888888888888888 1111111111111111177777777777777777777 1111116666666666 | 3T CD4 CTL (N=5,294) | 1177Mono CD14 IL6 (N=768) |     | 331Baso/Eos (N=25) |     |
| --- | --- | --- | --- | -------------------------------------------------------------------------------- | -------------------- | ------------------------- | --- | ------------------ | --- |
200
.50 2 PAMU TDA-ANR NNW 42 4T CD8 naive (N=33,590) 1188Mono CD16 (N=8,342) 3322Cycling (N=3,593)
|     |     |     | 31 30 | 334 | 5 T   C D 8  C M   ( | N = 1 2 , 8 3 0) 11 99 M o | no   C D 1 6 + C 1 (N=1,173)33 | 33 P l a te l e ts   (N = 1,784) |     |
| --- | --- | --- | ----- | --- | -------------------- | -------------------------- | ------------------------------ | -------------------------------- | --- |
|     |     |     | 28    | 37  | T  C D 8   EM   (    | N = 2 , 4 8 6 ) pD C       |  ( N = 1 ,2 4 5 )              | R B C   ( N = 3 85 )             |     |
.25 6 22 00 33 44
|     |     |                | 29    | 11111111444444444444444444444444 11111111111133333333333333 111111111111111222222222222222222 | 7 T   C D8   E M RRR | A  ( N = 6 ,4 4 3 ) 22 1 A S -D | C  (N = 5 9) | 35T CD4 naive IFN stim (N=8,134) |     |
| --- | --- | -------------- | ----- | --------------------------------------------------------------------------------------------- | -------------------- | ------------------------------- | ------------ | -------------------------------- | --- |
|     |     | 25555555555555 | 22226 | 1555 777777777777777777                                                                       | 8 T  C D 8   C TL  ( | N = 3 6 ,2 1 7 ) 22 22 cD C     | 1  (N =6 1 ) | 36T CD8 CTL IFN stim (N=134)     |     |
.00 4 1222222222222222222222222222222222227777777777777777777 36
etanoeN tnafnI dlihc gnuoY dlihC tnecselodA tludA ylredlE 4 0 99999999999999999 888888888 3 9T g/d (N=5,144) 2233cDC2 (N=2,963) 37NK IFN stim (N=1,211)
|                       |         | 2222222222224444444444444444 |     |                                                 | 1100Treg (N=8,567)    | 2244B naive (N=40,193)     |     | 38Mono CD14 IFN stim (N=7,124) |     |
| --------------------- | ------- | ---------------------------- | --- | ----------------------------------------------- | --------------------- | -------------------------- | --- | ------------------------------ | --- |
|                       |         |                              |     | 55555555555                                     | 111MAIT (N=3,961)     | 2255B n-sw mem (N=5,574)   |     | 39Mono CD16 IFN stim (N=1,167) |     |
|                       |         |                              |     | 4444 111111111111111111111111111111111111 33333 | 333333333322222       |                            |     |                                |     |
|                       |         |                              |     | 66666666666666666666666666                      | 1122NKKKT (N=687)     | 2266B sw mem (N=4,060)     |     | 40B naive IFN stim (N=2,019)   |     |
|                       |         |                              |     | 35 22222222222                                  | 1133NK (N=43,630)     | 2277B invar (N=1,944)      |     | 41B n-sw mem IFN stim (N=680)  |     |
| Convalescent COVID-19 | Healthy |                              |     | 1111111111                                      |                       |                            |     |                                |     |
|                       |         |                              |     | 1111111111100000000                             | 1144NK CD56 (N=4,723) | 2288Plasma cells (N=1,557) |     | 42HPC IFN stim (N=21)          |     |
WNN RNA-ADT UMAP 1
| c   |     |     | d   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
50% Adult Paediatric Correlations between circulating to nasal cell proportions in COVID-19+ children
ILC
| sCMBP fo egatnecreP detalumits NFI era taht |     |     |     | RBC |     |     |     |     |     |
| ------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Platelets
NK
NKT
| 25% |     |     | T CD8 EMRA |     |     |     |     |     |     |
| --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- |
B naive
B sw mem
B n-sw mem
T CD4 CTL
MAIT
| 0%  |     |     |     | T g/d |     |     |     |     |     |
| --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- |
noitalupop llec enummi gnitalucriC Monocyte CD14 Spearman’s rank
| 0 1 2 | >3 citamotpmysA 0 1 2 | >3  |               | cDC2 |     |     |     |     | correlation |
| ----- | --------------------- | --- | ------------- | ---- | --- | --- | --- | --- | ----------- |
|       |                       |     | Monocyte CD16 |      |     |     |     |     | coefficient |
B invar
Plasmablasts
|     |     |     | Plasma cells |     |     |     |     |     | -1 0 1 |
| --- | --- | --- | ------------ | --- | --- | --- | --- | --- | ------ |
T CD8 EM
T CD8 CM
HPC
NK CD56
cDC1
T CD8 naive
|     |     |     | T CD4 naive  |     |     |     |     |     | P value of  |
| --- | --- | --- | ------------ | --- | --- | --- | --- | --- | ----------- |
|     |     |     | T CD4 helper |     |     |     |     |     | correlation |
Baso/Eos Baso/Eos
|     |     |     |           | T reg |     |     |     |     | <0.001 |
| --- | --- | --- | --------- | ----- | --- | --- | --- | --- | ------ |
|     |     |     | T CD8 CTL |       |     |     |     |     | 0.01   |
Monocyte CD16 IFN stim
|     |     |     | Monocyte CD16+C1 |       |     |     |     |     | 0.1 |
| --- | --- | --- | ---------------- | ----- | --- | --- | --- | --- | --- |
|     |     |     |                  | AS-DC |     |     |     |     | 0.5 |
pDC
HPC IFN stim
Monocyte CD14 IFN stim
Monocyte CD14 IL6
Cycling
B n-sw mem IFN stim
NK IFN stim
T CD4 naive IFN stim
B naive IFN stim
T CD8 CTL IFN stim
|     |     |     |     | TKN ol65dc KN +6LI onoM 3 mem 8DC T gnilcyc T detavitca CDc CDp llec +2-VoC-SRAS | TIAM caM ih65dc KN ger T detavitca caM 2 mem 8DC T 1 mem 8DC T dg T evian T mem 4DC T hf T KgI amsalP | LgI amsalP detsuahxe 8DC T mem B evian B detsuahxe mem B CLI tueN tsaM CDf detavitca mem B gnilcyc B +1RABPG onoM | +4RCC 4DC T CL +01LCXC onoM tcuD etyconoI etyconaleM yrotammalfni 2 telboG | llec +2-VoC-SRAS 1 ipe tisnarT 1 telboG 1 detailiC rosrucerp kcolliH kcollih gnilcyC kcolliH 1 lasaB +2SBRDHK 1 lasaB 2 lasaB +4TNLAG yroterceS yroterceS suomauqS hsurB +2AFIPB 2 telboG +UALP 2 telboG 2 ipe tisnarT 2 detailiC bulC lamosoretueD lasab gnilcyC enircodneorueN |     |
| --- | --- | --- | --- | -------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- |
|     |     |     |     |                                                                                  | Nasal resident immune cell population                                                                 |                                                                                                                   |                                                                            | Nasal epithelial cell population                                                                                                                                                                                                                                                 |     |
e
Correlations between circulating to nasal cell proportions in COVID-19+ adults
ILC
RBC
Platelets
NK
NKT
T CD8 EMRA
B naive
B sw mem
B n-sw mem
T CD4 CTL
MAIT
|     |     |     |     | T g/d |     |     |     |     | Spearman’s rank |
| --- | --- | --- | --- | ----- | --- | --- | --- | --- | --------------- |
noitalupop llec enummi gnitalucriC Monocyte CD14
|     |     |     |               | cDC2 |     |     |     |     | correlation |
| --- | --- | --- | ------------- | ---- | --- | --- | --- | --- | ----------- |
|     |     |     | Monocyte CD16 |      |     |     |     |     | coefficient |
B invar
|     |     |     | Plasmablasts |     |     |     |     |     | -1 0 1 |
| --- | --- | --- | ------------ | --- | --- | --- | --- | --- | ------ |
Plasma cells
T CD8 EM
T CD8 CM
HPC
NK CD56
cDC1
T CD8 naive
|     |     |     | T CD4 naive  |     |     |     |     |     | P value of  |
| --- | --- | --- | ------------ | --- | --- | --- | --- | --- | ----------- |
|     |     |     | T CD4 helper |     |     |     |     |     | correlation |
Baso/Eos
|     |     |                        |           | T reg |     |     |     |     | <0.001 |
| --- | --- | ---------------------- | --------- | ----- | --- | --- | --- | --- | ------ |
|     |     |                        | T CD8 CTL |       |     |     |     |     | 0.01   |
|     |     | Monocyte CD16 IFN stim |           |       |     |     |     |     | 0.1    |
Monocyte CD16+C1
|     |     |     |     | AS-DC |     |     |     |     | 0.5 |
| --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- |
pDC
HPC IFN stim
Monocyte CD14 IFN stim
Monocyte CD14 IL6
Cycling
B n-sw mem IFN stim
NK IFN stim
T CD4 naive IFN stim
B naive IFN stim
T CD8 CTL IFN stim
|     |     |     |     | TKN ol65dc KN +6LI onoM 3 mem 8DC T gnilcyc T detavitca CDc CDp llec +2-VoC-SRAS | TIAM caM ih65dc KN ger T detavitca caM 2 mem 8DC T 1 mem 8DC T dg T evian T mem 4DC T hf T KgI amsalP | LgI amsalP detsuahxe 8DC T mem B evian B detsuahxe mem B CLI tueN tsaM CDf detavitca mem B gnilcyc B +1RABPG onoM +4RCC 4DC T | CL +01LCXC onoM tcuD etyconoI etyconaleM yrotammalfni 2 telboG | llec +2-VoC-SRAS 1 ipe tisnarT 1 telboG 1 detailiC rosrucerp kcolliH kcollih gnilcyC kcolliH 1 lasaB +2SBRDHK 1 lasaB 2 lasaB +4TNLAG yroterceS yroterceS suomauqS hsurB +2AFIPB 2 telboG +UALP 2 telboG 2 ipe tisnarT 2 detailiC bulC lamosoretueD lasab gnilcyC enircodneorueN |     |
| --- | --- | --- | --- | -------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- |
|     |     |     |     |                                                                                  | Nasal resident immune cell population                                                                 |                                                                                                                               |                                                                | Nasal epithelial cell population                                                                                                                                                                                                                                                 |     |
Extended Data Figure 7

a T CD4 naive
T CD4 helper
T CD4 CTL
T CD8 naive
T CD8 CM
T CD8 EM
T CD8 EMRA
T CD8 CTL
T g/d
T reg
MAIT
NKT
NK
NK CD56
ILC
Monocyte CD14
Monocyte CD14 IL6
Monocyte CD16
Monocyte CD16+C1
pDC
AS-DC
cDC1
cDC2
B naive
B n-sw mem
B sw mem
B invar
Plasma cells
Plasmablasts
HPC
Baso/Eos
Cycling
Platelets
RBC
T CD4 naive IFN stim
T CD8 CTL IFN stim
NK IFN stim
Monocyte CD14 IFN stim
Monocyte CD16 IFN stim
B naive IFN stim
B n-sw mem IFN stim
HPC IFN stim
D3DC 4DC A8DC 7RCC 72DC LLES 1RC3XC R7LI HMZG 1FRP 9VGRT 2VDRT 3PXOF AR2LI 7VART 2-1VART 01A4CLS 1RCN 1MACN YLNG 81FSRFNT 4FSRFNT G1RECF 41DC A3RGCF 6LI AQ1C C4CELC AR3LI LXA 6CELGIS A9CELC A1RECF 2RECF DHGI 91DC 42DC A1LCT MHGI A97DC 1A4SM B31FSRFNT 2RC 1KNAB NIAHCJ 1GHGI 12XBT 5LRCF 3LRCF 1DPTNE TIK 43DC 2KNIPS 1BASPT 2BSPT 2GRP XPE 76IKM PBPP 4FP BBH 2TSB 2KPMC 2KA2FIE 1ITSPE 5CREH 53IFI L44IFI 6IFI 3TIFI 51GSI E6YL 1XM 2XM 1SAO 2SAO 9PRAP 1RCSLP 9DMAS L9DMAS 011PS 1TATS 22MIRT 6L2EBU 1FAX 7FRI
|     | Average RNA expression |                  | Percent expressed |     |     |     |     |
| --- | ---------------------- | ---------------- | ----------------- | --- | --- | --- | --- |
|     |                        | (column z-score) | 0                 |     |     |     |     |
25
50
|     | 0.00.51.01.52.02.5 |     | 75  |     |     |     |     |
| --- | ------------------ | --- | --- | --- | --- | --- | --- |
100
| b                 |               |     |     |                              | c   |     |                               |
| ----------------- | ------------- | --- | --- | ---------------------------- | --- | --- | ----------------------------- |
|                   | T CD4 naive   |     |     |                              |     |     | RBC Platelets                 |
|                   | T CD4 helper  |     |     |                              |     |     | Cycling                       |
|                   | T CD4 CTL     |     |     |                              |     |     | Baso/Eos                      |
|                   | T CD8 naive   |     |     |                              |     |     | HPC                           |
|                   | T CD8 CM      |     |     |                              |     |     | Plasmablasts                  |
|                   | T CD8 EM      |     |     |                              |     |     | Plasma cells                  |
|                   | T CD8 EMRA    |     |     |                              |     |     | B invar                       |
|                   | T CD8 CTL     |     |     |                              |     |     | B sw mem                      |
|                   | T g/d         |     |     |                              |     |     | B n-sw mem B naive            |
|                   | T reg         |     |     | Percent                      |     |     | cDC2                          |
|                   | MAIT          |     |     |                              |     |     | c D C 1                       |
|                   | NKT           |     |     | expressed                    |     |     | A S -D C                      |
|                   | NK            |     |     | 0                            |     |     | pDC                           |
|                   | NK CD56       |     |     |                              |     |     | Monocyte CD16+C1              |
|                   | ILC           |     |     | 25                           |     |     | M o n o c y t e   C D 1 6     |
|                   | Monocyte CD14 |     |     |                              |     |     | Mo n o c y t e   C D 1 4  IL6 |
| Monocyte CD14 IL6 |               |     |     | 50                           |     |     | M IL o C nocyte CD14          |
|                   | Monocyte CD16 |     |     |                              |     |     | NK CD56                       |
| Monocyte CD16+C1  |               |     |     | 75                           |     |     | NK                            |
|                   | pDC           |     |     |                              |     |     | NKT                           |
|                   | AS-DC         |     |     | A v e r a g e   p r o t e in |     |     | M A I T                       |
|                   | cDC1          |     |     | e x p r e s s i o n          |     |     | T   r e g                     |
|                   | cDC2          |     |     | (c o lu m n   z - s c o r e) |     |     | T   g / d                     |
|                   | B naive       |     |     | 2.5                          |     |     | T   C D 8 CTL                 |
|                   | B n-sw mem    |     |     |                              |     |     | T CD8 EMRA T CD8 EM           |
|                   | B sw mem      |     |     | 2.0                          |     |     | T CD8 CM                      |
|                   | B invar       |     |     |                              |     |     | T CD8 naive                   |
|                   | Plasma cells  |     |     | 1.5                          |     |     | T   C D 4   C T L             |
|                   | Plasmablasts  |     |     |                              |     |     | T   C D 4   he l per          |
|                   | HPC           |     |     | 1.0                          |     |     | T CD4 naive                   |
Baso/Eos htyrE teletalP gnitarefilorP 4DC gnitarefilorP KN CPSH tsalbamsalP yromem B etaidemretni B evian B 2CDc 1CDc CDSA CDp onoM 61DC onoM 41DC CLI thgirb65DC_KN KN TIAM gerT Tdg Tnd MET 8DC MCT 8DC eviaN 8DC LTC 4DC MET 4DC MCT 4DC eviaN 4DC
|                      | Cycling   |     |     | 0.5 |     |     | Percentage  |
| -------------------- | --------- | --- | --- | --- | --- | --- | ----------- |
|                      | Platelets |     |     |     |     |     | overlap (%) |
|                      | RBC       |     |     | 0.0 |     |     |             |
| T CD4 naive IFN stim |           |     |     |     |     |     | 100         |
T CD8 CTL IFN stim
|     | NK IFN stim |     |     |     |     |     | 50  |
| --- | ----------- | --- | --- | --- | --- | --- | --- |
Monocyte CD14 IFN stim
| Monocyte CD16 IFN stim |     |     |     |     |     |     | 0   |
| ---------------------- | --- | --- | --- | --- | --- | --- | --- |
| B naive IFN stim       |     |     |     | d   |     |     |     |
B n-sw mem IFN stim Paediatric:COVID-19 Paediatric:Healthy Local true
|     | HPC IFN stim |     |     | Paediatric:Post-COVID-19 |     |     | sign rate |
| --- | ------------ | --- | --- | ------------------------ | --- | --- | --------- |
>0.9999
D3DC 4DC A8DC 7RCC 72DC LLES 1RC3XC R7LI AR54DC OR54DC 9VGRT 2VDRT AR2LI 7VART 1RCN 1MACN 81FSRFNT 41DC A3RGCF C4CELC AR3LI A9CELC A1RECF 2RECF DHGI 91DC MHGI 1A4SM B31FSRFNT 2RC 5LRCF 1DPTNE TIK 43DC Adult:COVID-19 Adult:Healthy 0.999
|     |     |     |     | Adult:Post-COVID-19 |     |     | 0.99 |
| --- | --- | --- | --- | ------------------- | --- | --- | ---- |
0.9 0.5
Neonate Infant
|     |     |     |     |     | Y o u n g   c h i l d    |     | F o ld   |
| --- | --- | --- | --- | --- | ------------------------ | --- | -------- |
|     |     |     |     |     | C h i l d                |     | ch a nge |
| e   |     |     |     |     | A d o le s Adult c e n t |     | >3       |
Elderly
Residual variance LTC 4DC T ME 8DC T LTC 8DC T ARME 8DC T ravni B mem ws B TIAM d/g T mem ws-n B evian B evian 8DC T evian 4DC T CBR 6LI 41DC onoM soE/osaB CPH gnilcyC 1C+61DC onoM MC 8DC T repleh 4DC T ger T CD-SA CLI 65DC KN KN TKN steletalP 41DC onoM 61DC onoM 1CDc CDp 2CDc stsalbamsalP sllec amsalP 1
Patient ID
|     | Age group |     |     |     |     |     | <1/3 |
| --- | --------- | --- | --- | --- | --- | --- | ---- |
Paediatric/Adult:COVID status
Ethnicity
Sex
|     |     |             |             |     | f   | Average cell type proportion |             |
| --- | --- | ----------- | ----------- | --- | --- | ---------------------------- | ----------- |
|     |     | 0.0 0.5 1.0 | 1.5 2.0 2.5 |     |     | 00. 52.                      | 05. 57. 0.1 |
Square root of explained variation
Paediatric - Healthy (N=24, K=126,691)
Paediatric - COVID-19 (N=12, K=64,057)
Paediatric - Post-COVID-19 (N=2, K=10,580)
| g   |     |     |     |     | Adult - Healthy (N=11, K=46,993) |     |     |
| --- | --- | --- | --- | --- | -------------------------------- | --- | --- |
Adult - COVID-19 (N=12, K=87,183)
Adult - Post-COVID-19 (N=18, K=86,644)
Neonate (N=46,499)
Infant (N=49,034)
Healthy (N=173,684) Young child (N=37,741) mits NFI CPH mits NFI mem ws-n B mits NFI evian B mits NFI 61DC etyconoM mits NFI 41DC etyconoM mits NFI KN mits NFI LTC 8DC T mits NFI evian 4DC T CBR steletalP gnilcyC soE/osaB CPH stsalbamsalP sllec amsalP ravni B mem ws B mem ws-n B evian B 2CDc 1CDc CD-SA CDp 1C+61DC etyconoM 61DC etyconoM 6LI 41DC etyconoM 41DC etyconoM CLI 65DC KN KN TKN TIAM ger T d/g T LTC 8DC T ARME 8DC T ME 8DC T MC 8DC T evian 8DC T LTC 4DC T repleh 4DC T evian 4DC T
COVID-19 (N=151,312)
Child (N=36,287)
|     |     | Post-COVID-19 (N=97,224) |     | Adolescent (N=31,839) |     |     |     |
| --- | --- | ------------------------ | --- | --------------------- | --- | --- | --- |
Adult (N=99,524)
Elderly (N=121,296)
Extended Data Figure 6

a b Nasal epithelial cells
100
COVID-19_status Age
80
Neonate
Infant 60
Young child COVID-19
Healthy Child Adolescent
Post-COVID-19 40
Adult
Elderly
20
0
c
Extended Data Figure 2
yhtlaeH,tludA )61351=k
,7=N(
91-DIVOC,tludA )06663=k
,01=N(
91-DIVOC-tsoP,tludA )8305=k
,3=N(
yhtlaeH,deP )62617=k
,03=N(
91-DIVOC,deP )06663=k
,81=N(
91-DIVOC-tsoP,deP )5453=k
,2=N(
Basal 1
Basal 1 KHDRBS2+
Basal 2
Cycling basal
Hillock precursor
Cycling hillock
Hillock
Squamous
Secretory
Secretory GALNT4+ Duct
Club
Goblet 1
Goblet 2 BPIFA2+
Goblet 2 PLAU+
Goblet 2 inflammatory
Transit epi 1
Transit epi 2
Deuterosomal
Ciliated 1
Ciliated 2
Ionocyte
Brush
Neuroendocrine
Melanocyte
2KLD 51TRK 2SBRDHK 1LPAD 1HCTON 76IKM 1PASUN 41TRK A6TRK 31TRK 87TRK 3RRPS 2SON 31NPAC 4TNLAG AIM 1SERRAR 1A3BGCS 1A1BGCS CA5CUM 1FFT 2AFIPB UALP 01LCXC 4.021176PF 2.383632PF E1H1TSIH 4NXOF B02CDC OFIP GMO 45PAFC 04CDCC 1IXOF 3LCSA XMB 31SGR 1XEB N1KSCP LEMP ANALM 01LCXC 1SAO 1TIFI 3TIFI
Basal 1
Basal 1 KHDRBS2+
Basal 2
Cycling basal
Hillock precursor
Cycling hillock
Hillock
Squamous
Secretory
Secretory GALNT4+
Duct
Club
Goblet 1
Goblet 2 BPIFA2+
Goblet 2 PLAU+
Goblet 2 inflammatory
Transit epi 1
Transit epi 2
Mean expression
Deuterosomal in group
Ciliated 1
Ciliated 2 0.5 1.0
Ionocyte
Brush Fraction of cells
Neuroendocrine in group (%)
Melanocyte
1020304050
D3DC 7RCC 1FEL 4DC 3PXOF 4ALTC 4RCC B4DMRF GL04DC A8DC 1NBD BLEH KMZG SEMOE 2VGRT 1VDRT YLNG 1MACN 12XBT 1FRLK 18TRK 9HDCP 1A4SM 2RECF 1A91LOC 72DC 5LRCF 4LRCF 3LRCF 1KMAC 76IKM 2MCM FPHC 1GHGI CKGI 2CLGI AQ1C OCRAM SDS 1ESANR 702DC C1DC 41DC 01LCXC NACV 1RABPG 6LI B3RGCF 2KORP 3PMAL 3A4RN C4CELC 4ARLIL PSCDF 2RC 2BSPT 2A4SM 01LCXC 1SAO 1TIFI 3TIFI
Mean expression
in group
0.250.500.751.00
Fraction of cells in group (%)
1020304050
sllec
lailehtipe
yawriA
sllec
enummi
yawriA
T naive
T reg
T fh
T CD4 CCR4+
T CD4 mem
MAIT
T cycling
T CD8 mem 1
T CD8 mem 2
T CD8 mem 3
T CD8 exhausted
T gd
NKT
NK cd56hi
NK cd56lo
ILC
B naive
B mem
B mem exhausted
B mem activated
B cycling
Plasma IgK
Plasma IgL
Mac
Mac activated
LC
Mono CXCL10+
Mono GPBAR1+
Mono IL6+
Neut
cDC activated
pDC
fDC Mast

a
Healthy cohort
|          |     | Neonate                                                                               | InfantYoung Child | Child | Adolescent |     | Adult |
| -------- | --- | ------------------------------------------------------------------------------------- | ----------------- | ----- | ---------- | --- | ----- |
| Patient  |     | 6                6                8                      5                          5 |                   |       |            |     | 11    |
Sample
|                          | Nasal brush | 6                6                8                      5                          5 |     |     |     |     |   7 |
| ------------------------ | ----------- | ------------------------------------------------------------------------------------- | --- | --- | --- | --- | --- |
| Tracheal/bronchial brush |             | 2                5                3                      3                          4 |     |     |     |     | 0   |
|                          |    Blood    |                                                                                       |     |     |     |     |  11 |
3                4                7                      5                          5
| Age group |     | Neonate | Infant Young Child | Child | Adolescent |         | Adult       |
| --------- | --- | ------- | ------------------ | ----- | ---------- | ------- | ----------- |
|           |     | 0 30d   | 1y 2y              | 6y    | 12y        | 18y 30y | 50y 70y 90y |
COVID-19 cohort
|          |     | Neonate                                                                               | InfantYoung Child | Child | Adolescent |     | Adult |
| -------- | --- | ------------------------------------------------------------------------------------- | ----------------- | ----- | ---------- | --- | ----- |
| Patient  |     | 6                3                1                      1                          8 |                   |       |            |     | 18    |
Sample
|     | Nasal brush | 5                3                1                      1                          8 |     |     |     |     | 10  |
| --- | ----------- | ------------------------------------------------------------------------------------- | --- | --- | --- | --- | --- |
Tracheal/bronchial brush 0                1                0                      0                          1 4 Bronchial brush
|     |    Blood | 5                3                0                      1                          4 |     |     |     |     | 12  |
| --- | -------- | ------------------------------------------------------------------------------------- | --- | --- | --- | --- | --- |
Tracheal brush
COVID-19Severe
severity  Nasal brush
Moderate
Blood
Mild/Asymptomatic
| Age group |     | Neonate | Infant Young Child | Child | Adolescent |         | Adult       |
| --------- | --- | ------- | ------------------ | ----- | ---------- | ------- | ----------- |
|           |     | 0 30d   | 1y 2y              | 6y    | 12y        | 18y 30y | 50y 70y 90y |
Post-COVID-19 cohort
|         |     | Neonate                                                                               | InfantYoung Child | Child | Adolescent |     | Adult |
| ------- | --- | ------------------------------------------------------------------------------------- | ----------------- | ----- | ---------- | --- | ----- |
| Patient |     | 0                1                0                      1                          0 |                   |       |            |     | 13    |
Sample
|                          | Nasal brush | 0                1                0                      1                          0 |     |     |     |     | 3   |
| ------------------------ | ----------- | ------------------------------------------------------------------------------------- | --- | --- | --- | --- | --- |
| Tracheal/bronchial brush |             | 0                0                0                      0                          0 |     |     |     |     | 0   |
|                          |    Blood    | 0                1                0                      1                          0 |     |     |     |     | 12  |
COVID-19 Severe
severity
Moderate
Mild/Asymptomatic
| Age group |     | Neonate | Infant Young Child | Child | Adolescent |         | Adult       |
| --------- | --- | ------- | ------------------ | ----- | ---------- | ------- | ----------- |
|           |     | 0 30d   | 1y 2y              | 6y    | 12y        | 18y 30y | 50y 70y 90y |
SARS-CoV2 PCR(+)
| b   |     |        |        |      | (days from COVID-19 diagnosis) |     |     |
| --- | --- | ------ | ------ | ---- | ------------------------------ | --- | --- |
|     | -14 | -10 -6 | -2 0 2 | 6 10 | 14 20 60                       | 100 | 140 |
AP1
AP2
AP3
AP4
AP5
AP6
Adult  AP7 AP8
COVID-19 AP9
AP10
AP11
AP12
AP13
AP14
BP1
BP2
BP3
BP4
PP1
PP2
PP3
PP4
PP5
PP6
PP7
Paediatric  PP8
COVID-19 PP9
P P 1 0
|     | P P 11  |     |     |     | symptom onset                        |     |     |
| --- | ------- | --- | --- | --- | ------------------------------------ | --- | --- |
|     | PP12    |     |     |     | SARS-CoV2 PCR detection              |     |     |
|     | P P 1 3 |     |     |     | Nasal/Tracheal/Bronchi brush, blood  |     |     |
P P 1 4
|     | PP15 |     |     |     | Convalescent blood  |     |     |
| --- | ---- | --- | --- | --- | ------------------- | --- | --- |
PP16
PP17
PP18
PP19
PC2
PC5
PC6
PC9
PC10
Post  P C 11
P C 1 2
COVID-19 PC17
PC18
PC19
PC21
PC24
PC26
PC27
PC29
Extended Data Figure 1
c

1 elbaT ataD dednetxE
)sry 28 - shtnom 4( 74
|              |                    |                                    | 650,1 ± 361,2 | 118,1 ± 453,5                      |                   |                   |                | )(                  |
| ------------ | ------------------ | ---------------------------------- | ------------- | ---------------------------------- | ----------------- | ----------------- | -------------- | ------------------- |
| 91DIVOC-tsoP |                    |                                    |               |                                    | )7.64( 7          | )3.35( 8          |                | )3.31( 2            |
| )51 = n(     | )0.08( 21 )0.02( 3 | )7.66( 01 )7.6( 1 )3.31( 2 )3.6( 1 | )7.6( 1       | )3.33( 5 )02( 3 )0.04( 6 )7.68( 31 | )0( 0 )0( 0 )0( 0 | )0( 0 )0( 0 )0( 0 | )001( 51 )0( 0 | )7.6( 1 )0( 0 )0( 0 |
|              |                    | )0( 0 )0( 0 )0( 0                  |               |                                    |                   |                   |                |                     |
-
stluda evitisop 2-VoC-SRAS
|          | )sry 29 - 52( 66   |                             | 1.405 ± 581,1 | 862,3 ± 572,6                |                            |                            |           |                                         |
| -------- | ------------------ | --------------------------- | ------------- | ---------------------------- | -------------------------- | -------------------------- | --------- | --------------------------------------- |
| )81 = n( | )6.55( 01 )4.44( 8 | )9.83( 7 )7.61( 3 )8.72( 5  |               | )6.55( 01 )8.61( 3 )7.66( 21 | )7.61( 3 )2.22( 4 )2.22( 4 | )9.83( 7 )8.72( 5 )7.61( 3 | )5.55( 01 |                                         |
|          |                    | )6.5( 1 )0( 0 )0( 0 )6.5( 1 | )6.5( 1       | )05( 9                       | )0( 0                      | )0( 0                      | )0( 0     | )7.5( 1 )0( 0 )7.5( 1 )7.5( 1 )0( 0     |
nerdlihc evitisop 2-VoC-SRAS
)sry 61 - syad 3( 4
307,2 ± 903,3 819,5 ± 996,6
|          | )7.37( 41 )3.62( 5 | )6.25( 01 )8.51( 3 )3.62( 5 |       | )4.74( 9 )1.24( 8 )3.62( 5 )6.13( 6 | )8.51( 3 )5.01( 2 | )8.63( 7 )3.62( 5 )1.12( 4 | )4.74( 9 )5.01( 2 | )8.51( 3                    |
| -------- | ------------------ | --------------------------- | ----- | ----------------------------------- | ----------------- | -------------------------- | ----------------- | --------------------------- |
| )91 = n( |                    | )0( 0 )0( 0 )0( 0 )3.5( 1   | )0( 0 |                                     | )4.74( 9 )3.5( 1  | )3.5( 1                    |                   | )3.5( 1 )3.5( 1 )0( 0 )0( 0 |
stluda evitagen 2-VoC-SRAS
)sry 76 - 62( 34
| )11 = n( | )4.63( 4 )6.36( 7 | )7.27( 8                                  |       |                         |       |          |       |         |
| -------- | ----------------- | ----------------------------------------- | ----- | ----------------------- | ----- | -------- | ----- | ------- |
|          |                   | )1.9( 1 )0( 0 )1.9( 1 )0( 0 )1.9( 1 )0( 0 | )0( 0 | )0( 0 )0( 0 )0( 0 )0( 0 | )0( 0 | AN AN AN | AN AN | AN      |
|          |                   |                                           | -     | -                       | - - - | -        |       | - - - - |
nerdlihc evitagen 2-VoC-SRAS
)sry 61 - syad 3( 78.2
6.486 ± 620,2 188,6 ± 078,7
|          | )3.34( 31 )7.65( 71 | )7.66( 02                                                                                                                       |                                             |                                                                                                                                  |                                                         |                                                |            |                                                 |
| -------- | ------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- | ---------------------------------------------- | ---------- | ----------------------------------------------- |
| )03 = n( |                     | )3.31( 4 )0( 0 )3.3( 1 )3.3( 1 )0( 0 )3.3( 1                                                                                    | )01( 3                                      | )7.6( 2                                                                                                                          |                                                         |                                                |            | )0( 0 )0( 0 )0( 0 )0( 0                         |
|          |                     |                                                                                                                                 |                                             | )0( 0 )0( 0 )0( 0                                                                                                                | )0( 0 - - -                                             | - AN AN AN                                     | AN AN      | AN                                              |
|          | )%( elaM )%( elameF | )%( etihW )%( kcalB )%( cinapsiH )%( naisA htuoS )%( naisA lartneC ro nretsaE elddiM )%( rednalsI cificaP /naisA tsaE )%( rehtO | )%( deificepsnU )lμ/sllec( tnuoc etycohpmyL | )lμ/sllec( tnuoc lihportueN )%( eugitaF ,reveF )%( motpmys evitsegiD )%( motpmys tcart yrotaripser reppU )%( eruliaf yrotaripseR | )%( rehtO )%( enoN )%( negyxo wolf woL )%( VPPIN / CNFH | )%( VMI )%( citamotpmysA )%( dliM )%( etaredoM | )%( ereveS | )%( lairetcaB )%( lariV )%( lagnuF )%( elptiluM |
gnilpmas ta tset doolb larehpireP
 )noitcelloc elpmas ot roirP(
|     |     |     |     | smotpmys detropeR | troppuS yrotaripseR |     | noitcefni-oC detceteD |  tnemtaerT 91-DIVOC |
| --- | --- | --- | --- | ----------------- | ------------------- | --- | --------------------- | ------------------- |
ytireves 91-DIVOC
ega naideM
yticinhtE
C-SIM
xeS

1 lasaB +2SBRDHK
1
lasaB
2 lasaB lasab
gnilcyC
rosrucerp
kcolliH
kcollih
gnilcyC
kcolliH suomauqS yroterceS +4TNLAG
yroterceS
tcuD bulC 1 telboG +2AFIPB
2 telboG
+UALP
2
telboG
yrotammalfni
2 telboG
1 ipe
tisnarT
2 ipe
tisnarT
lamosoretueD 1 detailiC 2 detailiC etyconoI hsurB enircodneorueN etyconaleM evian
T
ger T hf T +4RCC
4DC
T
mem
4DC
T
TIAM gnilcyc
T
1 mem
8DC
T
2 mem
8DC
T
3 mem
8DC
T
detsuahxe
8DC
T
dg T TKN ih65dc
KN
ol65dc
KN
CLI evian
B
mem
B
detsuahxe
mem
B
detavitca
mem
B
gnilcyc
B
KgI amsalP LgI amsalP caM detavitca
caM
CL +01LCXC
onoM
+1RABPG
onoM
+6LI
onoM
tueN detavitca
CDc
CDp CDf tsaM
1.5
1.0
0.5
0.0
ahpla-NFI
1
lasaB
+2SBRDHK
1 lasaB
2
lasaB
lasab
gnilcyC
rosrucerp
kcolliH
kcollih
gnilcyC
kcolliH suomauqS yroterceS +4TNLAG
yroterceS
tcuD bulC 1
telboG
+2AFIPB
2 telboG
+UALP
2
telboG
yrotammalfni
2 telboG
1
ipe tisnarT
2
ipe tisnarT
lamosoretueD 1
detailiC
2
detailiC
etyconoI hsurB enircodneorueN etyconaleM evian
T
ger
T
hf
T
+4RCC
4DC
T
mem
4DC
T
TIAM gnilcyc
T
1
mem 8DC
T
2
mem 8DC
T
3
mem 8DC
T
detsuahxe
8DC T
dg
T
TKN ih65dc
KN
ol65dc
KN
CLI evian
B
mem
B
detsuahxe
mem B
detavitca
mem B
gnilcyc
B
KgI
amsalP
LgI
amsalP
caM detavitca
caM
CL +01LCXC
onoM
+1RABPG
onoM
+6LI
onoM
tueN detavitca
CDc
CDp CDf tsaM
0.8
0.6
0.4
0.2
0.0
ammag-NFI
b
c
Expression signature scoring of cellular response to interferon
in whole cohort (healthy, COVID-19, post-COVID-19)
−300
−200
−100
0
−2 −1 0 1 2
Extended Data Figure 5
)p(01gol
Goblet 2 inflammatory
IFI6
−300
IFITMIF3IIFTIMTIM3F1IITFI6M1
IFIT1
MX1
ISG15 NTS
−200 IFIT3
OAS1 CYP4B1 NUPR1
LGALS3BP MSMB
−100
0
−2 −1 0 1
Log2FoldChange (COVID-19/Healthy)
)p(01gol
Transit epi 1
−300
MSMB −200
S100A9 IFITM3 S100A2
IFI6
SCGB1A1 −100 S100A8 IFITM1 RARRES1 MX1 XIST
MT1E 0
−2 0 2 4
)p(01gol
a
donor Age_bin
● ●● ●● ● ● ● ● ● ● ● ● ●● ●● ● ● ● ● ●● ●● ● ● ● ● ● ● ● ● ● ● ● ● ●● ● ● ●● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ●● ● ● ● ● ● ● ● ● ● ● ● ● ●● ● ● ●● ●● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ●● ● ● ●● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● Sample_location
●● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ●●● ●● ● ● ● ● ●● ● ● ● ● ● ● ● ● ●● ● ● ● ● ● ●●●● ● ● ● ●●●● ● ● ● ●● COVID_status:Group
●●●●●●● ●●●● ●●●● ●●● ●●●●●●●●● ● ●●●●●●● ●●●●●● ●●●●●●● ●●●●●●●●●●●
● ● ● ● ● ● ● ● ● ●● ● ● ● ● ● ● ● ● ●● ●● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ●● ● ● ●● ● ● ● ● ● ● ●● ● ● ● ● ● ● ● ● ● ● ● ● ●● ● ● ●● ●● ● ● ● ● ● ● ● ● ●● ● ● ● ● ● ● ● ● ● ●● ● ● ● ●● ● ● ●● ● ● ● ● ● ● ●● ●● ● ● ● ● ● ● ● dataset
● ●● ●● ●● ●● ●● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ●● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ●● ● ● ● ● ● ● ●● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ●● ● ● ● ● ●● ● ● ● ● ● ● ●● ● ● ● ● ●● ●● ● ● ● ● ● ● ● ● ● ● ● ● ● Sex
● ●● ● ● ● ●●●●●●●●●●●●●●● ● ● ●●● ● ●●● ● ● ● ● ● ● ● ● ●● ●● ● ●●●●●●● ● ●● ● ●● ● ●● Kit_version
●● ●●● ●●●● ●●●● ● ●●● ●●● ● ● ●●● ● ● ● ● ● ●●●●● ●● ● ● ● ●●●●●●●● ●●● ●●● ● ● ● ● ●
●●● ● ● ● ●● ● ● ●● ● ● ● ● ● ● ● ● ●● ● ● ● ● ● ● ● ●●● ● ● ● ● ● ● ● ● ●● ● ● ● ● ● ● ● ● ● ● ● ● ● ●● ● ● Smoker
● ●● ●● ●●●●●●●●●●●●●● ● ● ●● ●●●●●● ● ● ● ● ● ● ● ● ● ● ● ●●●●●●●●● ● ● ● ● ● ●● ● ● ●
● ● ● ● ● ● ●● ● ● ●● ● ● ● ●● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● Residual
●● ● ●●● ●● ● ● ●●● ●●●●● ●●● ● ●●●●● ● ●● ●●●●●●● ● ● ● ●●●●●●●● ●●●●●●● ● ● ●●
● ●● ●●●●● ● ● ●●● ● ● ● ● ● ●●● ● ●●●●● ● ● ● ●●●●●●● ●●● ● ● ● ●●● ● ● ●●●●●● ● ● ● ●● −0.5 0.0 0.5 1.0 1.5 ● ● ●● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ●●● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● Square root of explained variance
Airway cells
d
Monocyte IL6+
IFITM3
significant
IFIT2 IFITM1 Down None
HRASLS2 S100A8 APOBEC3A Up
MT IS R G N 1 R 5 2L12 S S 1 1 0 0 0 0 A A 4 9 LY IF 6 I E TM2 IS I G FI 1 6 5 IFI27 IFITM2 BCL2A1 MYL12A MX1
S100A12
Log2FoldChange (COVID-19/Healthy) Log2FoldChange (COVID-19/Healthy)
1 lasaB
+2SBRDHK
1 lasaB 2 lasaB lasab gnilcyC
rosrucerp
kcolliH kcollih gnilcyC kcolliH suomauqS yroterceS
+4TNLAG
yroterceS tcuD bulC 1 telboG
+2AFIPB
2 telboG
+UALP
2 telboG
yrotammalfni
2 telboG 1 ipe tisnarT 2 ipe tisnarT lamosoretueD 1 detailiC 2 detailiC etyconoI hsurB
enircodneorueN
etyconaleM evian T ger T hf T +4RCC 4DC T mem 4DC T TIAM gnilcyc T 1 mem 8DC T 2 mem 8DC T 3 mem 8DC T
detsuahxe
8DC T dg T TKN ih65dc KN ol65dc KN CLI evian B mem B
detsuahxe
mem B
detavitca
mem B gnilcyc B KgI amsalP LgI amsalP caM detavitca caM
+01LCXC
onoM
+1RABPG
onoM +6LI onoM tueN CL detavitca CDc CDp CDf tsaM
Nose Trachea
Bronchi
Neonate
Infant Young child
Child Adolescent
Adult
Elderly
Healthy,Adult
COVID-19,Adult
Post−COVID-19,Adult
Healthy,Paed Log2FC
COVID-19,Paed Post−COVID-19,Paed LTSR 1 0.5
0 0.9
0.99
−1
0.999

Treg
Secretory
CTL
B cell
NKT-p
pDC nrMa
Ionocyte
Ciliated
Squamous
MoD-Ma
MC
NK
rMa
Neu
FOXN4
IRC Secretory-diff
Basal
NKT
moDC
unknown_epithelial
Ciliated-diff outliers_epithelial
mem
B
detavitca
mem B
evian
B
detsuahxe
mem B
suomauqS tsaM +01LCXC
onoM
CDp KgI
amsalP
LgI
amsalP
tueN gnilcyc
B
gnilcyc
T
lasab
gnilcyC
kcollih
gnilcyC
3
mem 8DC
T
ih65dc
KN
1
mem 8DC
T
detsuahxe
8DC T
ol65dc
KN
2
mem 8DC
T
TKN hf
T
+4RCC
4DC
T
mem
4DC
T
CLI evian
T
ger
T
TIAM dg
T
lamosoretueD 1
detailiC
2
detailiC
+1RABPG
onoM
+6LI
onoM
caM detavitca
caM
CL detavitca
CDc
etyconoI hsurB enircodneorueN etyconaleM CDf 1
ipe tisnarT
2
ipe tisnarT
rosrucerp
kcolliH
2
lasaB
1
lasaB
kcolliH yrotammalfni
2 telboG
+yr2oSteBrRceDSHK
1 lasaB
tcuD +4TNLAG
yroterceS
1
telboG
+UALP
2
telboG
bulC +2AFIPB
2 telboG
0.8
0.6
0.4
0.2
etyconoI gnilcyc
B
mem
B
detsuahxe
mem B
evian
B
detavitca
mem B
CL detavitca
CDc
lamosoretueD +01LCXC
onoM
1
lasaB
+2SBRDHK
1 lasaB
rosrucerp
kcolliH
+4RCC
4DC
T
evian
T
CLI mem
4DC
T
TIAM gnilcyc
T
3
mem 8DC
T
ih65dc
KN
ol65dc
KN
1
mem 8DC
T
ger
T
TKN dg
T
hf
T
2
mem 8DC
T
detsuahxe
8DC T
suomauqS +6LI
onoM
tueN 1
detailiC
2
detailiC
+1RABPG
onoM
caM detavitca
caM
lasab
gnilcyC
kcollih
gnilcyC
CDp enircodneorueN KgI
amsalP
LgI
amsalP
tsaM hsurB etyconaleM 2C
lDasfaB
kcolliH tcuD +4TNLAG
yroterceS
yroterceS bulC 1
telboG
yrotammalfni
2 telboG
+2AFIPB
2 telboG
+UALP
2
telboG
1
ipe tisnarT
2
ipe tisnarT
a
Mac Fraction of cells
Mac activat L e C d in group (%)
Mono CXCL10+
Mono M G o P n B o A I R L6 1+ + 20406080100
Neut
cDC activated
pDC M fD as C t in group
0.0 0.5 1.0
b c
Probability of transfering Chua et al labels
CCNO CDC20B FOXN4
Deu
KRT4 KRT7 IFT43
Ba-d
ISG15 IFIT1 CXCL10
IRC
FP671120.4 S100A8 S100A9
d
Transit Probability of transfering Ziegler et al labels
epi
Extended Data Figure 3
4PBAF 3.963620CA DCS 4PBR 1CRM 1ESANR LPN 1PPS C02MAF 2DHDMA A1RECF 702DC BIKP 2BQD-ALH C1DC 01LCXC A3CEBOPA 3TIFI 02GSI 2TIFI 2F2UOP 1DSCR 1RGSA 1MARP 412PUN 1SBHT 6LI 2MTIFI 2KORP 2RCXC LPLA P001S 3PMAL 21PSU 1L1APIS SLG 08DC BMZG 31NAPST NIAHCJ 4FCT 1BZM 2SERRAR 7PBFGI 2ENIPRES MONELES 41LCXC 2BSPT 1BASPT 3APC 2A4SM TIK 1COPA BQ1C CQ1C BMNPG RFHCG 4GISV 41DC A3RGCF 1NCF NACV E003DC 1SBHT 2LCC
Mean expression
0.8
0.6
0.4
0.2
Interferon Responsive Cytotoxic CD8 T Cells B Cells
Basal Cells
Dendritic Cells
SERPINB11 high Secretory Cells
Ionocytes
Mitotic Basal Cells
Inflammatory Macrophages
MSR1 C1QB high Macrophages
CD8 T Cells
Interferon Responsive Macrophages
Deuterosomal Cells
SCGB1A1 high Goblet Cells
SPRR2D high Squamous Cells
Plasmacytoid DCs Developing Ciliated Cells
Interferon Responsive Ciliated Cells
ITGAX high Macrophages
BEST4 high Cilia high Ciliated Cells
KRT24 KRT13 high Secretory Cells
AZGP1 high Goblet Cells
Interferon Responsive Secretory Cells
AZGP1 SCGB3A1 LTF high Goblet Cells BPIFA1 high Secretory Cells
MUC5AC high Goblet Cells
Mast Cells
HOPX high Squamous Cells
VEGFA high Squamous Cells
Developing Secretory and Goblet Cells
BPIFA1 and Chemokine high Secretory Cells
FOXJ1 high Ciliated Cells FFAR4 high Macrophages
Early Response T Cells
Cilia high Ciliated Cells
CCL5 high Squamous Cells
Early Response Secretory Cells
Erythroblasts
Early Response FOXJ1 high Ciliated Cells
Enteroendocrine Cells
e
Basal 1 Basal 1 KHDRBS2+ Basal 2 Cycling basal Hillock precursor
1 2 3 4 0 0 0 0 0 (cid:1)(cid:1) (cid:1) (cid:1) (cid:1) (cid:1) (cid:1)(cid:1) (cid:1)(cid:1) (cid:1) (cid:1) (cid:1)(cid:1)(cid:1)(cid:1) (cid:1)(cid:1) (cid:1) (cid:1) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1) (cid:1)(cid:1)(cid:1) (cid:1) (cid:1) (cid:1)(cid:1) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1) (cid:1) 0 1 2 3 4 5 (cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1) (cid:1)(cid:1)(cid:1)(cid:1) (cid:1) (cid:1) (cid:1)(cid:1)(cid:1)(cid:1) (cid:1) (cid:1)(cid:1)(cid:1) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1) (cid:1)(cid:1)(cid:1) (cid:1) (cid:1) (cid:1)(cid:1) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1) (cid:1) 1 2 3 0 0 0 0 (cid:1) (cid:1)(cid:1) (cid:1) (cid:1) (cid:1) (cid:1)(cid:1) (cid:1)(cid:1)(cid:1) (cid:1) (cid:1) (cid:1)(cid:1)(cid:1) (cid:1)(cid:1) (cid:1) (cid:1) (cid:1)(cid:1) (cid:1)(cid:1)(cid:1) (cid:1) (cid:1) (cid:1) (cid:1)(cid:1) (cid:1)(cid:1) (cid:1)(cid:1) (cid:1) (cid:1)(cid:1) (cid:1) 1 1 0 5 0 5 (cid:1) (cid:1)(cid:1) (cid:1) (cid:1) (cid:1) (cid:1)(cid:1) (cid:1)(cid:1)(cid:1) (cid:1) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1) (cid:1) (cid:1) (cid:1)(cid:1)(cid:1) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1) (cid:1) 0 0 1 1 2 . . . . . 0 5 0 5 0 (cid:1)(cid:1) (cid:1) (cid:1) (cid:1)(cid:1) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1) (cid:1)(cid:1)(cid:1)(cid:1) (cid:1) (cid:1)(cid:1)(cid:1) (cid:1)(cid:1)(cid:1)(cid:1) (cid:1) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1) (cid:1)
Cycling hillock Hillock Squamous Secretory Secretory GALNT4+
0 0 1 1 . . . . 0 5 0 5 (cid:1) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1) (cid:1) (cid:1) 0 2 4 6 (cid:1) (cid:1) (cid:1) (cid:1) (cid:1) (cid:1) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1) (cid:1) (cid:1)(cid:1)(cid:1) (cid:1) (cid:1)(cid:1)(cid:1) (cid:1)(cid:1)(cid:1) (cid:1)(cid:1) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1) (cid:1) (cid:1) (cid:1) 1 0 2 5 7 0 . . . . . 0 5 0 5 0 (cid:1)(cid:1)(cid:1)(cid:1) (cid:1)(cid:1) (cid:1)(cid:1)(cid:1) (cid:1) (cid:1)(cid:1) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1) (cid:1)(cid:1)(cid:1) (cid:1) (cid:1) (cid:1) (cid:1) (cid:1)(cid:1)(cid:1) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1) (cid:1) 1 2 0 0 0 (cid:1) (cid:1) (cid:1)(cid:1)(cid:1) (cid:1) (cid:1) (cid:1) (cid:1)(cid:1)(cid:1) (cid:1) (cid:1) (cid:1) (cid:1) (cid:1) (cid:1)(cid:1)(cid:1)(cid:1) (cid:1) (cid:1)(cid:1) (cid:1)(cid:1) (cid:1)(cid:1) (cid:1)(cid:1) (cid:1) (cid:1)(cid:1)(cid:1) (cid:1) (cid:1) (cid:1) (cid:1) (cid:1) 1 2 3 0 0 0 0 (cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1) (cid:1)(cid:1)(cid:1)(cid:1) (cid:1) (cid:1) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1) (cid:1)(cid:1) (cid:1) (cid:1)(cid:1) (cid:1)(cid:1)(cid:1) (cid:1) (cid:1) (cid:1)(cid:1) (cid:1)(cid:1)(cid:1) (cid:1)(cid:1) (cid:1)
Duct Club Goblet 1 Goblet 2 BPIFA2+ Goblet 2 PLAU+ 0 1 2 3 (cid:1)(cid:1)(cid:1)(cid:1) (cid:1) (cid:1) (cid:1) (cid:1) (cid:1)(cid:1)(cid:1)(cid:1) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1) (cid:1)(cid:1)(cid:1) (cid:1) (cid:1) (cid:1) (cid:1)(cid:1) (cid:1) (cid:1) (cid:1)(cid:1) (cid:1) (cid:1) (cid:1)(cid:1)(cid:1) (cid:1) 10 0 5 (cid:1) (cid:1) (cid:1) (cid:1)(cid:1)(cid:1) (cid:1) (cid:1) (cid:1) (cid:1) (cid:1)(cid:1) (cid:1)(cid:1) (cid:1)(cid:1) (cid:1)(cid:1)(cid:1)(cid:1) (cid:1)(cid:1)(cid:1) (cid:1) (cid:1) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1) (cid:1) 1 2 0 0 0 (cid:1)(cid:1) (cid:1) (cid:1) (cid:1)(cid:1) (cid:1) (cid:1) (cid:1) (cid:1)(cid:1)(cid:1) (cid:1) (cid:1) (cid:1)(cid:1) (cid:1)(cid:1)(cid:1) (cid:1) (cid:1)(cid:1)(cid:1) (cid:1) (cid:1) (cid:1) (cid:1) (cid:1) (cid:1) (cid:1) (cid:1)(cid:1)(cid:1) (cid:1) (cid:1) (cid:1) (cid:1) (cid:1) 2 4 6 0 0 0 0 (cid:1)(cid:1) (cid:1)(cid:1)(cid:1)(cid:1) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1) (cid:1) (cid:1) (cid:1) (cid:1)(cid:1) (cid:1)(cid:1) (cid:1) (cid:1) (cid:1) (cid:1) (cid:1) (cid:1)(cid:1) (cid:1)(cid:1) (cid:1) (cid:1)(cid:1) (cid:1)(cid:1) (cid:1) (cid:1) (cid:1) (cid:1)(cid:1) (cid:1) 1 2 3 0 0 0 0 (cid:1)(cid:1) (cid:1) (cid:1) (cid:1)(cid:1) (cid:1) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1) (cid:1)(cid:1) (cid:1)(cid:1)(cid:1) (cid:1)(cid:1)(cid:1) (cid:1)(cid:1)(cid:1) (cid:1)(cid:1) (cid:1)(cid:1) (cid:1)(cid:1)(cid:1) (cid:1)(cid:1) (cid:1) (cid:1) (cid:1) (cid:1) (cid:1) (cid:1)
Goblet 2 inflammatory Transit epi 1 Transit epi 2 Deuterosomal Ciliated 1
10 0 5 (cid:1)(cid:1) (cid:1) (cid:1) (cid:1) (cid:1) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1) (cid:1)(cid:1) (cid:1) (cid:1)(cid:1) (cid:1) (cid:1) (cid:1) (cid:1)(cid:1)(cid:1)(cid:1) (cid:1)(cid:1) (cid:1) (cid:1) (cid:1)(cid:1) (cid:1) (cid:1) 10 0 5 (cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1) (cid:1)(cid:1)(cid:1)(cid:1) (cid:1) (cid:1)(cid:1) (cid:1) (cid:1)(cid:1) (cid:1)(cid:1) (cid:1) (cid:1)(cid:1)(cid:1)(cid:1) (cid:1) 2 4 6 0 0 0 0 (cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1) (cid:1) (cid:1) (cid:1) 0 1 2 3 4 5 (cid:1)(cid:1)(cid:1) (cid:1)(cid:1) (cid:1) (cid:1)(cid:1) (cid:1) (cid:1)(cid:1)(cid:1) (cid:1) (cid:1)(cid:1) (cid:1) (cid:1)(cid:1) (cid:1) (cid:1) (cid:1) (cid:1) (cid:1) (cid:1)(cid:1) (cid:1) (cid:1) (cid:1)(cid:1)(cid:1) (cid:1)(cid:1) (cid:1) (cid:1) (cid:1)(cid:1)(cid:1) (cid:1) 1 2 3 4 0 0 0 0 0 (cid:1)(cid:1) (cid:1) (cid:1) (cid:1)(cid:1) (cid:1)(cid:1) (cid:1)(cid:1)(cid:1) (cid:1) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1) (cid:1) (cid:1) (cid:1) (cid:1) (cid:1) (cid:1) (cid:1) (cid:1) (cid:1) (cid:1) (cid:1) (cid:1)(cid:1) (cid:1)(cid:1) (cid:1)(cid:1)(cid:1)(cid:1) (cid:1) (cid:1)
1 1 2 0 5 0 0 5 (cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1) (cid:1) (cid:1) (cid:1)(cid:1)(cid:1) (cid:1) C (cid:1) (cid:1) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1) ilia (cid:1)(cid:1) (cid:1) (cid:1)(cid:1) te (cid:1)(cid:1)(cid:1) (cid:1)(cid:1) d 2 (cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1) (cid:1) (cid:1) 0 2 4 6 8 (cid:1)(cid:1) (cid:1) (cid:1) (cid:1) (cid:1) (cid:1) (cid:1)(cid:1) (cid:1) (cid:1)(cid:1) I (cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1) (cid:1) on (cid:1) (cid:1) (cid:1) (cid:1)(cid:1) ocy (cid:1)(cid:1)(cid:1) (cid:1)(cid:1) te (cid:1)(cid:1) (cid:1) (cid:1) (cid:1)(cid:1)(cid:1) (cid:1) 0 0 0 0 . . . . 0 2 5 7 0 5 0 5 (cid:1) (cid:1) (cid:1) (cid:1) (cid:1) (cid:1) (cid:1)(cid:1)(cid:1) (cid:1) (cid:1)(cid:1) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1) (cid:1)(cid:1) Br (cid:1)(cid:1) (cid:1) (cid:1)(cid:1) us (cid:1)(cid:1)(cid:1)(cid:1)(cid:1) h (cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1) (cid:1) 0 0 0 0 . . . . 0 2 5 7 0 5 0 5 (cid:1) (cid:1)(cid:1) (cid:1) (cid:1)(cid:1) N (cid:1)(cid:1)(cid:1) (cid:1) (cid:1)(cid:1) eu (cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1) roe (cid:1)(cid:1)(cid:1)(cid:1)(cid:1) nd (cid:1)(cid:1)(cid:1)(cid:1)(cid:1) oc (cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1) rin (cid:1) e 0 0 0 0 . . . . 0 0 1 1 0 5 0 5 (cid:1) (cid:1) (cid:1) (cid:1) (cid:1)(cid:1) (cid:1)(cid:1)(cid:1) (cid:1) (cid:1) (cid:1) M (cid:1) (cid:1) (cid:1) (cid:1) (cid:1) (cid:1)(cid:1)(cid:1) ela (cid:1) (cid:1) (cid:1)(cid:1)(cid:1) no (cid:1) (cid:1) (cid:1)(cid:1)(cid:1) cy (cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1) te (cid:1)
Age bin
egatnecreP
Healthy nasal epithelial cells
Age bin Neonate
Infant Young child Child
Adolescent
Adult Elderly