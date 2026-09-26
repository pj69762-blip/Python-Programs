def find_duplicates(numbers):
    duplicates = []

    for number in numbers:
        if numbers.count(number) > 1 and number not in duplicates:
            duplicates.append(number)

    return duplicates


if __name__ == "__main__":
    print(find_duplicates([1, 2, 2, 3, 4, 4]))