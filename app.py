from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/saludo/<nombre>')
def saludo(nombre):
    return f'¡Hola, {nombre}!'


if __name__ == '__main__':
    app.run(debug=True)