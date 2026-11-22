from tkinter import *
import customtkinter as ctk

saldo=1000


def depositar ():
    global saldo
    pegar_saldo=display.get()
    if pegar_saldo == '':
        return
    
    valor_int= int(pegar_saldo)
    saldo= saldo+valor_int
    saldo_tk.set(saldo)
    display.delete(0, END)

def sacar():
    global saldo
    pegar_saldo=display.get()
    if pegar_saldo == '':
        return
    
    valor_int= int(pegar_saldo)
    if valor_int > saldo:
        print(f"Saldo insuficente!!")
        return

    saldo= saldo-valor_int
    saldo_tk.set(saldo)
    display.delete(0, END)


# def intvar ():
#     saldo_tk=intvar(saldo)

janela=ctk.CTk()
janela.title("Banco")
janela.geometry("400x400")
janela.maxsize(width=700, height=500)
janela.minsize(width=200, height=300)


saldo_tk=IntVar()
saldo_tk.set(saldo)


texto_usuario=ctk.CTkLabel(janela,text="Minato",font=("Times New Roman", 25))
texto_usuario.grid(row=1,column=1,pady=20)

texto_dosaldo1= ctk.CTkLabel(janela,text="Meu Saldo", font=("Times New Roman",16))
texto_dosaldo1.grid(row=4, column=1)

Meu_saldo=ctk.CTkLabel(janela,textvariable=saldo_tk,font=("Times New Roman",18))
Meu_saldo.grid(row=4,column=3)

texto_dosaldo=ctk.CTkLabel(janela,text="R$",font=("Times New Roman", 18))
texto_dosaldo.grid(row=4,column=2)

display = ctk.CTkEntry(janela,font=("Times New Roman",15))
display.grid(row=6, column=1)

botao_depositar=ctk.CTkButton(janela,
    text="Depositar",
        font=("Times New Roman",15),
            command=lambda: depositar())
botao_depositar.grid(row=5,column=1,pady=20)

botao_sacar=ctk.CTkButton(janela,
    text="Sacar",
        font=("Times New Roman",15),
            command=lambda: sacar())
botao_sacar.grid(row=5,column=2,pady=20)


janela.mainloop()