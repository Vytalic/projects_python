# 9/23/2022 Ben Clark
# Intent - create similar layout to runescape's skill tab



# Note that the base64 string is quite long.  You can get the code from Trinket that includes the button

import PySimpleGUI as sg
import output

#define layout
sz=(10,20)
col1=[[sg.Button('', image_data=output.attack, button_color=sg.TRANSPARENT_BUTTON, border_width=0, image_subsample=8, key='Exit')],
      [sg.Button('', image_data=output.strength, button_color=sg.TRANSPARENT_BUTTON, border_width=0, image_subsample=8, key='Exit')],
      [sg.Button('', image_data=output.defense, button_color=sg.TRANSPARENT_BUTTON, border_width=0, image_subsample=8, key='Exit')],
      [sg.Button('', image_data=output.ranged, button_color=sg.TRANSPARENT_BUTTON, border_width=0, image_subsample=8, key='Exit')],
      [sg.Button('', image_data=output.prayer, button_color=sg.TRANSPARENT_BUTTON, border_width=0, image_subsample=8, key='Exit')],
      [sg.Button('', image_data=output.magic, button_color=sg.TRANSPARENT_BUTTON, border_width=0, image_subsample=8, key='Exit')],
      [sg.Button('', image_data=output.runecrafting, button_color=sg.TRANSPARENT_BUTTON, border_width=0, image_subsample=8, key='Exit')],
      [sg.Button('', image_data=output.construction, button_color=sg.TRANSPARENT_BUTTON, border_width=0, image_subsample=8, key='Exit')]
     ]

col2=[[sg.Button('', image_data=output.hitpoints, button_color=sg.TRANSPARENT_BUTTON, border_width=0, image_subsample=8, key='Exit')],
      [sg.Button('', image_data=output.agility, button_color=sg.TRANSPARENT_BUTTON, border_width=0, image_subsample=8, key='Exit')],
      [sg.Button('', image_data=output.herblore, button_color=sg.TRANSPARENT_BUTTON, border_width=0, image_subsample=8, key='Exit')],
      [sg.Button('', image_data=output.thieving, button_color=sg.TRANSPARENT_BUTTON, border_width=0, image_subsample=8, key='Exit')],
      [sg.Button('', image_data=output.crafting, button_color=sg.TRANSPARENT_BUTTON, border_width=0, image_subsample=8, key='Exit')],
      [sg.Button('', image_data=output.fletching, button_color=sg.TRANSPARENT_BUTTON, border_width=0, image_subsample=8, key='Exit')],
      [sg.Button('', image_data=output.slayer, button_color=sg.TRANSPARENT_BUTTON, border_width=0, image_subsample=8, key='Exit')],
      [sg.Button('', image_data=output.hunter, button_color=sg.TRANSPARENT_BUTTON, border_width=0, image_subsample=8, key='Exit')]
     ]

col3=[[sg.Button('', image_data=output.mining, button_color=sg.TRANSPARENT_BUTTON, border_width=0, image_subsample=8, key='Exit')],
      [sg.Button('', image_data=output.smithing, button_color=sg.TRANSPARENT_BUTTON, border_width=0, image_subsample=8, key='Exit')],
      [sg.Button('', image_data=output.fishing, button_color=sg.TRANSPARENT_BUTTON, border_width=0, image_subsample=8, key='Exit')],
      [sg.Button('', image_data=output.cooking, button_color=sg.TRANSPARENT_BUTTON, border_width=0, image_subsample=8, key='Exit')],
      [sg.Button('', image_data=output.firemaking, button_color=sg.TRANSPARENT_BUTTON, border_width=0, image_subsample=8, key='Exit')],
      [sg.Button('', image_data=output.woodcutting, button_color=sg.TRANSPARENT_BUTTON, border_width=0, image_subsample=8, key='Exit')],
      [sg.Button('', image_data=output.farming, button_color=sg.TRANSPARENT_BUTTON, border_width=0, image_subsample=8, key='Exit')],
      [sg.Button('', image_data=output.hunter, button_color=sg.TRANSPARENT_BUTTON, border_width=0, image_subsample=8, key='Exit')]
     ]




layout = [  [sg.Text('Select a skill below')],
          
            [sg.Column(col1, element_justification='c' ), sg.Column(col2, element_justification='c' ), sg.Column(col3, element_justification='c' )]         
         ]

window = sg.Window('Window Title', layout, no_titlebar=True, grab_anywhere=True)

while True:             # Event Loop
    event, values = window.read()
    print(event, values)
    if event in (None, 'Exit'):
        break
window.close()
