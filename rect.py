#Topic 2 Code mentioned below

# Initialized Rectangle Class 
class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        # Yielding the length and width in the specified format
        yield {'Length': self.length}
        yield {'Width': self.width}

if __name__ == "__main__":
    rect1 = Rectangle(50, 7)
    
    for dim in rect1:
        print(dim)
