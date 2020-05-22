#!/usr/bin/env python3
import glob
import gzip
import ndjson
from pandas.io.json import json_normalize
import pandas as pd
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('year')
args = parser.parse_args()

year = args.year

path = '~' # change to this where the data is
files = glob.glob('openaq-fetches.s3.amazonaws.com/realtime-gzipped/' + year + '*/*')

df_list = []
for file in files:
    with gzip.open(file, 'rb') as ds:
        data_ndjson = ds.read()

    data_json = ndjson.loads(data_ndjson)

    df_list.append(json_normalize(data_json))
    
df = pd.concat(df_list, sort=False)

df.set_index('date.utc', inplace=True)
df.index = pd.to_datetime(df.index)

df.to_csv(path + 'openaq_data_' + year + '.csv')
