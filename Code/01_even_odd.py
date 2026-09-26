def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


if __name__ == "__main__":
    print(check_even_odd(10))