
from tkinter.font import BOLD
import PySimpleGUI as sg
import platform
import psutil
import time


def show_cpu_info():
    cpu_usage = psutil.cpu_percent()
    time.sleep(0.5)
    
    
#cpu_usage = psutil.cpu_percent()
#time.sleep(0.5)


num_of_cpu = psutil.cpu_count()


# All the stuff inside your window. This is the PSG magic code compactor...
layout = [  [sg.Text(f'Number os cores : {num_of_cpu}')],
          [sg.Text(f'CPU Usage : {show_cpu_info}')]
          ]

sg.Window("DELTA OS - System Information",icon='icons/command-line.ico').Layout(layout).read()

