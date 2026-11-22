from tkinter import *

janela = Tk()
janela.title("Calculadora Gráfica")
janela.geometry("400x500")
janela.resizable(False, False)

display = Entry(janela, width=20, font=("Arial", 16))
display.grid(column=0, row=0, columnspan=4, pady=20)

#Variáveis Globais
numero1 = None
operador = None
numero2 = None
limitador = int(2)
num = float(0)



def clicar_numero (numero):
    # texto_atual = display.get()
    # display.delete(0, END)
    display.insert(END,numero)

def operacao(op):
    global numero1, numero2, operador
    numero1=display.get()
    operador = op
    display.insert(END,operador)

def resultado():
    global limitador, num
    expressao = display.get()
    
    # separa pelo operador
    partes = expressao.split(operador)
    if len(partes) > 2:
        # display.delete(0, END)
        # display.insert(END, "Erro")
        # return
        while limitador < len(partes):
            for i in range(len(partes)):
                num = partes[i]+ num
                limitador +=1
            

    numero1 = float(partes[0])
    numero2 = float(partes[1])

    # Operação
    if operador == "+":
        resultado = numero1 + numero2
    elif operador == "-":
        resultado = numero1 - numero2
    elif operador == "*":
        resultado = numero1 * numero2
    elif operador == "/":
        resultado = numero1 / numero2
    else:
        resultado = "Erro"

    display.delete(0, END)
    display.insert(END, str(resultado))


texto_de_numeros=[
['1','2','3','+'],
['4','5','6','-'],
['7','8','9','*'],
['0','/','.','=']
]

#Criando a grade de teclas
for linha in range(4):
    for coluna in range(4):
        #Gerando o texto para cada botão
        botao_denumeros=texto_de_numeros[linha] [coluna]
        if botao_denumeros in "1234567890": #verificando se está entre 0 - 9
            botao = Button(janela,text=botao_denumeros, font=("Arial", 16),
                            command=lambda t= botao_denumeros: clicar_numero(t))
        elif botao_denumeros in "+-*/": # verificando operadores
                botao = Button(janela,text=botao_denumeros, font=("Arial", 16),
                            command=lambda t= botao_denumeros: operacao(t))
        elif botao_denumeros in "=":
            botao = Button(janela,text=botao_denumeros, font=("Arial", 16),
                           command= lambda: resultado()) 
        else:
            botao = Button(janela,text=botao_denumeros, font=("Arial", 16))
        botao.grid(row=linha+1, column=coluna, sticky="nsew")

#botão para limpar todo o display
botao_zerar=Button(janela,text="C", font=("Arial", 20),
                    command=lambda: display.delete(0, END))
botao_zerar.grid(row=5,column=0,columnspan=2, sticky="nsew")

#botão para limpar apenas um número
botao_limpar = Button(janela,text="<", font=("Arial", 16),
                      command=lambda: display.delete(0))
botao_limpar.grid(row=5, column=2,columnspan=2, sticky="nsew")
        

mainloop()



