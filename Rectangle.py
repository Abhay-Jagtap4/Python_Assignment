class Rectangle:
    def __init__(self, length: int, width: int):
        # Initialize the length and width attributes
        self.length = length
        self.width = width

    def __iter__(self):
        # Define the iteration behavior
        yield {'length': self.length}
        yield {'width': self.width}

# Example:
rect = Rectangle(5, 10)

# Iterating over the instance
for item in rect:
    print(item)
