# Create the first sentance
x = "There are %d types of people." % 10

# Store a single word variable
binary = "binary"

# Store another single word variable
do_not = "don't"

# Create a second sentence with the top two variables interpolated
y = "Those who know %s and those who %s." % (binary, do_not)

# Print out the first sentence
print x
# Print out the next sentence
print y

# Repeat x
print "I said: %r." % x

# Repeat y
print "I also said: '%s'." % y

# Create a variable that is False
hilarious = False
# Print out a sentence as well as the value of the hilarious variable
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious 

# Create two more sentence
w = "This is the left side of..."
e = "a string with a right side."

# Concatinate and print out the the previous two variables
print w + e
