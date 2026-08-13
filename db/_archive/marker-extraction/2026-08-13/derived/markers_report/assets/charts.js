(function() {
  var style = getComputedStyle(document.documentElement);
  var accent = style.getPropertyValue('--accent').trim();
  var accent2 = style.getPropertyValue('--accent2').trim();
  var ink = style.getPropertyValue('--ink').trim();
  var muted = style.getPropertyValue('--muted').trim();
  var rule = style.getPropertyValue('--rule').trim();
  var bg2 = style.getPropertyValue('--bg2').trim();
  var pns = style.getPropertyValue('--pns').trim();
  var warn = style.getPropertyValue('--warn').trim();

  // ---- Chart 1: Evidence Distribution (Pie) ----
  var chart1 = echarts.init(document.getElementById('chart-evidence'), null, { renderer: 'svg' });
  chart1.setOption({
    animation: false,
    tooltip: { trigger: 'item', appendToBody: true, formatter: '{b}: {c} ({d}%)' },
    legend: { bottom: 0, textStyle: { color: muted, fontSize: 12 } },
    series: [{
      type: 'pie',
      radius: ['35%', '65%'],
      center: ['50%', '45%'],
      label: { show: true, formatter: '{d}%', color: ink, fontSize: 12 },
      data: [
        { value: 3158, name: 'explicit', itemStyle: { color: accent } },
        { value: 652, name: 'implied', itemStyle: { color: accent2 } },
        { value: 57, name: 'inferred', itemStyle: { color: warn } },
        { value: 7, name: 'imported', itemStyle: { color: muted } }
      ]
    }]
  });
  window.addEventListener('resize', function() { chart1.resize(); });

  // ---- Chart 2: Species Distribution (Pie) ----
  var chart2 = echarts.init(document.getElementById('chart-species'), null, { renderer: 'svg' });
  chart2.setOption({
    animation: false,
    tooltip: { trigger: 'item', appendToBody: true, formatter: '{b}: {c} ({d}%)' },
    legend: { bottom: 0, textStyle: { color: muted, fontSize: 12 } },
    series: [{
      type: 'pie',
      radius: ['35%', '65%'],
      center: ['50%', '45%'],
      label: { show: true, formatter: '{d}%', color: ink, fontSize: 12 },
      data: [
        { value: 2965, name: 'human', itemStyle: { color: accent } },
        { value: 747, name: 'mouse', itemStyle: { color: accent2 } },
        { value: 109, name: 'rat', itemStyle: { color: warn } },
        { value: 39, name: 'zebrafish', itemStyle: { color: pns } },
        { value: 14, name: 'unknown', itemStyle: { color: muted } }
      ]
    }]
  });
  window.addEventListener('resize', function() { chart2.resize(); });

  // ---- Chart 3: PNS Distribution (Pie) ----
  var chart3 = echarts.init(document.getElementById('chart-pns'), null, { renderer: 'svg' });
  chart3.setOption({
    animation: false,
    tooltip: { trigger: 'item', appendToBody: true, formatter: '{b}: {c} ({d}%)' },
    legend: { bottom: 0, textStyle: { color: muted, fontSize: 12 } },
    series: [{
      type: 'pie',
      radius: ['40%', '70%'],
      center: ['50%', '45%'],
      label: { show: true, formatter: '{b}\n{d}%', color: ink, fontSize: 12 },
      data: [
        { value: 3431, name: '非 PNS', itemStyle: { color: accent } },
        { value: 391, name: 'PNS', itemStyle: { color: pns } },
        { value: 52, name: '不确定 (NA)', itemStyle: { color: warn } }
      ]
    }]
  });
  window.addEventListener('resize', function() { chart3.resize(); });

  // ---- Chart 4: Top 15 Papers (Horizontal Bar) ----
  var topPapers = [
    ['DOI_10.1038_s41588_022_01243_4', 79],
    ['DOI_10.1101_2021.09.17.21263540', 80],
    ['DOI_10.1038_s41588_025_02158_6', 82],
    ['DOI_10.1038_s41586_024_08560_0', 83],
    ['DOI_10.1101_2024.03.05.583423', 92],
    ['A_molecular_cell_atlas_of_the_human_lung_f...', 106],
    ['PNAS.117.9466.2020', 110],
    ['DOI_10.1084_jem.20191130', 112],
    ['DOI_10.1038_s41586_021_03852_1', 120],
    ['DOI_10.1164_rccm.202207_1384OC', 122],
    ['DOI_10.1038_s41586_026_10627_z', 140],
    ['DOI_10.1016_j.cell.2021.07.023', 151],
    ['DOI_10.1038_s41467_026_69587_7', 204],
    ['DOI_10.1016_j.jcf.2025.01.016', 208],
    ['FRONT-CELL-NEUROSCI.15.624826.2021', 213],
  ];

  var chart4 = echarts.init(document.getElementById('chart-top-papers'), null, { renderer: 'svg' });
  chart4.setOption({
    animation: false,
    tooltip: { trigger: 'axis', appendToBody: true, axisPointer: { type: 'shadow' } },
    grid: { left: '30%', right: '8%', top: 10, bottom: 30 },
    xAxis: { type: 'value', axisLine: { lineStyle: { color: rule } }, axisLabel: { color: muted }, splitLine: { lineStyle: { color: rule } } },
    yAxis: { type: 'category', data: topPapers.map(function(d) { return d[0]; }), axisLine: { lineStyle: { color: rule } }, axisLabel: { color: ink, fontSize: 10, width: 200, overflow: 'truncate' } },
    series: [{
      type: 'bar',
      data: topPapers.map(function(d) { return d[1]; }),
      itemStyle: { color: accent, borderRadius: [0, 4, 4, 0] },
      label: { show: true, position: 'right', color: ink, fontSize: 11 }
    }]
  });
  window.addEventListener('resize', function() { chart4.resize(); });

  // ---- Chart 5: Top 30 Genes (Horizontal Bar) ----
  var topGenes = [
    ['CD4',10],
    ['WNT2',10],
    ['RAG1',11],
    ['CD68',11],
    ['CD36',11],
    ['SOX2',11],
    ['KRT5',11],
    ['Pecam1',12],
    ['FCGR3A',12],
    ['IL1B',12],
    ['POSTN',12],
    ['FOXJ1',13],
    ['OLFM4',13],
    ['APOE',13],
    ['DCN',14],
    ['PDGFRA',14],
    ['SPP1',14],
    ['CCL19',14],
    ['SFTPC',14],
    ['LYVE1',15],
    ['TP63',15],
    ['SCGB3A2',15],
    ['RGS5',16],
    ['SOX9',16],
    ['LGR5',17],
    ['CD14',17],
    ['MUC5AC',17],
    ['MS4A1',20],
    ['MKI67',20],
    ['ACTA2',24],
  ];

  var chart5 = echarts.init(document.getElementById('chart-top-genes'), null, { renderer: 'svg' });
  chart5.setOption({
    animation: false,
    tooltip: { trigger: 'axis', appendToBody: true, axisPointer: { type: 'shadow' } },
    grid: { left: '15%', right: '8%', top: 10, bottom: 30 },
    xAxis: { type: 'value', axisLine: { lineStyle: { color: rule } }, axisLabel: { color: muted }, splitLine: { lineStyle: { color: rule } } },
    yAxis: { type: 'category', data: topGenes.map(function(d) { return d[0]; }), axisLine: { lineStyle: { color: rule } }, axisLabel: { color: ink, fontSize: 11 } },
    series: [{
      type: 'bar',
      data: topGenes.map(function(d) { return d[1]; }),
      itemStyle: { color: accent2, borderRadius: [0, 3, 3, 0] },
      label: { show: true, position: 'right', color: ink, fontSize: 10 }
    }]
  });
  window.addEventListener('resize', function() { chart5.resize(); });

  // ---- Chart 6: Top 20 Cell Types (Horizontal Bar) ----
  var topCT = [
    ['Neoplastic Cell',19],
    ['Mast Cells',20],
    ['β',22],
    ['T Cell',23],
    ['Secretory Cells',23],
    ['Alveolar Fibroblasts',24],
    ['Enteroendocrine Cells',25],
    ['Pericytes',26],
    ['Monocytes',28],
    ['Goblet Cells',28],
    ['Schwann Cells',33],
    ['Cancer Cells',37],
    ['B Cells',38],
    ['Neutrophils',42],
    ['T Cells',45],
    ['Endothelial Cells',61],
    ['Fibroblast',65],
    ['Fibroblasts',77],
    ['Macrophages',103],
    ['Macrophage',113],
  ];

  var chart6 = echarts.init(document.getElementById('chart-top-ct'), null, { renderer: 'svg' });
  chart6.setOption({
    animation: false,
    tooltip: { trigger: 'axis', appendToBody: true, axisPointer: { type: 'shadow' } },
    grid: { left: '28%', right: '8%', top: 10, bottom: 30 },
    xAxis: { type: 'value', axisLine: { lineStyle: { color: rule } }, axisLabel: { color: muted }, splitLine: { lineStyle: { color: rule } } },
    yAxis: { type: 'category', data: topCT.map(function(d) { return d[0]; }), axisLine: { lineStyle: { color: rule } }, axisLabel: { color: ink, fontSize: 10 } },
    series: [{
      type: 'bar',
      data: topCT.map(function(d) { return d[1]; }),
      itemStyle: { color: accent, borderRadius: [0, 3, 3, 0] },
      label: { show: true, position: 'right', color: ink, fontSize: 10 }
    }]
  });
  window.addEventListener('resize', function() { chart6.resize(); });

  // ---- Chart 7: PNS Cell Types Top 20 (Horizontal Bar) ----
  var pnsCT = [
    ['Lymphoid Associated Glial',6],
    ['Non-Myelinating Remak Schwann Cells',6],
    ['proprioceptor',7],
    ['peptidergic nociceptor',7],
    ['Non-Myelinating Schwann Cell',7],
    ['Non-Myelinating Schwann Cells',8],
    ['Glia 2',8],
    ['mySC',9],
    ['Glia 3',9],
    ['Schwann',9],
    ['Repair Cells',9],
    ['Glia 1',10],
    ['nonpeptidergic nociceptor',11],
    ['Neuronal Cells',11],
    ['Glial Cells',11],
    ['nmSC',17],
    ['Schwann Cell',17],
    ['Myelinating Schwann Cells',17],
    ['Glis',19],
    ['Schwann Cells',33],
  ];

  var chart7 = echarts.init(document.getElementById('chart-pns-ct'), null, { renderer: 'svg' });
  chart7.setOption({
    animation: false,
    tooltip: { trigger: 'axis', appendToBody: true, axisPointer: { type: 'shadow' } },
    grid: { left: '35%', right: '8%', top: 10, bottom: 30 },
    xAxis: { type: 'value', axisLine: { lineStyle: { color: rule } }, axisLabel: { color: muted }, splitLine: { lineStyle: { color: rule } } },
    yAxis: { type: 'category', data: pnsCT.map(function(d) { return d[0]; }), axisLine: { lineStyle: { color: rule } }, axisLabel: { color: ink, fontSize: 10 } },
    series: [{
      type: 'bar',
      data: pnsCT.map(function(d) { return d[1]; }),
      itemStyle: { color: pns, borderRadius: [0, 3, 3, 0] },
      label: { show: true, position: 'right', color: ink, fontSize: 10 }
    }]
  });
  window.addEventListener('resize', function() { chart7.resize(); });

  // ---- Paper Table ----
  var paperData = [
    ['A_molecular_cell_atlas_of_the_human_lung_from_single-cell_RN',32,106],
    ['CELL-STEM-CELL.30.20.2023',9,22],
    ['COMMUN-BIOL.5.1105.2022',9,32],
    ['DOI_10.1016_j.ccell.2025.12.003',21,72],
    ['DOI_10.1016_j.cell.2017.09.004',2,2],
    ['DOI_10.1016_j.cell.2019.06.029',6,18],
    ['DOI_10.1016_j.cell.2019.08.008',1,1],
    ['DOI_10.1016_j.cell.2020.12.016',24,55],
    ['DOI_10.1016_j.cell.2021.04.028',37,76],
    ['DOI_10.1016_j.cell.2021.07.023',30,151],
    ['DOI_10.1016_j.cell.2021.11.031',15,38],
    ['DOI_10.1016_j.cell.2023.11.026',13,37],
    ['DOI_10.1016_j.celrep.2018.11.086',8,28],
    ['DOI_10.1016_j.devcel.2020.11.010',8,20],
    ['DOI_10.1016_j.isci.2024.111628',1,3],
    ['DOI_10.1016_j.jcf.2025.01.016',52,208],
    ['DOI_10.1016_j.jcmgh.2022.02.007',1,2],
    ['DOI_10.1016_j.xcrm.2024.101556',1,1],
    ['DOI_10.1038_s41467_021_21783_3',4,13],
    ['DOI_10.1038_s41467_023_40173_5',17,48],
    ['DOI_10.1038_s41467_023_40505_5',2,2],
    ['DOI_10.1038_s41467_024_52052_8',1,1],
    ['DOI_10.1038_s41467_025_57487_1',21,47],
    ['DOI_10.1038_s41467_026_69587_7',104,204],
    ['DOI_10.1038_s41556_023_01337_z',1,4],
    ['DOI_10.1038_s41586_020_2922_4',24,55],
    ['DOI_10.1038_s41586_021_03569_1',8,19],
    ['DOI_10.1038_s41586_021_03710_0',7,19],
    ['DOI_10.1038_s41586_021_03852_1',33,120],
    ['DOI_10.1038_s41586_021_03929_x',7,9],
    ['DOI_10.1038_s41586_021_04345_x',15,40],
    ['DOI_10.1038_s41586_022_05060_x',6,16],
    ['DOI_10.1038_s41586_024_07069_w',17,27],
    ['DOI_10.1038_s41586_024_07571_1',3,12],
    ['DOI_10.1038_s41586_024_08560_0',28,83],
    ['DOI_10.1038_s41586_026_10627_z',40,140],
    ['DOI_10.1038_s41588_022_01243_4',31,79],
    ['DOI_10.1038_s41588_024_01702_0',9,11],
    ['DOI_10.1038_s41588_025_02158_6',17,82],
    ['DOI_10.1038_s41591_023_02327_2',12,43],
    ['DOI_10.1038_s41591_024_03215_z',4,14],
    ['DOI_10.1038_s42003_021_02562_8',6,14],
    ['DOI_10.1038_s42003_024_07315_x',3,49],
    ['DOI_10.1038_s42255_023_00876_x',17,61],
    ['DOI_10.1038_s43587_024_00613_3',7,22],
    ['DOI_10.1038_s44161_022_00183_w',9,47],
    ['DOI_10.1038_s44161_025_00612_6',14,52],
    ['DOI_10.1038_s44318_024_00328_6',2,8],
    ['DOI_10.1073_pnas.2313326120',19,34],
    ['DOI_10.1084_jem.20191130',18,112],
    ['DOI_10.1101_2021.09.17.21263540',41,80],
    ['DOI_10.1101_2024.03.05.583423',21,92],
    ['DOI_10.1101_2024.10.23.619925',21,55],
    ['DOI_10.1101_2025.01.17.633590',20,35],
    ['DOI_10.1101_2025.09.26.678707',24,68],
    ['DOI_10.1126_science.aat5031',9,49],
    ['DOI_10.1126_science.aba6500',1,1],
    ['DOI_10.1126_science.abl4290',24,66],
    ['DOI_10.1126_science.abl4896',9,25],
    ['DOI_10.1126_science.abo0510',27,67],
    ['DOI_10.1126_science.abo1984',5,21],
    ['DOI_10.1126_sciimmunol.adf9988',11,28],
    ['DOI_10.1158_2159_8290.CD_22_0824',5,29],
    ['DOI_10.1161_CIRCULATIONAHA.120.051921',1,1],
    ['DOI_10.1164_rccm.202207_1384OC',49,122],
    ['DOI_10.3389_fdmed.2021.806294',7,14],
    ['DOI_10.3389_fimmu.2023.1211505',8,31],
    ['DOI_10.7554_eLife.62522',1,1],
    ['DOI_10.7554_eLife.71752',16,61],
    ['ENEURO.0066-20.2020',22,65],
    ['Early_human_lung_immune_cell_development_and_its_role_in_epi',34,68],
    ['FRONT-CELL-NEUROSCI.15.624826.2021',27,213],
    ['GLIA.69.188.2020',14,18],
    ['J-NEUROINFLAMM.22.205.2025',9,52],
    ['NATURE.587.619.2020',6,13],
    ['Organoid_modeling_of_human_fetal_lung_alveolar_development_r',14,45],
    ['PNAS.117.9466.2020',22,110],
    ['SCI-IMMUNOL.8.adf9988.2023',24,50],
    ['s41467-025-60371-7',8,35],
  ];

  var tbody = document.getElementById('paper-tbody');
  paperData.forEach(function(row, idx) {
    var tr = document.createElement('tr');
    var status = row[2] === 0 ? '<span class="pns-tag pns-na">空</span>' :
                row[2] < 5 ? '<span class="pns-tag pns-na">少</span>' :
                '<span class="pns-tag pns-true">OK</span>';
    tr.innerHTML = '<td>' + (idx + 1) + '</td><td>' + row[0] + '</td><td>' + row[1] + '</td><td>' + row[2] + '</td><td>' + status + '</td>';
    tbody.appendChild(tr);
  });

})();
