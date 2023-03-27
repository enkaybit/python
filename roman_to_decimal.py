def roman_to_decimal(roman_numeral):
    # Define a dictionary mapping each Roman numeral to its decimal value
    roman_to_decimal_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    # Initialize the decimal value to 0
    decimal_value = 0
    
    # Iterate through the characters of the Roman numeral string
    for i in range(len(roman_numeral)):
        # Get the decimal value of the current Roman numeral character
        current_value = roman_to_decimal_dict[roman_numeral[i]]
        
        # If the next character has a higher decimal value, subtract the current value
        if i < len(roman_numeral) - 1 and roman_to_decimal_dict[roman_numeral[i+1]] > current_value:
            decimal_value -= current_value
        # Otherwise, add the current value
        else:
            decimal_value += current_value
            
    return decimal_value

# Prompt the user to input a Roman numeral string
roman_numeral = input("Enter a Roman numeral string: ")

# Convert the Roman numeral string to its corresponding decimal value
decimal_value = roman_to_decimal(roman_numeral)

# Output the result
print("The decimal value of", roman_numeral, "is", decimal_value)
