# -*- coding: utf-8 -*-
"""
Script para gerar áudio da narração do vídeo MATLAB
Autor: Felipe
Data: Agosto 2025
"""

import os
import sys

# Texto da narração dividido por cenas para melhor controle
CENAS = {
    "cena1": """
Então, pessoal... bateu aquela nostalgia e eu pensei: 'Vou fazer um gráfico radar no MATLAB, igual aos velhos tempos!'. 
Só que... nos VELHOS tempos mesmo, né? Quando a gente fazia isso num computador de tubo, digitando código no escuro, movido a café e puro desespero existencial. Era quase um ritual de passagem!
Agora? Agora é tudo num app bonitinho no celular. Ele até te dá exemplo, te mostra onde tá o erro com setinha vermelha... 
E eu aqui, olhando pra esse 'syntax error' como se fosse hieróglifo egípcio. Cara, EU JURO que eu sabia fazer isso! Mas aparentemente meu cérebro fez uma limpeza de cache e deletou essa pasta pra guardar mais memes de gatinho.
""",
    
    "cena2": """
Tá bom, plano B. Vou pedir ajuda pra uma IA qualquer aí. 'Ô, me faz um código de gráfico radar em MATLAB', eu disse. 
E ela até tentou, coitada... gerou um código bonitinho. Mas na hora de rodar no app... MAIS texto vermelho!
E o pior, gente... o PIOR não foi a IA errar. O pior foi eu perceber que EU não conseguia corrigir UMA. ÚNICA. LINHA. 
Meu diploma de engenharia deve estar se contorcendo na moldura da parede. Tipo, o MATLAB melhorou, ficou mais fácil, tem tutorial, tem exemplo... e eu aqui, perdido igual turista em Tokyo.
""",
    
    "cena3": """
Aí eu cansei. Abandonei o barco. Fui falar com quem REALMENTE me entende...
Abri a Monica, minha IA pessoal, e mandei o comando mais simples do mundo: 'Monica, faz um gráfico radar aí pra mim'. 
E... POOF! Mágica instantânea!
Olha só que coisa linda! Limpo, perfeito, responsivo, sem uma linha de código, sem dor, sem sofrimento, sem crise existencial. 
E o mais irônico? É um gráfico de 'Avaliação de Competências'... justamente quando a MINHA competência em MATLAB foi pro espaço sideral!
""",
    
    "cena4": """
Mas ó, antes que vocês pensem que eu virei um preguiçoso tecnológico... essa Monica não é qualquer IA não, viu? 
Faz 3 anos que eu alimento ela com base de dados dos MEUS próprios conhecimentos. Ela é tipo uma versão digital e bem mais inteligente de mim mesmo.
Então, na verdade, não é que eu não sei mais fazer gráfico... é que eu OTIMIZEI o processo, tá bom? É pura eficiência! Trabalho inteligente, não trabalho duro!
Pelo menos é isso que eu vou contar pro meu eu de 20 anos atrás quando ele aparecer nos meus sonhos cobrando satisfação...
"""
}

def gerar_audio_gtts():
    """Gera áudio usando Google Text-to-Speech (gTTS)"""
    try:
        from gtts import gTTS
        import pygame
        
        print("🎙️ Gerando áudio com gTTS...")
        
        for cena, texto in CENAS.items():
            print(f"Processando {cena}...")
            
            # Criar objeto TTS
            tts = gTTS(text=texto, lang='pt-br', slow=False)
            
            # Salvar arquivo
            filename = f"{cena}_naracao.mp3"
            tts.save(filename)
            print(f"✅ {filename} salvo!")
        
        # Gerar arquivo completo
        texto_completo = "\n\n".join(CENAS.values())
        tts_completo = gTTS(text=texto_completo, lang='pt-br', slow=False)
        tts_completo.save("naracao_completa.mp3")
        print("✅ naracao_completa.mp3 salvo!")
        
        return True
        
    except ImportError:
        print("❌ gTTS não instalado. Instale com: pip install gtts pygame")
        return False

def gerar_audio_pyttsx3():
    """Gera áudio usando pyttsx3 (offline)"""
    try:
        import pyttsx3
        
        print("🎙️ Gerando áudio com pyttsx3...")
        
        # Configurar engine
        engine = pyttsx3.init()
        
        # Configurar voz (português brasileiro se disponível)
        voices = engine.getProperty('voices')
        for voice in voices:
            if 'brazil' in voice.name.lower() or 'portuguese' in voice.name.lower():
                engine.setProperty('voice', voice.id)
                break
        
        # Configurar velocidade e volume
        engine.setProperty('rate', 180)  # Velocidade (palavras por minuto)
        engine.setProperty('volume', 0.9)  # Volume (0.0 a 1.0)
        
        for cena, texto in CENAS.items():
            print(f"Processando {cena}...")
            filename = f"{cena}_naracao.wav"
            engine.save_to_file(texto, filename)
        
        # Arquivo completo
        texto_completo = "\n\n".join(CENAS.values())
        engine.save_to_file(texto_completo, "naracao_completa.wav")
        
        engine.runAndWait()
        print("✅ Arquivos .wav gerados!")
        
        return True
        
    except ImportError:
        print("❌ pyttsx3 não instalado. Instale com: pip install pyttsx3")
        return False

def instrucoes_alternativas():
    """Mostra instruções para métodos alternativos"""
    print("\n" + "="*60)
    print("🎯 MÉTODOS ALTERNATIVOS PARA GERAR ÁUDIO")
    print("="*60)
    
    print("\n1️⃣ GOOGLE AI STUDIO (Recomendado)")
    print("   • Acesse: https://aistudio.google.com")
    print("   • Cole o texto do roteiro")
    print("   • Configure: Voz masculina, português brasileiro")
    print("   • Ajuste velocidade e tom")
    
    print("\n2️⃣ ELEVENLABS (Qualidade Premium)")
    print("   • Acesse: https://elevenlabs.io")
    print("   • Escolha voz brasileira")
    print("   • Cole o roteiro por partes")
    print("   • Ajuste estabilidade e clareza")
    
    print("\n3️⃣ MICROSOFT AZURE SPEECH")
    print("   • Acesse: https://speech.microsoft.com")
    print("   • Voz: pt-BR-AntonioNeural")
    print("   • Use SSML para controlar pausas e ênfase")
    
    print("\n4️⃣ AMAZON POLLY")
    print("   • Console AWS")
    print("   • Voz: Ricardo (pt-BR)")
    print("   • Formato: MP3, alta qualidade")

if __name__ == "__main__":
    print("🎬 GERADOR DE ÁUDIO - VÍDEO MATLAB")
    print("="*50)
    
    # Tentar métodos disponíveis
    sucesso = False
    
    print("\nTentando gTTS (Google)...")
    if gerar_audio_gtts():
        sucesso = True
    
    if not sucesso:
        print("\nTentando pyttsx3 (offline)...")
        if gerar_audio_pyttsx3():
            sucesso = True
    
    if not sucesso:
        print("\n⚠️ Nenhuma biblioteca TTS encontrada.")
        instrucoes_alternativas()
    
    print("\n📁 Arquivos de texto disponíveis:")
    print("   • roteiro_completo.txt - Roteiro formatado")
    print("   • gerar_audio.py - Este script")