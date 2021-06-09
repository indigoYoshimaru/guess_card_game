from model.command_controller import CommandController
import random


class Deck:
    _groups = {'A': 10, '2': 20, '3': 30, '4': 40, '5': 50, '6': 60,
               '7': 70, '8': 80, '9': 90, '10': 100, 'J': 110, 'Q': 120, 'K': 130}

    _suits = {'♥': 4, '♦': 3, '♣': 2, '♠': 1}

    _special = {'B': 135, 'R': 136}
    __cards = []

    def __init__(self, c_controller):
        self._c_controller = c_controller

    def start_deck(self):
        self.__cards = []
        self.__current_reward = 20
        for g in self._groups:
            for s in self._suits:
                card = Card(g, s, self._groups[g] +
                            self._suits[s], self._c_controller)
                self.__cards.append(card)

        for s in self._special:
            card = Card('ℑҡ', s, self._special[s], self._c_controller)
            self.__cards.append(card)

        def print_deck():
            self._c_controller.print_info('Opening new deck...')
            for card in self.__cards:
                card.draw_card()
        return print_deck()

    def get_random_card(self):
        if (len(self.__cards) <= 0):
            return None
        n = random.randint(0, len(self.__cards)-1)
        card = self.__cards.pop(n)
        return card

    def get_number_cards_left(self):
        return len(self.__cards)

    def reset_reward(self):
        # print("\u001b[35mWELL DONE, GENIUS! YOU'VE LOST ALL YOUR REWARDS")
        self._c_controller.print_blame(
            "well done, genius! You've lost all your rewards")
        self.__current_reward = 20
        self.show_reward()

    def update_reward(self):
        # print("\u001b[32mYOU WON THE ROUND!! YOUR REWARD HAS BEEN DOUBLED")
        self._c_controller.print_congrat(
            "you won the round! your reward has been doubled")
        self.__current_reward *= 2
        self.show_reward()
        return self.__current_reward

    def show_reward(self):
        self._c_controller.print_info(
            "Your current reward is: "+str(self.__current_reward))

    def get_current_reward(self):
        return self.__current_reward


class Card:
    def __init__(self, g, s, value, c_controller):
        self.group = g
        self.suit = s
        self.name = g+'-'+s
        self.value = value
        self._c_controller = c_controller

    def draw_card(self):
        card_string = '\n'

        card_string += '┌───────┐\n'
        card_string += f'| {self.group:<2}    |\n'
        card_string += '|       |\n'
        card_string += f'|   {self.suit}   |\n'
        card_string += '|       |\n'
        card_string += f'|    {self.group:>2} |\n'
        card_string += '└───────┘\n'
        self._c_controller.print_string(card_string, 'yellow')
