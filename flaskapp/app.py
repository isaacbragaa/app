from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        sinopse = request.form['sinopse']
        tipo = request.form['tipo']

        connection = sqlite3.connect('/app/database.db')
        cursor = connection.cursor()
        cursor.execute("INSERT INTO cadastros (nome, email, sinopse, tipo) VALUES (?, ?, ?, ?)",
                       (nome, email, sinopse, tipo))
        connection.commit()
        connection.close()

        return redirect(url_for('index'))

    return render_template('cadastro.html')

@app.route('/consultar')
def consultar():
    connection = sqlite3.connect('/app/database.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM cadastros")
    cadastros = cursor.fetchall()
    connection.close()
    return render_template('consultar.html', cadastros=cadastros)

if __name__ == '__main__':
    if not os.path.exists('/app/database.db'):
        import init_db
    app.run(host='0.0.0.0')