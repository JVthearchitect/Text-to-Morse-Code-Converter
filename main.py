from morse_code import morse_code_dict

def ConvertingMorse(given_input):
    given_input = given_input.lower()
    morse_output = ""
    for char in given_input:
        morse_output += morse_code_dict[char] + " "
    return morse_output


given_input = input("What would you like converted? ")
morse_output = ConvertingMorse(given_input)
print(morse_output)
