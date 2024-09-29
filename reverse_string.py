
#reverse string using loop

def reverse_string_approach_1(input_string):
    reversed_str=''
    
    for char in input_string:
        reversed_str=char + reversed_str
    return reversed_str
    
string='kaskikot'
reversed_str=reverse_string_approach_1(string)
print(reversed_str)
        













