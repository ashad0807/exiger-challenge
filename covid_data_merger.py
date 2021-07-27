import os
import pandas as pd
from configparser import ConfigParser
from pandas.core.algorithms import mode
import requests
from collections import defaultdict
import logging
from openpyxl import load_workbook


logging.basicConfig(level=logging.INFO)

URL = 'https://covid-api.com/api/reports?'

def append_df_to_excel(df, excel_path):
    df_excel = pd.read_excel(excel_path)
    result = pd.concat([df_excel, df], ignore_index=True)
    result.to_excel(excel_path, index=False)


def assert_data_fields(data):
    assert 'region' in data, 'No regions found in response data'
    assert 'iso' in data['region'], 'No iso found in response data'
    assert 'confirmed' in data, 'No confirmed found in response data'
    assert 'deaths' in data, 'No deaths found in response data'
    assert 'recovered' in data, 'No recovered found  in response data'

def merge_data_result(result_data):
    merged = defaultdict(dict)
    for d in result_data:
        assert_data_fields(d)
        date = d['date']
        iso = d['region']['iso']
        k = (date, iso)         #Make a combination key of date and iso 
        temp = merged[k]
        temp['date'] = date
        temp['iso'] = iso
        for src in ('confirmed', 'deaths', 'recovered'):
            tgt = f'num_{src}'
            temp[tgt] = temp.get(tgt, 0) + d[src]
    return merged


def get_api_response(date, iso, params):

    # sending get request and saving the response as response object
    logging.info(f"***Query with -> {params}")
    params_temp = params[0]
    r = requests.get(url = URL, params = params)
        # if r.status_code != 200:
        #     raise HTTPReturnCodeException(r.status_code)
    json_result = r.json()

    downloaded = defaultdict(dict)
    # extracting data in json format
    merged_data= merge_data_result(json_result.get('data'))

    d = dict(merged_data[date,iso])
    df = pd.DataFrame([d], columns = d.keys())

    print("results df",df)
    return df

def read_config(config_path):
    config = ConfigParser()
    with open(config_path) as f:
        config.read_file(f)
        results_file_path = config['paths']['results_file_path']
        input_xls_path = config['paths']['input_xls_path']
    return results_file_path, input_xls_path

#Start here
# Read input config file to get the XLS file path which has actual input data

results_file_path, input_xls_path = read_config('config.ini')
data = pd.read_excel(input_xls_path)
input_xls = pd.DataFrame(data)

print("rsults path", results_file_path)
print("input",input_xls_path)
print("input df", input_xls)

for i, row in input_xls.iterrows():
    # Construct query parameter string
    queryparams = row.index[0].lower()+"="+row[row.index[0]].strftime('%Y-%m-%d')+"&"+row.index[1].lower()+"="+row[row.index[1]]
    date= row[row.index[0]].strftime('%Y-%m-%d')
    iso = row[row.index[1]]
    resp_df = get_api_response(date,iso,queryparams)

    if not os.path.isfile(results_file_path):
        resp_df.to_excel(results_file_path)
    else:
        append_df_to_excel(resp_df, results_file_path)





