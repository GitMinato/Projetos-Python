from tkinter import *

janela = Tk()
janela.title("Calculadora Gráfica")
janela.geometry("400x500")
janela.resizable(False, False)

# Variáveis para guardar a operação
primeiro_numero = None
operacao = None
aguardando_novo_numero = False

# Display
display = Entry(janela, width=20, font=("Arial", 16))
display.grid(column=0, row=0, columnspan=4, pady=20)

# Função para quando clicar nos números
def clicar_numero(numero):
    global aguardando_novo_numero
    
    texto_atual = display.get()
    
    # Se estiver aguardando novo número, limpa o display
    if aguardando_novo_numero:
        display.delete(0, END)
        texto_atual = ""
        aguardando_novo_numero = False
    
    display.delete(0, END)
    display.insert(0, texto_atual + numero)

# Função para quando clicar nas operações (+, -, *, /)
def clicar_operacao(op):
    global primeiro_numero, operacao, aguardando_novo_numero
    
    # Guarda o número que está no display
    primeiro_numero = float(display.get())
    # Guarda a operação escolhida
    operacao = op
    # Marca que vamos digitar um novo número
    aguardando_novo_numero = True
    # Limpa o display
    display.delete(0, END)

# Função para quando clicar no =
def calcular():
    global primeiro_numero, operacao, aguardando_novo_numero
    
    if primeiro_numero is not None and operacao is not None:
        segundo_numero = float(display.get())
        
        # Faz o cálculo baseado na operação
        if operacao == '+':
            resultado = primeiro_numero + segundo_numero
        elif operacao == '-':
            resultado = primeiro_numero - segundo_numero
        elif operacao == '*':
            resultado = primeiro_numero * segundo_numero
        elif operacao == '/':
            if segundo_numero != 0:  # Evita divisão por zero
                resultado = primeiro_numero / segundo_numero
            else:
                resultado = "Erro"
        
        # Mostra o resultado
        display.delete(0, END)
        display.insert(0, str(resultado))
        
        # Reseta as variáveis
        primeiro_numero = None
        operacao = None
        aguardando_novo_numero = True

botoes_texto = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'], 
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]

# Criar os botões
for linha in range(4):
    for coluna in range(4):
        texto = botoes_texto[linha][coluna]

        if texto in '0123456789.':
            botoes = Button(janela, text=texto, font=("Arial", 16),
                          command=lambda t=texto: clicar_numero(t))
        elif texto == '=':
            botoes = Button(janela, text=texto, font=("Arial", 16),
                          command=calcular)
        else:  # Operações +, -, *, /
            botoes = Button(janela, text=texto, font=("Arial", 16),
                          command=lambda t=texto: clicar_operacao(t))
        
        botoes.grid(row=linha+1, column=coluna, sticky="nsew")

# Botão C (Limpar)
botao_limpar = Button(janela, text="C", font=("Arial", 16),
                     command=lambda: display.delete(0, END))
botao_limpar.grid(row=5, column=0, columnspan=4, sticky="nsew")

janela.mainloop()