
from game_logic import play_game




if __name__ == "__main__":
    while True:
        play_game()
        new_game_or_exit = input("Do you want to play again? (y/n): ")
        if new_game_or_exit == "n":
            break
