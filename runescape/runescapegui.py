# My first python program implementing a GUI --- 9/23/2022 Ben Clark


from turtle import onclick, right
import PySimpleGUI as sg
from random import randint
import math

sg.theme('DarkBlue')   # Add a touch of color

sz=(12,23) # size of listboxes
   
col1 = [[sg.Listbox(values = ('Agility', 'Attack', 'Construction', 
'Cooking', 'Crafting', 'Defence',
'Farming', 'Firemaking', 'Fishing',
'Fletching', 'Herblore', 'Hitpoints',
'Hunter', 'Magic', 'Mining', 'Prayer',
'Range', 'Runecrafting', 'Slayer', 
'Smithing', 'Strength', 'Thieving', 'Woodcutting'),
                           no_scrollbar = True,
                           size = sz,
                           background_color = 'black',
                           enable_events = True)]]

# Generate
def list_gen():
    listitems = []
    counter = 1
    
    while counter < 100:
        variable_new = f'lvl: {counter}'
        listitems.append(variable_new)
        counter += 1
    return listitems

col4 = [[sg.Combo(list_gen())], [sg.Button("Okay")]]

col3 = [[sg.Listbox(values = ('Hours:', 'Experience:', 'Current Level:', 'Expected Level:', 'Time:'),
                           no_scrollbar = True,
                           size = sz,
                           background_color = 'black',
                           enable_events = True,
                           )]]

col2 = [[sg.Listbox(values = ('Varrock', 'Falador', 'Canifis'),
                           no_scrollbar = True,
                           size = (12, 15),
                           background_color = 'black',
                           enable_events = True,
                           )],
        [sg.Ok()]]
             
frame_layout = [
                  [sg.T('Text inside of a frame')],
                  [sg.Column(col1, element_justification='c'),
                sg.Column(col4, element_justification='c', key = 'ttl', visible = False),
                sg.Column(col2, element_justification='c', key = 'agility', visible = False),
                sg.Column(col3, element_justification='c', key = 'stats', visible = False)]]

tab1_layout = [[sg.Frame('My Frame Title', frame_layout, font='Any 12', title_color='blue')]
               
              ]

tab2_layout = [
    [sg.T('Tab 2')],
    [sg.InputText('data 1', key='file 1'), sg.FileBrowse('data 1 download')]
]

tab3_layout = [
    [sg.T('Tab 3')],
    [sg.InputText('data 1', key='file 1'), sg.FileBrowse('data 1 download')]
]

layout = [
    
    [sg.TabGroup([[sg.Tab('Tab 1', tab1_layout),
                   sg.Tab('Tab 2', tab2_layout),
                   sg.Tab('Tab 3', tab3_layout)
                   ]])],
    [sg.Button('Run'), sg.Button("Cancel")]]


# Create the Window
window = sg.Window('Time to Goal...', layout)

# Event Loop to process "events" and get the "values" of the inputs

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit': # if user closes window or clicks cancel
        break
    
    if event == 'Ok':
        name = values['INPUT']
        window['OUTPUT'].update(value=name)
        
    if event == 'Okay':
        print('Does nothing except unhide next column ... for now')
     
    if values[0] == ['Agility']:
        
        window.Element('ttl').Update(visible = True) 
        
    if values[1] == 'choice 1':
        
        window.Element('agility').Update(visible = True)
    
    if values[2] == ['Varrock']:
        
        window.Element('stats').Update(visible = True)
        print('35k per hour')
    
    if values[2] == ['Falador']:
        
        window.Element('stats').Update(visible = True)
        print('Falador clicked')
   
    if values[2] == ['Canifis']:
        
        window.Element('stats').Update(visible = True)
        print('Canifis clicked')
    
    if values[3] == ['Experience:']:
        
        window.Element('ttl').Update(visible = True)
        print('column 3 works / experience clicked')
   
    if values[3] == ['##Experience']:
        
        window.Element('ttl').Update(visible = True)
        print(key = 'OUTPUT',)
window.close()

