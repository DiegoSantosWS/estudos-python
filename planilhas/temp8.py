import gspread
from oauth2client.service_account import ServiceAccountCredentials
import re

escopo = ['https://spreadsheets.google.com/feeds']
credenciais = ServiceAccountCredentials.from_json_keyfile_name('credenciais.json', escopo)
cliente = gspread.authorize(credenciais)

planilha = cliente.open("PlanilhaAulaPPT").sheet1

print(f"qtd linha: {planilha.row_count}")
planilha.delete_row(8)
print(f"qtd linha: {planilha.row_count}")