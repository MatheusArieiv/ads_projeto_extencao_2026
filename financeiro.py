import sqlite3
from datetime import datetime
import os

# Define o caminho para salvar o arquivo do banco de dados na mesma pasta do script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_NAME = os.path.join(BASE_DIR, "banco_de_dados.db")

def inicializar_banco():
    '''
    Cria a tabela no SQLite.
    '''
    # Faz a conexão com o arquivo do banco de dados
    conexao = sqlite3.connect(DB_NAME)
    # Curso é o obejto que permite executar comandos SQL dentro do banco
    cursor = conexao.cursor()

    # Criando a tabela
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transacoes (
                   id INTEGER PRIMARY KEY AUTOINCREMENT, -- Chave primaria que se auto-incrementa
                   data TEXT NOT NULL,                   -- Guarrda a data em formato texto (dd/mm/aaaa)
                   hora TEXT NOT NULL,                   -- Guarda a hora (hh:mm)
                   tipo TEXT NOT NULL,                   -- entrada ou gasto
                   categoria TEXT NOT NULL,              -- Categoria de registro
                   descricao TEXT,                       -- O texto completo que o usuario falou
                   valor REAL NOT NULL                   -- Tipo decimal para valores finalnceiros 
         )
    ''')

    # Confirma as alterações no banco de dados
    conexao.commit()
    conexao.close()

def adicionar_registro(tipo, categoria, descricao, valor):
    '''
    Insere um novo registro
    '''
    inicializar_banco() # Observa se a tabela existe antes de inserir

    conexao = sqlite3.connect(DB_NAME)
    cursor = conexao.cursor()

    #  captura a data e hora exatas do momento do resgistro
    agora = datetime.now()
    data = agora.strftime("%d/%m/%Y")
    hora = agora.strftime("%H:%M")

    # Comando SQL INSERT utilizando Placeholders para evitar SQL Injection
    cursor.execute('''
        INSERT INTO transacoes (data, hora, tipo, categoria, descricao, valor)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (data, hora, tipo.lower(), categoria.lower(), descricao, float(valor)))

    conexao.commit()
    conexao.close()

def total_dia():
    '''
    soma todo os valores movimentdos do dia atual
    '''
    inicializar_banco()
    conexao = sqlite3.connect(DB_NAME)
    cursor = conexao.cursor()

    hoje = datetime.now().strftime("%d/%m/%Y")

    # SUM do SQL, serve para somar
    cursor.execute("SELECT SUM(valor) FROM transacoes WHERE data = ?", (hoje,))
    resultado = cursor.fetchone()[0]# pega o priemeiro resultado retornado pela consulta

    conexao.close()
    # Se o banco estiver vazio hoje, retorna 0.0 para não quebrar
    return resultado if resultado is not None else 0.0


def total_mes():
    '''
    Soma todos os valores movimentados no mes atual
    '''
    inicializar_banco()
    conexao = sqlite3.connect(DB_NAME)
    cursor = conexao.cursor()

    # Pega o mes atual no formato /mm/aaaa
    mes_ano = datetime.now().strftime("/%m/%Y")

    # Usa o operador LIKE com '%' para buscar qualquer data que termine com mes atual
    cursor.execute("SELECT SUM(valor) FROM transacoes WHERE data like ?", ('%' + mes_ano,))
    resultado = cursor.fetchone()[0]

    conexao.close()
    return resultado if resultado is not None else 0.0

def saldo():
    '''
    Calcula o saldo atual liquido
    '''
    inicializar_banco()
    conexao = sqlite3.connect(DB_NAME)
    cursor = conexao.cursor()

    # Consultar a soma total das entradas
    cursor.execute("SELECT SUM(valor) FROM transacoes WHERE tipo = 'entrada'")
    entradas = cursor.fetchone()[0] or 0.0

    # Consulta a soma total dos gatos
    cursor.execute("SELECT SUM(valor) FROM transacoes WHERE tipo = 'gasto'")
    gastos = cursor.fetchone()[0] or 0.0

    conexao.close()
    # Retorna o calculo do saldo final
    return entradas - gastos