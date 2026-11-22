from tkinter import *

janela = Tk()
janela.title("Calculadora Gráfica")
janela.geometry("400x500")
janela.resizable(False, False)

display = Entry(janela, width=20, font=("Arial", 16))
display.grid(column=0, row=0, columnspan=4, pady=20)

def clicar_numero (numero):
    texto_atual = display.get()
    display.delete(0, END)
    display.insert(0, texto_atual + numero)

botoes_texto = [
    ['7', '8', '9', '/'],    # Linha 0
    ['4', '5', '6', '*'],    # Linha 1  
    ['1', '2', '3', '-'],    # Linha 2
    ['0', '.', '=', '+']     # Linha 3
]
# for linha in range(4):
#     for coluna in range(4):
#         texto = botoes_texto[linha] [coluna]
        
#         # Se for número (0-9) ou ponto (.)
#         if texto in '0123456789.':
#             botoes = Button(janela, text=texto, font=("Arial", 16),
#                           command=lambda t=texto: clicar_numero(t))
#         else:
#             # Operações (por enquanto sem função)
#             botoes = Button(janela, text=texto, font=("Arial", 16))
        
#         botoes.grid(row=linha+1, column=coluna, sticky="nsew")

for linha in range (4):
    for coluna in range (4):
        texto = botoes_texto[linha] [coluna]

        if texto in '0123456789.':      #verifica se é numero(0-9)
            botoes = Button(janela, text=texto, font= ("Arial", 16),
            command=lambda t=texto: clicar_numero(t))
        else: 
            botoes = Button(janela, text=texto, font=("Arial", 16))

        botoes.grid(row=linha+1, column=coluna, sticky="nsew")
botao_limpar = Button(janela, text="C",font=("Arial", 16),
                      command=lambda: display.delete(0, END))
botao_limpar.grid(row=5, column=0, columnspan=4, sticky="nsew")



janela.mainloop()