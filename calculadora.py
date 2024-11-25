import PySimpleGUI as sg

sg.theme("DarkGrey15")

def calculadora():
    
    layout_calculadora = [
        [sg.Input("0",font=("Helvetica",20),size=(15,1), key=("-Display-")),sg.Button("=",size=(3,1),font=("Helvetica",15))],
        [sg.HorizontalSeparator()],
        [sg.Button("7", size=(7,3)),sg.Button("8", size=(7,3)),sg.Button("9", size=(7,3)),sg.Button("+", size=(7,3))],
        [sg.Button("4", size=(7,3)),sg.Button("5", size=(7,3)),sg.Button("6", size=(7,3)),sg.Button("-", size=(7,3))],   
        [sg.Button("1", size=(7,3)),sg.Button("2", size=(7,3)),sg.Button("3", size=(7,3)),sg.Button("%", size=(7,3))],
        [sg.Button(".", size=(7,3)),sg.Button("0", size=(7,3)),sg.Button("C", size=(7,3)),sg.Button("*", size=(7,3))]
    ]
    
    window = sg.Window("Calculadora", layout_calculadora)
    
    valor_atual = "0"
    
    while True:
        event, values = window.read()
    
        if event == sg.WIN_CLOSED:
            break
        
        if event in "1234567890+-*%.":
            valor_atual = values["-Display-"]
            novo_valor = valor_atual + event if valor_atual != "0" else event
            valor_atual = novo_valor
            window["-Display-"].Update(novo_valor)
            
        elif event == "C":
            valor_atual = "0"
            window["-Display-"].Update(valor_atual)
            
        elif event == "=":
            try:
                resultado = eval(valor_atual)
                valor_atual = str(resultado)
                window["-Display-"].Update(valor_atual)
                
            except:
                valor_atual = "Erro"
                window["-Display-"].Update(valor_atual)
            
    
    return
