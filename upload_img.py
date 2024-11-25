import PySimpleGUI as sg
import requests

sg.theme("DarkGrey15")

def upload_img():
    
    layout = [
        [sg.Text("Digite a URL da imagem"),sg.Input(key="-URL-")],
        [sg.Text("Digite o nome do arquivo"),sg.Input(key="-NOME_ARQUIVO-")],
        [sg.HorizontalLine()],
        [sg.Button("Baixar imagem PNG"),sg.Button("Baixar imagem JPEG")]
    ]
    
    window = sg.Window("Baixar imagem", layout)
    
    while True:
        event, value = window.read()
        
        if event == sg.WIN_CLOSED:
            break
        
        if event == "Baixar imagem PNG":
            nome_arquivo = value["-NOME_ARQUIVO-"]
            url = value["-URL-"]
            
            try:
                resposta = requests.get(url)
                if resposta.status_code == 200:
                    img_png_path = (f"img_videos/{nome_arquivo}.png")
                    with open (img_png_path, 'wb') as arquivo:
                            
                        arquivo.write(resposta.content)
                        sg.popup(f"Imagem salva com sucesso {nome_arquivo}")
            
                else:
                    sg.popup("Erro ao baixar a imagem")
            
            except Exception as e:
                sg.popup("Erro", e)
                
        elif event == "Baixar imagem JPEG":
            nome_arquivo = value["-NOME_ARQUIVO-"]
            url = value["-URL-"]
            
            try:
                resposta = requests.get(url)
                if resposta.status_code == 200:
                    img_png_path = (f"img_videos/{nome_arquivo}.jpeg")
                    with open (img_png_path, 'wb') as arquivo:
                            
                        arquivo.write(resposta.content)
                        sg.popup(f"Imagem salva com sucesso {nome_arquivo}")
            
                else:
                    sg.popup("Erro ao baixar a imagem")
            
            except Exception as e:
                sg.popup("Erro", e)
    
        