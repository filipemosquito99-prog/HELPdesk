from flask import  Flask, render_template, request, redirect
import sqlite3

def  criar_banco():
    conexao = sqlite3.connect("status.db")
    conexao.execute('''CREATE TABLE IF NOT EXISTS  chamados (id INTEGER PRIMARY KEY AUTOINCREMENT, titulo TEXT NOT NULL, descricao TEXT NOT NULL, prioridade TEXT NOT NULL, status TEXT NOT NULL)''')
    conexao.commit()
    conexao.close()    

def salvar_chamado(titulo, descricao, prioridade):
    conexao = sqlite3.connect("status.db")
    conexao.execute("INSERT INTO chamados (titulo, descricao, prioridade, status) VALUES  (?, ?, ?, ?)", (titulo, descricao, prioridade, "aberto"))
    conexao.commit()
    conexao.close()

def mudar_status(id, status):
    conexao = sqlite3.connect("status.db")
    conexao.execute("UPDATE chamados SET status = ? WHERE id = ?", (status, id))
    conexao.commit()
    conexao.close()

app = Flask(__name__)

@app.route("/chamados/<int:id>", methods=["POST"])
def mudar_status_chamado(id,):
    mudar_status(id, request.form["status"])
    return redirect("/ver_chamados")

def listar_chamados():
    conexao = sqlite3.connect("status.db")
    cursor = conexao.execute("SELECT id, titulo, descricao, prioridade, status FROM chamados")
    chamados = cursor.fetchall()
    conexao.close()
    return chamados

@app.route("/")
def index():
    return render_template("inicio.html")

@app.route("/ver_chamados")
def ver_chamados():
    chamados = listar_chamados()
    return render_template("chamados.html", chamados=chamados)  

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")
@app.route("/fazer_chamados", methods = ["GET", "POST"])
def novo():
    if request.method == "POST":
        salvar_chamado(request.form["titulo"], request.form["descricao"], request.form["prioridade"])
    return render_template("fazer_chamados.html")
if __name__ == "__main__":
    criar_banco()
    app.run(debug=True)