# Python equivalent of the Java MyCollectionsPunto class

def main():
    list_strings = ["piano", "trompeta", "guitarra", "bateria", "trombon", "esternoscopio"]
    print(list_strings) #first in, first out

    # Reverse the list (last in, first out)
    list_strings.reverse()
    print(list_strings)

    # Sort alphabetically
    list_strings.sort()
    print(list_strings)

    # Sort in reverse alphabetical order
    list_strings.sort(reverse=True)
    print(list_strings)

    # Rotate the list by 2 (last 2 elements go to the front)
    n = 2
    list_strings = list_strings[-n:] + list_strings[:-n]
    print(list_strings)

    # Get the minimum value (alphabetically first)
    min_val = min(list_strings)
    print(min_val)

    # Swap second and third elements (index 1 and 2)
    list_strings[1], list_strings[2] = list_strings[2], list_strings[1]
    print("swap:", list_strings)

    # Working with a list of doubles
    list_double = [1.4, 0.5, 2.5, 1.41]

    # Reverse list
    list_double.reverse()
    print(list_double)

    # Sort ascending
    list_double.sort()
    print(list_double)

    # Sort descending
    list_double.sort(reverse=True)
    print(list_double)

    # Get the maximum value
    max_val = max(list_double)
    print(max_val)


if __name__ == "__main__":
    main()
