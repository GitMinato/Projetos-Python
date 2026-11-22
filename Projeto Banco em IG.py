from tkinter import *
import customtkinter as ctk
import time as time

#VARIAVEIS GLOBAIS
nome = ''
senha= ''
salvar_nome = ''
salvar_senha= ''
saldo = 0
usuarios=[{"nome":"aa","senha":"11"}]


Tela_principal=ctk.CTk()
Tela_principal.geometry("400x800")
Tela_principal.title("UniBank")

Frame_principal=Frame(Tela_principal,borderwidth=1,relief="solid",bg="black")
Frame_principal.pack(expand=True, fill="both")

def limpar_frame():
    for widgth in Frame_principal.winfo_children():
        widgth.destroy()

def cadastro():
    limpar_frame()

    def adicinar_usuario():
        pega_usuario=display_user.get()
        pega_senha=display_senha.get()
        if pega_usuario =='' and pega_senha== '':
            mensagem.configure(text="Campos incompletos, preencha todos para se cadastrar.", text_color="light")
        else:
            novo_usuario={"nome":pega_usuario,"senha": pega_senha}
            usuarios.append(novo_usuario)
            mensagem.configure(text="Cadastro Realizado! Seja bem Vindo.",text_color="Green")
            

    tela_cadastro= Frame(Frame_principal,highlightbackground="blue",bg="black", highlightthickness=2)
    tela_cadastro.place(width=399,height=499)


    texto_inicial=ctk.CTkLabel(tela_cadastro,
                               text="Dados para cadastro",
                               font=("JetBrains Mono",18))
    texto_inicial.place(x=30,y=30)

    texto_usuario=ctk.CTkLabel(tela_cadastro,
                               text="Digite o seu nome:",
                               font=("JetBrains Mono",16))
    texto_usuario.place(x=50,y=100)

    display_user=ctk.CTkEntry(tela_cadastro,
                              placeholder_text="Usuario",
                              font=("JetBrains Mono", 15),
                              width=220)
    display_user.place(x=50,y=140)

    texto_senha=ctk.CTkLabel(tela_cadastro,
                             text="Digite uma senha:",
                             font=("JetBrains Mono",16))
    texto_senha.place(x=50,y=220)

    display_senha=ctk.CTkEntry(tela_cadastro,
                               placeholder_text="Senha",
                               font=("JetBrains Mono",15),
                               width=220)
    display_senha.place(x=50, y=260,)

    botao_enviar=ctk.CTkButton(tela_cadastro,
                               text="Enviar",
                               font=(("JetBrains Mono",15)),
                               command=lambda:adicinar_usuario())
    botao_enviar.place(x=50,y=310)

    mensagem=ctk.CTkLabel(tela_cadastro,
                          text='',
                          font=("JetBrains Mono",15))
    mensagem.place(x=50, y=370)

    botao_voltar=ctk.CTkButton(tela_cadastro,
                               text="<- Voltar",
                               font=("JetBrains Mono",15),
                               command=lambda:tela_login())
    botao_voltar.place(x=20,y=450)

def tela_login(): #TELA DE LOGIN !=====!

    limpar_frame()

    def cadastrar_se():
        limpar_frame()
        cadastro()

    
    def enviar():
        global nome, senha, entrada,salvar_nome,salvar_senha
        nome=campo_nome.get()
        # campo_nome.delete(0,END)
        senha=campo_senha.get()
        # campo_senha.delete(0,END)
        if botao_lembrar_me.get()== 1:
            salvar_nome=nome
            salvar_senha=senha
        for usuario in usuarios:
            if usuario["nome"] == nome and usuario["senha"]== senha:
                limpar_frame()
                tela_banco()
            elif usuario["nome"] == nome and usuario["senha"] != senha:
                resultado_login.configure(text="Senha incorreta!",text_color="Red")
            elif usuario["nome"] != nome:
                resultado_login.configure(text="Usuario nao cadastrado",text_color="Red")
                resultado_login2.configure(text="Cadastre-se já aqui em baixo")
            # elif senha == '' or nome == '':
            #     resultado_login.configure(text="Campos incompletos.", text_color="Red")


    Frame_login= Frame(Frame_principal,borderwidth=1,relief="solid",highlightbackground="grey",bg="Black", highlightthickness=2)
    Frame_login.place(x=25,y=25,width=350,height=450)

    #texto do usuario
    textodp1= ctk.CTkLabel(Frame_login,
                           text="Usuario:",
                           font=("JetBrains Mono",18))
    textodp1.place(x=20,y=70)

    #campo de inserir nome
    campo_nome = ctk.CTkEntry(Frame_login,
                              width=300,
                              font=("JetBrains Mono",16),
                              placeholder_text="Nome do Usuario")
    campo_nome.place(x=20,y=100)

    #texto da senha
    textodp2= ctk.CTkLabel(Frame_login,
                           text="Senha:",
                           font=("JetBrains Mono",18))
    textodp2.place(x=20,y=152)

    #campo de inserir senha
    campo_senha = ctk.CTkEntry(Frame_login,show="*",
                               width=300,
                               font=("JetBrains Mono",16),
                               placeholder_text="Senha do Usuario")
    campo_senha.place(x=20,y=182)

    #botao de envio
    botao_enviar= ctk.CTkButton(Frame_login,
                                text="Enviar",
                                font=("JetBrains Mono",14),
                                width=250,bg_color="Black",
                                border_color="white",
                                fg_color="light green",
                                hover_color="#32CD32",
                                text_color="black",
                                text_color_disabled="White",
                                corner_radius=12,
                                command=lambda: enviar())
    botao_enviar.place(x=50,y=250)

    #checkbox para lembrar
    botao_lembrar_me= ctk.CTkCheckBox(Frame_login,
                                      text="Salvar")
    botao_lembrar_me.place(x=120,y=290)

    #mensagem de login
    resultado_login= ctk.CTkLabel(Frame_login,
                                  text='',
                                  font=("JetBrains Mono", 15))
    resultado_login.place(x=80,y=320)

    resultado_login2=ctk.CTkLabel(Frame_login,
                                  text='',
                                  font=("JetBrains Mono", 10))
    resultado_login2.place(x=20,y=380)

    botao_cadastro= ctk.CTkButton(Frame_login,
                                  text="cadastrar-se",
                                  font=("Jetbrains Mono",12),
                                  command=lambda:cadastrar_se())
    botao_cadastro.place(x=15,y=410)

    if salvar_nome:
        campo_nome.insert(0,salvar_nome)
        campo_senha.insert(0,salvar_senha)
 
def tela_banco(): #TELA DO BANCO !=====!
    limpar_frame()

    #funçao para depositar
    def depositar ():
        global saldo
        pegar_saldo=display.get()
        if pegar_saldo == '':
            return
        
        valor_int= int(pegar_saldo)
        saldo= saldo+valor_int
        saldo_tk.set(saldo)
        display.delete(0, END)
        mensagem.configure(text="Deposito Realizado!", text_color="Green")

    #funçao  para sacar
    def sacar():
        global saldo
        pegar_saldo=display.get()
        if pegar_saldo == '':
            return
        
        valor_int= int(pegar_saldo)
        if valor_int > saldo:
            mensagem.configure(text='Saldo insuficiente!', text_color='Red')
            return

        saldo= saldo-valor_int
        saldo_tk.set(saldo)
        display.delete(0, END)
        
   
    Frame_banco=Frame(Frame_principal,bg="black")
    Frame_banco.pack(expand=True, fill="both")

    #variaveis Globais /p tela principal 
    # saldo_tk=IntVar()
    saldo_tk = ctk.StringVar(value=f"R$ {saldo}")
    # FRAMES DO BANCO --------------------------------------------

    #FRAME DO USUARIO
    Frame_user = Frame(Frame_banco,bg="black",
                    #    highlightthickness=2,
                    #    highlightbackground="grey",
                       background="#E0115F")
    Frame_user.place(width=399,height=250)

    #FRAME DISPLAY INTERATIVO
    Frame_display=Frame(Frame_banco,bg="white")
    Frame_display.place(width=400,height=50,y=250)


    #FRAME area_trabalho
    Frame_trabalho=Frame(Frame_banco,bg="white",
                    #   highlightthickness=2,
                    #   highlightbackground="blue",
                      background="#11E04F")
    Frame_trabalho.place(y=300,width=399,height=400,)
    # FRAME DE BOTOES DA ESQUERDA
    Frame_botoes_esquerdo=Frame(Frame_trabalho,bg="white",)
                    #    highlightthickness=2,
                    #    highlightbackground="purple")
    Frame_botoes_esquerdo.place(x=0,width=200,height=400)
    #FRAME DE BOTOES DA DIREITA
    Frame_botoes_direita=Frame(Frame_trabalho,bg="white",
                        #  highlightthickness=2,
                        #  highlightbackground="green")
    )
    Frame_botoes_direita.place(x=200,width=200,height=400)

    Frame_openfinance=Frame(Frame_banco,bg="white")
    Frame_openfinance.place(width=400,height=100,y=700)



    texto_bradesco=ctk.CTkLabel(Frame_user,
                                text="Bradesco",
                                font=("Arial",22))
    texto_bradesco.place(x=150,y=30)

    texto_usuario=ctk.CTkLabel(Frame_user,
                               text=f"Olá {nome}",
                               font=("Font Awesome 6 Free Solid", 20))
    texto_usuario.place(x=30,y=100)

    # texto_linha=ctk.CTkLabel(Frame_user,
    #                          text="------------------")

    texto_dosaldo1= ctk.CTkLabel(Frame_user,
                                 text="meu saldo disponivel",
                                 font=("Arial",18))
    texto_dosaldo1.place(x=30,y=170)

    Meu_saldo=ctk.CTkLabel(Frame_user,
                           textvariable=saldo_tk,
                           font=("Arial",20))
    Meu_saldo.place(x=30,y=200)

    # texto_dosaldo=ctk.CTkLabel(Frame_user,
    #                            text="R$",
    #                            font=("JetBrains Mono", 26))
    # texto_dosaldo.place(x=70,y=40)

    display = ctk.CTkEntry(Frame_display,
                           font=("JetBrains Mono",15),
                           width=300,
                           height=40,
                           placeholder_text="Valores",
                           placeholder_text_color="Black",
                           bg_color="#FFFFFF",
                           corner_radius=20,
                           fg_color="white")
    display.place(x=50,y=5)

    #BOTOES E FUNÇOES -----------
    #BOTOES DA DIREITA
    botao_sacar=ctk.CTkButton(Frame_botoes_direita,
                              text="Sacar",
                              font=("JetBrains Mono",15),
                              corner_radius=10,
                              width=180,
                              height=80,
                              command=lambda: sacar(),)
    botao_sacar.place(x=10,y=100)

    botao_transferir=ctk.CTkButton(Frame_botoes_direita,
                                   text="Transferir",
                                   font=("JetBrains Mono",15),
                                   corner_radius=10,
                                   width=180,
                                   height=80,
                                   command=lambda:tela_transferencia())
    botao_transferir.place(x=10,y=200)

    botao_transferir=ctk.CTkButton(Frame_botoes_direita,
                                   text="Transferir",
                                   font=("JetBrains Mono",15),
                                   corner_radius=10,
                                   width=180,
                                   height=80,
                                   command=lambda:tela_transferencia())
    botao_transferir.place(x=10,y=200)

    botao_Investimento=ctk.CTkButton(Frame_botoes_direita,
                                   text="Investimentos",
                                   font=("JetBrains Mono",15),
                                   corner_radius=10,
                                   width=180,
                                   height=80,
                                   )
    botao_Investimento.place(x=10,y=300)
    
    #BOTOES DA ESQUERDA
    botao_depositar=ctk.CTkButton(Frame_botoes_esquerdo,
                                  text="Depositar",
                                  font=("Arial",15),
                                  corner_radius=10,
                                  command=lambda: depositar(),
                                  width=180,
                                  height=80,
                                  border_width=2,
                                  border_color="#373738",
                                  fg_color="#cfcfcf",
                                  text_color="Black",
                                  hover_color="#A0A0A0")
    botao_depositar.place(x=20,y=100)

    botao_pagamentos=ctk.CTkButton(Frame_botoes_esquerdo,
                                   text="Pagamentos",
                                   font=("Arial",15),
                                   corner_radius=10,
                                   width=180,
                                   height=80)
    botao_pagamentos.place(x=20,y=200)

    botao_cartaoes=ctk.CTkButton(Frame_botoes_esquerdo,
                                   text="Cartões",
                                   font=("Arial",15),
                                   corner_radius=10,
                                   width=180,
                                   height=80)
    botao_cartaoes.place(x=20,y=300)

    botao_openfinance=ctk.CTkButton(Frame_openfinance,
                                    text="Open Finance Bradesco",
                                    font=("Arial",16),
                                    corner_radius=10,
                                    fg_color="White",
                                    text_color="Black",
                                    hover_color="#A0A0A0",
                                    border_width=2,
                                    border_color="Black",
                                    width=350,
                                    height=70)
    botao_openfinance.place(x=25,y=10)


    botao_logout=ctk.CTkButton(Frame_user,
                               text="Sair",
                               font=("JetBrains Mono",15),
                               width=40,
                               fg_color="#E0115F",
                               hover_color="#E0115F",
                               command=lambda:tela_login())
    botao_logout.place(x=300,y=100)

    mensagem = ctk.CTkLabel(Frame_user,
                            text="",
                            font=("JetBrains Mono", 15),
                            width=30)
    mensagem.place(row=7,column=1)

    # menu=ctk.CTkProgressBar(Frame_botoes,orientation="horizontal")
    # menu.place(x=50,y=30)

def tela_transferencia(): #TELA DE TRANSFERENCIA BANCARIA!=====!
    limpar_frame()
    #
    #
    #
    #

    Frame_transferencia=Frame(Frame_principal,borderwidth=1,relief="solid",highlightbackground="grey",bg="black", highlightthickness=2)
    Frame_transferencia.pack(expand=True, fill="both")

    voltar=ctk.CTkButton(Frame_transferencia,
            text="Voltar",
                font=("JetBrains Mono",15),
                    command=lambda:tela_banco())
    voltar.place(x=30,y=100)

tela_login()
Tela_principal.mainloop()