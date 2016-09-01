"""
Controls script
use for setup the game controls

Alexandre BONIN - Python 3.5 - 2016
"""

import Graphics

class Control(object):

    def __init__(self, key, command):

        control_translation = {'Mouse 1': '<Button-1>',
                               'Mouse 2': '<Button-2>'}

        if key in control_translation:
            key = control_translation[command]

        Graphics.WINDOW.canvas.bind(command, self.control_use)
        self.command = command
        self.key = key

    def control_use(self):