from bs4 import BeautifulSoup
import requests
import pandas as pd

html = requests.get("https://www.tiobe.com/tiobe-index/").text

soap = BeautifulSoup(html, 'html5lib')

h2 = soap.find('h2')

print(h2.text)

table = soap.find_all('table', {'id':'top20'})

posicao, linguagem = [], []

for i in table:
    tr = i.findChildren("tr")
    for j in tr:
        tds = j.findChildren("td")
        count = 0
        for td in tds:
            if(count == 0):
                posicao.append(td.text)
            if (count == 4):
                linguagem.append(td.text)
            count = count + 1

df = pd.DataFrame({'Posição no Ranking': posicao, 'Nome da Linguagem': linguagem})
print(df)

df.to_excel(h2.text + '.xlsx', index=False)