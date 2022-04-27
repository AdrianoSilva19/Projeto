from rdkit.Chem import PandasTools
import pandas as pd

#sl_lipids=pd.read_table(r"C:\Users\ampsi\OneDrive\Ambiente de Trabalho\estruturas\swiss_lipids.tsv",encoding='iso-8859-1')
lm_lipids=PandasTools.LoadSDF(r"C:\Users\ampsi\OneDrive\Ambiente de Trabalho\estruturas\lipid_maps.sdf") #abbreviation

lm_lipids.info()
print(lm_lipids[['ABBREVIATION','SYNONYMS']])