import PySimpleGUI as sg

def tarefas ():
    
    sg.theme("DarkGrey15")

    def criar_janela_inicial():
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
            