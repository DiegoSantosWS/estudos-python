import gspread
from oauth2client.service_account import ServiceAccountCredentials

escopo = ['https://spreadsheets.google.com/feeds']
credenciais = ServiceAccountCredentials.from_json_keyfile_name('credenciais.json', escopo)
cliente = gspread.authorize(credenciais)

planilha = cliente.open("PlanilhaAulaPPT")
pasta_de_trabalho = planilha.sheet1

print(f"Celula da linha 4, coluna 5: {pasta_de_trabalho.cell(4,5).value}")
print(f"Celula B5: {pasta_de_trabalho.acell('B5').value}")