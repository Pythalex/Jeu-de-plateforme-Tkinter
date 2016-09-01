"""
Graphic Module
Used for create and use tkinter Windows

Alexandre BONIN - Python 3.5 - 2016
"""

import tkinter as t
import Color
import time
# Importations

class Window(object):

    def __init__(self, geometry : tuple):

        self.root = t.Tk()
        # Création fenêtre

        self.canvas = t.Canvas(master = self.root,
                               width = geometry[0],
                               height = geometry[1],
                               bg = 'black')
        self.canvas.pack()
        # Création canvas

    def refresh(self):

        self.root.update_idletasks()


def write_text(window, line : str, coord : tuple, color = Color.white(),
               transition = False, t_range = 1, font = 'ArcadeClassic 30'):

    global FRAMERATE

    if not transition:
        id = window.canvas.create_text(coord,
                                       anchor = t.NW,
                                       fill = color.code,
                                       text = line,
                                       font = font)
        return id

    else:
        shades = 255 // (t_range * 60)
        # Transition shades value

        if color.code == '#FFFFFF':
            shade = '#000000'
            rgb = 0
            color.code = shade
            text_id = write_text(window=window, coord=coord,
                                 color=Color.black(), line=line, font=font)
            while len(shade) < 8:
                window.canvas.delete(text_id)
                print(rgb)
                color.code = shade
                text_id = write_text(window = window, coord = coord,
                                     color = color, line = line, font = font)
                window.root.after(30)
                window.refresh()
                rgb = rgb + shades
                shade = Color.translate_to_hexadecimal('rgb(' + str(rgb) + ',' + str(rgb) + ',' + str(rgb) + ')', 'rgb')

        elif color.code == '#000000':
            pass
        else:
            raise Exception('TransitionColorError')

# ----------- MAIN VARIABLES  ----------- #

FRAMERATE = 60
# FPS
ALL_ID = t.ALL
# All canvas ID
WINDOW = Window(geometry = (640, 480))
# Main game Window

# --------------------------------------- #

if __name__ == '__main__':

    def write(window):

        id = write_text(window = window,
                        line='hello    world',
                        color=Color.white(),
                        coord=(200, 200),
                        transition=True)
        return id


    def test():

        fen = Window(geometry = (640,480))

        fen.root.wait_visibility()
        write(fen)

        fen.root.mainloop()

    test()
