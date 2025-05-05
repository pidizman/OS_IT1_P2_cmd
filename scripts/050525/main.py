import unicodedata
import json

with open("test.txt", 'r', encoding='utf-8') as file:
    radky = file.readlines()

pole = []
for radek in radky:
    rok, jmeno, prijmeni = radek.strip().split(' ')
    rok = int(rok) + 10
    jmeno = ''.join(c for c in unicodedata.normalize('NFD', jmeno) if unicodedata.category(c) != 'Mn')
    prijmeni = ''.join(c for c in unicodedata.normalize('NFD', prijmeni) if unicodedata.category(c) != 'Mn')
    print(f"Rok: {rok}, jmeno: {jmeno}, prijmeni: {prijmeni}")
    pole.append((rok, jmeno, prijmeni))
print(pole)
print(json.dumps(pole, ensure_ascii=False, indent=4))
