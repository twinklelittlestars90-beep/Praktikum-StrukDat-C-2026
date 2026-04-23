stack_URL = []

# Push
stack_URL.append('https://www.google.com')
stack_URL.append('https://www.google.com')
stack_URL.append('https://www.google.com')
print("Stack: ", stack_URL)

# Peek
topElement = stack_URL[-1]
print("Peek: ", topElement)

# Pop
poppedElement = stack_URL.pop()
print("Pop: ", poppedElement)

# Stack after Pop
print("Stack after Pop: ", stack_URL)

# isEmpty
isEmpty = not bool(stack_URL)
print("isEmpty: ", isEmpty)

# Size
print("Size: ",len(stack_URL))
