from operator import index
import pandas as pd
import re


def three_col_lm():
    df=pd.read_csv(r'C:\Users\ampsi\OneDrive\Ambiente de Trabalho\projeto\Projeto\Pratica\sl_treated.csv')
    df=df[['Lipid ID','Abbreviation*','Synonyms*']]
    return df

def treat(df):
    first_col=df[['Lipid ID']].values
    second_col=df[['Abbreviation*']].values
    third_col=df[['Synonyms*']].values
    df=pd.DataFrame(columns=['Lipid ID','Abbreviation*','Synonyms*'])
    l_ab=[]
    l_syn=[]
    l_id=[]

    for n in range (50):
        data=pd.DataFrame(columns=['Lipid ID','Abbreviation*','Synonyms*'])
        abrevs=second_col[n]
        synonyms=third_col[n]
        id=[]
        lista_ab=[]
        lista_sy=[]
        lista_id=[]
        if abrevs != None:
            for value in abrevs:
                value=str(value)
                value=value.split('|')
                for i in value:
                    lista_ab.append(''.join(i))

        if synonyms != None:    
            for value in synonyms:
                value=str(value)
                value=value.split('|')
                for i in value:
                    lista_sy.append(''.join(i))

        for a in range(max([len(lista_ab),len(lista_sy)])):
            for value in first_col[n]:
                value=str(value)
                lista_id.append(''.join(value))
      
        treated_data=pd.DataFrame.from_dict({'Lipid ID': lista_id, 'Abbreviation*': lista_ab, 'Synonym*':lista_sy},orient='index').T
        #df.append(treated_data,ignore_index=True,)
        print(treated_data)
        pd.concat([df,treated_data],ignore_index=True,sort=False)
        
    return df
        # pegar em cada linha e adicionar ao df


print(treat(three_col_lm()))