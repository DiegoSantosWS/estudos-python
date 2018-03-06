import gspread
from oauth2client.service_account import ServiceAccountCredentials
import re

escopo = ['https://spreadsheets.google.com/feeds']
credenciais = ServiceAccountCredentials.from_json_keyfile_name('credenciais.json', escopo)
cliente = gspread.authorize(credenciais)

planilha = cliente.open("PlanilhaAulaPPT")
#pasta_de_trabalho = planilha.worksheet("Minha Planilha")
#planilha.del_worksheet(pasta_de_trabalho)
pasta_de_trabalho = planilha.worksheet("Página2")
planilha.del_worksheet(pasta_de_trabalho)