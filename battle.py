import pokemon
import utils
import trainer
import json
import random

with open("data/moves.json") as move:
    moves = json.load(move)

def battle_start():
    game_active = True
    user_name = ""
    user_input = ""

    while game_active:
        print("Please enter your name: ", end="")
        utils.selection
        user_name = input("")

        player = trainer.Trainer(str(user_name), str(utils.generate_pokemon()))
        enemy = trainer.Trainer("Enemy", str(utils.generate_pokemon()))

        while enemy.get_pokemon().get_name() is player.get_pokemon().get_name():
            enemy = trainer.Trainer("Enemy", str(utils.generate_pokemon()))

        utils.line_break(20)
        print("You will be using ", end="")
        print(player.get_pokemon(), end="")
        utils.line_break(20, 4)

        print("The enemy will be using ", end="")
        print(enemy.get_pokemon(), end="")

        while int(player.get_pokemon().get_hp()) > 0 and int(enemy.get_pokemon().get_hp()) > 0 and game_active == True:
            user_input = ""

            utils.line_break(20)
            print("{}'s {}".format(enemy.get_name(), enemy.get_pokemon().get_name()))
            print(" {} HP".format(int(enemy.get_pokemon().get_hp()), utils.display_hp(int(int(enemy.get_pokemon().get_hp())))))

            utils.line_break(1)
            print("---------------------------")
            utils.line_break(1)

            print("{}'s {}".format(player.get_name(), player.get_pokemon().get_name()))
            print(" {} HP\n\nMoves:".format(int(player.get_pokemon().get_hp()), utils.display_hp(int(int(player.get_pokemon().get_hp())))))
            for move in player.get_pokemon().get_moves():
                print(move)

            user_input = input("\nSelect your move: ")
            user_input = user_input.title()

            while not user_input in player.get_pokemon().get_moves():
                utils.line_break(20)
                print("{}'s {}".format(enemy.get_name(), enemy.get_pokemon().get_name()))
                print(" {} HP".format(int(enemy.get_pokemon().get_hp()), utils.display_hp(int(int(enemy.get_pokemon().get_hp())))))

                utils.line_break(2)

                print("{}'s {}".format(player.get_name(), player.get_pokemon().get_name()))
                print(" {} HP\n\nMoves:".format(int(player.get_pokemon().get_hp()), utils.display_hp(int(int(player.get_pokemon().get_hp())))))
                for move in player.get_pokemon().get_moves():
                    print(move)

                print(user_input)
                user_input = input("\nbSelect your move: ")
                user_input = user_input.title()

            utils.line_break(20)
            print(enemy.get_pokemon().reduce_hp(moves[user_input]["power"], moves[user_input]["type"]), end="")
            utils.line_break(20, 2)

            enemy_move = random.randint(1, 2)
            match enemy_move:
                case 1:
                    enemy_move = enemy.get_pokemon().get_moves()[0]
                case 2:
                    enemy_move = enemy.get_pokemon().get_moves()[1]

            print("The enemy {} used {}".format(enemy.get_pokemon().get_name(), enemy_move))
            print(player.get_pokemon().reduce_hp(moves[user_input]["power"], moves[enemy_move]["type"]), end="")
            utils.line_break(20, 3)

        game_active = False

        utils.line_break(20)
        if (player.get_pokemon().get_hp() > 0):
            print("{}'s {} wins!\n\nThank you for playing!".format(player.get_name(), player.get_pokemon().get_name()))
        elif (enemy.get_pokemon().get_hp() > 0):
            print("{}'s {} wins!\n\nBetter luck next time.".format(enemy.get_name(), enemy.get_pokemon().get_name()))
        utils.line_break(0, 20)