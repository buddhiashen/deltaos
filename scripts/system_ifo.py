
from tkinter.font import BOLD
import PySimpleGUI as sg
import platform

info = f"System: {platform.system()}\n \
Username: {platform.node()}\n \
Release: {platform.release()}\n \
Version: {platform.version()}\n \
Machine: {platform.machine()}\n \
Processor: {platform.processor()}\n \
"

font = ("Arial", 12, BOLD)


# All the stuff inside your window. This is the PSG magic code compactor...
layout = [  [sg.Text(info, font=font)]
            ]

sg.Window("DELTA OS - System Information",icon='icons/command-line.ico').Layout(layout).read()

