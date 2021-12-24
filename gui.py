import PySimpleGUI as gui
#https://realpython.com/pysimplegui-python/

import os.path
import time


gui.theme("black")
layout = [
    [
        gui.Text("Input file:"),
        gui.FileBrowse("inputFile"),
    ],
    [
        gui.Text("Output folder:"),
        gui.FolderBrowse("outputFolder"),
        gui.Button("Start")
    ]
]


window = gui.Window("LiFi", layout)

while True:
    event, values = window.read()
    if event == "Start" or event == gui.WIN_CLOSED:
        print(values)
        break

window.close()



layout = [
    [
        gui.Text(key="time"),
        gui.Button("Start")
    ]
]


window = gui.Window("LiFi", layout)

while True:
    event, values = window.read()
    window['time'].update("aaaaaaaa")
    if event == "Start" or event == gui.WIN_CLOSED:
        print(values)
        break

window.close()
