def count_vowels(input_string):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in input_string:
        if char in vowels:
            count += 1
    return count

input = "Shequal project"
vowel_count = count_vowels(input)
print(" Total number of vowels are:", vowel_count)  
