"""
Scene_intro script
use for display the game intro

Alexandre BONIN - Python 3.5 - 2016
"""

import Graphics
import Color

def intro(window):

    text_id = Graphics.write_text(window = window,
                                  line = 'Pythalex    presente',
                                  coord = (106,193),
                                  color = Color.white(),
                                  font = 'ArcadeClassic 15',
                                  transition = True)

    window.root.after(1000)

    window.canvas.delete(Graphics.ALL_ID)

    text_id2 = Graphics.write_text(window=window,
                                  line='PasMario    Bros',
                                  coord=(170, 190),
                                  color=Color.white(),
                                  transition=True)

    window.root.after(1000)

    press_start_blink(window)

def press_start_blink(window):

    text_id = Graphics.write_text(window=window,
                                  line='PRESS START',
                                  coord=(230, 270),
                                  color=Color.white(),
                                  font = 'ArcadeClassic 20',
                                  transition=True)


def main():

    window = Graphics.WINDOW
    # game window

    intro(window)
    # Run intro


if __name__ == '__main__':

    def test():

        main()

    Graphics.WINDOW.root.wait_visibility()

    test()

    Graphics.WINDOW.root.mainloop()