#!/usr/bin/python3
# python3 ./facebook_ads_accounts.py

import sys
import requests
import json
import datetime
import os
from dotenv import load_dotenv
load_dotenv()

def get_facebook_ads_account(access_token,api_version):
    try:
        # url = f'''https://graph.facebook.com/{api_version}/me/adaccounts?
        # fields=id,name,account_id,currency,timezone_id, email&access_token={access_token}'''

        url = f'''https://graph.facebook.com/{api_version}/me/businesses?
        fields=id,name,account_id,currency,timezone_id&access_token={access_token}'''

        headers = {}

        r = requests.get(url = url, headers = headers)
        fb_ads_account_data = r.json()

        #print(fb_ads_account_data)
        fb_ads_accounts = fb_ads_account_data['data']
        
        for fb_ads_account in fb_ads_accounts:
            print("\n fb_ads_account -> ",fb_ads_account)

        return fb_ads_accounts
    except:
        print("\nFunction (get_facebook_ads_account) Failed",sys.exc_info())


if __name__ == '__main__':
    try:
        timestamp = datetime.datetime.strftime(datetime.datetime.now(),'%Y-%m-%d : %H:%M')
        print("DATE : ",timestamp,"\n")
        print("\n Process start")


        access_token = os.getenv("ACCESS_TOKEN")
        api_version = os.getenv("API_VERSION")

        accounts_details = get_facebook_ads_account(access_token, api_version)
        print("\n Account Details :\n",accounts_details)

        print("\n Process End \n")
    except:
        print("\n Process Failed !! ", sys.exc_info())
