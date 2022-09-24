# 9/23/2022 Ben Clark
# Intent - create similar layout to runescape's skill tab

from tkinter.font import BOLD, ITALIC
from turtle import back
import PySimpleGUI as sg
import output

#define layout
sg.theme('DarkBlue1')

border = 10  # Border_width
imgsize = 4 # lower number = bigger icons

sz=(10,20)
col1=[[sg.Button('', image_data=output.attack, button_color=sg.TRANSPARENT_BUTTON, border_width=border, image_subsample=imgsize, key='attack')],
      [sg.Button('', image_data=output.strength, button_color=sg.TRANSPARENT_BUTTON, border_width=border, image_subsample=imgsize, key='strength')],
      [sg.Button('', image_data=output.defense, button_color=sg.TRANSPARENT_BUTTON, border_width=border, image_subsample=imgsize, key='defense')],
      [sg.Button('', image_data=output.ranged, button_color=sg.TRANSPARENT_BUTTON, border_width=border, image_subsample=imgsize, key='ranged')],
      [sg.Button('', image_data=output.prayer, button_color=sg.TRANSPARENT_BUTTON, border_width=border, image_subsample=imgsize, key='prayer')],
      [sg.Button('', image_data=output.magic, button_color=sg.TRANSPARENT_BUTTON, border_width=border, image_subsample=imgsize, key='magic')],
      [sg.Button('', image_data=output.runecrafting, button_color=sg.TRANSPARENT_BUTTON, border_width=border, image_subsample=imgsize, key='runecrafting')],
      [sg.Button('', image_data=output.construction, button_color=sg.TRANSPARENT_BUTTON, border_width=border, image_subsample=imgsize, key='construction')]
     ]

col2=[[sg.Button('', image_data=output.hitpoints, button_color=sg.TRANSPARENT_BUTTON, border_width=border, image_subsample=imgsize, key='hitpoints')],
      [sg.Button('', image_data=output.agility, button_color=sg.TRANSPARENT_BUTTON, border_width=border, image_subsample=imgsize, key='agility')],
      [sg.Button('', image_data=output.herblore, button_color=sg.TRANSPARENT_BUTTON, border_width=border, image_subsample=imgsize, key='herblore')],
      [sg.Button('', image_data=output.thieving, button_color=sg.TRANSPARENT_BUTTON, border_width=border, image_subsample=imgsize, key='thieving')],
      [sg.Button('', image_data=output.crafting, button_color=sg.TRANSPARENT_BUTTON, border_width=border, image_subsample=imgsize, key='crafting')],
      [sg.Button('', image_data=output.fletching, button_color=sg.TRANSPARENT_BUTTON, border_width=border, image_subsample=imgsize, key='fletching')],
      [sg.Button('', image_data=output.slayer, button_color=sg.TRANSPARENT_BUTTON, border_width=border, image_subsample=imgsize, key='slayer')],
      [sg.Button('', image_data=output.hunter, button_color=sg.TRANSPARENT_BUTTON, border_width=border, image_subsample=imgsize, key='hunter')]
     ]

col3=[[sg.Button('', image_data=output.mining, button_color=sg.TRANSPARENT_BUTTON, border_width=border, image_subsample=imgsize, key='attack')],
      [sg.Button('', image_data=output.smithing, button_color=sg.TRANSPARENT_BUTTON, border_width=border, image_subsample=imgsize, key='strength')],
      [sg.Button('', image_data=output.fishing, button_color=sg.TRANSPARENT_BUTTON, border_width=border, image_subsample=imgsize, key='defense')],
      [sg.Button('', image_data=output.cooking, button_color=sg.TRANSPARENT_BUTTON, border_width=border, image_subsample=imgsize, key='ranged')],
      [sg.Button('', image_data=output.firemaking, button_color=sg.TRANSPARENT_BUTTON, border_width=border, image_subsample=imgsize, key='prayer')],
      [sg.Button('', image_data=output.woodcutting, button_color=sg.TRANSPARENT_BUTTON, border_width=border, image_subsample=imgsize, key='magic')],
      [sg.Button('', image_data=output.farming, button_color=sg.TRANSPARENT_BUTTON, border_width=border, image_subsample=imgsize, key='runecrafting')],
      [sg.Button('Exit ', font=('Arial', 14, BOLD, ITALIC),button_color='red', border_width=18, image_subsample=8, key='Exit')]
     ]

col4=[
    #   [sg.Button('', image_data=output.mining, button_color=sg.TRANSPARENT_BUTTON, border_width=4, image_subsample=5, key='mining')],
    #   [sg.Button('', image_data=output.smithing, button_color=sg.TRANSPARENT_BUTTON, border_width=4, image_subsample=5, key='smithing')],
    #   [sg.Button('', image_data=output.fishing, button_color=sg.TRANSPARENT_BUTTON, border_width=4, image_subsample=5, key='fishing')],
    #   [sg.Button('', image_data=output.cooking, button_color=sg.TRANSPARENT_BUTTON, border_width=4, image_subsample=5, key='cooking')],
    #   [sg.Button('', image_data=output.firemaking, button_color=sg.TRANSPARENT_BUTTON, border_width=4, image_subsample=5, key='firemaking')],
    #   [sg.Button('', image_data=output.woodcutting, button_color=sg.TRANSPARENT_BUTTON, border_width=4, image_subsample=5, key='woodcutting')],
    #   [sg.Button('', image_data=output.farming, button_color=sg.TRANSPARENT_BUTTON, border_width=4, image_subsample=5, key='farming')],
    #   [sg.Button('', image_data=output.hunter, button_color=sg.TRANSPARENT_BUTTON, border_width=4, image_subsample=5, key='Exit')]
     ]

tab1_layout = [  [sg.Text('Select a skill below')],
                 [sg.Column(col1, element_justification='c', background_color='grey' ), sg.Column(col2, element_justification='c', background_color='grey' ), sg.Column(col3, element_justification='c', background_color='grey'), sg.Column(col4, element_justification='c', background_color='grey' )]
              ]     
    

tab2_layout = [[sg.T('Tab 2')],
               [sg.InputText('data 2', key='file 2'), sg.FileBrowse('data 2 download')],
               ]
layout = [
    [sg.TabGroup([[sg.Tab('Tab 1', tab1_layout),
                   sg.Tab('Tab 2', tab2_layout)
                   ]])],
    [sg.Button('Run'), sg.Button("Cancel")]]





window = sg.Window('Window Title', layout, no_titlebar=True, grab_anywhere=True)

while True:             # Event Loop
    event, values = window.read()
    print(event, values)
    if event in (None, 'agility'):
        print('you successfully clicked agility')
        print()   
    
    if event in (None, 'Exit'):
        break
window.close()
