import yt_dlp
import random
import os
import requests
import PySimpleGUI as sg
from time import sleep

while True:
    os.system('cls')

    print ("Sistema de login!")
    print ('--------------------')
    print ("[1]. Fazer login")
    print ("[2]. Cadastrar")

    escolha_login = input ("Digite sua escolha: ")

    os.system('cls')

    if escolha_login == '1':
        print ("Fazer login!")
        print ('--------------------')
        usuario_none = input("Digite seu nome de usuario: ")
        senha_none = input ("Digite sua senha: ")

        try:
            with open(f'Banco de dados/{usuario_none}.txt', "r") as buscar_credenciais:
                ler = buscar_credenciais.readlines()

                usuario_encontrado = False
                for linha in ler:
                    usuario, email, senha = linha.strip().split(',')

                if usuario_none == usuario and senha_none == senha:
                    usuario_encontrado = True

            if usuario_encontrado:
                os.system('cls')
                print("Logado com sucesso!")
                sleep (2)
                break

            else:
               os.system('cls')
               print ("Usuario nao encontrado")
               sleep (2)

        except FileNotFoundError:
            print ("Usuario nao encontrado")

    elif escolha_login == '2':
        print ("Fazer cadastro")
        print ('--------------------')
        usuario = input("Digite seu nome de usuario: ")
        email = input("Digite seu email: ")
        senha = input ("Digite sua senha: ")

        with open (f'Banco de dados/{usuario}.txt', "w") as cadastro:
            cadastrar = cadastro.write(f'{usuario},{email},{senha}\n')

        print ("Cadastro realizado com sucesso ")
    
def tarefas ():

    def criar_janela_inicial():
        sg.theme('Black')
        layout_tarefa = [
            [sg.Checkbox(''), sg.Input('', border_width=0)]
        ]
        layout = [
            [sg.Frame("Tarefas", layout=layout_tarefa, key='container')],
            [sg.Button("Nova tarefa"),sg.Button("Resetar")]
        ]

        return sg.Window("Tarefas", layout=layout, finalize=True)

    janela = criar_janela_inicial()

    while True:
        event,value = janela.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "Nova tarefa":
            janela.extend_layout(janela["container"], [[sg.Checkbox(''), sg.Input('')]])
        if event == "Resetar":
            janela.close()
            janela = criar_janela_inicial()

def gerador_de_senha():
    class pass_gen:
        def __init__(self):
            sg.theme('Black')
            layout = [
                [sg.Text("Site/Software",size=(10,1)),sg.Input(key="site", size=(21,1))],
                [sg.Text("E-mail/Usuario", size=(10,1)),sg.Input(key="user", size=(21,1))],
                [sg.Text("Quantidade de caracteres", size=(24,1)), sg.Combo(values=list(range(31)),key="total_chars", default_value=1, size=(3,1))],
                [sg.Output(size=(32,5))],
                [sg.Button("Gerar senha")]
            ]

            self.janela = sg.Window("Gerador de senhas", layout)

        def iniciar(self):
            while True:
                event,value = self.janela.read()
                if event == sg.WINDOW_CLOSED:
                    break
                if event == "Gerar senha":
                    nova_senha = self.gerar_senha(value)
                    self.salvar_senha(nova_senha,value)
                    print (nova_senha)

        def gerar_senha(self,value):
            char_list = "ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%¨&*_-"
            chars = random.choices(char_list,k=int(value["total_chars"]))
            new_pass = ''.join(chars)
            return new_pass

        def salvar_senha(self,nova_senha,value):
            with open ("senhas.txt", 'a', newline='') as arquivo:
                arquivo.write(f"site: {value['site']}, usuario {value['user']}, nova senha: {nova_senha}")

            print("Arquivo salvo")

    gen = pass_gen()
    gen.iniciar()

def calculadora ():
    
    os.system ('cls')
    
    def somar (x,y):
        soma = x+y
        print ("O resultado da soma é: ",soma)
        print ("-----------------------------------------")
        return soma;
    
    def subtrair (x,y):
        subtracao = x-y
        print ("O resultado da subtração é: ",subtracao)
        print ("-----------------------------------------")
        return subtracao;
    
    def dividir (x,y):
        divisao = x/y
        print ("O resultado da divisão é: ",divisao)
        print ("-----------------------------------------")
        return divisao;
    
    def multiplicar (x,y):
        multiplicacao = x*y
        print ("O resultado da multiplicação é: ",multiplicacao)
        print ("-----------------------------------------")
        return multiplicacao;
    
    while True:
        print ("[1]. Somar")
        print ("[2]. Subtração")
        print ("[3]. Divisão")
        print ("[4]. Multiplicação")
        print ("[0]. Encerrar programa")
        escolha = int(input("Digite o numero de sua escolha: "))
        
        if escolha == 0:
            break
    
        os.system('cls')
    
        numero_1 = int(input("Digite o primeiro numero: "))
        
        if escolha == 1:
            print ("+")
            
        elif escolha == 2:
            print ("-")
            
        elif escolha == 3:
            print ("/")
            
        elif escolha == 4:
            print ("*")

        numero_2 = int(input("Digite o segundo numero: "))
    
        if escolha == 1:
            somar(numero_1,numero_2)
    
        elif escolha == 2:
            subtrair(numero_1,numero_2)
        
        elif escolha == 3:
            dividir(numero_1,numero_2)
        
        elif escolha == 4:
            multiplicar(numero_1,numero_2)
        
        else:
            print ("Digite uma opção valida ]: ")
    
    return;

def calcular_media ():
    
    os.system ('cls')
    
    def media_turma():
        
        contador = 0
        nota = 0
        
        quantidade_alunos = int(input("Digite a quantidade de alunos: "))
        
        os.system ('cls')
        
        while contador < quantidade_alunos:
            contador += 1
            nota += int(input("Digite a nota do aluno: "))
            
        nota_final = int(nota/quantidade_alunos)
        #developed by vrg8778
        os.system ('cls')
        print ("--------------------------")
        print ("A media da classe é ",nota_final)
        print ("--------------------------")
        
        return;
    
    def media_aluno():
        contador = 0
        nota = 0
        
        quantidade_alunos = int(input("Digite a quantidade de materias: "))
        
        os.system ('cls')
        
        while contador < quantidade_alunos:
            contador += 1
            nota += int(input("Digite a nota da materia: "))
            
        nota_final = int(nota/quantidade_alunos)
        os.system ('cls')
        print ("--------------------------")
        print ("A media do aluno é ",nota_final)
        print ("--------------------------")
        return;
    
    while True:
        
        print ("[1]. Calcular media dos alunos")
        print ("[2]. Calcular media da turma")
        print ("[0]. Encerrar programa")
    
        escolha = int(input("Digite a escolha: "))
    
        if escolha == 1:
            media_aluno()
            
        elif escolha == 2:
            media_turma()
            
        elif escolha == 0:
            break;
        
        else:
            print ("Digite um numero valido!")
    
    return;

def calcular_imc():
    
    os.system ('cls')
    
    print ("Calcular IMC")
    print ("Use ponto e nao virgula")
    print ("---------------------------------------")
    
    peso = float(input("Digite seu peso em KG: "))
    altura = float(input("Digite sua altura em metros: "))
    
    imc = peso / (altura ** 2)
    print (f"Seu IMC é {imc:.2f}")
    
    return;

def conversor_temperatura():
    
    os.system ('cls')
    
    while True:
        print ("[1]. Converter Fahrenheit para Celsius")
        print ("[2]. Converter Celsius para Fahrenheit")
        print ("[0]. Encerrar programa")
    
        escolha = int(input("Digite sua escolha: "))
    
        if escolha == 1:
            f = int(input("Digite o Fahrenheit: "))
            c = (f-32)*5/9
            print (f"{f}°F é igual a {c:.2f}°C")
        
        elif escolha == 2:
            c = int(input("Digite o  Celsius: "))
            f = (c*9/5)+32
            print (f"{c}°C é igual a {f:.2f}°F")
            
        elif escolha == 0:
            break;
        
        else:
            print("Digite uma opção valida")
            
    return;

def baixar_imagem():
    
    os.system ('cls')
    
    url = input("Digite sua URL: ")
    nome_do_arquivo = input("Digite o nome do arquivo:  ")
    
    os.system ('cls')
    
    print ("[1]. Baixar imagem PNG")
    print ("[2]. Baixar imagem JPG")
    
    escolha = int(input("Digite sua escolha: "))
    
    if escolha == 1:
        nome_do_arquivo += ".png"
        
    elif escolha == 2:
        nome_do_arquivo += ".jpg"
        
    
    try:
        resposta = requests.get(url)
        
        if resposta.status_code == 200:
            with open (nome_do_arquivo, 'wb') as arquivo:
                arquivo.write(resposta.content)
            print (f"Imagem salva com sucesso {nome_do_arquivo}")
            
        else:
            print ("Erro ao baixar a imagem")
            
    except Exception as e:
        print ("Erro", e)
    
    return;

def baixar_video_yt():
    
    os.system ('cls')
    
    url = input("digite a URL o video o YouTube: ")
    
    try:
        ydl_opts = {
            'format': 'best', 
            'noplaylist': True
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print ("Baixando...")
            ydl.download([url])
            print("Download concluido!")
        
    except Exception as e:
        print (f"Erro ao fazer download {e}")
    
    return;

def consultar_cep():

    def get_cep(cep):
        
        os.system ('cls')
    
        url = f"https://viacep.com.br/ws/{cep}/json/"
        request = requests.get(url)
        if request.status_code == 200:
            return request.json()
    
        else:
            return {"Erro": "Não foi possivel consultar o CEP"}

    cep = input("Digite seu CEP:")
    resultado = get_cep(cep)

    cep_consulta = resultado["cep"]
    logradouro = resultado["logradouro"]
    bairro = resultado["bairro"]
    localidade = resultado["localidade"]
    uf = resultado["uf"]

    print (f"CEP: {cep_consulta}\nLogradouro: {logradouro}\nBairro: {bairro}\nLocalidade: {localidade}\nUF: {uf}")

while True:
    os.system ('cls')
    print ("-------------------------------------")
    print ("Utilidades") 
    print ("[1]. Calculadora") 
    print ("[2]. Calculador de medias") 
    print ("[3]. Calculador de IMC") 
    print ("[4]. Conversor de temperatura")
    print ("[5]. Baixar imagens")
    print ("[6]. Baixar video Youtube")
    print ("[7]. Gerador de senhas") 
    print ("[8]. Tarefas")
    print ("[9]. Consultar CEP")
    print ("[0]. Encerrar programa")
    
    escolha = int(input("Digite a sua escolha: "))
    
    if escolha == 1:
        calculadora()
        
    elif escolha == 2:
        calcular_media()
        
    elif escolha == 3:
        calcular_imc()
        
    elif escolha == 4:
        conversor_temperatura()
        
    elif escolha == 5:
        baixar_imagem()
        
    elif escolha == 6:
        baixar_video_yt()
        
    elif escolha == 7:
        gerador_de_senha()
        
    elif escolha == 8:
        tarefas()    
        
    elif escolha == 9:
        consultar_cep()
    
    elif escolha == 0:
        break
        
    else:
        print("Digite uma esscolha valida")
        
####### DESENVOLVIDO POR VICTOR GABRIEL F.B. DIAS #######
