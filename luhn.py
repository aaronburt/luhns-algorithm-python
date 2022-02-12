def luhn(cardNumberInput): 
    cardResult = []

    for position in range(0, len(cardNumberInput)):
        if position % 2 == 0:
            doubledInput = int(cardNumberInput[position]) * 2
            if doubledInput >= 10:
                splitInput = [int(digit) for digit in str(doubledInput)]
                newCombinedInput = int(splitInput[0]) + int(splitInput[1])
                cardResult.append(newCombinedInput)
            else:
                cardResult.append(doubledInput)
        else:
            cardResult.append(int(cardNumberInput[position]))

    if sum(cardResult) % 10 == 0:
        return True
    else:
        return False

print(luhn(input("Card: ")))