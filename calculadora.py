from tkinter import *
from tkinter import messagebox
from tkinter import font

def alterarTextoBt_1():
    lblText["text"] += "1"
def alterarTextoBt_2():
    lblText["text"] += "2"
def alterarTextoBt_3():
    lblText["text"] += "3"
def alterarTextoBt_4():
    lblText["text"] += "4"
def alterarTextoBt_5():
    lblText["text"] += "5"
def alterarTextoBt_6():
    lblText["text"] += "6"
def alterarTextoBt_7():
    lblText["text"] += "7"
def alterarTextoBt_8():
    lblText["text"] += "8"
def alterarTextoBt_9():
    lblText["text"] += "9"
def alterarTextoBt_0():
    lblText["text"] += "0"
def alterarTextoBt_ponto():
    lblText["text"] += "."

valores = ""
def pegarValorDoMAis():
    lblText["text"] += "+"
def pegarValorDoMenos():
    lblText["text"] +="-"
def pegarValorDoDiv():
    lblText["text"] +="/"
def pegarValorDoMult():
    lblText["text"] +="*"

def calcular():

    valores = lblText["text"]
    try:
        resultado = eval(valores)
        lblText["text"] = str(resultado)
        lblOp["text"] = str(valores)+" ="
    except SyntaxError or ZeroDivisionError:
        lblText["text"] = "ERRO"
        lblText.config(fg="#c82d58")

        messagebox.showinfo("ERRO", "Expressão inválida!")
        lblText["text"] = ""
        lblText.config(fg="black")

def apagar():
    textDoLabel = lblText["text"]
    nvText = ""
    cont = 0
    tam = len(textDoLabel)
    if tam > 1:
        while(tam > cont):
            if(cont == (tam-1)):
                break
            else:
                nvText += textDoLabel[cont]
            cont += 1
    else:
        nvText = ""
    lblText["text"] = nvText
    print(textDoLabel)
def limpar():
    lblText["text"] = ""

def novaJanela():
    janela_cient = Toplevel()
    janela_cient.title('Calculadora Científica')
    janela_cient.geometry('400x500+720+300')
    janela_cient.resizable(False, False)
    janela_cient.transient(janela)
    janela_cient.focus_force()
    janela_cient.grab_set()
    #criando botoes na nova janela
    btVoltar = Button(janela_cient, text='Voltar', font='Arial 10 bold', command=janela_cient.destroy)
    btVoltar.place(width=70, height=20, x=0, y=0)


janela = Tk()
janela.title("Calculadora")
janela.geometry("400x500+720+300")
janela.resizable(False, False)

# Imagem do icon
janela.iconbitmap(default="imagens\\designs\\bmo.ico")

imagemFundo = PhotoImage(file="imagens\\designs\\calculadora_semfundo2.0.png")

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
img_Apagar = PhotoImage(file="imagens\\designs\\img.png")


#janela
labFundo = Label(janela, image=imagemFundo)
labFundo.pack()

#posicionando_botoes
bt_1 = Button(janela, bd=0.5, image=img_1,command= alterarTextoBt_1)
bt_1.place(width=45, height=60, x=45, y=145.5)

bt_2 = Button(janela, bd=0.5, image=img_2,command= alterarTextoBt_2)
bt_2.place(width=45, height=60, x=138, y=145.5)

bt_3 = Button(janela, bd=0.5, image=img_3,command= alterarTextoBt_3)
bt_3.place(width=45, height=60, x=231, y=145.5)

bt_4 = Button(janela, bd=0.5, image=img_4,command= alterarTextoBt_4)
bt_4.place(width=45, height=60, x=45, y=241)

bt_5 = Button(janela, bd=0.5, image=img_5,command= alterarTextoBt_5)
bt_5.place(width=45, height=60, x=138, y=241)

bt_6 = Button(janela, bd=0.5, image=img_6,command= alterarTextoBt_6)
bt_6.place(width=45, height=60, x=231, y=241)

bt_7 = Button(janela, bd=0.5, image=img_7,command= alterarTextoBt_7)
bt_7.place(width=45, height=60, x=45, y=336)

bt_8 = Button(janela, bd=0.5, image=img_8,command= alterarTextoBt_8)
bt_8.place(width=45, height=60, x=138, y=336)

bt_9 = Button(janela, bd=0.5, image=img_9,command= alterarTextoBt_9)
bt_9.place(width=45, height=60, x=231, y=336)

bt_0 = Button(janela, bd=0.5, image=img_0,command= alterarTextoBt_0)
bt_0.place(width=45, height=60, x=138, y=430)


# Criando botoes
btIgual = Button(janela,bd= 0.5, image=img_igaul,command= calcular)
btIgual.place(width= 78, height=48, x = 284, y= 442)

btMais = Button(janela,bd= 0.5, image=img_mais, command= pegarValorDoMAis)
btMais.place(width= 45, height=60, x = 317, y= 368)

btMenos = Button(janela,bd= 0.5, image=img_menos,command= pegarValorDoMenos)
btMenos.place(width= 45, height=60, x = 317, y= 294)

btMult = Button(janela,bd= 0.5, image=img_multiplicar, command= pegarValorDoMult)
btMult.place(width= 45, height=60, x = 317, y= 220)

btDividir = Button(janela,bd= 0.5, image=img_dividir, command= pegarValorDoDiv)
btDividir.place(width= 45, height=60, x = 317, y= 146 )

btApagar = Button(janela, bd=0.5, image=img_Apagar, command = apagar )
btApagar.place(width=78, height=48, x=12.5, y= 442)

btLimpar = Button(janela, bd= 0.5, command=  limpar, text="C", font="Arial 15 bold", bg="#2dbec8")
btLimpar.place(width=78, height=48, x=200, y= 442)

btPonto = Button(janela, bd=0.5, text=".", font="Arial 15 bold",command= alterarTextoBt_ponto, bg="#2dbec8")
btPonto.place( width= 45, height=60,x=92, y=430)

btCient = Button(janela, text='Científica', font='Arial 10 bold', command= novaJanela)
btCient.place(width=70, height=20, x=0, y=0)


# criando Label para o texto
lblText = Label(janela,text="", font=("Arial", 25), bg="#B6FFC7", anchor="e",width=2)
lblText.place(width=345, height=100, x=27, y=27)

lblOp = Label(lblText, text="", font=("Calculator 7 bold"), anchor="e", bg="#B6FFC7")
lblOp.place(width=300, height=20, x=30, y=10)


#entrada = Entry(janela, bd = 3, font = ("Arial", 15), justify = CENTER )
#entrada.grid(column =0 , row = 0)
janela.mainloop()


