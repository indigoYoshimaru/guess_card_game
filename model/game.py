import model.role_player as rp
import model.deck as deck
import re
current_deck = deck.Deck()
player = rp.Player()
house = rp.House()
# house.set_current_card(current_deck.cards[0])


def handle_input(input):
    # None  # regex here return true
    x = re.search("^(Y|y)", input)
    if (x):
        return True
    return False


def play_round():
    p_card = current_deck.get_random_card()
    h_card = current_deck.get_random_card()
    if (not p_card) or (not h_card):
        print("\u001b[36mEnd of deck")
        return None

    player.set_current_card(p_card)
    house.set_current_card(h_card)

    input_string = input(
        "\u001b[0mDo you think your card is greater than the house's card? \n[Accept answer starts with Y or y for 'yes', any other answers are considered as 'no'] ")
    is_greater = handle_input(input_string)
    player.show_current_card()
    # if win the match, player must decide to whether to continue or stop
    if (is_greater and player.get_current_card() > house.get_current_card()) or (not is_greater and player.get_current_card() < house.get_current_card()):
        current_deck.update_reward()
        input_string = input(
            "\u001b[0mDo you want to continue? \n[Accept answer starts with Y or y for 'yes', any other answers are considered as 'no'] ")
        player.set_state(handle_input(input_string))
        return True

    return False


def play_match():
    # player.reduce_point(25)
    # loop rounds

    round_won = play_round()
    if round_won == None:
        return

    if (round_won) and (not player.get_state()):
        return

    if not round_won:
        current_deck.reset_reward()
        return play_match()

    return play_match()


def play_game():

    # start match
    start_match = handle_input(input(
        "\u001b[36m\nStarting new match? \n[Accept answer starts with Y or y for 'yes', any other answers are considered as 'no'] "))
    if not start_match:
        print("\n Closing the game.... ")
        return

    current_deck.start_deck()
    player.reduce_point(25)
    play_match()

    reward = current_deck.get_current_reward()
    player.stop_match(reward)

    p_point = player.get_point()
    if p_point >= 10000:
        print("\u001b[32m\nCONGRATS!! YOU WON")
        return

    if p_point < 30:
        print("\u001b[35m\nYOU LOST")
        return

    play_game()
