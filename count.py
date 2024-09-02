def count_vowels(text):
    #define the vowels
    vowels = "AaEeIiOoUu"
    #set initial count
    count = 0
    
    #loop characters in the string
    for char in text:
    #if character is vowel, increase count by 1    
        if char in vowels:
            count += 1
    return count

print(count_vowels("aibohphobia"))