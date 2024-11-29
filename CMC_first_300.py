from requests import Request, Session
import requests
import json
import pprint
import datetime
import time
import os
from config import *

SLEEP_TIME = 0.2

## ==================================##
## setup config_cmc.py in the same folder
## ==================================##


# ## end of Config file



#===== Setup Date and Time #======== 
# Date
generation_date = datetime.datetime.now()
generation_date = generation_date.strftime("%d_%m_%Y")


# Time now
t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
#print(current_time)


#generation_time = now.strftime("%H:%M:%S")


# ======================== ### 
## Making the Call
# ======================== ### 

url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/historical"

parameters = {
    'limit':300
}

headers = {
    'X-CMC_PRO_API_KEY' : API_KEY,
    'Accept' : 'application/json'
}

response = requests.get(url, params=parameters, headers=headers)

data = response.json()

print(data)


# # #================================================
# ##### 
# #### Below is the Grouping and outputing function
# #####
# # # Group output from last Step
# # # to a list containing lists of n 
# ## requirement: symbols   ( a list )
# # # =============================================== ### 

# # Group size, in production n=400
# n=GROUP_SIZE

# def group_into_n(data_list, n):
#     return [data_list[i:i+n] for i in range(0, len(data_list), n)]

# #test = [1,2,3,4,5,6,7,8]
# #print(group_into_n(test, n))

# grouped_pairs = group_into_n(symbols, n)

# #print(grouped_pairs)


# #================================================
# # Step 5 #

# # write a function to output each of the group in step 4 
# # to a separate file
# # =============================================== ### 


# #def output_to_text_file(nested_grouped_pairs):
# #    for idx, group in enumerate(nested_grouped_pairs):
# #        with open(f'{idx+1}CMC p.{idx+1} {generation_date}.txt ', 'w') as f:
# #            for pair in group:
# #                f.write("%s,\n" % pair)


# # /Users/raysonkong/code/python/webscrapping/scripts_v2/cmc_api_to_tradingview/outputs
# def output_to_text_file(nested_grouped_pairs):
#     for idx, group in enumerate(nested_grouped_pairs):
#             filename=f"{os.getcwd()}/{EXCHANGE}_ALL_{generation_date}total{len(symbols)}/-0.4 {EXCHANGE}_ALL p.{idx+1} ({generation_date}).txt"
#             os.makedirs(os.path.dirname(filename), exist_ok=True)
#             with open(filename, "w") as f:
#                 for pair in group:
#                   f.write("%s,\n" % pair)

# #output_to_text_file(grouped_pairs)


# def run_srapper():
#     output_to_text_file(grouped_pairs)


#     print(f"== {EXCHANGE} All Tickers Retrieved ==")
#     print('\n')
#     #print("======================================================")
# if __name__ =='__main__':
#     run_srapper()

