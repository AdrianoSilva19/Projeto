from rdkit.Chem import PandasTools
import pandas as pd

sl_raw=pd.read_table(r"C:\Users\ampsi\OneDrive\Ambiente de Trabalho\estruturas\swiss_lipids.txt",low_memory=False)
lm_raw=PandasTools.LoadSDF(r"C:\Users\ampsi\OneDrive\Ambiente de Trabalho\estruturas\lipid_maps.sdf")

#sl_lipids.info()
#lm_lipids.info()
#df=pd.DataFrame(lm_lipids[['LM_ID','ABBREVIATION','SYNONYMS']])
#df.to_csv(r'C:\Users\ampsi\OneDrive\Ambiente de Trabalho\projeto\Projeto\Pratica\lipid_maps.csv', index=None)

def tratamento_raw_lm(dataset):
    dataset.info()    
    df=dataset[['LM_ID','ABBREVIATION','SYNONYMS']]
    df.to_csv('C:\\Users\\ampsi\\OneDrive\\Ambiente de Trabalho\\projeto\\Projeto\\Pratica\\lm_treated.csv', index=None)

def tratamento_raw_sl(dataset):
    dataset.info()
    df=dataset[['Lipid ID','Abbreviation*','Synonyms*']]
    df.to_csv('C:\\Users\\ampsi\\OneDrive\\Ambiente de Trabalho\\projeto\\Projeto\\Pratica\\sl_treated.csv', index=None)


def teste():
    tratamento_raw_lm(lm_raw)
    tratamento_raw_sl(sl_raw)

teste()

