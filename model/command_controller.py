import re


class CommandController():

    __color_codes = {'cyan': '\u001b[36;1m',
                     'white': '\u001b[37;1m',
                     'green': '\u001b[32;1m',
                     'magenta': '\u001b[35;1m',
                     'yellow': '\u001b[33;1m'}

    __decorators = ["❯❯", "❯¿", "🔥", "😂"]

    def __init__(self, is_color=False):
        self.__is_color = is_color

    def set_is_color(self, is_color):
        self.__is_color = is_color
        if not self.__is_color:
            for key in self.__color_codes:
                self.__color_codes[key] = "\u001b[0m"

    def print_info(self, info):
        print('\n', self.__color_codes['cyan'], self.__decorators[0], info)

    def print_question(self, question):
        print('\n', self.__color_codes['white'],
              self.__decorators[1], question)

    def print_congrat(self, congrat):
        print('\n', self.__color_codes['green'],
              self.__decorators[2], congrat.upper())

    def print_blame(self, blame):
        print('\n', self.__color_codes['magenta'],
              self.__decorators[3], blame.upper())

    def print_string(self, string, color=None):
        if not color:
            color = 'default'
        print(self.__color_codes[color], string)

    def print_file(self, file_dir, color=None):
        if not color:
            color = 'default'

        with open(file_dir) as f:
            for line in f:
                print(self.__color_codes[color], line, end='')
            print()

    # def print_card(self, card_string):
    #     print(self.__color_codes[4], card_string)

    def handle_y_input(self, input):
        x = re.search("^(Y|y)", input)
        if (x):
            return True
        return False

    def handle_g_input(self, input):
        x = re.search("^(G|g)", input)
        if (x):
            return True
        return False
