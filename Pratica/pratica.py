from rdkit.Chem import PandasTools
import pandas as pd

#sl_lipids=pd.read_csv(r"C:\Users\ampsi\OneDrive\Ambiente de Trabalho\estruturas\swiss_lipids.csv",encoding="ISO-8859-1”)
lm_lipids=PandasTools.LoadSDF(r"C:\Users\ampsi\OneDrive\Ambiente de Trabalho\estruturas\lipid_maps.sdf")

#sl_lipids.info()
#lm_lipids.info()
#id=lm_lipids['LM_ID']
#abreviation=lm_lipids['ABBREVIATION']
#synonym=lm_lipids['SYNONYMS']
#print(f'id=\n{id} \n abbreviation=\n {abreviation}\n synonym=\n{synonym}')
df=pd.DataFrame(lm_lipids[['LM_ID','ABBREVIATION','SYNONYMS']])
df.to_csv(r'C:\Users\ampsi\OneDrive\Ambiente de Trabalho\projeto\Projeto\Pratica\lipid_maps.csv', index=None)