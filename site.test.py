from flask import Flask, render_template
app = Flask(__name__)

# Passo 1 - criar a 1° pg do site

# 1.1 route -> site.com/"nome da pg" -> caminho para o link
# 1.2 função -> o que você quer exibir na pg

@app.route('/')
def homepage():
    return render_template(homepage.html)

@app.route('/login')
def login():
    return render_template(login.html)

@app.route('/contatos')
def contatos():
    return render_template(contatos.html)

@app.route('/usuario/<nome_usuario>')
def usuarios(nome_usuario=None):
    return render_template("usuario.html", nome_usuario=nome_usuario)


if __name__ == '__manin__':
    app.run()
