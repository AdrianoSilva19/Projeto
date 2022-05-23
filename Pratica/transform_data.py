from cmath import nan
import pandas as pd
from rdkit.Chem import PandasTools
import pendulum
import requests, zipfile, io
import numpy as np
from sqlalchemy import null

class LipidMapsExtractor():
    """
    Class to extract information from lipid maps
    """

    def extract(self, **kwargs):
        """
        This class calls the scrape_data method and creates a pandas dataframe with the scraped data.
        :return: pandas data frame of lipid maps data 
        """
        return self._extract(self.scrape_data())


    def _extract(self, raw) -> pd.DataFrame:
        """
        Method to create a pandas dataframe with the scraped data.
        :return: pandas data frame of lipid maps data 
        """
        raw=PandasTools.LoadSDF(raw)
        df=pd.DataFrame(raw)
        return df

    def scrape_data(self):
        """
        This class downloads the ZIP file and extracts the sdf file of lipid maps.
        :return: raw sdf file of lipid maps data
        """
        r = requests.get("https://www.lipidmaps.org/files/?file=LMSD&ext=sdf.zip")
        z = zipfile.ZipFile(io.BytesIO(r.content))
        return z.open('structures.sdf')  



class LipidMapsTransformer():

    def __init__(self) -> None:
        self.treated_dataframe=pd.DataFrame(columns=['LM_ID','ABBREVIATION','SYNONYMS'])

    def transform(self):
        """
        This method allows to transform the dataframe previously extracted into a desired datastructure
        :return:
        """
        data=LipidMapsExtractor()
        data_treated=self.treat(data.extract())
        return data_treated
    
    def three_col_lm(self,data_three):
        df_three_col=data_three[['LM_ID','ABBREVIATION','SYNONYMS']]
        return df_three_col

    def treat(self,data):
        df=self.three_col_lm(data)
        first_col=df[['LM_ID']].values
        second_col=df[['ABBREVIATION']].values
        third_col=df[['SYNONYMS']].values

        for n in range (50): #len(first_col)
            abrevs=second_col[n]
            synonyms=third_col[n]
            lista_ab=[]
            lista_sy=[]
            lista_id=[]
            if abrevs != None:
                for value in abrevs:
                    value=str(value)
                    value=value.split(';')
                    for i in value:
                        lista_ab.append(i)

            if synonyms != None:    
                for value in synonyms:
                    value=str(value)
                    value=value.split(';')
                    for i in value:
                        lista_sy.append(i)

            for a in range(max([len(lista_ab),len(lista_sy)])):
                for value in first_col[n]:
                    value=str(value)
                    lista_id.append(value)

            # pegar em cada linha e adicionar ao df
            treated_data=pd.DataFrame.from_dict({'LM_ID': lista_id, 'ABBREVIATION': lista_ab, 'SYNONYMS':lista_sy},orient='index').T
            #df.append(treated_data,ignore_index=True,)
            self.treated_dataframe=pd.concat([self.treated_dataframe,treated_data],ignore_index=True,sort=False,axis=0)
        
        return self.treated_dataframe



data=LipidMapsTransformer()
print(data.transform())