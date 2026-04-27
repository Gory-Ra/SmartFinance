import matplotlib.pyplot as plt
from analytics_engine import calcular_media_historica

def exibir_grafico_gastos(dados_por_categoria):
    if not dados_por_categoria:
        print("Nenhum dado de gasto encontrado para gerar o gráfico.")
        return

    categorias = list(dados_por_categoria.keys())
    valores = list(dados_por_categoria.values())

    # Configurações estéticas
    cores = ["#f77070","#7066ff","#57f157","#f8f1b5", '#c2c2f0', '#ffb3e6']
    fig, ax = plt.subplots(figsize=(8, 8))
    
    # Criando o gráfico de pizza
    wedges, texts, autotexts = ax.pie(
        valores, 
        labels=categorias, 
        autopct='%1.1f%%', 
        startangle=140, 
        colors=cores,
        pctdistance=0.85,
        explode=[0.05] * len(categorias) # Pequeno afastamento entre fatias
    )

    # Transformando em um gráfico de rosca 
    centro_circulo = plt.Circle((0,0), 0.70, fc='white')
    fig.gca().add_artist(centro_circulo)

    plt.setp(autotexts, size=10, weight="bold", color="black")
    ax.set_title("Distribuição de Gastos por Categoria", fontsize=15, pad=20)
    
    # Ajuste para não cortar as legendas
    plt.tight_layout()
    
    print(" Abrindo dashboard interativo...")
    plt.show()

def analisar_e_exibir(dados_por_categoria):
    print("\n--- ANALYTICS ESTATÍSTICO ---")
    for cat, valor_atual in dados_por_categoria.items():
        media = calcular_media_historica(cat) 
        
        if media > 0:
            variacao = ((valor_atual / media) - 1) * 100
            if variacao > 20:
                print(f" ATENÇÃO: {cat} está {variacao:.1f}% acima da média histórica!")
            elif variacao < -20:
                print(f" BOA: {cat} está {abs(variacao):.1f}% abaixo da média!")
            else:
                print(f" {cat}: Gasto dentro do padrão.")
    
    # Chame a função de gráfico que você já tinha
    exibir_grafico_gastos(dados_por_categoria)
