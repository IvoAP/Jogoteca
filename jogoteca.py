from flask import Flask, render_template

app = Flask(__name__)

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

@app.route('/inicio')
def ola():
    jogo1 = Jogo('tetrix' , 'Puzzle', 'Atari')
    jogo2 = Jogo ('God of War', 'Hackingslash', 'Play Station 2')
    jogo3 = Jogo('Dragon Ball Fighter Z', 'Luta', 'Play Station 3, Xbox, Computador')
    lista = [jogo1, jogo2, jogo3]
    return render_template('lista.html',titulo = 'Jogos', jogos = lista)

@app.route('/novo')
def novo():
    return render_template('novo.html', titulo ='Novo Jogo')

app.run(host = '0.0.0.0', port = 8080)

