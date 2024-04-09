from flask import Flask, render_template, request

app = Flask(__name__)

livros = []

@app.route('/')
def index():
    return render_template('index.html', livros=livros)

@app.route('/adicionar_livro', methods=['POST'])
def adicionar_livro():
    titulo = request.form['titulo']
    autor = request.form['autor']
    ano = request.form['ano']
    livros.append({'titulo': titulo, 'autor': autor, 'ano': ano})
    return index()

if __name__ == '__main__':
    app.run(debug=True)