import requests
from bs4 import BeautifulSoup


#Coletando o HTML com Requests:

url = 'https://www.vivareal.com.br/aluguel/minas-gerais/pocos-de-caldas/apartamento_residencial/?pagina=2#onde=Brasil,Minas%20Gerais,Poços%20de%20Caldas,,,,,,BR>Minas%20Gerais>NULL>Pocos%20de%20Caldas,,,&preco-ate=1400'
response = requests.get(url)

if response.status_code == 200:
    html = response.text
else:
    print(f'Erro: {response.status_code}')

#Coletando as informações necessárias com BeautifulSoup4:

soup = BeautifulSoup(html, 'html.parser')

apartments = soup.find_all(lambda tag: tag.name == 'div' and 'data-type' in tag.attrs and tag['data-type'] == 'property')
print(apartments)

for div in apartments:
    print(div.text)

#print(apartments)