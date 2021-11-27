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
import sys

pas = input('Password: ')
upper = 0
digit = 0
speChar = 0
limit = 0
for i in pas:
    if len(i) < 16:
        limit = 1
    elif i.upper():
        upper += 1
    elif i.isdigit():
        digit += 1
    if i == '!' or i == '@' or i == '#' or i == '$' or i == '%' or i == '^' or i == '&' or i == '*' or i == '(' or i == ')' or i == '_' or i == '+' or i == '-' or i == '=' or i == '`' or i == '[' or i == ']' or i == '{' or i == '}' or i == '|' or i == "'" or i == ':' or i == ';' or i == '"' or i == '<' or i == '>' or i == ',' or i == '.' or i == '/' or i == '?' or i == '~':
        speChar += 1
if limit == 1:
    print('Invalid')
    sys.exit
    if upper < 1:
        print('Invalid')
        sys.exit
        if digit < 1:
            print('Invalid')
            sys.exit
            if speChar < 1:
                print('Invalid')
                sys.exit
elif limit == 0:
    print('Valid')
    sys.exit
    if upper >= 1:
        print('Valid')
        sys.exit
        if digit >= 1:
            print('Valid')
            sys.exit
            if speChar >= 1:
                print('Valid')
                sys.exit
        




