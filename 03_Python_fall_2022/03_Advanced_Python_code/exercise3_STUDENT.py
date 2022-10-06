def products(*numbers):
    product = 1
    for number in numbers:
        product *= number
    return product


def printString(sentence):
    print(sentence)
