import customtkinter as ctk
from database import init_db
# Consolidei os imports para ficar mais limpo
from services import adicionar_transacao, calcular_saldo, gastos_por_categoria, listar_categorias
from visualizer import exibir_grafico_gastos  

# Inicializa o banco
init_db()

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("SmartFinance - Gestão Pessoal")
        self.geometry("400x550")

        # Elementos da Interface
        self.label_titulo = ctk.CTkLabel(self, text="Nova Transação", font=("Roboto", 20, "bold"))
        self.label_titulo.pack(pady=20)

        self.entry_desc = ctk.CTkEntry(self, placeholder_text="Descrição (ex: iFood)")
        self.entry_desc.pack(pady=10, padx=20, fill="x")

        self.entry_valor = ctk.CTkEntry(self, placeholder_text="Valor (ex: 50.00)")
        self.entry_valor.pack(pady=10, padx=20, fill="x")

        self.option_tipo = ctk.CTkOptionMenu(self, values=["Despesa", "Receita"])
        self.option_tipo.pack(pady=10)

        self.combo_cat = ctk.CTkComboBox(self, values=listar_categorias())
        self.combo_cat.pack(pady=10, padx=20, fill="x")
        self.combo_cat.set("Selecione ou digite a categoria")

        self.btn_salvar = ctk.CTkButton(self, text="Salvar Transação", command=self.salvar)
        self.btn_salvar.pack(pady=10)

        self.btn_grafico = ctk.CTkButton(self, text="📊 Ver Dashboard", fg_color="#2b2b2b", command=self.abrir_grafico)
        self.btn_grafico.pack(pady=10)

        self.label_saldo = ctk.CTkLabel(self, text=f"Saldo Atual: R$ {calcular_saldo():.2f}", font=("Roboto", 16))
        self.label_saldo.pack(pady=20)

    def salvar(self):
        desc = self.entry_desc.get()
        valor = float(self.entry_valor.get())
        tipo = self.option_tipo.get()
        cat = self.combo_cat.get() 

        adicionar_transacao(desc, valor, tipo, cat)

        # Atualiza a lista de categorias no menu após salvar
        self.combo_cat.configure(values=listar_categorias())

        # Limpa campos e atualiza saldo
        self.entry_desc.delete(0, 'end')
        self.entry_valor.delete(0, 'end')
        self.label_saldo.configure(text=f"Saldo Atual: R$ {calcular_saldo():.2f}")
        
    def abrir_grafico(self):
        dados = gastos_por_categoria()
        exibir_grafico_gastos(dados)

if __name__ == "__main__":
    app = App()
    app.mainloop()