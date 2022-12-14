import random as rd


# Rolls a random number from 0-5 and adds 1 to that index in dice_array
def diceRoll(max_rolls, dice_array):
    for i in range(0, max_rolls):
        dice_array[rd.randint(0, 5)] += 1


# Calculates ratio between max and min roll
def rollDifference(dice_array):
    maximum = max(dice_array)
    minimum = min(dice_array)

    if maximum == 0 or minimum == 0:
        return 100
    else:
        return ((maximum-minimum)/maximum) * 100


def main():
    dice_rolls = [0, 0, 0, 0, 0, 0]
    roll_amount = 10
    # Does 20 tests doubling roll_amount each time
    for tests in range(0, 20):
        diceRoll(roll_amount, dice_rolls)
        difference = rollDifference(dice_rolls)
        difference = float("{0:.2f}".format(difference))

        print(f"For {roll_amount}, the difference is: {difference}%")

        roll_amount *= 2
        dice_rolls = [0 for i in range(0, 6)]


if __name__ == "__main__":
    main()
