# A program that calculates how many boxes of candles that are
# necessary to purchase for a given birthday. Candles decrement by current age
def main():
    candle_box = [0, 0]

    for i in range(1, 101):
        if i > candle_box[1]:
            # Taking advantage of floor division rounding down
            # using the negative number and then negate it back to positive
            # to effectively round up.
            # Removing the left over candles to see how many boxes needed
            # to satisfy current birthday
            box_amount = -(-(i - candle_box[1]) // 24)
            candle_box[0] += box_amount
            candle_box[1] += (box_amount * 24)

            print(f"Before birthday {i}, buy {box_amount} box(es)")

            candle_box[1] -= i
        else:
            candle_box[1] -= i

    print(f"Total number of boxes: {candle_box[0]}, ", end="")
    print(f"Remaining candles: {candle_box[1]}")


if __name__ == "__main__":
    main()
