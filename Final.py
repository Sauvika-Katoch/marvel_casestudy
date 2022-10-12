import requests
import json
import pandas as pd
import warnings
warnings.simplefilter("ignore")
import argparse 
from CharExtractor.functions import func
f =func()

parser = argparse.ArgumentParser()  

parser.add_argument("apikey", help = "Public API Key")  
parser.add_argument("hash", help = "Hash value of ts+private key+ public key")  
args = parser.parse_args()

apikey_new=args.apikey
hash_new=args.hash

marvel_new=f.newfunc('s',apikey_new, hash_new)

marvel_new['comics']=marvel_new['comics'].astype(int)
marvel_new['id']=marvel_new['id'].astype(int)
marvel_new['series']=marvel_new['series'].astype(int)
marvel_new['stories']=marvel_new['stories'].astype(int)
marvel_new['event']=marvel_new['event'].astype(int)


filtered_dataframe=print(f.filtered_value(marvel_new, 'series', '>', 50))

