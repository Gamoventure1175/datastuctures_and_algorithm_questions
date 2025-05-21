# Seven different symbols represent Roman numerals with the following values:

# Symbol	Value
# I	        1
# V	        5
# X	        10
# L	        50
# C	        100
# D	        500
# M	        1000
# Roman numerals are formed by appending the conversions of decimal place values from highest to lowest. Converting a decimal place value into a Roman numeral has the following rules:

# If the value does not start with 4 or 9, select the symbol of the maximal value that can be subtracted from the input, append that symbol to the result, subtract its value, and convert the remainder to a Roman numeral.
# If the value starts with 4 or 9 use the subtractive form representing one symbol subtracted from the following symbol, for example, 4 is 1 (I) less than 5 (V): IV and 9 is 1 (I) less than 10 (X): IX. Only the following subtractive forms are used: 4 (IV), 9 (IX), 40 (XL), 90 (XC), 400 (CD) and 900 (CM).
# Only powers of 10 (I, X, C, M) can be appended consecutively at most 3 times to represent multiples of 10. You cannot append 5 (V), 50 (L), or 500 (D) multiple times. If you need to append a symbol 4 times use the subtractive form.
# Given an integer, convert it to a Roman numeral.


# Trying brute force method with whatever I understood
def roman_to_integers(num: int) -> str:
    """
    A function that takes a number and converts it to a roman numeral string and returns it
    """

    if not (0 < num < 4000):
        raise ValueError("Number should range from 1 to 3999")

    num_str = str(num)
    number_of_places = len(num_str)
    roman = ""

    r = {
        1: "I",
        4: "IV",
        5: "V",
        9: "IX",
        10: "X",
        40: "XL",
        50: "L",
        90: "XC",
        100: "C",
        400: "CD",
        500: "D",
        900: "CM",
        1000: "M",
    }

    place = 0
    if number_of_places == 4:
        place = 3
    elif number_of_places == 3:
        place = 2
    elif number_of_places == 2:
        place = 1
    elif number_of_places == 1:
        place = 0

    for i in range(0, len(num_str)):
        if place == 3:
            place -= 1
            roman += r[1000] * int(num_str[i])
        elif place == 2:
            place -= 1
            match num_str[i]:
                case "4":
                    roman += r[400]
                    continue
                case "9":
                    roman += r[900]
                    continue
                case "5":
                    roman += r[500]
                    continue
                case "1" | "2" | "3":
                    roman += r[100] * int(num_str[i])
                    continue
                case "6" | "7" | "8":
                    if num_str[i] == "6":
                        roman += r[500] + (r[100] * 1)
                        continue
                    elif num_str[i] == "7":
                        roman += r[500] + (r[100] * 2)
                        continue
                    else:
                        roman += r[500] + (r[100] * 3)
                        continue
                case "0":
                    continue
        elif place == 1:
            place -= 1
            match num_str[i]:
                case "4":
                    roman += r[40]
                    continue
                case "9":
                    roman += r[90]
                    continue
                case "5":
                    roman += r[50]
                    continue
                case "1" | "2" | "3":
                    roman += r[10] * int(num_str[i])
                    continue
                case "6" | "7" | "8":
                    if num_str[i] == "6":
                        roman += r[50] + (r[10] * 1)
                        continue
                    elif num_str[i] == "7":
                        roman += r[50] + (r[10] * 2)
                        continue
                    else:
                        roman += r[50] + (r[10] * 3)
                        continue
                case "0":
                    continue
        else:
            match num_str[i]:
                case "4":
                    roman += r[4]
                    continue
                case "9":
                    roman += r[9]
                    continue
                case "5":
                    roman += r[5]
                    continue
                case "1" | "2" | "3":
                    roman += r[1] * int(num_str[i])
                    continue
                case "6" | "7" | "8":
                    if num_str[i] ==  "6":
                        roman += r[5] + (r[1] * 1)
                        continue
                    elif num_str[i] ==  "7":
                        roman += r[5] + (r[1] * 2)
                        continue
                    else:
                        roman += r[5] + (r[1] * 3)
                        continue
                case "0":
                    continue

    return roman


print(roman_to_integers(2075))
