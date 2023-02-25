import PySimpleGUI as sg

sg.theme('Dark Gray 15')

layout = [[sg.Text("Are you dumb?", justification='left')],
            [sg.Button("YES"), sg.Button("NO")]]

layout2 = [[sg.Text("I knew it :)", justification='center')]]

# Create the window
window = sg.Window("Question", layout, margins=(100, 50), font=("Helvetica", 20), element_justification='c')

# Create an event loop
while True:
    event, values = window.read()
    
    # YES: open new window with message
    if event == "YES":~
        window.close()
        w2 = sg.Window(title="AHAH", layout=layout2, margins=(100, 50), font=("Helvetica", 20)).read()
        # sg.popup("I knew it :) ")
        while True:
            event, values = w2.read()
            if event == sg.WIN_CLOSED:
                break    
    # CLOSE WINDOW
    elif event == sg.WIN_CLOSED:
        break

window.close()
w2.close()