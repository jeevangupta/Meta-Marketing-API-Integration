#!/usr/local/bin/python3
#  python3 ./fb_main.py -s 2022-06-26 -e 2022-06-26
import getopt
import sys
from datetime import datetime, timedelta
import json
import time
import os
from dotenv import load_dotenv
load_dotenv()

from get_fb_campaign_data import *


def readfile(argv):
    global from_date
    global to_date
    try:
        opts, args = getopt.getopt(argv,"s:e:")
    except getopt.GetoptError:
        usage()
    for opt, arg in opts:
        if opt == '-s':
            from_date = arg
        elif opt == '-e':
            to_date = arg
        else:
            print("Invalid Option in command line")



if __name__ == '__main__':
    try:
        timestamp = datetime.strftime(datetime.now(),'%Y-%m-%d : %H:%M')
        print("DATE : ",timestamp,"\n")
        print("\n Process start")
        readfile(sys.argv[1:])

        access_token = os.getenv("ACCESS_TOKEN")
        account_id = os.getenv("ACCOUNT_ID")
        api_version = os.getenv("API_VERSION")
        

        campaign_list = get_campaign_list_graphQL(access_token, account_id, api_version)
        print("\n campaign_list : \n",campaign_list)
        print("\n number of campaign_list : ", len(campaign_list))

        campaign_analytics = get_campaign_analytics(access_token, api_version, campaign_list, from_date,to_date)
        print("\n campaigns analytics :\n",campaign_analytics)
         
        print("\n Process End \n")
    except:
        print("\n Process Failed !! ", sys.exc_info())
