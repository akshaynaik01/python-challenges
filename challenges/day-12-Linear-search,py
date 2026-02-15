def linear_search(data, key):
    for index, element in enumerate(data):
        if element == key:
            return index
    return -1


def main():
    n = int(input("Enter number of elements: "))
    data = []

    for _ in range(n):
        data.append(int(input()))

    key = int(input("Enter element to search: "))

    result = linear_search(data, key)

    if result != -1:
        print(f"Element found at index {result}")
    else:
        print("Element not found")


if __name__ == "__main__":
    main()
