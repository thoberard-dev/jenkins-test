from oauth2client.service_account import ServiceAccountCredentials
# import pandas as pd
import json
from datetime import datetime
import time

# Functions
from Functions.sheets import post_sheet, get_sheet

# from Functions.admin import change_pickup, get_onelogin


# Config
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('Files/secret_create_store.json', scope)

id_sheet = '1b1qK9fkheK3fidS8NQjs5pf2K0GS8DvC6dlr5pSNecU'

df_stores = get_sheet(id_sheet, 'Store PICKUP To Create', creds)
df_stores_created = get_sheet(id_sheet, 'Store PICKUP Created', creds)
df_stores_errors = get_sheet(id_sheet, 'Store PICKUP Errors', creds)

# token = str(get_onelogin())
# print(token)
# token = 'eyJhbGciOiJSUzUxMiJ9.eyJpYXQiOjE2MDQ1Njg3NjMsImlzcyI6ImJhY2tlbmQiLCJleHAiOjE2MDQ1Njk5NjMsInBheWxvYWQiOiJ7XCJpZFwiOjE1MDI0NDAyLFwidG9rZW5UeXBlXCI6XCJQQVNTV09SRFwiLFwicm9sZVwiOlwiQUNDRVNTXCJ9IiwidmVyc2lvbiI6IlYxIiwianRpIjoiYTdmMjY1ODMtOThhZC00ZTNmLThkZmItMzJiMTY5YWNkODg1In0.h83ZXB10snElb-QkRsaqmvJqWd9iBuGYOfne9D8zQHD2FimnxBBBWDUX87LnQssZ7-8_xVTaeQOCFqrEEpOkkE36ZalI2cW5C8bCegvKredxKSUqWOBCmdvbbqK7VOGuwMUBjPkCkQlHEmbSh_4y2Ftxy5SqkJdNFugNL1OGBsF-RSetXWY0rTN24TVhnEdU2BmdE0lrc6fz-CfP8OZaKdc8KZnJSN8VsOX6U7R-eYZ5tbhBAB0OWNy58EEBSeZG7zUjML3FV2OuoupvT05VABzGiyB-_U-9EQGXaQBFkDBS30RAALBIqLTzJG5exY6Sb1OKYUCDvZPOh6S3U6z7hQ'

start_time = time.time()

for _, store in df_stores[df_stores['STORE ADDRESS ID'] != ''].iterrows():
    print(store['STORE ADDRESS ID'])

# elapsed_time = (time.time() - start_time) / 60
# if elapsed_time > 15:
#    token = str(get_onelogin())
#   start_time = time.time()
#  print(token)

    try:
        """if store['TYPE COMMISSION'] == 'PERCENTAGE':
            json_pickup = {"enabled": True,
                           "commissionFeeType": "PERCENTAGE",
                           "commissionFlatFeeCents": None,
                           "commissionFeePercentage": str(store['VALUE COMMISSION'])}
        else:
            json_pickup = {"enabled": True,
                           "commissionFeeType": "FLAT",
                           "commissionFlatFeeCents": str(store['VALUE COMMISSION']),
                           "commissionFeePercentage": None}"""

        # r_get_store, store_pickup = change_pickup(token, store['STORE ADDRESS ID'], json_pickup)
        # if r_get_store:   #eliminar probar
        df_stores_created = df_stores_created.append({'STORE ADDRESS ID': store['STORE ADDRESS ID'],
                                                      'VALUE': 2,
                                                      'CREATION DATE': datetime.today().__str__()},
                                                     ignore_index=True)
        post_sheet(id_sheet, 'Store PICKUP Created', creds, df_stores_created, False)
        time.sleep(0.55)
        """else:
            df_stores_errors = df_stores_errors.append({'STORE ID': store['STORE ID'],
                                                        'STORE ADDRESS ID': store['STORE ADDRESS ID'],
                                                        'ERROR': store_pickup,
                                                        'CREATION DATE': datetime.today().__str__()},
                                                       ignore_index=True)
            post_sheet(id_sheet, 'Store PICKUP Errors', creds, df_stores_errors, False)
            time.sleep(1.2)"""

    except Exception as exception:
        df_stores_errors = df_stores_errors.append({'STORE ADDRESS ID': store['STORE ADDRESS ID'],
                                                    'ERROR': exception,
                                                    'CREATION DATE': datetime.today().__str__()},
                                                   ignore_index=True)
        post_sheet(id_sheet, 'Store PICKUP Errors', creds, df_stores_errors, False)
        time.sleep(1.2)
