import re
# importa as funcoes de manipulacao de banco de dados do financeiro.py
from financeiro import adicionar_registro, total_dia, total_mes, saldo

def extrair_valor(texto):
    '''
    Varre o texto em busca de padroes numericos
    '''
    # expressao para capturar numeros ou decimais
    padrao = r'\d+(?:[.,]\d+)?'
    valores = re.findall(padrao, texto)

    if valores:
        # Substitui a virgula por ponto pro python conseguir converter para float
        valor_texto = valores[0].replace(',', '.')
        return float(valor_texto)
    return 0.0

def interpretar(texto):
    '''
    interpreta o texto extraido do audio do whatsapp
    '''
    # padronizar o texto em letras minusculas para evitar erros
    texto = texto.lower()
    valor = extrair_valor(texto)

    # ************ FLUXO DE REGISTRO DE GASTOS ***************
    # palavras-chave de intencao: registrar um saida
    palavras_gasto = ["paguei", "gastei", "comprei", "pagar", "gasto", "pix enviado", "débito", "perdi"]

    if any(p in texto for p in palavras_gasto):
        if valor == 0:
            return 'Não consegui entender o valor do gasto do informado no áudio.'
        
        # chama o modulo financeiro para registrar o gasto no banco de dados
        adicionar_registro("gasto", "geral", texto, valor)
        return f" Gasto de R$ {valor:.2f} resgistrado com sucesso!"
    
    # ************* FLUXO DE REGISTRO DE ENTRADAS **************
    # palvras-chave de intencao: registrar uma saida
    palavras_entrada = ["recebi", "ganhei", "entrou", "entrada", "pix recebido", "crédito"]

    if any(p in texto for p in palavras_entrada):
        if valor == 0:
            return "Não consegui entender o valor da entrada!"
        
        # chama o modulo financeiro para registrar um entrada no banco de dados.
        adicionar_registro("entrada", "geral", texto, valor)
        return f"Entrada de R$ {valor:.2f} registrada com sucesso!"

    # ************ FLUXO EMISSAO DE RELATORIO ********************
    # intencao: consulta de movimentacao diaria
    if any(p in texto for p in ["hoje", "dia"]):
        return f"[Relatório] Moviementação total de hoje: R$ {total_dia():.2f}"
    
    # intencao: consulta de movimentacao mensal
    if any(p in texto for p in ["mês", "mes"]):
        return f"[Realatório] Movimentação total do mês: R$ {total_mes():.2f}"
    
    # intencao: consulta de saldo total do caixa
    if "saldo" in texto:
        return f"[Caixa] Seu saldo atual líquido é de: R$ {saldo():.2f}"
    
    # ************** TOLERANCIA DE ERROS **********************
    # respostas caso o audio nao contenha nehuma palavra-chave
    return(
        "NÃO CONSEGUI IDENTIFICAR O SEU PEDIDO!\n\n"
        "Tente mandar outro áudio."
    )
    

    