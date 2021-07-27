
from requests.api import get
from covid_data_merger import get_api_response
from covid_data_merger import write_results

import os

date='2020-04-15'
iso='IND'
params='date='+date+'&'+'iso='+iso
output_path='test_responses.xlsx'

def test_response(tmp_path):
    df = get_api_response(date, iso, params)
    
    write_results(df,output_path)
    assert os.path.exists(output_path)
