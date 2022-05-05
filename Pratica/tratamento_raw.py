from rdkit.Chem import PandasTools
import pandas as pd
import gzip
import requests, zipfile, io

# LIPID MAPS

def scrape_data():
    '''
    This class downloads the ZIP file and extracts the CSV files of lipid maps to a temporary folder.
    :return:
    '''
    r = requests.get("https://www.lipidmaps.org/files/?file=LMSD&ext=sdf.zip")
    z = zipfile.ZipFile(io.BytesIO(r.content))
    
    return z.open('structures.sdf')  


def _extract() -> pd.DataFrame:
    """
    #Method to create a pandas dataframe with the scraped data.
    #:return:
    """
    raw=PandasTools.LoadSDF(scrape_data())
    df=pd.DataFrame(raw)
    df.to_csv('C:\\Users\\ampsi\\OneDrive\\Ambiente de Trabalho\\projeto\\Projeto\\Pratica\\lm_whole_db.csv',index=None)
    return df
    


_extract()

#-----------------------------------------------------------------------------------#

# SWISS LIPIDS


def scrape_data_sl():
    """
    This class downloads the ZIP file and extracts the CSV files of lipid maps to a temporary folder.
    :return:
    """
    r = requests.get("https://www.swisslipids.org/api/file.php?cas=download_files&file=lipids.tsv")
    z = gzip.open(io.BytesIO(r.content),'rb')
    return z
    
     


def _extract_sl() -> pd.DataFrame:
    """
    Method to create a pandas dataframe with the scraped data.
    :return:
    """
    raw= pd.read_table(scrape_data_sl(),engine='python',encoding='ISO-8859-1')
    df=pd.DataFrame(raw)
    df.to_csv('C:\\Users\\ampsi\\OneDrive\\Ambiente de Trabalho\\projeto\\Projeto\\Pratica\\sl_whole_db.csv',index=None)
    return df

_extract_sl()

