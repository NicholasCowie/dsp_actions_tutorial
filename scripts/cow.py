from cowpy import cow

# Create a Cow
cheese = cow.Moose()

# Get a cowsay message by milking the cow
msg = cheese.milk("My witty mesage")

# do something with the message
print(msg)

# Create a Cow with a thought bubble
cheese = cow.Moose(thoughts=True)
msg = cheese.milk("My witty mesage, with thought")
print(msg)