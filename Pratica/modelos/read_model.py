import re
from statistics import median
from cobra.io import  read_sbml_model
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

results={'pc182n6180_c': [45682], 'pc182n61819Z_c': [415], 'pc1819Z182n6_c': [39365], 'pc182n6205n3_c': [26942], 'pc182n6226n3_c': [26784], 'pc205n3182n6_c': [39345], 'pc226n3182n6_c': [39343], 'pc140183n6_c': [30635], 'pc160183n6_c': [30626], 'pc1619Z183n6_c': [30614], 'pc180183n6_c': [30630], 'pc140160_c': [336], 'pc1401619Z_c': [39464], 'pc182n6183n6_c': [30613], 'pc140180_c': [45701], 'pc1401819Z_c': [39540], 'pc140205n3_c': [26964], 'pc1819Z183n6_c': [30615], 'pc205n3183n6_c': [30595], 'pc140226n3_c': [26806], 'pc226n3183n6_c': [30593], 'pc160140_c': [320], 'pc140183n3_c': [37043], 'pc160183n3_c': [37034], 'pc1601619Z_c': [39455], 'pc160180_c': [45693], 'pc1619Z183n3_c': [37022], 'pc1601819Z_c': [293], 'pc180183n3_c': [37038], 'pc160205n3_c': [26955], 'pc182n6183n3_c': [37021], 'pc160226n3_c': [26797], 'pc1819Z183n3_c': [37023], 'pc1619Z140_c': [48260], 'pc205n3183n3_c': [37003], 'pc1619Z160_c': [289], 'pc226n3183n3_c': [37001], 'pc140184n3_c': [27280], 'pc160184n3_c': [27271], 'pc1619Z180_c': [45683], 'pc1619Z184n3_c': [27259], 'pc1619Z1819Z_c': [39521], 'pc182n6225n3_c': [30850], 'pc1619Z205n3_c': [26943], 'pc1819Z225n3_c': [30852], 'pc180184n3_c': [27275], 'pc205n3225n3_c': [30832], 'pc1619Z226n3_c': [26785], 'pc182n6184n3_c': [27258], 'pc180140_c': [48275], 'pc226n3225n3_c': [30830], 'pc1819Z184n3_c': [27260], 'pc180160_c': [224], 'pc205n3184n3_c': [27240], 'pc1801619Z_c': [39459], 'pc226n3184n3_c': [27238], 'pc1801819Z_c': [39535], 'pc180205n3_c': [26959], 'pc180226n3_c': [26801], 'pc1819Z140_c': [48261], 'pc1819Z160_c': [288], 'pc1819Z1619Z_c': [39444], 'pc1819Z180_c': [302], 'pc1819Z205n3_c': [26944], 'pc1819Z226n3_c': [26786], 'pc205n3140_c': [48240], 'pc205n3160_c': [45358], 'pc205n31619Z_c': [39424], 'pc205n3180_c': [45663], 'pc205n31819Z_c': [39503], 'pc205n3226n3_c': [26765], 'pc226n3140_c': [48238], 'pc226n3160_c': [421], 'pc226n31619Z_c': [39422], 'pc226n3180_c': [45661], 'pc226n31819Z_c': [39501], 'pc226n3205n3_c': [26922], 'pc140182n6_c': [39385], 'pc160182n6_c': [39376], 'pc1619Z182n6_c': [39364], 'pc180182n6_c': [39380], 'pc182n6140_c': [48259], 'pc182n6160_c': [408], 'pc182n61619Z_c': [39443], 'pc140203n3_c': [36648], 'pc140203n6_c': [36727], 'pc160203n3_c': [36639], 'pc160203n6_c': [36718], 'pc1619Z203n3_c': [36627], 'pc1619Z203n6_c': [36706], 'pc180203n3_c': [36643], 'pe140160_c': [19942], 'pc180203n6_c': [36722], 'pe1401619Z_c': [8544], 'pc182n6203n3_c': [36626], 'pe140180_c': [22988], 'pc182n6203n6_c': [36705], 'pe1401819Z_c': [8623], 'pe140205n3_c': [46700], 'pc1819Z203n3_c': [36628], 'pe140226n3_c': [46542], 'pc1819Z203n6_c': [36707], 'pe160140_c': [23375], 'pc205n3203n3_c': [36608], 'pc205n3203n6_c': [36687], 'pe1601619Z_c': [295], 'pc226n3203n3_c': [36606], 'pe160180_c': [19937], 'pe1601819Z_c': [296], 'pe160205n3_c': [19906], 'pc226n3203n6_c': [36685], 'pe160226n3_c': [19904, 46533], 'pc140204n6_c': [27043], 'pe1619Z140_c': [23363], 'pc160204n6_c': [27034], 'pe1619Z160_c': [8535], 'pc1619Z204n6_c': [27022], 'pc180204n6_c': [27038], 'pe1619Z180_c': [8539], 'pc182n6204n6_c': [27021], 'pe1619Z1819Z_c': [8524], 'pc1819Z204n6_c': [27023], 'pe1619Z205n3_c': [8504], 'pc205n3204n6_c': [27003], 'pe1619Z226n3_c': [8502, 46521], 'pc226n3204n6_c': [27001], 'pe180140_c': [23379], 'pe180160_c': [22980], 'pc140225n3_c': [30872], 'pe1801619Z_c': [22968], 'pc160225n3_c': [30863], 'pc1619Z225n3_c': [30851], 'pe1801819Z_c': [22969], 'pc180225n3_c': [30867], 'pe180205n3_c': [22948], 'pe205n3204n6_c': [46660], 'pe180226n3_c': [22946], 'pe1819Z140_c': [23364], 'pe1819Z160_c': [8614], 'pe1819Z1619Z_c': [8603], 'pe1819Z180_c': [8618], 'pail1601619Z_c': [42886], 'pe1819Z205n3_c': [8583], 'pail160205n3_c': [33116], 'pe1819Z226n3_c': [8581, 46522], 'pe205n3140_c': [23343], 'pe205n3160_c': [46691], 'pail1619Z160_c': [58096], 'pe205n31619Z_c': [46679], 'pe205n3180_c': [46695], 'pail1619Z205n3_c': [33104], 'pe205n31819Z_c': [46680], 'pail205n3160_c': [58078], 'pail205n31619Z_c': [42855], 'pe205n3226n3_c': [46501, 46658], 'pe226n3140_c': [23341], 'pail160182n6_c': [42807], 'pail1619Z182n6_c': [42795], 'pail182n6160_c': [425], 'pe226n3180_c': [46537], 'pail182n61619Z_c': [42874], 'pail182n6205n3_c': [33103], 'pail205n3182n6_c': [42776], 'pe140182n6_c': [8465], 'pe160182n6_c': [422], 'pe1619Z182n6_c': [8523], 'pe180182n6_c': [22967], 'pe182n6140_c': [23362], 'pe182n6160_c': [8456], 'pe182n61619Z_c': [8444], 'pe182n6180_c': [8460], 'pe182n61819Z_c': [8445], 'pe1819Z182n6_c': [8602], 'pe182n6205n3_c': [8425], 'pe182n6226n3_c': [8423, 46520], 'pe205n3182n6_c': [46678], 'pe140183n6_c': [52009], 'pe160183n6_c': [19910], 'pe1619Z183n6_c': [8509], 'pe180183n6_c': [22953], 'pe182n6183n6_c': [8430], 'pe1819Z183n6_c': [8588], 'pe205n3183n6_c': [46664], 'pe140183n3_c': [8307], 'pe160183n3_c': [19922], 'pe1619Z183n3_c': [8521], 'pe180183n3_c': [22965], 'pe182n6183n3_c': [8442], 'pe1819Z183n3_c': [8600], 'pe205n3183n3_c': [46676], 'pe140204n6_c': [46779], 'pe160204n6_c': [411], 'pe1619Z204n6_c': [8505], 'pe180204n6_c': [22949], 'pe182n6204n6_c': [8426], 'pe1819Z204n6_c': [8584], 'pgp1619Z160_h': [299485], 'pgp205n3160_h': [299465], 'pg1619Z160_h': [7229], 'pg205n3160_h': [54301], 'pg1601613E_h': [427, 316752, 317048, 674861, 675995, 677972, 679825, 682419, 685907, 688850, 694808, 695784, 697869, 698793, 698794], 'pg1619Z1613E_h': [7454, 316964, 317101, 673745], 'pg205n31613E_h': [7434, 316800, 317060, 683442], 'pc205n3162n4_c': [37082]}
lplantarum_model = read_sbml_model(r"Projeto\Pratica\modelos\iLB1027_lipid.xml")
check_annotation={}
founf=False
for metabolite in lplantarum_model.metabolites:
        side_chain=[]
        backbone=None
        matches = re.finditer("[0-9]+:[0-9]+(\([a-zA-Z0-9,]*\))*", metabolite.name)
        metabolite_name = metabolite.name
        found = False
        for match in matches:
            found = True
            annotation=metabolite.annotation.keys()
            annotated=False
            check_annotation[metabolite.id]=annotated
            if "slm" in annotation or "lipidmaps" in annotation:
                annotated=True
                check_annotation[metabolite.id]=annotated


annotations_before_implementation=list(check_annotation.values())
print(len(annotations_before_implementation))
print(annotations_before_implementation.count(True))
print((annotations_before_implementation.count(True)/len(annotations_before_implementation))*100)

for l in check_annotation.keys():
    if l in results.keys():
        check_annotation[l]=True

annotations_after_implementation=list(check_annotation.values())
print(annotations_after_implementation.count(True))
print((annotations_after_implementation.count(True)/len(annotations_after_implementation))*100)

# desvio padrao e media


listr = []

     
for value in results.values():
    listr.append(value)

for count, value in enumerate(listr):
        listr[count]=len(value)
        
data=pd.Series(listr)
print(data.describe())

# grafico
names = ['Annoted before implementation', 'Annoted after implementation']
values = [(annotations_before_implementation.count(True)/len(annotations_before_implementation))*100 , (annotations_after_implementation.count(True)/len(annotations_after_implementation))*100]

y_pos = np.arange(len(names))
plt.bar(y_pos, values)

# Create names on the x-axis
plt.xticks(y_pos, names)
plt.yticks(np.arange(0, 101, 10))
# Show graphic
plt.show()
