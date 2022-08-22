from tkinter import *
from tkinter import messagebox


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
    except SyntaxError:
        lblText["text"] = "ERRO"
        lblText.config(fg="#c82d58")

        messagebox.showinfo("ERRO", "Expressão inválida!")
        lblText["text"] = ""
        lblText.config(fg="black")
    except ZeroDivisionError:
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
def limpar():
    lblText["text"] = ""


def novaJanela():
    def alterarTextoBt_1():
        lblText2["text"] += "1"
    def alterarTextoBt_2():
        lblText2["text"] += "2"
    def alterarTextoBt_3():
        lblText2["text"] += "3"
    def alterarTextoBt_4():
        lblText2["text"] += "4"
    def alterarTextoBt_5():
        lblText2["text"] += "5"
    def alterarTextoBt_6():
        lblText2["text"] += "6"
    def alterarTextoBt_7():
        lblText2["text"] += "7"
    def alterarTextoBt_8():
        lblText2["text"] += "8"
    def alterarTextoBt_9():
        lblText2["text"] += "9"
    def alterarTextoBt_0():
        lblText2["text"] += "0"
    def alterarTextoBt_ponto():
        lblText2["text"] += "."

    valores = ""
    def pegarValorDoMAis():
        lblText2["text"] += "!"
    def pegarValorDoMenos():
        lblText2["text"] +="-"
    def pegarValorDoDiv():
        lblText2["text"] +="**"
    def pegarValorDoMult():
        lblText2["text"] +="*"

    def calcular():
        valores = lblText2["text"]
        try:
            resultado = eval(valores)
            lblText2["text"] = str(resultado)
            lblOp2["text"] = str(valores)+" ="
        except SyntaxError:
            lblText2["text"] = "ERRO"
            lblText2.config(fg="#c82d58")

            messagebox.showinfo("ERRO", "Expressão inválida!")
            lblText2["text"] = ""
            lblText2.config(fg="black")
        except ZeroDivisionError:
            lblText2["text"] = "ERRO"
            lblText2.config(fg="#c82d58")

            messagebox.showinfo("ERRO", "Expressão inválida!")
            lblText2["text"] = ""
            lblText2.config(fg="black")

    def apagar():
        textDoLabel = lblText2["text"]
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
        lblText2["text"] = nvText
    def limpar():
        lblText2["text"] = ""
    janela_cient = Toplevel()
    janela_cient.title('Calculadora Científica')
    janela_cient.geometry('400x500+720+300')
    janela_cient.resizable(False, False)
    janela_cient.transient(janela)
    janela_cient.focus_force()
    janela_cient.grab_set()
    #criando botoes na nova janela
    barraMenu = Menu(janela_cient)
    menuVoltar = Menu(barraMenu, tearoff=0)
    menuVoltar.add_command(label='Voltar', command=janela_cient.destroy)
    menuVoltar.add_command(label='Histórico', command=historico)
    barraMenu.add_cascade(label='OPÇÕES', menu=menuVoltar)
    janela_cient.config(menu=barraMenu)
    labFundo = Label(janela_cient, image=imagemFundo)
    labFundo.pack()
    # criando e posicionando botoes dos numeros
    bt_1 = Button( janela_cient, bd=0.5, image=img_1,command=alterarTextoBt_1)
    bt_1.place(width=57, height=84, x=28, y=319)

    bt_2 = Button( janela_cient, bd=0.5, image=img_2,command=alterarTextoBt_2)
    bt_2.place(width=57, height=84, x=111, y=319)

    bt_3 = Button( janela_cient, bd=0.5, image=img_3,command=alterarTextoBt_3)
    bt_3.place(width=57, height=84, x=194, y=319)

    bt_4 = Button( janela_cient, bd=0.5, image=img_4,command=alterarTextoBt_4)
    bt_4.place(width=57, height=84, x=28, y=229)

    bt_5 = Button( janela_cient, bd=0.5, image=img_5,command=alterarTextoBt_5)
    bt_5.place(width=57, height=84, x=111, y=229)

    bt_6 = Button( janela_cient, bd=0.5, image=img_6,command=alterarTextoBt_6)
    bt_6.place(width=57, height=84, x=194, y=229)

    bt_7 = Button( janela_cient, bd=0.5, image=img_7,command=alterarTextoBt_7)
    bt_7.place(width=57, height=84, x=28, y=139.5)

    bt_8 = Button( janela_cient, bd=0.5, image=img_8,command=alterarTextoBt_8)
    bt_8.place(width=57, height=84, x=111, y=139.5)

    bt_9 = Button( janela_cient, bd=0.5, image=img_9,command=alterarTextoBt_9)
    bt_9.place(width=57, height=84, x=194, y=139.5)

    bt_0 = Button( janela_cient, bd=0.5, image=img_0,command=alterarTextoBt_0)
    bt_0.place(width=57, height=84, x=111, y=409)

    # Criando e posixionando botoes das operacoes
    btIgual = Button( janela_cient,bd= 0.8, image=img_igaul,command=calcular)
    btIgual.place(width= 85, height=57, x = 287, y= 437)

    btFator = Button( janela_cient,bd= 0.5, image=img_fatorial, command= pegarValorDoMAis)
    btFator.place(width= 85, height=57, x = 287, y= 375)

    btPorcent = Button( janela_cient,bd= 0.5, image=img_porcentagem,command= pegarValorDoMenos)
    btPorcent.place(width= 85, height=57, x = 287, y= 314)

    btRad = Button( janela_cient,bd= 0.5, image=img_rad, command= pegarValorDoMult)
    btRad.place(width= 85, height=57, x = 287, y= 253)

    btPoten = Button( janela_cient,bd= 0.5, image=img_potencia, command= pegarValorDoDiv)
    btPoten.place(width= 85, height=57, x = 287, y=192)

    btApagar = Button( janela_cient, bd=0.5, image=img_Apagar, command=apagar)
    btApagar.place(width=57, height=84, x=28, y= 409)

    btLimpar = Button( janela_cient, bd= 0.5, command= limpar, image=img_limpar)
    btLimpar.place(width=85, height=57, x=287, y= 132)

    btPonto = Button( janela_cient, bd=0.5, text=".", font="Arial 15 bold",command=alterarTextoBt_ponto,  image=img_ponto)
    btPonto.place( width=57, height=84,x=194, y=409)


    # criando Label para o texto
    lblText2 = Label(janela_cient,text="", font=("Anton 20 bold"), bg="#B6FFC7", anchor="e",width=2)
    lblText2.place(width=345, height=100, x=27, y=27)

    lblOp2 = Label(lblText2, text="", font=("Anton 8 bold"), anchor="e", bg="#B6FFC7")
    lblOp2.place(width=300, height=20, x=30, y=10)

def historico():
    print('')

janela = Tk()
janela.title("Calculadora")
janela.geometry("400x500+720+300")
janela.resizable(False, False)
barraMenu = Menu(janela)
menuOpções = Menu(barraMenu, tearoff=0)
menuOpções.add_command(label='Científica', command=novaJanela)
menuOpções.add_command(label='Histórico', command=historico)
barraMenu.add_cascade(label='OPÇÕES', menu=menuOpções)
janela.config(menu= barraMenu)

#imagens
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
img_mais = PhotoImage(file="imagens\\designs\\adicao.png")
img_menos = PhotoImage(file="imagens\\designs\\subt.png")
img_dividir = PhotoImage(file="imagens\\designs\\div.png")
img_multiplicar = PhotoImage(file="imagens\\designs\\multi.png")
img_Apagar = PhotoImage(file="imagens\\designs\\apagar.png")
img_limpar = PhotoImage(file="imagens\\designs\\C.png")
img_ponto =PhotoImage(file="imagens\\designs\\ponto.png")
img_porcentagem = PhotoImage(file="imagens\\designs\\porcen.png")
img_potencia = PhotoImage(file="imagens\\designs\\poten.png")
img_fatorial = PhotoImage(file="imagens\\designs\\fator.png")
img_rad = PhotoImage(file="imagens\\designs\\radi.png")

# Imagem do icon
janela.iconbitmap(default="imagens\\designs\\bmo.ico")
imagemFundo = PhotoImage(file="imagens\\designs\\calculadora_semfundo3.0.png")
#botoes_numeros


#janela
labFundo = Label(janela, image=imagemFundo)
labFundo.pack()


# criando e posicionando botoes dos numeros
bt_1 = Button(janela, bd=0.5, image=img_1,command=alterarTextoBt_1)
bt_1.place(width=57, height=84, x=28, y=319)

bt_2 = Button(janela, bd=0.5, image=img_2,command=alterarTextoBt_2)
bt_2.place(width=57, height=84, x=111, y=319)

bt_3 = Button(janela, bd=0.5, image=img_3,command=alterarTextoBt_3)
bt_3.place(width=57, height=84, x=194, y=319)

bt_4 = Button(janela, bd=0.5, image=img_4,command=alterarTextoBt_4)
bt_4.place(width=57, height=84, x=28, y=229)

bt_5 = Button(janela, bd=0.5, image=img_5,command=alterarTextoBt_5)
bt_5.place(width=57, height=84, x=111, y=229)

bt_6 = Button(janela, bd=0.5, image=img_6,command=alterarTextoBt_6)
bt_6.place(width=57, height=84, x=194, y=229)

bt_7 = Button(janela, bd=0.5, image=img_7,command=alterarTextoBt_7)
bt_7.place(width=57, height=84, x=28, y=139.5)

bt_8 = Button(janela, bd=0.5, image=img_8,command=alterarTextoBt_8)
bt_8.place(width=57, height=84, x=111, y=139.5)

bt_9 = Button(janela, bd=0.5, image=img_9,command=alterarTextoBt_9)
bt_9.place(width=57, height=84, x=194, y=139.5)

bt_0 = Button(janela, bd=0.5, image=img_0,command=alterarTextoBt_0)
bt_0.place(width=57, height=84, x=111, y=409)

# Criando e posixionando botoes das operacoes
btIgual = Button(janela,bd= 0.8, image=img_igaul,command=calcular)
btIgual.place(width= 85, height=57, x = 287, y= 437)

btMais = Button(janela,bd= 0.5, image=img_mais, command= pegarValorDoMAis)
btMais.place(width= 85, height=57, x = 287, y= 375)

btMenos = Button(janela,bd= 0.5, image=img_menos,command= pegarValorDoMenos)
btMenos.place(width= 85, height=57, x = 287, y= 314)

btMult = Button(janela,bd= 0.5, image=img_multiplicar, command= pegarValorDoMult)
btMult.place(width= 85, height=57, x = 287, y= 253)

btDividir = Button(janela,bd= 0.5, image=img_dividir, command= pegarValorDoDiv)
btDividir.place(width= 85, height=57, x = 287, y=192)

btApagar = Button(janela, bd=0.5, image=img_Apagar, command=apagar)
btApagar.place(width=57, height=84, x=28, y= 409)

btLimpar = Button(janela, bd= 0.5, command= limpar, image=img_limpar)
btLimpar.place(width=85, height=57, x=287, y= 132)

btPonto = Button(janela, bd=0.5, text=".", font="Arial 15 bold",command=alterarTextoBt_ponto,  image=img_ponto)
btPonto.place( width=57, height=84,x=194, y=409)


# criando Label para o texto
lblText = Label(janela,text="", font=("Anton 20 bold"), bg="#B6FFC7", anchor="e",width=2)
lblText.place(width=345, height=100, x=27, y=27)

lblOp = Label(lblText, text="", font=("Anton 8 bold"), anchor="e", bg="#B6FFC7")
lblOp.place(width=300, height=20, x=30, y=10)


janela.mainloop()


