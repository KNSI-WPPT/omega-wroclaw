import zipfile
import requests
import io
import os
from urllib.request import urlopen
import filecmp

przystanki = urlopen('http://geoportal.wroclaw.pl/www/pliki/KomunikacjaZbiorowa/SlupkiWspolrzedne.txt')
data = przystanki.read()

r = requests.get('http://www.wroclaw.pl/open-data/opendata/rozklady/OtwartyWroclaw_rozklad_jazdy_GTFS.zip')
z = zipfile.ZipFile(io.BytesIO(r.content))

des_url = 'C:\\Users\\Public\\PYTHON'
if os.path.exists(des_url):
    filecmp.clear_cache()
    check=filecmp.cmp("C:\\Users\\Public\\PYTHON\\przystanki.txt", data, shallow=False)
    if check:
        print("the same")
    else:
        filename = "C:\\Users\\Public\\PYTHON\\przystanki.txt"
        with open(filename, "r+") as f:
            f.seek(0)
            f.write(data)
    z.extractall(des_url) #uwaga

    print("check")
else:
    directory = os.path.dirname(des_url)
    os.mkdir(directory)
    z.extractall(des_url)

    filename = "C:\\Users\\Public\\PYTHON\\przystanki.txt"
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w") as f:
        f.write(data)
