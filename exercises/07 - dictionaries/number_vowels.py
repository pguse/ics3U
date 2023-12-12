f = open("emma.txt", 'r')

data = f.read()

# MODIFY THE CODE BELOW
# TO ADD THE NUMBER OF VOWELS a,e,i,o,u

vowels = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}

for ch in data:
    if ch.lower() == 'a':
        vowels['a'] += 1

print(f"Number of a's: {vowels['a']}")

f.close()