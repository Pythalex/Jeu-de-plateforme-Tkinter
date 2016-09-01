"""
Color Module
Used for create and use Color

Alexandre BONIN - Python 3.5 - 2016
"""

class Color(object):

    def __init__(self, color_string):
        """
        Create a color object

        :param color_string: color in
        RGB additive form / Hexadecimal

        e.g :
        RED =>
            rgb(255,0,0)
            #FF0000
        """

        if is_hexadecimal(color_string):
            self.code = color_string
        # Si la couleur est écrite en hexadécimale

        elif is_RGB_value(color_sting):
            self.code = translate_to_hexadecimal(color_string, 'rgb')
        # Si la couleur est écrite en RGB

def is_hexadecimal(string):
    """

    Check if string is hexadecimal value
    return True if it is, return False
    if it's not

    :param string: value
    :return: False or True
    """

    value = True

    if '#' in string:
        string = string.strip('#')
    else:
        return False

    hexam_list = ['0', '1', '2', '3', '4', '5',
                  '6', '7', '8', '9', 'A', 'B',
                  'C', 'D', 'E', 'F', 'a', 'b',
                  'c', 'd', 'e', 'f']

    for char in string:
        value = char in hexam_list and value

    return value

def is_RGB_value(string):
    """
    Check if string value is a
    RGB value in form :
    rgb(X,X,X) with X integer

    :param string: value
    :return: False / True
    """

    if '(' in string:
        str_tmp = string.split('(')

        if str_tmp[0].lower() == 'rgb':

            if ')' in str_tmp[1]:

                str_tmp = str_tmp[1].strip(')')

                str_tmp = str_tmp.split(',')

                if len(str_tmp) > 3:
                    return False

                value = True

                for elm in str_tmp:
                    value = elm.isdigit() and int(elm) in range(256) and value

                return value

    return False

def translate_to_hexadecimal(string, mode : str):
    """
    Translate an integer or RGB value into
    hexadecimal value. For RGB, hexadecimal
    value is under #XXXXXX form.

    :param string: number value
    :param mode: int or RGB
    :return: hexadecimal value
    """

    base10_converter = {0 : 0, 1 : 1, 2 : 2, 3 : 3, 4 : 4, 5 : 5, 6 : 6,
                      7 : 7, 8 : 8, 9 : 9, 10 : 'A', 11 : 'B',12 : 'C',
                      13 : 'D', 14 : 'E', 15 : 'F'}
    # Conversion dictionnary from base 10 to base 16

    if mode == 'rgb':
    # Translation RGB => hexadecimal value
        int_list = string.strip('rgb(').strip(')').split(',')
        translate_list = []

        for num in int_list:
            value = translate_to_hexadecimal(string = num, mode = 'int')
            # recurrence
            if value.isdigit():
                if int(value) < 10:
                    value = '0' + str(value)
            elif value in ['A', 'B', 'C', 'D', 'E', 'F']:
                value = '0' + value
            translate_list.append(value)
            # < 10 value checker
        # Translation loop

        return "#" + ''.join(translate_list)

    if mode == 'int':
    # Translation Int => hexadecimal value

        num = int(string)
        restes = []
        divisible = True
        # Variables initiation

        while divisible:
            quotient = num // 16
            restes.append(num % 16)

            if quotient == 0:
                break
            num = quotient
        # Division algorithm

        hexadecimal_number = ''
        restes.reverse()
        # Translation preparations

        for reste in restes:
            if reste > 16:
                break
            hexadecimal_number += str(base10_converter[int(reste)])
        # Translation loop

        return hexadecimal_number

def white():

    return Color('#FFFFFF')

def black():

    return Color('#000000')

def red():

    return Color('#FF0000')

def blue():

    return Color('#0000FF')

def green():

    return Color('#00FF00')

def magenta():

    return Color('#FF00FF')

def yellow():

    return Color('#FFFF00')

def cyan():

    return Color('#00FFFF')

if __name__ == '__main__':

    def test():

        white_color = white()
        print(white_color)
        # Get white color

        print(is_hexadecimal('#FFFFFF'))
        # verif hexam value

        print(is_hexadecimal('#gggege'))
        # verif false hexam value

        print('\n')

        print(is_RGB_value('rGb(152,255,236)'))

        print('\n')

        print(translate_to_hexadecimal('12', 'int'))
        print(translate_to_hexadecimal('(255,0,9)', 'rgb'))
        #Color()
        # create custom color

        input()

    test()




