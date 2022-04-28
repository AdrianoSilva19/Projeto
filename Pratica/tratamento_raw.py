from rdkit.Chem import PandasTools
import pandas as pd

sl_raw=pd.read_table(r"C:\Users\ampsi\OneDrive\Ambiente de Trabalho\estruturas\swiss_lipids.txt",low_memory=False)
lm_raw=PandasTools.LoadSDF(r"C:\Users\ampsi\OneDrive\Ambiente de Trabalho\estruturas\lipid_maps.sdf")

def tratamento_raw_lm(dataset):
    dataset.info()    
    df=pd.DataFrame(dataset[['LM_ID','ABBREVIATION','SYNONYMS']])
    df.to_csv('C:\\Users\\ampsi\\OneDrive\\Ambiente de Trabalho\\projeto\\Projeto\\Pratica\\lm_treated.csv', index=None)

def tratamento_raw_sl(dataset):
    dataset.info()
    df=pd.DataFrame(dataset[['Lipid ID','Abbreviation*','Synonyms*']])
    df.to_csv('C:\\Users\\ampsi\\OneDrive\\Ambiente de Trabalho\\projeto\\Projeto\\Pratica\\sl_treated.csv', index=None)


def teste():
    sl_raw=pd.read_table(r"C:\Users\ampsi\OneDrive\Ambiente de Trabalho\estruturas\swiss_lipids.txt",low_memory=False)
    lm_raw=PandasTools.LoadSDF(r"C:\Users\ampsi\OneDrive\Ambiente de Trabalho\estruturas\lipid_maps.sdf")
    tratamento_raw_lm(lm_raw)
    tratamento_raw_sl(sl_raw)

teste()

