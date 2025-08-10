class Node:
    def __init__(self, initData):
        self.data = initData
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newData):
        self.data = newData

    def setNext(self, newNext):
        self.next = newNext


class UnorderedList:

    def __init__(self):
        self.head = None

    def index(self, index):
        counter = 0
        current = self.head
        while current is not None:
            if counter == index:
                return current.getData()
            else:
                counter += 1
                current = current.getNext()

    def isEmpty(self):
        return self.head is None

    def add(self, item):
        temp = Node(item) # Creates a new node and places the item that we want to add as its data
        temp.setNext(self.head) # Changes the next reference of the new node to refer to the old first node of the linked list
        self.head = temp # Sets the head of the linked list

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count = count + 1
            current = current.getNext()
        return count

    def search(self, item):
        current = self.head

        while current is not None:
            if current.getData() == item:
                return True
            else:
                current = current.getNext()
        return False

    def remove(self, item):
        current = self.head
        previous = None
        found = False

        while current is not None and not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if found:
            if previous is None:
                self.head = current.getNext()
            else:
                previous.setNext(current.getNext())
        else:
            print("Element not present")

    def pop(self, index=None):
        if index is None:
            return self.__pop()
        else:
            return self.__popindex(index)

    def __pop(self):
        current = self.head

        if current is None:
            return "The list is empty"

        previous = None
        end = False

        while not end:
            if current.getNext() is None:
                end = True
            else:
                previous = current
                current = current.getNext()

        if previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(None)

        return current.getData()

    def __popindex(self, index):
        current = self.head

        if current is None:
            return "The list is empty"

        previous = None
        counter = 0
        found = False

        data = None

        while current is not None and not found:
            if counter == index:
                found = True
                data = current.getData()
            else:
                previous = current
                current = current.getNext()
                counter += 1

        if found:
            if previous is None:
                self.head = current.getNext()
            else:
                previous.setNext(current.getNext())
        else:
            print("Index too big")

        return data


if __name__ == "__main__":
    import random

    myLList = UnorderedList()
    for i in range(100):
        num = random.randint(0, 100)
        myLList.add(num)

    print(myLList.index(5))
    print(myLList.size())
    print(myLList.pop())
    myLList.remove(5)
    print(myLList.size())
    print(myLList.search(1))
