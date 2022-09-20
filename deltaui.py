#!/usr/bin/env python
import sys
import os
import PySimpleGUI as sg
import tkinter

"""
Demo Button Function Calls
Typically GUI packages in Python (tkinter, Qt, WxPython, etc) will call a user's function
when a button is clicked.  This "Callback" model versus "Message Passing" model is a fundamental
difference between PySimpleGUI and all other GUI.

There are NO BUTTON CALLBACKS in the PySimpleGUI Architecture

It is quite easy to simulate these callbacks however.  The way to do this is to add the calls
to your Event Loop
"""
sg.theme("BlueMono")

def system_infom():
    os.system('python ./scripts/system_ifo.py')
    
def system_stats():
    os.system("python ./scripts/cpu_ram.py")
    
def notepad():
    os.system("python ./scripts/notepad.py")
    
def browser():
    os.system("python ./scripts/browser.py")
    
def calculator():
    os.system("python ./scripts/calculator.py")
    
def pong():
    os.system("python ./scripts/pong.py")
    
def snake():
    os.system("python ./scripts/snake.py")

layout = [
          [sg.Button('System\nStatics', image_filename='icons/stats.png', button_color=("white", "red")), sg.Button('Calculator', image_filename='icons/calculator.png', button_color=("white", "purple"))], 
          [sg.Button('System\nInfo', image_filename='icons/system.png', button_color=("white", "green")), sg.Button('Pong', image_filename='icons/pingpong.png', button_color=("white", "grey"))],
          [sg.Button('Notepad', image_filename='icons/notepad.png', button_color=("white", "brown")), sg.Button('Snake', image_filename='icons/icons8-snake-64_50x50.png', button_color=("white", "blue"))]
          
          ]

web = [
    [sg.Button('Browser', image_filename='icons/web_1_50x50.png', button_color=("white", "orange"))]
]

window = sg.Window('DELTA OS - Main gui',icon='icons/delta.ico', finalize=True, size=(500, 300,)).Layout(layout).Layout(web)



while True:             # Event Loop
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'System\nStatics':
        system_stats()        # call the "Callback" function
    elif event == 'System\nInfo':
        system_infom()        # call the "Callback" function
    elif event == 'Notepad':
        notepad()
    elif event == 'Browser':
        browser()
    elif event == 'Calculator':
        calculator()
    elif event == "Pong":
        pong()
    elif event == 'Snake':
        snake()

window.close()