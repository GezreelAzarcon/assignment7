#Program 1:
#Create a program that ask for a sentence as input.
#Display the number of words, vowels and consonants in the input 
#ex.
#input: Bahala kayo dyan
#output:
#words: 3
#vowels: 6
#consonants: 8

sentence = input('Input a sentence: ')
vow = 0
cons = 0
for i in sentence:
    if i == 'a' or i == 'i' or i == 'u' or i == 'e' or i == 'o' or i == 'A' or i == 'I' or i == 'U' or i == 'E' or i == 'O':
        vow += 1
    elif i == ' ':
        continue
    elif i == '!' or i == '@' or i == '#' or i == '$' or i == '%' or i == '^' or i == '&' or i == '*' or i == '(' or i == ')' or i == '_' or i == '+' or i == '-' or i == '=' or i == '`' or i == '[' or i == ']' or i == '{' or i == '}' or i == '|' or i == "'" or i == ':' or i == ';' or i == '"' or i == '<' or i == '>' or i == ',' or i == '.' or i == '/' or i == '?' or i == '~':
        continue
    elif i == '1' or i == '2' or i == '3' or i == '4' or i == '5' or i == '6' or i == '7' or i == '8' or i == '9' or i == '0':
        continue
    else:
        cons += 1
print(len(sentence.split()))
print(vow)
print(cons)

