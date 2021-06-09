from model.command_controller import CommandController
import model.role_player as rp
import model.deck as deck


class Game:

    _c_controller = CommandController()
    __round = 0
    # house.set_current_card(current_deck.cards[0])

    def __init__(self, c_controller):
        self._c_controller = c_controller
        self.__current_deck = deck.Deck(c_controller)
        self.__player = rp.Player(c_controller)
        self.__house = rp.House(c_controller)

    def play_round(self):
        self.__round += 1
        self._c_controller.print_congrat("Round "+str(self.__round))
        p_card = self.__current_deck.get_random_card()
        h_card = self.__current_deck.get_random_card()
        if (not p_card) or (not h_card):
            self._c_controller.print_info("End of deck")
            # print("\u001b[36mEnd of deck")
            return None

        self.__player.set_current_card(p_card)
        self.__house.set_current_card(h_card)
        self._c_controller.print_question(
            "Greater or Smaller????")
        is_greater = self._c_controller.handle_g_input(input())
        self.__player.show_current_card()
        # if win the match, player must decide to whether to continue or stop
        if (is_greater and self.__player.get_current_card() > self.__house.get_current_card()) or (not is_greater and self.__player.get_current_card() < self.__house.get_current_card()):
            self.__current_deck.update_reward()
            self._c_controller.print_question("Continue match?")
            self.__player.set_state(
                self._c_controller.handle_y_input(input()))
            return True

        return False

    def play_match(self):
        # player.reduce_point(25)
        # loop rounds

        round_won = self.play_round()
        if round_won == None:
            return

        if (round_won) and (not self.__player.get_state()):
            return

        if not round_won:
            self.__current_deck.reset_reward()
            return self.play_match()

        return self.play_match()

    def play_game(self):

        # start match
        self._c_controller.print_question("Starting new match?")
        start_match = self._c_controller.handle_y_input(input())
        if not start_match:
            self._c_controller.print_info("Closing the game.... ")
            return

        self.__current_deck.start_deck()
        self.__player.reduce_point(25)
        self.play_match()

        reward = self.__current_deck.get_current_reward()
        self.__player.stop_match(reward)

        p_point = self.__player.get_point()
        if p_point >= 1000:
            self._c_controller.print_congrat("Congrats!!! You win the game!!")
            return

        if p_point < 30:
            self._c_controller.print_blame("Bravo!!! The game wins you!!")
            return

        self.play_game()
