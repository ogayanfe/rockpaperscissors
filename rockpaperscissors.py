import random


class RockPaperScissors:
    def __init__(self):
        self.options = ['rock', 'paper', 'scissors']
        self.rating = 0

    def check_win(self, user_choice, comp_choice):
        if user_choice == 'rock' and comp_choice == 'paper':
            print('Sorry, but the computer chose paper')
        elif user_choice == 'paper' and comp_choice == 'scissors':
            print('Sorry, but the computer chose scissors')
        elif user_choice == 'scissors' and comp_choice == 'rock':
            print('Sorry, but the computer chose rock')
        elif user_choice == comp_choice:
            print(f'There is a draw {comp_choice}')
            self.rating += 50
        else:
            print(f'Well done. The computer chose {comp_choice} and failed')
            self.rating += 100

    def get_rating(self, name):
        with open('rating.txt', 'r') as rate:
            for line in rate:
                if name in line:
                    self.rating = int(line.split()[1])  # Gets the integer of the second element in the list
                    break
                else:
                    self.rating = 0

    def impractical_game(self, prompt, user_choice, comp_choice):
        if user_choice == comp_choice:
            print(f'There is a draw {comp_choice}')
            self.rating += 50
        else:
            new_list = prompt[prompt.index(user_choice) + 1:] + prompt[:prompt.index(user_choice)]
            win_list = new_list[len(new_list) // 2:]
            if comp_choice in win_list:
                print(f'Well done. The computer chose {comp_choice} and failed')
                self.rating += 100
            else:
                print(f'Sorry, but the computer chose {comp_choice}')

    def main(self, name):
        self.get_rating(name)
        prompt = input().split(',')
        print("Okay, let's start")
        while True:
            user_choice = input()
            if user_choice not in self.options and user_choice != '!exit' and user_choice != '!rating' \
                    and user_choice not in prompt:
                print('Invalid input')
            elif user_choice == '!exit':
                print('Bye!')
                break
            elif user_choice == '!rating':
                print('Your rating:', self.rating)
            else:
                if len(prompt) == 1:
                    comp_choice = random.choice(self.options)
                    self.check_win(user_choice, comp_choice)
                else:
                    comp_choice = random.choice(prompt)
                    self.impractical_game(prompt, user_choice, comp_choice)


if __name__ == '__main__':
    game = RockPaperScissors()
    user = input('Enter your name: ')
    print('Hello,', user)
    game.main(user)
