import random as rd


def pronoun():
    '''Returns one out of five pronouns'''
    pronouns = ["I", "You", "It", "We", "They"]
    return pronouns[rd.randint(0, 4)]


def verb():
    '''Returns one out of five verbs'''
    verbs = ["will see", "will eat", "will buy", "will touch", "will throw"]
    return verbs[rd.randint(0, 4)]


def noun():
    '''Returns one out of five nouns'''
    nouns = ["a house", "a car", "a pancake", "a cat", "a rock"]
    return nouns[rd.randint(0, 4)]


def main():
    for i in range(0, 10):
        print(f"{pronoun()} {verb()} {noun()}")


if __name__ == "__main__":
    main()
