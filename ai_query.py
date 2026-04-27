import requests
from database import Session
from sqlalchemy import text

def consultar_com_ia(pergunta):
    # Prompt de sistema
    prompt = f"""
    Você é um tradutor SQL para SQLite. Tabela: 'transacoes'.
    Colunas e valores permitidos:
    - tipo: APENAS 'Receita' ou 'Despesa'.
    - categoria: Qualquer valor (ex: 'Cartão de crédito', 'Lanche', 'Salario').
    - descricao: Qualquer valor.

    REGRAS DE OURO:
    1. Nunca use um valor de 'categoria' dentro da coluna 'tipo'.
    2. Se o usuário falar "cartão", busque em 'categoria' ou 'descricao', NUNCA em 'tipo'.
    3. Sempre use 'Receita' ou 'Despesa' com a inicial maiúscula na coluna 'tipo'.
    4. Para datas:
       - Mês atual: "strftime('%Y-%m', data) = strftime('%Y-%m', 'now')"
       - Últimos 30 dias: "data >= date('now', '-30 days')"
    5. Sempre use LOWER(coluna) LIKE '%termo%' para buscas de texto para evitar erros de maiúsculas.
    6. Sempre coloque parênteses ao combinar categorias e descrições com OR. Exemplo: AND (categoria LIKE '%...%' OR descricao LIKE '%...%')

    Pergunta: "{pergunta}"
    Resposta (SQL):
    """

    try:
        # 1. Chamada para a IA
        response = requests.post("http://localhost:11434/api/generate", json={
            "model": "phi3",
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": 0,
                "num_predict": 50
            }
        }, timeout=30)
        
        sql_query = response.json()['response'].strip()
        
        # 2. Limpeza do SQL
        sql_query = sql_query.split(';')[0] + ';'
        sql_query = sql_query.replace("```sql", "").replace("```", "").strip()
        
        #print(f"DEBUG - IA gerou limpo: {sql_query}")
        
        # 3. Execução no Banco de Dados
        session = Session()
        resultado = session.execute(text(sql_query)).fetchall()
        session.close()
        
        # Retorna o resultado encontrado ou lista vazia se nada for achado
        return resultado if resultado else []

    except requests.exceptions.Timeout:
        print("A IA demorou demais para responder.")
        return "timeout"
    except Exception as e:
       # print(f"DEBUG - Erro na execução do SQL: {e}")
        # Retorna erro amigável para o gui.py identificar
        return "ERRO_SQL"