import random


class Deck:
    groups = {'A': 10, '2': 20, '3': 30, '4': 40, '5': 50, '6': 60,
              '7': 70, '8': 80, '9': 90, '10': 100, 'J': 110, 'Q': 120, 'K': 130}

    suits = {'♥': 4, '♦': 3, '♣': 2, '♠': 1}

    special = {'B': 135, 'R': 136}
    cards = []

    def start_deck(self):
        self.cards = []
        self.current_reward = 20
        for g in self.groups:
            for s in self.suits:
                card = Card(g, s, self.groups[g]+self.suits[s])
                self.cards.append(card)

        for s in self.special:
            card = Card('ℑҡ', s, self.special[s])
            self.cards.append(card)

        def print_deck():
            print('\u001b[36mOpening new deck...')
            for card in self.cards:
                card.draw_card()
        return print_deck()

    # def __init__(self):
    #     super().__init__
    #     self.start_deck()

    def get_random_card(self):
        if (len(self.cards) <= 0):
            return None
        n = random.randint(0, len(self.cards)-1)
        card = self.cards.pop(n)
        return card

    def get_number_cards_left(self):
        return len(self.cards)

    def reset_reward(self):
        print("\u001b[35mWELL DONE, GENIUS! YOU'VE LOST ALL YOUR REWARDS")
        self.current_reward = 20
        self.show_reward()

    def update_reward(self):
        print("\u001b[32mYOU WON THE ROUND!! YOUR REWARD HAS BEEN DOUBLED")
        self.current_reward *= 2
        self.show_reward()
        return self.current_reward

    def show_reward(self):
        print("\u001b[0mYour current reward is: ", self.current_reward)

    def get_current_reward(self):
        return self.current_reward


class Card:
    def __init__(self, g, s, value):
        super().__init__
        self.group = g
        self.suit = s
        self.name = g+'-'+s
        self.value = value

    def draw_card(self):
        print('\u001b[33m')
        print('┌───────┐')
        print(f'| {self.group:<2}    |')
        print('|       |')
        print(f'|   {self.suit}   |')
        print('|       |')
        print(f'|    {self.group:>2} |')
        print('└───────┘')
        print('\u001b[0m')
