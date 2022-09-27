import random as rd


def deck_builder():
    '''Creates a deck of 52 cards with all colours and values'''
    values = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]
    colour = ["Spades", "Clubs", "Hearts", "Diamonds"]
    deck = []
    # Loops through each colour and adds one of each value to that colour
    for col in colour:
        for val in values:
            deck.append([col, val])

    return deck


def shuffle_deck(deck):
    '''Durstenfeld version of Fisher-Yates shuffle
    ref: https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle'''
    length = len(deck)
    roll = length - 1

    for i in range(0, length):
        index_from = rd.randint(0, roll)
        deck[index_from], deck[roll] = deck[roll], deck[index_from]
        roll -= 1

    return deck


def main():
    deck = deck_builder()
    deck = shuffle_deck(deck)

    for i in range(0, 5):
        print(f"{deck[i][1]} of {deck[i][0]}")


if __name__ == "__main__":
    main()
