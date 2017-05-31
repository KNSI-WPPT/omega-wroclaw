import zipfile
import requests
import io
import os

przystanki=requests.get('http://geoportal.wroclaw.pl/www/pliki/KomunikacjaZbiorowa/SlupkiWspolrzedne.txt')
przystanki=przystanki.text

r = requests.get('http://www.wroclaw.pl/open-data/opendata/rozklady/OtwartyWroclaw_rozklad_jazdy_GTFS.zip')
z = zipfile.ZipFile(io.BytesIO(r.content))

des_url = 'C:\\Users\\Public\\PYTHON'
filename = "C:\\Users\\Public\\PYTHON\\przystanki.txt"
if os.path.exists(des_url):
    
    with open(filename, "w") as f:
        f.write(przystanki)
    z.extractall(des_url) #uwaga

else:
    directory = os.path.dirname(des_url)
    os.mkdir(directory)
    z.extractall(des_url)

    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w") as f:
        f.write(przystanki)
