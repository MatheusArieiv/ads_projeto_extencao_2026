# \# Assistente Financeiro Automatizado - Acessibilidade para Microempresas

# 

# Projeto de Extensão apresentado ao curso de Análise e Desenvolvimento de Sistemas como parte do Programa de Contexto à Comunidade.

# 

# \## Empresa Parceira

# Nivane Fazenda Park. Projeto alinhado com a meta global ODS 8 da ONU para incentivar o crescimento econômico local.

# 

# \## O Que é o Projeto

# Este projeto é um robô inteligente dentro do Telegram feito para ajudar pequenos comércios no controle do caixa diário. O sistema foi pensado para pessoas que não têm intimidade com tecnologia ou que vivem na correria do dia a dia. Ele elimina telas difíceis e permite registrar gastos e ganhos usando apenas mensagens normais de texto ou áudios de voz.

# 

# \## O Jeito Antigo vs. O meu Jeito

# 

# No modelo tradicional de gestão de pequenos negócios, o trabalho exige muito tempo e esforço:

# 1\. O dono faz uma compra rápida ou uma venda no meio do expediente.

# 2\. Precisa guardar notas de papel ou anotar em rabiscos para não esquecer.

# 3\. No fim do dia ou da semana, precisa ligar o computador, abrir sistemas complicados ou planilhas de Excel e digitar tudo manualmente.

# 

# O problema do jeito antigo: Por causa da correria e da falta de costume com computadores, os donos acabam esquecendo de marcar os pequenos gastos do dia. Isso gera furos no controle e no dinheiro da empresa.

# 

# Como a minha solução resolve: O assistente elimina a necessidade de abrir computadores ou usar planilhas. O usuário só precisa mandar um áudio no aplicativo. O robô recebe esse áudio, transforma em texto, entende o valor falado e salva tudo no banco de dados sozinho sem que o usuário precise mexer em nenhuma configuração.

# 

# \## Ferramentas Utilizadas

# Python 3 para a construção geral do sistema.

# SQLite para o armazenamento seguro dos dados no computador.

# API do Telegram para a comunicação direta com o usuário.

# Google Speech Recognition para traduzir os áudios de voz em texto.

# FFmpeg para ajustar o formato dos arquivos de áudio recebidos.

# 

# \## Como o Sistema Foi Organizado

# telegram\_bot.py: Cuida da conversa com o usuário. É a parte responsável por receber as mensagens e preparar os áudios gravados no celular para que o sistema consiga entender.

# interpretador.py: É o cérebro do robô. Ele analisa o texto que veio do áudio, identifica se a pessoa gastou ou recebeu e filtra a frase para extrair apenas o valor em dinheiro.

# financeiro.py: Cuida do cofre de dados. Abre a conexão com o banco de dados e cria os comandos necessários para salvar as informações ou mostrar o saldo atualizado na hora.

# 

# \## Autor

# Matheus Vieira - RA: 2025294049

