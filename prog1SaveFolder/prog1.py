#Program 1:
#Create a program that ask for a sentence as input.
#Display the number of words, vowels and consonants in the input 
#ex.
#input: Bahala kayo dyan
#output:
#words: 3
#vowels: 6
#consonants: 8

sen = input('Input: ')
vow = 0
cons = 0
for i in sen:
    if i == 'a' or i == 'i' or i == 'u' or i == 'e' or i == 'o' or i == 'A' or i == 'I' or i == 'U' or i == 'E' or i == 'O':
        vow += 1
    elif i == ' ':
        continue
    else:
        cons += 1
print(len(sen.split()))
print(vow)
print(cons)

