from decimal import Decimal

def decimal():
    list = []

    i = Decimal(2.0)

    while i < 6:
        list.append(i)
        i += Decimal(0.5)

    print(list)

decimal()
