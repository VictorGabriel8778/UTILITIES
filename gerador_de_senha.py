import PySimpleGUI as sg
import random

def gerador_de_senha():
    class pass_gen:
        def __init__(self):
            sg.theme("DarkGrey15")
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
            site_name = value['site']
            with open (f"Banco de senhas/{site_name}.txt", 'a', newline='') as arquivo:
                arquivo.write(f"site: {value['site']}\nusuario: {value['user']}\nnova senha: {nova_senha}")

            sg.popup(f"Arquivo salvo: {site_name}.txt")
            
    gen = pass_gen()
    gen.iniciar()
