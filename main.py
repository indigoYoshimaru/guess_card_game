from model import game
from model import command_controller as c_con

controller = c_con.CommandController()
is_color = controller.handle_y_input(input("Do you want to enable color?"))
controller.set_is_color(is_color)


controller.print_file('media/welcome.txt', 'yellow')
controller.print_file('media/rule.txt', 'magenta')


current_game = game.Game(controller)
current_game.play_game()
