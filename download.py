#!/usr/bin/env python3
# credit to https://github.com/barronh/scrapenaq
import pandas as pd
import urllib.request
import re
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('startdate', help='Find ndjson.gz created >= startdate')
parser.add_argument('enddate', help='Find ndjson.gz created <= enddate')

args = parser.parse_args()

dates = pd.date_range(args.startdate, args.enddate)
keyre = re.compile('<Key>(.+?)</Key>')
BROOT = 'openaq-fetches.s3.amazonaws.com/'

for date in dates:
    xrpath = (
        'https://{}?delimiter=%2F&'.format(BROOT) +
        'prefix=realtime-gzipped%2F{}%2F'.format(date.strftime('%F'))
    )
    xmlpath = BROOT + date.strftime('realtime-gzipped/%F.xml')
    zippedpath = BROOT + date.strftime('realtime-gzipped/%F')
    
    os.makedirs(zippedpath, exist_ok=True)

    if os.path.exists(xmlpath):
        print('Keeping cached', xmlpath)
    else:
        urllib.request.urlretrieve(xrpath, xmlpath)

    xmltxt = open(xmlpath, mode='r').read()
    keys = keyre.findall(xmltxt)
    
    for key in keys:
        url = 'https://' + BROOT + key
        outpath = BROOT + key
        if os.path.exists(outpath):
            print('Keeping cached', outpath)
        else:
            urllib.request.urlretrieve(url, outpath)
