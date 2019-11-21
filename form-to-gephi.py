import gspread
from oauth2client.service_account import ServiceAccountCredentials
from nlp_to_net import start_nlp, draw_nodes
import time


scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('form-to-gephi-e2ab2e110481.json', scope)

gc = gspread.authorize(credentials)

wks = gc.open("New test form (Responses)").sheet1

global_nlp = start_nlp()

# Keep track of old responses
old = []

while True:
    sheet_values = wks.get_all_values()

    # We only want the question column
    fresh = [lst[1] for lst in sheet_values[1:]]

    # We only want to send the new values to gephi
    to_gephi = [text for text in fresh if text not in old]
    for text in to_gephi:
        draw_nodes(text=text, nlp=global_nlp)
    old = fresh
    time.sleep(2)
