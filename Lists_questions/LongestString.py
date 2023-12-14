# List: Find Longest String ( ** Interview Question)
# Write a Python function called find_longest_string that takes a list of strings as an input and returns the longest string in the list. The function should iterate through each string in the list, check its length, and keep track of the longest string seen so far. Once it has looped through all the strings, the function should return the longest string found.

# Example:

# string_list = ['apple', 'banana', 'kiwi', 'pear']
# longest = find_longest_string(string_list)
# print(longest)  # expected output: 'banana'


def find_longest_string(string):
    if string:
        longest_str = string[0]
    
        for i in range(1, len(string)):
            longest_str = string[i] if len(string[i]) > len(longest_str) else longest_str
    
        return longest_str
        
    return ""

string_list = ['apple', 'banana', 'kiwi', 'pear']
longest = find_longest_string(string_list)
print(longest)  


"""
    EXPECTED OUTPUT:
    ----------------
    banana
    
"""