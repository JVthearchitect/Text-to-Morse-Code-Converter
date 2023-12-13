from morse_code import morse_code_dict

def ConvertingMorse(given_input):
    given_input = given_input.lower()
    morse_output = ""
    for char in given_input:
        morse_output += morse_code_dict[char] + " "
    return morse_output

# library or dictionary of morse code symbols and the alphabet

# convert each letter and space to morse code

# replace() letters with the morse code equivalent

#have exceptions to push past the use of symbols that aren't in the morse code

#change all letter inputs into lower case

given_input = input("What would you like converted? ")
morse_output = ConvertingMorse(given_input)
print(morse_output)


#convert input into morse code - maybe use a Class to make this happen (or is it called a function?)