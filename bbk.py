import requests
from bs4 import BeautifulSoup
import pandas

page = requests.get('https://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Palembang&AreaID=501568&Prov=35')
page = BeautifulSoup(page.content, 'html.parser')
data = []

inti1 = page.find(class_='prakicu-kabkota tab-v1 margin-bottom-30').find(id='TabPaneCuaca1').find_all(class_='cuaca-flex-child')

for i in inti1:
    waktu = [i.find(class_='kota').get_text()]
    cuaca = [i.find(class_='kiri').find('p').get_text()]
    waktu = [i.find(class_='kota').find('')]

    data.append({
        'jam':waktu,
        'cuaca':cuaca,
    })

data_selesai = pandas.DataFrame(data)
print(data_selesai)
