from tkinter import *

janela = Tk()
janela.title ('Calculadora Gráfica')
janela.geometry("400x500")
janela.resizable(False, False)
display = Entry(janela, width=20, font = ("Arial", 16))
display.grid(column=0, row=0, columnspan = 4, pady = 20)
botao1 =  Button(janela,text="1",font = ("Arial", 16))
botao1.grid(column=0, row=1)
botao2= Button(janela, text="2", font = ("Arial", 16))
botao2.grid(column=1, row=1)



janela.mainloop()