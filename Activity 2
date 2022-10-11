import requests
import json
import pandas as pd
import warnings
warnings.simplefilter("ignore")

website="http://gateway.marvel.com/v1/public/characters"

headers = {"Content-Type": "application/json; charset=utf-8"}
param={'ts':2,'apikey': '4eaeca831e75837712eaef3a1d4a1563','hash':'052a323c7c22a78965492fa15116c906',
        'nameStartsWith':'bat','limit':10}
response=requests.get(website,headers=headers,params=param, verify=False)

response.raise_for_status
res=response.json()

result=res['data']['results']

marvel=pd.DataFrame(columns=['Name','id', 'comics','series','stories','event'])
marvel2=pd.DataFrame(columns=['Name'])

for i in range(len(result)):
    name=result[i]['name']
    char_id=result[i]['id']
    comic_available= result[i]['comics']['available']
    series_available= result[i]['series']['available']
    stories_available= result[i]['stories']['available']
    event_available= result[i]['events']['available']
    sample_dic={'Name':name,'id':char_id,'comics':comic_available,'series':series_available,'stories':stories_available,'event':event_available}
    marvel=marvel.append(sample_dic,ignore_index=True)

##print(marvel)

##All alphabets and Digits
for i in range(97,123):
    param2={'ts':2,'apikey':'4eaeca831e75837712eaef3a1d4a1563','hash':'052a323c7c22a78965492fa15116c906','nameStartsWith':chr(i),'limit':100}
    response2=requests.get(website,headers=headers,params=param2,verify=False)
    response2.raise_for_status
    res2=response2.json()
    result2=res2['data']['results']
    for i in range(len(result2)):
        name=result2[i]['name']
        sample_dic2={'Name':name}
        marvel2=marvel2.append(sample_dic2,ignore_index=True)

print('Size of dataframe with all charaters is:',marvel2.shape[0])
