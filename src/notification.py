"""
    Author: Diego A. Santiago Uriarte 
    
    Summary: Functions used for returning info on countries as a 
    notification
    
"""
from automateSearches import *
import PySimpleGUI as sg
from random import randint
def returnInfo(country: str) -> list:
    """This Function takes in the country selected and 
    returns its associated assortment of subjects

    Args:x
        country (str): country selected either by input or random
    Returns: list of links divided by subjects as strings; line by line as it is found in the data txt file
    """

    NUMLINES: int = 28
    result = []

    with open(getcwd() + "\\links\\Result Study Guide.txt", 'r') as text:

        lines = text.readlines()

        for h in range(len(lines)):
            if lines[h].find(country.upper()) != -1:

                for i in range(NUMLINES - 1):
                    result.append(lines[h])
                    h += 1
                break

    return result


def gui():
    countries = read_csv(getcwd() + '\\Data\\countries of world.csv').Country
    font = 'arial 12'
    title_font = 'arial 24'

    sg.theme('DarkGrey5')  # Add a touch of color
    # All the stuff inside your window.
    layout = [[sg.Text(text="Welcome to Ideafy", font=title_font)],
              [sg.Text('Which Country Would You Like to Learn From?'), sg.InputText()],
              [sg.Button('find'), sg.Button('Random'), sg.Button('Cancel')],
              [sg.Multiline(
                  key='_OUT_',
                  size=(60, 40),
                  expand_x=True,
                  auto_refresh=True,
                  echo_stdout_stderr=True,
                  disabled=True,
                  autoscroll=True
              )],
              ]

    # Create the Window
    window = sg.Window(title='IDEAFY', layout=layout, size=(750,750))

    output = window["_OUT_"]

    window.refresh()
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
            break
        if event == 'find':
            result = automateSearchOnline(values[0])
        if event == 'Random':
            randi: int = randint(0, len(countries) - 1)
            result: list = returnInfo(countries[randi])

        for line in result:
            output.print(line)        

    window.close()


if __name__ == '__main__':
    gui()