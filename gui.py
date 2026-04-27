import customtkinter as ctk
from tkinter import messagebox, filedialog
from ai_query import consultar_com_ia # Importa a lógica da IA 
import customtkinter as ctk
from tkinter import filedialog
from database import init_db
from services import (
    adicionar_transacao, 
    calcular_saldo, 
    gastos_por_categoria, 
    listar_categorias, 
    exportar_para_csv
)
from visualizer import analisar_e_exibir

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

        # Botão Gráfico agora chama a função com Analytics
        self.btn_grafico = ctk.CTkButton(self, text="📊 Ver Dashboard", fg_color="#2b2b2b", command=self.abrir_grafico)
        self.btn_grafico.pack(pady=10)

        # SEÇÃO DE INTELIGÊNCIA ARTIFICIAL 
        self.label_ia = ctk.CTkLabel(self, text="Pergunte à IA (Local)", font=("Roboto", 14, "bold"))
        self.label_ia.pack(pady=(20, 0))

        self.entry_ia = ctk.CTkEntry(self, placeholder_text="Ex: Quanto gastei com lanche?")
        self.entry_ia.pack(pady=10, padx=20, fill="x")

        self.btn_ia = ctk.CTkButton(
            self, 
            text="🤖 Consultar Assistente", 
            fg_color="#57007f", 
            hover_color="#3a0055", 
            command=self.perguntar_ia # Liga o botão à função abaixo
        )
        self.btn_ia.pack(pady=5)

        self.label_saldo = ctk.CTkLabel(self, text=f"Saldo Atual: R$ {calcular_saldo():.2f}", font=("Roboto", 16))
        self.label_saldo.pack(pady=20)

        # Botão Exportar
        self.btn_exportar = ctk.CTkButton(self, text="📥 Exportar para CSV", fg_color="#333333", command=self.exportar)
        self.btn_exportar.pack(pady=10)

    def salvar(self):
        try:
            desc = self.entry_desc.get()
            valor = float(self.entry_valor.get())
            tipo = self.option_tipo.get()
            cat = self.combo_cat.get() 

            adicionar_transacao(desc, valor, tipo, cat)

            # Atualiza a lista de categorias e campos
            self.combo_cat.configure(values=listar_categorias())
            self.entry_desc.delete(0, 'end')
            self.entry_valor.delete(0, 'end')
            self.label_saldo.configure(text=f"Saldo Atual: R$ {calcular_saldo():.2f}")
        except ValueError:
            print("Erro: Verifique se o valor está no formato numérico correto.")
        
    def abrir_grafico(self):
        # Busca os dados e chama a análise estatística
        dados = gastos_por_categoria()
        analisar_e_exibir(dados)
    
    def exportar(self):
        caminho = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("Arquivo CSV", "*.csv")]
        )
        
        if caminho:
            exportar_para_csv(caminho)
            print(f"Dados exportados com sucesso para: {caminho}")

    def perguntar_ia(self):
        pergunta = self.entry_ia.get()
        if not pergunta: return
            
        resultado = consultar_com_ia(pergunta)
        
        if isinstance(resultado, list) and len(resultado) > 0:
            valor = resultado[0][0]
        if resultado == "ERRO_SQL":
            messagebox.showerror("Erro", "A IA gerou um comando SQL inválido. Tente perguntar de outra forma.")
            return

        if isinstance(resultado, list) and len(resultado) > 0:
            
            # --- CORREÇÃO AQUI: Verifica se o valor é None antes de formatar ---
            if valor is None:
                res_texto = "Não encontrei registros para essa busca específica."
            elif len(resultado[0]) == 1:
                # Agora só formata se 'valor' não for None
                res_texto = f"O total identificado é: R$ {float(valor):.2f}"
            else:
                res_texto = "Resultados encontrados:\n" + "\n".join([str(r) for r in resultado])
            
            messagebox.showinfo("🤖 Assistente SmartFinance", res_texto)
        else:
            messagebox.showinfo("🤖 Assistente SmartFinance", "A IA não conseguiu encontrar dados ou o comando gerado foi inválido para SQLite.")
if __name__ == "__main__":
    app = App()
    app.mainloop()