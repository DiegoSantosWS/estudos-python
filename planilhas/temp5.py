import gspread
from oauth2client.service_account import ServiceAccountCredentials

escopo = ['https://spreadsheets.google.com/feeds']
credenciais = ServiceAccountCredentials.from_json_keyfile_name('credenciais.json', escopo)
cliente = gspread.authorize(credenciais)

planilha = cliente.open("PlanilhaAulaPPT")
pasta_de_trabalho = planilha.sheet1

linha = ["15-05-2017", "Cliente teste", "01", "BRASIL", "90", "1212", "55555", "DALSDSKLAJD", "121212121121", "121212121DSD", "R$ 100.00", "SDASDASD", "KJSDKASJLD"]

indice = 8
pasta_de_trabalho.insert_row(linha, indice)