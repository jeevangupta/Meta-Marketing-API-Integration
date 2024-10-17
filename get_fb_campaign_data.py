#!/usr/bin/python3
import sys
import pandas as pd
from datetime import datetime, timedelta
import requests
import json


def get_campaign_list_graphQL(access_token, account_id, api_version):
    try:
        url =  f"https://graph.facebook.com/{api_version}/act_{account_id}/campaigns?"

        fields=['id','name','account_id','start_time','updated_time','status']

        headers = {}

        payload = {
            'limit':100,
            'fields':fields,
            'access_token': access_token
        }
        
        result = requests.get(url, params=payload, headers = headers)
        response = result.json()

        campaign_list = []

        if result.status_code == 200:
            campaigns = response['data']

            for campaign in campaigns:
                if not campaign["status"] in ["DELETED", "ARCHIVED"]:
                    campaign_list.append(dict(campaign))
        
        campaign_data_df = pd.DataFrame.from_records(campaign_list)


        return campaign_data_df
    except:
        print(f"\n !! Function get_campaign_list_graphQL Failed !! Error: {sys.exc_info()}")


def get_campaign_analytics(access_token, api_version, campaign_ids, start_date,end_date):
    try:

        fields =['account_id','account_name','campaign_name','campaign_id',
                'impressions','clicks','spend','conversions','cpm','cpc',
                'created_time','date_start','date_stop','action_values','actions','inline_link_clicks']
        
        payload = {
            "access_token": access_token,
            "fields": fields,
            "time_range": f'{{"since": "{start_date}", "until": "{end_date}"}}',
            "time_increment": "1",
            "limit": "500"}
        
        campaign_analytics_data = pd.DataFrame()
        campaign_data = []
        for campaign_id in campaign_ids:

            url =  f"https://graph.facebook.com/{api_version}/{campaign_id}/insights?"
            
            headers = {}
            result = requests.get(url, params=payload, headers = headers)
            
            if result.status_code == 200:
                response = result.json()
                if len(response['data']) > 0:
                    campaign = response['data'][0]
                    campaign_data.append(campaign)
            else:
                print(f" ** Something went wrong | function -> get_campaign_analytics | message: {result.json()}")
        
        campaign_analytics_data = pd.DataFrame.from_records(campaign_data)
        return campaign_analytics_data
    except:
        print(f"\n !! Function get_campaign_analytics Failed !! Error: {sys.exc_info()}")

      