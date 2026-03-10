


from flask import Flask, render_template
import time
from random import randint

app = Flask(__name__)

A = ['<a class="couleur i" href="./index.html">Accueil</a>', '<a class="couleur i" href="./Histoire.html">Son histoire</a>', '<a class="couleur i" href="./Feats.html">Feats et beatmakers</a>', '<a class="couleur i" href="./Statistiques.html">Statistiques</a>', '<a class="couleur" href="./Discographie.html">Discographie</a>']

def Aleatoire():
    KJ = []
    for roll in range(0, 15):
        number = randint(0, 4)
        KJ.append(A[number])
        time.sleep(0.2)
    return KJ

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_aleatoire')
def run_aleatoire():
    KJ = Aleatoire()
    return render_template('result.html', KJ=KJ)
if __name__ == '__main__':
    app.run(debug=True)
