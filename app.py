from database import init_db
from services import adicionar_transacao, listar_transacoes, calcular_saldo
from services import adicionar_transacao, gastos_por_categoria, verificar_alerta_excesso, total_gasto_no_mes
from datetime import datetime

# 1. Inicializa o banco de dados
init_db()

# 2. Mock de dados (Simulação)
if not listar_transacoes():
    print("Populando banco inicial...")
    adicionar_transacao("Salário", 5000.0, "Receita", "Trabalho")
    adicionar_transacao("Aluguel", 1200.0, "Despesa", "Moradia")
    adicionar_transacao("iFood", 80.0, "Despesa", "Alimentação")

# 3. Exibição Simples no Terminal
print("\n--- EXTRATO ATUAL ---")
for t in listar_transacoes():
    simbolo = "+" if t.tipo == "Receita" else "-"
    print(f"{t.data.strftime('%d/%m')} | {t.descricao[:15]:<15} | {simbolo} R$ {t.valor:>8.2f}")

print(f"\nSALDO TOTAL: R$ {calcular_saldo():.2f}")

print("\n--- ANÁLISE DE GASTOS ---")
distribuicao = gastos_por_categoria()
for cat, valor in distribuicao.items():
    print(f"📁 {cat}: R$ {valor:.2f}")

hoje = datetime.now()
total_abril = total_gasto_no_mes(hoje.month, hoje.year)

