from turtle import width
from operacoes import *
from tkinter import *


janela = Tk()
janela.title("Calculadora")
janela.geometry("400x500+720+300")

# Imagem do icon
janela.iconbitmap(default="imagens\\designs\\bmo.ico")

imagemFundo = PhotoImage(file="imagens\\designs\\calculadora_semfundo.png")

#botoes_numeros
img_1 = PhotoImage(file='imagens\\designs\\1.png')
img_2 = PhotoImage(file='imagens\\designs\\2.png')
img_3 = PhotoImage(file='imagens\\designs\\3.png')
img_4 = PhotoImage(file='imagens\\designs\\4.png')
img_5 = PhotoImage(file='imagens\\designs\\5.png')
img_6 = PhotoImage(file='imagens\\designs\\6.png')
img_7 = PhotoImage(file='imagens\\designs\\7.png')
img_8 = PhotoImage(file='imagens\\designs\\8.png')
img_9 = PhotoImage(file='imagens\\designs\\9.png')
img_0 = PhotoImage(file='imagens\\designs\\0.png')

img_igaul = PhotoImage(file="imagens\\designs\\igual.png")
img_mais = PhotoImage(file="imagens\\designs\\+.png")
img_menos = PhotoImage(file="imagens\\designs\\-.png")
img_dividir = PhotoImage(file="imagens\\designs\\divi.png")
img_multiplicar = PhotoImage(file="imagens\\designs\\multi.png")


#janela
labFundo = Label(janela, image=imagemFundo)
labFundo.pack()

#posicionando_botoes
bt_1 = Button(janela, bd=0.5, image=img_1)
bt_1.place(width=45, height=60, x=45, y=145.5)

bt_2 = Button(janela, bd=0.5, image=img_2)
bt_2.place(width=45, height=60, x=138, y=145.5)

bt_3 = Button(janela, bd=0.5, image=img_3)
bt_3.place(width=45, height=60, x=231, y=145.5)

bt_4 = Button(janela, bd=0.5, image=img_4)
bt_4.place(width=45, height=60, x=45, y=241)

bt_5 = Button(janela, bd=0.5, image=img_5)
bt_5.place(width=45, height=60, x=138, y=241)

bt_6 = Button(janela, bd=0.5, image=img_6)
bt_6.place(width=45, height=60, x=231, y=241)

bt_7 = Button(janela, bd=0.5, image=img_7)
bt_7.place(width=45, height=60, x=45, y=336)

bt_8 = Button(janela, bd=0.5, image=img_8)
bt_8.place(width=45, height=60, x=138, y=336)

bt_9 = Button(janela, bd=0.5, image=img_9)
bt_9.place(width=45, height=60, x=231, y=336)

bt_0 = Button(janela, bd=0.5, image=img_0)
bt_0.place(width=45, height=60, x=138, y=430)


# Criando botoes
btIgual = Button(janela,bd= 0.5, image=img_igaul)
btIgual.place(width= 78, height=48, x = 284, y= 442)

btMais = Button(janela,bd= 0.5, image=img_mais)
btMais.place(width= 45, height=60, x = 317, y= 368)

btMenos = Button(janela,bd= 0.5, image=img_menos)
btMenos.place(width= 45, height=60, x = 317, y= 294)

btMult = Button(janela,bd= 0.5, image=img_multiplicar)
btMult.place(width= 45, height=60, x = 317, y= 220)

btDividir = Button(janela,bd= 0.5, image=img_dividir)
btDividir.place(width= 45, height=60, x = 317, y= 146 )


#entrada = Entry(janela, bd = 3, font = ("Arial", 15), justify = CENTER )
#entrada.grid(column =0 , row = 0)
janela.mainloop()