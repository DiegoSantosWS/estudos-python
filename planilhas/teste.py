import gspread
from oauth2client.service_account import ServiceAccountCredentials

escopo = ['https://spreadsheets.google.com/feeds']
credenciais = ServiceAccountCredentials.from_json_keyfile_name('credenciais.json', escopo)
cliente = gspread.authorize(credenciais)