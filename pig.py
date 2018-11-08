import random
import sys


class Game:
    def __init__(self):
        pass

    turn_order = random.choice([0, 1])


    def get_player(self):
        if turn_order & 1:
            return player
        else:
            return computer
# play_turn(get_player())
   
    def play_turn(self):
        playing = self.get_player()
        if playing.is_computer:
            computer_turn(playing)
        else:
            player_turn(playing)

    def computer_turn(self, computer):
        computer.turn_score = 0
        while computer.turn_score < 20:
            roll = die.roll()
            if roll == 1:
                print(f"The computer rolled a pig!")
                return 0
            else:
                print(f"The computer rolled a {roll}")
                computer.turn_score += roll
        print(f"The computer gained a total of {computer.turn_score} points this round")
        return roll

    def player_turn(self):
        while not holding:
            player.turn

    def display_score():
        pass

    def ask_play_again():
        play = input('Would you like to play again? (y/n)').lower()
        if play == y:
            return True
        if play == n:
            print("Thanks for playing!")
            sys.exit()


class Player:
    def __init__(self, turn_score, total_score, is_computer=False):
        self.turn_score = turn_score
        self.total_score = total_score
        self.is_computer = is_computer

    def __eq__(self, other):
        return type(self) == type(other) and self.total_score == other.total_score and self.is_computer == other.is_computer

    def tally_turn_score(self):
        pass

    def tally_total_score(self):
        return self.total_score + self.turn_score


class Die:
    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        return random.choice(range(1,self.num_sides))


player = Player(0, 0)
computer = Player(0, 0, True) 

print(player.turn_score)

current_game = Game()