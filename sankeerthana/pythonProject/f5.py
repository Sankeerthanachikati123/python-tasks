def split_string_into_words(input_string):
    """
    Split a string into words without using the split() method.

    Args:
        input_string (str): The input string to split.

    Returns:
        list: A list of words.
    """
    words = []
    current_word = ""
    for char in input_string:
        if char.isalpha():  # If the character is a letter
            current_word += char
        elif current_word:  # If we've accumulated a word and encounter a non-letter character
            words.append(current_word)
            current_word = ""
    if current_word:  # If there's a remaining word at the end of the string
        words.append(current_word)
    return words

# Example usage:
input_string = "Hello World, this is a test string!"
words = split_string_into_words(input_string)
print(words)  # Output: ['Hello', 'World', 'this', 'is', 'a', 'test', 'tring']