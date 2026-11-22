import tkinter as tk
from tkinter import messagebox

class Calculadora:
    def __init__(self):
        # Configuração da janela principal
        self.janela = tk.Tk()
        self.janela.title("Calculadora")
        self.janela.geometry("300x400")
        self.janela.resizable(False, False)
        self.janela.configure(bg='#2C2C2C')
        
        # Variáveis
        self.expressao = ""
        self.entrada_texto = tk.StringVar()
        
        # Criar interface
        self.criar_interface()
        
    def criar_interface(self):
        # Frame para o display
        frame_display = tk.Frame(self.janela, bg='#2C2C2C')
        frame_display.pack(pady=20)
        
        # Display da calculadora
        display = tk.Entry(
            frame_display,
            textvariable=self.entrada_texto,
            font=('Arial', 20),
            justify='right',
            state='readonly',
            bg='#1A1A1A',
            fg='black',
            bd=0,
            relief='flat'
        )
        display.pack(ipady=10, ipadx=10, fill='both')
        
        # Frame para os botões
        frame_botoes = tk.Frame(self.janela, bg='#2C2C2C')
        frame_botoes.pack(expand=True, fill='both', padx=10, pady=10)
        
        # Layout dos botões
        botoes = [
            ['C', '⌫', '%', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['', '0', '.', '=']
        ]
        
        # Criar botões
        for i, linha in enumerate(botoes):
            for j, texto in enumerate(linha):
                if texto:  # Só cria botão se não for string vazia
                    # Definir cores baseadas no tipo de botão
                    if texto in ['C', '⌫']:
                        bg_color = '#FF9500'
                        fg_color = 'white'
                    elif texto in ['/', '*', '-', '+', '=']:
                        bg_color = '#FF9500'
                        fg_color = 'white'
                    elif texto == '%':
                        bg_color = '#A6A6A6'
                        fg_color = 'black'
                    else:
                        bg_color = '#505050'
                        fg_color = 'white'
                    
                    # Criar botão
                    botao = tk.Button(
                        frame_botoes,
                        text=texto,
                        font=('Arial', 16, 'bold'),
                        bg=bg_color,
                        fg=fg_color,
                        bd=0,
                        relief='flat',
                        command=lambda t=texto: self.clique_botao(t)
                    )
                    botao.grid(
                        row=i, 
                        column=j, 
                        padx=2, 
                        pady=2, 
                        sticky='nsew',
                        ipady=15
                    )
        
        # Configurar pesos das linhas e colunas
        for i in range(5):
            frame_botoes.grid_rowconfigure(i, weight=1)
        for j in range(4):
            frame_botoes.grid_columnconfigure(j, weight=1)
    
    def clique_botao(self, valor):
        try:
            if valor == '=':
                # Calcular resultado
                resultado = str(eval(self.expressao))
                self.entrada_texto.set(resultado)
                self.expressao = resultado
            elif valor == 'C':
                # Limpar tudo
                self.expressao = ""
                self.entrada_texto.set("")
            elif valor == '⌫':
                # Apagar último caractere
                self.expressao = self.expressao[:-1]
                self.entrada_texto.set(self.expressao)
            elif valor == '%':
                # Calcular porcentagem
                if self.expressao:
                    try:
                        resultado = str(eval(self.expressao) / 100)
                        self.entrada_texto.set(resultado)
                        self.expressao = resultado
                    except:
                        self.entrada_texto.set("Erro")
                        self.expressao = ""
            else:
                # Adicionar número ou operador
                if self.expressao == "0" and valor.isdigit():
                    self.expressao = valor
                else:
                    self.expressao += str(valor)
                self.entrada_texto.set(self.expressao)
                
        except Exception as e:
            messagebox.showerror("Erro", "Expressão inválida!")
            self.expressao = ""
            self.entrada_texto.set("")
    
    def executar(self):
        # Iniciar a aplicação
        self.janela.mainloop()

# Versão alternativa mais simples (se preferir)
class CalculadoraSimples:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Calculadora Simples")
        
        self.entrada = tk.Entry(self.janela, width=35, borderwidth=5, font=('Arial', 14))
        self.entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        
        # Definir botões
        botoes = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0)
        ]
        
        for (texto, linha, coluna) in botoes:
            tk.Button(
                self.janela,
                text=texto,
                padx=40,
                pady=20,
                font=('Arial', 12),
                command=lambda t=texto: self.botao_clicado(t)
            ).grid(row=linha, column=coluna)
    
    def botao_clicado(self, valor):
        if valor == '=':
            try:
                resultado = str(eval(self.entrada.get()))
                self.entrada.delete(0, tk.END)
                self.entrada.insert(0, resultado)
            except:
                self.entrada.delete(0, tk.END)
                self.entrada.insert(0, "Erro")
        elif valor == 'C':
            self.entrada.delete(0, tk.END)
        else:
            self.entrada.insert(tk.END, valor)
    
    def executar(self):
        self.janela.mainloop()

# Executar a calculadora
if __name__ == "__main__":
    print("Escolha a versão:")
    print("1 - Calculadora Avançada (Recomendada)")
    print("2 - Calculadora Simples")
    
    escolha = input("Digite 1 ou 2: ")
    
    if escolha == "1":
        calc = Calculadora()
    else:
        calc = CalculadoraSimples()
    
    calc.executar()