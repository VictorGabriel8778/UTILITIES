import yt_dlp
import PySimpleGUI as sg

sg.theme("DarkGrey15")

def baixar_video_yt():
    
    layout = [
        [sg.Text("Digite a URL do video"),sg.Input(key="-URL-")],
        [sg.HorizontalLine()],
        [sg.Button("Baixar video YouTube")]
    ]
    
    window = sg.Window("Baixar video YouTube", layout)
    
    while True:
        event, value = window.read()
        
        if event == sg.WINDOW_CLOSED:
            break
        
        elif event == "Baixar video YouTube":
            
            url = value["-URL-"]
            
            try:
                ydl_opts = {
                'format': 'best', 
                'noplaylist': True,
                'outtmpl': "img_videos/%(title)s.%(ext)s"
            }
        
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    sg.popup("Baixando...",auto_close=True, auto_close_duration=2)
                    ydl.download([url])
                    sg.popup("Download concluido!")
        
            except Exception as e:
                sg.popup (f"Erro ao fazer download ")
                
    