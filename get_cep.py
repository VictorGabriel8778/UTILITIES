import requests
import os
import PySimpleGUI as sg

def get_cep(cep):
    
    url = f"https://viacep.com.br/ws/{cep}/json/"
    request = requests.get(url)
    
    if request.status_code == 200:
        resultado = request.json()
        
        if "erro" in resultado:
            sg.popup("Erro: CEP nao encontrado")
            return None
        return resultado
    
    else:
        sg.popup("Nao foi possivel consultar o seu CEP")
        return None

def take_cep():
    
    sg.theme("DarkGrey15")
    
    layout = [
        [sg.Text("Digite seu CEP"), sg.Input(key="-CEP-", size=(20,1))],
        [sg.Line()],
        [sg.Button("Consultar CEP"),sg.Button("Sair")]
    ]
    
    window = sg.Window("Consultar CEP", layout)
    
    
    while True:
        event, value = window.read()
        
        if event == sg.WINDOW_CLOSED  or event == "Sair":
            break
        
        if event == "Consultar CEP":
            cep = str(value["-CEP-"])
                
            resultado = get_cep(cep)
            
            if resultado:
                cep_consulta = resultado.get("cep", "N/A")
                logradouro = resultado.get("logradouro", "N/A")
                bairro = resultado.get("bairro", "N/A")
                localidade = resultado.get("localidade", "N/A")
                uf = resultado.get("uf", "N/A")
                
                sg.popup (f"CEP: {cep_consulta}\nLogradouro: {logradouro}\nBairro: {bairro}\nLocalidade: {localidade}\nUF: {uf}")
                
    window.close()
    