print("Hello COSC1104")

'''
Week 2 Excercises - Variables, Conditions, Loops
Class: COSC1104
'''

# Ex.1 - Vowel Counter
#Skills: Variables, String Manipulation, Loops, Conditions

# Take user input
user_string = input("Enter a Random String:")

# List of vowels
vowels = ['a', 'e', 'i', 'o', 'u']
# Count the vowels
vowel_counter = [0, 0, 0, 0, 0]

# Iterate through each character in the user input
for each_char in user_string:
    if each_char in vowels:
        # Find the index of the vowel located in the vowels list
        index = vowels.index(each_char)
        # Increment the counter located in vowel_counter
        vowel_counter[index] += 1

# Display counter
for i in range (len(vowels)):
    print(f"{vowels[i]} - {vowel_counter[i]}")        


#Ex.2 - Sum of Digits
#Skills: Variables, Type Casting, Loops, Condition