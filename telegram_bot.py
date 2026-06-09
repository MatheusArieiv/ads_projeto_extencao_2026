import os
import speech_recognition as sr
from pydub import AudioSegment
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

# importa o interpretador.py
from interpretador import interpretar

# define uma variável para o token telegram
TOKEN_TELEGRAM = "8651322152:AAHTM39JwPBZ08V5yH2j6tLRhL-VgXGLHhM"

reconhecedor = sr.Recognizer()

def transcrever_audio_telegram(caminho_ogg):
    """
    Usa o FFmpeg local para converter o áudio nativo do Telegram .ogg
    em WAV e faz a transcrição usando o Google Speech.
    """
    caminho_wav = "audio_temporario.wav"
    try:
        print("[Bot] Convertendo áudio recebido do Telegram...")
        # Converte OGG para WAV usando pydub + FFmpe
        audio = AudioSegment.from_file(caminho_ogg, format="ogg")
        audio.export(caminho_wav, format="wav")

        print("[Bot] Enviando para reconhecimento de voz (Google)...")
        with sr.AudioFile(caminho_wav) as fonte:
            dados_audio = reconhecedor.record(fonte)
            texto = reconhecedor.recognize_google(dados_audio, language="pt-BR")
        return texto
    except sr.UnknownValueError:
        print("[Bot] Google não entendeu o áudio.")
        return None
    except Exception as e:
        print(f"[Bot] Erro ao converter/transcrever: {e}")
        return None
    finally:
        # Deleta o arquivo WAV temporário
        if os.path.exists(caminho_wav):
            os.remove(caminho_wav)

async def lidar_com_mensagem(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Função principal que intercepta texto e áudio enviados ao Telegram
    """
    mensagem = update.message
    if not mensagem:
        return
        
    id_usuario = mensagem.chat_id
    
    # SE FOR MENSAGEM DE TEXTO:
    if mensagem.text:
        texto_recebido = mensagem.text
        print(f"\n[Texto] Usuário {id_usuario}: {texto_recebido}")
        
        # Passa o texto para o interpretador.py
        resposta = interpretar(texto_recebido)
        await update.message.reply_text(resposta)

    # SE FOR MENSAGEM DE ÁUDIO
    elif mensagem.voice or mensagem.audio:
        arquivo_audio = mensagem.voice if mensagem.voice else mensagem.audio
        print(f"\n[Áudio] Baixando mensagem de voz de {id_usuario}...")
        
        # O Telegram da o link do arquivo direto, o Python baixa localmente
        caminho_ogg = "audio_temporario.ogg"
        arquivo_telegram = await context.bot.get_file(arquivo_audio.file_id)
        await arquivo_telegram.download_to_drive(caminho_ogg)
        
        # Faz a transcrição usando a função
        texto_transcrito = transcrever_audio_telegram(caminho_ogg)
        
        # Remove o arquivo OGG temporário
        if os.path.exists(caminho_ogg):
            os.remove(caminho_ogg)

        if texto_transcrito:
            print(f"[Áudio] Transcrição: '{texto_transcrito}'")
            # Envia o texto obtido da voz para o interpretador.py
            resposta = interpretar(texto_transcrito)
        else:
            resposta = "Desculpe, não consegui entender o áudio. Pode tentar falar mais perto ou digitar?"
            
        await update.message.reply_text(resposta)

def main():
    print("====================================================")
    print("     BOT FINANCEIRO DO TELEGRAM INICIADO COM SUCESSO")
    print("     Escutando mensagens de texto e áudio...")
    print("====================================================")
    
    # Inicializa a aplicação do Telegram
    app = Application.builder().token(TOKEN_TELEGRAM).build()
    
    # Configura o bot para escutar qualquer mensagem de texto ou áudio
    app.add_handler(MessageHandler(filters.TEXT | filters.VOICE | filters.AUDIO, lidar_com_mensagem))
    
    # Mantemo robô rodando continuamente
    app.run_polling()

if __name__ == "__main__":
    main()