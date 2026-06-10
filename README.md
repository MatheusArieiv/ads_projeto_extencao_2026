# Assistente Financeiro Automatizado - Acessibilidade para Microempresas

Projeto de Extensão apresentado ao curso de Análise e Desenvolvimento de Sistemas como parte do Programa de Contexto à Comunidade.

## Empresa Parceira

Nivane Fazenda Park. Projeto alinhado com a meta global ODS 8 da ONU para incentivar o crescimento econômico local.

## O Que é o Projeto

Este projeto é um robô inteligente dentro do Telegram feito para ajudar pequenos comércios no controle do caixa diário. O sistema foi pensado para pessoas que não têm intimidade com tecnologia ou que vivem na correria do dia a dia. Ele elimina telas difíceis e permite registrar gastos e ganhos usando apenas mensagens normais de texto ou áudios de voz.

## O Jeito Antigo vs. O meu Jeito

No modelo tradicional de gestão de pequenos negócios, o trabalho exige muito tempo e esforço:
1. O dono faz uma compra rápida ou uma venda no meio do expediente.
2. Precisa guardar notas de papel ou anotar em rabiscos para não esquecer.
3. No fim do dia ou da semana, precisa ligar o computador, abrir sistemas complicados ou planilhas de Excel e digitar tudo manualmente.

O problema do jeito antigo: Por causa da correria e da falta de costume com computadores, os donos acabam esquecendo de marcar os pequenos gastos do dia. Isso gera furos no controle e no dinheiro da empresa.

Como a minha solução resolve: O assistente elimina a necessidade de abrir computadores ou usar planilhas. O usuário só precisa mandar um áudio no aplicativo. O robô recebe esse áudio, transforma em texto, entende o valor falado e salva tudo no banco de dados sozinho sem que o usuário precise mexer em nenhuma configuração.

## Ferramentas Utilizadas

Python 3 para a construção geral do sistema.
SQLite para o armazenamento seguro dos dados no computador.
API do Telegram para a comunicação direta com o usuário.
Google Speech Recognition para traduzir os áudios de voz em texto.
FFmpeg para ajustar o formato dos arquivos de áudio recebidos.

## Como o Sistema Foi Organizado

telegram_bot.py: Cuida da conversa com o usuário. É a parte responsável por receber as mensagens e preparar os áudios gravados no celular para que o sistema consiga entender.

interpretador.py: É o cérebro do robô. Ele analisa o texto que veio do áudio, identifica se a pessoa gastou ou recebeu e filtra a frase para extrair apenas o valor em dinheiro.

financeiro.py: Cuida do cofre de dados. Abre a conexão com o banco de dados e cria os comandos necessários para salvar as informações ou mostrar o saldo atualizado na hora.

## Como Executar o Projeto

**1. Criar o bot no Telegram**

Antes de qualquer coisa, é necessário criar um bot oficial no Telegram. Para isso, abra o aplicativo, pesquise por @BotFather e envie o comando /newbot. Escolha um nome e um nome de usuário para o seu bot. Ao final, o BotFather vai te enviar um token, que é o código de identificação do seu bot. Guarde esse código.

**2. Colar o token no código**

Abra o arquivo telegram_bot.py em qualquer editor de texto e substitua o valor da variável pelo token que você recebeu:

```
TOKEN_TELEGRAM = "cole_seu_token_aqui"
```

**3. Instalar o Python**

Acesse python.org/downloads, baixe e instale a versão mais recente. No Windows, durante a instalação, marque obrigatoriamente a opção "Add Python to PATH" para que o sistema consiga encontrar o programa.

**4. Instalar o FFmpeg**

O FFmpeg é o programa responsável por converter os áudios recebidos pelo Telegram para um formato que o robô consegue entender.

- Windows: Baixe em ffmpeg.org, extraia a pasta e adicione o caminho da pasta `bin` às variáveis de ambiente do sistema (PATH).
- Mac: Com o Homebrew instalado, rode o comando `brew install ffmpeg` no Terminal.

**5. Instalar as dependências**

Abra o terminal na pasta onde os arquivos do projeto estão salvos e execute o comando abaixo. Ele vai baixar e instalar automaticamente todas as bibliotecas que o projeto precisa:

```
pip install python-telegram-bot pydub SpeechRecognition
```

**6. Executar o bot**

Ainda no terminal, na mesma pasta, execute:

```
python telegram_bot.py
```

O robô vai iniciar e ficará escutando as mensagens. Para encerrar, pressione CTRL+C.

## Dicas de Uso

Com o bot rodando, abra o Telegram, encontre o seu bot pelo nome de usuário que você criou e comece a conversar. Veja alguns exemplos do que você pode enviar por texto ou áudio:

- Para registrar um gasto: *"paguei 50 reais de almoço"*
- Para registrar uma entrada: *"recebi 200 reais de pagamento"*
- Para consultar o total movimentado hoje: *"quanto movimentei hoje?"*
- Para consultar o total do mês: *"resumo do mês"*
- Para ver o saldo atual do caixa: *"qual meu saldo?"*

## Autor

Matheus Vieira - RA: 2025294049
