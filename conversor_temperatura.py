import PySimpleGUI as sg

def conversor_temperatura ():
    
    sg.theme("DarkGrey15")
    
    layout_principal = [
        [sg.Text("      "),sg.Text("Conversor de temperatura"),sg.Text()],
        [sg.Line()],
        [sg.Text(),sg.Button("Converter Fahrenheit para Celsius"),sg.Text()],
        [sg.Text(),sg.Button("Converter Celsius para Fahrenheit"),sg.Text()]
    ]
    
    layout_f = [
        [sg.Text("Digite o Fahrenheit"),sg.Input(size=(16,1),key="-F-")],
        [sg.Line()],
        [sg.Button("Calcular"),sg.VerticalLine(),sg.Text("", size=(20, 1), key="-RESULTADO-", background_color="gray", text_color="cyan" ,relief="sunken")]
    ]
    
    layout_c = [
        [sg.Text("Digite o Celsius"),sg.Input(size=(19,1),key="-C-")],
        [sg.Line()],
        [sg.Button("Calcular"),sg.VerticalLine(),sg.Text("", size=(20, 1), key="-RESULTADO-", background_color="gray", text_color="cyan" ,relief="sunken")]
    ]
    
    window_principal = sg.Window("Conversor de temperatura", layout_principal)
    
    while True:
        event, value = window_principal.read()
        
        if event == sg.WIN_CLOSED:
            break
        
        if event == "Converter Fahrenheit para Celsius":
            window_principal.close()
            window_f = sg.Window("Converter Fahrenheit para Celsius", layout_f)
            
            while True:
                event_f, value_f = window_f.read()
                
                if event_f == sg.WIN_CLOSED:
                    break
                
                if event_f == "Calcular":
                    try:   
                        valor_f = float(value_f['-F-'])    
                        valor_c = (valor_f-32)*5/9
                        window_f["-RESULTADO-"].update(f"{valor_f}°F é igual a {valor_c:.2f}°C")
                    except:
                        sg.popup("Valor invalido!")
                              
        elif event == "Converter Celsius para Fahrenheit":
            window_principal.close()
            window_c = sg.Window("Converter Celsius para Fahrenheit", layout_c)
            
            while True:
                event_c, value_c = window_c.read()
                
                if event_c == sg.WIN_CLOSED:
                    break
                
                if event_c == "Calcular":
                    try:
                        valor_c = float(value_c['-C-'])    
                        valor_f = (valor_c*9/5)+32
                        window_c["-RESULTADO-"].update(f"{valor_c}°C é igual a {valor_f:.2f}°F")
                    except:
                        sg.popup("Valor invalido!")
