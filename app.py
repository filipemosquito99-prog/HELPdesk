from flask import  Flask, render_template, request, redirect
from classes import BancoChamados

banco = BancoChamados("status.db")

app = Flask(__name__)

@app.route("/chamados/<int:id>", methods=["POST"])
def mudar_status_chamado(id,):
    banco.mudar_status(id, request.form["status"])
    return redirect("/ver_chamados")

@app.route("/")
def index():
    return render_template("inicio.html")

@app.route("/ver_chamados")
def ver_chamados():
    chamados = banco.listar()
    return render_template("chamados.html", chamados=chamados)  

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")
@app.route("/fazer_chamados", methods = ["GET", "POST"])
def novo():
    if request.method == "POST":
        banco.salvar_chamado(request.form["titulo"], request.form["descricao"], request.form["prioridade"])
    return render_template("fazer_chamados.html")
if __name__ == "__main__":
    banco.criar_tabela()
    app.run(debug=True)