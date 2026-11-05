import sqlite3

class BancoChamados():
    def __init__(self, arquivo):
        self.arquivo = arquivo

    def criar_tabela(self):
        conexao = sqlite3.connect(self.arquivo)
        conexao.execute('''CREATE TABLE IF NOT EXISTS  chamados (id INTEGER PRIMARY KEY AUTOINCREMENT, titulo TEXT NOT NULL, descricao TEXT NOT NULL, prioridade TEXT NOT NULL, status TEXT NOT NULL)''')
        conexao.commit()
        conexao.close()  

    def salvar_chamado(self, titulo, descricao, prioridade):
        conexao = sqlite3.connect(self.arquivo)
        conexao.execute("INSERT INTO chamados (titulo, descricao, prioridade, status) VALUES  (?, ?, ?, ?)", (titulo, descricao, prioridade, "aberto"))
        conexao.commit()
        conexao.close()

    def listar(self):
        conexao = sqlite3.connect(self.arquivo)
        cursor = conexao.execute("SELECT id, titulo, descricao, prioridade, status FROM chamados")
        chamados = cursor.fetchall()
        conexao.close()
        return chamados

    def mudar_status(self, id, status):
        conexao = sqlite3.connect(self.arquivo)
        conexao.execute("UPDATE chamados SET status = ? WHERE id = ?", (status, id))
        conexao.commit()
        conexao.close()

banco = BancoChamados("status.db")