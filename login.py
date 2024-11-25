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