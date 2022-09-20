

'''[‘Black’, ‘BlueMono’, ‘BluePurple’, ‘BrightColors’, ‘BrownBlue’, ‘Dark’, ‘Dark2’, ‘DarkAmber’, ‘DarkBlack’, 
‘DarkBlack1’, ‘DarkBlue’, ‘DarkBlue1’, ‘DarkBlue10’, ‘DarkBlue11’, ‘DarkBlue12’, ‘DarkBlue13’, ‘DarkBlue14’,
‘DarkBlue15’, ‘DarkBlue16’, ‘DarkBlue17’, ‘DarkBlue2’, ‘DarkBlue3’, ‘DarkBlue4’, ‘DarkBlue5’, ‘DarkBlue6’,
‘DarkBlue7’, ‘DarkBlue8’, ‘DarkBlue9’, ‘DarkBrown’, ‘DarkBrown1’, ‘DarkBrown2’, ‘DarkBrown3’, ‘DarkBrown4’,
‘DarkBrown5’, ‘DarkBrown6’, ‘DarkGreen’, ‘DarkGreen1’, ‘DarkGreen2’, ‘DarkGreen3’, ‘DarkGreen4’, ‘DarkGreen5’,
‘DarkGreen6’, ‘DarkGrey’, ‘DarkGrey1’, ‘DarkGrey2’, ‘DarkGrey3’, ‘DarkGrey4’, ‘DarkGrey5’, ‘DarkGrey6’, ‘DarkGrey7’,
‘DarkPurple’, ‘DarkPurple1’, ‘DarkPurple2’, ‘DarkPurple3’, ‘DarkPurple4’, ‘DarkPurple5’, ‘DarkPurple6’, ‘DarkRed’,
‘DarkRed1’, ‘DarkRed2’, ‘DarkTanBlue’, ‘DarkTeal’, ‘DarkTeal1’, ‘DarkTeal10’, ‘DarkTeal11’, ‘DarkTeal12’, ‘DarkTeal2’,
‘DarkTeal3’, ‘DarkTeal4’, ‘DarkTeal5’, ‘DarkTeal6’, ‘DarkTeal7’, ‘DarkTeal8’, ‘DarkTeal9’, ‘Default’, ‘Default1’, 
‘DefaultNoMoreNagging’, ‘Green’, ‘GreenMono’, ‘GreenTan’, ‘HotDogStand’, ‘Kayak’, ‘LightBlue’, ‘LightBlue1’,
‘LightBlue2’, ‘LightBlue3’, ‘LightBlue4’, ‘LightBlue5’, ‘LightBlue6’, ‘LightBlue7’, ‘LightBrown’, ‘LightBrown1’, 
‘LightBrown10’, ‘LightBrown11’, ‘LightBrown12’, ‘LightBrown13’, ‘LightBrown2’, ‘LightBrown3’, ‘LightBrown4’,
‘LightBrown5’, ‘LightBrown6’, ‘LightBrown7’, ‘LightBrown8’, ‘LightBrown9’, ‘LightGray1’, ‘LightGreen’, ‘LightGreen1’,
‘LightGreen10’, ‘LightGreen2’, ‘LightGreen3’, ‘LightGreen4’, ‘LightGreen5’, ‘LightGreen6’, ‘LightGreen7’, ‘LightGreen8’,
‘LightGreen9’, ‘LightGrey’, ‘LightGrey1’, ‘LightGrey2’, ‘LightGrey3’, ‘LightGrey4’, ‘LightGrey5’, ‘LightGrey6’, 
‘LightPurple’, ‘LightTeal’, ‘LightYellow’, ‘Material1’, ‘Material2’, ‘NeutralBlue’, ‘Purple’, ‘Reddit’, ‘Reds’, 
‘SandyBeach’,
‘SystemDefault’, ‘SystemDefault1’, ‘SystemDefaultForReal’, ‘Tan’, ‘TanBlue’, ‘TealMono’, ‘Topanga’]
'''

import PySimpleGUI as g

def digit_input(button_key, keys_displayed):

    global percent
    global hold_operand
    
    if percent:
        keys_displayed = ''
        values['input'] = ''
        percent = False         
        hold_operand = False
    if button_key == '.':
        if button_key in keys_displayed:
            pass
        elif keys_displayed == '':
            keys_displayed = '0.'
        else:
            keys_displayed = keys_displayed + '.'
    elif keys_displayed == '0' and button_key != '0':
        keys_displayed = button_key                                
    elif keys_displayed == '0' and button_key == '0':
        pass
    else:
        keys_displayed += button_key
    return keys_displayed

def calc(op, operand_1, operand_2):                         # function which performs the given operation (op) on two given operands.

    global hold_operand

    if op == '/':
        try:
            result = str(float(operand_1)/float(operand_2))
        except (ZeroDivisionError, ValueError):
            result = 'Error'
    elif op == 'x':
        try:
            result = str(float(operand_1)*float(operand_2))
        except ValueError:
            result = 'Error'
    elif op == '-':
        try:
            result = str(float(operand_1) - float(operand_2))
        except ValueError:
            result = 'Error'
    elif op == '+':
        try:
            result = str(float(operand_1) + float(operand_2))
        except ValueError:
            result = 'Error'
    return result

def sign_display(sign, keys_displayed):                     # function which handles the +/- sign display of any current operand.

    if sign:
        key_list = list(keys_displayed)
        del key_list[0]
        sign = False
        return ''.join(key_list)
    else:
        sign = True
        return '-' + values['input']
             
in_elem = g.Input(size=(30, 1), do_not_clear=True, key='input')
                                                            # setup for calculator GUI layout.
layout = [
          [in_elem],
          [g.ReadFormButton('AC'), g.ReadFormButton('+/-'), g.ReadFormButton('%'), g.ReadFormButton('/')],
          [g.ReadFormButton('1'), g.ReadFormButton('2'), g.ReadFormButton('3'), g.ReadFormButton('x')],
          [g.ReadFormButton('4'), g.ReadFormButton('5'), g.ReadFormButton('6'), g.ReadFormButton('-')],
          [g.ReadFormButton('7'), g.ReadFormButton('8'), g.ReadFormButton('9'), g.ReadFormButton('+')],
          [g.ReadFormButton('.'), g.ReadFormButton('0'), g.ReadFormButton(''), g.ReadFormButton('=')],
          ]

form = g.FlexForm('Keypad', default_element_size=(5, 2), auto_size_buttons=False)
form.Layout(layout)

keys_entered = '0'
keys_entered_1 = ''
operator = ''
hold_operand = False
negative = False
percent = False
calculate = False

in_elem.Update(keys_entered)
while True:
    button, values = form.Read()
    if button is None:                                      # if the X button clicked, just exit.
        break
    if button is 'AC':                                      # clear all entries and flags if 'AC' is pressed.
        keys_entered = '0'
        keys_entered_1 = ''
        negative = False
        operator = ''
        hold_operand = False
        percent = False
    elif button in '1234567890.':
        if calculate:                                       # calculate flag is set to True immediately after = has been pressed, so new key_entered
            keys_entered = ''                               # is began with appropriate flags reset.
            keys_entered_1 = ''
            operator = ''
            calculate = False
        if operator != '':                                  # If operator has been entered, store the 2nd operand in keys_entered_1 and flag
            hold_operand = True                             #with hold_operand.
            keys_entered_1 = digit_input(button, keys_entered_1)
        else:                                               # If operator has not be entered, store digits in 1st operand.
            keys_entered = digit_input(button, keys_entered)  
    elif button is '%':                                     #% is special because operand (either 1st or 2nd) must be divided by 100.
        percent = True                                      #% flag is set to allow detection of new operand input if a digit is entered after %. 
        if hold_operand:
            keys_entered_1 = str(float(keys_entered_1)/100)
        else:
            keys_entered = str(float(keys_entered)/100)
    elif button in '/x-+':
        if hold_operand:
            hold_operand = False
            keys_entered = calc(operator, keys_entered, keys_entered_1)
        operator = button
        keys_entered_1 = ''
        calculate = False
        percent = False
    elif button is '+/-':
        if hold_operand:
            keys_entered_1 = sign_display(negative, keys_entered_1)
        else:
            keys_entered = sign_display(negative, keys_entered)
    elif button is '=':
        if keys_entered_1 != '':
            keys_entered = calc(operator, keys_entered, keys_entered_1)
            hold_operand = False
            calculate = True
        else:
            keys_entered = values['input']
            in_elem.Update(keys_entered)
       
    if hold_operand and keys_entered_1 != '':
        in_elem.Update(keys_entered_1)
    else:
        in_elem.Update(keys_entered)