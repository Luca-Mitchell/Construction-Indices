import requests
import pandas as pd
import os

def scrapeSpreadsheet(url : str) -> str:

    '''downloads most recent edition of Construction Output Price Indices from ONS website as 'data_[id].xlsx' in data folder and returns name of downloaded file'''

    response = requests.get(url)
    if response.status_code == 200:
        id = len(os.listdir('data'))
        with open(f'data/data_{id}.xlsx', 'wb') as f:
            f.write(response.content)
        return f'data_{id}.xlsx'
    else:
        print(f'ERROR: response status {response.status_code}')

def listify(dict : dict) -> list:

    '''converts dict of form {0 : data0, 1 : data1, 2 : data2, ...} to list of form [data0, data1, data2] and returns the list'''

    dictList = []
    for key, item in dict.items():
        dictList.append(item)
    return dictList

def extractData(file : str, sheet : str, columns : list[int], columnNames : list[str]) -> dict:

    '''extracts all numerical data from given columns and returns dict of form {columnName : [num1, num2, num3, ...], ...}'''

    df = pd.read_excel(f'data/{file}', sheet_name=sheet, header=None).to_dict()
    data = {}
    for i, columnNumber in enumerate(columns):
        data[columnNames[i]] = [x for x in listify(df[columnNumber]) if isinstance(x, (int, float)) and pd.notnull(x)]
    return data