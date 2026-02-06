import random

class GuessGame:
    def __init__(self):
        self.number = random.randint(1, 10)

    def play(self):
        print(" Guess the Number Game")
        print("Guess a number between 1 and 10")

        while True:
                guess = int(input("Enter your guess: "))

                if guess == self.number:
                    print("Correct You win!!!!!!!!!!!!!")
                    break
                else:
                    print(" Wrong guess, try again!!!!!!!!")


def main():
    game = GuessGame()
    game.play()


if __name__ == "__main__":
    main()
