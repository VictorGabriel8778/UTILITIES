from calculador_imc import calculador_imc
from  calculadora import calculadora
from conversor_temperatura import conversor_temperatura
from gerador_de_senha import gerador_de_senha
from get_cep import take_cep
from tarefas import tarefas
from upload_img import upload_img
from upload_yt import baixar_video_yt
import PySimpleGUI as sg
import os


sg.theme('DarkGrey15')

login_layout = [
    [sg.Text("Area de login - Utilities")],
    [sg.Line()],
    [sg.Text()],
    [sg.Text("User  "),sg.Input(key='user',size= 25)],
    [sg.Text("Senha"),sg.Input(password_char='*',key='senha', size= 25)],
    [sg.Text(size= (0,1))],
    [sg.Button('Entrar'), sg.Button("Cadastro")]
]

cadastro_layout = [
    [sg.Text("Area de cadastro - Utilities")],
    [sg.Line()],
    [sg.Text()],
    [sg.Text("User  "),sg.Input(key='user_cadastro',size= 25)],
    [sg.Text("Senha"),sg.Input(password_char='*',key='senha_cadastro', size= 25)],
    [sg.Text(size= (0,1))],
    [sg.Button('Cadastrar')]
]

window_login = sg.Window('Login', login_layout, size=(300,200))

while True:
    event, values = window_login.read()
    
    if event == sg.WIN_CLOSED:
        break
    
    
    elif event == 'Entrar':
        user_input = values['user']
        senha_input = values['senha']
        file_path = f'Banco de dados/{user_input}.txt'
        
        if os.path.exists(file_path):
            with open (file_path, 'r') as verificar:
                dados = verificar.readline().strip()
                user_salvo, senha_salva = dados.split(',')
                
                if user_input == user_salvo and senha_input == senha_salva:
                    sg.popup("Logado com sucesso!",auto_close=True, auto_close_duration=2)
                    window_login.close()
                    logado = True
                    
                else:
                    sg.Popup("Senha ou usuario incorreto!")
                    
        else:
            sg.popup('Usuario nao encontrado!')
            
    elif event == 'Cadastro':
        window_login.hide()
        window_cadastro = sg.Window('Cadastro', cadastro_layout, size= (300,200))
        while True:
            
            event2, value2 = window_cadastro.read()
            
            if event2 == sg.WIN_CLOSED:
                window_cadastro.close()
                break
            
            elif event2 == 'Cadastrar':
                user_input_cadastro = value2['user_cadastro']
                senha_input_cadastro = value2['senha_cadastro']
                file_path = f'Banco de dados/{user_input_cadastro}.txt'
                
                try:
                    with open(file_path, 'w') as cadastrar:
                        salvar_dados =  cadastrar.write(f'{user_input_cadastro},{senha_input_cadastro}')
                     
                    window_cadastro.close()   
                    sg.popup("Cadastro realizado com sucesso!")
                    window_login.un_hide()
                        
                except:
                    sg.Popup("Erro")

layout_app = [
    [sg.Text("Utilities - APP")],
    [sg.HorizontalLine()],
    [sg.Text("Calculadora                      "),sg.Button("ABRIR", key="-CALCULADORA-")],
    [sg.Line()],
    [sg.Text("Calculador de IMC            "),sg.Button("ABRIR", key="-IMC-")],
    [sg.Line()],
    [sg.Text("Conversor de temperaturas"),sg.Button("ABRIR", key="-CONVERSOR_TEMPERATURA-")],
    [sg.Line()],
    [sg.Text("Gerador de senhas           "),sg.Button("ABRIR", key='-GERADOR_SENHAS-')],
    [sg.Line()],
    [sg.Text("Consultar CEP                 "),sg.Button("ABRIR", key='-GET_CEP-')],
    [sg.Line()],
    [sg.Text("Tarefas                            "),sg.Button("ABRIR", key="-TAREFAS-")],
    [sg.Line()],
    [sg.Text("Baixar videos Youtube      "),sg.Button("ABRIR", key="-UPLOAD_YT-")],
    [sg.Line()],
    [sg.Text("Baixar imagem                 "),sg.Button("ABRIR", key="-UPLOAD_IMG-")],
    [sg.Line()],
    [sg.Text("        Desenvolvido por Vrg8778", text_color="Gray")]
]

if logado == True:
    
    window_app = sg.Window("Utilities - APP", layout_app)
    
    while True:
        event_app, value_app = window_app.read()
        
        if event_app == sg.WIN_CLOSED:
            break
        
        if event_app == '-CALCULADORA-':
            window_app.hide()
            calculadora()
            window_app.un_hide()
            
        elif event_app == '-IMC-':
            window_app.hide()
            calculador_imc()
            window_app.un_hide()
            
        elif event_app == '-CONVERSOR_TEMPERATURA-':
            window_app.hide()
            conversor_temperatura()
            window_app.un_hide()
            
        elif event_app == '-GERADOR_SENHAS-':
            window_app.hide()
            gerador_de_senha()
            window_app.un_hide()
            
        elif event_app == '-GET_CEP-':
            window_app.hide()
            take_cep()
            window_app.un_hide()
            
        elif event_app == '-TAREFAS-':
            window_app.hide()
            tarefas()
            window_app.un_hide()
        
        elif event_app == '-UPLOAD_YT-':
            window_app.hide()
            baixar_video_yt()
            window_app.un_hide()
            
        elif event_app == '-UPLOAD_IMG-':
            window_app.hide()
            upload_img()
            window_app.un_hide()