def reverse_string(text):
    #empty string for reversed word
    reversed_text = ""
    #loop each character in the string
    for char in text:
    #add each character infont of result
        reversed_text = char + reversed_text
    return reversed_text

result = reverse_string
print(result("aibohphobia"))