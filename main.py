import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
import csv

class Produto:
    def __init__(self, nome, quantidade, preco_compra, preco_venda, icms, pis, cofins, credito, debito):
        self.nome = nome
        self.quantidade = quantidade
        self.preco_compra = preco_compra
        self.preco_venda = preco_venda
        self.icms = icms
        self.pis = pis
        self.cofins = cofins
        self.credito = credito
        self.debito = debito

    def calcular_custo(self):
        return self.preco_compra + self.icms + self.pis + self.cofins

    def calcular_lucro(self):
        custo = self.calcular_custo()
        receita = self.preco_venda * self.quantidade
        despesa = custo * self.quantidade
        return receita - despesa

class SistemaDeGestao:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Sistema de Gestão")
        self.produtos = []

        # Tela de Abertura do Sistema
        self.abertura_label = tk.Label(self.root, text="Bem-vindo ao Sistema de Gestão", font=("Helvetica", 16))
        self.abertura_label.pack(pady=20)

        # Botões para acessar funcionalidades
        self.cadastrar_produto_button = tk.Button(self.root, text="Cadastrar Produto", command=self.abrir_janela_cadastro)
        self.cadastrar_produto_button.pack()

        self.calcular_custo_button = tk.Button(self.root, text="Calcular Custos", command=self.calcular_custos)
        self.calcular_custo_button.pack()

        self.vender_produto_button = tk.Button(self.root, text="Vender Produto", command=self.vender_produto)
        self.vender_produto_button.pack()

        self.calcular_lucro_button = tk.Button(self.root, text="Calcular Lucro", command=self.calcular_lucro)
        self.calcular_lucro_button.pack()

        self.alocar_despesa_button = tk.Button(self.root, text="Alocar Como Despesa", command=self.alocar_despesa)
        self.alocar_despesa_button.pack()

        self.gerar_dre_button = tk.Button(self.root, text="Gerar DRE", command=self.gerar_dre)
        self.gerar_dre_button.pack()

        self.gerar_pl_button = tk.Button(self.root, text="Gerar PL", command=self.gerar_pl)
        self.gerar_pl_button.pack()

        # Botão para importar dados de CSV
        self.importar_csv_button = tk.Button(self.root, text="Importar CSV", command=self.importar_csv)
        self.importar_csv_button.pack()

    def abrir_janela_cadastro(self):
        janela_cadastro = tk.Toplevel(self.root)
        janela_cadastro.title("Cadastrar Produto")

        nome_label = tk.Label(janela_cadastro, text="Nome do produto:")
        nome_label.pack()
        nome_entry = tk.Entry(janela_cadastro)
        nome_entry.pack()

        quantidade_label = tk.Label(janela_cadastro, text="Quantidade:")
        quantidade_label.pack()
        quantidade_entry = tk.Entry(janela_cadastro)
        quantidade_entry.pack()

        preco_compra_label = tk.Label(janela_cadastro, text="Preço de compra:")
        preco_compra_label.pack()
        preco_compra_entry = tk.Entry(janela_cadastro)
        preco_compra_entry.pack()

        preco_venda_label = tk.Label(janela_cadastro, text="Preço de venda:")
        preco_venda_label.pack()
        preco_venda_entry = tk.Entry(janela_cadastro)
        preco_venda_entry.pack()

        icms_label = tk.Label(janela_cadastro, text="ICMS:")
        icms_label.pack()
        icms_entry = tk.Entry(janela_cadastro)
        icms_entry.pack()

        pis_label = tk.Label(janela_cadastro, text="PIS:")
        pis_label.pack()
        pis_entry = tk.Entry(janela_cadastro)
        pis_entry.pack()

        cofins_label = tk.Label(janela_cadastro, text="COFINS:")
        cofins_label.pack()
        cofins_entry = tk.Entry(janela_cadastro)
        cofins_entry.pack()

        credito_label = tk.Label(janela_cadastro, text="Crédito:")
        credito_label.pack()
        credito_entry = tk.Entry(janela_cadastro)
        credito_entry.pack()

        debito_label = tk.Label(janela_cadastro, text="Débito:")
        debito_label.pack()
        debito_entry = tk.Entry(janela_cadastro)
        debito_entry.pack()

        cadastrar_button = tk.Button(janela_cadastro, text="Cadastrar",
                                     command=lambda: self.cadastrar_produto(
                                         nome_entry.get(),
                                         int(quantidade_entry.get()),
                                         float(preco_compra_entry.get()),
                                         float(preco_venda_entry.get()),
                                         float(icms_entry.get()),
                                         float(pis_entry.get()),
                                         float(cofins_entry.get()),
                                         float(credito_entry.get()),
                                         float(debito_entry.get())
                                     ))
        cadastrar_button.pack()

    def cadastrar_produto(self, nome, quantidade, preco_compra, preco_venda, icms, pis, cofins, credito, debito):
        produto = Produto(nome, quantidade, preco_compra, preco_venda, icms, pis, cofins, credito, debito)
        self.produtos.append(produto)
        messagebox.showinfo("Cadastro de Produto", "Produto cadastrado com sucesso.")

    def calcular_custos(self):
        # Crie uma janela separada para mostrar os custos dos produtos
        janela_custos = tk.Toplevel(self.root)
        janela_custos.title("Custos dos Produtos")

        for produto in self.produtos:
            custo = produto.calcular_custo()
            label = tk.Label(janela_custos, text=f"{produto.nome}: R$ {custo:.2f}")
            label.pack()

    def vender_produto(self):
        # Crie uma janela para selecionar um produto para venda
        if not self.produtos:
            messagebox.showwarning("Vender Produto", "Nenhum produto cadastrado.")
            return

        janela_venda = tk.Toplevel(self.root)
        janela_venda.title("Vender Produto")

        produtos_var = tk.StringVar()
        produtos_var.set("Selecione um produto:")
        produtos_menu = tk.OptionMenu(janela_venda, produtos_var, *[""] + [produto.nome for produto in self.produtos])
        produtos_menu.pack()

        quantidade_label = tk.Label(janela_venda, text="Quantidade:")
        quantidade_label.pack()
        quantidade_entry = tk.Entry(janela_venda)
        quantidade_entry.pack()

        vender_button = tk.Button(janela_venda, text="Vender", command=lambda: self.realizar_venda(produtos_var.get(), quantidade_entry.get()))
        vender_button.pack()

    def realizar_venda(self, nome_produto, quantidade):
        if not nome_produto:
            messagebox.showwarning("Vender Produto", "Selecione um produto.")
            return

        try:
            quantidade = int(quantidade)
            if quantidade <= 0:
                raise ValueError()
        except ValueError:
            messagebox.showerror("Vender Produto", "Quantidade inválida.")
            return

        produto = next((p for p in self.produtos if p.nome == nome_produto), None)
        if not produto:
            messagebox.showerror("Vender Produto", "Produto não encontrado.")
            return

        if quantidade > produto.quantidade:
            messagebox.showerror("Vender Produto", "Quantidade insuficiente em estoque.")
            return

        # Realize a venda
        produto.quantidade -= quantidade
        messagebox.showinfo("Vender Produto", f"{quantidade} unidades de {produto.nome} vendidas com sucesso.")

    def calcular_lucro(self):
        # Crie uma janela para selecionar um produto para calcular o lucro
        if not self.produtos:
            messagebox.showwarning("Calcular Lucro", "Nenhum produto cadastrado.")
            return

        produto_nome = simpledialog.askstring("Calcular Lucro", "Digite o nome do produto:")
        produto = next((p for p in self.produtos if p.nome == produto_nome), None)

        if not produto:
            messagebox.showerror("Calcular Lucro", "Produto não encontrado.")
            return

        lucro = produto.calcular_lucro()
        messagebox.showinfo("Calcular Lucro", f"Lucro do produto {produto.nome}: R$ {lucro:.2f}")

    def alocar_despesa(self):
        # Crie uma janela para selecionar um produto para alocar como despesa
        if not self.produtos:
            messagebox.showwarning("Alocar Despesa", "Nenhum produto cadastrado.")
            return

        janela_alocar_despesa = tk.Toplevel(self.root)
        janela_alocar_despesa.title("Alocar Despesa")

        produtos_var = tk.StringVar()
        produtos_var.set("Selecione um produto:")
        produtos_menu = tk.OptionMenu(janela_alocar_despesa, produtos_var, *[""] + [produto.nome for produto in self.produtos])
        produtos_menu.pack()

        alocar_button = tk.Button(janela_alocar_despesa, text="Alocar Como Despesa", command=lambda: self.alocar_produto_como_despesa(produtos_var.get()))
        alocar_button.pack()

    def alocar_produto_como_despesa(self, nome_produto):
        if not nome_produto:
            messagebox.showwarning("Alocar Despesa", "Selecione um produto.")
            return

        produto = next((p for p in self.produtos if p.nome == nome_produto), None)
        if not produto:
            messagebox.showerror("Alocar Despesa", "Produto não encontrado.")
            return

        # Aqui você pode implementar a lógica para alocar o produto como despesa.
        # Por exemplo, você pode ter uma lista de despesas e adicionar o produto a essa lista.
        # Você também pode atualizar seu modelo de dados ou arquivo CSV, conforme necessário.

        messagebox.showinfo("Alocar Despesa", f"{produto.nome} alocado como despesa com sucesso.")

    def gerar_dre(self):
        # Crie uma janela para selecionar o período (mês/ano) para o DRE
        periodo = simpledialog.askstring("Gerar DRE", "Digite o período (mês/ano) para o DRE (por exemplo, 'Janeiro/2023'):")
        if not periodo:
            messagebox.showwarning("Gerar DRE", "Período não informado.")
            return

        # Crie uma janela para selecionar os produtos a serem incluídos no DRE
        if not self.produtos:
            messagebox.showwarning("Gerar DRE", "Nenhum produto cadastrado.")
            return

        janela_selecionar_produtos = tk.Toplevel(self.root)
        janela_selecionar_produtos.title("Selecionar Produtos para o DRE")

        produtos_var = tk.StringVar()
        produtos_var.set("Selecione os produtos para incluir no DRE (segure Ctrl para selecionar vários):")
        produtos_listbox = tk.Listbox(janela_selecionar_produtos, selectmode=tk.MULTIPLE)
        for produto in self.produtos:
            produtos_listbox.insert(tk.END, produto.nome)
        produtos_listbox.pack()

        gerar_button = tk.Button(janela_selecionar_produtos, text="Gerar DRE", command=lambda: self.gerar_relatorio_dre(periodo, produtos_listbox.curselection()))
        gerar_button.pack()

    def gerar_relatorio_dre(self, periodo, produtos_selecionados):
        # Verifique se pelo menos um produto foi selecionado
        if not produtos_selecionados:
            messagebox.showwarning("Gerar DRE", "Selecione pelo menos um produto para incluir no DRE.")
            return

        # Inicialize as variáveis para calcular receitas, custos e despesas
        total_receitas = 0
        total_custos = 0
        total_despesas = 0

        # Calcule as receitas, custos e despesas para cada produto selecionado
        for index in produtos_selecionados:
            produto = self.produtos[int(index)]
            receitas_produto = produto.preco_venda * produto.quantidade
            custos_produto = produto.calcular_custo() * produto.quantidade

            # Você pode implementar a lógica para as despesas aqui, se necessário
            # Por exemplo, você pode ter uma lista de despesas associadas a cada produto

            total_receitas += receitas_produto
            total_custos += custos_produto

        # Calcule o lucro líquido
        lucro_liquido = total_receitas - total_custos - total_despesas

        # Crie uma janela para exibir o relatório do DRE
        janela_dre = tk.Toplevel(self.root)
        janela_dre.title(f"DRE - {periodo}")

        # Exiba as informações do DRE na janela
        label_periodo = tk.Label(janela_dre, text=f"Período: {periodo}")
        label_periodo.pack()

        label_receitas = tk.Label(janela_dre, text=f"Receitas: R$ {total_receitas:.2f}")
        label_receitas.pack()

        label_custos = tk.Label(janela_dre, text=f"Custos: R$ {total_custos:.2f}")
        label_custos.pack()

        label_despesas = tk.Label(janela_dre, text=f"Despesas: R$ {total_despesas:.2f}")
        label_despesas.pack()

        label_lucro_liquido = tk.Label(janela_dre, text=f"Lucro Líquido: R$ {lucro_liquido:.2f}")
        label_lucro_liquido.pack()

    def gerar_pl(self):
        # Calcule o Patrimônio Líquido (PL) aqui
        if not self.produtos:
            messagebox.showwarning("Gerar PL", "Nenhum produto cadastrado.")
            return

        # Você pode implementar a lógica para calcular o PL com base nos dados do seu sistema
        # Aqui, vou calcular o PL como a diferença entre o ativo (receitas) e o passivo (custos + despesas)

        # Calcule o ativo (receitas)
        ativo = sum(produto.preco_venda * produto.quantidade for produto in self.produtos)

        # Calcule o passivo (custos + despesas)
        passivo = sum(produto.calcular_custo() * produto.quantidade for produto in self.produtos)

        # Calcule o Patrimônio Líquido (PL)
        patrimonio_liquido = ativo - passivo

        # Crie uma janela para exibir o Patrimônio Líquido (PL)
        janela_pl = tk.Toplevel(self.root)
        janela_pl.title("Patrimônio Líquido (PL)")

        # Exiba o valor do Patrimônio Líquido (PL)
        label_pl = tk.Label(janela_pl, text=f"Patrimônio Líquido (PL): R$ {patrimonio_liquido:.2f}")
        label_pl.pack()

    def importar_csv(self):
        # Abrir uma janela de diálogo para selecionar o arquivo CSV
        file_path = filedialog.askopenfilename(filetypes=[("Arquivos CSV", "*.csv")])

        if file_path:
            try:
                # Use a biblioteca csv para ler o arquivo CSV e importar os dados
                with open(file_path, 'r', newline='') as file:
                    reader = csv.reader(file)
                    next(reader)  # Pule a linha de cabeçalho, se houver

                    for row in reader:
                        nome, quantidade, preco_compra, preco_venda, icms, pis, cofins, credito, debito = row
                        produto = Produto(
                            nome,
                            int(quantidade),
                            float(preco_compra),
                            float(preco_venda),
                            float(icms),
                            float(pis),
                            float(cofins),
                            float(credito),
                            float(debito)
                        )
                        self.produtos.append(produto)

                messagebox.showinfo("Importar CSV", "Dados CSV importados com sucesso.")
            except Exception as e:
                messagebox.showerror("Erro ao Importar CSV", str(e))

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = SistemaDeGestao()
    app.run()