import PySimpleGUI as sg
from time import time, ctime

def get_notification(text):
    """Function for gettin a notification when some tasks are finished
    Args:
        text: str message to print in  the pop-up window
    """
    # esthetics
    sg.theme('Dark Gray 15')
    layout = [[sg.Text(text, justification='center')], [sg.Button("OK")]]

    # Create the window
    window = sg.Window("Message", layout, margins=(100, 50), font=("Helvetica", 20), element_justification='c')
    # Create an event loop
    while True:
        event, values = window.read()
        if event in ["OK", sg.WIN_CLOSED]:
            break    
    
    window.close()
    return

# example
t = ctime(time())
get_notification(text=f'Measurement done {t}')