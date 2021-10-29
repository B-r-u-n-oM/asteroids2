#For tests only
from sys import argv as cmd
from settings import *
cmd.pop(0)


if cmd[0] == "get":
    if cmd[1] == "game":
        try:
            print(f"game: {cmd[2]}={game[cmd[2]]}")
        except KeyError:
            print(f"Not recognized command: '{cmd[2]}'.")
        except IndexError:
            print("Missing argument in 'game'.")
    elif cmd[1] == "player":
        try:
            print(f"player: {cmd[2]}={player[cmd[2]]}")
        except KeyError:
            print(f"Not recognized command: '{cmd[2]}'.")
        except IndexError:
            print("Missing argument in 'player'.")
    elif cmd[1] == "asteroid":
        try:
            print(f"asteroid: {cmd[2]}={asteroid[cmd[2]]}")
        except KeyError:
            print(f"Not recognized command: '{cmd[2]}'.")
        except IndexError:
            print("Missing argument in 'asteoid'.")
    elif cmd[1] == "bullet":
        try:
            print(f"bullet: {cmd[2]}={bullet[cmd[2]]}")
        except KeyError:
            print(f"Not recognized command: '{cmd[2]}'.")
        except IndexError:
            print("Missing argument in 'bullet'.")
    elif cmd[1] == "enemy":
        try:
            print(f"enemy: {cmd[2]}={enemy[cmd[2]]}")
        except KeyError:
            print(f"Not recognized command: '{cmd[2]}'.")
        except IndexError:
            print("Missing argument in 'enemy'.")
    else:
        print("Not recognized command.")

if cmd[0] == "set":
    if cmd[1] == "game":
        try:
            if cmd[2] in game.keys():
                game[cmd[2]] = cmd[3]
                print(f"Now,\ngame: {cmd[2]}={game[cmd[2]]}")
            else:
                print("This field doesn't exist in 'game'.")
        except KeyError:
            print(f"Not recognized command: '{cmd[2]}'.")
        except IndexError:
            print("Missing argument in 'game'.")
    elif cmd[1] == "player":
        try:
            print(f"player: {cmd[2]}={player[cmd[2]]}")
        except KeyError:
            print(f"Not recognized command: '{cmd[2]}'.")
        except IndexError:
            print("Missing argument in 'player'.")
    elif cmd[1] == "asteroid":
        try:
            print(f"asteroid: {cmd[2]}={asteroid[cmd[2]]}")
        except KeyError:
            print(f"Not recognized command: '{cmd[2]}'.")
        except IndexError:
            print("Missing argument in 'asteoid'.")
    elif cmd[1] == "bullet":
        try:
            print(f"bullet: {cmd[2]}={bullet[cmd[2]]}")
        except KeyError:
            print(f"Not recognized command: '{cmd[2]}'.")
        except IndexError:
            print("Missing argument in 'bullet'.")
    elif cmd[1] == "enemy":
        try:
            print(f"enemy: {cmd[2]}={enemy[cmd[2]]}")
        except KeyError:
            print(f"Not recognized command: '{cmd[2]}'.")
        except IndexError:
            print("Missing argument in 'enemy'.")
    else:
        print("Not recognized command.")


elif cmd[0] == "list":
    try:
        [print(k) for k in eval(cmd[1]).keys()]
    except NameError:
        print("Not recognized command.")
    except IndexError:
        print("Missing argument in 'list'.")


"""

if cmd[-1] == "clear_records":
    password = input("Password: ")
    if password == "3141":
        ans = input("ALERT: This will erase all the data. Do you want to continue? [y/n] ")
        if ans == "y":
            print("Okay. Cleaning the leaderboard.\nStarting the game.")
            break
        elif ans == "n":
            print("Operation aborted. Starting the game.")
            break
        else:
            print("Not recognized command. Please, try again. Or type 'cancel' to abort the operation")
    else:
        ans = input("Wrong password. Operation aborted.\nStarting the game.")
        break

"""