# Ask user for their name.

name = input("What is your name?: ")

# Ask the user for their age.

age = input("How old are you?: ")

# Ask user for their city.

city = input("What city do you live in?: ")

# Ask user what they enjoy.

love = input("What do you love to do?: ")

# Create output text.
string = "Your name is {0} and you are {1} years old. You live in {2} and you love {3}"
#output = "Hello " + name + ", nice to meet you. \nI see you are "+age+" years old and live in "+ city + " and also love "+love+"."
output = string.format(name,age,city,love)
# print output to screen.
print(output)
