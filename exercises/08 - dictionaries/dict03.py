# Open the text file and assign a variable name
f = open("provinces.csv", 'r')
# Create an empty list
questions = []
# Read the data line-by-line from the file
# and append it to your list
for line in f:
    questions.append(line)

print(questions)

# Parsing Examples
# print("Ontario,Toronto\n".split(','))   # split string into list of strings
# print(questions[0].split(','))          # split string into list of strings
# print(questions[0].split(',')[0])       # element 0 of a list - a string
# print(questions[0].split(',')[1])       # element 1 of a list - a string
# print(questions[0].split(',')[1][:-1])  # string splice minus last character

# Using the examples above, ask the user
# the capital of Ontario and respond according
# to their answer


# Create a quiz that asks 8 random questions and
# keeps track of the number of correct answers


# Challenge - modify your quiz so that it does not
# repeat any questions


# Close the file
f.close()