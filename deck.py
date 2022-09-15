import random as rd


def deck_builder():
    '''Creates a deck of 52 cards with all colours and values'''
    values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]
    colour = ["Spades", "Clubs", "Hearts", "Diamonds"]
    deck = []

    for col in colour:
        for val in values:
            deck.append([col, val])

    return deck


def main():
    deck = deck_builder()
    rd.shuffle(deck)
    for i in range(0, 5):
        print(f"{deck[i][1]} of {deck[i][0]}")


if __name__ == "__main__":
    main()
