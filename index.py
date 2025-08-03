def reverse_words(input_string):
    words = input_string.split()
    reversed_words = words[::-1]
    reversed_string = ' '.join(reversed_words)
    return reversed_string


def main():
    input_string = input("Please enter a long string containing multiple words: ")
    reversed_string = reverse_words(input_string)
    print("Here is the same string, except with the words in backwards order:")
    print(reversed_string)

if __name__ == "__main__":
    main()
