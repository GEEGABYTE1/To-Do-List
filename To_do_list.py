from datetime import datetime
import time

class Node:
    def __init__(self, value, link=None):
        self.value = value 
        self.link = link 

    def get_value(self):
        return self.value 

    def get_link(self):
        return self.link 

    def set_link(self, new_link):
        self.link = new_link 

class Queue:
    def __init__(self, limit=None):
        self.head_node = None 
        self.tail_node = None 
        self.limit = limit 
        self.size = 0
    def is_empty(self):
        if self.size == 0:
            return True 

    def has_space(self):
        if self.limit == None:
            return True 
        else:
            if self.limit > self.size:
                return True 

    def peek(self):
        if not self.is_empty():
            return self.head_node.get_value()
        else:
            print("The queue is full")
    
    def enqueue(self, new_value):
        if self.has_space() == True:
            new_node = Node(new_value)
            if self.is_empty():
                self.head_node = new_node 
                self.tail_node = new_node 
            else:
                self.tail_node.set_link(new_node)
                self.tail_node = new_node 
            self.size += 1
        else:
            print('The queue is full')
    
    def dequeue(self):
        if not self.is_empty():
            item_to_remove = self.head_node 
            if self.size == 1:
                self.head_node = None 
                self.tail_node = None 
            else:
                self.head_node = item_to_remove.get_link()
            self.size -= 1
            return item_to_remove.get_value()
        else:
            print("The queue is empty")
class LinkedList:
    def __init__(self, value=None):
        self.head_node = Node(value)

    def get_head_node(self):
        return self.head_node 
    
    def insert_node(self, new_value):
        new_node = Node(new_value)
        current_node = self.get_head_node()
        while current_node:
            if current_node.get_link() == None:
                current_node.set_link(new_node)
                current_node = new_node 
                break 
            else:
                current_node = current_node.get_link()
    
    def stringify_list(self):
        string = ""
        current_node = self.get_head_node()
        while current_node:
            if current_node.get_value() != None:
                string += str(current_node.get_value()) + '\n'
            current_node = current_node.get_link()
        return string

    def remove_node(self, value):
        current_node = self.get_head_node()
        if current_node.get_value() == value:
            self.head_node = current_node.get_link()
        else:
            while current_node:
                next_node = current_node.get_link()
                if next_node.get_value() == value:
                    current_node.set_link(next_node.get_link())
                    current_node = None 
                else:
                    current_node = next_node

    

playing = True 
print("Made by Jaival Patel")
time.sleep(1.2)
name = input("Please enter your name: ")
print("Welcome {name}, here is your to-do list for today!".format(name=name))
time.sleep(1)
print("type /add to add an event")
print("type /complete if you have completed the event")
updated_date = datetime.strftime(datetime.now(), " %c ")
print("The current date and time is: " + updated_date)
print("\n")
q = Queue()
ll = LinkedList()


while True:
    prompt = input() 
    
    if prompt == "/add":
        occasion = input("Please type in the event: ")
        q.enqueue(occasion + " | Time Added: " + str(updated_date))
        ll.insert_node(occasion + " | Time Added: " + str(updated_date))
        

    elif prompt == "/complete":
        ll.remove_node(q.peek())
        q.dequeue()
        if q.size == 0:
            print("You have no events that take place today!")
        else:
            print(ll.stringify_list())
    
    elif prompt == "":
        pass
    
    else:
        print("The command is not available!")
    
    print(ll.stringify_list())


