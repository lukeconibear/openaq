### Download OpenAQ data and convert to Pandas DataFrame

##### Requirements
- Bash
- Python environment with pandas and ndjson.  

##### Steps
- First download the data in .ndjson.gz format for a given date range (e.g. 1st Jan 2015 to 31st Dec 2015) using `python download.py 2015-01-01 2015-12-31`.  
- Convert the .ndjson.gz data to a Pandas DataFrame for a given year (e.g. 2015) using `python convert.py 2015`.  
