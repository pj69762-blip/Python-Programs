def common_elements(list1, list2):
    return list(set(list1) & set(list2))


if __name__ == "__main__":
    print(common_elements([1, 2, 3], [2, 3, 4]))