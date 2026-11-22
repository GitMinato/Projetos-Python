# # import tkinter as tk

# # root = tk.Tk()
# # root.title("Sistema Completo Centralizado")
# # root.geometry("500x400")

# # # Frame principal para agrupar todos os elementos
# # frame_central = tk.Frame(root)
# # frame_central.place(relx=0.5, rely=0.5, anchor="center")

# # # Título
# # label_titulo = tk.Label(
# #     frame_central,
# #     text="Configurações do Sistema",
# #     font=("Arial", 16, "bold")
# # )
# # label_titulo.pack(pady=(0, 20))

# # # Checkboxes
# # var_opcao1 = tk.BooleanVar()
# # var_opcao2 = tk.BooleanVar()
# # var_opcao3 = tk.BooleanVar()

# # checkbox1 = tk.Checkbutton(
# #     frame_central,
# #     text="Ativar notificações por email",
# #     variable=var_opcao1,
# #     font=("Arial", 12)
# # )
# # checkbox1.pack(anchor="w", pady=5)

# # checkbox2 = tk.Checkbutton(
# #     frame_central,
# #     text="Modo escuro",
# #     variable=var_opcao2,
# #     font=("Arial", 12)
# # )
# # checkbox2.pack(anchor="w", pady=5)

# # checkbox3 = tk.Checkbutton(
# #     frame_central,
# #     text="Login automático",
# #     variable=var_opcao3,
# #     font=("Arial", 12)
# # )
# # checkbox3.pack(anchor="w", pady=5)

# # # Linha separadora
# # separador = tk.Frame(frame_central, height=2, bg="gray")
# # separador.pack(fill="x", pady=20)

# # # Botões
# # frame_botoes = tk.Frame(frame_central)
# # frame_botoes.pack(pady=10)

# # btn_salvar = tk.Button(
# #     frame_botoes,
# #     text="Salvar Configurações",
# #     font=("Arial", 10),
# #     width=15
# # )
# # btn_salvar.pack(side="left", padx=5)

# # btn_cancelar = tk.Button(
# #     frame_botoes,
# #     text="Cancelar",
# #     font=("Arial", 10),
# #     width=15
# # )
# # btn_cancelar.pack(side="left", padx=5)

# # # Função para mostrar seleções
# # def mostrar_configuracoes():
# #     configuracoes = []
# #     if var_opcao1.get():
# #         configuracoes.append("Notificações por email")
# #     if var_opcao2.get():
# #         configuracoes.append("Modo escuro")
# #     if var_opcao3.get():
# #         configuracoes.append("Login automático")
    
# #     if configuracoes:
# #         print("Configurações ativas:", ", ".join(configuracoes))
# #     else:
# #         print("Nenhuma configuração ativa")

# # btn_salvar.config(command=mostrar_configuracoes)

# # root.mainloop()

# import tkinter as tk

# root = tk.Tk()
# root.title("Centralização com Frame")
# root.geometry("400x300")

# # 🔑 Configurar a janela principal para expansão
# root.grid_rowconfigure(0, weight=1)
# root.grid_columnconfigure(0, weight=1)

# # Frame que vai conter todo o conteúdo
# frame_central = tk.Frame(root, bg="lightgray")
# frame_central.grid(row=0, column=0, sticky="nsew")

# # Agora organizamos os elementos DENTRO do frame
# checkbox = tk.Checkbutton(
#     frame_central,
#     text="Checkbox no frame centralizado",
#     font=("Arial", 12)
# )
# checkbox.grid(row=0, column=0, pady=20)

# botao = tk.Button(
#     frame_central,
#     text="Botão no frame",
#     font=("Arial", 10)
# )
# botao.grid(row=1, column=0, pady=10)

# root.mainloop()

from tkinter import *

saldo = 1000
saldo_tk = IntVar()
saldo_tk.set(saldo)  # define o valor inicial

def depositar():
    global saldo
    pegar_saldo = display.get()
    
    # Evita erro se o campo estiver vazio
    if pegar_saldo.strip() == "":
        return  
    
    valor_int = int(pegar_saldo)
    saldo += valor_int
    
    saldo_tk.set(saldo)  # 🔹 atualiza o valor mostrado na tela
    display.delete(0, END)  # limpa o campo depois do depósito

def sacar():
    global saldo
    pegar_saldo = display.get()
    
    if pegar_saldo.strip() == "":
        return  
    
    valor_int = int(pegar_saldo)
    saldo -= valor_int
    
    saldo_tk.set(saldo)  # 🔹 atualiza o valor mostrado na tela
    display.delete(0, END)

# --- JANELA ---
janela = Tk()
janela.title("Banco")
janela.geometry("400x400")
janela.resizable(False, False)

texto_usuario = Label(janela, text="Minato", font=("Times New Roman", 25))
texto_usuario.grid(row=1, column=1, pady=20)

texto_dosaldo1 = Label(janela, text="Meu Saldo", font=("Times New Roman", 16))
texto_dosaldo1.grid(row=4, column=1)

texto_dosaldo = Label(janela, text="R$", font=("Times New Roman", 18))
texto_dosaldo.grid(row=4, column=2)

# Label que mostra o saldo em tempo real
Meu_saldo = Label(janela, textvariable=saldo_tk, font=("Times New Roman", 18))
Meu_saldo.grid(row=4, column=3)

display = Entry(janela, font=("Times New Roman", 15))
display.grid(row=6, column=1)

botao_depositar = Button(janela, text="Depositar", font=("Times New Roman", 15), command=depositar)
botao_depositar.grid(row=5, column=1, pady=20)

botao_sacar = Button(janela, text="Sacar", font=("Times New Roman", 15), command=sacar)
botao_sacar.grid(row=5, column=2, pady=20)

janela.mainloop()
