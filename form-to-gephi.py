import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import time


scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('form-to-gephi ... .json', scope)

gc = gspread.authorize(credentials)

wks = gc.open("Some form (Responses)").sheet1

old = []
while True:
    sheet_values = wks.get_all_values()
    fresh = [lst[1] for lst in sheet_values[1:]]
    to_gephi = [text for text in fresh if text not in old]
    print(to_gephi)
    old = fresh
    time.sleep(10)
