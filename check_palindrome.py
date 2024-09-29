def is_palindrome(input_string):
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_string = ''.join(char.lower() for char in input_string if char.isalnum())
    # Compare cleaned string with its reverse
    return cleaned_string == cleaned_string[::-1]

string_input = "madam"
print(is_palindrome(string_input))  
