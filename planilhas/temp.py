import gspread
from oauth2client.service_account import ServiceAccountCredentials

escopo = ['https://spreadsheets.google.com/feeds']
credenciais = ServiceAccountCredentials.from_json_keyfile_name('credenciais.json', escopo)
cliente = gspread.authorize(credenciais)

planilha = cliente.open("PlanilhaAulaPPT")
pasta_de_trabalho = planilha.sheet1
lista_registros = pasta_de_trabalho.get_all_records()

print(f"Lista com todos registros: {lista_registros}")

lista_valores = pasta_de_trabalho.get_all_values()
print(f"Lista de valores: {lista_valores}")
