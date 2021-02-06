import random
test = input("People, seperated by a comma and a space: ")
testl = test.split(", ")
print("Random Person is: " + random.choice(testl))
