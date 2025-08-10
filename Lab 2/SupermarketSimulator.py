#
# A Supermarket simulation
#

"""
import sys
sys.path.append("..")

from LinearStructures import Queue
"""

import random

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        if not self.isEmpty():
            return self.items.pop()

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

# A Customer has an ID and a random number of items
class Customer:
    def __init__(self, number, max_items):
        self.id = number
        # generate a random number of items between 1 and max_items
        self.items = random.randint(1, max_items)


# A cash desk has and ID and a queue of clients
# A new client is dequeued only after all the items of the current customer are checked out
class Cashdesk:
    def __init__(self, number):
        self.id = number
        self.queue = Queue()
        self.tot_customers_served = 0
        self.current_customer = None

    # Method to enqueue a new Customer c
    def addCustomer(self, c):
        self.queue.enqueue(c)

    # Method for check out
    #
    # if current_customer != None check the number of items:
    #     if it is zero: print a message with the cash desk and Customer ids, reset current_customer to None
    #                    and increase the tot_customers_served counter
    #     else: decrease the number of items of current_customer by 1
    #
    # if current_customer = None and queue not empty, then dequeue a Customer that becomes the current_customer
    #
    # Example of message: "Cash desk 1 served Customer number 2"
    
    def checkOut(self):
        if self.current_customer is not None:
            if self.current_customer.items == 0:
                print("Cash desk", self.id, "served Customer number", self.current_customer.id)
                self.tot_customers_served += 1
                self.current_customer = None
            else:
                self.current_customer.items -= 1
        elif not self.queue.isEmpty():
            self.current_customer = self.queue.dequeue()


# A Supermarket has a number of check desks specified by user
class Supermarket:
    def __init__(self, num_checdesks):
        self.cashdesks_list = [Cashdesk(i) for i in range(1, num_checdesks + 1)]

    # Return True if all the check desks are empty, False otherwise
    def isEmpty(self):
        for cd in self.cashdesks_list:
            # we need to check if the queue is empty and if there are no current client
            if not cd.queue.isEmpty() or cd.current_customer:
                return False
        return True

    # Add a new Customer to the check desk with the shortest queue
    def newCustomer(self, new_customer):
        min_cdesk = self.cashdesks_list[0]
        min_len = min_cdesk.queue.size()

        # Alternative using index
        # for i in range(1, len(self.cashdesks_list)):
        #     current_cd = self.cashdesks_list[i]
        #     if current_cd.queue.size() < min_len:
        #         min_len = current_cd.queue.size()
        #         min_cdesk = current_cd

        for cdesk in self.cashdesks_list:
            if cdesk.queue.size() < min_len:
                min_len = cdesk.queue.size()
                min_cdesk = cdesk

        min_cdesk.addCustomer(new_customer)

    # Execute the method checkOut for each check desk
    def run(self):
        for cdesk in self.cashdesks_list:
            cdesk.checkOut()

    # Print the total number of customers served by each check desks
    #
    # E.g.: Cash deck 1 served 2426 clients
    #       Cash deck 2 served 2361 clients
    #       ...
    #
    def printRecap(self):
        for cdesk in self.cashdesks_list:
            print("Cash deck", cdesk.id, "served", cdesk.tot_customers_served, "clients")


# Test code
if __name__ == "__main__":
    num_checkdesks = 5  # number of check desks
    max_num_items = 20  # max number of items for each Customer
    num_customers = 10000  # total number of customers

    # Create an object Supermarket
    mySupermarket = Supermarket(num_checkdesks)
    # Create a list of Customer objects
    customers_list = [Customer(i, max_num_items) for i in range(num_customers, 0, -1)]

    #
    # Loop until all the customers are entered and served (i.e. both customer_list and all the queue are empty
    # A new Customer enters in the Supermarket with probability of 30% (use random function)
    # The function run is always called at each iteration
    #
    while len(customers_list) > 0 or not mySupermarket.isEmpty():
        if len(customers_list) > 0 and random.random() > 0.7: # The probability is just to slow down a bit the program
            c = customers_list.pop()
            mySupermarket.newCustomer(c)
        mySupermarket.run()

    # Print the total number of customers served by each check desk
    mySupermarket.printRecap()
