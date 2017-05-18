import zipfile
import requests
import io
import os
import urlopen

przystanki = urlopen('http://geoportal.wroclaw.pl/www/pliki/KomunikacjaZbiorowa/SlupkiWspolrzedne.txt')
data = przystanki.read()
txt_str = str(data)
lines = txt_str.split("\\n")

r = requests.get('http://www.wroclaw.pl/open-data/opendata/rozklady/OtwartyWroclaw_rozklad_jazdy_GTFS.zip')
z = zipfile.ZipFile(io.BytesIO(r.content))

des_url = 'C:\\Users\\Public\\PYTHON'
if os.path.exists(des_url) :
    #TODO:porownaj
    print("check")
else:
    directory = os.path.dirname(des_url)
    os.mkdir(directory)
    z.extract(des_url)
    
    fx = open(des_url, "w")
    for line in lines:
        fx.write(line + "\n")
    fx.close()
    
#     TODO:
# Traceback (most recent call last):
# 200
#   File "C:/Users/Mona/Desktop/pythonowate/omega-wroclaw-dev-mine-positions/miners/update.py", line 7, in <module>
#     przystanki = urlopen('http://geoportal.wroclaw.pl/www/pliki/KomunikacjaZbiorowa/SlupkiWspolrzedne.txt')
# TypeError: 'module' object is not callable
