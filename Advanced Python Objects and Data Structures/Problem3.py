s = "hello how are you mary, are you feeling okay?"

# Check if every letter is lowercase
is_lowercase = all(char.islower() for char in s if char.isalpha())

# Print the result
print("Every letter is lowercase:", is_lowercase)
