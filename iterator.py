class CustomRange:
    def __init__(self, begin, end):
        self.begin = begin
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.begin >= self.end:
            raise StopIteration
        else:
            current = self.begin
            self.begin += 10
            return current


# Use custom range iterator
my_range = CustomRange(0, 101)
# This should print numbers increasing with 10
for number in my_range:
    print(number)

# An equivalent way to print the same
for number in range(0, 101, 10):
    print(number)
