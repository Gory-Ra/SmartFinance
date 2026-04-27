from ai_query import consultar_com_ia

# Esta pergunta força a IA a buscar dados na sua tabela
pergunta = "Liste todas as minhas transacoes" 

print("Enviando pergunta para IA...")
resultado = consultar_com_ia(pergunta)

print("-" * 30)
print(f"Resultado da consulta: {resultado}")
print("-" * 30)