import requests
import csv

spreadsheet_url = 'url'

response = requests.get(spreadsheet_url)

if response.status_code == 200:
    csv_data = response.text

    with open('dados_da_planilha.csv', 'w', newline='', encoding='utf-8') as csvfile:
        csvfile.write(csv_data)
    print("Dados da planilha foram baixados como 'dados_da_planilha.csv'")
else:
    print("Erro ao acessar a planilha:", response.status_code)
