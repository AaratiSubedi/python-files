def longest_substring_length(input_string):
    # Initialize variables
    max_length = 0
    start = 0
    char_index_map = {}

    # Iterate through the string
    for i, char in enumerate(input_string):
        # If the character is already in the map and its index is after the start of the current substring
        if char in char_index_map and char_index_map[char] >= start:
            start = char_index_map[char] + 1

        # Update the index of the current character
        char_index_map[char] = i

        # Calculate the length of the current substring
        current_length = i - start + 1

        # Update the maximum length
        max_length = max(max_length, current_length)

    return max_length


input_str = "abcabcbb"
print(longest_substring_length(input_str))  
