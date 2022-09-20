
import PySimpleGUI as sg
import pathlib
sg.ChangeLookAndFeel("BrownBlue")

WIN_W = 90
WIN_H = 25
STARTUP = True
filename = None


file_new = 'New......(CTRL+N)'
file_open = 'Open......(CTRL+O)'
file_save = 'Save......(CTRL+S)'

menu_layout = [['File', [file_new, file_open, file_save, 'Save as', '------', 'Exit']],
               ['Tools', ['Word Count']],
               ['Help', ['About']]
               ]

layout = [
    [sg.Menu(menu_layout)],
    [sg.Text('> New file <', font=('Consolas', 10), size=(WIN_W, 1), key='_INFO_')],
    [sg.Multiline(font=('Consolas', 12), size=(WIN_W, WIN_H), key='_BODY_')]
    
]




window = sg.Window('Notepad - DELTA OS', layout=layout, margins=(0,0), resizable=True, return_keyboard_events=True, icon='icons/notepad.ico')


def new_file() -> str:
    window['_BODY_'].update(value='')
    window['_INFO_'].update(value='> New File <')
    filename = None
    return filename


def open_file():
    filename = sg.popup_get_file('Open', no_window=True)
    if filename:
        file = pathlib.Path(filename)
        window['_BODY_'].update(value=file.read_text())
        window['_INFO_'].update(value=file.absolute())
        return file

def word_count():
    words: list = [w for w in values['_BODY_'].split(' ') if w!='\n']
    word_count: int = len(words)
    sg.PopupQuick('Word Count: {:,d}'.format(word_count), auto_close=False, icon='icons/notepad.ico')


def save_file(file):
    '''Save file instantly if already open; otherwise use `save-as` popup'''
    if file:
        file.write_text(values.get('_BODY_'))
    else:
        save_file_as()

def save_file_as():
    '''Save new file or save existing file with another name'''
    filename = sg.popup_get_file('Save As', save_as=True, no_window=True)
    if filename:
        file = pathlib.Path(filename)
        file.write_text(values.get('_BODY_'))
        window['_INFO_'].update(value=file.absolute())
        return file

def about_me():
    '''A short, pithy quote'''
    sg.popup_no_wait('"NOTEPAD" is a simple text editor build using python and it \nis a part of the DELTA OS environment\n deisgned and build by Buddhi ashen', icon='icons/notepad.ico')




while True:
    event, values = window.read(timeout=1)
    
    if STARTUP:
        window.maximize()
        window['_BODY_'].expand(expand_x=True, expand_y=True)
        STARTUP = False
        
        
    if event in (None, 'Exit'):
        break
    if event in (file_new, 'n:78'):
        filename = new_file()
    if event in (file_open, 'o:79'):
        filename = open_file()
    if event in (file_save, 's:83'):
        save_file(filename)
    if event in ('Save as',):
        filename = save_file_as()
    if event in ('Word Count',):
        word_count()
    if event in ('About',):
        about_me()
        
        
window.close()