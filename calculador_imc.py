import PySimpleGUI as sg

def calculador_imc():
    
    sg.theme("DarkGrey15")
    
    layout = [
        [sg.Text("Digite seu peso "),sg.Input(size=(13,1),key="-PESO-")],
        [sg.Text("Digite sua altura"),sg.Input(size=(13,1),key="-ALTURA-")],
        [sg.Line()],
        [sg.Button("Calcular"),sg.VerticalLine(),sg.Input(disabled=True,size=(17,1),key="-IMC-")]
    ]
    
    janela = sg.Window("Painel de Resultados", layout)

    while True:
        event, value = janela.read()

        if event == sg.WINDOW_CLOSED:
            break
        
        elif event == "Calcular":
            peso_string = value["-PESO-"]
            altura_string = value['-ALTURA-']
            
            try:
                peso = float(peso_string.replace(",", "."))
                altura = float(altura_string.replace(",", "."))
                
                if peso <= 0 or altura <= 0:
                    sg.popup("Digite valores validos")
                    continue
                    
                imc = peso / (altura ** 2)
                janela["-IMC-"].update(f"{imc:.2f}")
                
            except ValueError:
                sg.popup("Por favor, insira valores numéricos válidos para peso e altura!")
