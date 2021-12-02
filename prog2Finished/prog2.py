#Program 2: Password validator
#Create a program that check if password is valid
#The password is valid if all criteria are met:
#a. Greater than 15 letters
#b. Have at least one capital letter
#c. Have at least one number
#d. Have at least one special char (!@#$%^&*()_+ etc)
#ex.
#input: P@ssw0rd+P@ssw0rd
#ouput: Valid
def passvalidator():
    pas = input('Password: ')
    upper = 0
    lower = 0
    digit = 0
    special = 0
    for i in pas:
        if i == 'A' or i == 'B' or i == 'C' or i == 'D' or i == 'E' or i == 'F' or i == 'G' or i == 'H' or i == 'I' or i == 'J' or i == 'K' or i == 'L' or i == 'M' or i == 'N' or i == 'O' or i == 'P' or i == 'Q' or i == 'R' or i == 'S' or i == 'T' or i == 'U' or i == 'V' or i == 'W' or i == 'X' or i == 'Y' or i == 'Z':
            upper = 1
        if i == 'a' or i == 'b' or i == 'c' or i == 'd' or i == 'e' or i == 'f' or i == 'g' or i == 'h' or i == 'i' or i == 'j' or i == 'k' or i == 'l' or i == 'm' or i == 'n' or i == 'o' or i == 'p' or i == 'q' or i == 'r' or i == 's' or i == 't' or i == 'u' or i == 'v' or i == 'w' or i == 'x' or i == 'y' or i == 'z':
            lower = 1
        elif i == '1' or i == '2' or i == '3' or i == '4' or i == '5' or i == '6' or i == '7' or i == '8' or i == '9' or i == '0':
            digit = 1
        elif i == '!' or i == '@' or i == '#' or i == '$' or i == '%' or i == '^' or i == '&' or i == '*' or i == '(' or i == ')' or i == '_' or i == '+' or i == '-' or i == '=' or i == '`' or i == '[' or i == ']' or i == '{' or i == '}' or i == '|' or i == "'" or i == ':' or i == ';' or i == '"' or i == '<' or i == '>' or i == ',' or i == '.' or i == '/' or i == '?' or i == '~':
            special = 1
    if len(pas) <= 15:
        length = 0
    elif len(pas) > 15:
        length = 1
    final = (upper + lower + digit + special + length)
    if final == 5:
        print()
        print(f'Input: {pas}')
        print('Output: Valid')
        print()
    else:
        print()
        print(f'Input: {pas}')
        print('Output: Invalid')
        if upper == 0:
            print()
            print('Write atleast one uppercase character!')
            print()
        elif lower == 0:
            print()
            print('Write atleast one lowercase character!')
            print()
        elif digit == 0:
            print()
            print('Write atleast one digit character')
            print()
        elif special == 0:
            print()
            print('Write atleast one special character!')
            print()
        elif length == 0:
            print()
            print('Write more than 15 characters!')
            print()
   
passvalidator()


