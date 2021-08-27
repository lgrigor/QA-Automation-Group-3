n = int(input("Введите число: "))


def prime(x):
    if n > 2:
        for i in range(2, n):
            while n % i == 0:
                return "не простое число."
            continue
        else:
            return "простое число"
    elif n == 1:
        return "не простое число."
    elif n == 2:
        return "простое число."


print(n, prime(n))