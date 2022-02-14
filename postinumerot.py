# Kopioi aikaisempi ratkaisusi tänne. Lisää tarvittaessa myös muut ratkaisusi tiedostot.
# Esimerkkisuoritus:
#
# Kirjoita postitoimipaikka: Porvoo
# Postinumerot: 06100, 06101, 06150, 06151, 06200, 06400, 06401, 06450, 06500
import json
from typing import Optional

with open('postinumerot.json') as f:
        tiedoston_sisalto = f.read()


def get_postal_numbers(code: str) -> Optional[str]:
    data = json.loads(tiedoston_sisalto)

    postinumerot = []
    arvo = ''

    if code in data.values():
        for key, value in data.items():
            if code == value:
                postinumerot.append(key)
        arvo = ''.join(map(str, postinumerot))
        return arvo
    else:
        return None


if __name__ == '__main__':

    data = json.loads(tiedoston_sisalto)

    postitoimipaikka = input('Kirjoita postitoimipaikka: ').upper()
    postinumerot = []

    if postitoimipaikka == 'SMART POST':
        postitoimipaikka.replace('SMART POST', 'SMARTPOST')

    viesti = ''

    for key, value in data.items():
        if postitoimipaikka.replace(" ", "") == value.replace(" ", ""):
            postinumerot.append(key)

    if not postinumerot:
      print('Tuntematon postitoimipaikka')
    else:
        postinumerot.sort()
        for i in postinumerot:
            if postinumerot.index(i) < (len(postinumerot) -1):
                viesti += ''.join(str(i + ', '))
            else:
                viesti += ''.join(str(i))
        print(f"Postinumerot: {viesti}")

