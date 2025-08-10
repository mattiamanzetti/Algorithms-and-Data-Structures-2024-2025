class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


class OrderedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count = count + 1
            current = current.getNext()

        return count

    def index(self, index):
        counter = 0
        current = self.head
        while current is not None:
            if counter == index:
                return current.getData()
            else:
                counter += 1
                current = current.getNext()

    def search(self, item):
        current = self.head

        while current is not None:
            if current.getData() == item:
                return True
            else:
                if current.getData() > item:
                    return False
                else:
                    current = current.getNext()

        return False

    def add(self, item):
        current = self.head
        previous = None
        stop = False
        while current is not None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = Node(item)
        if previous is None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

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



