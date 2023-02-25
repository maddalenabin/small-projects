# execute with
# python notif.py

import PySimpleGUI as sg

sg.theme('Dark Gray 15')

layout = [[sg.Text("Are you dumb?")], [sg.Button("YES"), sg.Button("NO")]]
layout2 = [[sg.Text("I knew it :)")]]

# Create the window
window = sg.Window("Question", layout, margins=(100, 50))#ize=(400, 3000))

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "YES":
        window.close()
        sg.Window(title="AHAH", layout=layout2, margins=(100, 50)).read()
        # sg.popup("I knew it :) ")

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break
    elif event == "NO":
        pass
    elif event == sg.WIN_CLOSED:
        break
    

window.close()