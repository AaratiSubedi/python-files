def string_anagrams(string1, string2):
    # Removing non-alphanumeric characters and convert to lowercase
    cleaned_str1 = ''.join(char.lower() for char in string1 if char.isalnum())
    cleaned_str2 = ''.join(char.lower() for char in string2 if char.isalnum())
    
    return sorted(cleaned_str1) == sorted(cleaned_str2)

str1 = "listen"
str2 = "silent"
print(string_anagrams(str1, str2)) 


# By  take input from user

def string_anagrams(string1, string2):
 
    cleaned_str1 = ''.join(char.lower() for char in string1 if char.isalnum())
    cleaned_str2 = ''.join(char.lower() for char in string2 if char.isalnum())
    
    return sorted(cleaned_str1) == sorted(cleaned_str2)

def check_anagrams():
    str1 = input("Enter the first string: ")
    str2 = input("Enter the second string: ")

    if string_anagrams(str1, str2):
        print("The strings are anagrams of each other.")
    else:
        print("The strings are not anagrams of each other.")

check_anagrams()

