def is_palindrome(number):
    return str(number) == str(number)[::-1]


if __name__ == "__main__":
    print(is_palindrome(121))