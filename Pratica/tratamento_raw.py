from rdkit.Chem import PandasTools
import pandas as pd
import gzip
import requests, zipfile, io

# LIPID MAPS

def extract():
    """
    This class calls the scrape_data method and creates a pandas dataframe with the scraped data.
    :return:
    """
    df=_extract(scrape_data())
    return df

def _extract(raw) -> pd.DataFrame:
    """
    Method to create a pandas dataframe with the scraped data.
    :return:
    """
    raw=PandasTools.LoadSDF(raw)
    df=pd.DataFrame(raw)
    print(df.head())
    return df

def scrape_data():
    """
    This class downloads the ZIP file and extracts the CSV files of lipid maps to a temporary folder.
    :return:
    """
    r = requests.get("https://www.lipidmaps.org/files/?file=LMSD&ext=sdf.zip")
    z = zipfile.ZipFile(io.BytesIO(r.content))

    return z.open('structures.sdf')
def transform(df):
    data=df[['LM_ID','ABBREVIATION','SYNONYMS']]
    return data

transform(extract())

#-----------------------------------------------------------------------------------#

# SWISS LIPIDS
'''
def scrape_data_sl():
    
    #This class downloads the ZIP file and extracts the CSV files of lipid maps to a temporary folder.
    #:return:
    
    r = requests.get("https://www.swisslipids.org/api/file.php?cas=download_files&file=lipids.tsv")
    z = gzip.open(io.BytesIO(r.content),'rb')
    return z
    
     


def _extract_sl() -> pd.DataFrame:
    
    #Method to create a pandas dataframe with the scraped data.
    #:return:
    
    raw= pd.read_table(scrape_data_sl(),engine='python',encoding='ISO-8859-1')
    df=pd.DataFrame(raw)
    print(df.head())
    return df

_extract_sl()
'''