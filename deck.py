import random as rd


def deck_builder():
    '''Creates a deck of 52 cards with all colours and values'''
    values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]
    colour = ["Spades", "Clubs", "Hearts", "Diamonds"]
    deck = []
    # Loops through each colour and adds one of each value to that colour
    for col in colour:
        for val in values:
            deck.append([col, val])

    return deck


def shuffle_deck(deck):
    new_deck = [0 for i in range(len(deck))]
    length = len(deck)
    loop_check = True

    for element in deck:
        while loop_check:
            rand_index = rd.randint(0, length-1)
            if new_deck[rand_index] == 0:
                new_deck[rand_index] = element
                loop_check = False
            else:
                rand_index = rd.randint(0, length-1)
        loop_check = True

    return new_deck


def main():
    deck = deck_builder()
    deck = shuffle_deck(deck)
    for i in range(0, 5):
        print(f"{deck[i][1]} of {deck[i][0]}")


if __name__ == "__main__":
    main()
