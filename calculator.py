def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mult(x, y):
    return x * y


def div(x, y):
    return x / y


def avg(numbers: list) -> float:
    total = 0
    for i in numbers:
        total += i
    return total/len(numbers)


print(avg([1, 2, 4]))
