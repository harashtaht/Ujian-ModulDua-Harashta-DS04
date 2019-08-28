from flask import Flask, request, jsonify, render_template, redirect
import requests

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return render_template('homePoke.html')

@app.route('/hasil', methods=['POST'])
def hasil():
    body = request.form
    nama_Pokemon = str(body['namaPoke']).lower()
    url = f'https://pokeapi.co/api/v2/pokemon/{nama_Pokemon}'
    
    dataPoke = requests.get(url)

    if dataPoke.status_code == 200:
        dataComplete = dataPoke.json()
        return render_template(
            'pokeResults.html', 
            namaPoke = str(dataComplete['name']).capitalize(),
            idPoke = dataComplete['id'],
            pictPoke = dataComplete['sprites']['front_default'],
            htPoke = dataComplete ['height'],
            wtPoke = dataComplete ['weight'])
    elif str(dataPoke) == """<Response [404]>""":
        return render_template('notFound.html')


if __name__ == '__main__':
    app.run(
        debug=True,
        host='localhost',
        port=5000
    )