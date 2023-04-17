'''
Filename: DecryptorUI.py
The User Interface for The Decryptor
'''

import PySimpleGUI as sg
from decryptor import decrypt

sg.theme('DarkAmber')

layout = [
    [sg.Text('', size=(20,1)), sg.Text('THE DECRYPTOR', font=('Any 20'), auto_size_text=True, justification='center'), sg.Text('', size=(20,1))],
    [sg.Text('Enter text to decrypt: '), sg.InputText(key='input')],
    [sg.Text('Decrypted Text: '), sg.Text(key='output', font=('Roboto', 14), background_color='black')],
    [sg.Button('Decrypt', bind_return_key=True), sg.Button('Quit')]
]

window = sg.Window('Decryptor', layout)

while True:
    event, values = window.read()

    if (event == sg.WIN_CLOSED or event == 'Quit'):
        break

    elif (event == 'Decrypt' or event == '\r'):
        decrypted_text = decrypt(values['input'])
        window['input'].update('')
        window['output'].update(decrypted_text)

window.close()
