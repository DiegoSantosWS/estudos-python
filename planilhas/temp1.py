import gspread
from oauth2client.service_account import ServiceAccountCredentials

escopo = ['https://spreadsheets.google.com/feeds']
credenciais = ServiceAccountCredentials.from_json_keyfile_name('credenciais.json', escopo)
cliente = gspread.authorize(credenciais)

planilha = cliente.open("PlanilhaAulaPPT")
pasta_de_trabalho = planilha.sheet1

print(f"Linha 1: {pasta_de_trabalho.row_values(1)}")
print()
print(f"Linha 2: {pasta_de_trabalho.row_values(2)}")
print()
print(f"Linha 3: {pasta_de_trabalho.row_values(3)}")
##PEGANDO CONTEUDO DA COLUNA A
print()
print(f"Coluna A (1): {pasta_de_trabalho.col_values(1)}")