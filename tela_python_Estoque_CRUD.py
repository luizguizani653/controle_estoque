from tkinter import messagebox
import ttkbootstrap as ttk 
from ttkbootstrap.constants import *
import mysql.connector

############# CONEXÃO COM O BANCO DE DADOS ########################
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="300121",
    database="bdluizdev",
)

cursor = conexao.cursor()
####################### FUNÇÃO DA BIBLIOTECA TKINTER PARA CRIAR UMA JANELA ##################

janela = ttk.Window(themename="darkly")
janela.configure()
janela.title("------SISTEMA DE ESTOQUE------") # titulo da janela
janela.geometry("900x600") # tamanho da janela
janela.rowconfigure(1, weight=1) # função para centralizar os componentes da janela
janela.columnconfigure(0, weight=1) # função para centralizar os componentes da janela

frame = ttk.Frame(janela, padding=20)
frame.grid(row=1, column=0,)

ttk.Label(frame, text="SISTEMA DE ESTOQUE", font=("Segoe UI", 20, "bold")).grid(row=0, column=0, columnspan=2, pady=20)

ttk.Label(frame, text="Nome:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_nome_produto = ttk.Entry(frame, width=25) 
entry_nome_produto.grid(row=1, column=1, padx=5, pady=5)

ttk.Label(frame, text="Valor:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
entry_valor = ttk.Entry(frame, width=25)
entry_valor.grid(row=2, column=1, padx=5, pady=5)

ttk.Label(frame, text="Quantidade:").grid(row=3, column=0, padx=5, pady=5, sticky="e")
entry_quantidade = ttk.Entry(frame, width=25)
entry_quantidade.grid(row=3, column=1, padx=5, pady=5)


########################## FUNÇÃO CREATE ######################

def inserir_produto():
    nome_produto = entry_nome_produto.get()
    valor = entry_valor.get()
    quantidade = entry_quantidade.get()

    if not nome_produto or not valor or not quantidade:
        messagebox.showwarning("AVISO!!!", "Produto não inserido, campos em branco!")
        return

    comando ='INSERT INTO venda (nome_produto, valor, quantidade) VALUES (%s, %s, %s)'
    valores = (nome_produto, float(valor), int(quantidade))
    
    cursor.execute(comando, valores,)
    conexao.commit()

    messagebox.showinfo("Success", "Produto inserido com Sucesso! ")

    carregar_dados() #atualiza a tabela automaticamente.

##################### FUNÇÃO READ ###########################

def buscar_produto():
    nome_produto = entry_nome_produto.get()
    tabela.delete(*tabela.get_children())

    comando = 'SELECT idprodutos, nome_produto, valor, quantidade FROM venda WHERE nome_produto LIKE %s'
    valor_busca = (f"%{nome_produto}%",)

    cursor.execute(comando, valor_busca)
    resultados = cursor.fetchall()

    # um aviso caso o programa não localize a consulta.
    if not resultados:
        messagebox.showwarning("AVISO!!!", "Nenhum produto encontrado!")
        return
    
    for linha in resultados:
        tabela.insert("",END, values=linha)


###################### FUNÇÃO UPDATE #########################

def atualizar_produto():
    selecionado = tabela.focus()
    if not selecionado:
        messagebox.showwarning("AVISO!!!", "Nenhum item selecionado!")
        return

    idprodutos = tabela.item(selecionado)["values"][0]
    novo_valor = entry_valor.get().strip()
    novo_nome = entry_nome_produto.get().strip()
    novo_quant = entry_quantidade.get().strip()

    campos = []
    valores = []

    if novo_valor:
        campos.append("valor = %s")
        valores.append(novo_valor)

    if novo_nome:
        campos.append("nome_produto = %s")
        valores.append(novo_nome)

    if novo_quant:
        campos.append("quantidade = %s")
        valores.append(novo_quant)

    if not campos:
        carregar_dados() #atualiza a tabela automaticamente.
        return
    
    query = f"UPDATE venda SET {', '.join(campos)} WHERE idprodutos = %s"
    valores.append(idprodutos)

    try:
        cursor.execute(query, valores) 
        conexao.commit()
        carregar_dados()
        messagebox.showinfo("Success", "Produto atualizado com sucesso!")
    except Exception as e :
        messagebox.showerror("ERROR", f"Erro ao atualizar: {e}")

################## FUNÇÃO DELETE ################################

def deletar_produto():
    selecionado = tabela.focus()
    if not selecionado:
        messagebox.showwarning("AVISO!!!", "Selecione um produto para deletar!")
        return
    
    id_produtos = tabela.item(selecionado)["values"][0]

    if messagebox.askyesno("CONFIRMAÇÃO!!!", "Tem certeza que deseja deletar esse item ?"):
        cursor.execute("DELETE FROM venda WHERE idprodutos = %s",(id_produtos,))
        conexao.commit()

        carregar_dados() #atualiza a tabela automaticamente.
        messagebox.showinfo("Success", "Deletado com Sucesso! ")

frame_botoes = ttk.Frame(janela)
frame_botoes.grid(row=2, column=0)

############ ESQUEMA DE BOTÕES PARA REALIZAR A NAVEGAÇÃO NO PROGRAMA  ##############

ttk.Button(frame_botoes, text="Inserir", bootstyle="success", command=inserir_produto ).grid(row=0, column=0, padx=5)

ttk.Button(frame_botoes, text="Buscar", bootstyle="Success", command=buscar_produto).grid(row=0, column=1, padx=5)

ttk.Button(frame_botoes, text="Atualizar", bootstyle="primary", command=atualizar_produto).grid(row=0, column=2, padx=5)

ttk.Button(frame_botoes, text="Deletar", bootstyle="danger", command=deletar_produto).grid(row=0, column=3, padx=5) 

frame_tabela = ttk.Frame(janela)
frame_tabela.grid(row=3, column=0, pady=20)

######### ESQUEMA DA TABELA DE PRODUTOS #############

tabela = ttk.Treeview(frame_tabela, columns=("ID", "Nome", "Valor", "Quantidade"), show="headings")
tabela.heading("ID", text="Id_produto")
tabela.heading("Nome", text="Nome")
tabela.heading("Valor", text="Valor")
tabela.heading("Quantidade", text="Quantidade")
tabela.grid()

############### FUNÇÃO PARA CARREGAR OS DADOS AO ABRIR O PROGRAMA #############

def carregar_dados():
    tabela.delete(*tabela.get_children())

    comando = "SELECT idprodutos, nome_produto, valor, quantidade FROM venda"
    cursor.execute(comando)
    resultado = cursor.fetchall()

    for linha in resultado:
        tabela.insert("", END, values=linha)

carregar_dados() #faz com que a tabela seja mostrada no programa.

janela.mainloop()

cursor.close()
conexao.close()