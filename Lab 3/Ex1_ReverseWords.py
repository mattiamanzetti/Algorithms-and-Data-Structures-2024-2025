# Reverse each word in a string using a Stack
# Words must stay in the same initial position
# E.g., "Algorithm and Data Structures" will become "mhtiroglA dna ataD serutcurtS"

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)



# Reverse each words of a string maintaining their position
def reverserWords(input_string):
    st = Stack()
    revString = ""

    # Split the string in words
    words = input_string.split()

    for word in words:

        # Traverse given word and push all characters into the stack
        for character in word:
            st.push(character)

        # Pop all the element in the stack
        while not st.isEmpty():
            revString += st.pop()

        # add a space between words
        revString += " "

    return revString


# Test Code
if __name__ == "__main__":
    myString = "Algorithm and Data Structures"
    print(reverserWords(myString))