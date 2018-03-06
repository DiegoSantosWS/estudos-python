import gspread
from oauth2client.service_account import ServiceAccountCredentials

escopo = ['https://spreadsheets.google.com/feeds']
credenciais = ServiceAccountCredentials.from_json_keyfile_name('credenciais.json', escopo)
cliente = gspread.authorize(credenciais)

planilha = cliente.open("PlanilhaAulaPPT")
pasta_de_trabalho = planilha.sheet1

lista_celulas = pasta_de_trabalho.range('C3:C7')
for celula in lista_celulas:
    celula.value = "TESTE DIEGO"

pasta_de_trabalho.update_cells(lista_celulas)