import requests
import json
import pandas as pd

class func:

    def filtered_value(self, df, column, operator, value):
        if(operator=='>'):
            a= lambda df,column, val: df[df[column]>val]
            x= a(df,column,value)
        elif(operator=='<'):
            a= lambda df,column, val: df[df[column]<val]
            x= a(df,column,value)
        elif (operator=='='):
            a= lambda df,column, val: df[df[column]==val]
            x= a(df,column,value)
        return x
        
    def newfunc(self, startchar,apikey='NULL',hash='NULL'):
        if(apikey=='NULL' or hash=='NULL'):
            raise Exception("Api key or hash key not provided")
        else:
            website="http://gateway.marvel.com/v1/public/characters"
            headers = {"Content-Type": "application/json; charset=utf-8"}
            param={'ts':2,'apikey':apikey,'hash':hash,'nameStartsWith':startchar}
            response=requests.get(website,headers=headers,params=param, verify=False)
            response.raise_for_status
            res=response.json()
            result=res['data']['results']
        
            marvel=pd.DataFrame(columns=['Name','id', 'comics','series','stories','event'])
            for i in range(len(result)):
                name=result[i]['name']
                char_id=result[i]['id']
                comic_available= result[i]['comics']['available']
                series_available= result[i]['series']['available']
                stories_available= result[i]['stories']['available']
                event_available= result[i]['events']['available']
                sample_dic={'Name':name,'id':char_id,'comics':comic_available,'series':series_available,'stories':stories_available,'event':event_available}
                marvel=marvel.append(sample_dic,ignore_index=True)
            
        return marvel
