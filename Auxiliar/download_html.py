import requests

url = 'url'

response = requests.get(url)

if response.status_code == 200:
    html = response.text

    with open('codigo.html', 'w', encoding='utf-8') as file:
        file.write(html)

    print("Código HTML baixado e salvo como 'codigo.html'")
else:
    print(f"Falha ao obter a página. Código de status: {response.status_code}")
