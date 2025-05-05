from flask import Flask
import unicodedata

app = Flask(__name__)
pole = []

@app.route('/')
def home():
    return "Hello, Flask!"

@app.route('/nacti')
def nacti():
    with open("test.txt", 'r', encoding='utf-8') as file:
        radky = file.readlines()
    for radek in radky:
        rok, jmeno, prijmeni = radek.strip().split(' ')
        rok = int(rok) + 10
        jmeno = ''.join(c for c in unicodedata.normalize('NFD', jmeno) if unicodedata.category(c) != 'Mn')
        prijmeni = ''.join(c for c in unicodedata.normalize('NFD', prijmeni) if unicodedata.category(c) != 'Mn')
        print(f"Rok: {rok}, jmeno: {jmeno}, prijmeni: {prijmeni}")
        pole.append((rok, jmeno, prijmeni))
    return "data loaded successfully"

if __name__ == '__main__':
    app.run(debug=True)
