import gspread
from oauth2client.service_account import ServiceAccountCredentials
import re

escopo = ['https://spreadsheets.google.com/feeds']
credenciais = ServiceAccountCredentials.from_json_keyfile_name('credenciais.json', escopo)
cliente = gspread.authorize(credenciais)

planilha = cliente.open("PlanilhaAulaPPT").sheet1

data = re.compile(r'\d{2}-\d{2}-\d{2}')

celulas = planilha.findall(data)
for celula in celulas:
    print(f"valor: {celula.value}, linha {celula.row}, coluna {celula.col}")
