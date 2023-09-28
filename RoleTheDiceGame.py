import random

def roll_dice():
    return random.randint(1, 6)

def main():
    input("Press Enter to roll the dice...")

    dice1 = roll_dice()
    dice2 = roll_dice()

    print(f"You rolled a {dice1} and a {dice2}")

    if dice1 == dice2:
        print("Congratulations! You won!")
    else:
        print("Sorry, you lost!")

if __name__ == "__main__":
    main()
