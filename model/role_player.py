# Singleton will be used in this exercise
# since there should be only 1 player and 1 house in this exercise

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwds):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwds)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Player(metaclass=SingletonMeta):
    def __init__(self):
        self.__point = 60

    def set_state(self, is_continued):
        self.__is_continued = is_continued

    def get_state(self):
        return self.__is_continued

    def show_current_card(self):
        print("\nYour card is: ")
        return self.__current_card.draw_card()

    def set_current_card(self, card):
        self.__current_card = card

    def get_current_card(self):
        return self.__current_card.value

    def get_point(self):
        return self.__point

    def reduce_point(self, point):
        self.__point -= point
        print("\nYou have %s points left" % self.__point)

    def add_point(self, point):
        self.__point += point

    def stop_match(self, reward):
        print("YOU REWARDS AFTER THE ROUNDS: ", reward)
        self.add_point(reward)
        print("YOUR CURRENT POINT: ", self.get_point())


class House(metaclass=SingletonMeta):
    def set_current_card(self, card):
        self.__current_card = card

        # closure
        def show_card():
            print("\nThe house's card is: ")
            self.__current_card.draw_card()

        return show_card()

    def get_current_card(self):
        return self.__current_card.value
